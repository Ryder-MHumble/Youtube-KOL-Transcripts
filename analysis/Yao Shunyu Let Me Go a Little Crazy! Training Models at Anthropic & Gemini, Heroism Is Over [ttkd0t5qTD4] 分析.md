---
title: 'Yao Shunyu: Let Me Go a Little Crazy! Training Models at Anthropic & Gemini, Heroism Is Over（外部迁移分析）'
source: repository_import
youtube_url: https://www.youtube.com/watch?v=ttkd0t5qTD4
video_id: ttkd0t5qTD4
transcript: '[[Yao Shunyu Let Me Go a Little Crazy! Training Models at Anthropic & Gemini, Heroism Is Over [ttkd0t5qTD4]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260511-zhang-xiaojun-yao-shunyu.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[Yao Shunyu Let Me Go a Little Crazy! Training Models at Anthropic & Gemini, Heroism Is Over [ttkd0t5qTD4]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=ttkd0t5qTD4) · 视频 ID：`ttkd0t5qTD4`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260511-zhang-xiaojun-yao-shunyu.md)

## 迁移说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面迁移生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 中方长视频里罕见的、由一线前沿模型研究员给出的技术+组织双重内部视角。姚顺宇学理论物理出身，先后在 Anthropic（做大规模 RL、参与 Claude 3.7）和 Gemini（ML coding、long horizon）训模型，因此本期是**中美三大实验室（Anthropic / OpenAI / Google DeepMind）横向对照**的第一手材料。本库据此把 [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md) 与 [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md) 两个主题大幅补全。

## 概要

覆盖当前 AI 阶段判断、模型同质化与差异化、预训练 Scaling Law 是否到头、coding 为何最快、程序员命运、中美模型差距与蒸馏、字节/豆包、机器人、三大实验室的组织文化对照、TPU vs GPU、个人成长（物理→AI）、以及"个人英雄主义已过去"的世界观。

## 核心观点

### 当前 AI 阶段：从"能不能做到"到"是否被良好定义"
- 一年前大家还担心"追不上 OpenAI 的 reasoning"；现在 Gemini/OpenAI/Anthropic 三家**没有谁真担心自己追不上**。更难的事变成了"想明白要做什么"——是个 bet，也需要人的 insight（[00:05:12]–[00:06:13]）。
- 模型能力被拉平、同质化、商品化：**纸面 benchmark 趋同**（SWE-bench 大家都在 80% 附近，高低"主要是噪声不是信号"）；但实际体验仍有区别——Claude 通用工具使用/Agent 最强，Codex 纯 coding 最近追上一点，Gemini 纯 reasoning 与日常使用较好（[00:06:13]–[00:09:19]）。
- 差异过去主要来自**意愿**（愿意投精力搭 infra、备数据）；现在意愿和能力都有，且很多差异来自"想象不到的"细节（如早年不做筛选时 GitHub 代码天然质量更高）（[00:09:19]–[00:10:21]）。

### OpenClaw / Manus：模型能力的自然溢出
- OpenClaw 在业外讨论比业内激烈；对业内"不是特别令人惊讶的事"——是模型能力（去年 Claude Opus 4.5 的 tool use）的**自然溢出**，Google 内部早有人做类似 demo，只是大公司流程长、要负法律/品牌/资源责任，不便发（[00:11:21]–[00:14:23]、[00:21:26]–[00:23:31]）。
- "壳"难逃模型掌心，生存只有两条路：**长得够快**（在模型公司反应过来前占领用户心智并演化出自己的模型，Cursor 在走这条路且已很有危机感）或**市场够小**到模型公司懒得管（Midjourney）（[00:16:24]–[00:19:25]）。
- 目前除 **Agentic coding** 外，没有哪个场景是"AI 真正原生"且形成数据飞轮的；Chatbot 本质是搜索的交互式延伸（[00:15:23]–[00:16:24]）。

### 预训练 Scaling Law 没到头
- 作为一线研究员，认为模型进步速度"完全没有放缓"；判断标准是"模型学东西的能力越来越强了"（[00:24:32]–[00:26:32]）。
- 关键论断：**过去几个月预训练其实变强了**，未来 4 个月也没看到到头迹象。觉得"撞墙"的人多半是三种情况之一，而**绝大多数是第三种——工作里有个自己没发现的 bug**（另两种是误判适用范围、或某个条件如数据被认为撞墙）（[00:26:32]–[00:29:35]）。
- 应对之道不是玄学而是**做事系统**：设计合理的 ablation 实验、系统性排除各种可能因素——"Gemini 和 Anthropic 在预训练上做得比较好的正是这件事"（[00:29:35]–[00:30:37]）。
- 驱动力：算力与数据强关联；算法作用是**相变式**的——Transformer 那种"从完全不能做到能做"的跳变之后，更多是平滑的效率提升。语言生成已不是科学问题（工程上还有很多要做），但**多模态生成仍是科学问题**（[00:31:39]–[00:33:41]、[00:44:51]）。

### Coding 为什么发展最快
- 三个结构性优势：**回馈信号清晰**（输入→输出可测）、**GitHub 提供天然优质数据基础**、**产品需求单一**（好代码有共识标准：简洁、结构清楚、合理抽象）（[00:35:42]–[00:38:49]、[00:47:54]–[00:49:54]）。
- 自述：保守估计 **90% 的代码由模型产生**（"不保守就是 99% 或 100%"），最重要的工作变成设计逻辑、给合理 context、审查代码是否合理；做实验/实现 idea 的效率比一年半前"提升 20 甚至 50 倍"，但工作时间反而更长、密度更高——"越试越想试"（[00:38:49]–[00:42:50]）。顺带："Google 不能用 Claude Code"（[00:37:46]）。
- coding 之后哪爆发？看好但难成"市场热门方向"的是**基础科学**：数学/理论物理研究者已大量用 AI（Gemini Deep Think 做推导/证明/文献归纳），只是难万众瞩目，除非出现"AI 产生爱因斯坦级理论"的时刻（[00:42:50]–[00:44:51]）。

### 程序员与就业
- AI 会取代程序员，但是**渐变**而非隔夜（已有公司裁员）。AI 是一种 **centralized technology**：让少部分人更强、让大部分人失去独特价值——传统软件工程的终局可能是"1/1000 的人干过去所有人的活、拿 100 倍工资"（自称著名悲观主义者，也强调 1/1000 是虚数）（[00:45:51]–[00:48:54]）。
- 未来"活下来"的程序员三特质：技术强（充分非必要条件）、理解自己的工作如何嵌入大组织、规划能力强（能把复杂事拆解交给不同 AI）——"可能 6 个月后这些 AI 也能干了，我的回答会更悲观"（[00:47:54]–[00:49:54]）。
- **为什么 AI 先做人类觉得最难的事**（数学/代码/科研）：因为这些"理性、客观"的事一旦想清楚怎么评价就知道怎么训练；反而**产品经理很难训**——没有客观标准、回馈信号不明确（[00:44:51]–[00:46:52]）。

### 中美模型差距与"蒸馏"
- 快照（2026 Q1）：过去一年半中美 gap **明显缩小**，但会不会完全弥合甚至反超"不清楚"（[00:53:01]–[00:54:04]）。
- 中国算力劣势"逼出了有趣的事"——对**蒸馏**很在行。区分两种：**硬蒸**（直接取 Claude 的 token 强行训练，"商业上不道德、智力上愚蠢"，说明这家公司自己都不知道要干嘛）vs **软蒸**（用别家模型做生成链条的辅助或评价者，商业灰色但技术有趣）——他认为中国实验室因此**可能成了真正 Multi-Agent 训练的先驱**（不同家模型分布不同）（[00:54:04]–[00:57:05]）。呼应 Dario 点名 3 家蒸馏 Anthropic 一事。
- 字节蒸馏得少、模型有特点：**豆包语音生成"是全世界最好的之一，不客气说就是最好"**、生成快、不强推思维链——差异源于用户群体（美国专注工作效率，中国重日常）（[00:57:05]–[01:03:10]、[01:02:10]–[01:04:11]）。字节多模态生成（Seedance）优势"猜是数据占大头"、非范式变化；评价吴永辉"层级高、senior 却技术很强，非常少见"（[00:49:54]–[00:53:01]、[01:03:10]）。

### 机器人
- 硬件成熟且便宜得惊讶（体现中国供应链优势），但**软件/模型还在 feature engineering 时代**：给定单一场景能优化，但没有泛化性——"还没到语言模型的 GPT-1 时刻"。方向是拿语言模型做基底训 VLA（视觉-语言-动作）（[01:03:10]–[01:08:13]）。

### 三大实验室的组织文化对照
- **Anthropic**：执行力极强、top down、reactive 快。能"make bets"（重注 coding）的独特条件是——技术 1 号位（cofounder Jared Kaplan、Sam McCandlish）既有技术公信力又能为公司负责，CEO 不成阻力，且 cofounding team 互信（"一起趴过战壕"，是 Scaling Law / GPT-3 论文合著者，没一个人离开）。"这对其他公司很难，OpenAI 就干不了"（[01:59:54]–[02:06:58]、[02:31:21]–[02:36:24]）。
- **Google DeepMind**：传统 bottom up 大公司打法，"我不赌、方方面面都有储备"；现在**预训练变得非常 top down/清晰**（进入 Google 工程管理的舒适区、可预测），后训练仍更 bottom up。最终拍板人是 Sergey Brin；一线是 Koray Kavukcuoglu（DeepMind CTO / Google SVP）；Demis 更管偏 science 的事（Isomorphic Labs）。Google 擅长"极简产品形态 + 疯狂卷技术"（搜索），但产品慢（[02:33:22]–[02:34:22]、[02:48:33]–[02:56:40]、[03:12:51]–[03:13:56]）。
- **OpenAI**：文化上"踏实做事的人没 Gemini 多、更没 Anthropic 多"，是他没去 OpenAI 的主因；曾把预训练当"第一个挖完的金矿"而卡了很久（[02:14:05]–[02:15:08]、[02:49:34]）。
- 组织哲学：最好的状态往往最不稳定，需要一个**技术 leader**来控制、把 bottom-up 的创新与秩序融合——组织好坏"归根结底是技术 leader 的问题"；好 leader 两特质：能亲自下场救火、能理解并容纳别人做自己不做的事（[03:18:59]–[03:20:59]）。

### 离开 Anthropic → Gemini
- 主因是想学不一样的东西（Anthropic 不做多模态生成、不太做底层工程 infra），加上公司变大后文化受冲击（有人在 Slack "讲大道理，idea is cheap"）；**不认同 Dario 反华**是"很大但非控股的原因"（公开场合说约 40%）（[02:23:19]–[02:25:19]、[02:53:37]–[02:55:37]）。
- 选 Gemini 而非 OpenAI/xAI：文化与人的亲近感 + 研究自由 + 能从更广泛的人学习（[02:25:19]–[02:27:20]、[02:49:34]）。

### Gemini 的转折
- 两件事叠加让 Gemini 成为举足轻重的玩家：**Nano Banana**（爆款把量打起来）+ **Gemini 3**（把人留下），市占约 20%（[01:49:45]–[02:52:37]）。
- 犀利判断："**OpenAI 救了 Google 一命**"——先做了 chatbot 让 Google 意识到搜索危机，却没做到极致、没干掉搜索，反让 Google 追上来（[02:52:37]–[02:54:37]）。

### 系统、黑盒与"AI 本质上简单"
- "所有东西都是黑盒"，物理也是；**Scaling Law 是经验规律**，类比热力学定律，未来理解微观机制后可能变"科学规律"；"智能涌现"是主观感觉/技术涌现（能水平提升所有能力），非行为涌现（[01:44:41]–[01:47:43]）。
- **"AI 本质上简单"**——因为它能做实验、不被"能标"束缚（不像高能理论没有对应能标的实验数据就理解不了）。现在不是没想法可试，而是**想法太多、要一个个试、花时间**。预测未来 6–12 个月 **AI 会开始自己做实验**（完整链条：写码→跑→看结果→分析→提假设→设计新实验）（[02:35:24]–[02:37:25]）。

### TPU vs GPU
- 大规模商用无绝对优劣。设计理念差异：GPU（Hopper/H 系列）一个 pod 内约 8 卡两两 NVLink 高速互联；TPU 抛弃两两互联、采 **3D Torus 拓扑**，尽量多卡放一个架子，编译器/sharding 写得好则等效更大存储 + 减少通信 bound。TPU 劣势：小 scale 更固定、通用性弱、无开源生态（但大规模自用时生态不是问题）（[03:20:59]–[03:23:02]）。

### 中美生态差异（C 端 vs enterprise）
- 中国强 **C 端**：能想出"很间接、很不自然却能滚起利润"的复杂产品（抖音免费看视频 + 广告 + 直播 + 电商）；美国强**直接的效率软件/enterprise**（写码成本 150 卖 200，直接挣 50）（[03:24:04]–[03:27:05]）。
- 2026 国内看重 super app / C 端叙事，硅谷不讲（美国 enterprise 市场大、利润高，C 端"没油水"）——"中美趋势已分化，整个互联网时代就不一样"。**字节被严重低估**，美国没公司能在 C 端与字节竞争，Meta 从字节挖人但学不来（[03:13:56]–[03:14:56]、[03:24:04]–[03:28:05]）。

### "个人英雄主义已过去"
- LLM 的个人英雄主义时代结束于 Transformer 那一刻之后：**"每个人都是冲浪的人，本质上是一个浪（AI），而不是那个冲浪的人"**——浪都会拍到岸上，只是有人赶上浪尖。AI"不太需要脑子"，最重要特质是**靠谱、做事细、对自己做的事负责任**（[03:04:45]–[03:05:46]、[03:29:08]–[03:30:09]）。
- 系统性做 AI 需要"reliable、为公司全局负责"的人，因为任何评价框架都容易被 hack；这与学术界"为自己项目负责"是两种心态（[03:14:56]–[03:18:59]）。
- 招人面试题：**24 小时从 0 到 1 做一个 RL 项目 + 1 小时讨论**——考察能否有效利用 AI、是否真理解 AI 做了什么（全盘扔给 AI 会在讨论中露馅）、以及有多看重这个机会（[03:31:10]–[03:33:11]）。
- 给年轻人：纯做语言模型已不是蓝海（"末班车已发车，我自己就是末班车"），应做"现在没人做到的事"——多模态生成、机器人、AI for science（如量子调控）（[03:33:11]–[03:34:12]、[03:22:01]–[03:23:02]）。

### 个人成长与观点风格
- 宁夏大武口出生 → 上海 → 清华机科班（物理）→ 斯坦福理论高能物理 → 伯克利博后两周 → Anthropic 一年 → Gemini。本科在清华高研院随汪忠做**非厄米系统/拓扑**（自评"范式级"工作）；博士高能理论"学了很多但对世界几乎零贡献，买了个大教训"——要做**有客观评价标准、对世界有影响**的事（[01:08:13]–[01:10:13]、[01:19:22]–[01:27:28]、[01:35:35]–[01:40:40]）。
- 物理对做 AI 的帮助"硬实力上几乎没有"，主要是性格（刨根问底、系统性）；Anthropic 早期多物理出身其实主因是 connection（创始人做物理）（[01:42:40]–[01:43:40]、[01:52:47]–[01:53:47]）。
- 说话直接、"厌蠢症"、恨"老登"（不懂还爱指手画脚）：因为 AI 领域客观、没有导师旧友的负担，"想喷谁喷谁"（[03:28:05]–[03:29:08]、[03:39:16]–[03:42:17]）。崇拜：物理有（Haldane 的远见、Douglas Stanford 的聪明），AI 没有——但 Hinton 算英雄级、Transformer 八作者是"英雄集体"（[03:27:05]–[03:28:05]、[03:38:16]–[03:39:16]）。
- 关键 bet：**long horizon**（"train with finite context, use as infinite context"）；影响 AI 的论文点名 seq2seq 与 Scaling Law（[03:45:19]–[03:46:21]、[02:41:31]–[02:42:32]）。

## 相关主题

- [中美 AI 生态对照](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/china-us-ai.md)（本期是中方视角的主来源）
- [AI 实验室文化与组织](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-lab-culture.md)
- [LLM 训练管线](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-training-pipeline.md)（预训练 Scaling Law、后训练 RL、3.7 分水岭）
- [评估与 Benchmark](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/evaluation-and-benchmarks.md)（纸面 benchmark 趋同）
- [AI 与就业](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-and-jobs.md)（渐变取代、centralized technology）
- [LLM 实用方法论](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)（coding 占 90%）
- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（TPU vs GPU）
- [AI 与科学发现](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-for-science.md)（基础科学用 AI）

## 深度关联

- 语料层关联：[[KOL语料库对比与迁移评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的迁移状态与该评估保持一致。
