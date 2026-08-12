---
title: Poolside’s Model Factory, Laguna S, Open Models, and the Race to AGI — Eiso Kant, Poolside AI
source: repository_import
youtube_url: https://www.youtube.com/watch?v=9_0hs2sxHHo
video_id: 9_0hs2sxHHo
transcript: '[[Poolside’s Model Factory, Laguna S, Open Models, and the Race to AGI — Eiso Kant, Poolside AI [9_0hs2sxHHo]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260722-latent-space-poolside-eiso-kant.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Poolside’s Model Factory, Laguna S, Open Models, and the Race to AGI — Eiso Kant, Poolside AI [9_0hs2sxHHo]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=9_0hs2sxHHo) · 视频 ID：`9_0hs2sxHHo`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260722-latent-space-poolside-eiso-kant.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

## 概要

本库首个成体系的 **"neo-lab / 西方开源前沿实验室"内部工程视角**。Poolside 三年前从零起步（不脱胎于任何已有大厂）、从头写训练代码、押注"RL 是 LLM 能力最大驱动"（当时非共识），2026 年初从"抢先做到 AGI"转向**开源**，理由是"我宁愿活在有 100 家基础模型公司的世界，而不是 5 家——哪怕我是那 5 家之一"。核心干货有两块：(1) **Model Factory**——把模型训练做成 SpaceX 式的端到端工厂，5–8 周从预训练到发布；(2) **Laguna S**（118B 总/8B 激活）证明**"行为比原始智能更能压榨小模型"**，进而支撑一个关于模型商品化/开源能赢的论证。此外有大量对 RL 前移、MCP/工具"愚蠢论"、监管、算力政治的强观点。

## 核心观点

### 开源转向："宁要 100 家基础模型公司，不要 5 家"
- Poolside 起步于两条当时的非共识信念：**技术会持续复利、RL 是能力最大驱动**（三年前 OpenAI/Google/Anthropic 都不这么认为）（[00:05:07]–[00:06:07]）。
- 2026 年初重拾开源议题，因为世界正走向"三四家公司创造所有智能"的**反乌托邦剧本**（chapter 14 of dystopian sci-fi）。关键判断：**只有还没到前沿时才做得出这个决定**——"资本和预期堆太多之后就改不了主意了"（[00:07:08]–[00:09:08]）。
- **开源研究 > 开源权重**："权重是二进制的，给你权重也无法重建我在做的事；分享研究——我们怎么做的、几万次实验的教训——才是最有意义的贡献。"点名感谢中国实验室的开放研究（DeepSeek、Zhipu/Z.ai 的 GLM 5.2），"在接收端就有回馈的义务"（[00:11:10]–[00:12:10]、[00:31:24]–[00:33:25]）。
- 使命升级：主动**鼓励研究员离职去当自己的竞争对手**、开更多 neo-lab——"我们有一个小窗口，在模型真正驱动 RSI 到追赶不可行之前，应尽量多催生 neolab"（[00:33:25]–[00:34:25]）。

### Model Factory：把模型当工厂的产物，而非一件作品
- **核心度量**：一个想法从研究员到"可信赖的实验结果、并进入下一次训练"的墙钟时间。少于 70 个研究员 + ~35 工程师，每月跑 **1 万–2 万次实验**（[00:19:16]–[00:20:18]）。
- **SpaceX 类比**：第一枚火箭最难，但更难的是建工厂；建好后每次发射都只是"又一次发射"。Laguna XS2 从预训练到发布 **5 周**、Laguna S **8 周**；发布当天就把算力挪去训下一个（Laguna M）（[00:20:18]–[00:24:22]）。
- **不可变数据层 + experiments-as-code = 完美可复现**：能追溯到"哪个 cursor、哪个代码版本、哪个 token"；两年前的 run 现在还能精确重跑。花了约一年半才意识到工程不只是要快，而是**服务于严谨的科学过程**（真正的 ablation）（[00:27:22]–[00:29:22]）。
- **数据流式喂进训练**（just-in-time）：不再"打包→拷到集群→分发"，而是边训边物化；数据混配变成 config（"blender"服务：这个源 20%、那个源 10%）（[00:25:22]–[00:27:22]）。
- **零 on-call**：Laguna S 整个训练零 on-call 事件；唯一例外是新 run 前 6 小时因配错 config 需干预（[00:23:22]）。
- **agent 正在接管 model factory**：研究员屏幕上默认一堆 agent 在写代码、起 job、评估结果——"这就是 RSI 的雏形"，数据侧尤甚，正扩到架构侧；一个原本做 agent 的工程师半年内成了正经 RL 研究员（[00:21:21]–[00:22:22]、[00:36:25]）。
- **95% 的模型构建 = 改进数据 OR 改进算力效率**（其余是真正的突破研究）；"有无限算力大概明天就 AGI 了"（[00:34:25]–[00:36:25]）。

### Laguna S：行为比原始智能更能压榨小模型
- 118B 总参 / **8B 激活**（很稀疏），3:1 滑窗注意力:全局注意力，FP8 训练，**能装进 DGX Spark**、~30–40 tok/s；独立解出 Erdos 397（[00:38:25]、[00:55:30]–[00:56:30]）。
- co-head Peng 的原话（被反复引用）：**"Laguna S 的收益不是来自更多智能，而是来自不同的行为——更多验证、不轻易 take for granted、不过早宣布胜利、更持久。对成功而言这些比原始智能更有预测力，人也如此。"** Eiso 自称 10 天里每天花 8–10 小时读它的 trajectory（[00:37:25]–[00:39:25]）。
- **由此推出的商品化论证**：知识工作（占全球经济约 25%、$25T）靠的更多是"持久、回溯、查文档"而非"跨领域拼三个想法"（后者才需要 Einstein 级的大模型）。所以存在一个**知识工作的最优模型尺寸**：过了峰值再加大 ROI 就为负。这个峰值以前以为很远，Laguna S 让他改判**可能就在 1T/5T/10T**，不需要再大 2–3 个数量级——**这是开源能赢、模型会商品化的论证**（[00:40:26]–[00:43:27]）。
- **但明确不反对 scaling**："只有把模型 scale 到和竞争一样大我们才可能赢；'只做小开源模型之王'是自欺欺人的 copout"（[00:43:27]–[00:44:27]）。
- 上述行为**完全来自 post-training**；不同尺寸模型的 post-training 配方不能直接套用，但**大模型的配方套到小模型几乎总是很好的基线**（[00:44:27]、[01:43:03]–[01:45:06]）。

### 预训练没做完：RL 会越来越早前移
- **RL 前移进预训练**（早于 mid-training）：DeepSeek-zero 论文（约一年半前）已展示"很早就能诱导推理"；花了两年研究**如何把 web 从 next-token 变成"更早教模型思考"**，认为这里还有大量金矿（[00:44:27]–[00:47:28]）。
- 行业的"毒品"：**蒸馏**和**更多 environments**——好用、都上瘾，但"web 还远远没被压榨干净，光靠 next-token 预训练不够"；不确定"通往 AGI 的路就是无限堆 environments"（[00:46:28]–[00:47:28]）。
- **mid-training 只是 web 上一个很粗糙的两段式课程**：终极想要的是从 token 0 到 token 40T 的最优连续课程，只是算力/组织设计还不到位；"mid-training 存在是因为有了 mid-training 团队"（组织决定命名）（[00:48:28]–[00:50:28]）。
- 低精度是最兴奋的方向：ternary、NVFP4（点名 Nematron 的 NVFP4 训练被低估）；现在还在 10k H200（Hopper）集群、相对小，转 Blackwell 后会上 NVFP4/低精度 RL（[00:53:29]–[00:55:30]、[01:41:02]–[01:42:02]）。

### "MCP 和工具是愚蠢的"——模型该写代码，不该调 50 个工具
- **强观点**："我支持 MCP 也支持 tools，但它们对我毫无道理。"复杂长任务里，我们在模型和系统之间塞了一层 MCP/tool call；**应该给模型一个装好 binary 的虚拟机 + 一个可操作的 codebase + 一个写 memory 的文件夹，让它写代码（含 if/for/条件）去干活**（[01:10:45]–[01:13:45]）。
- 预测："**12 个月内不会再看到塞了 20–40 个工具的 system prompt。**"这是 Sinofsky/Steinberger"软件变 headless"的模型侧对应：模型自己写小脚本，而非编排预设工具（[01:12:45]–[01:13:45]）。
- Poolside 的 harness 极简：约 6 个工具（shell / shell kill / shell wait / write / fetch web / bash），这是首个做**并行 tool calling** 的模型（补课）（[01:02:36]、[01:13:45]）。
- **多 harness "polishing"**：小模型需要少量多 harness 训练，让自家 harness 里的行为迁移到别人的 harness（open code / kilo code / Hermes）；但 RL 算力都投在自家 harness（理解最深、科学最严谨），所以自家 harness 永远略好——"真在别人 harness 上做大量工作的人应该、也会超过我们"（[00:59:35]–[01:05:40]）。

### 模型公司，不是 agent 公司；聚焦是唯一的武器
- **定位**：Poolside 是模型公司（自 day zero 就是"AGI coding"）；押注 coding/长时程软件任务是通往 AGI 的路（逼你解决长时程、推理、外部工具/数据的硬问题），能力会泛化（这个模型没为 deep research 训过却很好用、legal bench 首跑就不错）（[01:05:40]–[01:09:43]）。
- **视觉理解是下一步**（现在完全没有），**音频很长时间不碰**——"说不 = 把研究员和算力留给通用进展"；语言是**信息密度最高的编码方式**（一篇 20 页物理论文的比特里编码了海量智能，视频/图像信噪比差得多）（[01:14:46]–[01:18:48]）。
- **拒绝蒸馏**：这些模型是"双用途"——既是自己 model factory 是否进步的检验、也是发布物；频繁从零训练（而非 6 个月一次）能避免"改进堆成一锅汤、分不清哪个配料起效"（[01:15:46]–[01:17:48]、[01:45:06]–[01:47:08]）。
- **naming 是基础模型公司最难的事**：Laguna XS / S / M / L / XL；如今 Mistral 的"small"都过 100B（"我们的 small 是 118B"）。Poolside 名字来自一次被迫换名的会议——"提醒我们永远别 round down 自己的野心、永远选更难的路"（[01:20:50]–[01:24:51]）。

### 监管、算力政治与竞争
- **监管观**：技术更强时应越来越**让位给民主**去决定；任何单一公司做单边决定都危险（权力集中、缺乏制衡）；要**区分 misuse 与 doomsday**；当前能力水平**不该以任何形式限制开源模型**，否则伤创新——但**会随真实风险场景改变立场**（[01:28:52]–[01:33:56]）。
- **香烟广告禁令类比**：禁烟草广告是好事，却也**给烟草业固化了寡头**（没人再能竞争）；"现在基于 2026 的模型能力，就决定这东西只有两三家能做——这读起来就像最反乌托邦小说的第 14 章"（[01:33:56]–[01:35:57]）。
- **Nvidia 比美国政府更有权力**（算力分配 → TSMC → 下面）；但 Eiso 认为 Nvidia 促进竞争、且受政府监管，与"政府用监管禁止别人做基础模型"性质不同（[01:35:57]–[01:37:59]）。也指出 Anthropic/白宫在限制"用我的模型做基础模型开发"——"这是资本主义、他们的权利，但我们对此 OK 很疯狂"（[01:28:52]）。
- **融资侧**：约一年半前融 $500M 时多数投资人还在争"是不是随机鹦鹉"；如今相信 AGI 的人呈指数增长，投资人分野变成**"相信智能寡头 vs 相信寡头能被打破"**——"认为只有两家的那群人，从年初到现在小了很多"（[01:24:51]–[01:27:52]、[01:37:59]）。

### 工程生产力与招人
- **唯一该看的是 lead time**：从"识别出有价值的事"到"交付给用户"的墙钟时间；其余（代码量、PR、review）都是先行指标。AI-native 公司的工程组织不像 pedalm 时代——常常就是**一个 builder 贴着客户**，中间没有大团队；要让参与人数更少、端到端时间更短（[01:47:08]–[01:51:08]）。
- **招人第一看 agency**（能动性）：AI 越强，agency 越是最重要的品质，且一定在过去经历里被展示过；对齐高 agency 的人靠**共同目标 + 明确边界（lanes）**，否则每个人都变成"探索算法"、陷入抢资源的政治（[01:50:08]–[01:53:08]）。
- **约束催生创新**：用相对少的算力和钱、买很少外部数据，反而逼出了别人没有的能力——"高 agency 的人你要放权，但也要说清'这些是我们不去的地方'"（[01:53:08]–[01:54:09]）。

### RL 是墙钟瓶颈：把 PD 解耦引入 RL 训练
- **RL 是 batch-size 受限的**（任务数有限，不像整个 web 可无限放大 batch），所以**不能像预训练那样堆 GPU 扩算力**；RL 时间是当前最大的墙钟瓶颈（[01:37:59]–[01:41:02]）。
- 兴奋点：把推理侧已在做的 **prefill/decode 解耦（PD disaggregation）、混搭异构硬件**（GPU + Groq/LPU 类专用芯片）引入 RL 训练——"这是当下能给行业提速最大的事之一，因为竞赛是按日历时间算的"（[01:37:59]–[01:41:02]）。详见 [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)。

## 相关主题

- [AI 商业化与价值捕获](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-business-and-value-capture.md)（"100 家 vs 5 家"、知识工作最优模型尺寸、商品化论证、智能寡头 vs 可被打破）
- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（Model Factory、行为 > 智能、RL 前移预训练、mid-training 是粗课程、拒绝蒸馏、频繁训练避免"soup"）
- [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md)（工厂化研究、agency、约束催生创新、聚焦/blinders、从零起步的资历劣势变优势）
- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（西方开源前沿实验室、致敬中国开源研究、开源紧咬前沿的价值分配含义）
- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（RL 的 PD 解耦、低精度训练 NVFP4/ternary、10k H200 集群、Nvidia 算力政治）
- [使用 LLM 的方法论](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)（MCP/工具"愚蠢论"、minimal harness、模型写代码替代工具编排）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
