#!/usr/bin/env python3
"""Search timestamped transcript passages without external dependencies."""

from __future__ import annotations

import argparse
import json
import math
import re
import urllib.parse
from collections import Counter
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
TIMESTAMP_RE = re.compile(
    r"^\s*(?:\*\*)?(\d{1,2}:\d{2}(?::\d{2})?)(?:\*\*)?\s*(?:[·|\-–—]\s*)?(.*)$"
)
WORD_RE = re.compile(r"[a-z0-9][a-z0-9'+.-]*", re.IGNORECASE)
CJK_RE = re.compile(r"[\u3400-\u9fff]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--account", default="")
    parser.add_argument("--person", default="")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()


def find_repo(explicit: Path | None) -> Path:
    if explicit:
        return explicit.resolve()
    starting_points = [Path.cwd(), Path(__file__).resolve()]
    for starting_point in starting_points:
        for candidate in (starting_point, *starting_point.parents):
            if (candidate / "catalog.jsonl").is_file() and (candidate / "transcripts").is_dir():
                return candidate
    raise FileNotFoundError("cannot find repository root; run from the clone or pass --repo")


def tokenize(text: str) -> list[str]:
    lowered = text.lower()
    tokens = WORD_RE.findall(lowered)
    for sequence in CJK_RE.findall(lowered):
        tokens.extend(sequence)
        tokens.extend(sequence[index : index + 2] for index in range(len(sequence) - 1))
    return [token for token in tokens if len(token) > 1 or token.isdigit()]


def load_catalog(repo: Path) -> list[dict]:
    with (repo / "catalog.jsonl").open(encoding="utf-8") as source:
        return [json.loads(line) for line in source if line.strip()]


def transcript_body(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    body = text[match.end() :] if match else text
    marker = re.search(r"^##\s+Transcript\s*$", body, re.IGNORECASE | re.MULTILINE)
    return body[marker.end() :] if marker else body


def timestamped_segments(body: str) -> list[tuple[str, str]]:
    segments: list[tuple[str, str]] = []
    timestamp = ""
    lines: list[str] = []

    def flush() -> None:
        if timestamp and lines:
            quote = " ".join(line.strip() for line in lines if line.strip())
            if quote:
                segments.append((timestamp, quote))

    for line in body.splitlines():
        match = TIMESTAMP_RE.match(line)
        if match:
            flush()
            timestamp = match.group(1)
            lines = [match.group(2)] if match.group(2) else []
        elif timestamp and line.strip() and not line.lstrip().startswith("#"):
            lines.append(line)
    flush()
    return segments


def fallback_segments(body: str) -> list[tuple[str, str]]:
    paragraphs = re.split(r"\n\s*\n", body)
    return [("", paragraph.replace("\n", " ").strip()) for paragraph in paragraphs if len(paragraph.strip()) >= 80]


def timestamp_seconds(value: str) -> int:
    parts = [int(part) for part in value.split(":")]
    if len(parts) == 2:
        return parts[0] * 60 + parts[1]
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def timestamp_url(url: str, timestamp: str) -> str:
    if not timestamp:
        return url
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    query["t"] = [str(timestamp_seconds(timestamp))]
    return urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(query, doseq=True)))


def candidate_segments(repo: Path, records: list[dict]) -> list[dict]:
    candidates: list[dict] = []
    for record in records:
        body = transcript_body(repo / record["path"])
        segments = timestamped_segments(body) or fallback_segments(body)
        metadata_text = " ".join(
            [record["title"], record["account"], " ".join(record.get("featured_people", []))]
        )
        for timestamp, quote in segments:
            candidates.append(
                {
                    **record,
                    "timestamp": timestamp,
                    "timestamp_url": timestamp_url(record["source_url"], timestamp),
                    "quote": quote,
                    "search_text": f"{metadata_text} {quote}",
                }
            )
    return candidates


def rank(query: str, candidates: list[dict]) -> list[dict]:
    query_tokens = Counter(tokenize(query))
    if not query_tokens:
        return []
    document_frequency = Counter()
    tokenized: list[Counter] = []
    for candidate in candidates:
        counts = Counter(tokenize(candidate["search_text"]))
        tokenized.append(counts)
        document_frequency.update(counts.keys())

    total = max(len(candidates), 1)
    query_lower = query.lower().strip()
    results = []
    for candidate, counts in zip(candidates, tokenized):
        score = 0.0
        matched = set(query_tokens).intersection(counts)
        for token in matched:
            inverse_frequency = math.log((total + 1) / (document_frequency[token] + 1)) + 1
            score += inverse_frequency * min(counts[token], 4) * query_tokens[token]
        if query_lower and query_lower in candidate["search_text"].lower():
            score += 12
        if score <= 0:
            continue
        result = {key: value for key, value in candidate.items() if key != "search_text"}
        result["score"] = round(score, 3)
        results.append(result)
    return sorted(results, key=lambda item: (-item["score"], item["title"], item["timestamp"]))


def main() -> int:
    args = parse_args()
    repo = find_repo(args.repo)
    records = load_catalog(repo)
    if args.account:
        records = [record for record in records if args.account.lower() in record["account"].lower()]
    if args.person:
        records = [
            record
            for record in records
            if any(args.person.lower() in person.lower() for person in record.get("featured_people", []))
        ]
    results = rank(args.query, candidate_segments(repo, records))[: max(args.limit, 0)]
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for result in results:
            people = ", ".join(result.get("featured_people", [])) or "Unverified speaker"
            print(f"[{result['score']}] {result['title']}")
            print(f"Account: {result['account']} | People: {people}")
            print(f"Quote: {result['quote']}")
            print(f"Source: {result['timestamp_url']}")
            print(f"Path: {result['path']}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
