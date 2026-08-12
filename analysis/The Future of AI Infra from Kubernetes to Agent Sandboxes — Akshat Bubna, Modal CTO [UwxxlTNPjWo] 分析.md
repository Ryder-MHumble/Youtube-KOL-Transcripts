---
title: 'The Future of AI Infra: from Kubernetes to Agent Sandboxes — Akshat Bubna, Modal CTO'
source: repository_import
youtube_url: https://www.youtube.com/watch?v=UwxxlTNPjWo
video_id: UwxxlTNPjWo
transcript: '[[The Future of AI Infra from Kubernetes to Agent Sandboxes — Akshat Bubna, Modal CTO [UwxxlTNPjWo]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260708-latent-space-modal-agent-infra.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[The Future of AI Infra from Kubernetes to Agent Sandboxes — Akshat Bubna, Modal CTO [UwxxlTNPjWo]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=UwxxlTNPjWo) · 视频 ID：`UwxxlTNPjWo`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260708-latent-space-modal-agent-infra.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

## 概要

Modal 是一家"从零为 AI 应用重造原语"的 capital-light 云平台（不自建数据中心，跑在 17 家 NeoCloud 之上）。Akshat 复盘起源（为解决 Kubernetes 对 bursty/自定义镜像/GPU workload 的糟糕体验）、2023 年 5 月就做了 sandbox、如何把 SDK 团队从"开发者体验（DX）"改成"**agent 体验（AX）**"，以及弹性推理、投机解码、多节点训练、auto research 等具体产品。

## 核心观点

### self-provisioning runtime：把基础设施写进 decorator
- Modal 的核心是"自供给运行时"——把硬件/扩缩容配置放进代码里的 **decorator**（与代码 collocate），而非让人（或 agent）读几百个 Kubernetes YAML（还是无类型的）（[00:04:06]–[00:06:08]）。
- **DX 与 AX 的余弦相似度约 0.9**：让 agent 用得爽的东西和让开发者用得爽的东西高度一致；agent 用 Modal 明显比操作别的 substrate 快。做法是建 **modal bench** 找 agent 做不到的事，若 agent 反复"幻觉"某个功能、就把它做成真的 CLI（[00:06:08]–[00:07:10]、[00:57:42]–[00:58:42]）。
- 代码变黑箱后 **observability 反而更重要**——把日志/指标也放进 CLI 让 agent 自查，但仍需人做判断（[00:06:08]–[00:07:10]）。

### Sandbox：2023 年就做、去年才爆
- 2023 年 5 月建 sandbox（第一个例子就是把 small-developer 放进 loop 让 agent 自迭代，但当时模型 10 步后就发散）；沉寂两年，去年 agentic 用例才引爆（[00:10:12]–[00:12:13]）。
- **RL rollout 极度 bursty**——有时要 10 万个 sandbox 同时起；agent 本身反而不 bursty。sandbox 现支持 sidecar（一个 sandbox 是一个 pod、可跑多容器，≈docker compose）、出站网络控制（man-in-the-middle proxy 做 RL logging、注入凭证）、跨节点 sandbox 互联（[00:15:14]、[00:27:21]–[00:29:23]）。

### 弹性推理是最早的 PMF；投机解码的真相
- 最早在**自定义模型的弹性推理**上找到 PMF（音频 Suno、视频 Runway、机器人、comp bio 等），避开 LLM 空间；难点是**跨区域自动扩缩容**（不同区域流量周期错开）+ **GPU snapshotting**（快照 torch-compiled 模型态、加速冷启动）（[00:13:13]–[00:15:14]）。
- 开源 **DFlash**（block-based speculator）：投机解码用小 draft 模型预测、大模型批量验证，**提升 accept length 是乘法级 2–4x 提速**（改 kernel 只有几个百分点），且不降质量（只接受"更好或相同"的 token）（[00:17:15]–[00:19:15]）。
- Auto endpoints：一键起带全部优化的 endpoint、可 eject 出完整代码；下一步是随数据分布演化自动更新 draft 模型（[00:19:15]–[00:21:17]）。

### 编译器/网络/多节点训练的系统本质
- 上游贡献回 SGLang（差异化在"团队专家能第一时间帮客户拿到那份性能"+ 真正的 scale-to-zero 弹性），而非只做 GPU 出租（[00:21:17]–[00:22:18]）。
- 私有 overlay 网络 **i6pn**（IPv6，同 workspace 容器互相寻址、无加密、EBPF 控制放行）；本为 serverless 分布式训练（RDMA、3 Tb/s 内网）而建，用户拿去干别的。RL 本质是"把内存（KV cache、权重）在训练/推理 GPU 间高效搬运+调度"的系统问题（[00:29:23]–[00:33:27]）。
- 多节点训练不做大规模预训练，专注**中等规模后训练**（如 post-train quen 模型提推理质量）+ auto research 弹性小跑（[00:33:27]–[00:34:29]）。

### Inference inflection：GPU:CPU 从 8:1 摆回 1:1
- 借 Jensen GTC keynote 的说法："**inference inflection**"——AI workload 里 GPU:CPU 从 8:1 摆回约 1:1，因为 agent 频繁 block/call out 到 CPU 重活，limiting factor 在 GPU 和 CPU 间来回摆，必须把一切 collocate（[00:24:19]–[00:25:20]）。
- Capital-light、跨 17 家云建统一容量池 + 自建可靠性层（GPU 掉线不影响 workload）；"compute strategy"团队做容量规划（1yr vs 3yr 预留混合、对供应链下注）——类比航空公司对冲燃油（[00:38:30]–[00:40:30]）。

### 对生态与"meta harness"的看法
- 对 harness 不持立场（cloud managed agent 挂 Modal sandbox，或 harness 跑在 sandbox 里都行）；对 **OpenPipe / Vercel / Databricks Omnigent** 这类"meta harness / 伪 agent cloud"没深玩——"只要消耗更多 infra，Modal 都看多"（[00:45:35]–[00:47:37]、[00:56:42]–[00:57:42]）。
- sandbox 层要**硬边界**，怀疑 LLM 中介的权限控制（可外挂软 guardrail 但硬边界不能少）；对 swyx 抛的"LLM OS 内核就是个 LLM"的非共识观点持保留（[00:43:32]–[00:44:34]）。
- runtime sandbox 比 buildtime sandbox 赢（GitPod/owner→OpenAI 的对照）；Python + TypeScript 仍是"世界上最后两种语言"，runtime 用 Rust、不绑 Python（[00:54:41]–[00:57:42]）。

## 相关主题

- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（本期核心：agent sandbox/云、self-provisioning、投机解码、RDMA/overlay、inference inflection）
- [AI 实用方法论](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)（AX≈DX、modal bench、skill/CLI 补足 agent）
- [LLM OS 与新计算范式](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-os.md)（"LLM 内核"之辩、agent 生成 agent/自供给基础设施）
- [LLM 安全](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-security.md)（sandbox 硬边界 vs LLM 中介权限、出站网络控制）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
