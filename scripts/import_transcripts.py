#!/usr/bin/env python3
"""Import transcript Markdown files into the account-first Obsidian structure."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import yaml


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE = re.compile(r"^\[\[(.*?)(?:\|.*?)?\]\]$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Directory containing transcript Markdown files")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--refresh-youtube", action="store_true", help="Resolve channel names with YouTube oEmbed")
    return parser.parse_args()


def parse_document(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"missing YAML frontmatter: {path}")
    metadata = yaml.safe_load(match.group(1)) or {}
    return metadata, text[match.end() :]


def unwrap_wikilink(value: object) -> str:
    text = str(value).strip()
    match = WIKILINK_RE.match(text)
    return match.group(1) if match else text


def source_url(metadata: dict) -> str:
    value = metadata.get("youtube_url") or metadata.get("source")
    if not isinstance(value, str) or not value.startswith("http"):
        raise ValueError("missing source URL")
    return value


def youtube_id(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc == "youtu.be":
        return parsed.path.strip("/")
    video_id = urllib.parse.parse_qs(parsed.query).get("v", [""])[0]
    if not video_id:
        raise ValueError(f"cannot extract YouTube video id from {url}")
    return video_id


def fallback_account(metadata: dict) -> str:
    authors = metadata.get("author") or []
    if isinstance(authors, str):
        authors = [authors]
    names = [unwrap_wikilink(author) for author in authors]
    if not names:
        raise ValueError("missing account/author metadata")
    return ", ".join(names)


def fetch_oembed(url: str) -> tuple[str, str]:
    endpoint = "https://www.youtube.com/oembed?" + urllib.parse.urlencode({"url": url, "format": "json"})
    with urllib.request.urlopen(endpoint, timeout=15) as response:
        data = json.load(response)
    return data["author_name"], data.get("author_url", "")


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    if not slug:
        raise ValueError(f"cannot create slug for {value!r}")
    return slug


def clean_body(body: str, url: str) -> str:
    body = re.sub(r"^\s*对应分析[:：].*?\n+", "", body, count=1)
    body = re.sub(r"^\s*!\[\]\([^)]*\)\s*", "", body, count=1, flags=re.DOTALL)
    return f"![]({url})\n\n{body.strip()}\n"


def dump_frontmatter(metadata: dict) -> str:
    rendered = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False, width=1000).strip()
    return f"---\n{rendered}\n---\n"


def link(path: str, label: str) -> str:
    return f"[[{path}|{label}]]"


def main() -> int:
    args = parse_args()
    repo = args.repo.resolve()
    overrides = yaml.safe_load((repo / "data/featured-people.yml").read_text(encoding="utf-8")) or {}
    transcripts = repo / "transcripts"
    accounts_dir = repo / "accounts"
    people_dir = repo / "people"
    transcripts.mkdir(exist_ok=True)
    accounts_dir.mkdir(exist_ok=True)
    people_dir.mkdir(exist_ok=True)
    for generated_dir in (accounts_dir, people_dir):
        for generated_file in generated_dir.glob("*.md"):
            generated_file.unlink()

    account_docs: dict[str, list[dict]] = defaultdict(list)
    person_docs: dict[str, list[dict]] = defaultdict(list)
    catalog: list[dict] = []

    for path in sorted(args.source.glob("*.md")):
        source_meta, body = parse_document(path)
        url = source_url(source_meta)
        video_id = youtube_id(url)
        account_name = fallback_account(source_meta)
        account_url = ""
        if args.refresh_youtube:
            try:
                account_name, account_url = fetch_oembed(url)
            except Exception as error:
                print(f"warning: oEmbed failed for {video_id}: {error}")
        account_slug = slugify(account_name)
        featured_people = overrides.get(video_id, [])

        destination = transcripts / account_slug / path.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        relative_path = destination.relative_to(repo).as_posix()
        account_link = link(f"accounts/{account_slug}", account_name)
        people_links = [link(f"people/{slugify(person)}", person) for person in featured_people]
        normalized_meta = {
            "title": source_meta["title"],
            "source_url": url,
            "video_id": video_id,
            "account": account_link,
            "account_name": account_name,
        }
        if account_url:
            normalized_meta["account_url"] = account_url
        normalized_meta.update(
            {
                "featured_people": people_links,
                "published": source_meta.get("published"),
                "created": source_meta.get("created"),
                "language": "en",
                "speaker_attribution": "contextual",
                "description": source_meta.get("description", ""),
                "tags": ["transcript", "kol"],
            }
        )
        destination.write_text(dump_frontmatter(normalized_meta) + clean_body(body, url), encoding="utf-8")

        record = {
            "title": source_meta["title"],
            "path": relative_path,
            "source_url": url,
            "video_id": video_id,
            "account": account_name,
            "account_slug": account_slug,
            "featured_people": featured_people,
            "published": str(source_meta.get("published") or ""),
            "speaker_attribution": "contextual",
        }
        catalog.append(record)
        account_docs[account_slug].append(record)
        for person in featured_people:
            person_docs[person].append(record)

    for account_slug, records in sorted(account_docs.items()):
        account_name = records[0]["account"]
        lines = [f"# {account_name}", "", f"Transcripts: {len(records)}", ""]
        for record in sorted(records, key=lambda item: (item["published"], item["title"]), reverse=True):
            lines.append(f"- [[{Path(record['path']).with_suffix('').as_posix()}|{record['title']}]]")
        (accounts_dir / f"{account_slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for person, records in sorted(person_docs.items()):
        lines = [f"# {person}", "", f"Appearances: {len(records)}", ""]
        for record in sorted(records, key=lambda item: (item["published"], item["title"]), reverse=True):
            lines.append(f"- [[{Path(record['path']).with_suffix('').as_posix()}|{record['title']}]]")
        (people_dir / f"{slugify(person)}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    catalog.sort(key=lambda item: (item["account"].lower(), item["published"], item["title"]))
    with (repo / "catalog.jsonl").open("w", encoding="utf-8") as output:
        for record in catalog:
            output.write(json.dumps(record, ensure_ascii=False) + "\n")

    account_lines = ["# Accounts", ""]
    chinese_lines = ["# 账号索引", ""]
    for account_slug, records in sorted(account_docs.items(), key=lambda item: item[1][0]["account"].lower()):
        name = records[0]["account"]
        entry = f"- [[accounts/{account_slug}|{name}]] ({len(records)})"
        account_lines.append(entry)
        chinese_lines.append(entry)
    (repo / "Index.md").write_text("\n".join(account_lines) + "\n", encoding="utf-8")
    (repo / "索引.md").write_text("\n".join(chinese_lines) + "\n", encoding="utf-8")

    print(f"Imported {len(catalog)} transcripts across {len(account_docs)} accounts.")
    print(f"Created {len(person_docs)} person nodes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
