---
title: Building an AI Guardian for Enterprise with Onyx Security CEO Maxim Bar Kogan（外部迁移分析）
source: repository_import
youtube_url: https://www.youtube.com/watch?v=QDsbFLEt9ro
video_id: QDsbFLEt9ro
transcript: '[[Building an AI Guardian for Enterprise with Onyx Security CEO Maxim Bar Kogan [QDsbFLEt9ro]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260528-no-priors-onyx-security.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Building an AI Guardian for Enterprise with Onyx Security CEO Maxim Bar Kogan [QDsbFLEt9ro]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=QDsbFLEt9ro) · 视频 ID：`QDsbFLEt9ro`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260528-no-priors-onyx-security.md)

## 迁移说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 一家以色列安全创业公司做"**AI 看管 AI**"：用小而专的模型监督自主 agent 的动作，判断哪些动作可疑到需要更强的 agent 介入。本库首个"agent 安全/治理"公司视角，与 [Gray Swan](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/gray-swan-founders.md)（对抗鲁棒性）、[Databricks](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/databricks-founders.md)（有状态安全策略）互补，落点 [LLM 安全](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-security.md)。

## 概要

Maxim 把赌注押在 **agent 动作（agent actions）** 而非"员工往 ChatGPT 里粘什么"（两年前的 DLP 叙事）。转折点是 AutoGPT 让人看到"模型够强时能做任何人在电脑上能做的事"；如今 Claude Code / co-working / openclaw 这类**很不受限的自主 agent**真的被大企业采用（>50% 的企业 agent 是自主编码 agent，且增长最快），却几乎不带任何控制。Onyx 的两件事：训练能监督其他 agent 的模型 + 产品化为"secure control plane"。关键工程约束是成本/延迟/可靠性——不能给每个 agent 都配一个同等聪明的 agent 看着。

## 核心观点

### 为什么押注 agent 动作
- **AutoGPT 是转折点**：第一个让 LLM"决定做什么"而非"生成文本"、给工具在循环里跑的自主 agent；当时模型不够强（GPT-4 不够）但概念对了，Claude Code 是它的今日版（[00:01:00]–[00:03:01]）。
- 恐惧来自"模型会比我们聪明得多、还去管水电电网时怎么控制"；早期"太早"差点耗尽资金，但市场真的来了——推理模型能做长程任务 + Claude Code 成第一个广泛使用的自主 agent（[00:03:01]–[00:05:03]）。
- 企业里三类：低代码 SaaS"自动化"（约 45%）、自建第一方 agent（约 2%，最难）、**自主编码 agent/助手（>50% 且增长最快）**——CEO 强推 AI，连 openclaw 都被当成合规工具采用（[00:08:06]–[00:09:08]）。

### 传统安全栈为何失灵
- 传统首要控制是**限制权限**（即使被攻破也做不了越权事）；但自主 agent"我们希望它有我们的权限"（好让它替你干活你去吃午饭），身份/权限安全因此失效（[00:10:09]–[00:11:10]）。
- endpoint/API 安全**不知道 agent 在想什么**：Claude Code 删库重建在某任务里是省事的好事，在无关任务里却是灾难——现有工具没有 context 理解"这些灵活、不可预测的系统在做什么"（[00:11:10]–[00:12:12]）。
- 代理 + 策略引擎（proxy + policy engine）不够：proxy 有时技术上不可行（AI 跑在别人云/你的 endpoint 上），且**难点不是看到数据，而是判断该不该做这个动作**——要理解另一个系统在想什么、在计划什么，并对此有自己的判断（[00:12:12]–[00:13:13]）。

### 小而专的"守门模型" + blitz chess 类比
- 天真做法是"让 Claude Code 给每个 agent spawn 一个自己去监控"——成本/延迟直接 dealbreaker（安全供应商比 AI 本身还贵）（[00:14:14]–[00:15:14]）。
- Onyx 训**很小、几乎只会做一件事的模型**：判断"该不该让更聪明的 agent 来看这个动作"；把这种直觉 bake 进小模型，既不漏也不过度调用，就能平衡性能/成本/延迟（[00:15:14]–[00:16:15]）。
- **blitz chess 类比**：顶尖棋手大多数走子靠直觉（见过太多局），偶尔在关键局面停很久深算——高效计算就是"低风险处别花智能、高风险处狠花智能"（[00:16:15]–[00:18:16]）。

### 独立第三方、可解释性与长期定位
- 团队 DNA 是**cyber × AI 混血**（以色列情报单位、数学+网络攻防；联创 Gil 出身 NVIDIA 合成数据）；长期目标不止安全公司，而是"如何长期控制先进 AI"——若 AI 公司是 10 万亿美元公司，你想要一个**非 AI 供应商本身**的独立方来看管它（[00:18:16]–[00:20:17]）。
- 信 **mechanistic interpretability**：理解内部权重/激活的数学结构会是解法一部分；且"当模型比我们聪明后，我们反而能更有效破解 mech interp"（[00:21:17]–[00:23:20]）。
- **数据不对称**是护城河：企业不愿让 Anthropic/OpenAI 保存 agent 历史行为数据（怕被拿去训练），却可以给 Onyx——所以 Onyx 能看历史行为、判断"这次是否偏离常态"，这是模型厂商没有的 context（[00:34:31]–[00:36:32]）。
- 为何 lab 不会自己全包：安全买家**不会信任卖你产品的人认证产品**（买车不会让卖车的人验车）；且世界走向多模型/多供应商（含开源），不现实指望所有厂商都提供同等安全（[00:32:29]–[00:36:32]）。

### Mythos（自动化漏洞挖掘）与分阶段发布
- **Mythos 级模型**（自动化漏洞研究）："10 年前觉得要 20–50 年才有，现在一下子全来了"；市场没有反应过度。务实的安全人要先做最快的补救，再补齐基础（身份锁死、防火墙、endpoint 检测）——为 AI 攻击面也建一套基础安全（[00:25:24]–[00:27:27]）。
- 对 glass swing / daybreak 式**分阶段/受控发布**（Anthropic/OpenAI）：没有强烈立场，但若无人很快放出 Mythos 级模型就好，能给防御方准备时间；风险是"若中国有 Mythos 级模型而你没让企业提早准备，回头看会是巨大错误"——建议**假设这些模型总会来**，现在能做的就是投基础控制（[00:27:27]–[00:28:28]）。
- 金融业更谨慎（限定只允许某几个工具），但**几乎没有全面封禁的 holdout 了**；押注允许多种工具的公司会赢（去年押 OpenAI 最安全，如今 Anthropic 更强）——大公司该有更细致的风险画像（[00:29:28]–[00:31:29]）。
- 最终客户从"人 + 少数 agent"转向"更多 agent"：既优化人的体验（别信息过载），也**优化 agent 的体验**（别浪费 context token）；安全团队本身未来也会被 AI agent 驱动（[00:39:33]–[00:40:34]）。

## 相关主题

- [LLM 安全](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-security.md)（本期核心：agent 动作监督、小守门模型、独立第三方治理、Mythos 自动化漏洞挖掘、数据不对称护城河）
- [AI 商业化与价值捕获](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-business-and-value-capture.md)（"独立方验证"买家心理、为何 lab 不会全包、以色列安全人才 DNA）
- [LLM 作为操作系统](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-os.md)（自主 agent 需要我们的权限→身份安全失效、context 才是判断难点）
- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（"若中国先有 Mythos 级模型"作为分阶段发布的核心变量）

## 深度关联

- 语料层关联：[[KOL语料库对比与迁移评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。
