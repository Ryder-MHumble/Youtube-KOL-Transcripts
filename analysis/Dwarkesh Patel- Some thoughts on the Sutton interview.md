---
title: "Dwarkesh Patel- Some thoughts on the Sutton interview"
source: feishu
feishu_doc_id: AVVudnLElou2tvx9lmMcnNJvnsE
tags:
  - kol情报
created: 2026-06-08
order: 25
---

[deprecated] docs +fetch is using the v1 API. Check the installed lark-doc skill first; if it is not the v2 skill, run `lark-cli update` to upgrade skills.
# Dwarkesh Patel: Some thoughts on the Sutton interview

> 即使 LLM 先到 AGI，它们构建的继任系统几乎必然基于 Sutton 的愿景——持续学习、样本效率、摆脱人类数据依赖。LLM 不是死胡同，但 Sutton 指出的结构性缺陷是真实的。
>
> —— Dwarkesh Patel, 2025

视频链接：https://www.youtube.com/watch?v=u3HBJVjpXuw

概述：这是 Dwarkesh Patel 在访谈 Richard Sutton 之后发布的反思视频（11分钟）。Sutton 认为当前 LLM 范式是死胡同——部署时不学习、训练阶段极度低效、完全依赖人类数据。Dwarkesh 不同意这个二分法：他认为模仿学习与 RL 是连续的而非对立的，LLM 的「人类模型」可以作为先验来促进真正的世界模型，而持续学习可能通过 test-time fine-tuning 等技术被近似实现。但他承认 Sutton 识别了 LLM 的三个真实结构性缺陷。

主题脉络：(1) The Bitter Lesson 的真正含义 (2) 模仿学习与 RL 的连续性 (3) 持续学习的可能路径 (4) 即使 LLM 先到 AGI，Sutton 的愿景仍定义了下一代系统

# 一、The Bitter Lesson 的真正含义：不是「扔算力」，是「有效利用算力」

## 1.1 LLM 部署时不学习——算力的巨大浪费

Sutton 的 The Bitter Lesson 被广泛误读为「只需要更多算力」。Dwarkesh 澄清：原文的核心论点是找到最有效、最可扩展地利用算力的技术。LLM 在推理阶段消耗了绝大部分算力，但在整个部署期间完全不学习——只在训练阶段学习。这本身就是对算力的低效利用。更糟的是，训练阶段本身极度低效：LLM 通常需要等价于数万年人类经验的数据量才能学会一件事。
```plaintext {wrap}
[00:38] Most of the compute that's spent on an LLM is used in running it during deployment. And yet it's not learning anything during this entire period. It's only learning during this special phase we call training. That is obviously not an effective use of compute.
```

## 1.2 人类数据是有限资源，RLVR 也只是人类设计的游乐场

Sutton 的另一个核心批评：LLM 的学习来源几乎全是人类数据。预训练数据显然如此，但连 RLVR（当前业界最前沿的后训练技术）也只是让 LLM 在人类预设的技能框架中学习——环境是人类搭建的，目标是人类定义的。Agent 并没有在与世界的有机互动中自主发现什么。人类数据是不可扩展的有限资源，把 AGI 的基础建立在一种不可扩展的资源上，从长远看不是一条可行的路。
```plaintext {wrap}
[01:16] these RL environments are human furnished playgrounds to teach LLMs the specific skills we have prescribed for them. The agent is in no substantial way learning from organic and self-directed engagement with the world.
```

更深一层：LLM 学到的不是真正的世界模型，而是「人类会说什么」的模型。它构建的是人类概念的表示，而不是行动如何改变环境的因果模型。Dwarkesh 用一个思想实验说明这一点——如果你只用 1900 年以前的数据训练 LLM，它几乎不可能独立推导出相对论。
```plaintext {wrap}
[01:49] they are building a model of what a human would say next. And this leads them to rely on human-derived concepts. [...] suppose you trained an LLM on all the data up to the year 1900. That LLM probably wouldn't be able to come up with relativity from scratch.
```

# 二、模仿学习与强化学习不是对立的两极

## 2.1 化石燃料类比：预训练数据是过渡性能源，不是死胡同

Dwarkesh 引用 Ilya Sutskever 的类比：预训练数据就像化石燃料——不可再生，但使用它并不意味着走入了死胡同。人类文明从水车到太阳能，中间必须经过化石燃料这个廉价且充足的过渡阶段。没有化石燃料，不可能直接跳到核聚变。同样，AlphaGo（基于人类棋谱训练）已经超越了所有人类棋手，尽管 AlphaZero（从零开始自我对弈）最终更强。关键判断：人类数据对 AGI 不是「有害的」，只是在足够大的规模上「不再显著有用」。
```plaintext {wrap}
[03:43] Just because fossil fuels are not a renewable resource does not mean that our civilization ended up on a dead-end track by using them. In fact they were absolutely crucial. You simply couldn't have transitioned from the water wheels of 1800 to solar panels and fusion power plants.
```

## 2.2 模仿学习就是短视界的 RL——它们是连续的

Dwarkesh 的核心反驳：模仿学习和 RL 不是两种根本不同的学习范式，而是同一连续体上的不同端点。模仿学习就是 episode 长度为一个 token 的 RL——模型基于对世界的理解对下一个 token 做出猜想，根据预测的准确程度获得奖励。人类的文明积累本身就是一种模仿学习——我们没有发明自己使用的语言、法律体系或技术，而是从前人那里继承。这个继承过程更像模仿学习而非从零开始的 RL。
```plaintext {wrap}
[06:07] Imitation learning is just short horizon RL. The episode is a token long. The LLM is making a conjecture about the next token based on its understanding of the world and how the different pieces of information in the sequence relate to each other.
```

更关键的判断：LLM 的「人类模型」是否可以成为学习「真实世界模型」的先验？Dwarkesh 认为答案显然是肯定的。经过 RL 训练的预训练模型已经赢得了 IMO 金牌、能从零构建完整应用——这些都是基于真实反馈的检验。你不可能从零开始 RL 出这样的能力，你需要一个基于人类数据的合理先验来启动 RL 过程。关于「人类模型」和「世界模型」的语义争论并不重要——重要的是这个先验是否能帮助你开始从真实反馈中学习。Dwarkesh 打了个精准的比方：这就像对着一个正在巴氏杀菌牛奶的人说「别煮了，我们最终要冷着端上桌！」当然——但这是通往最终产出的中间步骤。
```plaintext {wrap}
[07:40] It's a bit like saying to someone pasteurizing milk, "Hey stop boiling that milk because we eventually want to serve it cold!" Of course. But this is an intermediate step to facilitate the final output.
```

# 三、持续学习：LLM 真正的结构性缺陷

## 3.1 信息效率的鸿沟：每 episode 1 bit vs. 动物的海量感知

Dwarkesh 承认这是 LLM 最真实的结构性缺陷。当前 LLM 在基于结果奖励的 RL 中，每个 episode 只能学到大约 1 bit 的信息——而一个 episode 可能耗费数万个 token。动物和人类显然能从环境互动中提取远比「episode 结束时的奖励信号」多得多的信息。在 Sutton 的 OaK 架构中，外层 RL 激励了一个内层学习系统（transition model）从环境中提取最大信号。当前的 LLM+RLVR 范式缺少这个内层学习系统。
```plaintext {wrap}
[08:35] An LLM being RLed on outcome-based rewards learns on the order of 1 bit per episode, and an episode may be tens of thousands of tokens long. Obviously, animals and humans are clearly extracting more information from interacting with our environment than just the reward signal at the end of each episode.
```

## 3.2 桥接路径：SFT 作为工具调用 + 上下文学习的扩展

尽管持续学习的能力目前不存在，Dwarkesh 认为存在一些相对直接的方式将其嫁接到 LLM 上。例如，可以将 SFT 变成模型的工具调用——外层 RL 激励模型通过监督学习有效地「自学」，来解决超出上下文窗口的问题。他对此持开放态度（「我对此真的不可知——我不是 AI 研究者」），但不会惊讶于这些技术最终能近似实现持续学习。模型在上下文窗口内已经展现出了类似持续学习的能力——in-context learning 从训练中自然涌现。如果信息能跨窗口流动，模型可能会 meta-learn 出同样的灵活性。
```plaintext {wrap}
[10:10] The fact that in-context learning emerged spontaneously from the training incentive to process long sequences makes me think that if information could flow across windows longer than the current context limit, models could meta-learn the same flexibility that they already show in-context.
```

# 四、即使 LLM 先到 AGI，Sutton 的愿景仍定义了下一代系统

Dwarkesh 在结尾做了一个精妙的总结：进化用 meta-RL 制造了 RL agent，那个 agent 可以选择性地做模仿学习。而 LLM 走了完全相反的路径——先做一个纯模仿学习的基座模型，再做足够的 RL 让它变成有目标和自我意识的 agent。也许这条路走不通。但那些关于 LLM 没有「真正世界模型」的第一性原理论证，并没有证明太多，也不完全符合今天的模型——它们正在接受大量基于真实反馈的 RL。
```plaintext {wrap}
[10:40] Evolution does meta-RL to make an RL agent. That agent can selectively do imitation learning. With LLMs, we're going the opposite way. We first made a base model that does pure imitation learning. And we're hoping that we do enough RL on it to make a coherent agent with goals and self-awareness.
```

即便 Sutton 的柏拉图理想不是通往第一个 AGI 的路径，他的第一性原理批评识别了当前模型的一些真实底层缺陷——我们之所以不觉得这些缺陷存在，只是因为它们在当前范式中如此普遍以至于习以为常。缺乏持续学习、糟糕的样本效率、对不可扩展的人类数据的依赖——这些是 Sutton 凭数十年的视角才能看到的盲点。Dwarkesh 最终判断：如果 LLM 先达到 AGI（他预期如此），它们构建的继任系统几乎必然基于 Sutton 的愿景。
```plaintext {wrap}
[11:08] Even if Sutton's Platonic ideal doesn't end up being the path to first AGI, his first principles critique is identifying some genuine basic gaps these models have. We don't even notice because they are so pervasive in the current paradigm, but because he has this decades-long perspective they're obvious to him.
```

---

元信息
```plaintext {wrap}
标题: Some thoughts on the Sutton interview
频道: Dwarkesh Patel
发布时间: 2025-10-04
时长: 11min
YouTube链接: https://www.youtube.com/watch?v=u3HBJVjpXuw
分析时间: 2026-06-07
```
