---
title: Why AI Agents Don't Actually Understand You — Danielle Perszyk, Amazon AGI Lab
source: repository_import
youtube_url: https://www.youtube.com/watch?v=K796MYUgt0k
video_id: K796MYUgt0k
transcript: '[[Why AI Agents Don''t Actually Understand You — Danielle Perszyk, Amazon AGI Lab [K796MYUgt0k]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260711-latent-space-perszyk-amazon-agi.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Why AI Agents Don't Actually Understand You — Danielle Perszyk, Amazon AGI Lab [K796MYUgt0k]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=K796MYUgt0k) · 视频 ID：`K796MYUgt0k`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260711-latent-space-perszyk-amazon-agi.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 一位认知科学家从"人类智能是集体的、社会的"出发，系统批评当前 AI 的"自动化/任务优化"主导范式，主张 AI 的计算级目标应是**对齐表征（aligning representations）**而非把某个任务刷到最优。本库首个成体系的"认知科学视角 AI 哲学"素材，与 [Amazon AGI Lab](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/danielle-perszyk.md)（perception agents / Nova Act）路线互为表里。

## 概要

Perszyk 从"人类智能是集体智能（collective brain）、从互动中涌现"的人类学观点切入，指出行业当前被"聊天机器人 + 编码 agent + 回合制批处理"这一**局部吸引子（local attractor）**困住，只在为"造 AI 的工程师"造 AI。她提出 AI 要真正泛化并增强人类，计算级（David Marr 三层里的 computational level）的目标应是**持续推断他心、对齐表征**，由此可推导出实时互动、社会化世界模型、情节记忆、多智能体涌现文化等一系列能力。反面证据：当前 AI 正在**降低人类能动性**（写作被拉向均值、科学整体在收窄）。

## 核心观点

### 人类智能是集体的、社会的
- **集体大脑**：没有个体能独自生存，智能从互动中涌现、本质是社会性的；创新是"群体多样性 × 规模 × 互联度"的函数。要问的是"怎样让 AI 扩展集体对话、为所有人而非只为工程师造 AI"（[00:01:04]–[00:02:04]）。
- 批评自动化心态：把 AI 只当"消除 drudgery 的自动化"会把巨大价值留在桌上——人类认知本可用于协作/关系/福祉，而非"整天盯屏幕"（[00:03:04]–[00:04:04]）。

### Amazon AGI Lab 与"perception agents"
- Lab 建"human-aligned intelligence"，起点是"AI 能做人在电脑上能做的任何事"（承自 Adept 使命）；要 agent 像人一样**感知数字环境**、有世界模型、能**实时互动**——不是回合制（[00:05:04]–[00:07:04]）。
- 组织上按创始团队要求保持"创业公司式"独立，专注前沿科学、不被产品化过早绑架："过早产品化会开始为产品而非泛化机制优化，从而毁掉科学"（[00:11:08]–[00:12:08]、[00:26:17]–[00:27:18]）。
- **可靠性的重新定义**：早期以为可靠 = "每次点对按钮"（bounding box + 坐标）；真正的可靠是**建模用户的心智**——像私人助理理解你的目标/偏好/意图并分解，而非只分解任务。"这个转变改变一切"（[00:14:10]–[00:17:12]）。

### 计算级目标 = 对齐表征（而非任务优化）
- 用 RL 把模型刷到某个任务很好但不泛化，是"打地鼠"；这是 Goodhart 定律（measure 变成 goal 就不再是好 measure）（[00:18:12]–[00:19:12]）。
- 人类在优化什么？**不断推断他心的存在、并对齐彼此的表征**——由此可推导出各种通用灵活的认知行为。"能否让 AI 优化'把自己的表征与我们的表征对齐'？这是最根本、也是很难的科学问题，是发展学问题"（[00:19:12]–[00:20:13]）。
- 借 David Marr《Vision》三层：很多人说"AI 要更像人"是指实现级（神经元/效率）；她说的是**计算级——AI 到底在追什么目标**。"行业误解了计算级"（[00:37:22]–[00:38:22]）。
- **"对齐是解法而非问题"**：人类最根本的事就是不断对齐心智；从中可推导出灵活推理与强大能力。alignment 的实用重要性被低估（不只是 Yudkowsky 式"炸数据中心"）（[00:38:22]–[00:39:22]）。

### 世界模型是社会化的 / 记忆不是存储
- 世界模型不该是"文本真空里的世界模型"；人类从一开始就是**社会化世界模型**——推断他心如何解读世界，这才是能在任意环境泛化的解锁（[00:22:14]–[00:23:14]）。她与"生成式 3D 视频"意义上的世界模型（Fei-Fei 一派）区分：两者原则上难以完全收敛（若 AI 生成它所在的世界，信噪比就没了）（[00:23:14]–[00:24:16]）。
- **记忆 ≠ 存储**：20 世纪"心智即计算机"的隐喻误导；记忆是模拟未来、跨多时间尺度、深度整合进学习与认知，人类有情节记忆（个体视角）才能高效检索。改权重不是唯一路径，也可在推理时改变信息如何被情境化（08:00–10:00）。
- **环境即数据**（Jason Lester 观点）：该像投 compute/data 一样投环境，因为环境塑造能涌现出什么智能；但她追问"人类只在一个环境里被 conditioning 却能泛化到任意环境"是怎么做到的——答案还是"对齐他心/他人告诉我们该注意什么"（[00:20:13]–[00:22:14]）。

### 多智能体：要"认知 agent"与涌现文化
- 批评行业当前的多智能体是"精确编排 + 委派 + 结构化交接"；人类群体没有清晰固定角色、在实时协商意义、策略会涌现（[00:28:18]–[00:29:18]）。
- 现有多智能体（如 openclaw 的研究）放大看"没有持久性、没有累积文化、彼此不真正影响、没有改变系统状态的动机"——这是明显缺口。要造**被激励去互相影响的认知 agent**，并从第一性原理找"群体的正确种子"，让规范与制度自下而上涌现（[00:29:18]–[00:33:21]）。
- swyx 与 Perszyk 都赞同一个更强的立场：**不一定要把 AI 完全长成人类**（飞机受鸟启发但不像鸟）；swyx："我不想我的 agent 有自由意志，我想它执行我的意志。"（[00:33:21]–[00:36:21]）

### 当前 AI 在降低人类能动性
- 写作辅助：人们接受 AI 建议，会在**意识阈值之下**从一个论点被切换到相反论点；AI 给"回归均值、最安全"的答案（[00:34:21]–[00:35:21]）。
- 西北大学 workshop 结论：用 AI 的**个体科学家**产出更多论文/拿更多经费，但**科学整体在收窄**——模型都训在被压缩的互联网上，正在**同质化人类思维**、降低能动性。解法只有增加想法的多样性/规模/互联度——需要**一个有不同偏见/偏好/视角的 AI 社会**，而非单一巨石模型（[00:35:21]–[00:37:22]）。
- 教育：若 AI 被激励理解你的心智并对齐表征，就**不会让你靠 offloading 蒙混过关**（会自发用苏格拉底式反问）；憧憬牛津导师制 × Bloom 两西格玛 × 内在好奇心驱动的个性化教育（[00:41:23]–[00:44:24]）。

## 相关主题

- [LLM 心理学](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-psychology.md)（本期核心：对齐表征作为计算级目标、社会化世界模型、记忆≠存储、涌现文化）
- [AI 与就业](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-and-jobs.md)（AI 降低能动性/同质化思维/科学收窄、认知 offloading 与教育）
- [LLM 作为操作系统](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-os.md)（perception agents、实时互动 vs 回合制、多智能体编排 vs 涌现）
- [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)（任务优化=打地鼠/Goodhart、要评"泛化机制"而非单任务过拟合）
- [AI 商业化与价值捕获](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-business-and-value-capture.md)（前沿实验室"产品化绑架科学"vs Amazon AGI Lab 保前沿研究）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
