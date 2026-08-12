#!/usr/bin/env python3
"""Import Mally-cj/zhangxiaojun-archives raw transcripts as source variants."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import unicodedata
from pathlib import Path
from urllib.parse import quote

import yaml


TODAY = dt.date.today().isoformat()
SOURCE_REPO_URL = "https://github.com/Mally-cj/zhangxiaojun-archives"
SOURCE_BLOB_BASE = SOURCE_REPO_URL + "/blob/main/"
ACCOUNT_LINK_REPO = "[[accounts/zhang-xiaojun|Zhang Xiaojun Podcast]]"
ACCOUNT_NAME = "Zhang Xiaojun Podcast"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repo", type=Path, required=True)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--vault", type=Path, default=Path("/Users/rydersun/Documents/Obsidian Vault"))
    parser.add_argument("--report-date", default=TODAY)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def yaml_text(metadata: dict) -> str:
    return "---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False, width=1000).strip() + "\n---\n"


def clean(value: object) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def sanitize_filename(value: str, limit: int = 150) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"[/:*?\"<>|]", " ", value)
    value = re.sub(r"\s+", " ", value).strip().rstrip(".")
    return value[:limit].rstrip() or "未命名"


def episode_id(path: Path) -> str:
    match = re.match(r"(\d{3})", path.name)
    if not match:
        raise ValueError(f"cannot parse episode number: {path}")
    return match.group(1)


def source_blob_url(rel_path: str) -> str:
    return SOURCE_BLOB_BASE + "/".join(quote(part) for part in rel_path.split("/"))


def parse_source_file(path: Path, source_repo: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="replace").strip()
    lines = raw.splitlines()
    episode = episode_id(path)
    title = clean(lines[0]).removesuffix("_原文")
    published_raw = clean(lines[1]) if len(lines) > 1 else ""
    published_match = re.search(r"(\d{4})年(\d{2})月(\d{2})日", published_raw)
    published = "-".join(published_match.groups()) if published_match else ""
    rel_path = path.relative_to(source_repo).as_posix()
    source_id = f"zhangxiaojun-ep-{episode}"
    stem = f"{sanitize_filename(title)} [{source_id}]"
    return {
        "episode": episode,
        "source_id": source_id,
        "title": title,
        "published": published,
        "published_raw": published_raw,
        "source_path": rel_path,
        "source_url": source_blob_url(rel_path),
        "stem": stem,
        "raw": raw,
    }


def build_transcript(row: dict, analysis_link: str) -> str:
    metadata = {
        "title": row["title"],
        "source": "xiaoyuzhou_archive",
        "source_url": row["source_url"],
        "source_id": row["source_id"],
        "account": ACCOUNT_LINK_REPO,
        "account_name": ACCOUNT_NAME,
        "featured_people": [],
        "published": row["published"],
        "created": TODAY,
        "language": "zh",
        "speaker_attribution": "unattributed",
        "description": "Imported from Mally-cj/zhangxiaojun-archives; original raw text preserved. This archive source has no YouTube video_id.",
        "source_repository": SOURCE_REPO_URL,
        "source_path": row["source_path"],
        "imported_at": TODAY,
        "analysis_report": analysis_link,
        "tags": ["transcript", "kol", "imported", "zhangxiaojun-archives", "podcast-archive"],
        "status": "imported",
    }
    return (
        yaml_text(metadata)
        + f"来源原文：[Mally-cj/zhangxiaojun-archives]({row['source_url']})\n\n"
        + f"对应分析：{analysis_link}\n\n"
        + "## Transcript\n\n"
        + row["raw"].rstrip()
        + "\n"
    )


def build_analysis(row: dict, transcript_link: str, comparison_link: str) -> str:
    metadata = {
        "title": f"{row['title']}",
        "source": "repository_import",
        "source_id": row["source_id"],
        "transcript": transcript_link,
        "source_repository": SOURCE_REPO_URL,
        "source_path": row["source_path"],
        "tags": ["kol情报", "imported", "zhangxiaojun-archives"],
        "status": "imported",
        "created": TODAY,
    }
    lines = [
        yaml_text(metadata).rstrip(),
        "",
        f"对应逐字稿：{transcript_link}",
        f"来源原文：[Mally-cj/zhangxiaojun-archives]({row['source_url']})",
        f"稳定来源 ID：`{row['source_id']}`",
        "",
        "## 来源说明",
        "",
        "本文件由 `Mally-cj/zhangxiaojun-archives` 的公开原文归档生成。源文件没有 YouTube video_id，因此本库按节目期号 `source_id` 管理，不按标题覆盖已有 YouTube 版本。",
        "",
        "## 主题线索",
        "",
        f"- 标题：{row['title']}",
        f"- 原文时间：{row['published_raw'] or row['published'] or '未标注'}",
        "- 来源属性：播客/访谈原文归档，非本地浏览器插件 canonical 捕获。",
        "",
        "## 后续复核",
        "",
        "- 若后续需要 canonical YouTube 逐字稿，应使用 Obsidian 浏览器插件重新捕获对应视频来源。",
        "- 若仅做张小珺商业访谈录的主题图谱，本文件可作为公开归档来源参与检索和关联。",
        "",
        "## 深度关联",
        "",
        f"- 三方语料层关联：{comparison_link}",
    ]
    return "\n".join(lines).rstrip() + "\n"


def write_if_missing(path: Path, text: str, dry_run: bool) -> bool:
    if path.exists():
        return False
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return True


def comparison_report(rows: list[dict], comparison_stem: str, vault_mode: bool) -> str:
    latest = max((row["published"] for row in rows if row["published"]), default="未知")
    lines = [
        "---",
        f"title: \"三方 KOL 语料库对比（{TODAY}）\"",
        "source: repository_audit",
        f"created: {TODAY}",
        "tags:",
        "  - kol情报",
        "  - repository-audit",
        "  - zhangxiaojun-archives",
        "status: canonical",
        "---",
        "",
        "# 三方 KOL 语料库对比",
        "",
        "## 结论",
        "",
        f"`Mally-cj/zhangxiaojun-archives` 提供 **{len(rows)} 份张小珺商业访谈录原文**，覆盖第 {min(row['episode'] for row in rows)} 到第 {max(row['episode'] for row in rows)} 期中的 16 个节目。它没有 YouTube video_id，因此已按 `zhangxiaojun-ep-xxx` source_id 作为独立来源变体导入。",
        "",
        "它补的是张小珺播客原文侧的覆盖面，而不是和 YouTube 版本互相替代。已有 YouTube 逐字稿继续保留原视频 ID；同一期节目若同时存在 YouTube 版本和原文归档版本，知识图谱中保留为不同来源。",
        "",
        "## 可复现口径",
        "",
        "| 来源 | 文件/记录 | 主键 | 最新原文时间 |",
        "|---|---:|---|---:|",
        f"| Mally-cj/zhangxiaojun-archives | {len(rows)} | `source_id` | {latest} |",
        "| nolimitkun/ai-kol-wiki | 81 | YouTube video_id | 2026-08-09 |",
        "| Ryder-MHumble/Youtube-KOL-Transcripts | 207+ | YouTube video_id / source_id | 2026-08-09 |",
        "",
        "## 本次导入清单",
        "",
    ]
    for row in sorted(rows, key=lambda item: item["episode"]):
        analysis_stem = f"{row['stem']} 分析" if vault_mode else f"analysis/{row['stem']} 分析"
        lines.append(f"- [[{analysis_stem}|{row['title']}]] · `{row['source_id']}` · {row['published'] or '未标注'}")
    lines.extend(
        [
            "",
            "## 运行边界",
            "",
            "本次读取的是公开 GitHub 归档原文，不是通过 YouTube 或 Obsidian 浏览器插件重新抓取。所有导入文件均标记为 `status: imported`，后续如需 canonical 逐字稿，应单独复核来源。",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def update_moc(vault: Path, comparison_stem: str, created: int, dry_run: bool) -> None:
    moc = vault / "KOL情报" / "KOL情报 MOC.md"
    marker = "## 张小珺原文"
    if dry_run:
        return
    moc.parent.mkdir(parents=True, exist_ok=True)
    moc_text = moc.read_text(encoding="utf-8") if moc.exists() else "# KOL情报 MOC\n"
    if marker in moc_text:
        return
    block = [
        "",
        f"{marker}（{TODAY}）",
        "",
        f"- [[{comparison_stem}]]：Mally-cj 张小珺原文归档的 source_id 口径、导入清单和边界说明。",
        f"- 本次新增 {created} 个文件（逐字稿与分析合计），均标记为 `status: imported`。",
    ]
    moc.write_text(moc_text.rstrip() + "\n" + "\n".join(block) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    source_repo = args.source_repo.resolve()
    repo = args.repo.resolve()
    vault = args.vault.resolve()
    rows = [parse_source_file(path, source_repo) for path in sorted((source_repo / "原文").glob("*.md"))]
    comparison_stem = f"KOL语料库三方对比-{args.report_date}"

    created_repo = 0
    created_vault = 0
    for row in rows:
        repo_transcript = repo / "transcripts" / "zhang-xiaojun" / f"{row['stem']}.md"
        repo_analysis_stem = f"{row['stem']} 分析"
        repo_analysis = repo / "analysis" / f"{repo_analysis_stem}.md"
        repo_transcript_link = f"[[transcripts/zhang-xiaojun/{row['stem']}|{row['title']}]]"
        repo_analysis_link = f"[[analysis/{repo_analysis_stem}|{row['title']} 分析]]"
        repo_comparison_link = f"[[deep-reports/{comparison_stem}|{comparison_stem}]]"

        if write_if_missing(repo_transcript, build_transcript(row, repo_analysis_link), args.dry_run):
            created_repo += 1
        if write_if_missing(repo_analysis, build_analysis(row, repo_transcript_link, repo_comparison_link), args.dry_run):
            created_repo += 1

        vault_transcript_stem = f"{row['stem']}"
        vault_analysis_stem = f"{vault_transcript_stem} 分析"
        vault_transcript = vault / "KOL逐字稿" / f"{vault_transcript_stem}.md"
        vault_analysis = vault / "KOL情报" / f"{vault_analysis_stem}.md"
        vault_transcript_link = f"[[{vault_transcript_stem}]]"
        vault_analysis_link = f"[[{vault_analysis_stem}]]"
        vault_comparison_link = f"[[{comparison_stem}]]"
        if write_if_missing(vault_transcript, build_transcript(row, vault_analysis_link), args.dry_run):
            created_vault += 1
        if write_if_missing(vault_analysis, build_analysis(row, vault_transcript_link, vault_comparison_link), args.dry_run):
            created_vault += 1

    manifest = {
        "generated_at": TODAY,
        "source_repository": SOURCE_REPO_URL,
        "source_files": len(rows),
        "source_ids": [row["source_id"] for row in rows],
        "created_repo_files": created_repo,
        "created_vault_files": created_vault,
    }
    if not args.dry_run:
        (repo / "deep-reports").mkdir(parents=True, exist_ok=True)
        (repo / "deep-reports" / f"{comparison_stem}.md").write_text(comparison_report(rows, comparison_stem, vault_mode=False), encoding="utf-8")
        (repo / "deep-reports" / f"{comparison_stem}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (vault / "KOL情报").mkdir(parents=True, exist_ok=True)
        (vault / "KOL情报" / f"{comparison_stem}.md").write_text(comparison_report(rows, comparison_stem, vault_mode=True), encoding="utf-8")
        update_moc(vault, comparison_stem, created_vault, args.dry_run)

    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
