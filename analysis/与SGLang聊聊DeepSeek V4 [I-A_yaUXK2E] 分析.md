---
title: 与SGLang聊聊DeepSeek V4
source: repository_import
youtube_url: https://www.youtube.com/watch?v=I-A_yaUXK2E
video_id: I-A_yaUXK2E
transcript: '[[与SGLang聊聊DeepSeek V4 [I-A_yaUXK2E]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260501-uncle-moon-sglang-deepseek-v4.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[与SGLang聊聊DeepSeek V4 [I-A_yaUXK2E]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=I-A_yaUXK2E) · 视频 ID：`I-A_yaUXK2E`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260501-uncle-moon-sglang-deepseek-v4.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> DeepSeek V4 技术报告发布次日的"Infra 界春晚"直播。三位 SGLang/Miles 工程师讲他们如何为 V4 全新架构做推理引擎和 RL 训练框架适配。全程技术细节密集，是本库中最贴近推理/训练 infra 一线工程的中方素材，与 [朱邦华（SGLang）](20260518-uncle-moon-banghua-zhu-sglang.md)、[江鋆晨（KV Cache）](20260609-uncle-moon-junchen-jiang-kvcache.md) 构成 infra 三连。

## 概要

DeepSeek V4 的注意力机制相比前代大改，给推理和训练框架都带来巨大工程量。推理侧：五类 KV cache 状态的 shadow radix cache 管理、kernel fusion、lightning topk、PD 分离、KV cache offload 到 CPU。训练侧（Miles/RL）：在 Megatron 里重写 V4 的算子、六种并行、逐 tensor 精度验证、训练稳定性（deterministic ops）。

## 核心观点

### DeepSeek V4 的新架构：混合稀疏注意力
- V4 的注意力对每个新词源同时处理**多类机制**：**SWA（sliding window attention，只看最近几个 token 的 KV cache）** + 两类压缩注意力——**Compress-4（每 4 个 token 压成 1 个，做 hierarchical top-k 选最有影响力的 token 算）** 与 **Compress-128（每 128 个压 1 个，做全注意力）**（[00:04:06]–[00:06:08]）。
- 框架要维护**五类状态**：SWA、C4、C128，以及 C4/C128 各自对应的 in-flight 计算（每算够 4/128 个 token 才压缩一次）（[00:06:08]–[00:07:09]）。
- **KV cache 被大幅压缩**：100 万 token 上下文只需不到 10GB——这直接打开了 offload 到 CPU/硬盘的空间（万诚认为是长远趋势，coding/agent 应用对上下文要求越来越高）（[00:19:47]–[00:21:49]）。呼应 [罗福莉](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/luo-fuli.md) 的 hybrid attention（sliding window + full attention 混合、更省 KV cache）判断——两条中方素材独立指向"混合稀疏是大势所趋"（[00:41:06] 万诚："因为系统的约束，混合架构会一直存在"）。

### 推理侧优化（万诚）
- **Shadow radix cache**：为五类复杂状态维护一套虚拟地址列表，KV cache 搬运/radix 查找只需检索虚拟地址（结合当前层数 + 所需 KV cache 大小映射到物理状态）；SWA 中已不影响计算的前段在物理内存中删除、只留索引（[00:07:09]–[00:09:16]）。
- **Kernel fusion**：V4 的 KV 压缩流程原本涉及 5 次内存读取（读数据→加法→softmax→点乘→写回），把中间三个计算合成一个算子，减少内存访问（显卡计算的关键优化）（[00:09:16]–[00:10:20]）。但万诚强调**算子融合并非总有效**：两算子融合要求能沿同一维度切分并行，否则某算子的切分方式不最优反而增开销（[00:47:22]）。
- **Lightning topk**：长上下文（如 100 万 token）下 topk 计算极慢——纯 PyTorch 实现单词源需 ~100 微秒，而 V4 有 60 层、每层都要，累计 6 毫秒，严重限制推理速度。改进并行度后从 **100 微秒优化到 15 微秒**（[00:10:20]–[00:12:29]）。
- **并行策略**：长上下文用 **CP（context parallelism）**（单机内通讯快、能用满全部计算单元），跨机用 **PP（pipeline parallelism）**（省跨机通讯但一次只用部分资源）；V4 注意力**不天然支持张量并行**（底层 kernel 要求头数是 64 的倍数），用 padding 补齐；MoE 部分支持专家并行；已支持 **PD 分离**（prefill=阅读理解 / decode=写作，分到两个集群）（[00:12:29]–[00:18:47]）。
- **KV cache offload 到 CPU 已支持**，验证可带来 **3 倍上下文性能提升**；latency 长的 agentic 请求可临时 abort 腾出 KV cache 空间、稍后再处理（[00:19:47]、[00:51:28]）。
- V4 算法与 SGLang main branch 直接结合"有些不优雅"，团队近期在重构（[00:52:29]）。GB200 上 V4 现达约 **200 token/s**（[00:53:31]）。

### RL 训练侧（袁月明 / Miles 框架）
- **给训练做"day-0"支持比推理难得多**：推理只需实现 forward kernel、可靠 benchmark 掉点判正确；训练还要 backward，且**没有标准 baseline**——整套 recipe 是否正确要靠"训几天涨点"来验证，debug 成本极大。Miles 的目标是让人第一天就用上完整 RL 系统（[00:21:49]–[00:22:50]）。
- 三部分工作：① **在 Megatron 里重写 V4 算子**（compressor attention、indexer、MHC 等无原生支持）+ 六种并行（DP/TP/SP/EP/PP/CP 全支持，CP 最复杂——C4 的 overlap transform 使 naive CP 出错，需 all-gather 后再恢复）；② **RL feature**（FP8 rollout + FP8/BF16 training、weight update 跨引擎格式对齐、实验性的 **indexer replay**——把推理时 attention router 的 routing 结果记录下来在训练中重放，降不确定性）；③ **训练稳定性**（[00:22:50]–[00:33:58]）。
- **精度是最耗时的部分**：逐 tensor（每层 activation、每个 gradient）与改动前做端到端比较。举例：CP=1 vs CP=2 时 attention 的 **KV gradient** 差异极大（cosine similarity 差 0.2，其他 tensor 是 1e-4~1e-5 量级）——根因是 compress attention 很稀疏、reduction 复杂使 BF16 精度不够，把该 tensor 换 **FP32** 即解决（[00:30:56]–[00:33:58]）。
- 借鉴 DeepSeek 的 **deterministic ops**：在 kernel/MoE 用 deterministic mode、禁用 NCCL 非确定性做法——原本 KL loss 的 spike 消失了（[00:33:58]）。
- **DSA（DeepSeek sparse attention）这类架构本身训练难稳**：加了 attention indexer（类似 MoE router）带来更多不确定性，从 V3.2 起就在做相关 exploration（[00:34:59]）。
- 初步结果：DAPO 上 4000 max response length、32 张 GB300，reward、eval score 上涨、log prob 稳定（time 有限没测更大 scale）。Flash 模型 RL 约需 64 张 H200 或 32 张 GB300；1.6T 的 Pro 约需 256 张 H200 或 128 张 GB300（验证中）。下一步做 **FP4** rollout + QAT 训练（[00:34:59]–[00:39:01]）。
- **Miles 从 slime fork 而来**，功能大量共享；差异在 Blackwell 新硬件适配、fully async agentic training；有 AMD 适配、国产加速器暂无（[00:41:06]–[00:46:07]）。

### 方法论：从"补窟窿"到 system research（月球大叔）
- **做 MLSys 若只盯 profiling、天天补代码小窟窿，不算 research**：应站在更高处问"过去几个月补的几十个窟窿有无共性、能否用一套框架的精巧 API 端出来"——"system research 需要一定的抽象与美感；当你决定把它做得更美，你就开始做 system research"（[00:59:40]–[01:01:44]）。
- **存储、通信、计算三要素的优雅平衡**：每代新硬件的架构改变都会打破旧平衡，需要新算法/新设计——而类似问题在过去几十年（如文件系统设计）已有人处理过（[01:01:44]–[01:02:46]）。
- **数据管理是被低估的新方向**：很多问题正从"算力压榨"转向"数据存储/管理"（agent 的持续记忆、Dreams vs Memory，引 Anthropic 文章）；"做数据库/传统后端的人不是没出路，反而机会更大"（[01:02:46]–[01:03:47]）。与 [江鋆晨"KV Cache 是下一个数据层"](20260609-uncle-moon-junchen-jiang-kvcache.md) 精确同频。
- 新手入门 SGLang：从 `good first issue` 起步（万诚第一个 PR 修了大输入下 MoE kernel 的 illegal memory access，逐步扩到专家并行、投机解码）；推荐 **mini-SGLang** 项目（命名/scheduler 比正式版更清晰）+ Karpathy 的底层课（01:55–01:00:41）。

## 相关主题

- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（V4 混合注意力的推理/训练适配、shadow radix cache、kernel fusion、KV offload、RL infra）
- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（RL 训练精度调试、deterministic ops、DSA 训练稳定性）

## 相关视频

- [朱邦华：SGLang 与 RL 训练 Infra](20260518-uncle-moon-banghua-zhu-sglang.md)
- [江鋆晨：KV Cache 作为独立数据层](20260609-uncle-moon-junchen-jiang-kvcache.md)
- [罗福莉：hybrid attention / MTP 面向 agent 的架构](20260424-zhang-xiaojun-luo-fuli-agent-paradigm.md)

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
