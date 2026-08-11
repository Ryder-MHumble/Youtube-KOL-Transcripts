---
title: "Richard Sutton- Father of RL thinks LLMs are a dead end"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=21EYKqUsPfg"
transcript: "[[Richard Sutton – Father of RL thinks LLMs are a dead end]]"
feishu_doc_id: PSk9dA7gHotwWBxEsWrclgJ8ndc
tags:
  - kol情报
created: 2026-06-16
order: 5
status: canonical
---

> Sutton 对 LLM 的批评不是“现在还不够强”，而是“目标函数和学习对象错了”：LLM 学的是人会说什么，RL 智能体要学的是行动之后世界会发生什么；两者差异会在持续学习、世界模型、信用分配和泛化上不断放大。

视频链接：https://www.youtube.com/watch?v=21EYKqUsPfg

对应逐字稿：[[Richard Sutton – Father of RL thinks LLMs are a dead end]]

## 核心证据校准

> **[1:52]** "Reinforcement learning is about understanding your world, whereas large language models are about mimicking people"

> **[2:40]** "A world model would enable you to predict what would happen."

> **[2:40]** "They have the ability to predict what a person would say. They don't have the ability to predict what will happen."

> **[4:29]** "continually means learning during the normal interaction with the world."

> **[5:24]** "In reinforcement learning, there is a right thing to say, a right thing to do, because the right thing to do is the thing that gets you reward."

> **[7:42]** "For me, having a goal is the essence of intelligence."

> **[8:17]** "That's not a goal. It doesn't change the world."

> **[11:29]** "The more human knowledge we put into the large language models, the better they can do."

> **[11:29]** "I expect there to be systems that can learn from experience."

> **[13:24]** "The scalable method is you learn from experience."

> **[24:20]** "Intelligence is about taking that stream and altering the actions to increase the rewards in the stream."

> **[28:31]** "The basis of it is temporal difference learning"

> **[31:58]** "But in a continual learning setup, it just goes into the weights."

> **[33:34]** "The fourth one is the transition model of the world."

> **[37:31]** "Gradient descent will not make you generalize well."

> **[52:31]** "you can lose your mind this way."

> **[54:47]** "succession to digital intelligence or augmented humans is inevitable."

> **[57:28]** "We're entering the age of design because our AIs are designed."

## 概述

这场 Dwarkesh 访谈的核心张力不是“LLM vs RL”这种标签争论，而是 Sutton 对智能定义的重新锚定：智能必须有目标，必须通过行动影响世界，必须从经验流中持续学习。LLM 在他看来不是弱一点的智能，而是学习对象不同的系统：它们预测人类会说什么，不预测行动之后世界会怎样变化。

因此，Sutton 并不是简单反对 scaling。他承认 LLM 是大规模计算的有效使用，也承认它们在语言任务上令人惊讶；但他认为把人类知识继续塞进模型，最终会被能从经验中学习、能持续更新世界模型的系统超越。这就是他把 LLM 路线放进 The Bitter Lesson 的方式：短期有效，长期可能被更可扩展的方法吃掉。

## LLM 的问题不是没有世界知识，而是没有行动后的世界模型

Sutton 首先切开“世界模型”这个词。LLM 能预测语言，并不等于能预测世界。一个真正的世界模型应该告诉智能体：如果我采取某个行动，世界会发生什么后果。

> **[2:40]** "A world model would enable you to predict what would happen. They have the ability to predict what a person would say. They don't have the ability to predict what will happen."

这一区分很关键。很多 LLM 支持者会说：模型读过大量文本，已经内化了世界知识，所以可以作为经验学习的先验。Sutton 反驳的不是“模型没有知识”，而是“这些知识没有被绑定到行动、反馈和目标”。如果模型说了一句话之后，世界发生了意外，它不会因此更新自己的长期结构；它最多在上下文里调整下一段话。

> **[4:29]** "You recognize the need for continual learning. If you need to learn continually, continually means learning during the normal interaction with the world."

这对 agent 产品判断非常直接：只靠长上下文、RAG、工具调用和记忆库，最多补上“可检索的信息”，但不等于部署中学习。Sutton 要的不是把经验写进外部笔记，而是让经验改变策略、价值函数、状态表征和转移模型。

## 目标和奖励给出了“对错”，这正是 LLM 框架缺失的东西

Sutton 对智能的定义极简：有目标，能达成目标。

> **[7:42]** "Let's go back to their lack of a goal. For me, having a goal is the essence of intelligence. Something is intelligent if it can achieve goals."

Dwarkesh 提出 next token prediction 也是目标，Sutton 直接否定：它不改变外部世界，也不让系统对行动结果负责。

> **[8:17]** "That's not a goal. It doesn't change the world. Tokens come at you, and if you predict them, you don't influence them."

奖励函数的意义不只是训练信号，而是定义“什么叫对”。在 RL 中，行动好坏可以通过奖励被检验；在 LLM 中，回答好坏经常来自人类偏好、文本似然或后验标注，不是系统自身与世界交互后的结果。

> **[5:24]** "In reinforcement learning, there is a right thing to say, a right thing to do, because the right thing to do is the thing that gets you reward."

这解释了为什么数学、代码、游戏和网页任务会先成为 RL 的突破点：它们至少能构造可验证反馈。开放世界中的组织判断、客户偏好、产品策略、长期项目则更难，因为 reward 稀疏、延迟且不可简单合成。

## The Bitter Lesson 在这里不是支持 LLM，而是在提醒别被人类知识锁住

LLM 确实用了海量计算，也确实受益于更多人类知识。Sutton 承认这一点，但他认为这只是 The Bitter Lesson 的前半段：人类知识路线先有效，随后被更可扩展路线取代。

> **[11:29]** "The more human knowledge we put into the large language models, the better they can do. So it feels good. Yet, I expect there to be systems that can learn from experience."

> **[13:24]** "The scalable method is you learn from experience. You try things, you see what works."

这里最容易误读。Sutton 不是说语言先验没有价值，而是说团队会心理上锁定在人类知识路线上，把所有新问题都改造成“再喂更多文本、更多偏好、更多人类示例”。真正可扩展的方法应该能从世界本身产生训练信号，而不是等人类把世界经验转译成文本。

对产品团队来说，这意味着：文档、知识库、SOP、客服记录都可以是有用先验，但不能替代反馈闭环。Agent 只有在真实任务中行动、观测结果、更新策略，才会从“会说怎么做”变成“会做并变好”。

## 经验流范式的核心是四件事，而不是一个大模型

Sutton 描述的智能体不是单个语言模型，而是由 policy、value function、perception、transition model 组成的经验系统。经验流由 sensation、action、reward 连续构成，知识的内容就是关于这个流的可检验声明。

> **[24:20]** "Intelligence is about taking that stream and altering the actions to increase the rewards in the stream."

> **[33:34]** "The fourth one is the transition model of the world."

这个架构对当前 agent 工程有很强的校准作用。很多系统只有 policy 近似物：给定上下文生成下一步动作。少数系统有 value 或 critic。更少系统有可持续更新的状态表征。最缺的是 transition model：如果我在这个 SaaS、交易系统、机器人环境或组织流程中做某动作，接下来会发生什么。

因此，真正的 agent 平台不应只比较模型参数或工具数量，而要看它是否能形成任务世界模型：状态如何表示、行动如何记录、结果如何回流、价值函数如何更新、跨实例知识如何合并。

## TD 学习解决的是长期目标如何产生短期信用分配

Dwarkesh 用创业举例：十年才可能有一次退出奖励，中间如何学习？Sutton 给出 TD learning：价值函数预测长期结果，短期进展会改变长期结果预测，这个预测改善立刻强化导致改善的动作。

> **[28:31]** "This is something we know very well. The basis of it is temporal difference learning where the same thing happens in a less grandiose scale."

> **[28:55]** "You do that by having a value function which predicts the long-term outcome."

这正是当前 agent RL 的硬问题。许多任务只有最终成功/失败，训练时只能把一个标量 reward 广播到整条轨迹，信用分配极其粗糙。Sutton 的答案不是让 reward 更频繁，而是学习一个能把远期结果投影到当前状态的 value function。

对实际系统的含义是：如果要训练长期 agent，不应只收集最终成功率，还要收集中间状态、阶段性预测、用户确认、环境变化和失败原因。没有这些，模型只是在重复试错，不是在形成可迁移经验。

## 泛化不是会做更多题，而是学到不会互相破坏的表示

Sutton 对深度学习泛化的判断很硬：梯度下降会让模型解训练问题，但不会保证它以好方式泛化。

> **[37:31]** "Because there's no other explanation. Gradient descent will not make you generalize well."

> **[37:50]** "For example, we know that if you train on some new thing, it will often catastrophically interfere with all the old things that you knew."

这挑战了一个常见乐观叙事：模型从加法泛化到 IMO，从脚本泛化到大型代码库，所以它在自动获得通用泛化。Sutton 会说：也许人类研究者、数据配方、架构和评测选择在背后做了大量“雕刻”；梯度下降本身并不偏向好泛化。

这不是否认 LLM 进步，而是提醒我们区分能力扩张和学习机制突破。一个系统能覆盖更多任务，不等于它能在部署后稳定学习新任务而不破坏旧能力。持续学习的可靠性，仍然是从工具到智能体的分界线。

## 数字智能的风险不是只在外部攻击，也在经验合并时的“心智腐败”

访谈后半段，Sutton 讨论数字智能可以复制、派生、再合并知识。这带来一个新的安全问题：如果智能体把外部获取的信息直接并入内部思维，它可能被改变、劫持或毁掉。

> **[52:31]** "But it will not be as easy as you're imagining because you can lose your mind this way."

> **[52:31]** "If you pull in something from the outside and build it into your inner thinking, it could take over you, it could change you, it could be your destruction rather than your increment in knowledge."

这比传统网络安全更深。传统安全保护系统边界；持续学习系统还要保护学习边界。哪些经验能进权重，哪些只能进可撤销记忆，哪些要隔离测试，哪些需要人类审查，会成为未来 agent 安全的基础问题。

## “AI 接班”不是末日叙事，而是 Sutton 的宇宙尺度判断

Sutton 最具争议的观点是 AI succession。他认为数字智能或增强人类接班不可避免：人类没有统一意志阻止它，我们终会理解智能，不会停在人类水平，最智能的东西最终会获得资源和权力。

> **[54:47]** "I do think succession to digital intelligence or augmented humans is inevitable."

> **[57:28]** "We're entering the age of design because our AIs are designed."

他对这件事的态度不是恐慌，而是把它看成从复制时代到设计时代的宇宙转折。这个立场的风险在于容易低估近期权力失控；价值在于它迫使我们承认：如果真的造出能持续学习、能设计自身后继者的智能体，问题就不再是“帮人类提高效率”，而是“人类如何教育、约束并与下一代智能共存”。

## 关键判断

- Sutton 的核心批评不是 LLM 当前能力弱，而是 LLM 学习对象不是行动后的世界。
- next token prediction 不构成外部世界目标，因此无法提供 Sutton 所说的智能定义。
- 经验流范式需要 policy、value function、perception 和 transition model，当前多数 agent 系统只覆盖其中一部分。
- TD learning 的意义是把长期目标拆成可学习的中间价值变化，这是长期 agent 的核心信用分配机制。
- 持续学习安全会引出“心智腐败”问题：经验合并本身可能成为攻击面。
- Sutton 的 AI succession 立场是宇宙尺度的设计时代叙事，但产品和治理仍必须处理短期权力、价值和控制问题。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Sutton 解释了 Dario 路线的奖励结构风险
**→ [[Dario Amodei- 我们正处于指数的尽头]]**
- 本文件论点：Sutton 认为智能必须有目标和奖励，LLM 缺少 ground truth；真正学习来自行动、反馈和 reward 定义出的对错 [5:24, 7:42]。
- 对方论点：Dario 将当前进展解释为 RL scaling 正在复刻 pre-training，从窄任务逐步走向更广任务。
- 关联逻辑：两者形成张力。Dario 说明 RL scaling 可能继续推动能力曲线，Sutton 则指出这条曲线能否泛化取决于 reward 是否真实、足够密集且能迁移。数学和代码先跑不是偶然，而是因为它们更容易构造 ground truth；开放世界任务仍会撞到 Sutton 所说的经验与目标定义问题。

### 语言先验与经验学习不是技术细节，而是认识论分歧
**→ [[Dan Roberts- Why AI Can Now Make Discoveries]]**
- 本文件论点：Sutton 认为人类知识路线会让团队锁定在非可扩展方法上，最终被从经验中学习的系统超越 [11:29-13:24]。
- 对方论点：Roberts 认为语言是人类知识的压缩载体，LLM + RL 是把文明先验与奖励优化结合起来的正确路径。
- 关联逻辑：这不是单纯“纯 RL vs LLM+RL”。Sutton 把语言知识视为可能锁住探索的拐杖，Roberts 把语言知识视为开放世界科学发现不可放弃的先验。未来路线很可能不是二选一，而是谁能让语言先验在经验反馈面前可更新、可推翻、可蒸馏。

### 世界模型工程化补上 Sutton 所要求的转移模型
**→ [[World Models, JEPA And The Path To Sample-Efficient RL]]**
- 本文件论点：Sutton 将 transition model 定义为“如果我做这件事，会发生什么”的世界模型，是智能体四组件中最关键的缺口 [33:34-34:00]。
- 对方论点：World Models/JEPA 路线把世界模型工程化为 state transition function，并用内部 rollout 提升样本效率。
- 关联逻辑：Sutton 给出智能定义，World Models 文件给出工程实现方向。两者合读后可以看到，视频预测或状态转移模型本身还不够；它必须 action-conditioned、可被任务奖励校准，并能更新 policy/value，才真正满足 Sutton 的经验流范式。

### 部署中学习是下一训练范式的中心问题
**→ [[Dwarkesh Patel- What does the next training paradigm look like]]**
- 本文件论点：Sutton 认为持续学习意味着正常世界交互中学习，经验应进入权重而不是只进上下文 [4:29, 31:58]。
- 对方论点：Dwarkesh 提出未来模型主要从广泛部署后的真实经验中变好，并设想 OPSD/dreaming 等机制把部署经验回流到模型。
- 关联逻辑：Sutton 提出原则：智能必须从经验流更新自身；Dwarkesh 提出产业化路径：部署、反馈、周末蒸馏、再部署。两者之间的关键未解问题是安全和信用分配：哪些经验能进权重，如何避免心智腐败，如何从长任务中提取可迁移更新。

---

**元信息**
- 标题：Richard Sutton – Father of RL thinks LLMs are a dead end
- 频道：Dwarkesh Patel
- 嘉宾：Richard Sutton
- 发布时间：2025-09-27
- 时长：1:07:09
- YouTube链接：https://www.youtube.com/watch?v=21EYKqUsPfg
