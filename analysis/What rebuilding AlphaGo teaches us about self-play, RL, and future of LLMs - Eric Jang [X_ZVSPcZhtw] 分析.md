---
title: What rebuilding AlphaGo teaches us about self-play, RL, and future of LLMs - Eric Jang
source: repository_import
youtube_url: https://www.youtube.com/watch?v=X_ZVSPcZhtw
video_id: X_ZVSPcZhtw
transcript: '[[What rebuilding AlphaGo teaches us about self-play, RL, and future of LLMs - Eric Jang [X_ZVSPcZhtw]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260515-dwarkesh-eric-jang.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[What rebuilding AlphaGo teaches us about self-play, RL, and future of LLMs - Eric Jang [X_ZVSPcZhtw]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=X_ZVSPcZhtw) · 视频 ID：`X_ZVSPcZhtw`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260515-dwarkesh-eric-jang.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 这是一期"黑板课"式深度技术访谈：Eric 在 sabbatical 期间用约 $10K 租用算力从零重建了一个强 Go bot（AutoGo），借此系统对比 AlphaGo 的 MCTS self-play 与今天 LLM 的 RL，为"AI 自动化 AI 研究"提供一线观察。转录稿前 3/4 是 AlphaGo/MCTS 的逐步推导，本页聚焦其可迁移的判断。

## 概要

AlphaGo 的核心突破：用神经网络（value + policy 双头）把 Go 那棵 361³⁰⁰ 量级、被认为本世纪不可解的搜索树同时在**深度**（value 函数截断到底搜索）与**广度**（policy 剪枝）上压到可解。**MCTS 作为 policy 的"改进算子"**：搜索出比当前策略更好的动作分布，再把它蒸馏回 policy 网络（"把 TPU pod 的算力压进一次前向传播"）。Eric 由此反观 LLM 的 RL，指出两者在样本效率上的巨大差异。

## 核心观点

### 为什么 LLM 的 RL 效率极低（本期最有价值的对比）
- **MCTS 给每一步都提供监督目标**（低方差）；LLM 的 policy-gradient RL 则是把整条获胜轨迹的所有 token 一起上调——Karpathy 所谓"**用吸管吸取监督信号**（sucking supervision through a straw）"，一整局只有极少数"真正更好的"动作是有效信号，其余是噪声（[01:24:36]–[01:27:58]、[01:45:50]–[01:46:50]）。
- **bits per FLOP 框架**：学习速度 = 每 FLOP 样本数 × 每样本比特数。① 长程 RL 让**每 FLOP 样本数下降**（要展开两天的工作才拿到一个信号）；② 每样本比特数也远逊于监督学习——未训练模型要在 10 万词表里靠瞎猜撞到 "blue" 约 10 万次才有一次信号，而绝大部分训练时间耗在"低通过率区"几乎学不到东西（[02:12:10]–[02:17:29]）。
- **AlphaGo 的优雅在于永远不用从 0% 成功率起步、不用解探索难题**：全程是"在改进后的标签上做监督学习"，训练稳定、无需复杂的 on-policy 分布式基础设施（[02:19:33]–[02:21:40]）。
- **软标签/蒸馏为何高效**：AlphaGo 训 policy 去模仿 MCTS 的**整个分布**而非单一动作，soft target 的熵远高于 one-hot，每样本携带的信息多得多——这也解释了蒸馏的威力（[02:18:30]–[02:19:33]）。呼应 [姚顺宇](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/yao-shunyu.md) 关于"软蒸/硬蒸"的讨论（见 [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)）。

### 前向搜索（MCTS）为何难迁移到 LLM 推理
- Go 里 MCTS 好用靠两个前提：value 可被具体估计（截断深度）、动作集离散有限（PUCT 剪枝广度）。**语言的动作空间过大**——多步思考几乎不会两次采样到同一"子节点"，PUCT 的 √N/(1+Nₐ) 探索启发式失效（[01:44:50]–[01:49:58]）。
- LLM 其实"原生"就会做类似 MCTS 的事（尝试→发现不行→回溯），无需显式树；但"用前向搜索模拟未来以判断价值"的思路**未来可能以别的形态回归**（[01:47:57]–[01:49:58]）。

### test-time compute 早在 2021 年就被预示
- Andy Jones《Scaling Scaling Laws with Board Games》(2021) 证明：**可用更多搜索（MCTS sims）换取更少训练算力**，等效性能——提前预示了后来 LLM 的 inference scaling；还能预测"解更大棋盘需要多少算力"（[01:51:03]–[01:52:08]）。可与 [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)、[LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md) 的 test-time compute 讨论对照。

### 摊销搜索、P vs NP 与"混沌的可预测宏观结构"
- 一个 10 层网络能把近乎 NP 难的搜索**摊销进一次前向传播**（AlphaGo/AlphaFold 同理），令他怀疑"我们用最坏情况复杂度来框定 NP 难问题"的思路不完整——现实问题大多有结构（[01:16:04]–[01:19:20]）。
- 类比天气：混沌系统对初值极敏感，但我们真正关心的是**宏观结构**（飓风在哪、Lorenz 吸引子的形状），而非微观态——value 函数正是在预测这种宏观量（[01:19:20]–[01:22:28]）。

### AI 自动化 AI 研究的一线观察
- Opus 4.6/4.7 **擅长**：开放式超参优化（不止 grid search，能"发现某层梯度小就改架构/加数据增强"）、端到端执行实验（他写了个叫 Experiment 的 Claude Skill，描述 x/y 轴即自动跑实验、出图、写报告）（[02:22:41]–[02:24:47]）。
- **不擅长**：选"下一个该做的实验"、做横向/第一性原理的退一步思考；infra bug 常要他自己 prompt 引导才被发现（[02:24:47]–[02:25:50]）。引 Ilya 的话：好研究员的关键是**对"正确想法"的强信念**，从而能分辨"是 bug 还是想法本身错了"（[02:28:57]）。与 [Mark Chen](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/mark-chen.md) 的 vibe researcher、[Noam Brown](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/noam-brown.md) 的"research taste 是当前短板"、[Gray Swan](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/gray-swan-founders.md) 的"用 agent 自动化科学"同题（见 [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)、[AI 与科学发现](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-for-science.md)）。
- 用 Go 这类**快速可验证**的游戏作为训练"自动化科学家"的外循环，再迁移到生物/机器人/AI 研究本身（[02:26:51]、[02:33:07]–[02:34:11]）。

### 抢先 vs 追赶、Bitter Lesson 的暂时性
- **抢先做成一件事所需算力，远大于追赶所需**：AlphaGo Zero 当年是算力曲线上的巨大异常（3E23 FLOPS），而今 $10K 即可复现——和 LLM 里"别人做出来后可用蒸馏等捷径追赶"是同一个故事（[01:55:16]–[01:56:18]）。呼应 [姚顺宇](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/yao-shunyu.md) 的中国实验室蒸馏追赶论。
- **compute multiplier 是暂时的、且不叠加**：KataGo 的诸多算法技巧在 Blackwell GPU 上大多不再重要；好想法之间常有"诡异的负交互"（传闻某些 lab 训练失败正因两个各自不错的想法凑一起坏了），故需要**自上而下的统一技术愿景**（[02:31:03]–[02:32:03]、02:54）。呼应 [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md) 里的 top-down 讨论。
- Google/DeepMind 的**游戏基因**（Atari/Go/StarCraft）大概率对做 LLM 有正迁移，但也可能把它们绑在旧范式上；TPU 的长期投入是"短期无用、长期制胜"的赌注——"连人类都难判断最优研究策略"（[02:33:07]–[02:35:14]）。接 [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md) 的 TPU vs GPU。

## 相关主题

- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（RL 的样本效率、MCTS vs policy gradient、蒸馏/软标签、off-policy）
- [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)（test-time vs 训练算力的可换性、自动化研究的可验证外循环）
- [AI 与科学发现](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-for-science.md)（摊销搜索、P vs NP、AI 自动化 AI 研究）
- [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md)（compute multiplier 不叠加、需要 top-down 愿景）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
