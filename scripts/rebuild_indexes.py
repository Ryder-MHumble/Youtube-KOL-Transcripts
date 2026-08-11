#!/usr/bin/env python3
"""Rebuild generated indexes and site data from transcript markdown files."""

from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from typing import Iterable

import yaml


ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^]|]+)(?:\|([^]]+))?\]\]")
YOUTUBE_RE = re.compile(r"(?:https?://(?:www\.)?youtube\.com/watch\?v=|https?://youtu\.be/)([A-Za-z0-9_-]{11})")
VALID_ATTESTATION = {"explicit", "contextual", "unattributed"}
ACCOUNT_ALIASES = {
    "zhang-xiaojun": ["张小珺", "张小珺（商业访谈录）"],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--site-out", type=Path, default=ROOT / "site" / "data.json")
    parser.add_argument("--write-indexes", action="store_true", default=True)
    parser.add_argument("--no-write-indexes", dest="write_indexes", action="store_false")
    return parser.parse_args()


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    return yaml.safe_load(match.group(1)) or {}, text[match.end() :]


def dump_frontmatter(meta: dict) -> str:
    return "---\n" + yaml.safe_dump(meta, allow_unicode=True, sort_keys=False, width=1000).strip() + "\n---\n"


def normalize_text(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def unwrap_wikilink(value: object) -> str:
    text = normalize_text(value)
    match = WIKILINK_RE.fullmatch(text)
    if not match:
        return text
    return normalize_text(match.group(2) or match.group(1))


def as_list(value: object) -> list[object]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "imported"


def youtube_id_from_url(url: str) -> str:
    match = YOUTUBE_RE.search(url or "")
    return match.group(1) if match else ""


def parse_wikilink_target(value: object) -> tuple[str, str]:
    text = normalize_text(value)
    match = WIKILINK_RE.fullmatch(text)
    if not match:
        return "", text
    target = normalize_text(match.group(1))
    label = normalize_text(match.group(2) or match.group(1))
    return target, label


def source_url(meta: dict, body: str) -> str:
    for key in ("source_url", "source", "youtube_url"):
        value = normalize_text(meta.get(key))
        if value.startswith("http"):
            return value
    match = YOUTUBE_RE.search(body)
    return match.group(0) if match else ""


def published_value(meta: dict) -> str:
    value = meta.get("published")
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, datetime):
        return value.date().isoformat()
    return normalize_text(value)


def account_info(meta: dict, rel_path: Path) -> tuple[str, str]:
    account_name = normalize_text(meta.get("account_name"))
    account_field = meta.get("account")
    author_field = meta.get("author")
    account_slug = ""
    slug_from_link = False

    if isinstance(account_field, str):
        target, label = parse_wikilink_target(account_field)
        if target:
            target = target.removeprefix("accounts/")
            account_slug = target
            slug_from_link = True
            account_name = account_name or label
        else:
            account_name = account_name or account_field
    elif isinstance(account_field, list):
        names = [unwrap_wikilink(item) for item in account_field if normalize_text(item)]
        if names:
            account_name = account_name or ", ".join(names)

    if not account_name and author_field is not None:
        if isinstance(author_field, list):
            names = [unwrap_wikilink(item) for item in author_field if normalize_text(item)]
            account_name = ", ".join(names)
        else:
            account_name = unwrap_wikilink(author_field)

    if not account_name:
        account_name = rel_path.parent.name.replace("-", " ").strip() or rel_path.parent.name

    if not account_slug:
        derived_slug = slugify(account_name) if account_name else ""
        account_slug = derived_slug if derived_slug != "imported" else rel_path.parent.name

    if slug_from_link and not account_name:
        account_name = account_slug.replace("-", " ").strip() or account_slug

    return account_slug, account_name


def account_link(slug: str, label: str) -> str:
    return f"[[accounts/{slug}|{label}]]"


def person_list(value: object) -> list[str]:
    people = []
    for item in as_list(value):
        text = unwrap_wikilink(item)
        if text:
            people.append(text)
    return people


def transcript_records(root: Path) -> list[dict]:
    records: list[dict] = []
    for path in sorted((root / "transcripts").glob("*/*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        meta, body = parse_frontmatter(text)
        url = source_url(meta, body)
        video_id = normalize_text(meta.get("video_id")) or youtube_id_from_url(url)
        account_slug, account_name = account_info(meta, path.relative_to(root))
        featured_people = person_list(meta.get("featured_people"))
        analysis_report = normalize_text(meta.get("analysis_report"))
        analysis_path = ""
        if analysis_report:
            target, _ = parse_wikilink_target(analysis_report)
            if target:
                target = target.removeprefix("analysis/")
                analysis_path = f"analysis/{target}"

        tags = [normalize_text(tag) for tag in as_list(meta.get("tags")) if normalize_text(tag)]
        status = normalize_text(meta.get("status")) or ("imported" if "imported" in tags else "")
        speaker_attribution = normalize_text(meta.get("speaker_attribution"))
        if speaker_attribution not in VALID_ATTESTATION:
            speaker_attribution = ""
        account_aliases = ACCOUNT_ALIASES.get(account_slug, [])

        record = {
            "kind": "transcript",
            "title": normalize_text(meta.get("title")) or path.stem,
            "path": path.relative_to(root).as_posix(),
            "source_url": url,
            "video_id": video_id,
            "source_id": normalize_text(meta.get("source_id")),
            "account_slug": account_slug,
            "account_name": account_name,
            "featured_people": featured_people,
            "published": published_value(meta),
            "created": published_value({"published": meta.get("created")}) if meta.get("created") else "",
            "speaker_attribution": speaker_attribution,
            "status": status,
            "tags": tags,
            "description": normalize_text(meta.get("description")),
            "analysis_path": analysis_path,
            "analysis_title": normalize_text(parse_wikilink_target(analysis_report)[1]) if analysis_report else "",
            "search_text": "",
            "account_aliases": account_aliases,
        }
        search_tokens = [
            record["title"],
            record["account_name"],
            record["account_slug"],
            " ".join(record["account_aliases"]),
            record["video_id"],
            record["source_id"],
            record["published"],
            record["status"],
            record["description"],
            " ".join(record["featured_people"]),
            record["analysis_title"],
            " ".join(record["tags"]),
            record["path"],
        ]
        record["search_text"] = normalize_text(" ".join(token for token in search_tokens if token))
        records.append(record)
    return records


def choose_canonical(group: list[dict]) -> dict:
    def score(record: dict) -> tuple[int, int, int, int, int]:
        return (
            1 if record["account_name"] else 0,
            1 if record["source_url"] else 0,
            1 if record["analysis_path"] else 0,
            1 if record["speaker_attribution"] else 0,
            len(record["featured_people"]),
        )

    return sorted(group, key=lambda item: (score(item), item["published"], item["title"]), reverse=True)[0]


def group_canonical(records: list[dict]) -> tuple[list[dict], dict[str, list[dict]]]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        key = record["video_id"] or record["source_id"] or record["path"]
        grouped[key].append(record)

    canonical: list[dict] = []
    for key, group in grouped.items():
        chosen = choose_canonical(group)
        chosen = dict(chosen)
        chosen["variant_count"] = len(group)
        chosen["variant_paths"] = [item["path"] for item in group]
        canonical.append(chosen)

    canonical.sort(key=lambda item: (item["published"], item["account_name"], item["title"]), reverse=True)
    return canonical, grouped


def build_accounts(records: Iterable[dict]) -> dict[str, dict]:
    accounts: dict[str, dict] = {}
    for record in records:
        slug = record["account_slug"]
        entry = accounts.setdefault(
            slug,
            {
                "slug": slug,
                "name": record["account_name"],
                "path": f"accounts/{slug}.md",
                "transcripts": [],
                "latest_published": "",
            },
        )
        entry["name"] = entry["name"] or record["account_name"]
        entry["transcripts"].append(record)
        if record["published"] and record["published"] > entry["latest_published"]:
            entry["latest_published"] = record["published"]
    return accounts


def build_people(records: Iterable[dict]) -> dict[str, dict]:
    people: dict[str, dict] = {}
    for record in records:
        for name in record["featured_people"]:
            slug = slugify(name)
            entry = people.setdefault(
                slug,
                {
                    "slug": slug,
                    "name": name,
                    "path": f"people/{slug}.md",
                    "appearances": [],
                    "latest_published": "",
                },
            )
            entry["appearances"].append(record)
            if record["published"] and record["published"] > entry["latest_published"]:
                entry["latest_published"] = record["published"]
    return people


def write_account_pages(root: Path, accounts: dict[str, dict]) -> None:
    account_dir = root / "accounts"
    account_dir.mkdir(parents=True, exist_ok=True)
    for slug, account in sorted(accounts.items(), key=lambda item: item[0]):
        records = sorted(account["transcripts"], key=lambda item: (item["published"], item["title"]), reverse=True)
        lines = [f"# {account['name']}", "", f"Transcripts: {len(records)}", ""]
        for record in records:
            lines.append(f"- [[{record['path'].removesuffix('.md')}|{record['title']}]]")
        (account_dir / f"{slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index_pages(root: Path, accounts: dict[str, dict]) -> None:
    sorted_accounts = sorted(accounts.values(), key=lambda item: (item["name"].lower(), item["slug"]))
    english = ["# Accounts", ""]
    chinese = ["# 账号索引", ""]
    for account in sorted_accounts:
        entry = f"- [[accounts/{account['slug']}|{account['name']}]] ({len(account['transcripts'])})"
        english.append(entry)
        chinese.append(entry)
    (root / "Index.md").write_text("\n".join(english) + "\n", encoding="utf-8")
    (root / "索引.md").write_text("\n".join(chinese) + "\n", encoding="utf-8")


def write_catalog(root: Path, records: list[dict]) -> None:
    lines = []
    for record in sorted(records, key=lambda item: (item["account_name"].lower(), item["published"], item["title"])):
        lines.append(
            json.dumps(
                {
                    "title": record["title"],
                    "path": record["path"],
                    "source_url": record["source_url"],
                    "video_id": record["video_id"],
                    "source_id": record["source_id"],
                    "account": record["account_name"],
                    "account_slug": record["account_slug"],
                    "featured_people": record["featured_people"],
                    "published": record["published"],
                    "speaker_attribution": record["speaker_attribution"] or "contextual",
                },
                ensure_ascii=False,
            )
        )
    (root / "catalog.jsonl").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_site_data(root: Path, canonical: list[dict], accounts: dict[str, dict], people: dict[str, dict]) -> dict:
    latest = max((record["published"] for record in canonical if record["published"]), default="")
    imported_count = sum(1 for record in canonical if record["status"] == "imported")
    records = []
    for record in canonical:
        records.append(
            {
                "kind": record["kind"],
                "title": record["title"],
                "path": record["path"],
                "source_url": record["source_url"],
                "video_id": record["video_id"],
                "source_id": record["source_id"],
                "account_slug": record["account_slug"],
                "account_name": record["account_name"],
                "featured_people": record["featured_people"],
                "published": record["published"],
                "speaker_attribution": record["speaker_attribution"] or "contextual",
                "status": record["status"] or "canonical",
                "tags": record["tags"],
                "description": record["description"],
                "analysis_path": record["analysis_path"],
                "variant_count": record["variant_count"],
                "variant_paths": record["variant_paths"],
                "search_text": record["search_text"],
            }
        )

    return {
        "generated_at": date.today().isoformat(),
        "repo": "Ryder-MHumble/Youtube-KOL-Transcripts",
        "counts": {
            "transcript_files": len(list((root / "transcripts").glob("*/*.md"))),
            "source_records": len(canonical),
            "unique_video_ids": len({record["video_id"] for record in canonical if record["video_id"]}),
            "non_youtube_sources": sum(1 for record in canonical if not record["video_id"]),
            "account_pages": len(accounts),
            "people_pages": len(people),
            "analysis_files": len(list((root / "analysis").glob("*.md"))),
            "imported_transcripts": imported_count,
            "latest_published": latest,
        },
        "accounts": [
            {
                "slug": account["slug"],
                "name": account["name"],
                "path": account["path"],
                "transcript_count": len(account["transcripts"]),
                "latest_published": account["latest_published"],
                "sample_titles": [item["title"] for item in sorted(account["transcripts"], key=lambda item: (item["published"], item["title"]), reverse=True)[:5]],
                "search_text": normalize_text(
                    " ".join(
                        [
                            account["name"],
                            account["slug"],
                            account["latest_published"],
                            " ".join(item["title"] for item in account["transcripts"]),
                        ]
                    )
                ),
            }
            for account in sorted(accounts.values(), key=lambda item: item["name"].lower())
        ],
        "people": [
            {
                "slug": person["slug"],
                "name": person["name"],
                "path": person["path"],
                "appearance_count": len(person["appearances"]),
                "latest_published": person["latest_published"],
                "sample_titles": [item["title"] for item in sorted(person["appearances"], key=lambda item: (item["published"], item["title"]), reverse=True)[:5]],
                "search_text": normalize_text(
                    " ".join(
                        [
                            person["name"],
                            person["slug"],
                            person["latest_published"],
                            " ".join(item["title"] for item in person["appearances"]),
                        ]
                    )
                ),
            }
            for person in sorted(people.values(), key=lambda item: item["name"].lower())
        ],
        "records": records,
    }


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    all_records = transcript_records(root)
    canonical_records, grouped = group_canonical(all_records)
    accounts = build_accounts(canonical_records)
    people = build_people(canonical_records)

    if args.write_indexes:
        write_account_pages(root, accounts)
        write_index_pages(root, accounts)
        write_catalog(root, all_records)

    site_data = build_site_data(root, canonical_records, accounts, people)
    args.site_out.parent.mkdir(parents=True, exist_ok=True)
    args.site_out.write_text(json.dumps(site_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "transcript_files": len(all_records),
                "source_records": len(canonical_records),
                "unique_video_ids": site_data["counts"]["unique_video_ids"],
                "non_youtube_sources": site_data["counts"]["non_youtube_sources"],
                "account_pages": len(accounts),
                "people_pages": len(people),
                "analysis_files": len(list((root / "analysis").glob("*.md"))),
                "imported_transcripts": site_data["counts"]["imported_transcripts"],
                "latest_published": site_data["counts"]["latest_published"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
