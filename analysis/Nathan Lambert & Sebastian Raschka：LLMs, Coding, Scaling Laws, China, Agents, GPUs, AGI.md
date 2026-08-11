---
title: Lex Fridman - Nathan Lambert & Sebastian Raschka：LLMs, Coding, Scaling Laws, China, Agents, GPUs, AGI
source: youtube
youtube_url: https://www.youtube.com/watch?v=EV7WhVT270Q
transcript: '[[Lex Fridman - State of AI in 2026 LLMs, Coding, Scaling Laws, China, Agents, GPUs, AGI 逐字稿]]'
tags:
- kol情报
status: canonical
---

> 2026 年 AI 竞争已无法用单一模型榜单解释：真正的差异来自后训练、工具使用、推理成本、开源扩散和组织执行速度的组合。

视频链接：https://www.youtube.com/watch?v=EV7WhVT270Q

对应逐字稿：[[Lex Fridman - State of AI in 2026 LLMs, Coding, Scaling Laws, China, Agents, GPUs, AGI 逐字稿]]

## 访谈定位

两位研究者把模型竞争拆成美国与中国、闭源与开源、预训练与后训练、编码与机器人、能力与商业化等多条轴线。其价值在于纠正“某个模型赢了就代表路线终局”的媒体叙事。

这篇分析不按节目目录逐段复述，而是围绕决定性张力重组材料。下列判断均以对应逐字稿的完整时间戳段落为证据。

## 主题脉络

| 主题 | 对应章节 | 关键判断 |
| --- | --- | --- |
| 国家竞争比榜单更像产业系统竞争 | China vs US: Who wins the AI race? | 模型分数只是结果层，中国的工程人才、开源发布与成本压力，美国的资本、芯片与前沿实验室，共同决定追赶和扩散速度。 |
| Coding 是 agent 的首个高密度验证场 | Best AI for coding | 代码具备可执行反馈、真实工具链和明确失败信号，因此最早把模型从对话推向长任务；它是 agent 工程的试验场，不是全部未来。 |
| 开源的战略价值是压缩能力扩散时差 | Open Source vs Closed Source LLMs | 开放权重未必长期领先前沿能力，却能让研究、部署和本地优化迅速复制，从而改变闭源厂商的定价与生态控制。 |
| Scaling 从一条曲线变成三段流水线 | How AI is trained: Pre-training, Mid-training, and Post-training | 能力提升不再只靠更大预训练；领域中训练、强化学习、合成数据与推理预算共同决定产品可用性。 |
| 长上下文不等于持续学习 | Continual learning | 能把更多内容塞进窗口不代表模型形成稳定记忆或更新能力；产品必须区分临时检索、用户记忆和模型参数更新。 |
| AGI 叙事降温不等于商业机会收缩 | Is the dream of AGI dying? | 即使通用智能时间线后移，编码、研究、客服和工作流中的局部能力仍可创造巨大价值；商业判断不应押注单一终局。 |

## 核心证据校准

> **[2:32]** "Lex Fridman: Let’s discuss all of this today, and maybe let’s start with some spicy questions if we can. Who’s winning at the international level? Would you say it’s the set of companies in China or the set of companies in the United States? Sebastian, Nathan, it’s good to see you guys. So Sebastian, who do you think is winning?"

> **[24:27]** "Sebastian Raschka: Honestly, building an LLM from scratch is a lot of fun and a lot to learn. Like you said, it’s probably the best way to learn how something really works, because you can look at figures, but figures can have mistakes. You can look at conceptual explanations, but you might misunderstand them. But if there is code and the code works, you know it’s correct. There’s no misunderstanding; it’s precise. Otherwise, it wouldn’t work. I think that’s the beauty behind coding. It doesn’t lie. It’s math, basically. Even with math, you can have mistakes in a book you would never notice because you aren’t running the math while reading, so you can’t verify it. And with code, what’s nice is you can verify it."

> **[34:13]** "Nathan Lambert: If you’re releasing an open model, you want people to use it, is the first and foremost thing. And then after that comes things like transparency and trust. I think when you look at China, the biggest reason is that they want people around the world to use these models, and I think a lot of people will not. If you look outside of the US, a lot of people will not pay for software, but they might have computing resources where you can put a model on it and run it. I think there can also be data that you don’t want to send to the cloud. So the number one thing is getting people to use models, use AI, or use your AI that might not be able to do it without having access to the model."

> **[1:05:33]** "Sebastian Raschka: And I think that’s the idea. I think it’s like if someone took that and rephrases it in a, let’s say, more concise and structured way— I think it’s higher quality data that gets the LLM maybe the same—you get the same LLM out of it at the end, but it gets there faster. It trains faster because if the grammar and the punctuation are correct, it already learns the correct way versus getting information from a messy way and then learning later how to correct that. So, I think that is how pre-training evolved and why scaling still works; it’s not just about the amount of data, it’s also the tricks to make that data better for you. And then mid-training is… I mean, it used to be called pre-training."

> **[2:41:24]** "Sebastian Raschka: I think, to be honest with you, continual learning—the updating of weights—we already have that in different flavors. I think the distinction here is: do you do that on a personalized custom model for each person, or do you do it on a global model scale? And I think we have that already with going from GPT-5 to 5.1 and 5.2. It’s maybe not immediate, but it is like a quick curated update where there was feedback by the community on things they couldn’t do. They updated the weights, released the next model, and so forth. So it is kind of a flavor of that. Another even finer-grained example is RLVR; you run it, it updates."

> **[3:26:52]** "Nathan Lambert: Yeah. I guess my statement with the dream is dying depends on exactly what you think it’s going to be doing. Like Claude Code is a general model that can do a lot of things, but it depends a lot on integrations and other things. I bet Claude Code could do a fairly good job of doing your email, and the hardest part is figuring out how to give it information and how to get it to be able to send your emails and stuff like this. But I think it goes back to what is the “one model to rule everything” ethos, which is just like a thing in the cloud that handles your entire digital life and is way smarter than everybody."

### 主线之外的补充证据

**Transformers: Evolution of LLMs since 2019**

> **[43:25]** "Sebastian Raschka: Picture like the Mixture of Experts. The attention mechanism in gpt-oss-120b, that would be the Group Query Attention mechanism. So it’s a slight tweak from multi-head attention to Group Query Attention, so that we have two. I think they replaced LayerNorm by RMSNorm, but it’s just like a different normalization there and not a big change. It’s just like a tweak. The nonlinear activation function—for people familiar with deep neural networks, I mean, it’s the same as changing sigmoid with ReLU. It’s not changing the network fundamentally. It’s just like a tweak. And that’s about it, I would say. It’s not really fundamentally that different. It’s still the same architecture. So you can convert one from one… You can go from one into the other by just adding these changes, basically."

**Advice for beginners on how to get into AI development & research**

> **[2:09:13]** "Nathan Lambert: When you’re collecting the data, they all get compressed into, “I like this more than another.” There’s a lot of research in other areas of the world that goes into how you should actually do this. I think social choice theory is the subfield of economics around how you should aggregate preferences. I went to a workshop that published a white paper on how you can think about using social choice theory for RLHF. I want people who get excited about the math to stumble into this broader context. I also keep a list of all the tech reports of reasoning models that I like. In Chapter 14, where there’s a short summary of RLVR, there’s a gigantic table where I list every single reasoning model that I like. I think in education, a lot of it needs to be, at this point, what I like—"

# 1、国家竞争比榜单更像产业系统竞争

模型分数只是结果层，中国的工程人才、开源发布与成本压力，美国的资本、芯片与前沿实验室，共同决定追赶和扩散速度。

在逐字稿的 **China vs US: Who wins the AI race?** 章节，Lex Fridman 于 **2:32** 给出了这一判断的直接材料。这里不能只把它当作个人经历或技术细节：它揭示的是决定结果的约束从哪里转移，以及旧的评价方式为何会失效。

**情报含义**：如果把“国家竞争比榜单更像产业系统竞争”作为决策框架，下一步不是复制嘉宾的具体做法，而是检查自己的产品、组织或内容是否仍在优化已经不再稀缺的变量。

# 2、Coding 是 agent 的首个高密度验证场

代码具备可执行反馈、真实工具链和明确失败信号，因此最早把模型从对话推向长任务；它是 agent 工程的试验场，不是全部未来。

在逐字稿的 **Best AI for coding** 章节，Sebastian Raschka 于 **24:27** 给出了这一判断的直接材料。这里不能只把它当作个人经历或技术细节：它揭示的是决定结果的约束从哪里转移，以及旧的评价方式为何会失效。

**情报含义**：如果把“Coding 是 agent 的首个高密度验证场”作为决策框架，下一步不是复制嘉宾的具体做法，而是检查自己的产品、组织或内容是否仍在优化已经不再稀缺的变量。

# 3、开源的战略价值是压缩能力扩散时差

开放权重未必长期领先前沿能力，却能让研究、部署和本地优化迅速复制，从而改变闭源厂商的定价与生态控制。

在逐字稿的 **Open Source vs Closed Source LLMs** 章节，Nathan Lambert 于 **34:13** 给出了这一判断的直接材料。这里不能只把它当作个人经历或技术细节：它揭示的是决定结果的约束从哪里转移，以及旧的评价方式为何会失效。

**情报含义**：如果把“开源的战略价值是压缩能力扩散时差”作为决策框架，下一步不是复制嘉宾的具体做法，而是检查自己的产品、组织或内容是否仍在优化已经不再稀缺的变量。

# 4、Scaling 从一条曲线变成三段流水线

能力提升不再只靠更大预训练；领域中训练、强化学习、合成数据与推理预算共同决定产品可用性。

在逐字稿的 **How AI is trained: Pre-training, Mid-training, and Post-training** 章节，Sebastian Raschka 于 **1:05:33** 给出了这一判断的直接材料。这里不能只把它当作个人经历或技术细节：它揭示的是决定结果的约束从哪里转移，以及旧的评价方式为何会失效。

**情报含义**：如果把“Scaling 从一条曲线变成三段流水线”作为决策框架，下一步不是复制嘉宾的具体做法，而是检查自己的产品、组织或内容是否仍在优化已经不再稀缺的变量。

# 5、长上下文不等于持续学习

能把更多内容塞进窗口不代表模型形成稳定记忆或更新能力；产品必须区分临时检索、用户记忆和模型参数更新。

在逐字稿的 **Continual learning** 章节，Sebastian Raschka 于 **2:41:24** 给出了这一判断的直接材料。这里不能只把它当作个人经历或技术细节：它揭示的是决定结果的约束从哪里转移，以及旧的评价方式为何会失效。

**情报含义**：如果把“长上下文不等于持续学习”作为决策框架，下一步不是复制嘉宾的具体做法，而是检查自己的产品、组织或内容是否仍在优化已经不再稀缺的变量。

# 6、AGI 叙事降温不等于商业机会收缩

即使通用智能时间线后移，编码、研究、客服和工作流中的局部能力仍可创造巨大价值；商业判断不应押注单一终局。

在逐字稿的 **Is the dream of AGI dying?** 章节，Nathan Lambert 于 **3:26:52** 给出了这一判断的直接材料。这里不能只把它当作个人经历或技术细节：它揭示的是决定结果的约束从哪里转移，以及旧的评价方式为何会失效。

**情报含义**：如果把“AGI 叙事降温不等于商业机会收缩”作为决策框架，下一步不是复制嘉宾的具体做法，而是检查自己的产品、组织或内容是否仍在优化已经不再稀缺的变量。

## 矛盾、边界与未说出口的部分

- 圆桌判断覆盖面广，但许多预测尚未经过时间检验。
- 编码领域的成功容易让人高估其他领域的可验证性和自动化速度。
- 国家竞争框架可能遮蔽跨国人才、供应链与开源社区的相互依赖。

这些边界很重要，因为访谈是高密度的一手观点来源，但不是经过对抗性验证的研究报告。嘉宾的身份、利益位置和叙事习惯本身也是证据的一部分。

## 对个人 IP / 产品情报的可行动启发

- 建立多维模型评估：质量、延迟、成本、工具成功率、可部署性与供应商风险。
- 把长期任务拆成可验证阶段，为每段提供环境反馈。
- 开源与闭源采用组合策略，按数据敏感度和能力差距分配任务。

## 可延展选题

- **国家竞争比榜单更像产业系统竞争**：以“模型分数只是结果层，中国的工程人才、开源发布与成本压力，美国的资本、芯片与前沿实验室，共同决定追赶和扩散速度。”为主论点，补充一个反例和一项可执行检查表，形成可独立发布的文章。
- **Coding 是 agent 的首个高密度验证场**：以“代码具备可执行反馈、真实工具链和明确失败信号，因此最早把模型从对话推向长任务；它是 agent 工程的试验场，不是全部未来。”为主论点，补充一个反例和一项可执行检查表，形成可独立发布的文章。
- **开源的战略价值是压缩能力扩散时差**：以“开放权重未必长期领先前沿能力，却能让研究、部署和本地优化迅速复制，从而改变闭源厂商的定价与生态控制。”为主论点，补充一个反例和一项可执行检查表，形成可独立发布的文章。
- **Scaling 从一条曲线变成三段流水线**：以“能力提升不再只靠更大预训练；领域中训练、强化学习、合成数据与推理预算共同决定产品可用性。”为主论点，补充一个反例和一项可执行检查表，形成可独立发布的文章。
- **长上下文不等于持续学习**：以“能把更多内容塞进窗口不代表模型形成稳定记忆或更新能力；产品必须区分临时检索、用户记忆和模型参数更新。”为主论点，补充一个反例和一项可执行检查表，形成可独立发布的文章。
- **AGI 叙事降温不等于商业机会收缩**：以“即使通用智能时间线后移，编码、研究、客服和工作流中的局部能力仍可创造巨大价值；商业判断不应押注单一终局。”为主论点，补充一个反例和一项可执行检查表，形成可独立发布的文章。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 机制互证——补充当前访谈的核心判断

**← [[Dario Amodei- 我们正处于指数的尽头]]**
- 本文件论点：中美 AI 竞争不是单一模型榜单，而是人才、算力、开源生态和应用速度的复合竞争。
- 对方论点：Dario 把前沿 AI 描述为指数曲线临近现实约束的阶段，强调能力、部署和社会影响会在短时间内叠加。
- 关联逻辑：当前材料把判断落在“中美 AI 竞争不是单一模型榜单，而是人才、算力、开源生态和应用速度的复合竞争。”；对方则从另一层说明“Dario 把前沿 AI 描述为指数曲线临近现实约束的阶段，强调能力、部署和社会影响会在短时间内叠加。”。两者互为机制证据：前者指出需要改变的决策对象，后者补上该变化成立的条件或代价。因此，不能把任一论点孤立地升级为趋势，必须同时检查两套机制是否在目标场景出现。

### 边界修正——重构当前访谈的核心判断

**→ [[Karpathy- Skill Issue — Code Agents, AutoResearch, and the Loopy Era]]**
- 本文件论点：编码能力是最早被真实工作流验证的 AI 能力，因此比聊天能力更能说明 agent 化进度。
- 对方论点：Karpathy 将代码 agent 的瓶颈从生成能力转向任务分解、验证回路和人机协作习惯。
- 关联逻辑：当前材料把判断落在“编码能力是最早被真实工作流验证的 AI 能力，因此比聊天能力更能说明 agent 化进度。”；对方则从另一层说明“Karpathy 将代码 agent 的瓶颈从生成能力转向任务分解、验证回路和人机协作习惯。”。两者构成边界修正：前者指出需要改变的决策对象，后者补上该变化成立的条件或代价。因此，不能把任一论点孤立地升级为趋势，必须同时检查两套机制是否在目标场景出现。

### 行动映射——约束当前访谈的核心判断

**→ [[Chamath Palihapitiya- AI Doom Narratives and the Economic Leveler]]**
- 本文件论点：开源/闭源不是意识形态问题，而是扩散速度、可控性、商业捕获之间的结构性取舍。
- 对方论点：Chamath 把 AI 叙事看作资本、开放生态和身份化准入之间的博弈，而不只是技术风险争论。
- 关联逻辑：当前材料把判断落在“开源/闭源不是意识形态问题，而是扩散速度、可控性、商业捕获之间的结构性取舍。”；对方则从另一层说明“Chamath 把 AI 叙事看作资本、开放生态和身份化准入之间的博弈，而不只是技术风险争论。”。两者形成行动约束：前者指出需要改变的决策对象，后者补上该变化成立的条件或代价。因此，不能把任一论点孤立地升级为趋势，必须同时检查两套机制是否在目标场景出现。

## 元信息

- 访谈发布日期：2026-01-31
- 逐字稿来源：https://lexfridman.com/ai-sota-2026-transcript/
- 分析状态：canonical（基于完整逐字稿重构）
