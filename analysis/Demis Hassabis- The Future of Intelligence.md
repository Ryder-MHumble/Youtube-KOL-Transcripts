---
title: "Demis Hassabis- The Future of Intelligence"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=PqVbypvxDto"
transcript: "[[Demis Hassabis- The Future of Intelligence 逐字稿]]"
tags:
  - kol情报
created: 2026-06-08
order: 37
status: canonical
---

> Hassabis 的 AGI 路线不是纯 scaling，也不是纯研究浪漫主义，而是一个 50/50 的双引擎判断：算力仍有显著回报，但越接近 AGI，越需要算法创新、一致性、世界模型和可控的自我检查机制。

视频链接：https://www.youtube.com/watch?v=PqVbypvxDto

对应逐字稿：[[Demis Hassabis- The Future of Intelligence 逐字稿]]

## 概述

这场访谈的主线不是 Google DeepMind 的年度盘点，而是 Hassabis 对 AGI 路线的重新分层：root node 问题证明 AI 可以解锁科学下游，jagged intelligence 暴露当前系统离通用智能仍有一致性缺口，world models 补语言模型够不到的物理和经验维度，而后 AGI 的制度问题必须提前设计。

他最重要的判断是：scaling 没有撞墙，但也不再是单独答案。DeepMind 的竞争优势在于把世界级工程、TPU 基础设施和研究传统绑在一起。Hassabis 不是在说“继续堆算力就行”，而是在说“地形变难时，研究能力重新成为护城河”。

## Root Node：科学问题的上游杠杆

Hassabis 把 AlphaFold 看作 root node 方法的 proof point：解决一个上游科学问题，就会释放一批下游能力。蛋白质折叠之后，他点名材料、室温超导、更好电池、聚变和量子纠错。

> **[2:39]** "Well, of course, the big proof point was AlphaFold."

> **[2:54]** "And we're exploring all the other ones now."

> **[3:13]** "We've just announced a partnership with a deep one."

> **[3:46]** "And we're helping them with error correction codes, where we're using our machine learning to help them."

聚变在这里不是单点技术兴奋，而是 root node 思维的典型案例。能源如果近乎免费，海水淡化、火箭燃料、气候问题都会被重新定价。

> **[4:33]** "I mean, it opens up many-- this is why we think of it as a root node."

> **[4:44]** "But also, if energy really was renewable and clean and super cheap, almost free, then many other things would become viable, like water access because we could have desalination plants pretty much everywhere, even making rocket fuel."

对科研转化的启发是：AI 项目不要只按单个应用 ROI 排序，而应识别“上游瓶颈”。真正高杠杆的问题，是解开后会让多个下游问题同时变便宜的问题。

## Jagged Intelligence：AGI 缺的不是峰值，而是一致性

Hassabis 对当前模型的诊断很明确：它们在某些任务上达到 PhD 水平，却会在高中级问题、逻辑题、甚至棋类游戏中出错。这种 jagged intelligence 是“还没到 AGI”的关键证据。

> **[5:29]** "I think it's fascinating, actually, one of the most fascinating things, and probably that needs to be fixed as one of the key things why we're not at AGI yet."

> **[6:17]** "And so sometimes people call it jagged intelligences."

> **[6:21]** "So they're really good at certain things, maybe even PhD level."

> **[6:25]** "But then, other things, they're not even high school level."

真正的通用智能不是某几个维度的峰值，而是跨任务的一致可靠。Hassabis 把一部分问题归因于 tokenization 等局部机制，但更深的问题是 reasoning/thinking 是否会被稳定地用于自检。

> **[7:00]** "And each one of those can be fixed, and then you can see what's left, but I think consistency."

> **[7:08]** "So we have thinking systems now that, at inference time, they spend more time thinking, and they're better at outputting their answers."

> **[7:16]** "But it's not super consistent yet in terms of, is it using that thinking time in a useful way to actually double-check and use tools to double-check what it's outputting?"

这对产品评估的含义是：不要只看最难任务的成功样例，要看跨难度、跨模态、跨边界条件的一致性。一个模型能解 IMO，不代表它能可靠承担企业流程或科学工作。

## 当前 LLM 仍在 AlphaGo 阶段

Hassabis 用 AlphaGo/AlphaZero 对 LLM 阶段做了精准定位。当前 foundation models 更像 AlphaGo：它们从人类知识出发，把互联网压缩成可查询、可泛化的 artifact，但还缺少可靠的 search/thinking 层来使用这些知识。

> **[7:45]** "I think what we're trying to build today, it's more like AlphaGo."

> **[7:49]** "So effectively, these large language models, these foundation models, they're starting with all of human knowledge, what we put on the internet, which is pretty much everything these days, and compressing that into some useful artifact which they can look up and generalize from."

> **[8:06]** "But I do think we're still in the early days of having this search or thinking on top, like AlphaGo had, to use that model to direct useful reasoning traces, useful planning ideas, and then come up with the best solution to whatever the problem is at that point in time."

下一步才是 AlphaZero 式的自主发现知识，但 Hassabis 认为必须先把 AlphaGo-like system 做稳。

> **[8:42]** "I think once you have AlphaGo there, you could go back, just like we did with the Alpha series, and do an AlphaZero, where it starts discovering knowledge for itself."

> **[8:57]** "And so I think it's good to try and create the first step first with some kind of AlphaGo-like system."

他还点出一个关键缺失：部署后的在线持续学习。当前模型训练、后训练、上线后基本冻结，这和人类每天学习的方式不同。

> **[9:06]** "But that is also one of the things missing from today's systems is the ability to online learn and continually learn."

> **[9:18]** "But they don't continue to learn out in the world, like we would."

这与 Ilya 的“超级智能不是成品，而是会学习的系统”高度同构。未来 AGI 产品不应只围绕静态模型快照设计，而要围绕持续学习过程设计权限、审计和回滚。

## Scaling 没撞墙，但地形变难了

Hassabis 明确反对“scaling 撞墙”的二元叙事。他承认递减回报存在，但递减回报不是零回报；指数和渐近线之间还有很大空间。

> **[13:03]** "I think a lot of people thought that, especially as other companies have had slower progress, shall we say."

> **[13:09]** "But I think we've never really seen any wall, as such."

> **[13:17]** "And when I say that, people only think, oh, so there's no returns."

> **[13:26]** "Actually, there's a lot of room between those two regimes."

数据不够也不是简单终局，因为代码和数学这类可验证领域可以生成合成数据。但他马上把这归为 research question，而不是工程采购问题。

> **[13:57]** "But there are ways to get around that-- synthetic data, generating-- these systems are good enough, they can start generating their own data."

> **[14:04]** "Especially in certain domains like coding and math, where you can verify the answer, in some sense, you could produce unlimited data."

> **[14:11]** "So all of these things, though, are research questions."

这就导向他的 50/50 判断：DeepMind 既做 scaling，也做 innovation。AGI 需要两条引擎同时运转。

> **[14:49]** "So I think that's just what's transpiring."

> **[15:22]** "And, effectively, you can think of as 50% of our effort is on scaling, 50% of it is on innovation."

> **[15:28]** "And my betting is you're going to need both to get to AGI."

这个判断对行业路线的修正很重要：Ilya 强调回到 research 时代，Hassabis 补充说这不是放弃 scaling，而是在大规模条件下重新让研究成为差异化来源。

## 幻觉问题的本质是“不知道何时拒答”

Hassabis 没有把 hallucination 只解释为事实错误，而是解释为系统在该拒答时仍被迫回答。它缺少类似 AlphaFold 的整体置信度判断。

> **[15:53]** "And I think we need that, actually."

> **[16:27]** "But it still sometimes-- it forces itself to answer when it probably shouldn't, and then that can lead to a hallucination."

他进一步指出，下一个 token 概率不能回答“整个事实或陈述是否可靠”。thinking step 应该用于回看、检查和调整，而不只是生成更长的链路。

> **[16:54]** "Yes, there is of the next token."

> **[16:57]** "But that doesn't tell you the overall arching piece, is how confident are you about this entire fact or this entire statement?"

> **[17:06]** "And I think that's why you'll need this-- I think we'll need to use the thinking steps and the planning steps to go back over what you just output."

这对 AI 应用设计非常直接：可靠系统需要置信度、拒答、工具复核和事后检查，而不是单纯延长推理。思考时间只有在被用于自检时才有价值。

## World Models 补语言够不到的物理经验

Hassabis 承认语言模型比预期更能理解世界，因为语言里包含了很多世界知识。但空间动态、物理上下文、感官体验很难写进文本语料。

> **[17:53]** "What can a world model do that a language model can't?"

> **[18:09]** "And I think language models are able to understand a lot about the world-- I think, actually, more than we expected, more than I expected, because language is actually probably richer than we thought."

> **[18:26]** "But there's still a lot about the spatial dynamics of the world-- spatial awareness and the physical context we're in and how that works mechanically-- that is hard to describe in words and isn't generally described in corpuses of words."

他对 world model 的定义是理解世界的因果机制和直觉物理。它是 robotics、universal assistant、科学模拟的共同底座。

> **[19:06]** "And I think if we want robotics to work or a universal assistant that maybe comes along with you in your daily life, maybe on glasses or on your phone and helps you in your everyday life, not just on your computer, you're going to need this kind of world understanding, and world models are at the core of that."

> **[19:26]** "So what we mean by world model is this sort of model that understands the causative and effect of the mechanics of the world-- intuitive physics, but how things move, how things behave."

Genie + SIMA 的组合给出一个潜在训练循环：一个 AI 生成世界，另一个 AI 在其中行动，环境按行动实时变化。Hassabis 把这看成可能的无限任务生成器。

> **[22:14]** "But then we thought, well, wouldn't it be fun if we plugged Genie into SIMA and dropped a SIMA agent into another AI that was creating the world on the fly?"

> **[22:47]** "And I think this could be the beginning an interesting training loop, where you almost have infinite training examples because, whatever the SIMA agent is trying to learn, Genie can basically create on the fly."

但他也强调，真实感不等于物理正确。视频模型看起来像世界，不代表它具备机器人训练所需的可依赖物理。

> **[23:40]** "It's basically hallucinations again."

> **[24:03]** "But, yes, when you're trying to train a SIMA agent, you don't want Genie hallucinating physics that are wrong."

> **[24:46]** "And right now, they're not."

> **[24:48]** "And they look realistic when you just casually look at them, but they're not accurate enough yet to rely on for, say, robotics."

这对具身智能判断很关键：视频生成的视觉真实感只是第一层，能否作为训练环境，取决于物理规律是否可验证、可控、可重复。

## 后 AGI 问题不是技术自动解，而是制度提前量

Hassabis 对 AGI 后社会的判断不是“技术自然带来丰裕”，而是“丰裕仍需制度设计”。工业革命用了约一个世纪让社会适应，AGI 可能 10 倍更大、10 倍更快。

> **[38:26]** "And we're probably going to have to because the difference this time is that it's probably going to be 10 times bigger than the Industrial Revolution, and it will probably happen 10 times faster, so more like a decade, unfold over a decade, than a century."

他认为新的经济系统、分配机制、UBI 或其他制度都需要提前研究；丰裕不会自动等于公平分配，目的感也会成为问题。

> **[39:22]** "And I think at least that level of change is going to happen again."

> **[40:43]** "And then there's the philosophical side of it of, OK, so jobs will change and other things like that, but maybe fusion will have been solved."

> **[41:01]** "But then what happens to purpose?"

这里的政策含义是：如果时间线是 5-10 年，制度建设已经偏慢。技术公司说“模型会变强”并不足够，政府、经济学家、社会科学家要提前设计分配、身份、目的和国际合作机制。

## 信息主义是 Hassabis 的底层信念

访谈结尾，Hassabis 把自己的 AGI 信念连接到 Turing machine 问题。他的立场接近信息主义：除非物理证明有不可计算的东西，否则他会假设世界可以被计算系统建模。

> **[45:26]** "And this comes back to the Turing machine question of, what is the limit of a Turing machine?"

> **[46:40]** "Maybe in the universe, everything is computationally tractable if you look at it in the right way, and therefore, Turing machines might be able to model everything in the universe."

> **[47:02]** "Nobody's found anything in the universe that's non-computable, so far."

他进一步把生物学、感觉和疾病都理解为信息处理问题，甚至认为信息可能比物质和能量更基本。

> **[48:09]** "But in the end, it's all information, and we're information-processing systems."

> **[48:17]** "That's how I think we'll end up curing all diseases is by thinking about biology as an information-processing system."

> **[48:24]** "And I think, in the end, that's going to be-- and I'm working on, in my spare time, my two minutes of spare time, physics theories about things like information being the most fundamental unit, shall we say, of the universe-- not energy, not matter, but information."

这解释了他为什么同时重视 AlphaFold、world models、simulation 和 AGI：在他的世界观里，它们不是不同项目，而是同一个命题的不同实例：如果某个系统可以被足够好地表示为信息过程，就有可能被 AI 学会、模拟和优化。

## 关键判断

- Root node 问题是 AI 科研转化的最高杠杆：解决上游瓶颈，会重估一组下游问题。
- 当前模型的关键短板不是峰值能力，而是一致性；AGI 需要跨任务可靠，而不是局部 PhD 水平。
- LLM 仍在 AlphaGo 阶段：压缩人类知识后，需要可靠 search/thinking 层；AlphaZero 式自主发现仍在后面。
- Scaling 没撞墙，但递减回报让 research 重新成为核心护城河；Hassabis 的路线是 50% scaling + 50% innovation。
- 幻觉治理需要整体置信度、拒答机制和 thinking step 自检，而不是只看 next-token probability。
- World models 是语言模型够不到的物理经验层，但视频真实感必须经过物理 benchmark 才能用于机器人训练。
- AGI 后社会需要提前设计制度；工业革命的世纪级适应过程可能被压缩到十年。
- Hassabis 的底层哲学是信息主义：智能、生命和科学问题都可被看作信息处理问题。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Research 时代不是反 scaling，而是大计算下的配方竞争
**→ [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]**
- 本文件论点：Hassabis 认为 scaling 没有墙，但 AGI 需要 50% scaling + 50% innovation [15:22]。
- 对方论点：Ilya 认为 2020-2025 是 scaling 时代，现在回到 research 时代，关键问题是算力是否被用于最高生产率的学习机制。
- 关联逻辑：Ilya 给出阶段判断，Hassabis 给出资源配比。两者合并后，“回到 research”不是缩小规模，而是在大计算条件下寻找新配方；下一轮竞争会从买更多 GPU 变成谁能让 GPU 更有效地产生泛化。

### 可验证域生成数据，仍然绕不开验证瓶颈
**→ [[Grant Sanderson- AI and the future of math]]**
- 本文件论点：Hassabis 认为 coding/math 因为答案可验证，可以生成近乎无限合成数据 [14:04]。
- 对方论点：Grant 把数学和代码进步解释为“可磨性”：环境可复制、失败可检查、单次试错成本低，但概念创造和消化性仍无法短周期验证。
- 关联逻辑：Hassabis 解释可验证域为什么还能延长 scaling，Grant 指出可验证并不等于真正理解。放在一起看，合成数据能扩大可评分能力，但不能自动解决研究品味、概念生成和人类消化的问题。

### World model 是信用分配的环境侧解法
**→ [[World Models, JEPA And The Path To Sample-Efficient RL]]**
- 本文件论点：Hassabis 设想 Genie + SIMA 构成无限任务训练循环，但要求世界模型不能幻觉错误物理 [22:47]。
- 对方论点：World Models/JEPA 路线把世界模型视为信用分配稀疏性的架构解法，让 agent 在合成环境中预演每步后果。
- 关联逻辑：Hassabis 给出产品和科研路线，World Models 笔记给出算法机制。二者共同说明，世界模型的价值不是生成逼真视频，而是提供可学习、可验证、可反复试错的环境；物理正确性决定它能否成为训练引擎。

### 指数增长需要双引擎，不是单一曲线宿命
**→ [[Ray Kurzweil- 指数增长不是预言是不可逆的物理现实]]**
- 本文件论点：Hassabis 明确要求 scaling 与 innovation 同时存在，单靠任一项都不足以到 AGI [15:28]。
- 对方论点：Kurzweil 把计算指数增长视为长期规律，强调技术曲线在临界点突然显现。
- 关联逻辑：Hassabis 对 Kurzweil 的指数叙事给出工程修正：曲线看起来连续，是因为算力和算法创新交替补位。若算法停滞，指数曲线不会自动兑现为智能跃迁；若算力不足，创新也无法充分验证。

---

**元信息**

| 字段 | 值 |
|---|---|
| 标题 | The future of intelligence | Demis Hassabis |
| 频道 | Google DeepMind |
| 发布时间 | 2025-12-17 |
| 时长 | 56min |
| 对话者 | Demis Hassabis，Hannah Fry |
| 分析时间 | 2026-07-22 |
