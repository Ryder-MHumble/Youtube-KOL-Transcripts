---
title: Causal Models Need Causal Data - Xaira’s X-Cell model (Bo Wang & Ci Chu)（外部迁移分析）
source: repository_import
youtube_url: https://www.youtube.com/watch?v=2AdS-2uuH80
video_id: 2AdS-2uuH80
transcript: '[[Causal Models Need Causal Data - Xaira’s X-Cell model (Bo Wang & Ci Chu) [2AdS-2uuH80]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260721-latent-space-xaira-xcell-virtual-cell.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Causal Models Need Causal Data - Xaira’s X-Cell model (Bo Wang & Ci Chu) [2AdS-2uuH80]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=2AdS-2uuH80) · 视频 ID：`2AdS-2uuH80`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260721-latent-space-xaira-xcell-virtual-cell.md)

## 迁移说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 本库第三块系统性 AI-for-science 素材（前两块是 [Genesis Molecular AI](20260630-latent-space-genesis-diffusion-drug-discovery.md) 的小分子结构预测和 [Lila Sciences](20260716-latent-space-lila-sciences.md) 的"实验室即 verifier"）。核心命题一句话：**要预测"如果我干预了会怎样"，就必须用干预产生的数据来训练——观测数据在原理上就欠定**。这是本库里对"数据质量 > 架构"这条经验规律最干净的一次实证。

## 概要

Xaira 是 AI 原生药物发现公司（联创之一是 David Baker），有三条 AI 平台线：**蛋白设计**（Baker 实验室血统）、**虚拟细胞 / 生物学基础模型**（本期主题，即 X-Cell）、**患者表征模型**（刚起步）。Bo 强调三者不是各干各的，而是要互相接口：设计虚拟细胞模型时就要看"能不能找到更适合蛋白工程模型下手的靶点"。

X-Cell 是 Xaira 的第一个虚拟细胞模型，49 亿参数，预测细胞对**基因扰动**的响应。配套发布的 **Pisces 数据集**：16 种细胞类型、2500 万个细胞（最严格质控后的数字）、全基因组尺度、由 7 场全基因组 perturb-seq 战役拼起来。模型与数据均开源。

## 核心观点

### 主命题：描述性数据学不出因果

- 虚拟细胞不是新概念。**virtual cell 1.0**（约 20 年前）是写微分方程描述通路响应，"largely a failed attempt——生物学复杂到写不进几个预设方程"；**virtual cell 2.0** 是 ChatGPT 之后的数据驱动路线，由 CZI 牵头的一篇 Cell 观点论文正式命名（[00:13:28]–[00:17:40]）。
- Cell×Gene（初期 3300 万细胞）是**观测性/描述性**数据，多来自健康供体。在这上面训的模型（scGPT、Geneformer）擅长描述性任务——跨批次整合、去 batch effect；但在**因果 / 扰动 / 反事实**任务上**至今打不过线性基线**（[00:20:43]–[00:22:48]）。
- 为什么必然如此："如果你观察到基因 A、B、C 一起上下波动，你可以推断 A 调控 B 和 C；也可以说 B 调控 A 和 C；也可以说 A 调控 B 而 C 由别的东西调控——**有 N 种因果结构能拟合同一份相关性数据**。原始数据在根本上 underpowered，学不出真正的因果"（Chu，[00:21:45]–[00:22:48]）。
- 因此结论是把钱花在**造因果数据**上：**Causal models need causal data**。

### 怎么造因果数据：perturb-seq 的工程化

- **Perturb-seq = 高通量池化 CRISPR 扰动 × 单细胞 RNA-seq**，产出一张二维表：一个轴是扰动（2 万个基因都可以被敲），另一个轴是读出（同时测这 2 万个基因的表达）。Chu 明确类比：**这和训练 AlphaFold 的 PDB 数据是同构的二维数据集**（行是蛋白条目、列是每个氨基酸的 XYZ 坐标）（[00:22:48]–[00:27:52]）。
- 池化的技巧在条码：CRISPR-Cas9 需要投递两样东西——Cas9 蛋白，和一段告诉它去哪的 guide RNA。guide 被设计成结合基因的**启动子**区并带上沉默子，于是那个基因不再被转录。**读出 guide RNA 本身就等于读出条码**，因此可以"每个细胞敲一个基因、一次实验横跨 2 万个基因"，完美打散、没有孔间差异（[00:23:48]–[00:26:48]）。
- **真正难的是工程而非科学**：学术界发表的方法都建立在"处理新鲜细胞、实验一两小时内做完"上；要做全基因组规模就得在 14 小时里处理**上亿个细胞**——"到一天结束时，你能从细胞和实验室的科学家身上都检测到应激信号"。Xaira 的解法是引入**化学固定**，在实验开始时就把细胞状态锁死，从而把流程改成**错时（time-shifted）作业**，天然不产生 batch effect（[00:27:52]–[00:30:57]）。
- **数据设计的度量不是细胞数，而是"每美元的信息比特"**（bits per dollar in information content）——所以要在扰动维度和**生物学上下文维度**同时 scale（[00:32:59]–[00:32:59]）。
- 最有野心的一场筛选：把 iPSC 在一次实验里分化成 **10 种细胞类型**，再对它们做全基因组扰动——"library on library"，等于 1 万个实验 × 10 种细胞（[00:31:59]–[00:32:59]）。

### 架构：从自回归换成 diffusion language model

- scGPT 沿用了自回归下一 token 预测，代价是**必须假设基因有顺序**（按表达值排序等）。但表达数据本质是矩阵，"你把基因顺序打乱，生物学不怎么变"——顺序假设是为了复用语言模型的现成技巧而付的税（[00:40:12]–[00:42:15]）。
- X-Cell 换成 **diffusion language model**，双向、不需要顺序假设。Bo 的类比很清楚：**自回归是"打字"（I → I like → I like coffee），diffusion 是"编辑"**——从很粗糙的表达谱迭代精修到收敛（[00:42:15]–[00:43:19]）。论文里显示随扩散步数增加，loss 单调下降、与 ground truth 的拟合单调上升。
- 仍是 **decoder-only 的生成式模型**，因为目标是生成整个转录组、建模完整的基因调控网络，而不是预测一小撮预设基因（回应 Brandon"为什么不干脆当成集合操作"的质疑，[00:43:19]–[00:45:23]）。
- **先验知识注入**：X-Cell 据称是第一批同时注入**五类**生物学先验的模型——文献嵌入（GenePT：直接问 LLM"告诉我这个基因的一切"再嵌入）、PPI 蛋白互作网络、DepMap（癌症必需基因）、形态学信息、scGPT 嵌入（细胞类型）。训完之后这些先验已内化为可学习参数、推理时不必再给；但**推理时再给一遍相当于虚拟细胞的 in-context learning / prompting**。看不同先验的权重还带来可解释性——能看出哪类先验对哪类细胞更重要（[00:46:24]–[00:50:31]）。

### 消融：数据 > 架构 > 先验

- Bo 给出的明确排序（并注明只适用于他们这套架构）：**数据集的质量与规模贡献最大，其次是架构，最后是先验知识**（[00:50:31]–[00:52:31]）。
- 架构的 delta 不是均匀的：**从自回归换到 diffusion，在"难任务"尤其是泛化到未见上下文上有显著提升**；先验则是 condition-specific——某些细胞类型上差别巨大，另一些上边际收益很小。Bo 自己怀疑是 cross-attention 这种注入方式限制了元数据的作用范围。
- 他们也做了公平消融：**把场上所有虚拟细胞模型（State、scGPT 等）放在同一份数据上重训**再比 delta。

### 评估：MAE 是个坏指标

- 现有 benchmark 多建立在 **Replogle 数据集**上、指标多为 **MAE**。问题：单细胞数据极稀疏，**"所有细胞的平均谱"是一个极好的 MAE 局部最优——它的 MAE 有时比技术重复（technical replicates，扰动实验事实上的 ground-truth 天花板）还低**。"这本身就说明这个指标不可靠"（[01:02:53]–[01:03:56]）。
- 他们主推的指标是 **Pearson Delta**——预测的表达**变化量**与真实变化量的相似度。"这个很难作弊，你必须真的把变化预测对"（Chu，[01:04:59]–[01:04:59]）。
- Chu 的方法论一句："**What gets measured will get improved**"——她把这个领域"缺乏一致且被普遍接受的 benchmark"列为核心痛点。

### 泛化的三个证据

1. **未见细胞状态**：只在**静息** T 细胞上训练，然后告诉模型"这是激活态 T 细胞长什么样，去预测所有扰动在激活态下的效果"。线性基线是把静息态的扰动 delta 线性平移过去。X-Cell 既预测对了已知生物学（TCR 复合物会灭活 T 细胞），也预测对了他们在筛选中发现的**推定新的** T 细胞失活因子（[00:55:38]–[00:58:44]）。
2. **未见细胞类型**：10 种 iPSC 分化细胞类型中留一种不训练，模型在这一未见类型上跨数千基因 × 数千扰动做出了良好预测（[00:58:44]）。
3. **细胞系 → 原代细胞**：只在 T 细胞**系**上训练，去预测 Alex Marson 实验室新发表的**原代** T 细胞 perturb-seq（多个供体），预测准确。RJ 的总结是对的：**这是整个理论的验证——在"有点怪的"易培养细胞上训练，居然能外推到真人身上取下来的真细胞**（[00:58:44]–[01:00:50]）。
- 为什么非线性模型该赢：把 7 场全基因组筛选拼起来后，生物学家一眼看出**有些扰动是"上下文普适"的（管家基因），另一些是强上下文依赖的**（比如发育相关基因只在 iPSC 实验里亮起来）。要同时抓住这两类效应，线性模型必然不够（[01:04:59]–[01:07:02]）。

### 边界与承认的局限

- 目前是**单基因功能缺失扰动 + 只读 RNA + 主要在细胞系**。三个轴同时在扩：走向多模态读出、走向通路级/组合扰动、走向原代细胞 / 类器官 / 体内扰动（[01:07:02]–[01:09:04]）。
- 组合扰动可以**纯 in-silico 做**（同时扰动两个基因的 token），但"没有真实组合扰动数据训过，精度未必在"——定位是生成假设（[01:09:04]–[01:10:08]）。
- 目的不是取代实验："**虚拟细胞的圣杯是泛化到那些更难甚至不可能做实验的上下文**"（Bo）。动机数字：**90% 的疾病无药可治；多数药死在三期；三期成功率只有 5–10%**（[01:00:50]）。

### 开放科学、学术界 vs 工业界

- 模型和数据全部开源。理由是 PDB 的先例：**开放数据 → AlphaFold / RoseTTAFold → 整个蛋白领域繁荣**。"虚拟细胞这个领域太早了，捂着数据和模型没好处"（[01:18:20]–[01:20:23]）。
- Bo 对学术界处境的直白描述：**"学生加入一个教授实验室时问的第一个问题是'你有多少张 GPU'"**；大量教授因为资源离开大学；AlphaFold 这类突破来自工业界（[01:12:10]–[01:13:12]）。
- 但学术界不可替代的地方也很具体：Chu 逐一点名——**CRISPR、CRISPR 哺乳动物高通量筛选、液滴包裹 scRNA-seq、perturb-seq 本身，全部首先在学术界诞生**（Weissman、Regev 等实验室）。"这些实验室侧的创新耗时极长、发现过程极偶然，未必适合纯工业界来扛；但一旦露出苗头，把它规模化、稳健化、产出 AI 级别的高质量数据，工业界做得很好"（[01:17:18]–[01:18:20]）。
- Bo 的补充：教学**逼着你每年更新**（他在多大教 600 人的深度学习课）；加拿大学术体系让他能拿到工业界因合规拿不到的医疗数据集。

### 关于品味与 agent

- **"在 agentic AI 时代人人都能写代码了，更重要的是对项目有正确的品味，这样你才不会漫无目的地烧 token"**（Bo，[01:21:26]）。
- 工作方式的位移："我们过去花大量时间写代码、一点时间调试；现在让 agent 写大部分代码，我们把大部分时间花在**调试**上"——他实验室在专门讨论"怎么发现 AI 犯的错"、"AI 在哪些地方特别好、哪些地方仍然受限"（[01:22:29]–[01:23:31]）。
- 他自己用 agentic AI 每天监控所有 AI 论文；也坦承"节奏快到我早上醒来会焦虑——这么多人发了论文，我们手头的工作怎么办。学生大概是 10 倍焦虑"（[01:11:10]–[01:12:10]）。

### 两个"魔杖"愿望

- **Chu**：能像做基因组学那样**高通量测蛋白质**。"RNA 很好，它预告了哪些蛋白会被造出来，但**蛋白才是细胞里的功能单元**"——丰度、翻译后修饰、亚细胞定位、构象状态都重要（[01:25:37]–[01:26:37]）。
- **Bo**：**能对同一批细胞在多个时间点重复测序的技术**。"现在为了测序你必须杀死细胞。"如果能测同一批细胞的时间演化，"**那才是真正的虚拟细胞**"——因为现在测的、建模的一切都是静态的（[01:26:37]–[01:27:37]）。

## 与本库其它观点的关系

- 与 [Genesis Molecular AI](20260630-latent-space-genesis-diffusion-drug-discovery.md) 高度互补：Genesis 讲**结构**（diffusion 在 3D 结构预测），Xaira 讲**功能/因果**（diffusion 在表达空间）。两家都在用 diffusion 作为核心 primitive，也都强调"数据比架构重要"。见 [AI 与科学发现](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-for-science.md)。
- 与 [Lila Sciences](20260716-latent-space-lila-sciences.md) 的"verifier 是一整间实验室"是同一枚硬币：Lila 强调**湿实验作为奖励信号**，Xaira 强调**湿实验作为训练数据源**。二者共同点是"AI-for-science 公司的真正资本开支在湿实验，不在 GPU"。
- "MAE 上平均谱打败技术重复"是本库 [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md) 里**指标失效**的最强案例，与 Genesis 的"RMSD<2Å 不够"、swyx/Mark Chen 的"bench maxing"同属一族。
- "描述性数据学不出因果"对 [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md) 有直接外推价值：这是"预训练语料的分布决定了模型能学到哪一类结构"这一命题在生物学上的一个可证伪版本。
- "学生问教授有多少 GPU" + "教授流向工业界"补入 [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md) 与 [AI 与就业](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-and-jobs.md)。
- "agent 写代码、人调试"与 [志鹏"编程在编两样东西"](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/zhipeng.md)、[Anton Osika"工程不再是瓶颈"](20260715-all-in-gelsinger-lovable.md) 是同一位移的三个版本，见 [LLM 实用方法论](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)。

## 事实性断言与预测（可验证）

- X-Cell 为 **49 亿参数** diffusion language model；Pisces 数据集 **16 种细胞类型 / 2500 万细胞（严格质控后）/ 全基因组 / 7 场全基因组 perturb-seq**（**断言**，[00:50:31]–[00:52:31]、[00:53:33]）。
- 在描述性数据上训练的单细胞基础模型（scGPT、Geneformer）**在扰动预测任务上不优于线性基线**（**断言**，[00:20:43]–[00:22:48]、[01:02:53]–[01:04:59]）。
- 在 Replogle 数据集上，**"细胞平均谱"的 MAE 有时低于技术重复**（**断言**，[01:02:53]–[01:03:56]）。
- 消融排序：**数据质量/规模 > 架构（AR→diffusion）> 先验知识**（**断言**，[00:50:31]–[00:52:31]）。
- 只在 T 细胞系上训练的 X-Cell，可外推到 Alex Marson 实验室的**原代** T 细胞多供体 perturb-seq（**断言**，[00:58:44]–[01:00:50]）。
- 90% 的疾病无治愈手段；三期临床成功率 **5–10%**（**断言**，[01:00:50]）。
- Bo 预测：未来的虚拟细胞模型应整合 spatial omics、ATAC-seq 等多模态；下一版 X-Cell 将支持 spatial-aware 表征（**预测**，[00:35:06]–[00:40:12]）。

## 深度关联

- 语料层关联：[[KOL语料库对比与迁移评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。
