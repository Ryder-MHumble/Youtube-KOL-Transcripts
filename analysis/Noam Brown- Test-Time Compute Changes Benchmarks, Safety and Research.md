---
title: "Noam Brown- Test-Time Compute Changes Benchmarks, Safety and Research"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=AZrU6y3pUcU"
transcript: "[[Really Big Test-Time Compute in AI Changes Benchmarks, Safety and Research with OpenAI's Noam Brown]]"
tags:
  - kol情报
status: canonical
---

> Noam Brown 的核心判断是：模型能力不再是一个静态属性，而是模型、预算、时间和 scaffold 的函数；因此 benchmark grid、安全评估、发布节奏和科研竞争都在用旧语言描述一个已经变形的问题。

视频链接：https://www.youtube.com/watch?v=AZrU6y3pUcU

对应逐字稿：[[Really Big Test-Time Compute in AI Changes Benchmarks, Safety and Research with OpenAI's Noam Brown]]

## 核心证据校准

> **[0:00]** "The problem is we're in a world now where the capability of the model is a function of how much money you put into it."

> **[0:27]** "At what budget should you evaluate these models?"

> **[1:58]** "It's like a single number for a model on a single benchmark."

> **[2:23]** "They're not controlling for the amount of test time compute that is being used on that benchmark question."

> **[2:54]** "how long should they think for?"

> **[3:31]** "5.5 and other models can think for if you scaffold them reasonably well, can think for weeks"

> **[3:31]** "the point at which they plateau is simply too far out to reasonably test."

> **[4:00]** "you either have some kind of budget for the benchmark whether it's tokens or cost or time"

> **[4:40]** "if you run them for 100 million tokens, they're still improving at beyond that point."

> **[6:08]** "it's not very practical when working u because like okay you ask the model a question and then you sit there for a week waiting for it to come back to you."

> **[6:26]** "the thinking time I think needs to be flexible."

> **[8:34]** "I use them to make poker bots and see how good they can make a poker bot."

> **[9:47]** "it kind of felt like a grad student"

> **[12:45]** "the capability of the model is a function of how much money you put into it."

> **[14:54]** "you can actually scaffold, for example, 5.5 into doing a series of experiments that can run for weeks, for months."

> **[15:54]** "the only way to be fully sure is to actually run it for a month."

> **[17:14]** "I think absolutely."

> **[17:14]** "the model was able to do something that they weren't able to do"

> **[18:53]** "nobody had explored sufficiently what happens if I put $100,000 worth of compute into 5.5 what could it do?"

> **[21:22]** "I don't think we're at the point where, okay, you just give it an arbitrary extremely high inference budget and it's just it's just super intelligent across the board."

> **[22:10]** "there's some benchmarks where they clearly improve with more test time compute and there's some where they don't."

> **[24:18]** "it's not able to do it."

> **[24:55]** "I wouldn't be surprised if we encounter that point for research taste as well."

> **[25:24]** "The models are definitely accelerating what researchers can do inside the labs."

> **[25:28]** "it's more about transforming what researchers do rather than fully replacing the researchers"

> **[25:55]** "I don't think we're headed to that world"

> **[27:57]** "billions of humans thinking for a long time and building off of each other's accumulated knowledge."

> **[29:58]** "the ability to use the models to improve the model research is a real thing"

## 概述

Noam Brown 这场 No Priors 访谈的关键，不是“test-time compute 很重要”这个已经被行业接受的结论，而是他指出 test-time compute 正在破坏 AI 行业默认的测量语言。过去我们说“模型 A 比模型 B 强”，默认能力是模型本身的属性；Brown 说，现在能力越来越像一个函数：模型、推理预算、运行时间、scaffold 和任务类型共同决定结果。

> **[0:00]** "The problem is we're in a world now where the capability of the model is a function of how much money you put into it."

这个变化会连锁影响四件事：benchmark grid 不再能用单个数字表达能力；安全评估必须说明预算假设；发布周期和评估周期开始错位；科研中的“研究品味”暂时仍是人类瓶颈，但模型已经在加速部分研究工作。

## Benchmark grid 的问题不是噪声，而是缺少预算轴

Brown 对 5.5 发布时外界短暂怀疑的解释很具体：大家看的 benchmark grid，把每个模型在每个 benchmark 上压成一个数字。

> **[1:58]** "It's like a single number for a model on a single benchmark."

这个呈现方式的问题是没有控制 test-time compute。5.5 看起来只比 5.4 提高几个百分点，但用户实际感受差距大，因为 5.5 的 thinking 更高效。

> **[2:23]** "They're not controlling for the amount of test time compute that is being used on that benchmark question."

一旦你问“那就让 5.5 想得和 5.4 一样久”，问题立刻变成：到底该想多久？

> **[2:54]** "how long should they think for?"

旧方法是让模型思考到性能平台期，但 Brown 说现代模型的平台期已经远到无法合理测试。

> **[3:31]** "5.5 and other models can think for if you scaffold them reasonably well, can think for weeks"

> **[3:31]** "the point at which they plateau is simply too far out to reasonably test."

所以正确表达不是“一个模型一个分数”，而是把性能画成 test-time compute 的函数，或者固定 token、cost、time 等预算。

> **[4:00]** "you either have some kind of budget for the benchmark whether it's tokens or cost or time"

这对所有模型评测都有直接影响：如果没有预算轴，benchmark 可能系统性低估“更高效思考”的模型，也可能高估“只是烧更多推理”的模型。

## 能力随预算增长，安全框架就不能只问“模型能不能”

Brown 最尖锐的安全判断，是 preparedness framework 和 responsible scaling policy 仍然在用 GPT-3 时代的假设。GPT-3 给 10 美元或 1000 万美元预算，能力差别不大；现在不是这样。

> **[12:45]** "the capability of the model is a function of how much money you put into it."

这让安全评估的问题从“模型是否具备某危险能力”变成“在什么预算、什么 scaffold、什么运行时间下具备危险能力”。Brown 在冷开场直接提出这个未解问题：

> **[0:27]** "At what budget should you evaluate these models?"

这不是形式主义。若低预算评估放行，高预算攻击者可能发现隐藏能力；若按极高预算评估，又可能让任何模型都显得过于危险。安全政策需要把预算作为一等变量，而不是把它隐含在评估流程里。

更麻烦的是评估周期和发布周期的错位。Brown 说，真正知道模型一个月运行能力的唯一方式，就是真的跑一个月。

> **[15:54]** "the only way to be fully sure is to actually run it for a month."

当模型两三个月一代，而某些 agent 任务可能需要数周或数月才能显现能力，实验室不可能在每次发布前完整探索能力边界。这意味着每一次模型发布都携带大量未开采、未评估的潜在能力。

## 长思考不是默认产品形态，交互节奏必须可变

Brown 并没有把“让模型想更久”当成万能答案。他承认长时间推理在 benchmark 上好看，但对真实用户不一定实用。

> **[6:08]** "it's not very practical when working u because like okay you ask the model a question and then you sit there for a week waiting for it to come back to you."

他给出的产品原则是 flexible thinking time：该快时快，该慢时慢。

> **[6:26]** "the thinking time I think needs to be flexible."

这对 AI 产品设计很关键。未来的产品不应该只有“普通模式/深度研究模式”这种粗粒度按钮，而要能根据任务价值、失败成本、预算上限和用户等待意愿动态路由。一个税务问题、一个代码修复、一个药物发现假设、一个数学猜想反例，不应该使用同一种推理预算策略。

这也对应 Sarah Guo 最后问的 specialized domains routing layer：应用公司如果能把大目标拆成多类任务，并管理每类任务该花多少 inference，就可能在模型层之上形成新的价值。

## 已发布模型里有未开采能力，Erdős 例子说明 scaffold 是关键

Brown 认为当前模型里有大量 latent capability。

> **[17:14]** "I think absolutely."

他举了 Erdős unit distance conjecture 的例子：OpenAI 内部模型找到了反证，之后社区发现 5.5 也能做到，但不是直接问就行，而是需要 scaffold：列策略、探索路径、迭代深入。

> **[17:14]** "the model was able to do something that they weren't able to do"

关键句是：

> **[18:53]** "nobody had explored sufficiently what happens if I put $100,000 worth of compute into 5.5 what could it do?"

这说明模型能力不只由权重决定，也由人类是否愿意设计 scaffold、投入预算和探索潜在能力决定。某种意义上，前沿模型发布后并不是“能力已经被展示完”，而是“一个能力矿藏被公开”，用户社区和研究者还要继续开采。

## Recursive self-improvement 会发生，但更像渐进重塑研究分工

Brown 不支持“给模型无限预算，它就全域超智能”的简单叙事。

> **[21:22]** "I don't think we're at the point where, okay, you just give it an arbitrary extremely high inference budget and it's just it's just super intelligent across the board."

原因之一是任务类型不同。有些 benchmark 明显随 test-time compute 改善，有些不会。

> **[22:10]** "there's some benchmarks where they clearly improve with more test time compute and there's some where they don't."

更核心的是研究品味。Brown 说模型可以把他的 poker solver 优化到 10-100 倍，但当他要求模型综合所有论文、提出比现有算法更好的新算法时，它做不到。

> **[24:18]** "it's not able to do it."

不过他也没有把 research taste 当作永久人类护城河：

> **[24:55]** "I wouldn't be surprised if we encounter that point for research taste as well."

所以 RSI 的形态不是“今晚爆炸”，而是研究工作被逐步重构。模型已经在加速实验室研究者，但加速不均匀：某些步骤 100x，另一些步骤还是瓶颈。

> **[25:24]** "The models are definitely accelerating what researchers can do inside the labs."

> **[25:28]** "it's more about transforming what researchers do rather than fully replacing the researchers"

Brown 明确反对 overnight intelligence explosion：

> **[25:55]** "I don't think we're headed to that world"

这个判断比乐观或悲观都更实用：AI 研究竞争会越来越被模型放大，但瓶颈会迁移到研究品味、问题选择、实验设计、预算分配和评估治理。

## 多智能体的真正潜力是知识积累，而不是复制同一个模型

Brown 对 multi-agent 的类比很有启发。他不是说“多个 agent 互相聊天就更强”，而是把它类比为人类文明：人类个体没有在 5 万年里进化得更聪明，但文明因为数十亿人长期思考并积累知识而变强。

> **[27:57]** "billions of humans thinking for a long time and building off of each other's accumulated knowledge."

这把 multi-agent 的问题从“并行多少个模型”转向“知识如何沉淀、共享、校验和再利用”。如果 agent 之间只是短期并行采样，那只是更贵的搜索；如果它们能形成可继承知识结构，才接近 Brown 所说的人类文明隐喻。

这也解释了为什么前沿竞争仍然激烈但未必是一夜起飞。模型确实在改进模型研究：

> **[29:58]** "the ability to use the models to improve the model research is a real thing"

但这个改进仍然通过人类研究组织、算力预算、评估方法和安全政策发生。未来优势不会只来自“谁的模型最大”，还来自谁能让模型群体更有效地积累和传递研究知识。

## 关键判断

- 模型能力正在从静态属性变成预算、时间、scaffold 和任务类型的函数。
- benchmark grid 若没有预算轴，会系统性误导模型比较。
- 安全评估必须声明预算假设，否则“模型是否危险”这个问题本身不完整。
- 长时间推理不是默认产品形态，真实产品需要灵活分配 thinking time。
- 已发布模型里存在未开采 latent capability，scaffold 和预算会决定能否释放。
- RSI 更可能先表现为研究工作被模型加速和重构，而不是一夜智能爆炸。
- multi-agent 的长期价值不在并行复制，而在全局知识积累、共享和可继承。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Brown 把 Dwarkesh 的下一训练范式问题推到评估层
**→ [[Dwarkesh Patel- What does the next training paradigm look like]]**
- 本文件论点：Brown 认为模型能力随 test-time compute、预算和 scaffold 变化，甚至需要运行数周或数月才能知道上限 [0:00, 3:31, 15:54]。
- 对方论点：Dwarkesh 认为当前训练范式的问题是部署经验困在 context window 里，无法回流到权重，下一范式要解决持续学习和部署经验蒸馏。
- 关联逻辑：Dwarkesh 讨论模型如何从部署中继续变强，Brown 说明一旦模型运行期变长、能力随预算变化，评估也必须变成长期、预算化、轨迹化。训练范式和评估范式必须一起升级，否则我们既不知道模型学到了什么，也不知道它在高预算下能做什么。

### Brown 为 Sutton 的“目标与奖励”补上预算维度
**→ [[Richard Sutton- Father of RL thinks LLMs are a dead end]]**
- 本文件论点：Brown 认为不是所有任务都会随推理预算改善；事实检索类任务和 Sudoku 类任务对 test-time compute 的响应完全不同 [21:22-22:37]。
- 对方论点：Sutton 认为智能必须有目标和奖励，RL 智能体要从行动后的世界反馈中学习，而不是只预测人会说什么。
- 关联逻辑：Sutton 解释“什么任务有可学习的目标结构”，Brown 解释“给定目标结构后，预算如何改变能力”。两者合起来说明，test-time compute 不是魔法，只有任务有可搜索、可验证、可累积的反馈结构时，长思考才会有效。

### Brown 的 budget curve 具体化了 Evans 的 AI 成本纪律问题
**→ [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Brown 主张评估模型时必须固定 token、cost 或 time，能力要画成 test-time compute 的函数 [4:00]。
- 对方论点：Evans 认为 AI 基础设施处在非均衡状态，未来真正问题是价格纪律、成本上限和价值捕获。
- 关联逻辑：Evans 从产业经济问“钱花到哪里才收得回来”，Brown 从模型评估问“花多少钱才算测到了能力”。两者连接后可以看到，AI 产品未来竞争不是单纯模型强弱，而是单位预算下的能力曲线；谁能用更低成本触达足够能力，谁才有应用层定价权。

### Brown 与 Karpathy 共同把工程师角色推向编排和验证
**→ [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]**
- 本文件论点：Brown 认为模型像 grad student，可以在 gentle steering 下做出很强工作，但研究品味和任务拆解仍是瓶颈 [9:47, 24:18, 25:28]。
- 对方论点：Karpathy 将工程从 vibe coding 推向 agentic engineering，人类职责从直接写代码转向约束、编排、评审和验证 agent。
- 关联逻辑：Brown 给出了为什么人类还没被替代的底层原因：不是模型不会执行，而是高价值任务需要预算分配、scaffold 设计和研究品味。Karpathy 的 agentic engineering 正是这个变化在软件工程里的产品化表达。

---

**元信息**
- 标题：Really Big Test-Time Compute in AI Changes Benchmarks, Safety and Research with OpenAI's Noam Brown
- 频道：No Priors
- 嘉宾：Noam Brown
- 发布时间：2026-06-26
- 时长：36:18
- YouTube链接：https://www.youtube.com/watch?v=AZrU6y3pUcU
