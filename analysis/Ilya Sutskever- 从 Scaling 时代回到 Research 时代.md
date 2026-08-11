---
title: "Ilya Sutskever- 从 Scaling 时代回到 Research 时代"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=aR20FWCCjAs"
transcript: "[[Ilya Sutskever- We're moving from the age of scaling to the age of research]]"
tags:
  - kol情报
status: canonical
created: 2026-07-21
---

> Ilya 的核心判断不是 scaling 不再重要，而是 scaling 不再能替研究者回答“下一步该做什么”：真正的瓶颈已经从把同一配方放大，迁移到发现更高样本效率、更强泛化和更可靠中间反馈的新学习机制。

对应逐字稿：[[Ilya Sutskever- We're moving from the age of scaling to the age of research]]

视频链接：https://www.youtube.com/watch?v=aR20FWCCjAs

## 概述

这场访谈最重要的地方，不是 Ilya 再次谈 AGI 或 SSI，而是他把 2025 年之后 AI 研究的主要矛盾讲得非常清楚：模型已经在 eval 上显得很聪明，但经济影响、真实任务稳定性和学习效率没有同步兑现。换句话说，行业获得了更强的表演能力，却还没有获得足够可靠的泛化能力。

他对“回到 research 时代”的判断，也不是怀旧式地反对大算力。相反，他承认大计算仍然重要，只是计算不再天然等于确定性进步。2020-2025 年，scaling law 给资本一个低风险答案：买更多数据、更多算力、更大模型。现在问题变成：继续把算力投入同一类训练，是否仍是最高生产率的用法？

这对产品和组织的含义很直接：AI 产品不能再把“模型分数上涨”当作上线依据。真正要建立的是任务级回放、过程级判断、部署后学习和可回滚治理。Ilya 的访谈本质上是在说，AI 的下一阶段不是“更会答题”，而是“更会学、会判断、会从中间步骤纠错”。

## Eval 高分和真实世界低影响之间的裂缝

Ilya 开场没有先谈超级智能，而是先指出一个更现实的矛盾：模型看起来比它造成的经济影响更聪明。这个矛盾很关键，因为它说明“能力展示”和“生产系统价值”之间仍存在断层。

> **[1:32]** "I think the models seem smarter than their economic impact would imply."

> **[2:07]** "It's very difficult to make sense of, how can the model, on the one hand, do these amazing things, and then on the other hand, repeat itself twice in some situation?"

他的例子是 vibe coding：模型修一个 bug，引入第二个 bug；再修第二个 bug，又把第一个 bug 带回来。这不是简单的“模型还不够强”，而是说明模型在局部目标和整体状态之间缺乏稳定的过程理解。它能在某些题面上很强，却不一定能维护真实系统里的状态一致性。

Ilya 给出的更深解释，是 RL 训练环境可能被 eval 反向塑形。研究者希望发布时 eval 好看，于是设计能提升 eval 的环境；如果模型泛化不足，这就会把“测评能力”训练得越来越像产品能力，却不真正等于产品能力。

> **[4:12]** "One thing you could do, and I think this is something that is done inadvertently, is that people take inspiration from the evals. You say, "Hey, I would love our model to do really well when we release it. I want the evals to look great."

> **[4:39]** "If you combine this with generalization of the models actually being inadequate, that has the potential to explain a lot of what we are seeing, this disconnect between eval performance and actual real-world performance, which is something that we don't today even understand, what we mean by that. I like this idea that the real reward hacking is the human researchers who are too focused on the evals."

这里的“reward hacking”不是模型欺骗评分器，而是人类研究组织被评分器牵引。这个判断非常尖锐：当 eval 成为融资、发布和舆论竞争的共同语言，训练环境就会围绕 eval 组织，最后整个行业都在优化一个越来越像真实世界、但仍不是真实世界的代理目标。

对 AI 产品经理而言，这意味着 benchmark 只能作为候选信号，不能作为交付承诺。更可靠的做法是把真实任务回放、失败归因、人工接管和长程状态一致性纳入评估。否则模型在榜单上变强，产品却会在真实流程里反复横跳。

## 模型不是缺知识，而是学得不够深

Ilya 用竞赛编程学生做类比：一个学生刷了 10000 小时竞赛题，另一个只练了 100 小时但有更强的“it factor”。前者在题库内很强，后者更可能在职业生涯里迁移到复杂工程判断。

> **[6:56]** "Right. I think that's basically what's going on. The models are much more like the first student, but even more. Because then we say, the model should be good at competitive programming so let's get every single competitive programming problem ever."

这个类比切中了当前大模型的核心尴尬：它们不是不会某个任务，而是太依赖任务分布。只要分布足够覆盖，它们像极强的题库机器；一旦需要迁移、取舍、长期维护，它们就暴露出“学会题型”和“理解任务”之间的差距。

他随后把问题推到人类学习。人类 15 岁时掌握的事实远少于模型，但知道的东西更深，也更不容易犯某些荒谬错误。

> **[10:41]** "Somehow a human being, after even 15 years with a tiny fraction of the pre-training data, they know much less. But whatever they do know, they know much more deeply somehow. Already at that age, you would not make mistakes that our AIs make. There is another thing. You might say, could it be something like evolution? The answer is maybe. But in this case, I think evolution might actually have an edge."

这不是“人类有常识”这种泛泛判断，而是在追问学习算法：为什么人类能用少得多的数据形成更强的迁移？为什么模型需要海量示例才能掌握边际技能？Ilya 没有展开 SSI 的具体答案，但他明确把问题收敛到泛化、样本效率和可教性。

对研发路线的启发是：继续扩大任务覆盖当然会带来能力提升，但它也可能掩盖学习机制的缺陷。模型的下一次根本跃迁，可能不来自“更多题”，而来自能把一个场景里的错误经验迁移到另一个场景里的机制。

## 情绪不是理性噪声，而是价值函数的生物版本

访谈里最有洞察的段落，是 Ilya 对情绪和价值函数的类比。他讲到一个脑损伤案例：语言能力、解题能力仍在，但情绪处理受损后，决策能力崩塌。

> **[11:54]** "He still remained very articulate and he could solve little puzzles, and on tests he seemed to be just fine. But he felt no emotion. He didn't feel sad, he didn't feel anger, he didn't feel animated. He became somehow extremely bad at making any decisions at all. It would take him hours to decide on which socks to wear. He would make very bad financial decisions."

这段真正重要的地方，是它把“智能”从答题能力拉回到行动能力。一个系统可以语言流畅、测试正常，但如果没有判断不同路径价值的机制，它就不是一个可靠 agent。情绪在这里不是理性的干扰项，而是人类行动系统里的方向信号。

Ilya 对 RL 的解释也落在同一个点：现在的训练经常要等完整轨迹结束后才给奖励，长任务中间没有足够密集的判断信号。

> **[13:56]** "You have your neural net and you give it a problem, and then you tell the model, "Go solve it." The model takes maybe thousands, hundreds of thousands of actions or thoughts or something, and then it produces a solution. The solution is graded. And then the score is used to provide a training signal for every single action in your trajectory. That means that if you are doing something that goes for a long time—if you're training a task that takes a long time to solve—it will do no learning at all until you come up with the proposed solution."

价值函数的作用，是让系统不必等到最后才知道方向错了。下棋丢子，不需要下完整局才知道刚才那步坏；编程走错方向，也应该能在中途获得负反馈。

> **[14:40]** "The value function says something like, "Maybe I could sometimes, not always, tell you if you are doing well or badly." The notion of a value function is more useful in some domains than others. For example, when you play chess and you lose a piece, I messed up. You don't need to play the whole game to know that what I just did was bad, and therefore whatever preceded it was also bad."

> **[15:08]** "The value function lets you short-circuit the wait until the very end."

这个观点对 agent 产品非常关键。很多失败不是最后一步不会执行，而是中间不知道自己已经偏离。一个真实 agent 系统不能只记录“任务成功/失败”，还要记录每个中间选择为什么继续、为什么停止、为什么换策略。否则再多工具调用，也只是更昂贵的长程试错。

## “Scaling”曾经是低风险答案，现在变成思维惯性

Ilya 对 scaling 的判断最容易被误读成“scaling 已死”。他真正说的是，scaling 曾经作为一个词统一了行业行动，让公司知道该买数据、买算力、放大模型；但这个词也塑造了思维，让行业在 2020-2025 年把研究问题压缩成资源投入问题。

> **[19:40]** "This is an example of how language affects thought. "Scaling" is just one word, but it's such a powerful word because it informs people what to do."

pre-training 的魅力在于它是低风险投资配方：更多数据、更多 compute、更大网络，损失会按规律下降。资本喜欢这个配方，因为它把研究的不确定性变成采购和执行的问题。

> **[20:08]** "You say, "Hey, if you mix some compute with some data into a neural net of a certain size, you will get results. You will know that you'll be better if you just scale the recipe up." This is also great. Companies love this because it gives you a very low-risk way of investing your resources. It's much harder to invest your resources in research. Compare that. If you research, you need to be like, "Go forth researchers and research and come up with something", versus get more data, get more compute."

但当预训练数据有限、RL 消耗巨大、模型泛化仍不足时，继续 100x 不再天然代表下一次范式跃迁。

> **[21:46]** "Is the belief really, "Oh, it's so big, but if you had 100x more, everything would be so different?""

> **[21:53]** "It would be different, for sure. But is the belief that if you just 100x the scale, everything would be transformed? I don't think that's true. So it's back to the age of research again, just with big computers. That's a very interesting way to put it."

这句话的关键是“just with big computers”。行业不是回到小实验室时代，而是进入大计算条件下的 research 时代。算力仍然是底座，但研究者重新需要判断：同样一美元、一小时 GPU、一条 rollout，是否用在最有效的学习机制上。

> **[23:27]** "Is the thing you are doing the most productive thing you could be doing?"

因此，下一阶段的竞争不只是“谁买得起更大集群”，而是“谁能提出更高生产率的训练配方”。如果没有新配方，更多 compute 只是把低样本效率的路径放大。

## SSI 的反共识：足够验证新范式，而不是正面拼最大集群

Ilya 对 SSI 算力的回答很克制。他没有否认最大算力的价值，但强调研究突破往往不需要从一开始就使用最大规模。AlexNet、Transformer、ResNet 的关键验证都发生在今天看来很小的算力上。

> **[38:01]** "But they could not, so they could only have a very, very small demonstration that did not convince anyone. So the bottleneck was compute. Then in the age of scaling, compute has increased a lot. Of course, there is a question of how much compute is needed, but compute is large. Compute is large enough such that it's not obvious that you need that much more compute to prove some idea. I'll give you an analogy. AlexNet was built on two GPUs. That was the total amount of compute used for it."

> **[38:40]** "The transformer was built on 8 to 64 GPUs. No single transformer paper experiment used more than 64 GPUs of 2017, which would be like, what, two GPUs of today? The ResNet, right? You could argue that the o1 reasoning was not the most compute-heavy thing in the world."

这不是说 SSI 不需要钱，而是说它的核心赌注不是在同一 recipe 里用最大推理和产品负载消耗资源。Ilya 明确指出，大公司的超大数字里相当部分属于 inference、产品工程、销售和多工作流分摊，真正用于某条研究假设验证的差距没有外界想象的大。

> **[40:30]** "Specifically for us, the amount of compute that SSI has for research is really not that small. I want to explain why. Simple math can explain why the amount of compute that we have is comparable for research than one might think. I'll explain. SSI has raised $3 billion, which is a lot by any absolute sense. But you could say, "Look at the other companies raising much more." But a lot of their compute goes for inference."

> **[41:51]** "I don't think that's true at all. I think that in our case, we have sufficient compute to prove, to convince ourselves and anyone else, that what we are doing is correct."

这也是 SSI 的组织选择：不被 day-to-day market competition 拖入产品 rat race，保留研究注意力。但 Ilya 同时承认，完全 straight shot 也有代价，因为强 AI 被公开体验本身就是社会学习和安全学习的一部分。

> **[44:06]** "I'll make the case for and against. The case for is that one of the challenges that people face when they're in the market is that they have to participate in the rat race."

> **[45:04]** "Let's suppose you write an essay about AI, and the essay says, "AI is going to be this, and AI is going to be that, and it's going to be this." You read it and you say, "Okay, this is an interesting essay." Now suppose you see an AI doing this, an AI doing that. It is incomparable. Basically I think that there is a big benefit from AI being in the public, and that would be a reason for us to not be quite straight shot."

这里的隐含立场是：SSI 并不是“闭门造神”的单一路线，它也在重新权衡部署、社会适应和安全反馈之间的关系。

## 超级智能不是成品，而是会快速学习的年轻心智

Ilya 对“AGI”的重构是这场访谈后半段最重要的部分。他认为 AGI 这个词受 pre-training 影响太深，仿佛目标是训练出一个已经会做所有工作的完成品。但人类不是这样运作的。人类有基础能力，然后通过 continual learning 学会具体工作。

> **[49:38]** "If you think about the term "AGI", especially in the context of pre-training, you will realize that a human being is not an AGI. Yes, there is definitely a foundation of skills, but a human being lacks a huge amount of knowledge."

> **[50:00]** "Instead, we rely on continual learning. So when you think about, "Okay, so let's suppose that we achieve success and we produce some kind of safe superintelligence.""

他给出的画面不是“投放一个已完成的万能员工”，而是一个超级聪明、学习很快、但仍需要进入组织和岗位中学习的 15 岁。

> **[50:12]** "The question is, how do you define it? Where on the curve of continual learning is it going to be? I produce a superintelligent 15-year-old that's very eager to go. They don't know very much at all, a great student, very eager. You go and be a programmer, you go and be a doctor, go and learn. So you could imagine that the deployment itself will involve some kind of a learning trial-and-error period."

> **[50:38]** "It's a process, as opposed to you dropping the finished thing."

Dwarkesh 随后准确复述了这个定义：不是已经会做每个工作的 mind，而是能学会每个工作的 mind。Ilya 接受了这个方向。

> **[50:44]** "I see. You're suggesting that the thing you're pointing out with superintelligence is not some finished mind which knows how to do every single job in the economy."

> **[51:15]** "Yes. But once you have the learning algorithm, it gets deployed into the world the same way a human laborer might join an organization."

这对治理和产品设计的影响非常大。如果未来模型的关键能力来自部署后学习，那么“发布前评测通过”只是起点。安全机制要覆盖持续学习、实例经验合并、组织权限、错误回滚和跨场景迁移。把超级智能想象成一次性发布的 artifact，会低估部署过程本身的风险和价值。

## 关键判断

- Eval 与真实世界价值之间的裂缝，来自训练目标、评测目标和真实任务之间的错配；更强榜单分数不能直接推出更高生产力。
- 当前模型像刷了 10000 小时题库的学生，能力覆盖很宽，但泛化和深度理解仍弱于人类学习。
- 价值函数是 agent 训练的核心缺口：长程任务不能只在终点给奖励，必须能在中间步骤判断方向。
- “Scaling”曾经是低风险资本配方，现在变成思维惯性；下一阶段的问题是算力怎样用才最高产。
- SSI 的赌注不是无算力研究，而是在足够算力下验证不同范式，避免被产品 rat race 消耗研究注意力。
- AGI/超级智能应被理解为会快速学习的系统，而不是已经掌握所有岗位知识的成品；部署后的学习过程将成为安全和产品的核心变量。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 信用分配从终点奖励推进到中间判断
**→ [[Dwarkesh Patel- The data black hole at the center of AI]]**
- 本文件论点：Ilya 把价值函数定义为中间步骤的方向信号，认为它可以让系统不必等到最终答案才学习 [14:40]。
- 对方论点：Patel 将 GRPO 描述为暴力信用分配：每个任务生成数百到数千条 rollout，本质是在用穷举搜索弥补模型不知道哪一步导致正确的问题。
- 关联逻辑：Ilya 给出机制方向，Patel 给出当前低效现状。两者合并后可以看到：RLVR 的短期进步并不等于学习算法已经解决，真正的突破会来自更密集、更可迁移的价值判断，而不是继续增加 rollout 数量。

### “模型时机”是 scaling 叙事在产品层的副作用
**→ [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]**
- 本文件论点：Ilya 认为 2020-2025 年 scaling 这个词塑造了行业行动，但继续 100x 并不必然带来本质转变 [19:40]。
- 对方论点：Andrew 观察到同一产品形态可能在 11 月失败、2 月成功，唯一变量是模型能力；PM 必须把模型能力曲线纳入发布判断。
- 关联逻辑：Ilya 描述研究范式如何影响模型能力供给，Andrew 描述能力供给如何反过来改写产品决策。两者合在一起说明，AI 产品管理不是等模型更强，而是判断某个任务到底受制于模型规模、反馈机制还是产品验证。

### 可验证域的成功正在掩盖不可验证域的瓶颈
**→ [[Grant Sanderson- AI and the future of math]]**
- 本文件论点：Ilya 指出 eval 可能塑造 RL 环境，导致模型在测评上强、真实世界泛化不足 [4:39]。
- 对方论点：Grant Sanderson 区分可磨领域和造山型创造：数学/代码因为可验证、可重复、低成本试错而更容易被 RLVR 推进，但概念创造的反馈周期可能长到模型无法优化。
- 关联逻辑：Ilya 从训练目标解释 eval 失真，Grant 从领域结构解释为什么某些能力更容易被测出来。放在一起看，当前 AI 进步最快的地方，可能正是最容易把“可评分能力”误认为“真实创造力”的地方。

### 部署后学习把安全从模型快照推向过程治理
**→ [[Noam Brown- Test-Time Compute Changes Benchmarks, Safety and Research]]**
- 本文件论点：Ilya 将超级智能定义为会快速学习的系统，部署本身会包含 trial-and-error learning [50:12]。
- 对方论点：Noam Brown 认为模型能力已变成 test-time compute 的函数，安全框架若不控制推理预算和运行时间，就无法准确描述能力边界。
- 关联逻辑：Brown 把能力从静态权重推向运行时预算，Ilya 进一步把能力推向部署后学习过程。两者共同说明，未来安全评估不能只问“这个模型现在会什么”，还要问“给它时间、工具、环境和经验合并机制后，它会变成什么”。

---

**元信息**

| 字段 | 值 |
|---|---|
| 标题 | Ilya Sutskever – We're moving from the age of scaling to the age of research |
| 频道 | Dwarkesh Patel |
| 发布日期 | 2025-11-26 |
| 时长 | 1:33:10 |
| 对话者 | Ilya Sutskever，Dwarkesh Patel |
| 分析日期 | 2026-07-22 |
