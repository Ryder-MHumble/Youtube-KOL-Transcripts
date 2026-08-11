---
title: "Karpathy- We're summoning ghosts, not building animals"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=lXUZvyajciY"
transcript: "[[Andrej Karpathy — “We’re summoning ghosts, not building animals”]]"
tags:
  - kol情报
status: canonical
created: 2026-07-23
order: 10
---

Karpathy 这场访谈的核心判断是：当前 AI 不是正在突然长成“动物”，而是先用互联网模仿造出一类数字幽灵；agent、持续学习、RL、教育和软件工程的所有困难，都来自我们还没有把这个幽灵改造成能在真实世界中积累经验的实体。

对应逐字稿：[[Andrej Karpathy — “We’re summoning ghosts, not building animals”]]

## Agent 不是元年问题，而是十年工程

Karpathy 对“Agent 元年”的反应非常明确：这不是一年，而是一个十年级别的工程。他不是否认 Claude、Codex 这类工具已经有用，而是强调要把它们从“每天可用的强工具”推进到“能像员工/实习生一样可靠承担任务”，还缺一整组基础能力。

> **[1:21]** "In my mind, this is more accurately described as the decade of agents."

他列出的缺口很具体：智能不够、多模态不够、computer use 不够、持续学习缺失。尤其是持续学习这点，直接指向当前 agent 的组织落地瓶颈：你不能像带新人一样告诉它一件事并期望它长期记住。

> **[2:11]** "The reason you don't do it today is because they just don't work."

> **[2:20]** "They don't do a lot of the things you've alluded to earlier. They don't have continual learning."

这对产品判断很重要。现在很多 agent demo 看起来像“快到临界点”，但 Karpathy 的时间尺度更像自动驾驶：可演示不等于可部署，能跑一次不等于能承受长尾、责任和持续组织记忆。对工作流产品来说，真正要问的不是“模型能不能完成这个任务”，而是“它失败时谁发现、经验如何回流、下次是否不再犯同样错误”。

## 过早做代理，是 Atari 和 Universe 留下的教训

Karpathy 回顾 OpenAI Universe 时，给了一个很有价值的历史校正：早期大家想让 agent 用键盘鼠标操作网页，但那时表征能力还没准备好。没有强表示，端到端地在网页里乱点、等稀疏 reward，基本就是烧算力。

> **[6:17]** "My project at OpenAI, for example, was within the scope of the Universe project, on an agent that was using keyboard and mouse to operate web pages."

> **[6:42]** "Because if you're just stumbling your way around and keyboard mashing and mouse clicking and trying to get rewards in these environments, your reward is too sparse and you just won't learn."

这段解释了为什么 computer use 到今天仍比 coding 慢。代码环境可复制、可回滚、可自动验证；网页和真实软件是活环境，有登录态、权限、反爬、不可重放状态和真实副作用。早期 Universe 做不起来，不是方向错，而是先后顺序错：先要有 LLM 级表征，再把行动、工具和反馈接上去。

对当前 Codex/浏览器自动化任务也是同一个判断：computer use 不应被看成“模型自己随便点网页”，而应被设计成带审计、带状态回放、带明确权限边界的工程系统。否则只是把 Universe 的稀疏 reward 问题重演一遍。

## “幽灵而非动物”：LLM 的起点不是进化，而是互联网模仿

整场访谈最有穿透力的隐喻是“ghosts, not animals”。Karpathy 反对直接拿动物智能启发 LLM，因为动物来自进化，出生时带有大量硬件先验；LLM 来自互联网文档模仿，是另一类智能起点。

> **[9:25]** "We're building ghosts or spirits or whatever people want to call it, because we're not doing training by evolution."

他把 pre-training 称为“crappy evolution”：不是因为它没用，而是因为它是我们当前技术条件下能做的、粗糙压缩版的进化替代品。它把互联网中的知识和算法模式压进权重里，作为后续 RL、tool use、agent training 的起点。

> **[12:28]** "That's why I call pre-training this crappy evolution."

这个框架的隐含立场很清楚：Sutton 想从经验流构造动物式智能，Karpathy 更务实地承认我们不会复刻进化，至少短期不会。我们先造出会模仿人的数字幽灵，再逐步给它加上动物缺的东西：行动、长期记忆、持续学习、具身反馈和自我修正。

## 认知核心：智能不等于记住更多互联网

Karpathy 对模型内部的一个关键区分，是知识和算法。预训练同时让模型记住大量互联网，也让模型学到解题、类比、in-context learning 等算法模式。但他怀疑，过多记忆反而妨碍智能；理想方向是剥离知识，留下 cognitive core。

> **[14:17]** "figure out ways to remove some of the knowledge and to keep what I call this cognitive core."

他的工作记忆类比也非常有用：权重里的信息像一年前读过的模糊记忆，context window 里的信息才是直接工作记忆。KV cache 每个 token 承载的信息远高于权重压缩后的 token 信息量。

> **[18:57]** "Whereas anything that happens in the context window of the neural network—you're plugging in all the tokens and building up all those KV cache representations—is very directly accessible to the neural net."

但 context 不是长期学习。Karpathy 指出，人类睡眠中似乎有某种把日间经验压缩回长期结构的过程，而当前 LLM 没有这个 distillation phase。

> **[23:27]** "These models don't really have a distillation phase of taking what happened, analyzing it obsessively, thinking through it, doing some synthetic data generation process and distilling it back into the weights"

这里和 Dwarkesh Patel 的持续学习判断完全咬合：长 context 不是权重更新。一个企业 agent 如果只是把全部历史塞进上下文，本质上是在堆工作记忆，不是在形成组织经验。真正有价值的系统要能把交互经验压缩成规则、偏好、异常处理和长期技能。

## RL 的根本问题：用吸管嘬监督信号

Karpathy 对 RL 的批评集中在信用分配：一个长达一分钟的 rollout，最后只得到一个标量 reward，再把这个信号广播到整条轨迹。这种训练方式在数学上可行，但在人类学习视角下很荒谬。

> **[43:19]** "The way I like to put it is you're sucking supervision through a straw."

> **[43:22]** "You've done all this work that could be a minute of rollout, and you're sucking the bits of supervision of the final reward signal through a straw and you're broadcasting that across the entire trajectory and using that to upweight or downweight that trajectory."

这个判断应该放在 KOL 情报库的“信用分配稀疏性”主轴上：AI 不是没有试错能力，而是试错信号太粗。人类解决问题后会复盘哪一步有效、哪一步绕远；当前 RL 往往只知道整条路径“最后赢了”。

这也解释了为什么 process supervision 看起来应该更好，却没有简单成功：你需要 judge 每一步，但 LLM judge 本身会被对抗样本攻击。

> **[47:02]** "It's the fact that anytime you use an LLM to assign a reward, those LLMs are giant things with billions of parameters, and they're gameable."

> **[48:17]** "How is it getting a reward of one or 100%?"

所以 Karpathy 的批评不是“不要 RL”，而是“现在的 RL 监督密度太低，judge 又不可靠”。这给产品和组织自动化一个很具体的设计要求：不要只看最终任务是否成功，要记录中间决策、状态变化、工具调用和人为纠错，让监督信号从终点标量变成可追踪的过程反馈。

## 合成数据的死结：单样本看不出坍缩，多样性已经死了

Karpathy 对 synthetic data 的担忧集中在“silent collapse”。单个模型输出看起来合理，但多采几次会发现分布很窄，缺少人类输出的熵和多样性。继续在这种输出上训练，会进一步加剧坍缩。

> **[52:10]** "That's because all of the samples you get from models are silently collapsed."

> **[52:38]** "It only has like three jokes."

他把这件事和记忆问题连起来：人类记忆差反而是特性，因为忘记迫使我们寻找模式和泛化；LLM 记忆太强，反而会被预训练文档的具体记忆分散注意力。

> **[56:10]** "We're not actually that good at memorization, which is actually a feature."

这对内容生产也有直接启发。用 AI 生成观点总结时，不能让模型“整理得更顺”就算完成，因为模型天然会压窄表达分布、抹平异常和尖锐处。KOL 分析必须保留原话，尤其保留 speaker 的犹豫、隐喻、反直觉表述和边界条件；否则分析会变成一篇更流畅但信息密度更低的二手文章。

## AGI 不会像单点爆炸，更可能混入 2% 增长曲线

Karpathy 对“超级智能突然降临”的叙事比较谨慎。他不喜欢把 intelligence 当成单一维度，更倾向从任务 horizon、上下文复杂度、责任面和自动化范围去看进展。

> **[1:07:41]** "Then they can autonomously do tasks that take an hour, a human an hour, a human a week."

他对未来风险的想象也不是一个单体超级智能统治一切，而是很多逐渐自治的数字实体形成热锅式活动，人类把越来越多任务委托出去，系统整体越来越难理解。

> **[1:21:10]** "not even a single entity that takes over everything, but multiple competing entities that gradually become more and more autonomous."

这比“AGI 某年到来”更适合做产品判断。真正会改变组织的不是一个日期，而是任务 horizon 的持续延长：从几分钟、几小时，到几天、几周；从单一工具，到跨系统；从建议，到执行；从人类确认，到 agent-agent 协商。每一层都不是新闻标题，但都会改变流程和权力结构。

## 自动驾驶给软件 agent 的警告：长尾和安全把 demo 拖成十年

Karpathy 用自动驾驶解释为什么从 demo 到产品需要很久：失败成本高、长尾复杂、表示学习和常识需要时间。更关键的是，他把软件工程也放进类似框架：软件失败可能不伤人，但安全、隐私和系统面更广，后果可以很严重。

> **[1:45:32]** "So in software, people should be careful, kind of like in self-driving."

自动驾驶的教训不是“agent 会很慢”，而是“越接近真实责任面，越不能只看平均表现”。企业软件、支付、医疗、政务、数据处理都属于这种场景。一个 agent 在 90% 情况下节省时间，如果 1% 情况下泄露数据、错删记录、错误授权，产品就无法直接放权。

这也解释了为什么 Karpathy 在另一场 AI Ascent 里强调 agentic engineering：vibe coding 抬高地板，但质量、安全和责任仍由人负责。Agent 可以填空，但人必须定义 spec、测试、边界和审美。

## 教育是后 AGI 时代的人类自保机制

Karpathy 最后谈 Eureka 和教育时，不是把教育当知识分发，而是当“booting up a brain”。他关心的是 AI 发展在“人类旁边”发生，最终使人类被边缘化；教育是让人保持认知自主的方式。

> **[1:57:42]** "My personal big fear is that a lot of this stuff happens on the side of humanity, and that humanity gets disempowered by it."

他对教育的定义很硬：不是柔性的知识扩散，而是为知识搭坡道，让复杂知识变成可攀爬的路径。

> **[2:03:21]** "In my mind, education is the very difficult technical process of building ramps to knowledge."

后 AGI 时代，教育可能像健身房：不再因为产业必须用你的脑力，而是因为保持认知能力本身有心理、社会和人类意义。

> **[2:09:30]** "Education will play out in the same way. You'll go to school like you go to the gym."

这对个人 IP 也有现实意义：未来内容的价值不是把信息搬给别人，而是把复杂知识铺成能走的坡道。真正的教育型内容不是“总结得更短”，而是让读者形成可复用的认知结构。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 世界模型是 Karpathy 信用分配诊断的架构解法
**→ [[World Models, JEPA And The Path To Sample-Efficient RL]]**
- 本文件论点：Karpathy 认为 RL 是“sucking supervision through a straw”，长 rollout 最后只得到一个标量，再广播到整条轨迹 [43:19, 43:22]。
- 对方论点：World Models 一文中，Francois 把 world model 定义为 state transition function，并用 Dreamer 合成 rollout 让 agent 在行动前预演状态变化。
- 关联逻辑：具体化。Karpathy 说问题是监督信号太稀疏，World Models 给出的是让中间信号变密的架构方向：如果模型能预测每一步动作后的状态，就不必等终点 reward 才知道方向。世界模型把“最后对错”拆成一串可预演后果，是对吸管式监督的结构性回应。

### 持续学习不是长上下文，而是经验压缩回权重
**→ [[Dwarkesh Patel- What does the next training paradigm look like]]**
- 本文件论点：Karpathy 认为当前 LLM 没有 sleep-like distillation phase，不能把会话经验分析、生成合成数据并回写权重 [23:27]。
- 对方论点：Dwarkesh Patel 认为部署中学到的知识困在 context window，OPSD 和 dreaming 可能成为让经验回流权重的下一条 scaling 轴。
- 关联逻辑：补充。Karpathy 从认知类比解释“缺了什么”，Dwarkesh 从训练范式提出“可能怎么补”。两者共同反驳“context window 变长就等于持续学习”：context 是工作记忆，持续学习需要压缩、筛选和固化。

### Computer use 的不可磨性解释了 Universe 为什么太早
**← [[Grant Sanderson- AI and the future of math]]**
- 本文件论点：Karpathy 回顾 OpenAI Universe，认为早期用键盘鼠标操作网页时 reward 太稀疏，表征不足，烧算力也学不起来 [6:17, 6:42]。
- 对方论点：Grant Sanderson 把“可验证”进一步拆成“可磨”：数学和代码可复制、可并行 rollout，computer use 虽可验证结果却难以低成本重放真实网站。
- 关联逻辑：解释。Grant 的可磨性框架为 Karpathy 的历史经验提供结构原因。Universe 不是纯粹失败方向，而是进入得太早：真实网页不能像代码容器一样复制一千份并行试错，稀疏反馈和真实副作用让 RL 无法有效学习。

### Software 3.0 的个人能力前提是 cognitive core，而不是记忆外包
**→ [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]**
- 本文件论点：Karpathy 区分记忆和 cognitive core，希望模型减少记忆、保留思维算法；人类记忆差反而迫使泛化 [14:17, 56:10]。
- 对方论点：AI Ascent 一文中，Karpathy 认为 Software 3.0 下 prompt/context 成为编程界面，但人仍负责理解、spec、审美、安全和 agentic engineering。
- 关联逻辑：递进。本访谈解释了为什么“理解不可外包”：无论模型还是人，真正值钱的是 cognitive core，不是 API 细节或事实记忆。AI Ascent 把这一点落到工程实践：API 细节可以交给 agent，但底层概念、质量判断和系统理解不能丢。

### 教育从知识传递转向认知训练
**← [[Grant Sanderson- AI and the future of math]]**
- 本文件论点：Karpathy 说教育是 building ramps to knowledge，后 AGI 时代教育会像健身房，用于保持认知能力和自我塑造 [2:03:21, 2:09:30]。
- 对方论点：Grant Sanderson 认为 AI 数学不只需要给出正确证明，还需要能被人类消化、迁移和解释；概念创造和解释能力仍有长期价值。
- 关联逻辑：补充。Grant 从数学知识的消化性说明“正确答案不等于理解”，Karpathy 从教育哲学说明“知识获取不等于大脑启动”。两者共同指向后 AI 教育的任务：不是压缩信息，而是搭建可攀爬的理解路径，让人保持解释、迁移和判断能力。

**元信息**
- 标题：Andrej Karpathy — “We’re summoning ghosts, not building animals”
- 频道：Dwarkesh Patel
- 发布时间：2025-10-18
- 时长：2:26:08
- YouTube 链接：https://www.youtube.com/watch?v=lXUZvyajciY
- 处理时间：2026-07-23
