---
title: "Dan Roberts- Why AI Can Now Make Discoveries"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=oWOz2htozfI"
tags:
  - kol情报
---

> 当强化学习从蛋糕上的樱桃变成蛋糕本身，AI 正在用「逆势思考 + 长链推理」跨越从工具到科学家的临界点——而这场跨越的赌注，是人类能否用 RL 把算力真正转译为发现新知识的能力。
> —— Dan Roberts / Matt Turck, 2026-06

视频链接：https://www.youtube.com/watch?v=oWOz2htozfI

**概述**：2026 年 6 月初，在 OpenAI、DeepMind、Anthropic 几乎同时宣布攻克 Erdős 数学问题的数日之后，Matt Turck 邀请 OpenAI 强化学习基础团队负责人 Dan Roberts 做客 The MAD Podcast。Roberts 是理论物理博士（MIT，量子引力与量子信息方向），曾任职 FAIR，合著《The Principles of Deep Learning Theory》，两年前加入 OpenAI。这场对话的核心赌注是：RL + test-time compute 是否构成了 AI 从「执行指令」到「自主发现」的范式跃迁，以及这条路能走多远。

**主题脉络**：
1. Erdős 问题的两条路线——形式化验证 vs 非形式推理，折射出不同实验室对「AI 科学家」的定义分歧
2. RL 范式的反转——从「蛋糕上的樱桃」到「蛋糕本身」，算力转译为智能的主引擎
3. 语言先验 vs 纯 RL——对 Rich Sutton 立场的隐性反驳
4. 可验证奖励的边界——从数学到创意写作的鸿沟
5. 物理学方法移植——从大到小理解 scaling，追求 AI 的热力学

---

## 一、Erdős 问题的两条路线：谁在定义「AI 科学家」

### 1.1 一个逆势的证明

对话开场即锚定在一个具体事件上：OpenAI 的模型攻克了 Erdős 中的 unit distance conjecture。这个猜想说的是关于平面上点对距离的一个下界，所有人都默认它成立——但 OpenAI 的模型做了一件人类很少做的事：假设它是错的。

```plaintext
[~03:30] This conjecture everyone assumed was true and uh but could not prove it. One of the things that ChatGPT was able to do was assume it was false. And when you go against the grain and do something contrarian like that, you really have to have strong conviction in what you're doing in order to persevere down a really long calculation path.
```

Roberts 强调了三个要素的叠加：逆势假设、长链计算的持久性、以及跨领域专业知识（代数数论）。这条路径上任何一个选择出错，整条证明链就断裂。模型不仅需要知道哪个问题有趣，还需要在一个完全不同的数学领域拥有深度，然后还必须足够「叛逆」去反驳共识。这三者的交集——Roberts 自己也承认——在人类研究者中极其罕见。

### 1.2 形式化 vs 非形式化：两种「AI 数学家」

真正揭示产业分歧的，是 Roberts 对 OpenAI 和 DeepMind 两条路线的对比。

```plaintext
[~05:00] One of the approaches that GDM takes is to take problems, present them in a formal language called lean and then use methods to search for proofs in that language... it's designed so that the proofs can be airtight... Another approach is to just take the problem in English with mathematical expressions as well but just the English statement of it which is informal and understand what is meant by that and solve that in informal language presenting a proof much like the way a human mathematician would.
```

DeepMind 的路线是：数学问题 → Lean 形式化语言 → 自动搜索证明 → 结果天然可验证。OpenAI 的路线是：直接用自然语言理解问题，像人类数学家一样在非形式化空间中推理，然后需要人工或外部检查验证。这不是技术细节的差异，而是对「AI 科学家应该像什么」的根本分歧：是构建一个在封闭形式系统中搜索的定理证明器，还是构建一个像人类一样在模糊自然语言中思考、能跨越不同领域建立联系的推理者？Roberts 明确将 OpenAI 定位在后者，并暗示这条路更接近真正的科学发现——因为真正的科学发现往往不在形式化系统内发生。

---

## 二、RL 范式的反转：从樱桃到蛋糕

### 2.1 一个被反转的 meme

Roberts 在一年半前的一次公开演讲中翻转了 LeCun 的著名比喻。

```plaintext
[~17:00] RL is really exciting. That's why what I'm here talking about. And I think that when you have a lot of compute, you want to turn that compute into intelligence in a way that's that's useful. And RL is one way of doing it. and we just started doing it then and we're going to do a lot more of it now.
```

LeCun 说 RL 是蛋糕上的樱桃（占比极小），Roberts 反过来说 RL 现在是蛋糕本身。这个反转的背后是一个产业级判断：pre-training 的 scaling 正在进入递减区间，而 RL on top of pre-training 是新的 scaling 维度。Roberts 甚至给出了更具体的表述——「如果你只 scale pre-training，你到不了我们现在能到达的地方；同时在 pre-training 上 scale RL，模型就强大得多」。这是对「scale is all you need」的一次精细修正：scale 仍然是对的，但 scale 的对象从 pre-training 转移到了 RL。

### 2.2 「吸管」批判与 RL 的信息效率

Matt Turck 引用了一个 2025 年初的病毒式分析——RL 每一万个 token 产出不到一比特有用信息，Karpathy 称之为「通过吸管吮吸监督信号」。Roberts 的回应值得拆解：

```plaintext
[~20:00] if you look at like the DeepSeek algorithm which is a public thing that that we can talk about then the you train on sequences that are correct. So whether it's correct or not is maybe one bit of information. So I think there's you know you can see where that logic comes from. I think the question is like is this doing a kind of thing that you can't otherwise do?
```

他没有否认「一比特」的描述——在 DeepSeek 式的 GRPO 算法中，信号确实近似于「对/错」的一比特。但他的反驳角度是：你没法用其他方式提供更多监督。稀疏奖励的效率低下是结构性的，但它是目前唯一能在数学和编程等可验证领域实现突破的路径。换句话说，吸管虽细，但它是唯一能接到水的管子。

### 2.3 探索与利用的交织

Roberts 用 unit distance 证明和后续的人类跟进工作，描绘了科学发现中 explore-exploit 的真实图景。

```plaintext
[~15:00] the OpenAI unit distance proof I think is very much in the explorer setting where the model was happy to be contrarian... it was spending a very long amount of time... hours and hours trying different things... a lot of times though you can ask these models to compute something that they understand very well and then that has a different structure and might look a lot like exploit.
```

他提到 OpenAI 模型 disproved unit distance conjecture 后，人类研究者受此启发，将类似思路应用于另一个不相关的集合论问题（sum-product 猜想）并同样成功反驳。这是 exploit——但 exploit 的种子来自 AI 的 explore。科学发现不是纯粹的探索或纯粹的利用，而是两者的交织循环。这也暗示了 AI 与人类科学家的互补结构：AI 做长链探索，人类做跨域 exploit。

---

## 三、语言先验 vs 纯 RL：对 Sutton 的隐性反驳

### 3.1 酒吧里的三个学科

Roberts 讲了一个年轻时在牛津酒吧的辩论：物理学家（他）认为物理最根本，认知科学家认为认知偏差更根本，语言学家（维特根斯坦立场）认为一切都经过语言。

```plaintext
[~25:00] I sort of feel like he and Victor like that that was correct, right? That's what's what or at least the path through AI suggests that that is a correct path... everything goes through language right all the internet... it incorporates the grounding of the real world all of our scientific knowledge all of our mathematical knowledge... having the model have a prior of language and being able to think in language and then train on top of that. That seems like clearly the right thing to do.
```

这是对 Rich Sutton「LLM 不是真正的智能，纯 RL 才是」的直接反驳。Roberts 的论证不是从计算理论出发，而是从认识论出发：语言是人类知识的载体，互联网上凝聚了人类文明的全部产出。用语言作为先验，等于让模型站在整个人类知识积累的肩膀上。纯 RL（如 AlphaGo 式的从零自对弈）固然能在封闭博弈中超越人类，但在开放世界的科学发现中，没有语言先验就等于放弃了人类数千年积累的全部知识。这个立场也解释了为什么 OpenAI 选择 LLM + RL 的路线，而非 DeepMind 早期式的纯 RL 路线。

### 3.2 「好主意」的来源

Roberts 还给出了一个更隐蔽的反驳——他不认同 Sutton「scale is all you need」背后的还原论。

```plaintext
[~27:00] I have a somewhat contrarian take that with the better lesson that it's not that scale is all you need. You need to also have good ideas to guide the scaling... if you were just trying to scale pre-training, you wouldn't get anywhere near as far as also trying to scale RL on top of pre-training.
```

这里的措辞很关键：他说「good ideas come from humans」——在当前阶段，scaling 的方向选择仍然依赖人类的科学判断。这既是对纯 scaling 主义的修正，也是对「AI 自主研究 AI」时间线的隐含判断：在人类还无法完全将「如何 scale」这个判断本身交给 AI 之前，纯粹的自递归提升不会发生。

---

## 四、test-time compute 的机制与可验证奖励的边界

### 4.1 链式思考不是黑箱

Roberts 对 test-time compute 的描述异常坦诚——它就是你看到的那串 token。

```plaintext
[~31:00] I think it does what what you see it do. We lightly rewrite it or summarize it. But it just produces tokens and those tokens are like a running thought process... it's a forward pass the model. So we're using a bunch of computation... it's a way of leveraging a lot more computation on a problem than you would before.
```

这里的核心机制是：单个 forward pass 的算力有限，但通过生成一长串 token（思考链），模型可以复用自身权重，将最终答案变成一个远大计算量的函数。Noam Brown 的 reasoning hypothesis 是这个逻辑的极致版本——如果模型能思考数年，它能解决什么？Roberts 明确指出，RL 训练的产出就是「让模型能在 test time 思考」的能力本身。推理努力旋钮（reasoning effort dial）不是后处理，而是 RL 训练的直接产物。

### 4.2 可验证奖励的硬边界

Matt Turck 追问了一个关键问题：RL 能否泛化到没有可验证奖励的领域——咨询、银行、法律？Roberts 的回答结构性地回避了技术路径的正面回答。

```plaintext
[~36:00] I definitely think OpenAI will have amazing products that will be relevant in those domains and some amount of RL will play a role in there.
```

注意措辞的精确性：他说的是「OpenAI 会有 amazing products」和「some amount of RL will play a role」——而不是「RL 会有效解决不可验证领域的问题」。他回避了机制层面的回答。在定义可验证奖励时，他自己也承认了这个抽象「有各种问题」，而不可验证的问题（如创意写作的好坏）涉及「taste」和分布性判断。这暴露了当前 RL 范式的结构性边界：在 reward 可被 string match 的领域（数学、编程），RL 带来了突破；在 reward 本身模糊的领域，RL 的角色从「引擎」退化为「辅助」。Roberts 没有展开这个判断，但他的措辞选择本身就是一种信号。

---

## 五、物理学方法移植：从大到小理解 scaling

### 5.1 「涌现」是一种理解失败

Roberts 提出了一个极具方法论意义的反直觉观点：scaling 应该从大到小理解，而非从小到大。

```plaintext
[~38:00] I reject that entirely. I think it means that you didn't understand something about what you were scaling up... your job is to then figure out how to restore smoothness to the scaling sequence. Go back and make smaller and simpler models or simpler toy examples such that the whole thing is smooth. And if you can do that, if you can figure out what to put into the small thing, then you understand the thing.
```

当人们说某个能力「在 scale 上涌现了」，Roberts 认为这恰恰说明你没有理解你在 scale 什么。正确的方法论是回退到更小的模型或更简单的 toy example，找到能复现该现象的最小设置——这正是物理学的方法。标准模型写出来有一整页、无数粒子和抵消项，但你研究电磁学时可以忘掉其他一切。物理学家不是在研究「球面奶牛」（spherical cow）的简化，而是在找到包含你所关心现象的最简系统。如果这个简化能复现现象，你就理解了它；如果不能，你的简化选错了。

### 5.2 AI 的热力学尚未完成

Roberts 将 scaling laws 类比为热力学的早期阶段——Kaplan/McCandlish 的 scaling laws 是一种有效描述，就像理想气体定律，但从微观（权重和偏置）到宏观（scaling law）的统计力学桥梁还缺失。

```plaintext
[~42:00] the missing piece is going from all the individual weights and biases and how does that add up to the scaling law. I have some very initial work... but I think that's the missing piece, the sort of statistical mechanics to thermodynamics of how do these things emerge.
```

这个判断的产业含义是：当前 AI 领域有宏观的实证规律（scaling laws），但缺乏从微观到宏观的理论桥梁。Roberts 自己正在做这个方向的最早期工作。这也暗示了一个更深层的信念——AI 系统不是不可理解的黑箱，它应该像物理系统一样服从可被理论化的规律。这种信念与「emergence」叙事形成对立：后者将大规模模型的能力视为不可预测的涌现，前者则认为一切都可以被还原理解。

---

## 六、九年到爱因斯坦：预测的解构与边界

### 6.1 一个被解构的笑话

Roberts 一年前曾「开玩笑」预测九年到达 Einstein 级 AI——逻辑是：取 AI 自主工作时间的倍增周期，推算到能自主思考八年（爱因斯坦发现广义相对论所用时间）需要多久。

```plaintext
[~44:00] I hate making predictions, but I'm pretty sure something will break before that. In general, we're not just going to set up a system and let it think autonomously for 8 years, if anything, because the systems 8 years after will be so much more powerful.
```

他自己拆解了这个预测的脆弱性：第一，你不会真的让一个系统思考八年，因为八年后的系统会强大得多，让旧系统慢慢想不如等新系统；第二，系统改进速度与思考时间存在交叉点，交叉之后 scaling walls 会以非预期方式断裂。这是一个研究者在公开表达预测时的标准防御——但也是对「线性外推」思维的否定。

### 6.2 「研究品味」作为最后的壁垒

Roberts 在结尾给出了他对 AI 科学家缺失环节的判断。

```plaintext
[~45:00] there's part of the scientific process that the models haven't been imbued with yet... trying to get to what is the right question as opposed to here's a well-defined thing and go calculate... some of that involves research taste that's not an easily verifiable thing.
```

Erdős 问题是「给一个定义良好的问题去计算」，但真正的物理学研究——Roberts 自己的领域——是「找到正确的问题」。这种「研究品味」不是可验证的 reward，无法通过 string match 判定好坏。这是他留给整场对话的最深层判断：AI 在「解题」上已经跨越了临界点，但在「提问」上还有一段路。而这段路的长度，取决于能否将「研究品味」转化为某种可训练的信号——这恰恰是第四节中可验证奖励边界的回响。

---

## 深度关联

- **RL 的稀疏奖励与信用分配** → [[Karpathy- We're summoning ghosts, not building animals]] | 本文：Roberts 承认 RL 每万 token 不到一比特信息，但反问「你能用其他方式提供更多监督吗」 | 对方：Karpathy 称之为「通过吸管吮吸监督信号」，Sutton 认为稀疏 reward 是 RL 的本质特征 | 关联逻辑：Roberts 没有否认稀疏性诊断，而是将论点转向「唯一管道」——这恰好回应了 Karpathy/Sutton 对信用分配效率的结构性批判，但给出了不同的规范性结论。

- **Scaling 天花板与 RL 作为新维度** → [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]] | 本文：Roberts 提出 pre-training scaling 单独走不远，RL on top of pre-training 是新的 scaling 维度 | 对方：Ilya/Dario 等讨论 pre-training scaling 的渐近极限及后训练突破路径 | 关联逻辑：Roberts 的「蛋糕反转」论为 scaling ceiling 讨论提供了具体机制——不是 pre-training 本身撞墙，而是 RL 开辟了正交的 scaling 方向，test-time compute 是这个方向上的具体载体。

- **验证瓶颈的三层递进** → [[Terence Tao- How the world's top mathematician uses AI]] | 本文：OpenAI 的非形式化路线依赖外部验证，DeepMind 的 Lean 路线内置验证但限制问题范围 | 对方：Tao/Dario 讨论形式化验证与 AI 发现之间的张力 | 关联逻辑：两条路线的对比正是验证瓶颈的具体化——形式化验证确保正确性但牺牲发现范围，非形式化推理扩展发现范围但引入验证成本。Roberts 对「研究品味不可验证」的判断将这一瓶颈推到了第三层：不仅答案需要验证，「问题是否值得问」本身也缺乏验证机制。

- **语言作为先验的认识论立场** → [[Richard Sutton- Father of RL thinks LLMs are a dead end]] | 本文：Roberts 通过酒吧辩论的叙事，论证语言先验是 AI 的正确起点，隐性反驳 Sutton 的纯 RL 立场 | 对方：Sutton 主张 LLM 非真正智能，纯 RL 才是路径 | 关联逻辑：这场分歧的实质不是技术路线选择，而是认识论立场——Roberts 认为人类知识以语言为载体是宝贵先验，Sutton 认为从经验中学习才是智能本质。OpenAI 选择 LLM+RL 的混合路线，正是这两种立场的工程化折中。

---

**元信息**
```plaintext
标题: OpenAI's Dan Roberts: Why AI Can Now Make Discoveries
频道: The MAD Podcast with Matt Turck
发布时间: 2026-06-04
时长: 49min
YouTube链接: https://www.youtube.com/watch?v=oWOz2htozfI
分析时间: 2026-06-26
```
