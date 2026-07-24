#!/usr/bin/env python3
"""Validate transcript metadata, links, timestamps, and catalog coverage."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TIMESTAMP_RE = re.compile(r"^\s*(?:\*\*)?\d{1,2}:\d{2}(?::\d{2})?(?:\*\*)?", re.MULTILINE)
LINK_RE = re.compile(r"\[\[([^]|]+)(?:\|[^]]+)?\]\]")
REQUIRED = {
    "title",
    "source_url",
    "video_id",
    "account",
    "account_name",
    "featured_people",
    "published",
    "language",
    "speaker_attribution",
}


def main() -> int:
    errors: list[str] = []
    video_ids: set[str] = set()
    paths: set[str] = set()
    timestamped = 0
    transcript_files = sorted((ROOT / "transcripts").glob("*/*.md"))

    for path in transcript_files:
        text = path.read_text(encoding="utf-8")
        match = FRONTMATTER_RE.match(text)
        if not match:
            errors.append(f"{path}: missing frontmatter")
            continue
        metadata = yaml.safe_load(match.group(1)) or {}
        missing = REQUIRED.difference(metadata)
        if missing:
            errors.append(f"{path}: missing {sorted(missing)}")
        video_id = str(metadata.get("video_id", ""))
        if video_id in video_ids:
            errors.append(f"{path}: duplicate video_id {video_id}")
        video_ids.add(video_id)
        if not str(metadata.get("source_url", "")).startswith("https://www.youtube.com/"):
            errors.append(f"{path}: unsupported source_url")
        if metadata.get("speaker_attribution") not in {"explicit", "contextual", "unattributed"}:
            errors.append(f"{path}: invalid speaker_attribution")
        for target in LINK_RE.findall(match.group(1)):
            if not (ROOT / f"{target}.md").exists():
                errors.append(f"{path}: broken link {target}")
        if TIMESTAMP_RE.search(text[match.end() :]):
            timestamped += 1
        paths.add(path.relative_to(ROOT).as_posix())

    catalog = [json.loads(line) for line in (ROOT / "catalog.jsonl").read_text(encoding="utf-8").splitlines()]
    catalog_paths = {record["path"] for record in catalog}
    if paths != catalog_paths:
        errors.append("catalog paths do not match transcript files")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(
        f"Validated {len(transcript_files)} transcripts, {len(video_ids)} unique videos, "
        f"and {timestamped} timestamped files."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
