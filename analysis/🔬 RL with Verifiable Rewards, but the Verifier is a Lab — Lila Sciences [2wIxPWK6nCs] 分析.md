---
title: 🔬 RL with Verifiable Rewards, but the Verifier is a Lab — Lila Sciences
source: repository_import
youtube_url: https://www.youtube.com/watch?v=2wIxPWK6nCs
video_id: 2wIxPWK6nCs
transcript: '[[🔬 RL with Verifiable Rewards, but the Verifier is a Lab — Lila Sciences [2wIxPWK6nCs]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260716-latent-space-lila-sciences.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[🔬 RL with Verifiable Rewards, but the Verifier is a Lab — Lila Sciences [2wIxPWK6nCs]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=2wIxPWK6nCs) · 视频 ID：`2wIxPWK6nCs`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260716-latent-space-lila-sciences.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

## 概要

本库迄今最系统的一期"AI for science"素材。Lila 的核心命题：**互联网数据已被"压榨"殆尽（Ilya："我们只有一个互联网，它是化石燃料"），下一个互联网级数据源是科学本身**——用"跑科学方法、以自然/实验做 verifier"来做大规模 post-training。他们把物理实验室建成"AI Science Factory"（科学工厂）= 大规模 verifier，产出"实验验证过的推理轨迹"这种互联网上"约等于零"的数据。横跨生命科学、化学、材料，不只是 tech bio。

## 核心观点

### 命题：科学是"无限 token 生成器"，为数据加一根新 scaling 轴
- 全面押注 **bitter lesson + scale**：可规模化、通用的方法胜过不可规模化的（这与 AI 70 年历史的直觉相反）（[00:05:10]–[00:06:11]）。
- RL 的本质是"模型自己生成数据、reward 信号强化好数据/惩罚坏数据"；在数学/编码已很有效。**Lila 认为"以实验/自然做 verifier"是这一框架的终极版本**——AI Science Factory 就是"可规模化的科学 verifier"（[00:06:11]–[00:07:12]）。
- 关键技术难点：不同实验反馈时间尺度差几个数量级（生物按天/周、材料化学更快），要 multiplex、把不同尺度的数据在训练侧对齐（[00:07:12]–[00:08:16]）。

### 实验室即 data center：PCI 总线、96 孔板、人在 API line 之下
- 实验室是一张图：每台仪器是节点、节点间有物理传输层（planar motor 平面电机让 96 孔板磁悬浮移动）——**"实验室的 PCI 总线"**（[00:10:19]–[00:11:20]）。
- **一切都是 API call**：有时接机械臂、有时接人手——**"人在 API line 之下"**；不做"自动化最大化"，而是"token 生成/灵活性最大化"，优先通用性而非吞吐（拔试管盖很难自动化，"实验室假设你有对生拇指且好用"）（[00:11:20]–[00:13:25]）。
- 给模型控制实验室倒逼你把平时不 care 的数据全暴露出来（如湿度），从而能解释输出方差、并一键重跑验证（[00:20:42]–[00:21:43]）。仍有大量硬骨头：自写 driver/firmware（"全球最大的作废保修单收藏"）、甚至用 **VLM 控制 Windows 95 机器**、机械手指按 iPad（[01:03:07]–[01:05:09]）。

### 10 万亿科学 token：广度带来深度
- 组装了 **10T 实验验证的科学推理 token**（跨生命科学/化学/材料，是 English + tool call + 实验反馈的"准英文" token，不是把 DNA/PDB 直接 tokenize）；预训练语料通常 15–30T，进入万亿区间才见 emergent（[01:18:17]–[01:20:20]）。
- 不做预训练——用"约 10 亿美元算力等价的 open-weight 模型"（NVIDIA/Nemotron 合作）做 base camp，在其上叠 10T（[01:20:20]–[01:21:22]）。
- **"广度带来深度"**：通用模型常胜过领域专用模型；如小分子药物学到的化学迁移去推理 MOF/COF 材料（吸 CO2）。"实验验证的推理轨迹"在互联网上 order-of-zero，一展示给模型就立刻见提升，哪怕参数处于劣势（[00:32:04]–[00:33:08]、[01:22:25]–[01:23:29]）。
- chain of thought 里既有推理也有 tool call，**实验室仪器就是 tool call、全英文可读**；病态：跳过实验直接给答案、重复坍缩（不算严格 reward hacking，但物理科学的 reward hacking 是真实担忧）（[00:24:47]–[00:27:55]）。

### 科学示例：材料与生物用同一平台
- **绿氢电催化剂**：找非铂族（避开 ruthenium/iridium）催化剂降 overpotential；模型给的建议从"无聊"到专家（发过 40 篇该主题论文）眼里的"愚蠢"，结果是他们**至今最好的非铂族催化剂**——"move 37"式惊喜（[00:17:33]–[00:18:37]、[00:22:44]–[00:23:46]）。
- 量子点（QD）：控制纳米尺寸出纯色，访客选波长、参观一圈就做出命中该颜色的量子点；同一 liquid handler 改造而来。还做 thin films、magnetron sputtering、MOF/COF、formulation（混"黏糊糊的东西"——润滑剂/LNP/凝胶/护肤，被低估的通用平台）（[00:35:11]–[00:41:19]）。
- **in vivo CAR-T**：把 binder 设计 + LNP formulation + mRNA 设计三块合起来；做出比 Capstan（被 AbbVie 21 亿美元收购）更好的 NHP B 细胞清除数据；关键是**怪兽级 UTR 把表达量做到 Moderna/Pfizer 参考序列约 10x**；2–3 人 6 个月做到接近 IND，≈5 年生物技术工作、10% 成本（[00:44:25]–[00:49:35]）。

### 商业模式：模型本身是价值（neo-lab）、"零 FTE 虚拟创业"
- **模型本身才是 moat**，实验室平台是 token 生成器/数据护城河——是"neo-lab"而非 biotech，不冲临床（[00:27:55]–[00:28:56]）。
- 回应"若你有数据训模型、有了数据又何必模型"：narrow scope 下成立，但通用平台下**领域数据需求随广度下降、相邻领域可降到零**（[00:28:56]–[00:29:58]、[00:40:18]–[00:41:19]）。
- 商业形态是**"零 FTE 虚拟创业"**：客户带一个明确问题，在 Lila 上跑完整个 program（平台接入费+试剂+分成），可从数十个扩到成千上万个并行虚拟创业（[00:49:35]–[00:51:40]）。
- "科学家还在用二进制编程"——有问题却要手动 compile 成实验协议、搬液体搬到得关节炎；Lila 是"科学版 Claude Code"，帮科学家上抽象阶梯、快速失败（[00:51:40]–[00:52:44]）。

### 尺度、评估、瓶颈
- "材料里 scaling 是**又苦又甜**"——只有能规模化的东西才 matter，所以从第一个实验就 supply-chain conscious、有 techno-economic agent 蹲在角落（[00:42:19]–[00:43:21]、[00:52:44]–[00:54:50]）。
- 内部有约 **1000 个科学 RL environment** 的测试套件（可 drop-in frontier model 对比），会开源一个子集 + 部分数据；每个 close-ended 问题都有内部 benchmark（科学预训练+tool call 的模型"碾压"其他做法）（[00:21:43]–[00:22:44]、[01:21:22]–[01:22:25]）。
- Ken Stanley 领 **open-endedness（机器创造力）** 团队做 outer loop——"只会考试的不是超级智能，得会提出有趣的问题"（[00:59:00]–[01:01:01]）。
- 迭代速度 > 大规模高噪并行；pooled（DNA-encoded library、"一切 value tech 都是把读出映射到 NGS"）"又快又广"最爱；把 MOF 吸附测量从 BET 一天/样本改成 96 孔板/小时、约 2500x（[01:09:13]–[01:13:14]）。
- **瓶颈许愿**：Rafa 要"物理仿真的 sim-to-real"（"材料没有 AlphaFold"，而 AlphaFold 恰是训在实验而非仿真上）；Andy 要把 **RL 的 MFU 从 5–6% 拉到 100%**（省 GPU 转投实验室），并主张把 RL 训练"因式分解"成并行专家模型再蒸馏回中心模型（[01:35:44]–[01:39:49]）。
- 中美对照：**"美国生物技术输给中国生物技术不是创新问题，是监管框架"**；材料创新很大程度由政府/国家安全驱动（与英美政府有合作、参与 Mission Genesis）（[00:53:49]–[00:54:50]、[01:34:42]–[01:35:44]）。

## 相关主题

- [AI 与科学发现](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-for-science.md)（本期核心：科学即 token 生成器、实验室即 verifier、广度带来深度）
- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（RLVR 扩展到物理 verifier、reward hacking、蒸馏并行专家、MFU、从 open-weight 起步）
- [AI 商业化与价值捕获](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-business-and-value-capture.md)（模型即价值/neo-lab、零 FTE 虚拟创业、材料"苦甜 scaling"）
- [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)（1000 个科学 RL environment、内部实验对照）
- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（美生物技术输在监管而非创新）
- [AI 与就业](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-and-jobs.md)（"人在 API line 之下"、零 FTE 创业）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
