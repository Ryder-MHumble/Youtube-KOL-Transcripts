---
title: "Dwarkesh Patel- What does the next training paradigm look like"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=20p5-kQXF_Q"
tags:
  - kol情报
---

> 当 AI 在部署中学习的一切都困在 context window 里、无法回到权重——你面前是一个"天才实习生每六个月被格式化一次"的荒谬循环。下一个训练范式的赌注，就是打破这个循环。
>
> —— Dwarkesh Patel, 2026年6月

**视频链接**：https://www.youtube.com/watch?v=20p5-kQXF_Q

**概述**：Dwarkesh Patel 以独白视频 essay 形式（改编自其博客文章），系统梳理 AI 实验室正在下的"大赌注"：通过 RLVR（Reinforcement Learning from Verifiable Rewards）在数千个可验证环境中训练 AI，最终实现 AGI。但这场赌注有三个未被解决的深层缺口：样本效率比人类低百万倍、部署中学到的知识无法回到权重、无法在不可验证域（创业、政治、交易）中构建 RL 环境。Patel 提出"做梦"（dreaming）作为可能的第四条 scaling 轴，并勾勒了 2027 年持续学习可能的工作图景。

**主题脉络**：RLVR 大赌注 → Grindability 比 verifiability 更关键 → RLVR 能否泛化 → 部署学习的权重回流难题 → 在策略自蒸馏（OPSD）→ 做梦：第四条 scaling 轴 → 2027 图景。

---

## 一、RLVR 的大赌注——"在容器化世界里训练出的智能，能处理真实世界吗？"

### 1.1 实验室的隐含假设

所有 AI 实验室正在押注同一个方向：在数千个可验证、可并行的 RL 环境中训练 AI 完成数百万个任务，就能造出 AGI。Patel 指出，乐观主义者认为当前训练范式的所有"根本缺陷"——数据低效、缺乏持续学习——都可以被更多训练碾压，就像 NLP 的所有研究问题在 LLM 出现后都坍缩了一样。

但 Patel 在前一个视频中已经论证：这些模型训练时的样本效率只有人类的一百万分之一。乐观派的反驳是——那只发生在训练时，训练是一次性成本，被数十亿次会话摊薄；真正重要的是会话中模型的智能和泛化能力，而这确实在改善。

```plaintext
[02:00] the people who are optimistic about this vision will say that all these things we talk about as the fundamental deficits in the current training paradigm — for example, the data inefficiency of these models, or the fact that they lack continual learning — can just be steamrolled if we scale training more, in the same way that all the fundamental research problems in natural language processing collapsed when we threw enough compute into LLMs.
```

### 1.2 持续学习——"不需要"论的脆弱

乐观派还主张：持续学习（权重在部署中更新）可能根本不必要。如果 in-context learning 足够好、context window 足够大，为什么不把"六个月入职期"全部塞进 context window？几年后可能有无穷大的 context window。

Patel 对此没有直接否定，而是转向一个"切线问题"来揭示深层结构。

---

## 二、Grindability——比可验证性更隐蔽的瓶颈

### 2.1 为什么 computer use 进展比编码慢？

Computer use 明明是可验证的——Etsy 订单送达了吗？场地订好了吗？报税提交了吗？但它的进展远慢于编码和数学。Patel 给出了一个被低估的原因：一个领域不仅要"可验证"（verifiable），还要"可研磨"（grindable）——你必须能从同一起点跑大量并行 rollout，环境必须是确定性的、可重放的。

编码可以：定义一个容器，里面有缺失功能的代码仓库，让一千个并行 agent 各自尝试。但 computer use 做不到：你不能让一千个 agent 在 Amazon 上跑同一个结账流程，因为 Andy Jassy 会封杀你的 bot。

```plaintext
[05:00] you can't just have a thousand agents go try the same checkout flow on Amazon to get better at using websites, because Andy Jassy will find your bots and shut your ass down.
```

### 2.2 不可研磨的领域——真实世界没有重放按钮

这揭示了一个更深的限制：大量人类技能的 RL 环境无法在数据中心内重建。怎么训练 AI 像 Elon Musk 一样建立火箭公司？像 LBJ 一样赢参议院选举？这些 rollout 需要与真实世界交互，无法重放、无法并行、outer-loop 验证可能需要数月或数年。

```plaintext
[07:30] the outer-loop verification here may take months or even years of real-world actions to elicit, and you can't re-observe it by perturbing the model's actions slightly in thousands of parallel rollouts to isolate exactly what the model did that actually worked.
```

---

## 三、RLVR 能否泛化——Dario 的暗示

### 3.1 从短horizon到长horizon的泛化断裂

Patel 引用 Dario Amodei 在播客中说的一句话作为反证：Dario 解释为什么模型在长 context 下性能退化时说——"你训练时的 context 长度和推理时的 context 长度是两件事。如果你在短 context 训练、在长 context 推理，就会退化。"

Patel 的推论：如果短horizon RL 训练不能泛化到长horizon性能，那你怎么期望模型从"在白领任务上训练"泛化到"被丢到真实世界从零创业"？

```plaintext
[10:30] if you can't generalize from short horizon to long horizon, then how are agents supposed to generalize from getting trained at a bunch of white-collar tasks to, say, having the ability to be dropped in the real world and build a business from scratch as well as Sam Walton?
```

---

## 四、权重回流——"天才实习生每六个月被格式化"

### 4.1 30-50% 算力被浪费

Patel 指出一个巨大的结构性浪费：实验室 30-50% 的算力用于推理，但这些推理过程中产生的信息——模型在真实部署中学到的最宝贵的知识——没有对模型本身产生任何改进。模型在每次会话中学到的东西都困在 context window 里，会话结束就消失。

```plaintext
[12:00] around 30 to 50 percent of a lab's compute goes to inference, and that compute is currently not playing any productive role in helping improve the model. This seems like a huge waste.
```

Patel 的隐喻一针见血：一个天才研究生，从不被允许实习，只给课堂案例。已经被广泛部署到经济中、掌握大量组织特定隐性知识的 AI，却无法利用这些知识。

### 4.2 为什么不能直接用更大的 context window？

因为 context window 的扩展不像权重更新。人类学习不是把所有观察到的信息精确存放在"脑子里"——人类大脑没有参数和激活之间的清晰分界，学习伴随着压缩，压缩帮助泛化。而有自闭症学者症候群的人——能精确回忆随机数字表——这种信息量反而削弱了抽象和隐喻能力。

```plaintext
[14:00] when we learn stuff, there's clearly some kind of compression, and this aids our generalization and grokking.
```

---

## 五、OPSD——在策略自蒸馏

### 5.1 机制

Patel 介绍了 on-policy self-distillation（OPSD）的技术思路：鼓励 base model 做出与"积累了长会话经验的 veteran model"相同的预测。不要求外部可验证的 reward——只需要一个能在 context window 内学到正确东西的模型。而且比 RL 的信号更密集——不用把单个 reward 投射到整条轨迹，而是逐 token 训练。

### 5.2 为什么比 SFT 和 RL 都好

朴素 SFT 的问题：训练模型预测会话中观察到的所有 token——但"更好工作的方式不是回忆每天发生的一切"。RL 的问题：信号太稀疏。OPSD 保留了 RL 的"只改变必要的部分"特性，同时提供了更密集的监督。

```plaintext
[18:00] you only change the model as much as is absolutely necessary to achieve the outcome, and no more. OPSD preserves this property of RL, where instead of slingshotting towards the teacher distribution as supervised learning would have you do, you only extract the knowledge that is necessary.
```

---

## 六、做梦——第四条 Scaling 轴

### 6.1 EfficientZero 的先例

DeepMind 发布 AlphaZero 几年后，EfficientZero 证明：如果模型在真实游戏每一步都在"脑中"跑几十局模拟，那么用同样的两小时游戏数据，模型可能击败新手人类。AI 可能用类似方式——在"脑中"构建现实模拟，在其中练习新技能，体验远超真实世界能提供的样本量。

```plaintext
[20:00] for each step in the real game, EfficientZero is playing dozens of simulated games in its head. In a similar way, future LLMs might be able to consume far less real-world data while practicing endlessly against environments that they build for themselves.
```

### 6.2 /dream 命令

Patel 的愿景：未来的模型不会只按 /compact 做小规模摘要计算，而是按 /dream——烧掉大量算力，构建一个真实世界的"游戏版本"，在其中排练即将在真实部署中使用的所有技能。这会成为继 pretraining、RL、inference-time compute 之后的第四条 scaling 轴。

```plaintext
[21:00] instead of hitting /compact in Codex or Cursor or Claude, which kindles a small amount of compute to write up a summary, you hit /dream. And this incinerates huge amounts of compute to build and train against a video-game version of what the model is witnessing in the real world.
```

---

## 七、2027 图景——持续学习的完整循环

### 7.1 从 RLVR 到部署到回流

Patel 勾勒的可能路径：RLVR 训练出一个"足够胜任"的 agent → 部署到真实世界做实际工作（即使任务在训练分布外）→ AI 与人类 cowork 一周 → 周末给出 thumbs up/down → base model 蒸馏会话中学到的一切（用 OPSD、dreaming 或未知技术）→ 下一轮 AI 在之前学到的领域附近变得更好 → 循环往复。

```plaintext
[23:00] the main way that AIs get better is not from the training they have received before they are released to the public. Rather, it's from all this experience that they'll be accumulating from being broadly deployed in the economy.
```

### 7.2 每次交互都让 AI 更聪明

在这个图景中，AI 改进的主要来源不再是发布前的训练，而是部署后的经验积累。每次你与 AI 交互，它都更聪明——不仅因为它从你的会话中学到，还因为它从所有其他用户的会话中学到。

```plaintext
[24:00] every time that you interact with an AI, it'll be smarter, not only because it's been learning from your previous sessions, but also because it's been learning from all its interactions with all the other users in the world. And that's very scary and exciting and different from the way that AI improves right now.
```

---

## 元信息

| 字段 | 值 |
|------|-----|
| 标题 | What does the next training paradigm look like? |
| 频道 | Dwarkesh Patel |
| 发布时间 | 2026-06-26 |
| 时长 | 19:53 |
| YouTube 链接 | https://www.youtube.com/watch?v=20p5-kQXF_Q |
| 分析时间 | 2026-06-30 |

---

## 深度关联

### → [[Dwarkesh Patel- The data black hole at the center of AI]]

**本文件论点**：Dwarkesh 论证 RLVR 的大赌注——在可验证环境中训练出通用 agent——面临泛化断裂：短horizon训练无法泛化到长horizon性能（引用 Dario 的话作为反证）。

**对方论点**：Dwarkesh 在前一个视频中论证 GRPO 暴力穷举是样本效率百万倍差距的结构性根源——模型不是在"思考"而是在穷举搜索正确路径。

**关联逻辑**：递进——同一作者的两篇文章构成递进关系。前一篇诊断了"为什么样本效率低"（信用分配太稀疏），本篇追问"低样本效率下 RLVR 大赌注能否成立"。前一篇的结论（GRPO 是暴力穷举）直接支撑了本篇的质疑——如果训练时就是穷举而非学习，那么"穷举出的智能能否泛化到真实世界"就是必然要问的下一题。

### ← [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]

**本文件论点**：Dwarkesh 提出持续学习需要权重回流——部署中学到的知识必须通过 OPSD 或 dreaming 回到权重，否则 AI 是"每六个月被格式化的天才实习生"。

**对方论点**：Ilya 论证"Scaling"这个词塑造了5年行业方向，现在需要回到 Research 时代。

**关联逻辑**：补充——Ilya 宣告了 Scaling 时代的终结，Dwarkesh 指出了下一个时代要解决的核心问题：持续学习。如果 pretraining scaling 和 RLVR scaling 都无法让模型在部署中学习，那么下一个突破必然来自新的训练范式（OPSD/dreaming），而非更大的 pretraining run。Dwarkesh 的"dreaming 作为第四条 scaling 轴"是 Ilya"回到 Research"的具体路径之一。

### → [[Karpathy- We're summoning ghosts, not building animals]]

**本文件论点**：Dwarkesh 指出 AI 在部署中学习的一切困在 context window 里无法回到权重——KV cache 不断膨胀但不可持续，人类学习伴随压缩而非堆叠。

**对方论点**：Karpathy 诊断 RL 信号太稀疏——一分钟轨迹只得到一个标量，无法判断哪一步导致了正确或错误。

**关联逻辑**：互补——Karpathy 诊断了训练阶段的信用分配稀疏（RL 只在最后给一个 reward），Dwarkesh 诊断了部署阶段的信用分配缺失（部署中学到的知识无法回到权重）。两人共同指向同一个结构缺口：AI 缺乏"从经验中提取关键洞察并固化"的机制——训练时信号太稀疏，部署时信号根本不回流。Dwarkesh 的 OPSD 方案正是对 Karpathy 诊断的直接回应。
