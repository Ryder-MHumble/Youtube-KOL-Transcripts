#!/usr/bin/env python3
"""Sync recent Lex Fridman transcript notes into this repository."""

from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path("/Users/rydersun/Documents/Obsidian Vault/KOL逐字稿")
ACCOUNT_NAME = "Lex Fridman"
ACCOUNT_SLUG = "lex-fridman"
ACCOUNT_URL = "https://www.youtube.com/lexfridman"
SINCE = "2025-07-24"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    if not slug:
        raise ValueError(f"cannot create slug for {value!r}")
    return slug


def parse_note(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"missing frontmatter: {path}")
    return yaml.safe_load(match.group(1)) or {}, text[match.end() :]


def youtube_id(url: str) -> str:
    match = re.search(r"[?&]v=([A-Za-z0-9_-]{11})", url)
    if not match:
        raise ValueError(f"cannot extract video id from {url}")
    return match.group(1)


def wikilink(path: str, label: str) -> str:
    return f"[[{path}|{label}]]"


def people_from_body(body: str) -> list[str]:
    names: list[str] = []
    for match in re.finditer(r"^\*\*[^*]+(?:\*\*)?\s*·\s*([^:\n]+):", body, re.M):
        name = match.group(1).strip()
        if name == ACCOUNT_NAME or not name:
            continue
        if name not in names:
            names.append(name)
    return names


def clean_body(body: str, source_url: str) -> str:
    body = re.sub(r"^\s*!\[\]\([^)]*\)\s*", "", body, count=1, flags=re.S).strip()
    return f"![]({source_url})\n\n{body}\n"


def dump_frontmatter(metadata: dict) -> str:
    rendered = yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False, width=1000).strip()
    return f"---\n{rendered}\n---\n"


def load_catalog() -> list[dict]:
    catalog_path = ROOT / "catalog.jsonl"
    if not catalog_path.exists():
        return []
    return [json.loads(line) for line in catalog_path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_catalog(records: list[dict]) -> None:
    records = sorted(records, key=lambda item: (item["account"].lower(), item["published"], item["title"]))
    with (ROOT / "catalog.jsonl").open("w", encoding="utf-8") as output:
        for record in records:
            output.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_indexes(records: list[dict]) -> None:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[record["account_slug"]].append(record)

    english = ["# Accounts", ""]
    chinese = ["# 账号索引", ""]
    for slug, items in sorted(grouped.items(), key=lambda item: item[1][0]["account"].lower()):
        name = items[0]["account"]
        line = f"- [[accounts/{slug}|{name}]] ({len(items)})"
        english.append(line)
        chinese.append(line)
    (ROOT / "Index.md").write_text("\n".join(english) + "\n", encoding="utf-8")
    (ROOT / "索引.md").write_text("\n".join(chinese) + "\n", encoding="utf-8")


def write_account_docs(records: list[dict]) -> None:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[record["account_slug"]].append(record)

    accounts_dir = ROOT / "accounts"
    accounts_dir.mkdir(exist_ok=True)
    for slug, items in grouped.items():
        name = items[0]["account"]
        lines = [f"# {name}", "", f"Transcripts: {len(items)}", ""]
        for record in sorted(items, key=lambda item: (item["published"], item["title"]), reverse=True):
            stem = Path(record["path"]).with_suffix("").as_posix()
            lines.append(f"- [[{stem}|{record['title']}]]")
        (accounts_dir / f"{slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_people_docs(records: list[dict]) -> None:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        for person in record.get("featured_people") or []:
            grouped[person].append(record)

    people_dir = ROOT / "people"
    people_dir.mkdir(exist_ok=True)
    for person, items in grouped.items():
        lines = [f"# {person}", "", f"Appearances: {len(items)}", ""]
        for record in sorted(items, key=lambda item: (item["published"], item["title"]), reverse=True):
            stem = Path(record["path"]).with_suffix("").as_posix()
            lines.append(f"- [[{stem}|{record['title']}]]")
        (people_dir / f"{slugify(person)}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_featured_people(records: list[dict]) -> None:
    mapping = {
        record["video_id"]: record["featured_people"]
        for record in sorted(records, key=lambda item: item["video_id"])
        if record.get("featured_people")
    }
    (ROOT / "data" / "featured-people.yml").write_text(
        yaml.safe_dump(mapping, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )


def update_readmes(records: list[dict]) -> None:
    transcript_count = len(records)
    account_count = len({record["account_slug"] for record in records})
    people_count = len({person for record in records for person in record.get("featured_people") or []})
    replacements = [
        (ROOT / "README.md", [
            (r"\*\*\d+ complete transcripts\*\*", f"**{transcript_count} complete transcripts**"),
            (r"\*\*\d+ publishing accounts\*\*", f"**{account_count} publishing accounts**"),
            (r"\*\*\d+ featured-person nodes\*\*", f"**{people_count} featured-person nodes**"),
        ]),
        (ROOT / "README.zh-CN.md", [
            (r"\*\*\d+ 份完整逐字稿\*\*", f"**{transcript_count} 份完整逐字稿**"),
            (r"\*\*\d+ 个重点发布账号\*\*", f"**{account_count} 个重点发布账号**"),
            (r"\*\*\d+ 个人物节点\*\*", f"**{people_count} 个人物节点**"),
        ]),
    ]
    for path, rules in replacements:
        text = path.read_text(encoding="utf-8")
        for pattern, replacement in rules:
            text = re.sub(pattern, replacement, text)
        path.write_text(text, encoding="utf-8")


def main() -> int:
    catalog = [record for record in load_catalog() if record.get("account_slug") != ACCOUNT_SLUG]
    destination_dir = ROOT / "transcripts" / ACCOUNT_SLUG
    destination_dir.mkdir(parents=True, exist_ok=True)

    new_records: list[dict] = []
    for source_path in sorted(SOURCE_DIR.glob("Lex Fridman - *逐字稿.md")):
        source_meta, body = parse_note(source_path)
        published = str(source_meta.get("published") or "")
        if published < SINCE:
            continue
        source_url = str(source_meta.get("source") or "")
        video_id = youtube_id(source_url)
        title = str(source_meta.get("title") or source_path.stem)
        people = people_from_body(body)
        destination = destination_dir / source_path.name
        relative_path = destination.relative_to(ROOT).as_posix()
        metadata = {
            "title": title,
            "source_url": source_url,
            "video_id": video_id,
            "account": wikilink(f"accounts/{ACCOUNT_SLUG}", ACCOUNT_NAME),
            "account_name": ACCOUNT_NAME,
            "account_url": ACCOUNT_URL,
            "featured_people": [wikilink(f"people/{slugify(person)}", person) for person in people],
            "published": published,
            "created": str(source_meta.get("created") or ""),
            "language": "en",
            "speaker_attribution": "explicit",
            "description": str(source_meta.get("description") or ""),
            "tags": ["transcript", "kol"],
        }
        destination.write_text(dump_frontmatter(metadata) + clean_body(body, source_url), encoding="utf-8")
        new_records.append({
            "title": title,
            "path": relative_path,
            "source_url": source_url,
            "video_id": video_id,
            "account": ACCOUNT_NAME,
            "account_slug": ACCOUNT_SLUG,
            "featured_people": people,
            "published": published,
            "speaker_attribution": "explicit",
        })

    all_records = catalog + new_records
    write_catalog(all_records)
    write_indexes(all_records)
    write_account_docs(all_records)
    write_people_docs(all_records)
    write_featured_people(all_records)
    update_readmes(all_records)
    print(f"Synced {len(new_records)} Lex Fridman transcripts.")
    print(f"Repository now has {len(all_records)} transcripts.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
