---
title: "Matan Grinberg- 暗厂不是全自动编程幻想，而是软件组织的会计系统"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=ZesOukBjPmI"
transcript: "[[Factory's Matan Grinberg The Coming ‘Dark Factory’ Where Software Builds Itself]]"
tags:
  - kol情报
status: canonical
created: 2026-07-30
---

> Matan Grinberg 这场访谈的核心不是“AI 会写更多代码”，而是把企业软件开发从手工业流程改造成可计量、可路由、可反馈的生产系统：模型只是劳动力，harness、token 分配和业务反馈闭环才是暗厂的控制层。

视频链接：https://www.youtube.com/watch?v=ZesOukBjPmI

对应逐字稿：[[Factory's Matan Grinberg The Coming ‘Dark Factory’ Where Software Builds Itself]]

## 概述

Matan 的位置很特殊：Factory 既不是前沿模型实验室，也不是传统企业软件公司，而是在 Claude Code、Codex、Cognition 和企业自建 agent 之间做“软件工厂”的控制层。因此这场 Sequoia 访谈真正有价值的地方，不是他预测更多代码会由 AI 生成，而是他给出了企业为什么需要一个独立于模型实验室的 agent harness。

他的反命题很清楚：OpenAI/Anthropic 的模型 + harness 垂直整合在实验室内部看起来合理，但企业最怕的是把命运交给单一模型提供商。Factory 的赌注是，多模型 harness 会比单模型共设计更强，因为它不会过拟合某个模型的脾气；router 会把不同 token 分配给不同任务；最终软件开发会从同步 copiloting 迁移到异步暗厂。

这篇应放进三条线：企业 AI 集成鸿沟、价值捕获层级、Scaling 天花板的具体机制。它把前几篇里分散的判断连起来：Andrew Ambrosino 说实现成本下降后产品工作被倒置，Anthropic 平台团队说价值迁移到 strategy layer，Sinofsky 说企业软件真正价值在 system of record 和例外处理。Matan 给出的补充是：如果企业要把 AI 真正接进软件生产，它必须先把软件生产本身变成可观察、可审计、可分配预算的系统。

## 企业要的是模型独立，而不是第二个锁定点

访谈开场的竞争问题很快转成企业信任问题。Matan 说大企业当然会试 Claude Code 和 Codex，但它们不会把自己的软件生产命运交给任何一个模型实验室。

> **[2:33]** "they do not want anyone to kind of be their single point of failure"

这个判断不是普通多供应商采购，而是企业从云时代带来的制度记忆。AWS/Azure 的三年合约和续约涨价让企业知道，单点依赖最终会变成迁移成本。因此 Factory 的 model independence 不只是兼容更多模型，而是在企业 CIO 面前提供一个可解释的控制面：新模型更快、更便宜、更可靠时，可以热切换；某个模型实验室发生治理、价格、政策或供给波动时，企业不被锁死。

这也解释了 Factory 为什么要强调 artifacts 留在客户代码库里。主持人追问“是不是只是从模型锁定变成 Factory 锁定”，Matan 的回答是：automations、skills registry 和 artifacts 都留在客户侧，不把组织知识变成供应商私有资产。这一层信任建设，比单次 benchmark 更重要。

## 早两年等于错：产品时机比愿景正确更残酷

Factory 的早期故事给 AI 产品一个现实校准。Matan 承认他们 2023 年就押注 fully autonomous agents，但企业工程师、采购、模型能力和行为习惯都没准备好。主持人说你们愿景很早，他给出的回答很冷：

> **[5:24]** "being 2 3 2 or 3 years early is the same as being wrong"

这句话和 Andrew Ambrosino 的“模型时机成为产品变量”是同一类经验。AI 产品不是只要方向对就能活下来；如果产品承诺领先于模型可靠性和用户行为太多，它在市场上就是错误产品。

Factory 更极端的一步是主动退还接近 200 万美元收入。Matan 的理由不是道德叙事，而是产品信号：销售可以签单，但开发者没有爱上产品，收入只是延迟爆炸的定时炸弹。

> **[7:56]** "we proactively gave all of those customers their money back"

这里的行业信号是：agent 产品的 PMF 不能只看 CIO 采购或董事会 AI 压力，必须看一线开发者是否愿意把真实工作交给它。企业 AI 的扩散路径仍然需要个人行为层的信任，不能只靠 top-down 指令。

## Droid CLI 的转折：模型变强和开发者放下戒备同时发生

Matan 不把 2025 年 9 月 Droid CLI 的成功完全归因于模型变强。他认为交互形态的降低门槛同样重要：从 fully autonomous agents 退到 CLI，让开发者在熟悉环境里使用 agent，而不是要求他们一次性改变整个工作方式。

> **[15:50]** "The model's getting better, so you need to do less in the way of providing guardrails"

但这只是半句。另一半是开发者降低防御，开始接受 agent 会做出自己不喜欢的改动，并学会提供 guardrails。Karpathy 对 agentic work 的公开认可也被 Matan 视为行为改变的真实触发器。这里的隐含立场很明确：AI 产品采纳不是纯理性性能曲线，而是模型能力、交互形态、同侪信号和可信 KOL 背书共同推动的行为迁移。

这对企业推广很重要。先让所有人“必须用 AI”会造成 token maxing；先把工具放回开发者熟悉的 terminal 里，才可能形成真实习惯。Factory 的 CLI 不是 UI 选择，而是 adoption strategy。

## 多模型 harness 的反直觉：模型越多，harness 越不容易过拟合

这场访谈最有技术密度的段落，是 Matan 反对 model-harness co-design 的直觉。他承认很多人会认为实验室同时训练模型和构建 harness 会更强，但 Factory 的经验相反：

> **[19:27]** "If you build a harness that supports different models, that harness will be better."

他的类比很锋利：

> **[20:00]** "what data is to a model, models are to a harness"

意思是：模型吃的数据越多，泛化越好；harness 暴露给越多模型，越不容易只适配某个模型的偏好。Opus 可能会主动删掉不必要任务，GPT 5.6 可能会机械完成全部列表；如果 harness 只为单一模型优化，就会把模型脾气写进产品结构。多模型 harness 反而迫使产品抽象出更稳定的用户体验、任务状态、tool use、compaction 和待办保持机制。

这和 Anthropic 平台团队的“strategy layer”形成紧张关系。Anthropic 认为策略层是平台 alpha，Matan 则认为独立 harness 的 alpha 来自跨模型暴露。两者并非简单冲突：Anthropic 的策略层适合优化 Claude 生态内 token 工作分配，Factory 的策略层适合企业在多个模型之间做鲁棒调度。企业最终可能不会只买“最强模型”，而是买“能让模型不重要”的控制层。

## Open models 的份额信号：大多数 token 会走向便宜可替代模型

Matan 对开源/开放权重模型的判断很实用：不要拿 GLM 5.2 和最新前沿模型比，而要和前沿上一代比。企业真实问题不是“谁是绝对最聪明”，而是“某个任务是否需要爱因斯坦级 token”。

> **[27:37]** "half of our tokens are open to open models"

他进一步判断，open models 会向 token share 的大多数逼近，但不会占据全部 leverage share。高价值、复杂决策仍需要前沿模型；大量实现 token、低风险 token、特定代码库 token 会被更便宜的模型吸收。

> **[30:52]** "the frontier of intelligence will inherently always be valuable"

这提供了一个比“开源是否追上闭源”更好的口径：token share 和 leverage share 必须分开。开放模型可能拿走大多数 token，但前沿模型仍可能拿走最关键的判断时刻和最高毛利。对企业来说，router 的价值不是省钱本身，而是把 token 预算按任务风险、组织职能和验证强度重新分配。

## 从 token 到 dollar：CIO 要回答的是算力和人力的边际分配

Factory 的商业模式讨论不是简单 usage-based 定价。Matan 认为 seat-based 对这种产品不合理，usage-based 是当前阶段，但长期会走向 outcome-based。原因是 agent 任务天然带验证条件：你不是让模型“写点代码”，而是给它任务、测试、验收标准和失败边界。

> **[32:53]** "usage-based is clearly the way to go"

但他又立即踩刹车：

> **[33:11]** "We are not going to impose things"

这句话透露出 Factory 早期失败的教训：企业没准备好时，不要把未来商业模式强塞给客户。真正的迁移顺序是：先让企业从无 router 到有 router，再进入自然语言 routing procedure，再从 token 预算变成 outcome 预算。

最关键的问题在 [38:04] 之后。Matan 说今天 CIO 问“每个增量 token 放在哪里”，两年后会变成“每个增量 dollar 放在哪里”：

> **[38:04]** "where do you put every incremental dollar?"

这就是暗厂的会计意义。企业过去按 headcount、部门预算和项目优先级分配资源；AI 之后，tokens 成为可观测的劳动力投入。某些组织节点加 token 比加人有效，某些节点加人比加 token 有效。没有软件工厂的反馈闭环，企业只能凭感觉裁员、扩招或买模型。

## 暗厂不是无人编程，而是把软件生产变成可反馈的装配线

Matan 对“software factory”的定义比标题更克制。他不是说每家公司都还没有软件工厂，而是说每家公司已经有一个，只是效率极低：

> **[36:16]** "everyone has a software factory whether they know it or not"

大型组织里，一个 feature 从信号到发布可能穿过几百上千人，连流程图都画不出来。软件工厂的意义不是让机器人替代所有人，而是把客户输入、市场输入、产品领导判断、审批、代码生成、验证和业务结果连成可观测链路。

> **[38:24]** "you need kind of more rigor and more process"

这和“AI 让流程消失”的叙事正相反。Matan 认为 AI 时代反而需要更多 rigor 和 process，因为只有这样才能知道哪个 feature 没带来留存、哪个部门给 token 有回报、哪个业务需要人际关系而不是更多推理预算。他把公司类比为 AGI，组织节点、load-bearing 人、tokens 和 humans 都要被优化；这其实是把软件组织变成可反向传播的系统。

这里有一个危险信号：如果企业把 AI 当成裁员口号，而不是当成资源分配仪表盘，就会“shooting from the hip”。Matan 对 20,000 人裁员没有科学依据的批评，说明他并不支持简单自动化替代论。他支持的是更数学化的资源重分配。

## 90% 异步 token：真正的 agent-native 从人类不在场开始

Matan 对未来 12-24 个月最明确的预测，是 AI consumption 从同步迁移到异步。今天很多 Claude Code/Codex/Droid 使用还是“人叫一下，agent 做一下”；如果所有人明天生病，很多同步用量会归零。真正的 agent-native 是 droid 自己发现客户信号，自己生成 first-pass solution。

> **[46:19]** "90% of tokens will be asynchronous tokens"

这也是“dark factory”的具体含义：

> **[47:06]** "dark factory where like the lights are off and things are just happening"

这句话容易被误读成全自动编程幻想。结合前文更准确的解释是：暗厂不是没有人，而是人不再是每个任务的启动器。人类转向定义输入信号、验证标准、资源分配和业务 outcome；agent 在后台持续把信号转成候选变更。同步 copilot 只是过渡形态，异步 token 才会让软件产能真正脱离人类在线时长。

但 Matan 的乐观不是“工程师消失”。他承认短期会有痛苦的资源错配修正，但长期认为世界上大量问题可以用软件解决，而当前只有小部分被软件解决。工程师会从过度配置的问题迁移到未被软件化的问题。这个判断和 Aaron Levie/Casado 的复杂性扩张论一致：AI 降低软件成本后，软件会进入更多行业和流程，工程能力的配置边界反而扩大。

## 关键判断

- Factory 的差异化不是“也做 coding agent”，而是给企业一个独立于模型实验室的多模型 harness 和 token 控制层。
- 企业害怕的不是某个模型暂时落后，而是被单一模型/工具链变成软件生产的 single point of failure。
- AI 产品“早两年”等于错；愿景正确必须匹配模型可靠性、交互形态和用户行为准备度。
- 多模型 harness 的核心价值是避免过拟合单一模型脾气，把任务状态、compaction、tool use 和用户体验抽象得更稳定。
- 开放模型可能拿走多数 token share，但前沿模型仍保留最高 leverage share；企业需要按任务风险路由，而不是按模型名采购。
- 暗厂的本质是软件组织的会计系统：把 feature 流程、token 投入、人力投入和业务 outcome 连接成反馈闭环。
- 90% 异步 token 的预测意味着 agent 产品会从“人类发起任务”迁移到“系统持续发现信号并生成候选动作”。
- Matan 并不支持简单裁员叙事；他主张的是用可观测反馈决定哪里加 token、哪里加人、哪里回到核心能力。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 模型时机决定产品承诺能否兑现
**← [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]**
- 本文件论点：Matan 说 Factory 押注自主 agent 早了两年，而“being 2 3 2 or 3 years early is the same as being wrong” [5:24]；Droid CLI 的成功来自模型变强与开发者行为准备同步发生 [15:50]。
- 对方论点：Andrew 认为 Codex app 如果在 2025 年 11 月发布会失败，2026 年 2 月成立，唯一差异是模型能力；AI 产品规划必须把模型时机作为变量。
- 关联逻辑：Andrew 从 OpenAI 内部产品节奏说明“功能形态要等模型”，Matan 从创业公司生死线说明“愿景太早就是错误”。两者合并后，AI 产品路线图不能只按需求优先级排，而要维护一组等待模型跃迁后重测的 artifact。

### Strategy layer 与多模型 harness 的平台路线分歧
**← [[Katelyn Lesse & Angela Jiang- Anthropic 的策略层赌注（token 工作分配与开放生态）]]**
- 本文件论点：Matan 认为“what data is to a model, models are to a harness” [20:00]，多模型暴露能避免 harness 过拟合，并让企业保留模型独立性。
- 对方论点：Anthropic 平台团队认为真正 alpha 在 coordination/strategy layer：给不同 token 分配 advising、executing、reflecting、memory 等不同工作。
- 关联逻辑：两篇都把价值从单次模型调用上移到 harness/strategy，但路线不同。Anthropic 通过模型家族和接口规范优化策略层，Factory 通过跨模型路由让策略层不依附任何实验室。放在一起看，未来平台竞争不是“谁模型更强”，而是“谁拥有 token 工作分配权”。

### 企业软件价值从 UI 迁移到可审计生产链
**← [[Steven Sinofsky- Headless Software 不是去 UI，而是重估企业软件的价值层]]**
- 本文件论点：Matan 认为每家公司都有低效软件工厂，关键是把输入信号、feature 流程、token/人力投入和 business outcome 连接起来 [36:16, 38:24]。
- 对方论点：Sinofsky 认为 headless 后价值不在表层 UI，而在 system of record、权限、例外处理、业务逻辑和跨职能桥层。
- 关联逻辑：Sinofsky 给出企业软件价值层的静态拆解，Matan 给出软件生产过程的动态闭环。两者合并后，AI 创业机会不是做一个漂亮 agent UI，而是把过去藏在 SOP、审批、导出和会议里的生产链变成可追踪系统。

### 快速推理只是同步阶段，异步 token 才是产能跃迁
**← [[Andrew Feldman- 快速推理不是体验优化，而是 AI 产品形态迁移的底层变量]]**
- 本文件论点：Matan 预测 12-24 个月内“90% of tokens will be asynchronous tokens” [46:19]，暗厂意味着人在不启动每个任务时软件仍持续生产 [47:06]。
- 对方论点：Feldman 认为 fast tokens 会改变产品类别，tokens per second per user 决定实时协作体验，agent 行动还会把瓶颈外溢到 CPU 和系统调用。
- 关联逻辑：Feldman 解释同步协作为什么需要快，Matan 进一步指出同步只是过渡：当 agent 从人类 prompt 驱动转为信号驱动，核心指标会从响应速度扩展到后台任务吞吐、验证闭环和资源分配效率。二者共同定义了 agent 基础设施的两段式迁移。
