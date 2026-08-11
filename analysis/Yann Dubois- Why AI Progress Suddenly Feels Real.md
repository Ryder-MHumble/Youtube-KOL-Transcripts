---
title: "Yann Dubois- Why AI Progress Suddenly Feels Real"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=DhD1zZ8w8Mw"
transcript: "[[OpenAI's Yann Dubois Why AI Progress Suddenly Feels Real]]"
tags:
  - kol情报
status: canonical
created: 2026-06-25
---

# OpenAI's Yann Dubois: Why AI Progress Suddenly Feels Real — 深度分析报告

> 当模型从"偶尔惊艳"跨过可靠性阈值的那一刻，进步的体感从渐变变成了跃迁——而这场跃迁的真正赌注，是后训练强化学习从竞赛沙盘走向真实世界的 messy 工作，以及持续学习这个 ChatGPT 三年后仍未解决的难题。
> —— Yann Dubois, OpenAI Post-training Frontiers, 2026

视频链接：https://www.youtube.com/watch?v=DhD1zZ8w8Mw

对应逐字稿：[[OpenAI's Yann Dubois Why AI Progress Suddenly Feels Real]]

**概述**：2026年5月，GPT-5.5 发布数周后，Matt Turck 邀请 OpenAI 后训练前沿团队 co-lead Yann Dubois 做了一场74分钟深度对话。Yann 是 Stanford Alpaca 的合著者——那个开启了现代后训练研究社区的项目。对话覆盖了从可靠性阈值的跨越、强化学习从"竞赛沙盘"到真实世界的迁移、预训练是否撞墙、SFT 与 RL 的本质差异、泛化的边界、评测危机、到持续学习这个三年未解的难题。整场访谈的核心赌注是：AI 进步"突然感觉真实"不是一次能力跃迁，而是可靠性曲线穿过可用阈值的相变——而这场相变正在从编码向所有垂直领域渗透。

## 核心证据校准

> **[2:00]** "the progress is actually pretty continuous"
> **[2:30]** "now we can trust these models to do a lot of the work that we are doing."
> **[3:10]** "these models were still like optimized for uh what what we call verifiable rewards."
> **[3:40]** "we moved from like competitions to usefulness to users"
> **[4:13]** "The longer that they run, the the higher the probability that like the final answer is going to be wrong."
> **[10:11]** "research basically tries to move this curve to the left."
> **[17:51]** "we are able to optimize really like user utility"
> **[18:49]** "the longer the model think for uh the better answers we will get."
> **[26:37]** "it seems like we did not quite hit it."
> **[27:54]** "once we go to embodied agents, embodied AI, you will learn a lot about the world"
> **[29:57]** "we as a field have a tendency of optimizing something that is simulated or not quite realistic"
> **[37:10]** "pre-training, when it's trained on all of the internet, arguably already has all capabilities in it."
> **[41:23]** "you get very little information per token"
> **[42:53]** "the simplest method that where you can scale up in terms of compute usually is the one that ends up working the best."
> **[52:49]** "the world is very messy and these coding competitions and math competitions are extremely well specified."
> **[55:13]** "SFT is going to force like hallucination"
> **[57:23]** "an extremely good model at like explicit explicit instruction following will change the wrong file"
> **[1:00:28]** "Evaluation has been harder and harder as models become better."
> **[1:04:53]** "this will definitely permeate, I think, through many other verticals."
> **[1:07:53]** "3 years later, I don't think we're there yet."
> **[1:12:16]** "most of the time the bottleneck is the the last mile."

**主题脉络**：
1. 可靠性阈值：为何进步"突然"感觉真实
2. 从竞赛到有用：强化学习的第二次生命
3. 预训练没死，但它换了形状
4. SFT 制造幻觉，RL 杀死幻觉——泛化的真实边界
5. 评测的危机与飞轮
6. 持续学习：三年仍未解决，他也不知道为什么

---

## 一、虚假的断崖与真实的阈值

Yann 开场就抛出了一个反直觉的判断：AI 进步的本质是连续的，但体感是阶跃的。原因不在于能力突变，而在于可靠性曲线穿过了"可用"这道门槛。他用 OpenAI 内部的时间线锚定了这个相变点——去年十二月。

```plaintext
[02:19] you need to reach this level of reliability to really make any of these AI tools very useful and I think we just crossed that probably December last year at least at Open AI. Now we can trust these models to do a lot of the work that we are doing.
```

这个判断的产业含义极其明确：在阈值之前，所有 AI 工具的"有用"都是演示性质的；阈值之后，才进入"可信任地替代部分工作"的阶段。Yann 用三个原因解释了为什么最近几个月"感觉特别快"：第一是可靠性阈值被越过（相变体感）；第二是模型自己加速了自己——内部编码工具被模型加速，形成自反馈回路；第三是去年全年积累的推理模型和 RL 技术开始从"可验证奖励"迁移到真实用例。

他给出的可靠性框架值得注意——将 agent 模型的可靠性理解为概率衰减问题：

```plaintext
[04:33] the longer if you just think about it as like every two minutes there's like a certain probability that they're wrong. The longer that they run, the higher the probability that like the final answer is going to be wrong.
```

这意味着 agent 可靠性的核心不是单点准确率，而是**单位时间错误概率的降低**。对任何构建 agent 系统的人来说，这是一个直接的工程指标：你的系统价值不取决于"能不能做对一次"，而取决于"在 N 步 rollout 中累积错误概率是否可控"。

关于 GPT-5.5 本身，Yann 提到两个让他自豪的点：效率（2x faster）和全公司对齐。效率部分揭示了一个重要的技术框架——test-time scaling 曲线：

```plaintext
[10:21] the usual plot that you should be looking at is x-axis the number of tokens that you think for and y-axis the performance... research basically tries to move this curve to the left. So, think less to be the same level or more correct.
```

研究团队把曲线左移（同样性能、更少 token），推理团队把 x 轴从 token 数换成真实延迟，最终落在"延迟-性能"图上。GPT-5.5 的突破在于所有维度同时改善。这里有一个隐含信号：Yann 将效率归功于"整个公司"而非某个团队——这在 OpenAI 内部组织对齐的叙事上很精心，也暗示后训练的效率收益离不开预训练和推理工程的协同。

---

## 二、从竞赛到有用：强化学习的第二次生命

这场访谈的技术核心是一条迁移路径：RL 从"可验证奖励"（数学竞赛、编程比赛）走向"真实世界效用"。Yann 用一句话概括了这条路径：

```plaintext
[04:08] So we moved from like competitions to usefulness to users and that's what we are feeling right now.
```

这条路径的起点是 O1 和 O3——它们证明了"模型可以思考，且思考越久越正确"，但仅在竞赛环境中成立。真正的突破在于：这些为可验证奖励开发的 RL 工具，被成功地迁移到了真实世界任务上。

```plaintext
[17:07] we were able to take these arguments that work with verifiable rewards... to the messy real world and really optimize for the utility that we provide to users and like making them more productive.
```

这里有一个关键的范式判断：Yann 认为"进步突然感觉真实"不是因为模型变聪明了，而是因为优化目标从"竞赛分数"切换到了"用户效用"。SWE-bench 比 Codeforces 更真实，GPD-bench 比数学竞赛更真实。这个切换意味着后训练的奖励函数设计正在从"对/错"的二值判断，进化到"这对用户有多大用"的连续优化。

Yann 还坦诚了一个重要事实——ChatGPT 发布时他不在 OpenAI，而且他最初认为 RL 是"过度复杂的方法"，可以用纯 SFT 复现。Alpaca 项目就是这一直觉的产物。后来他改变了看法：

```plaintext
[40:19] it seems that after crossing a certain scale of models that know basically everything about the world and what we call like good priors about the world, it seems that reinforcement learning just started to work.
```

这是一个重要的范式判断：RL 的有效性依赖于预训练提供的"世界先验"足够强。在模型知识量不足时，RL 是脆弱且低效的；当模型"已经知道一切"时，RL 才开始稳定工作。Yann 还提到机器人领域也在经历同样的转变——从"RL 太 finicky"到"有了好的世界模型基础后 RL 开始 work"。

关于 RL 当前的前沿，Yann 提到开源世界正在收敛到 GRPO，原因是它足够简单、可以规模化：

```plaintext
[42:57] the simplest method that where you can scale up in terms of compute usually is the one that ends up working the best.
```

但他也指出了两个 RL 的结构性难题：基础设施成本（采样大量答案非常昂贵）和**信用分配问题**——在长 agent rollout 中，你只在最后知道对错，无法判断哪一步导致了正确或错误：

```plaintext
[41:23] you only know whether you're correct at the end of your very long roll out. So, you get very little information per token of whether you are correct or not and it's hard to say... which part of your entire answer was the one that led you to being correct.
```

这个信用分配问题是 agent RL 的核心技术瓶颈——它意味着当前 RL 在多步推理任务中的样本效率极低。任何在 agent 系统中做 RL 的人都会撞到这堵墙。

---

## 三、预训练没死，但它换了形状

去年叙事是"预训练撞墙了"。Yann 直接反驳了这一点，但方式值得玩味——他没有说"预训练在算法上突破了"，而是指向了一个更简单的解释：**更大的模型 = 更高效的推理**。

```plaintext
[24:42] if you have larger models, the amount of thinking time, so the amount of tokens they will think for, will usually decrease. And the way that you can think about it is that metaphorically, the model already thinks through its weights when it generates a certain token.
```

这是一个重要的技术洞察：预训练的规模和后训练的推理效率不是独立的——更大的模型在权重中"压缩"了更多推理，因此生成时需要更少的思考 token。而且大模型在推理时可以更好地并行化，抵消了单 token 成本的增加。这意味着"预训练撞墙"的叙事和"推理效率飞跃"其实是同一个硬币的两面。

关于数据墙，Yann 的判断也很直接：

```plaintext
[26:48] it seems like we did not quite hit it. So, the larger the model is, the more data it needs to ingest to be trained. And it seems like different companies kind of found different ways to overcome the fact that we don't have that much data on the internet.
```

他没有透露 OpenAI 的做法，但点出了两个方向：合成数据（"在数据受限时可能有用"）和多模态数据。不过他对多模态的态度很微妙——他认为多模态对推理"应该有帮助"，但 Anthropic 的模型"多模态不太好但仍然很聪明"，说明它"没有我过去认为的那么必要"。唯一他坚持需要多模态/具身的场景是"常识"和"理解物理世界"：

```plaintext
[29:01] they kind of understand gravity without having seen that but it still seems not obvious... they are still kind of missing some common sense aspects.
```

关于世界模型，他给出了一个克制的警告——整个领域有过度优化模拟环境的倾向：

```plaintext
[30:29] we as a field have a tendency of optimizing something that is simulated or not quite realistic past the point where this is useful.
```

这个判断对任何做仿真训练、合成环境的团队都是一个直接的提醒：仿真在早期有用，但过度优化会偏离真实世界的分布。Yann 认为最终始终需要真实世界的训练来弥合"模拟-现实"差距。

在 mid-training 部分，Yann 给出了一个清晰的定义：mid-training 是在预训练（学习互联网的一切）和后训练（让模型对用户有用）之间，对高质量数据（Wikipedia、GitHub 等）进行过度训练的阶段。这个阶段在开源社区已经是标准做法。

---

## 四、SFT 制造幻觉，RL 杀死幻觉——泛化的真实边界

这是整场访谈中认知密度最高的部分。Yann 引用 John Schulman 的分析，给出了一个反直觉的判断：**SFT 是幻觉的来源，RL 是解药**。

逻辑链条是这样的：SFT（行为克隆）要求模型模仿人类给出的"金标准答案"。当模型不知道某篇论文是否存在时，如果金标准答案是"引用这篇论文"，你实际上在训练模型**编造不存在的引用**：

```plaintext
[54:58] if the model doesn't know about a paper, and now in an answer that you give that is given by a ground truth answer given by a human, you say here's where I got the information and then you cite that paper. Like what you're actually optimizing the model to do is citing something that doesn't exist because it doesn't know that that paper exists.
```

而 RL 天然避免这个问题——因为 RL 需要模型自己采样答案，如果模型不知道某件事，它几乎不可能"碰巧"采样到正确的引用，因此不会被奖励"编造"的行为：

```plaintext
[55:35] extremely likely that it samples something that it doesn't know and it's correct. That's like extremely unlikely. So, you will never reward that behavior.
```

这个判断的隐含立场非常强：**SFT 是有上限的——你永远无法超越人类标注者的水平**。而 RL 的核心价值在于它可以超越人类基线，因为它优化的不是"模仿正确答案"，而是"最大化奖励信号"。

但 Yann 也划清了泛化的边界。他指出两种泛化：算法泛化和能力泛化。算法泛化很好——GRPO 可以从一个领域迁移到另一个领域。能力泛化在"同类技能"内也有效（数学竞赛 → 编程竞赛），但**不会跨技能类别迁移**：

```plaintext
[52:27] if my model is very intelligent in terms of being correct on like competitions... but that is really not true. Because many things where we need to have humans working on like expert domains, like the world is very messy and these coding competitions and math competitions are extremely well specified.
```

竞赛任务和真实世界任务之间有一道结构性鸿沟：竞赛任务信息完备（所有信息在 prompt 里），真实世界任务需要先**搜索、提取、理解**信息，然后才能推理。这种"处理 messy 输入"的能力是一种横向能力，不会从竞赛训练中自然获得。

关于负迁移，Yann 给了一个非常具体的例子——**显式指令遵循 vs 隐式指令遵循**：

```plaintext
[57:33] if I make a typo and I say like change this file and I make a typo in this file... an extremely good model at like explicit instruction following will change the wrong file, the one that has a typo. But like humans would probably realize that you made a typo.
```

这是一个信号：OpenAI 模型在"精确执行指令"上很强，但这种强度可能以"理解用户意图"为代价。横向能力之间存在张力。

---

## 五、评测的危机与飞轮

Yann 对评测的态度出人意料地直率——他把 evals 称为"没有人愿意做但影响最大的事情"，并把它和自己在 OpenAI 的第一个项目联系起来：

```plaintext
[62:32] my first project at OpenAI I just came in and I was like I want to work on data and evals cuz I know that this is the thing that no one is working on. And as a result I know that's like super impactful to work on that.
```

他指出了评测变难的三个结构性原因：任务越来越开放（"建一个网站" vs "找到 bug"）、模型在特定轴上超越了大多数人类（能评测的人越来越少）、以及文化问题——人们更想训练模型而不是评测模型。

关于模型作为裁判（model-as-judge），Yann 认为这是最重要的方向之一，因为它形成了一个自我强化的飞轮：

```plaintext
[64:00] we have this capability flywheel where better models become better teachers for other models. And this is really important for training, but then you can also do the same thing for evaluation.
```

但他也指出了一个悖论：每次你构建一个 eval，你实际上也在构建一个训练数据集——因为 RL 的算法泛化意味着模型会在同类数据上快速变好，你的 eval 很快就会过时。这形成了一个军备竞赛：评测必须不断进化，否则就会被训练数据追上。

---

## 六、持续学习：三年仍未解决，他也不知道为什么

访谈的最后部分聚焦在两个问题上：持续学习和"模型吃掉 harness"的争论。Yann 对持续学习的态度出人意料地坦诚——他承认这是一个未解决的问题，而且他"不知道为什么这么久还没解决"。

他给出了一个极其清晰的框架来理解这个问题——**效用曲线**：

```plaintext
[66:34] most models at day zero, if you just drop them in a company, arguably, they're more useful than most new employees. So, they start higher at T0, but then across time, they're mostly constant because they don't really learn kind of company knowledge... while humans learn really quickly.
```

关键不是 T0 的起点，而是曲线下的面积。模型起点高但平坦，人类起点低但陡升——在足够长的时间窗口内，人类仍然更优。这就是持续学习的赌注：让模型曲线从平坦变为单调递增。

Yann 坦承三年前他做创业时就预期 OpenAI 会解决持续学习，但至今未解决：

```plaintext
[67:50] Three years ago when ChatGPT came out, I remember I was doing a startup with friends. And we were thinking about working on continual learning and like personalization and like memories in general. We were like, "Ah, OpenAI is going to do that in the next 6 months." And 3 years later, I don't think we're there yet.
```

被追问"根本困难是什么"时，他直接说"我不知道"：

```plaintext
[68:08] I actually don't quite know, to be completely honest with you. I don't quite know why it's taking us that long to figure it out.
```

这是一个来自 OpenAI 后训练负责人的重大信号：持续学习不是一个"我们知道怎么解决但还没来得及做"的问题，而是一个"我们甚至不确定为什么它这么难"的问题。对于创业者和投资者来说，这意味着持续学习/个性化/企业知识嵌入仍然是一个开放赛道——不是被 OpenAI 内部垄断的方向。

关于"模型吃掉 harness"的争论，Yann 给出了一个微妙的立场：harness 在短期内、针对特定垂直领域有价值（从80%到85%的可靠性），但长期不可持续。他的核心论点是——**如果今天冻结模型，只优化 harness，人们就会在每个领域感受到 AGI**：

```plaintext
[71:04] I think if we froze the models that we have right now and you really worked on the harness... I think people would really feel the AGI in every single domain.
```

但模型没有被冻结，所以 harness 的最终形态还不确定，而且会不断变化。这对 harness/agent 框架创业公司是一个直接信号：你的价值在短期内是真实的，但你的护城河需要假设模型能力会持续提升来重新定义。

Yann 最后给创业生态的信息很明确：**瓶颈不是原始智能，而是最后一英里**——权限、连接器、垂直领域适配。OpenAI 会专注于横向进步，垂直领域的 last mile 留给了外部生态：

```plaintext
[72:34] I think most of the time the bottleneck is the last mile. It's like making sure that the model has access to like the right permissions or like has access to like the right connectors.
```

---

## 深度关联

### ← [[Karpathy- We're summoning ghosts, not building animals]]
**本文件论点**：Yann 明确指出信用分配是 agent RL 的结构性瓶颈——在长 rollout 中只在最后知道对错，无法判断哪一步导致正确或错误 [41:23]
**对方论点**：Karpathy 诊断 RL 用"吸管嘬监督信号"——一分钟轨迹只得到一个标量，走错的步骤如果答案对了也被强化
**关联逻辑**：补充。Karpathy 从外部诊断了信用分配稀疏性的症状，Yann 从 OpenAI 内部确认了它是当前 agent RL 的核心技术瓶颈。两人从不同位置指向同一堵墙——Yann 的"我们不知道哪一步导致正确"就是 Karpathy "吸管嘬监督信号"的工程语言翻译。

### → [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]
**本文件论点**：Yann 反驳"预训练撞墙"叙事，但方式是指向"更大模型=更高效推理"——预训练换了形状而非死亡 [24:42]
**对方论点**：Ilya 论证"Scaling"这个词塑造了5年集体思维方向，但现在从 Scaling 时代回到 Research 时代
**关联逻辑**：张力。Ilya 认为 Scaling 作为唯一范式的时代已结束，需要回到研究创新；Yann 认为预训练 scaling 仍在产出收益（只是换了形态——从直接能力提升变为推理效率提升）。两人对"scaling 是否撞墙"给出了不同但非互斥的判断：Ilya 说范式需要多元化，Yann 说旧范式还有余热只是变形了。

### ← [[Dario Amodei- 我们正处于指数的尽头]]
**本文件论点**：Yann 认为 RL 正在从可验证域（竞赛）迁移到不可验证域（真实世界效用），且这条迁移路径已经开始 work [17:07]
**对方论点**：Dario 划分了可验证域（编程，1-2年到达）和不可验证域（规划/发现/写作，时间线不确定）的时间线差异
**关联逻辑**：补充/具体化。Dario 从外部给出了时间线预测，Yann 从内部给出了这条迁移路径的技术机制——RL 优化目标从"竞赛分数"切换到"用户效用"。Yann 的"GPT-5.5 就是这条路径的第一个产物"是对 Dario "RL scaling 正在重演 pre-training 轨迹"的阶段性验证。

### ← [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]]
**本文件论点**：Yann 坦承持续学习是 ChatGPT 三年后仍未解决的问题，且"不知道为什么这么难"——这是对创业生态的开放信号 [67:50]
**对方论点**：Levie 论证企业 AI 的真正瓶颈在"桥层"——数据、权限、预算、人才、工作流改造，而非模型能力
**关联逻辑**：镜像。Yann 从模型层确认了"持续学习未解决"（模型不会自动获得企业知识），Levie 从企业层确认了"桥层"岗位（internal FDE）因此必然兴起。两人从不同方向指向同一结论：模型→企业的知识传递仍然需要人工桥梁，这个缺口是创业机会而非技术失败。

---

**元信息**

| 字段 | 值 |
|------|-----|
| 标题 | OpenAI's Yann Dubois: Why AI Progress Suddenly Feels Real |
| 频道 | The MAD Podcast with Matt Turck |
| 发布日期 | 2026-05-21 |
| 时长 | 74min |
| YouTube链接 | https://www.youtube.com/watch?v=DhD1zZ8w8Mw |
| 分析时间 | 2026-06-25 |
