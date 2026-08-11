---
title: "Andrew Feldman- 快速推理不是体验优化，而是 AI 产品形态迁移的底层变量"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=UEOSUSz--Ig"
transcript: "[[Cerebras CEO Why GPUs Can't Do Fast Inference]]"
tags:
  - kol情报
status: canonical
---

> Andrew Feldman 这场访谈的核心不是 Cerebras 反 NVIDIA，而是把 AI 竞争从“谁训练出更聪明模型”改写为“谁能用更低延迟、更少数据搬运和更稳定供给，把模型变成实时可用的产品”。

视频链接：https://www.youtube.com/watch?v=UEOSUSz--Ig

对应逐字稿：[[Cerebras CEO Why GPUs Can't Do Fast Inference]]

## 概述

这场 MAD Podcast 访谈表面上讲 Cerebras 的 wafer-scale chip、OpenAI deal 和 CUDA moat，实际主线更清楚：AI 已经从训练期进入使用期，推理速度变成产品形态变量。Feldman 一开始就把转折点放在 2025 年中，AI 从“parlor trick”变成生产工具，用户开始真正等待输出，于是延迟、tokens per second per user、agent 多轮调用和数据中心供给一起成为新瓶颈。

这篇应放进“Scaling 天花板的具体机制”和“价值捕获层级”两条线。它补充 Dylan Patel、Bryan Catanzaro 和 Jensen Huang 的硬件-软件协同判断：当模型层趋同，产品差异会下沉到内存、封装、数据搬运、推理 API 和电力供给。

## 从训练竞赛转向使用竞赛

Feldman 对速度问题的解释不是工程指标，而是产品分水岭。他说 AI 过去更像新奇表演，直到人们真的开始使用它 [1:41]。

转折之后，关键问题从“能不能回答”变成“回答是否足够快到让人持续使用”：

> **[2:13]** "fast tokens are more productive"

这改变了 AI 产品的评价方式。chat 查询、agent 多轮调用、代码生成、工具使用和验证环节都会把等待放大。Feldman 给出的指标是：

> **[2:40]** "the right metric is tokens per second per user"

这句话的产品含义是：推理速度不是后端优化项，而是决定用户是否愿意把任务交给 AI 的前台体验。慢速 agent 不是“同样聪明但慢一点”，而是会改变用户任务选择、交互频率和可接受复杂度。

## 速度会改变产品类别，而不是让旧产品更高效

Feldman 用 Netflix 类比说明速度的真正作用。互联网变快后，Netflix 没有更高效地送 DVD，而是变成电影工作室：

> **[3:20]** "They became a movie studio"

他随后说速度打开了新的使用域：

> **[3:52]** "It it opens up a whole new domain"

所以 fast inference 的意义不是把 ChatGPT 的响应从 8 秒降到 2 秒，而是让 AI 产品从“等待结果”变成“实时协作”。这会影响 SaaS、agent、IDE、搜索、客服和数据分析。一个需要用户等十几秒的 agent 只能做后台任务；一个足够快的 agent 才能进入同步工作流，甚至让用户在连续反馈中工作。

这也解释了为什么 Cerebras 把“fast tokens”包装成 cloud/API 产品，而不只是芯片性能。客户买的不是 wafer，而是更快完成任务的交互节奏。

## 推理瓶颈本质是内存搬运，而不是单纯算力

访谈中最关键的技术论证在 [31:32-32:36]。Feldman 说图形负载和 AI 推理负载不同：图形是把数据搬到 GPU 后长时间计算；推理是每生成一个词，都要搬一次大量权重。

> **[32:15]** "all the time is dominated by the movement of data"

因此，GPU 在 decode 阶段慢，不只是“算力不够”，而是架构假设错位。Cerebras 选择 SRAM 和 wafer-scale，是为了用更大的芯片面积换更快的数据访问：

> **[32:52]** "build a part vastly larger than any part in history"

这个论证对 AI 基础设施判断很重要：下一阶段竞争不只是 FLOPS，也不是单纯买更多 GPU，而是模型形状、内存层级、decode/prefill 分工、数据中心位置和电力一起决定每个用户的有效推理速度。

## Agent 让 CPU 重新成为瓶颈

Feldman 还给了一个容易被低估的信号：agentic AI 会推高 CPU 需求。原因是 AI 不再只生成文本，而是发起行动：访问网站、取数据、下订单、调存储。

> **[23:22]** "AI doesn't just provide answers it initiates action"

他把 AI accelerator 比作 brain，CPU 比作 body：

> **[24:51]** "the AI processor is like the brains and the CPUs are like the body"

这意味着 agent scaling 会把瓶颈扩散到传统数据中心部件。不是所有问题都由更强模型或更快 GPU 解决。只要 agent 要操作真实数字世界，就会调动 CPU、网络、存储、浏览器、权限系统和外部 API。OpenClaw/Codex 这类 24/7 agent 的成本结构，必须把“行动成本”纳入，而不是只看模型 token。

## CUDA 护城河在训练和推理上分裂

访谈标题强调 CUDA is not a moat，但 Feldman 的说法更细。他承认 CUDA 对行业形成非常重要，同时指出前沿训练已经分裂：Gemini 用 TPU，Anthropic 用 Trainium，OpenAI 用 CUDA。

> **[1:01:42]** "the mode is clearly shrinking"

真正激进的是推理侧：

> **[1:02:21]** "it takes you eight keystrokes to move from a GPU to us in the cloud"

这里的隐含判断是：CUDA 的护城河在训练期强，在 API 化推理期弱。训练依赖软件栈、框架、调试和组织经验；推理 API 只要兼容模型调用，客户切换成本可能更低。Cerebras 的护城河不是开发者生态，而是“做别人做不到的快”。

## 关键判断

- AI 从 novelty 进入生产使用后，推理速度成为产品形态变量，而不是后端体验优化。
- tokens per second per user 比单卡峰值更接近用户价值，尤其适用于 agent 多轮任务。
- 推理瓶颈主要来自权重数据搬运；decode 阶段的架构选择会决定产品延迟。
- Agentic AI 会把需求扩散到 CPU、网络、存储和行动系统；不能只按 GPU 供需看 AI 基础设施。
- CUDA 在训练期仍有生态价值，但推理 API 化削弱了用户切换成本。
- Cerebras 的战略不是“替代所有 GPU”，而是在 fast inference 这个场景里把硬件、云和 API 绑定成产品。

## 深度关联

> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 硬件-软件协同从模型形状推进到用户等待时间
**← [[Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x]]**
- 本文件论点：Feldman 把推理速度定义为 tokens per second per user，并把 GPU decode 困境归因于权重搬运主导时间 [2:40, 32:15]。
- 对方论点：Dylan Patel 认为 AI 的真正 100x 来自模型、系统软件、网络拓扑和硅片形状的联合设计，而不是单层优化。
- 关联逻辑：Patel 描述协同设计的结构，Feldman给出用户侧落点：协同设计最终要体现在每个用户等待的 token 上。两者合并后，硬件架构不再是后台资产，而是直接决定 AI 产品可用性的前台变量。

### 算法域公司在推理时代要变成速度域公司
**← [[Jensen Huang- 系统思维与 NVIDIA 的算法域公司]]**
- 本文件论点：Cerebras 不以 CUDA 生态为主要护城河，而以 wafer-scale + SRAM + cloud API 提供 fast tokens [32:52, 58:56-1:00:45]。
- 对方论点：Jensen 把 NVIDIA 定义为算法域加速公司，核心能力是围绕新算法重写 processor、middleware、application 和系统栈。
- 关联逻辑：Jensen 解释 NVIDIA 为什么不是普通芯片公司，Feldman 说明新 entrant 如何攻击同一系统栈中的推理速度层。二者不是简单竞争关系，而是在不同算法域和使用阶段争夺“谁定义加速栈”。

### Agent 的行动成本让基础设施瓶颈外溢到 CPU 与系统调用
**← [[Diamandis #231- 多 Agent Scaling、OpenClaw 与权限边界]]**
- 本文件论点：Feldman 认为 agentic AI 会不断调用 CPU 执行动作，AI processor 是 brain，CPU 是 body [23:22-25:08]。
- 对方论点：Diamandis #231 把 OpenClaw 视为 24/7 headless agent 形态，核心问题是权限、支付、安全和常驻执行。
- 关联逻辑：#231 讨论 agent 的产品与制度边界，Feldman 补上底层计算边界：agent 常驻执行不只消耗 token，也消耗 CPU 行动、浏览器调用和外部系统接口。真正的 agent 成本模型必须覆盖“思考”和“行动”两部分。
