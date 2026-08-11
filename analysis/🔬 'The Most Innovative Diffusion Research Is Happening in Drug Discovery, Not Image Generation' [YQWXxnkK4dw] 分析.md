---
title: 🔬 'The Most Innovative Diffusion Research Is Happening in Drug Discovery, Not Image Generation'（外部迁移分析）
source: repository_import
youtube_url: https://www.youtube.com/watch?v=YQWXxnkK4dw
video_id: YQWXxnkK4dw
transcript: '[[🔬 ''The Most Innovative Diffusion Research Is Happening in Drug Discovery, Not Image Generation'' [YQWXxnkK4dw]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260630-latent-space-genesis-diffusion-drug-discovery.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[🔬 'The Most Innovative Diffusion Research Is Happening in Drug Discovery, Not Image Generation' [YQWXxnkK4dw]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=YQWXxnkK4dw) · 视频 ID：`YQWXxnkK4dw`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260630-latent-space-genesis-diffusion-drug-discovery.md)

## 迁移说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 本库第二块系统性"AI for science"素材（与 [Lila Sciences](20260716-latent-space-lila-sciences.md) 并置）：一家做**小分子药物发现**基础模型的公司，主题句是"**当下最创新的 diffusion 研究发生在 3D 结构预测，而不是图像/视频生成**"。核心贡献是把 LLM 的 scaling 三段式（预训练/后训练/推理时）搬到分子结构预测，并把精度基准从"业界惯用的 RMSD<2Å"推进到 **1Å 以下**——因为药物发现本质是"分辨率的科学"。

## 概要

Genesis 做 **protein–small molecule（蛋白-小分子）结合**的结构预测，这是十年来最抵抗 ML 的子领域。主力模型 **Pearl** 是 co-folding（类比 AlphaFold 3 / Boltz / OpenFold 3，但专注小分子）。他们用三招对应 LLM scaling：① 预训练侧用**物理模拟造合成数据**（因公开晶体结构库 PDB 只有约 20 万个、增长极慢）；② **推理时 scaling**——模型不在语言 token 上"思考"，而在"晶体结构表征"上迭代（diffusion head 本就是多步迭代），并用**物理引导（physics-based guidance）**steer 输出；③ RL（含"实验室 in-the-loop"）。与 [Insilico/Insight] 类 CRO 伙伴组"设计-合成-测试-分析"闭环。反复强调 AlphaFold 3 拿诺奖 ≠ 药物发现被解决。

## 核心观点

### 命题：diffusion 的最前沿在结构生物学
- 2017–18 大家以为 GAN 是图像生成的未来，但 GAN（mode collapse）对蛋白/复合物构象不 work；**diffusion 才是对的 primitive**。如今讽刺的是：图像/视频有些转回 autoregressive，而"最创新的 diffusion 研究在 3D 结构预测"——十年前无人能预料（[00:00:00]、[01:06:51]–[01:08:52]）。
- 别把药物发现当"零到一然后解决"：没有单一 iPhone/ChatGPT 时刻，是**跨越十年的迭代复利**；有 2 万个蛋白编码基因，每个都能致病，永远有更多问题可解（[00:04:05]–[00:07:10]）。

### Pearl：把 LLM scaling 三段式搬到结构预测
- 输入蛋白序列 + 配体表征，预测二者在 3D 空间"合体"后的结构（co-folding）。专注**小分子**：看似更简单，实则搜索空间巨大（宇宙中约 **10^60 个类药小分子**，还能旋转/多构象）（[00:12:17]–[00:14:20]）。
- **合成数据**：PDB 约 20 万晶体结构、扩张"冰川速度"；但小分子可用**物理建模**造更多训练数据（大蛋白太复杂、物理建模算力代价高）（[00:15:21]–[00:16:21]）。
- **推理时 scaling**：diffusion head 天然多步迭代，模型被迫"思考"——不是语言 token，而是"内存里未完全物化的晶体结构表征"来回；用物理引导 steer，"提升很大"（[00:16:21]–[00:19:24]）。像 diffusion 力场与物理力场之间平衡；但内部到底学到什么"很难解释"，mech interp 是开放方向（[00:19:24]–[00:20:24]）。
- 方法论"无聊但真"：**data / infra / evals** 三件事；"只能改进你度量的东西"，从第一天就盯 1Å 精度，这个目标会传导到数据过滤、架构、loss（[00:51:43]–[00:53:44]）。

### 为什么是 1Å：药物发现是分辨率的科学
- 业界惯用 RMSD<2Å 太粗：2Å 下整个芳香环可能翻转仍算"有效输出"；且不像模糊图像你知道它模糊，**翻转的芳香环看起来很正常**——med chemist 会被误导（[00:41:36]–[00:43:37]）。
- 氢键的供体-受体距离是 2.7–3.3Å（窗口约 0.6Å），差一点就从氢键变成 clash 或失效；所以核心结合区要**亚埃分辨率**（溶剂暴露区更动态、可较松）（[00:49:41]–[00:51:43]）。
- **eval 危机**：RMSD<2 其实源自 AI 之前的物理 docking 学术研究（学者写论文而非造药），被 AI 社区沿用；PoseBusters（牛津，加物理有效性）、LDDT、OpenBind 正推动 eval 转型。类比 SWE-bench——Gemini 刷榜赢但没人用它写代码（[00:55:45]–[00:58:47]）。

### 结构不等于药：ADMET 与"反相关"的多参数优化
- AlphaFold 3 诺奖让大众以为"药物发现解决了"，实则很远：单个静态结构不够，还要动态、要预测约 **30+ 种 ADMET 性质**（吸收/分布/代谢/排泄/毒性，如溶解度、CYP450 抑制、hERG 心毒）（[00:35:33]–[00:37:33]、[01:00:50]–[01:02:51]）。
- 药物性质常**反相关**：结合力越强往往越疏水（口袋是"油腻"的）→溶解度变差；加极性改善溶解度→过膜变难。多参数优化像打地鼠，常要找真正的**离群分子**——而这类新颖化学恰恰是自动化合成难做的（[01:19:03]–[01:21:03]）。
- Genesis 早年发的 PotentialNet（图神经网）与 MoleculeNet、多任务图网络做 ADMET，是被引数千次的奠基工作；从一开始就聚焦"药物发现全套 ML 模型"，不碰 target ID（生物学）与临床（[00:59:49]–[01:03:51]）。

### 数据闭环、RL 与"实验室 in-the-loop"
- 与 **Insight/Insilico** 类伙伴组"设计-合成-测试-分析"闭环：Genesis 出预测→伙伴极快合成+测性质→回传训练；是"天作之合"（[01:11:56]–[01:14:58]）。最兴奋的是 **RL**：先用物理反馈，最终"实验室 in-the-loop"——预测→合成→测量→回灌（[01:09:53]–[01:11:56]）。
- 泼冷水"机器人自动化实验室"：合成/纯化/表征（NMR、质谱确认"你造出来的确实是想造的")都不 trivial；高通量筛选（DEL/DNA 编码库）到 denovo 低通量高保真的 R² **低得惊人**、假阳性巨大——所以大家才盼 AI 预测能比湿实验更干净（[01:15:59]–[01:20:03]）。
- **中美对照**：西方 pharma 越来越依赖 CRO 把湿实验外包→尖端实验能力下降；而中国 biotech（如 Insight）**自建极强的 in-house 实验能力、产出数据极快**，是"设计-造-测-分析"闭环的关键。"美国生物技术输给中国不是创新问题"的话题被点为"房间里的大象"（[01:12:57]–[01:14:58]）。

### Agent、商业模式与公司改名
- 在建 24/7 药物发现 agent 平台（代号 **Sapphire**）："几百个 med chemist/CAD 科学家式 agent 夜以继日"；前提是底层模型（pose/potency/ADMET）都够好，否则 agent 只会放大 slop（[00:46:39]–[00:48:40]、[01:29:08]–[01:35:11]）。agent 能"看"预测的晶体结构做决策（crystal structure 作为 LLM 的一种模态）（[01:32:08]–[01:34:11]）。
- 商业模式：主要**给大 pharma（Gilead、GSK、Insight 等）做 AI 服务**（fine-tune 基础模型到伙伴数据），同时自有 pipeline（"dogfooding + 药物发现的内在价值"）。改名 Genesis Therapeutics→**Genesis Molecular AI** 是回归"我们从第一天就是 AI 公司"的身份（[01:22:04]–[01:29:08]）。
- **narrow models 观**：Sergey 反对为分子做"通用智能模型"，主张为窄任务做很不同、很有意思的架构（"LLM 架构本质还是 2017 年的 transformer，有点无聊"）；瓶颈许愿都是 **GPU**——"LLM 公司在吸走所有 GPU 容量"，质疑"纯 LLM 空间剩下的 alpha"（[01:42:14]–[01:46:17]、[01:15:59]–[01:17:00]）。

## 相关主题

- [AI 与科学发现](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-for-science.md)（本期核心：diffusion 最前沿在结构生物学、结构≠药、ADMET、实验室 in-the-loop）
- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（scaling 三段式搬到结构预测、物理合成数据、推理时在结构表征上"思考"、RL 闭环、diffusion vs GAN vs AR primitive）
- [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)（eval 危机、RMSD<2Å 不足、1Å 阈值、PoseBusters/LDDT/OpenBind、SWE-bench 刷榜类比）
- [AI 商业化与价值捕获](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-business-and-value-capture.md)（AI 模型公司 vs 药企、narrow model、给 pharma 做服务 + 自有 pipeline）
- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（中国 biotech 自建湿实验能力/数据产出快、西方依赖 CRO 致尖端能力退化）

## 深度关联

- 语料层关联：[[KOL语料库对比与迁移评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。
