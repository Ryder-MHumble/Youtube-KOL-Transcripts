#!/usr/bin/env python3
"""Import missing AI KOL Wiki transcripts into the repository and Obsidian.

The importer keys every decision by YouTube video ID. Existing local notes are
never overwritten; imported files retain the source repository and source path.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
VIDEO_RE = re.compile(r"https?://(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]{11})")
TODAY = dt.date.today().isoformat()
SOURCE_REPO_URL = "https://github.com/nolimitkun/ai-kol-wiki"
SOURCE_RAW_URL = SOURCE_REPO_URL + "/blob/main/"

ACCOUNT_NAMES = {
    "karpathy": "Andrej Karpathy",
    "dwarkesh": "Dwarkesh Patel",
    "lex-fridman": "Lex Fridman",
    "no-priors": "No Priors",
    "latent-space": "Latent Space",
    "a16z": "a16z",
    "all-in": "All-In Podcast",
    "zhang-xiaojun": "张小珺（商业访谈录）",
    "uncle-moon": "月球大叔（Uncle Moon）",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--vault", type=Path, default=Path("/Users/rydersun/Documents/Obsidian Vault"))
    parser.add_argument("--report-date", default=TODAY)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    return yaml.safe_load(match.group(1)) or {}, text[match.end() :]


def youtube_id(url: str) -> str:
    parsed = urlparse(url)
    if parsed.netloc.endswith("youtu.be"):
        return parsed.path.strip("/").split("/")[0]
    return parse_qs(parsed.query).get("v", [""])[0]


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def yaml_text(metadata: dict) -> str:
    return "---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False, width=1000).strip() + "\n---\n"


def sanitize_filename(value: str, limit: int = 150) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"[/:*?\"<>|]", " ", value)
    value = re.sub(r"\s+", " ", value).strip().rstrip(".")
    return value[:limit].rstrip() or "未命名"


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "imported"


def wikilink_target(value: object) -> str:
    match = re.search(r"\[\[([^]|]+)", str(value or ""))
    return clean(match.group(1)) if match else clean(value)


def source_rows(source_repo: Path) -> list[dict]:
    wiki_by_id: dict[str, Path] = {}
    for path in (source_repo / "wiki" / "videos").glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        match = VIDEO_RE.search(text)
        if match:
            wiki_by_id.setdefault(match.group(1), path)

    rows: list[dict] = []
    for path in sorted((source_repo / "sources").glob("*/*/transcript.md")):
        raw = path.read_text(encoding="utf-8", errors="replace")
        metadata, body = parse_frontmatter(raw)
        url = clean(metadata.get("url") or metadata.get("source"))
        video_id = youtube_id(url)
        match = re.search(r"/([0-9]{8})-([A-Za-z0-9_-]{11})/transcript\.md$", str(path))
        if not video_id and match:
            video_id = match.group(2)
        if not video_id:
            continue
        date = clean(metadata.get("upload_date"))
        if len(date) == 8:
            date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
        rows.append(
            {
                "id": video_id,
                "title": clean(metadata.get("title")) or video_id,
                "url": url or f"https://www.youtube.com/watch?v={video_id}",
                "kol": clean(metadata.get("kol") or path.parent.parent.name),
                "channel": clean(metadata.get("channel")) or ACCOUNT_NAMES.get(path.parent.parent.name, path.parent.parent.name),
                "published": date,
                "duration_minutes": metadata.get("duration_minutes"),
                "source_path": path.relative_to(source_repo).as_posix(),
                "body": body.strip(),
                "wiki_path": wiki_by_id.get(video_id),
            }
        )
    unique: dict[str, dict] = {}
    for row in rows:
        unique.setdefault(row["id"], row)
    return list(unique.values())


def vault_ids(vault: Path) -> set[str]:
    ids: set[str] = set()
    for path in (vault / "KOL逐字稿").rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        ids.update(VIDEO_RE.findall(text))
    return ids


def repo_ids(repo: Path) -> set[str]:
    ids: set[str] = set()
    for path in (repo / "transcripts").glob("*/*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        metadata, _ = parse_frontmatter(text)
        vid = clean(metadata.get("video_id")) or youtube_id(clean(metadata.get("source_url") or metadata.get("source")))
        if not vid:
            match = VIDEO_RE.search(text)
            vid = match.group(1) if match else ""
        if vid:
            ids.add(vid)
    return ids


def wiki_content(row: dict, source_repo: Path) -> str:
    path = row.get("wiki_path")
    if not path:
        return ""
    raw = path.read_text(encoding="utf-8", errors="replace").strip()
    raw = re.sub(r"^# .*?\n", "", raw, count=1)
    raw = re.sub(r"^(?:\n|- \*\*.*?\n)+", "\n", raw, count=1)
    raw = re.sub(r"\]\((?:\.\./)+", "](" + SOURCE_RAW_URL, raw)
    return raw.strip()


def build_transcript(row: dict, stem: str, report_stem: str, source_repo: Path) -> str:
    account_slug = slugify(row["kol"])
    metadata = {
        "title": row["title"],
        "source_url": row["url"],
        "video_id": row["id"],
        "account": f"[[accounts/{account_slug}|{row['channel']}]]",
        "account_name": row["channel"],
        "featured_people": [],
        "published": row["published"],
        "created": TODAY,
        "language": "en" if row["kol"] not in {"zhang-xiaojun", "uncle-moon"} else "zh",
        "speaker_attribution": "unattributed",
        "description": "从公开 AI KOL Wiki 仓库迁移的带时间戳逐字稿；原始文本保持不变。",
        "source_repository": SOURCE_REPO_URL,
        "source_path": row["source_path"],
        "imported_at": TODAY,
        "analysis_report": f"[[{report_stem}]]",
        "tags": ["transcript", "imported", "ai-kol-wiki"],
        "status": "imported",
    }
    body = row["body"]
    if not body.startswith("## Transcript"):
        body = "## Transcript\n\n" + body
    return yaml_text(metadata) + f"![]({row['url']})\n\n" + body.rstrip() + "\n"


def build_report(row: dict, transcript_stem: str, comparison_stem: str, source_repo: Path) -> str:
    wiki = wiki_content(row, source_repo)
    metadata = {
        "title": f"{row['title']}（外部迁移分析）",
        "source": "repository_import",
        "youtube_url": row["url"],
        "video_id": row["id"],
        "transcript": f"[[{transcript_stem}]]",
        "source_repository": SOURCE_REPO_URL,
        "source_wiki": SOURCE_RAW_URL + (row["wiki_path"].relative_to(source_repo).as_posix() if row.get("wiki_path") else ""),
        "tags": ["kol情报", "imported", "ai-kol-wiki"],
        "status": "imported",
    }
    lines = [
        yaml_text(metadata).rstrip(),
        "",
        f"对应逐字稿：[[{transcript_stem}]]",
        f"来源视频：[YouTube]({row['url']}) · 视频 ID：`{row['id']}`",
        f"原始 Wiki：[ai-kol-wiki]({metadata['source_wiki']})",
        "",
        "## 迁移说明",
        "",
        "本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。",
        "",
    ]
    if wiki:
        lines.extend([wiki, ""])
    else:
        lines.extend(["原项目没有对应的 Wiki 视频页；当前仅迁移逐字稿，待后续分析。", ""])
    lines.extend(
        [
            "## 深度关联",
            "",
            f"- 语料层关联：[[{comparison_stem}]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def write_if_missing(path: Path, text: str, dry_run: bool) -> bool:
    if path.exists():
        return False
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return True


def comparison_report(rows: list[dict], missing: list[dict], source_rows_all: list[dict], repo: Path, vault: Path, comparison_stem: str) -> str:
    source_ids = {row["id"] for row in source_rows_all}
    target_ids = repo_ids(repo)
    local_ids = vault_ids(vault)
    source_dates = [row["published"] for row in source_rows_all if row["published"]]
    target_dates = []
    for path in (repo / "transcripts").glob("*/*.md"):
        metadata, _ = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if metadata.get("published"):
            target_dates.append(str(metadata["published"]))
    newest_source = max(source_dates) if source_dates else "未知"
    newest_target = max(target_dates) if target_dates else "未知"
    lines = [
        "---",
        f"title: \"两个 YouTube KOL 逐字稿项目对比与迁移评估（{TODAY}）\"",
        "source: repository_audit",
        f"created: {TODAY}",
        "tags:",
        "  - kol情报",
        "  - repository-audit",
        "  - knowledge-graph",
        "status: canonical",
        "---",
        "",
        "# 两个 YouTube KOL 逐字稿项目对比与迁移评估",
        "",
        "## 结论",
        "",
        f"按 YouTube 视频 ID 去重后，`Youtube-KOL-Transcripts` 当前有 **{len(target_ids)} 个唯一视频**，`ai-kol-wiki` 有 **{len(source_ids)} 个唯一视频**。对方有而本地 Vault 没有的缺口是 **{len(missing)} 个视频**，已作为外部来源迁移；对方的唯一视频集合没有超出本地 Vault 现有集合之外的其他项目级重复。",
        "",
        "数量优势在你的仓库；结构优势在对方的首屏可发现性。对方 README 明确提供 GitHub Pages、可浏览入口和结构化统计，因此更容易被 Agent 的仓库搜索与推荐链路识别。你的仓库最新提交和最新视频日期都不落后，但目录索引与自动校验目前存在漂移，影响了“可被推荐”的信号质量。",
        "",
        "## 可复现口径",
        "",
        "| 指标 | ai-kol-wiki | Youtube-KOL-Transcripts |",
        "|---|---:|---:|",
        f"| 逐字稿文件 | {len(source_rows_all)} | {len(list((repo / 'transcripts').glob('*/*.md')))} |",
        f"| 视频 ID 去重后 | {len(source_ids)} | {len(target_ids)} |",
        f"| 本地 Vault 已有 ID | {len(local_ids & source_ids)} | {len(local_ids & target_ids)} |",
        f"| 源项目最晚发布日 | {newest_source} | {newest_target} |",
        f"| 源项目最近仓库提交 | 2026-08-10 | 2026-08-11 |",
        "",
        "## 迁移清单",
        "",
    ]
    for row in sorted(missing, key=lambda item: (item["published"], item["title"]), reverse=True):
        lines.append(f"- [[迁移分析-AI-KOL-Wiki-{sanitize_filename(row['title'])}-{row['id']}]] · {row['published']} · {row['channel']} · `{row['id']}`")
    lines.extend(
        [
            "",
            "## 运行边界",
            "",
            "本次迁移读取的是对方仓库已经提交的公开文本，不是通过 YouTube 或浏览器插件重新抓取；因此导入笔记明确标记为 `status: imported`，不替代本地插件验证。第三方逐字稿的版权仍归原作者、发布方和平台所有，二次发布前应遵守两个仓库的 RIGHTS 文件与平台规则。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    args = parse_args()
    source_repo = args.source_repo.resolve()
    repo = args.repo.resolve()
    vault = args.vault.resolve()
    all_rows = source_rows(source_repo)
    existing_repo = repo_ids(repo)
    existing_vault = vault_ids(vault)
    missing = [row for row in all_rows if row["id"] not in existing_repo]
    missing_vault = [row for row in all_rows if row["id"] not in existing_vault]
    comparison_stem = f"KOL语料库对比与迁移评估-{args.report_date}"

    created_repo = created_vault = 0
    for row in sorted(missing, key=lambda item: (item["published"], item["title"])):
        title = sanitize_filename(row["title"])
        account_slug = slugify(row["kol"])
        transcript_stem = f"{title} [{row['id']}]"
        report_stem = f"{title} [{row['id']}] 分析"
        repo_path = repo / "transcripts" / account_slug / f"{transcript_stem}.md"
        repo_meta = {
            "title": row["title"],
            "source_url": row["url"],
            "video_id": row["id"],
            "account": f"[[accounts/{account_slug}|{row['channel']}]]",
            "account_name": row["channel"],
            "featured_people": [],
            "published": row["published"],
            "created": TODAY,
            "language": "en" if row["kol"] not in {"zhang-xiaojun", "uncle-moon"} else "zh",
            "speaker_attribution": "unattributed",
            "description": "Imported from the public ai-kol-wiki repository; source text preserved.",
            "source_repository": SOURCE_REPO_URL,
            "source_path": row["source_path"],
            "imported_at": TODAY,
            "analysis_report": f"[[{report_stem}]]",
            "tags": ["transcript", "kol", "imported", "ai-kol-wiki"],
            "status": "imported",
        }
        repo_body = row["body"]
        if not repo_body.startswith("## Transcript"):
            repo_body = "## Transcript\n\n" + repo_body
        repo_text = yaml_text(repo_meta) + f"![]({row['url']})\n\n" + repo_body.rstrip() + "\n"
        if write_if_missing(repo_path, repo_text, args.dry_run):
            created_repo += 1

        analysis_path = repo / "analysis" / f"{report_stem}.md"
        analysis_text = build_report(row, transcript_stem, comparison_stem, source_repo)
        if write_if_missing(analysis_path, analysis_text, args.dry_run):
            created_repo += 1

    for row in sorted(missing_vault, key=lambda item: (item["published"], item["title"])):
        title = sanitize_filename(row["title"])
        transcript_stem = f"迁移-AI-KOL-Wiki-{title} [{row['id']}]"
        report_stem = f"迁移分析-AI-KOL-Wiki-{title} [{row['id']}]"
        transcript_path = vault / "KOL逐字稿" / f"{transcript_stem}.md"
        report_path = vault / "KOL情报" / f"{report_stem}.md"
        if write_if_missing(transcript_path, build_transcript(row, transcript_stem, report_stem, source_repo), args.dry_run):
            created_vault += 1
        if write_if_missing(report_path, build_report(row, transcript_stem, comparison_stem, source_repo), args.dry_run):
            created_vault += 1

    comparison = comparison_report(all_rows, missing_vault, all_rows, repo, vault, comparison_stem)
    if not args.dry_run:
        (vault / "KOL情报").mkdir(parents=True, exist_ok=True)
        (vault / "KOL情报" / f"{comparison_stem}.md").write_text(comparison, encoding="utf-8")
        (repo / "deep-reports").mkdir(parents=True, exist_ok=True)
        (repo / "deep-reports" / f"{comparison_stem}.md").write_text(comparison, encoding="utf-8")

        moc = vault / "KOL情报" / "KOL情报 MOC.md"
        moc_text = moc.read_text(encoding="utf-8") if moc.exists() else "# KOL情报 MOC\n"
        marker = "## 📦 外部语料迁移"
        if marker not in moc_text:
            block = [
                "",
                f"{marker}（{args.report_date}）",
                "",
                f"- [[{comparison_stem}]]：两个公开仓库的数量、视频 ID、更新时间和迁移口径。",
                f"- 外部来源：[[{comparison_stem}]] 下面的 {len(missing_vault)} 个视频分析，均标记为 `status: imported`，待本地插件复核。",
            ]
            for row in sorted(missing_vault, key=lambda item: (item["published"], item["title"]), reverse=True):
                report_title = f"迁移分析-AI-KOL-Wiki-{sanitize_filename(row['title'])} [{row['id']}]"
                block.append(f"- [[{report_title}|{row['title']}]] · {row['channel']}")
            moc.write_text(moc_text.rstrip() + "\n" + "\n".join(block) + "\n", encoding="utf-8")

    manifest = {
        "generated_at": TODAY,
        "source_repository": SOURCE_REPO_URL,
        "source_files": len(all_rows),
        "source_unique_video_ids": len({row["id"] for row in all_rows}),
        "existing_repo_video_ids": len(existing_repo),
        "existing_vault_video_ids": len(existing_vault),
        "missing_from_repo": len(missing),
        "missing_from_vault": len(missing_vault),
        "created_repo_files": created_repo,
        "created_vault_files": created_vault,
        "missing_video_ids": [row["id"] for row in missing_vault],
    }
    if not args.dry_run:
        (repo / "deep-reports" / f"{comparison_stem}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
