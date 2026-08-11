---
title: 与vLLM团队畅聊多模态（上）（外部迁移分析）
source: repository_import
youtube_url: https://www.youtube.com/watch?v=SK1HUqXDBp0
video_id: SK1HUqXDBp0
transcript: '[[与vLLM团队畅聊多模态(上) [SK1HUqXDBp0]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260511-uncle-moon-vllm-omni.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[与vLLM团队畅聊多模态(上) [SK1HUqXDBp0]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=SK1HUqXDBp0) · 视频 ID：`SK1HUqXDBp0`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260511-uncle-moon-vllm-omni.md)

## 迁移说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

## 概要

「与 vLLM 团队畅聊多模态（上）」。**vLLM Omni** 是从 vLLM 主库拆出的独立开源项目，专做**多模态/全模态（omni）模型的推理与 serving**：不仅支持多模态输入（理解），更支持多模态输出（生成，含 TTS/文生图/文生视频）。核心贡献是把 PD（prefill/decode）分离推广成通用的 **stage 抽象**，用一套框架管理 Qwen-Omni、Bagel、混元、小米 MemoAudio、Mistral Voxtro TTS 等 30+ 端到端模型。是本库首个专注"多模态 serving 基建"的中方一线素材。

> ⚠️ 无字幕本地 whisper 转录，专有名词多处误识，已按上下文归一化：VLM/VRM/BIM→**vLLM**、"VM Omni"→**vLLM Omni**、"签问/切碗/千万"→**Qwen（千问）**、"笼包"→**美团 LongCat**、"汇圆一密集"→**混元 image / Hunyuan（80B）**、"月签"→**月谦**、"Voctro/vostro TTS"→**Voxtro TTS**、"手包延迟"→**首包延迟（first-audio latency）**。DiT block 级缓存技术名（转录作"开始 DIT"）与项目具体版本号待官方确认。

## 核心观点

### 项目缘起：一个 +10000/-1000 行的 PR
- 起点是 Qwen 2.5-Omni、MiniCPM-o（OpenBMB/清华）等端到端多模态理解+生成模型出现。多模态**输入/理解**在 vLLM/SGLang/TRT-LLM 上已成熟，但端到端 N2N（含多模态**输出**）还是 question mark（[00:00:00]–[00:02:02]）。
- Qwen 团队（范洋）给 vLLM 提的支持 Qwen-Omni N2N 的 PR **加一万行、减一千行**、几乎重写 vLLM，"肯定接不了"、且过度偏向单一模型——于是决定**另立独立项目**（不放 vLLM 主库下，因为图景 still unclear、要随模型演化）；发起时只有 Roger 一人，去卖点子，华为等国内同学感兴趣加入，去年年中立项、年底做出，现约 4000 stars（[00:01:01]–[00:06:06]、[00:19:16]–[00:20:19]）。

### 核心抽象：把 PD 分离推广成通用 "stage"
- 今天大家谈 PD 部署，其实是 prefill / decode 两个 stage；vLLM Omni 是其扩展——一个 stage 可能是**多模态 encode、多模态生成**，模与模之间还有额外交互（[00:03:02]–[00:04:04]）。
- stage 间要传的不只 KV cache，还有 **embedding / metadata**，且**方向可双向、可跳 stage**（如 stage1 直跳 stage3），比纯 LLM 的 PD 复杂得多（[00:04:04]）。
- 两个 engine：**AR**（自回归，直接复用 vLLM 主库的 KV cache/PD 优化）+ **Diffusion/DiT**（从头写，无 prefill/decode、序列长度问题需单独优化）。最好的抽象就是 stage，stage 里跑 vLLM/diffusers/HuggingFace 都行、越 flexible 越好（[00:14:10]、[00:21:20]–[00:22:24]）。

### 工程要点：omni connector、控制/数据面解耦、chunkwise 流式
- **omni connector** 统一 stage 间传输：接口一致（不管底层传 tensor 还是 float），单卡走 shared memory pool、多卡自动走 **Mooncake**（[00:28:38]–[00:29:43]）。
- **控制面/数据面解耦（control & data plane decoupling）**：request id/采样参数等轻控制信息与 embedding/音频等重 payload 分开传，避免拖慢（[00:29:43]）。
- **chunkwise 异步流式**把首包延迟从近 10 秒降到 <1 秒、real-time factor <1（不必等 thinker 生成完所有 token，头几个 chunk 出来就送下一个 stage 生成音频）——语音 agent 可随时被打断，"响应快的 AI 能给人情绪价值"（[00:31:46]–[00:33:47]、[01:08:55]）。
- 部署：各 stage 可放不同 GPU、设不同 utilization、天然支持分离式部署（多人共用一张卡时按 stage 摆放）；混元 image（80B）会像 PD 分离那样部署 1 个 AR 配多个 DiT 实例（[00:27:33]、[00:46:15]–[00:47:16]）。

### DiT 加速与并行（志鹏部分）
- DiT 对精度要求高、难做大幅量化（MP4 难），改用两种缓存跳步：**TeaCache**（layer 级跳过——今天样品与前几天相似就复用）+ **block 级缓存**（一天工序做一半发现像某天结果、直接把后续 hidden state 改动加上来跳过）；均需 case-by-case 测精度损失，仓库提供多项式系数拟合工具做 good-first-issue（[00:52:27]–[00:56:37]）。
- Diffusion 并行：TP/DP/EP/PP + **USP（Ulysses SP）+ Ring Attention**（两者正交可同开）、**HSDP**（类 FSDP 切权重）、**VAE patching**（图像 hidden state 分块并行解码）、**CFG parallel（CFGP，最稳最明显的加速）**；实测现代显卡算力过剩，diffusion 可做 continuous batching（把不同 step 的 request 拼 batch）（[00:41:08]–[00:42:09]、[00:49:19]–[00:57:38]）。
- **边缘部署**：module-wise / layer-wise CPU offload（权重逐块从 CPU 加载到 GPU 算完卸回），因很多用户在个人电脑/边缘设备跑 diffusion（[00:50:21]）。

### 硬件插件与未来：world model / VLA
- hardware plugin 系统：支持 CUDA/ROCm、**华为昇腾 MPU、百度昆仑**——新硬件接入不改核心 AR/Diffusion 逻辑，只实现插件接口（[00:24:27]–[00:25:30]）。
- v0→QE 版架构：把调度器与前端融合、进程通讯改线程通讯，multi-stage 模型普遍省 1–2 秒（[01:02:48]–[01:03:51]）。
- 未来（下季度）：**streaming input 支持 world model / VLA**（世界模型需流式视频输入+键鼠操作、流式视频输出）、与 veRL 集成做多模态 RL（已支持用 Qwen-Omni 做 rollout）、更多 multi-stage 模型（Bagel、Qwen-Omni）的 RL 适配（[01:03:51]–[01:08:55]）。

## 相关主题

- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（本期核心：多模态 serving、stage 抽象、DiT 加速、国产芯片插件、Mooncake）
- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（中方多模态推理基建一线、昇腾/昆仑适配、开源社区）
- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（与 veRL 集成做多模态 RL、world model/VLA 方向）

## 深度关联

- 语料层关联：[[KOL语料库对比与迁移评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。
