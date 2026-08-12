---
title: Open Source Wins, AGI Is Here, and Scorsese’s AI Toolkit with CEOs of Cerebras & Black Forest Labs
source: repository_import
youtube_url: https://www.youtube.com/watch?v=Y7p4rUCdqi0
video_id: Y7p4rUCdqi0
transcript: '[[Open Source Wins, AGI Is Here, and Scorsese’s AI Toolkit with CEOs of Cerebras & Black Forest Labs [Y7p4rUCdqi0]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260710-all-in-cerebras-bfl-open-source.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Open Source Wins, AGI Is Here, and Scorsese’s AI Toolkit with CEOs of Cerebras & Black Forest Labs [Y7p4rUCdqi0]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=Y7p4rUCdqi0) · 视频 ID：`Y7p4rUCdqi0`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260710-all-in-cerebras-bfl-open-source.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 两段访谈：Cerebras 的 Andrew Feldman 谈 AI 大基建、推理即算力、开源与主权、分阶段发布、递归/loop maxing 与丰饶叙事；Black Forest Labs 的 Robin Rombach 谈 latent diffusion → 多模态 → action prediction → 机器人，以及与 Scorsese 的合作、生成式影视与 IP。Feldman 的另一维度补充见其[人物页](https://github.com/nolimitkun/ai-kol-wiki/blob/main/people/andrew-feldman.md)（已收录 [No Priors 访谈](20260521-no-priors-cerebras-feldman.md)）。

## 核心观点

### Andrew Feldman / Cerebras：基建、推理与 Moore's law
- **史无前例的 buildout**：数据中心未来几年用电将超过"地球过去 50 年"，单栋建筑用电超过中型城市；遍布美/加/北欧/中东/哈萨克/亚美尼亚等；买家（OpenAI/Anthropic/SpaceX AI/Google）"永不满足"，**在追赶昨天的需求**（Cerebras 有 **$250 亿 backlog**）（[00:01:00]–[00:04:02]）。
- **token maxing 有价值也有实验**：类比早期 AWS/Costco——一开始"随便刷 token"，如今企业开始像做生意一样按难度路由（难题用前沿、普通题用便宜/开源）；涌现出"会部署这项技术、懂系统思维"的人（[00:04:02]–[00:07:03]）。
- **推理即算力**：从"猜下一个词/总结 PDF"到"理解意图→定策略→与其他 agent/线程互评"；reasoning 是 inference、极耗 token，正好喂给 Cerebras 这种极快机器（Hermes agent / GLM 52 无限算力时能看到 reasoning 模型"自我辩论"去哪找信息）（[00:07:03]–[00:11:06]）。
- **推理的 Moore's law**：所有前代芯片遵循 18 个月翻倍，Cerebras 打破它——未来 18 个月"远超 2x"；新架构还有大量优化空间，20 年老架构（GPU）只能靠更小制程（[00:12:06]–[00:13:06]）。
- 为何 OpenAI/Amazon 自研芯片：**没人喜欢依赖**（x86 时代依赖 Intel、GPU 时代依赖少数超算的教训）；不必造最快的芯片，只是不能完全依赖别人的芯片（[00:14:07]–[00:16:09]）。

### Feldman：开源、主权与分阶段发布
- **开源今年闭合了 gap**：Jason 从 openclaw 转 Kimi 后"分不出差别"、smart routing 后开源也会 reasoning 了；"不会开法拉利去买菜"——难题用前沿、日常用开源（[00:16:09]–[00:17:09]）。
- **主权是趋势**：Cerebras 跑 GLM/Kimi/Qwen + OpenAI 闭源 + GSK/G42/MBZUAI 自研模型；美国需要更多**本土开源模型**（现只有 OSS 12B 或中国模型可选），给世界一个选择（[00:18:11]–[00:20:12]）。
- 对政府介入 fable/56 的**分阶段发布**：不确定时机对不对，但"模型强到有意义威胁时，政府要求分步放出并不 unreasonable"——类比强效药/FDA、给 NSA 两三周补洞、iPhone beta 里有你 opt 不进去的安全 beta；**极化伤害清晰思考**（换成 AOC 总统也一样该想）；行业该更好地**自我监管**，但"他们也在边跑边发明规则、没有 playbook"；Palo Alto Networks 用新模型对自家软件"发现从不知道的 bug、停工打补丁 6 周"——快芯片能让 guardrail 不那么痛（[00:20:12]–[00:26:21]）。
- **必然会有大数据泄露**（像再保险/黑天鹅），要提前储备、想好响应；"AI 会告诉你没在问的问题"——Feldman 现在 prompt 结尾固定加"检查你的工作 + 告诉我我没考虑到什么 + 每次运行都反问我几个问题"（[00:26:21]–[00:28:22]）。

### Feldman：AGI 已至、递归与丰饶
- **"AGI 我们已经命中，只是没完全部署"**：任何 20 年前的定义（图灵测试等）都被碾过；该听那些"听起来在边缘"的人（Ilya 谈安全、Elon 谈火箭降成本，都对了）（[00:29:22]–[00:30:23]）。
- **递归/loop maxing**：Sam/Ilya/Dario/Demis 五六年前看到的是"递归增益是指数的"——问→学→再问，答案不是好一点而是好很多，"不知道它在哪停"；当问题从智力问题变成**人的问题**（如何组织人、动机），领导者"给团队喷 WD40"（[00:30:23]–[00:33:23]）。
- 用"跨代传承"类比：凡尔赛宫由几代同一石匠家族建成、传承学习；AI 把"每代 15–20 年"压缩成"果蝇一天两代"、跨千代地学；范式不会死、是持范式的人死了（[00:34:23]–[00:37:24]）。
- **丰饶叙事**：有机会让"我们的孩子或他们认识的人无人死于癌症"；会有像汽车取代马车般的错位，但对账（无限能源/卡路里/知识/教育/住房）后是丰饶；教育该像亚里士多德教亚历山大的一对一导师制，而非"工厂化教到中位"（[00:37:24]–[00:40:28]）。

### Robin Rombach / Black Forest Labs：diffusion → 机器人
- 出身：latent diffusion 发明者（PhD 在慕尼黑）——把图像/视频/音频**压缩成高效表征再训 transformer**（JPEG/MP3 的神经版），是所有生成模型的底层算法；做过 Stable Diffusion，开源 **Flux**（Freiburg + 旧金山双基地，刚过 100 人、在招）（[00:40:28]–[00:42:30]、[01:01:47]–[01:02:48]）。
- **收敛到多模态 world-action model**：同一模型做图/视频/音频 + **action prediction**，最终可部署为机器人大脑；"要生成世界的视频，你必须理解世界"——直觉智能（图像入手、算力低）+ 深度推理层，两者互补（[00:42:30]–[00:44:32]）。视频预训练给出对物理/交互的隐式理解→可产出 action prediction/机器人（[00:44:32]）。
- 生成"老虎机"批评的解法是**暴露尽量多的操控层**：从 text→image 扩展到 text+image→image（编辑/迭代）、多图语义合成，同原理推广到视频，输入输出都在同一模型时更有意思（[00:44:32]–[00:46:33]）。
- **Scorsese 合作**：与"活着最伟大的导演"同室，看他探索模型——把脑中场景（东欧村庄）迭代成图像帮助沟通，"语言是有损媒介、视觉信息更丰富"；他不认为终极目标是"用视频模型生成整部电影"，而是**human-in-the-loop 当作媒介**、平行化 brainstorming/storyboard（Ridley Scott/Spielberg/Lucas 都做 storyboard）（[00:46:33]–[00:50:39]）。
- 生产落地：创业公司花一两周和导演做 launch video（原本 $25 万）；一部"比特币电影"在 sound stage 无绿幕拍、背景全用生成式 AI（$3000 万预算，否则要 $1.5 亿、根本不会被 green-light）——高端影视是最苛刻用例，技术在快速改进的轨迹上（[00:50:39]–[00:53:41]）。
- **开源 + IP**：给 Disney 等 IP 方的建议是共同训练模型（部分基于开源、部分基于更强的闭源）；公开工具**限制生成特定 IP**是合理做法；最有意思的是**粉丝二创**（Star Wars 同人从 fanfiction→fan film→AI 重现未讲过的故事，"Star Wars Stories Untold"百万播放），让 IP 方通过授权费赋能创作（[00:57:45]–[01:01:47]）。

## 相关主题

- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（本期核心：史无前例 buildout、推理即算力、推理的 Moore's law、超算/云自研芯片去依赖、主权、开源模型运行）
- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（开源 gap 今年闭合、跑 GLM/Kimi/Qwen、美国缺本土开源模型、"若中国先有强模型"作为分阶段发布变量）
- [物理 AI 与机器人](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/physical-ai-and-robotics.md)（latent diffusion→多模态 world-action model→机器人大脑、视频预训练给物理理解、in-context 提示机器人）
- [AI 商业化与价值捕获](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-business-and-value-capture.md)（Cerebras 纯 AI play/backlog、生成式影视重排成本结构、开源+IP 授权、粉丝二创商业化）
- [使用 LLM 的实践](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)（token/loop maxing、prompt 结尾"检查工作+反问我"、reasoning 模型自我辩论、human-in-the-loop 当媒介）
- [AI 与就业](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-and-jobs.md)（错位 vs 丰饶叙事、导师制教育、问题从智力问题变人的问题）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
