---
title: 'Cooking with OpenAI’s Research Chief: AGI, o1, Evals, and Scaling Laws — Mark Chen（外部迁移分析）'
source: repository_import
youtube_url: https://www.youtube.com/watch?v=fpAthTtha8c
video_id: fpAthTtha8c
transcript: '[[Cooking with OpenAI’s Research Chief AGI, o1, Evals, and Scaling Laws — Mark Chen [fpAthTtha8c]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260625-latent-space-mark-chen.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Cooking with OpenAI’s Research Chief AGI, o1, Evals, and Scaling Laws — Mark Chen [fpAthTtha8c]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=fpAthTtha8c) · 视频 ID：`fpAthTtha8c`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260625-latent-space-mark-chen.md)

## 迁移说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 边做韩式豆腐汤边聊的轻松格式（灵感来自 Zuckerberg "带汤挖人"的传闻），但研究内容扎实。

## 概要

OpenAI 首席研究官谈 scaling laws 信念、pre-training 未死、reasoning/o1 这个 bet 的由来、评估危机与 bench maxing、研究品味与组织方法、以及"vibe researcher"的未来。

## 核心观点

### Scaling laws 与"pre-training 未死"
- **坚信 exponential 与 scaling laws**，强烈反对各种 bear takes。"pre-training is dead"这个叙事在 LLM 历史上反复出现，每次都有人说"因为某个瓶颈无法再 scale"，但总能靠更细的研究/数据/工程工程突破——已 hold 了近 **10 个数量级**，"没理由不继续"（[00:08:06]–[00:10:08]、[00:37:25]–[00:38:26]）。
- Reasoning / **o1** 是"曾被质疑最终成立"的最大 bet：当时 pre-training + post-training 是舒适范式，"有能用的机器为何要另起炉灶"；靠 Yakub、Ilya 等人的 conviction 才把全公司推上这条路（[00:09:07]–[00:11:08]）。

### 评估危机与 bench maxing
- **evals crisis**：canonical gold-standard benchmark 太少，SAT 等经典基准都已 saturate。**bench maxing**（找与 benchmark 极像的实例过训）会让泛化失真（[00:19:13]–[00:20:13]）。
- 解法：始终在有代表性的 eval 混合上评估、持续造新 eval（"一个 eval 一旦公开就已不是好 eval"）；**把造 eval 的团队与优化模型的团队分开**，形成对抗、避免自欺；与外部组织合作打造 gold standard（[00:21:14]–[00:23:15]）。
- 工具如 **Codex** 让一个人快速产出高质量 eval；部署本身也是一种 eval（从真实使用中看模型在哪里 fall over）（[00:20:13]–[00:21:14]）。

### Jagged frontier、context 与 continual learning
- 模型能解 IMO/IOI 却在平凡任务上翻车："对模型直觉的东西对人类不直觉"（jagged frontier）；很多归结为 **context**——模型缺乏把单任务教训迁移到未来任务的能力（人类天然会）（[00:24:16]–[00:25:16]）。
- 长 context："实现 long context"与"实现得好"不同；除 naive 增窗外可用 **compaction** 等工程/研究捷径压缩工作状态（[00:25:16]–[00:26:16]）。**continual learning 是必须解锁的 basic primitive**，不确定算不算"breakthrough"，但"there are many shots on goal, I'm pretty sure they'll work"（[00:29:18]）。

### 研究品味与组织方法
- research taste 有点被高估但可培养，**最好的机制是 replication**（完整复现你敬佩的论文、逼近其训练曲线）；trader 背景有用是因为交易"unhackable"、注重细节（[00:02:03]–[00:04:04]、[00:15:13]–[00:16:13]）。
- 高层 research roadmap 应稳定（给人 grounding），但 implementation/排序/资源分配随时间变；compute 分配是强制重估的节点（[00:12:09]–[00:13:10]）。
- 每 1–2 月过约 **300 个项目**；做法是聚焦——每个 org 3–5 个大 bet 进主 roadmap，用 directive compute allocation + flexible pools，不微观管理 manager（[00:14:12]–[00:15:13]）。
- **高风险 bet 是 OpenAI 的 alpha**：有些不会 pan out，但失败的 write-up 也很重要（能让别人少走弯路）；肯冒险者"只要偶尔命中一次就值得"（[00:34:23]–[00:36:25]、00:46–00:48）。

### Vibe researcher 与多模态
- 工作正快速转向 **orchestration-focused**：研究员出 idea、模型做执行；三年 roadmap 终点是模型端到端做研究——但"教模型 taste 很难"，所以现在仍需研究员出 idea（[00:32:20]–[00:33:22]、00:45–00:46）。
- 倾向**单一多模态模型**（图像/音频/视频/文本），因为维护一套 infra stack 的优势不可低估（[00:31:19]–[00:32:20]）。
- 被高估/低估：若还持"pre-training is dead"观点，那 pre-training 被低估；把研究 primitive 连到真实 agentic use case 的"产品/端到端思考"也被低估（[00:37:25]–[00:38:26]、00:49–00:50）。

## 相关主题

- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（scaling laws、reasoning/o1）
- [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)（evals crisis、bench maxing、分离评估团队）
- [LLM 心理学与认知短板](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-psychology.md)（jagged frontier、continual learning）
- [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md)（OpenAI 研究文化、高风险 bet）

## 深度关联

- 语料层关联：[[KOL语料库对比与迁移评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。
