---
title: "Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=f6D_aiy8qyU"
transcript: "[[Why Hardware-Software Co-Design Is AI's Real 100x Dylan Patel of SemiAnalysis]]"
tags:
  - kol情报
status: canonical
---

> Dylan Patel 的核心判断不是“芯片会更快”，而是 AI 计算的效率曲线正在被联合设计重写：模型形状、kernel、网络拓扑、硅片和数据中心资本结构不能再分开看，真正的 100x 来自跨层协同，而不是任何单层的 2x。

视频链接：https://www.youtube.com/watch?v=f6D_aiy8qyU

对应逐字稿：[[Why Hardware-Software Co-Design Is AI's Real 100x Dylan Patel of SemiAnalysis]]

## 核心证据校准

> **[0:00]** "we have 90 people and like a big chunk of them are technologists engineers across the whole supply chain."

> **[0:00]** "And then someone the engineers like, "No, no, no, but this technology is the coolest.""

> **[5:04]** "Nvidia is better because they use a smaller chip to get you know better performance at better power efficiencies and their margins better"

> **[14:09]** "inference whether it's open models or closed models will be like one of the biggest markets in the world much bigger than oil"

> **[15:02]** "inference benchmarking was like point in time."

> **[15:41]** "model cost drop for equivalent quality by like 60x a year."

> **[15:41]** "You need to have benchmarks be living and breathing"

> **[16:35]** "We've got over $50 million of hardware uh donated to us."

> **[17:04]** "all the results are public and all the configurations are public."

> **[17:45]** "how fast is it responding to me versus you know batch size"

> **[18:18]** "most things in hardware infrastructure uh model application layer everything is downstream of that curve"

> **[18:45]** "right now the way we treat AI infrastructures, it's like one-sizefits-all."

> **[24:40]** "you've got this huge improvement on model layer, you've got this pretty sizable improvement on hardware"

> **[25:18]** "the shapes of all the experts in in DeepSeek, uh V3, they were all optimized for Hopper."

> **[25:51]** "all these different things are co-optimized between the model and the and the and the hardware and the infrasoftware in between"

> **[27:56]** "It's called software hardware co-design"

> **[28:19]** "instead of being multiplicative to 8x, it's actually 100x because you've optimized across all three layers."

> **[34:10]** "it comes down to hardware software codeesign."

> **[34:42]** "open eyes are much more sparse"

> **[35:31]** "that influences the model architecture."

> **[36:20]** "models are just great at coding and all software gets commoditized in that case."

> **[36:45]** "what people call the CUDA mode is not actually anything to do with CUDA"

> **[36:45]** "their models are co-designed for GPUs"

> **[38:28]** "I'll choose the best hardware and I'll co-design my model and infrastructure software through and through for that hardware"

> **[42:25]** "AI has no ROI infuriates me"

> **[42:25]** "the line has been up and to the right in terms of capabilities this entire time"

> **[50:13]** "there's different architecture bets and different paths for AI."

> **[50:33]** "because the market has gotten so big, niches will be carved out"

> **[59:38]** "25 or something crazy billion dollars per gigawatt or $25 million per megawatt"

> **[1:04:54]** "in the AI cloud a lot of this stuff hurt performance"

> **[1:07:07]** "he wants to create a multipolar world."

## 概述

Dylan Patel 这场 Sequoia Training Data 访谈的价值，不在于他讲了很多半导体细节，而在于他把 AI 计算的竞争单位从“芯片性能”重写成“整条栈的联合优化”。过去讨论算力，常常把硬件、系统软件、模型算法、数据中心和资本市场拆成不同话题；Patel 的框架正好相反：真正的效率跃迁发生在这些层之间。

SemiAnalysis 这个组织本身就是这个框架的缩影：一部分人懂完整供应链，一部分人来自 hedge fund，技术可行性和成本约束在同一张桌子上争吵。

> **[0:00]** "we have 90 people and like a big chunk of them are technologists engineers across the whole supply chain."

> **[0:00]** "And then someone the engineers like, "No, no, no, but this technology is the coolest.""

这解释了为什么 Patel 的判断经常比单纯技术分析更锋利。他不是只问“哪个芯片更快”，而是同时问：这个模型形状为什么适合某种互联？这个 kernel 是否能被 AI 写出来？这个数据中心每吉瓦多少钱？这个硬件生态五年后会不会把买方权力交给 hyperscaler？

## InferenceX 的意义：基准必须变成活系统

Patel 先把推理市场的规模定得很高。他认为 token 使用和 AI adoption 会成为最大市场之一，推理市场甚至会大于石油。

> **[14:09]** "inference whether it's open models or closed models will be like one of the biggest markets in the world much bigger than oil"

这个判断如果成立，传统“跑一次 benchmark、写一篇报告”的方式就完全不够。推理性能不是静态指标，因为模型每周变、PyTorch/vLLM/SGLang 更新、驱动更新、优化方法更新，今天的最优点明天可能就不是最优点。

> **[15:02]** "inference benchmarking was like point in time."

> **[15:41]** "You need to have benchmarks be living and breathing"

InferenceX 的核心不是排行榜，而是把推理性能变成持续运行的市场仪表盘。Patel 说他们拿到了超过 5000 万美元硬件，未来加入 TPU 和 Trainium 后接近 1 亿美元，并每天在不同硬件、模型和配置上跑公开结果。

> **[16:35]** "We've got over $50 million of hardware uh donated to us."

> **[17:04]** "all the results are public and all the configurations are public."

真正重要的曲线是吞吐量和交互性的 tradeoff：一个任务需要即时响应，还是可以批处理一夜？用户愿意为低延迟付多少溢价？同一模型在不同 batch size、speculative decoding、多 token prediction 下的成本差异会很大。

> **[17:45]** "how fast is it responding to me versus you know batch size"

> **[18:18]** "most things in hardware infrastructure uh model application layer everything is downstream of that curve"

这对产品判断很直接：未来 AI 产品的成本结构不是一个统一 token 单价，而是按任务的响应速度、可批处理性、模型质量需求和交互频率拆开。今天很多公司把 AI 基础设施当成 one-size-fits-all，Patel 认为这只是早期形态。

> **[18:45]** "right now the way we treat AI infrastructures, it's like one-sizefits-all."

## 100x 来自跨层协同，而不是单层优化叠加

Patel 最核心的反驳发生在 Sean 认为过去三年进步主要来自硬件层时。他直接说不同意：模型层贡献巨大，硬件层也有贡献，但真正的突破来自 co-design。

> **[24:40]** "you've got this huge improvement on model layer, you've got this pretty sizable improvement on hardware"

DeepSeek 是他的公开案例。DeepSeek V3 的专家形状为 Hopper 优化，后续版本又面向 Blackwell 和华为芯片优化。TPU 是优秀芯片，但跑 DeepSeek 不一定好，因为模型形状和底层矩阵单元、网络 IO、attention arithmetic intensity、collectives 都绑定在一起。

> **[25:18]** "the shapes of all the experts in in DeepSeek, uh V3, they were all optimized for Hopper."

> **[25:51]** "all these different things are co-optimized between the model and the and the and the hardware and the infrasoftware in between"

这就是他所说的 software hardware co-design：

> **[27:56]** "It's called software hardware co-design"

他的 100x 框架不是夸张口号。如果硬件、模型、系统软件各自独立优化 2x，乘起来是 8x；但如果三个层同时设计，可能直接换掉抽象边界，得到 100x。

> **[28:19]** "instead of being multiplicative to 8x, it's actually 100x because you've optimized across all three layers."

这里的关键不是“协同设计很重要”这种泛话，而是 AI 栈的抽象边界正在变软。模型实验室不再只选择现成硬件，硬件公司也不再只做通用矩阵乘法。模型稀疏度、专家形状、网络拓扑、HBM 带宽、kernel、数据中心供电，都在互相塑形。

## GPU vs TPU 不是宗教问题，而是模型形状问题

Patel 对 GPU 和 TPU 的态度很克制。他说自己可以为两边都辩护，因为最终还是 hardware software co-design。

> **[34:10]** "it comes down to hardware software codeesign."

OpenAI 和 Anthropic 的分歧在这里很有代表性。Patel 判断 OpenAI 模型更 sparse，而 Anthropic 虽然也 sparse，但整体更 dense；矩阵乘法单元大小、attention 结构、专家结构和网络拓扑会让不同实验室自然偏向不同硬件。

> **[34:42]** "open eyes are much more sparse"

> **[35:31]** "that influences the model architecture."

这意味着“哪个芯片赢”不是一个脱离模型路线的问题。一个硬件生态可能在某种模型形状上是局部最优，却在另一个模型路线中失去优势。未来不是单一赢家，而是不同模型、不同工作负载、不同延迟需求对应不同硬件和云基础设施。

> **[50:13]** "there's different architecture bets and different paths for AI."

> **[50:33]** "because the market has gotten so big, niches will be carved out"

对创业者和投资者来说，这个判断比“押 Nvidia 还是押 TPU”更有用：要问目标模型和工作负载会不会稳定。如果模型架构每年变化，过早固化在某个专用芯片上可能陷入局部最优；如果工作负载足够稳定、规模足够大，专用芯片和定制数据中心就会变得合理。

## CUDA 护城河正在从软件兼容迁移到模型生态

Patel 对 CUDA 护城河的判断很微妙。他承认模型很会写代码后，传统“很多客户需要 CUDA 编程兼容”的软件护城河被部分拆解。

> **[36:20]** "models are just great at coding and all software gets commoditized in that case."

但他没有因此说 Nvidia 护城河消失。相反，他把护城河重新定位到下游模型生态：很多开源模型本身就是为 GPU 协同设计的，所以它们在 GPU 上跑得更好，在 TPU 上不一定好。

> **[36:45]** "what people call the CUDA mode is not actually anything to do with CUDA"

> **[36:45]** "their models are co-designed for GPUs"

这是一种更深的锁定。过去的锁定是开发者写 CUDA kernel；未来的锁定是模型的数学形状、开源生态和推理服务商默认适配 GPU。如果 Google 想让 TPU 生态反过来锁定开发者，需要开源一批真正为 TPU 协同设计且足够强的模型，让用户感知到“这个模型在 Nvidia 上跑不好，在 TPU 上跑得好”。

大实验室则不同。OpenAI、Anthropic 这类公司不必依赖开源栈，它们可以直接选择最合适硬件，然后为它端到端重写模型和基础设施软件。

> **[38:28]** "I'll choose the best hardware and I'll co-design my model and infrastructure software through and through for that hardware"

这说明 CUDA 的问题不是“还在不在”，而是护城河的位置变了：从编程 API 迁移到模型-硬件-生态的共同演化。

## “AI 没有 ROI”在 Patel 看来是错看了能力曲线

Patel 最不耐烦的叙事是“AI has no ROI”和“模型没有进步”。他的反驳很直接：看旧 benchmark 不涨，只是因为旧 benchmark 已经饱和；换新 benchmark，能力曲线仍然向右上。

> **[42:25]** "AI has no ROI infuriates me"

> **[42:25]** "the line has been up and to the right in terms of capabilities this entire time"

这个观点有一个值得保留的风险：Patel 从供给侧和能力曲线看 ROI，容易低估企业真实部署中的组织摩擦、集成成本和责任边界。但他的反驳仍然有力，因为很多“无 ROI”讨论把模型能力停滞、成本太高、用例不清混成一件事。Patel 要拆开看：能力是否在涨？单位质量成本是否在降？工作负载是否因为能力提升而扩张？如果三者同时成立，短期应用层 ROI 不稳定不等于基础设施没有经济价值。

这也解释了他为什么坚持推理会是巨型市场。能力提升不是减少算力需求，而是打开更多可以自动化或增强的任务。

## Neocloud 机会来自传统云优势的反转

Patel 对数据中心和 neocloud 的判断，把技术分析推进到资本和组织层。AI 云不只是“买 GPU 出租”，而是土地、电力、网络、机柜、软件、长期承购协议、融资和交付速度的组合。

他给出的价格信号很极端：

> **[59:38]** "25 or something crazy billion dollars per gigawatt or $25 million per megawatt"

更重要的是，传统 hyperscaler 在 CPU 云时代积累的一些优势，在 AI 云里可能变成负担。Amazon 的 Nitro、安全隔离、传统 CPU 网络和存储优化，在 AI 工作负载里可能损害性能。

> **[1:04:54]** "in the AI cloud a lot of this stuff hurt performance"

这解释了为什么 Crusoe、CoreWeave 这类 neocloud 有窗口。它们没有完整传统云包袱，团队激励又更强，能为了特定 AI 集群做更快交付。AI 云的竞争优势不只是谁拿到 GPU，而是谁能更快把电力、土地、网络、散热、融资和可用集群组织起来。

## Jensen 的多极世界：Nvidia 在喂养自己的需求侧

Patel 对 Jensen Huang 的战略解释很关键：Nvidia 不希望 hyperscaler 或少数模型实验室拥有全部权力，因为那会削弱 GPU 的议价空间，也会让自研芯片更强。

> **[1:07:07]** "he wants to create a multipolar world."

所以 Nvidia 投资 AI labs、支持 neocloud、给集群背书，不只是卖更多芯片，而是在塑造未来五年的买方结构。今天卖给 Google、Amazon、Crusoe、CoreWeave 的 GPU 价格一样；但五年后，如果 neocloud 和非闭源模型实验室存在，TPU 和 Trainium 的相对权力就会被削弱。

这个判断可以解释 Nvidia 为什么既支持大客户，又支持它们的潜在替代供给方。Nvidia 的真正风险不是单个竞争芯片，而是买方集中和模型闭环导致 GPU 变成可替代输入。多极生态越繁荣，GPU 作为通用、开放、可迁移基础设施的价值越高。

## 关键判断

- AI 计算的核心变量已经从单芯片性能转向模型、kernel、网络拓扑、硅片和数据中心的联合设计。
- InferenceX 的价值在于把推理 benchmark 从一次性测量变成持续运行的市场仪表盘。
- CUDA 护城河正在从开发者 API 迁移到模型形状和开源生态默认适配。
- GPU、TPU、Trainium 都会有空间，决定因素不是宗教式选边，而是模型架构、互联和工作负载是否匹配。
- AI 基础设施不是 one-size-fits-all，未来会按延迟、吞吐、批处理、模型质量和成本曲线分层。
- Neocloud 的机会来自传统云优势在 AI workload 下的部分反转，以及更强的交付速度和资本组织能力。
- Nvidia 的多极战略是在主动管理需求侧结构，避免 hyperscaler 和少数闭源模型实验室集中全部权力。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Patel 解释了 Rowan 所说 AI 资本密集化的技术根因
**← [[Marc Rowan- 私募市场、软件重定价与资本配置]]**
- 本文件论点：Patel 认为 AI 的 100x 来自模型、硬件、系统软件跨层协同设计，模型形状会直接影响芯片、互联和数据中心选择 [25:18-28:19]。
- 对方论点：Rowan 认为数据中心、芯片、机器人、制造、国防会带来不可想象规模的资本密集度，必须把风险拆给信用、混合权益和股权分别承接。
- 关联逻辑：Rowan 看到的是资本结构结果，Patel 给出技术成因。正因为模型路线会塑造硬件形状和数据中心形态，AI capex 才不是普通服务器采购，而是持续变化的专用基础设施投资；这要求金融系统能承接更复杂的资产风险分层。

### Patel 与 Balaban 共同反驳“GPU 商品化”，但层级不同
**→ [[Stephen Balaban- The GPU Myth State of AI Compute 2026]]**
- 本文件论点：Patel 认为 CUDA 护城河不再只是 CUDA，而是开源模型和前沿模型与 GPU 形状共同演化，许多模型天然为 GPU 协同设计 [36:20-38:28]。
- 对方论点：Balaban 认为 GPU cloud 从土地、电力、服务器到软件是高度垂直整合服务，H100 资产反而可能越租越贵。
- 关联逻辑：Patel 解释 GPU 非商品化的模型生态原因，Balaban 解释 GPU 非商品化的物理和金融原因。两者叠加后，GPU 的价值不是单片芯片，而是模型形状、软件栈、数据中心和融资结构共同构成的资产网络。

### Patel 把 Evans 的模型商品化问题重新定位到基础设施分层
**→ [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Patel 认为推理基础设施不能 one-size-fits-all，吞吐量-交互性曲线会决定硬件、模型和应用层选择 [17:45-18:45]。
- 对方论点：Evans 认为基础模型可能商品化，价值捕获会向上层应用和具体工作流逃逸。
- 关联逻辑：Evans 讨论“模型层有没有定价权”，Patel 补上一层：即使模型趋同，推理服务也会因延迟、批处理、硬件形状和成本曲线分层。商品化不是全栈一起商品化，价值可能从模型参数迁移到最懂工作负载形状的基础设施和应用编排层。

### Patel 具体化了硬件-软件协同如何形成下一条 scaling 轴
**→ [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]]**
- 本文件论点：Patel 认为前沿实验室和硬件公司会同时优化模型、infrasoftware 和 silicon，抽象层之间的联合设计能把 8x 变成 100x [27:56-28:44]。
- 对方论点：Catanzaro 认为 Moore's Law 死亡后，NVIDIA 通过 Nemotron、MoE、4-bit 训练和 multi-token prediction 把模型架构反馈到硬件设计。
- 关联逻辑：Patel 给出跨层协同设计的产业框架，Catanzaro 给出 NVIDIA 内部如何执行这件事。合读后可以看到，未来 scaling 不只是更大模型或更多 GPU，而是模型形状反过来定义硬件形状，硬件形状再约束下一代模型搜索空间。

---

**元信息**
- 标题：Why Hardware-Software Co-Design Is AI's Real 100x: Dylan Patel of SemiAnalysis
- 频道：Sequoia Capital
- 嘉宾：Dylan Patel
- 发布时间：2026-06-30
- 时长：1:10:14
- YouTube链接：https://www.youtube.com/watch?v=f6D_aiy8qyU
