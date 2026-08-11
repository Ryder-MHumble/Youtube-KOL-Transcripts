---
title: "Alfred Wahlforss- AI原生的市场研究"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=Rumft-rsEu4"
transcript: "[[Knowing What Your Customers Want, All the Time Listen Labs' Alfred Wahlforss]]"
feishu_doc_id: E5bHdY1XLoYBAwxZ4XNcuoK6nqf
tags:
  - kol情报
created: 2026-06-08
order: 31
status: canonical
---

> Alfred Wahlforss 的核心判断是：当 AI 让 execution 变得越来越便宜，真正稀缺的不是“怎么 build”，而是持续、低摩擦、可验证地知道“what to build”；Listen Labs 要把用户偏好做成 agent 可以调用的 human API。

视频链接：https://www.youtube.com/watch?v=Rumft-rsEu4

对应逐字稿：[[Knowing What Your Customers Want, All the Time Listen Labs' Alfred Wahlforss]]

## 核心证据校准

> **[1:25]** "we have this AI agent that can understand your customers better than you can."

> **[1:48]** "as we get closer to AGI, it will be easier to build things, but the hard part will know what to build."

> **[4:05]** "they were like radically inconsistent."

> **[4:26]** "when you have actually have to think, and you have to really reason through your answer, and then you're much more consistent"

> **[5:31]** "it's essentially a Zoom call that you have with the agent."

> **[6:58]** "for every data point you can always click and then look at the video or see the quote."

> **[9:50]** "most decisions that that gets made are not based on the customer input."

> **[10:14]** "you can get input within 5 minutes from real people"

> **[11:01]** "people are more honest talking to an AI."

> **[11:01]** "It's a very therapeutic experience because it's a non-judgmental entity that's really interested in you"

> **[11:54]** "the audience is extremely important."

> **[11:54]** "that's actually where we spend 80% of our engineering resources."

> **[12:23]** "that's 80% of the revenue."

> **[13:16]** "we build profiles of people as we do more interviews in the platform and then we can search and find the right person."

> **[18:35]** "you'll be doing kind of two orders magnitude more of research."

> **[18:35]** "unlock the 99% of use cases where you would never have time to talk to real people."

> **[19:40]** "telling another agent to go and solve that problem."

> **[21:12]** "in some cases we're able to get 95% accuracy to predict how they will answer certain questions."

> **[22:57]** "the models are trained on the average person."

> **[24:07]** "what we found was the best data set is interviews"

> **[26:15]** "almost an human API where the agents are able to call the preferences of your users."

> **[29:16]** "that eval was like 20%. Now, we've been able to climb that eval to be 85%."

> **[29:38]** "they have this proprietary eval that they can use and essentially climb that climb that eval."

> **[30:12]** "a company is figure out what to build, build it, figure out what to build, build it."

> **[30:24]** "the build it is coming up rapidly up in exponential."

> **[30:59]** "we'll have a coding agent and listen and then run that in the loop."

> **[34:04]** "in the future you'll still need to have human input"

> **[35:14]** "what is in a human's mind that isn't in the AI's mind, only becomes more important."

> **[35:59]** "as we do more interviews, you gets better simulation."

> **[36:27]** "customers want something that's stupid simple."

## 概述

Alfred Wahlforss 这场 Sequoia Training Data 访谈讲的是 Listen Labs，但更重要的是它把一个应用层判断说透了：AI 正在把“构建”压缩成越来越便宜、越来越快的动作，企业真正缺的会变成稳定知道该构建什么。Listen Labs 的产品形态是 AI 原生用户访谈，战略形态则是把用户偏好变成 agent 可以调用的需求层基础设施。

> **[1:48]** "as we get closer to AGI, it will be easier to build things, but the hard part will know what to build."

这句话是整场访谈的主轴。过去市场研究是慢服务、问卷、焦点小组和咨询报告；Alfred 的赌注是，当 AI 访谈可以同时和成千上万人对话，用户研究会从低频项目变成产品循环中的实时输入。

## 问卷的问题不是慢，而是让人不思考

Alfred 对传统问卷的批判不是“体验差”这么简单，而是数据质量本身有问题。他们做过 repeat test：同一个人再次回答同一份多选问卷，会高度不一致。

> **[4:05]** "they were like radically inconsistent."

原因在于问卷把复杂偏好压缩成选项，用户不用真的推理自己的答案。Listen 的对话式访谈强迫受访者解释、反思、补充上下文，因此回答更稳定。

> **[4:26]** "when you have actually have to think, and you have to really reason through your answer, and then you're much more consistent"

这不是“AI 替代问卷工具”，而是从选择题式偏好采样转向推理过程采样。对产品经理来说，关键价值不只是知道用户选了 A 还是 B，而是知道他为什么选、在哪个场景下选、哪些语气和表情暴露了真实强度。

> **[5:31]** "it's essentially a Zoom call that you have with the agent."

这也解释了为什么 Listen 强调 traceability：

> **[6:58]** "for every data point you can always click and then look at the video or see the quote."

AI 总结本身不够，必须能回到原始视频和 quote，否则市场研究会从“人类主观偏差”滑向“模型幻觉偏差”。Listen 的可信度来自可追溯证据链，而不是漂亮的洞察卡片。

## AI 访谈的反直觉优势：人可能对 AI 更诚实

访谈中最有信号的发现，是人们面对 AI 可能比面对真人更坦诚。

> **[11:01]** "people are more honest talking to an AI."

Alfred 的解释不是“AI 更懂人”，而是 AI 更低压、更异步、更不评判。

> **[11:01]** "It's a very therapeutic experience because it's a non-judgmental entity that's really interested in you"

这对用户研究是一个结构性变化。传统访谈的最大成本之一，不只是招募和分析，而是受访者在真人面前会自我修饰。AI 作为非评判性倾听者，反而可能获得更真实的信息。这个洞察的外延很大：客服、医疗、教育、心理支持、员工反馈、儿童研究等场景里，“愿不愿意说真话”可能比模型理解能力更关键。

但这也意味着 AI 访谈公司会掌握非常高敏感度的心理和偏好数据。Listen 的护城河越强，隐私、同意、数据治理和用途边界就越重要。

## 找对人比问对问题更难

Alfred 说 Listen 把 80% 工程资源花在 audience 上，而不是访谈 agent 本身。

> **[11:54]** "that's actually where we spend 80% of our engineering resources."

这句话很重要，因为它反驳了“AI 访谈工具就是一个 voice agent”的浅层理解。真正决定洞察质量的是找对受访者。Sweetgreen 看似大众消费品，但真正的高价值用户可能是城市、高收入、女性、懂 seed oils 的小众人群。

> **[11:54]** "the audience is extremely important."

> **[12:23]** "that's 80% of the revenue."

这里出现的是幂律用户研究：不是平均用户定义产品，而是高价值 segment 定义机会。Listen 的数据网络效应也在这里形成：

> **[13:16]** "we build profiles of people as we do more interviews in the platform and then we can search and find the right person."

每一次访谈都不只是完成一次项目，而是在构建一个可检索的人群知识图谱。某人在无关访谈里透露自己是 sneakerhead，下次 Nike 要找早期 adopters，这条信息就变成供给侧资产。

## Simulation 的价值不是替代真人，而是打开原本不值得访谈的问题

Alfred 对 simulation 的说法很克制。他不是说“以后不用真人”，而是说真人访谈会支撑对具体用户或细分人群的偏好模拟。

> **[21:12]** "in some cases we're able to get 95% accuracy to predict how they will answer certain questions."

真正重要的是使用场景分层。大型决策仍需要真实访谈，小型决策可以用 simulation 快速跑。

> **[18:35]** "unlock the 99% of use cases where you would never have time to talk to real people."

这解释了市场扩张逻辑：单次访谈价格可能下降，但研究总量会上升两个数量级。

> **[18:35]** "you'll be doing kind of two orders magnitude more of research."

Simulation 的上限不取决于通用模型，而取决于专有访谈数据。Alfred 对 ChatGPT 的比较很直接：通用模型训练的是平均人，而产品决策关心的是具体 niche。

> **[22:57]** "the models are trained on the average person."

他们试过信用卡数据、购买行为数据，最后发现最好的数据仍然是访谈，因为访谈能追问、跑偏、问行为问题，捕捉思考方式。

> **[24:07]** "what we found was the best data set is interviews"

这对 AI 产品很有启发：行为数据告诉你发生了什么，访谈数据解释为什么发生；simulation 如果只吃行为数据，会缺少用户心理模型。

## 垂直 AI 的护城河是 proprietary eval

Alfred 对 vertical AI moat 的解释非常清楚。Listen 一开始只是让 AI 生成 interview guide，但客户拿回来的数据不可用。后来他们围绕“是否重复提问、是否遵循指令、是否不引导证人、是否能根据上下文跳过问题”建立 eval，模型表现从 20% 爬到 85%。

> **[29:16]** "that eval was like 20%. Now, we've been able to climb that eval to be 85%."

然后他们又把 eval 升级到更难的问题，例如理解 screen recording 和跳过无关问题，分数又回到 20%。这就是垂直 AI 公司持续复利的方式：

> **[29:38]** "they have this proprietary eval that they can use and essentially climb that climb that eval."

这与“通用模型越来越强，应用层没护城河”的观点相反。应用层护城河不在模型参数，而在任务定义、数据闭环、eval 标准和行业最佳实践。通用模型能做一版 demo，但不知道什么样的访谈会得到可用数据；这部分知识来自大量失败案例和专有评估。

## Human API：用户偏好会成为 agent loop 的输入层

整场访谈最具未来感的概念是 human API：

> **[26:15]** "almost an human API where the agents are able to call the preferences of your users."

这不是营销词，而是一个很具体的 agent 工作流：coding agent 或其他业务 agent 在构建前调用 Listen，查询目标用户偏好、测试 message、定位 bug、理解 churn，再把结果送回执行 agent。

Alfred 说他们已经被客户推向这个方向：

> **[19:40]** "telling another agent to go and solve that problem."

主持人把公司循环总结成“figure out what to build, build it, repeat”：

> **[30:12]** "a company is figure out what to build, build it, figure out what to build, build it."

而 AI 正在让 build 端指数级变快：

> **[30:24]** "the build it is coming up rapidly up in exponential."

所以 Listen 要占的是 strategy/input 端，而不是 execution 端。Alfred 对未来 one-person company 的想象也很清晰：

> **[30:59]** "we'll have a coding agent and listen and then run that in the loop."

这对个人 IP 和产品工作有直接启示：未来小团队的优势不只是会用 coding agent，而是能不能建立一个持续理解目标人群的输入系统。执行能力趋同后，需求理解会变成更硬的差异化。

## 越接近 AGI，人类输入反而越重要

Alfred 最后没有走向“simulation 替代一切”的结论。他明确说未来仍需要 human input：

> **[34:04]** "in the future you'll still need to have human input"

原因很简单：公司服务的是人，而人是混乱、情绪化、会被 TikTok 趋势突然改变的对象。主持人的总结更锋利：AI 越接近智能极限，人类心智里 AI 没有的部分越重要。

> **[35:14]** "what is in a human's mind that isn't in the AI's mind, only becomes more important."

这可能是 Listen 这个方向最强的长期论证。AI 越强，执行越便宜，产品之间越容易被复制；不可复制的是对具体人群、具体场景、具体动机的实时理解。

## 关键判断

- AI 原生市场研究的本质不是“自动化问卷”，而是把用户推理过程、情绪和上下文变成可追溯数据。
- 人可能对 AI 更诚实，因为 AI 异步、低压、非评判，这会改变访谈数据质量。
- Listen 的核心工程难点不是 voice agent，而是找对受众；用户研究服从幂律，而不是平均人逻辑。
- Simulation 的价值不是替代真人，而是解锁原本不值得做访谈的 99% 小决策。
- 通用模型训练的是平均人，垂直 AI 需要具体 niche 的真实访谈数据。
- 垂直 AI 护城河来自 proprietary eval、数据闭环和行业最佳实践，而不是模型调用能力。
- Human API 是 agent 时代的需求层：执行 agent 需要调用用户偏好来决定构建什么。
- 越接近 AGI，人类输入反而越重要，因为执行趋同后，需求理解成为稀缺资源。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Alfred 把 Satya 的 private eval 落到垂直应用护城河
**← [[Satya Nadella- The Rise of the Full-Stack Builder]]**
- 本文件论点：Alfred 认为 vertical AI 的优势是 proprietary eval，能围绕真实任务从 20% climb 到 85%，再设计更难 eval 继续爬坡 [29:16, 29:38]。
- 对方论点：Satya 认为企业最大的 IP 可能是 private eval，能用自己的 eval 和 trace 在不同模型间 hill climb。
- 关联逻辑：Satya 给出平台级判断：private eval 是控制权；Alfred 给出应用层证据：proprietary eval 是垂直 AI 的复利飞轮。两者合起来说明，应用层护城河不会来自“接入哪个模型”，而来自持续定义和爬升自己的任务评估标准。

### Alfred 为 Karpathy 的 coding agent 补上需求输入层
**→ [[Karpathy- Skill Issue — Code Agents, AutoResearch, and the Loopy Era]]**
- 本文件论点：Alfred 认为 build 端正在指数级加速，未来需要 coding agent 和 Listen 在 loop 中运行，以 human API 决定 what to build [26:15, 30:24, 30:59]。
- 对方论点：Karpathy 认为工程师正在从写代码转向分派 agent、审查宏观动作，并最大化 token throughput。
- 关联逻辑：Karpathy 解释“build it”如何被 agent 加速，Alfred 指出加速后真正稀缺的是“figure out what to build”。两者合在一起，才构成完整的 AI 原生公司循环：用户洞察驱动任务，coding agent 执行，结果再回流用户研究。

### Alfred 具体化 Evans 的“应用层价值捕获”
**← [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Alfred 认为通用模型训练的是 average person，Listen 的差异化来自具体 niche 的访谈数据、受众图谱和 simulation [22:57, 24:07]。
- 对方论点：Evans 认为基础模型会商品化，价值将由懂具体任务、具体工具、具体用户的应用层捕获。
- 关联逻辑：Evans 从产业结构说明为什么模型层难以保留全部价值，Alfred 展示了应用层如何实际捕获价值：不是做一个 wrapper，而是拥有独特数据、任务 eval 和用户偏好接口。

### Alfred 与 DeepMind 共同指向 agent 之间的接口经济
**→ [[DeepMind- 当百万 AI Agent 相遇]]**
- 本文件论点：Alfred 设想 human API，让 coding agents 和 other agents 调用用户偏好，并把 churn interview 发现的问题交给另一个 coding agent 解决 [19:40, 26:15]。
- 对方论点：Tomašev 认为当大量 agent 相互委托、交易和执行任务时，安全范式必须从单模型对齐转向 agentic economy 的机制设计。
- 关联逻辑：Alfred 描述的是 agent economy 的正向产品接口：需求信息如何被 agent 调用；Tomašev 描述的是同一经济的风险边界：委托、权限、合约和激励如何治理。Human API 如果进入 agent loop，本质上也需要可验证调用、用途限制和责任边界。

---

**元信息**
- 标题：Knowing What Your Customers Want, All the Time: Listen Labs' Alfred Wahlforss
- 频道：Sequoia Capital
- 嘉宾：Alfred Wahlforss
- 发布时间：2026-06-02
- 时长：40:22
- YouTube链接：https://www.youtube.com/watch?v=Rumft-rsEu4
