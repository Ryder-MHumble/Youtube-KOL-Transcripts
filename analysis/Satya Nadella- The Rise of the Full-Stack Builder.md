---
title: "Satya Nadella- The Rise of the Full-Stack Builder"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=RQE8OS392dU"
transcript: "[[We Need An Ecosystem in AI, And Every Company Can Win A Place In It]]"
feishu_doc_id: Hw9Gd2P6Iojg2UxVtDwcDNuynUc
tags:
  - kol情报
created: 2026-06-08
order: 29
status: canonical
---

> Satya Nadella 的核心判断是：AI 平台的胜负不在于让所有企业崇拜同一个 frontier model，而在于让每家公司用自己的 eval、trace、context 和 tools 持续复利出自己的 frontier intelligence。

视频链接：https://www.youtube.com/watch?v=RQE8OS392dU

对应逐字稿：[[We Need An Ecosystem in AI, And Every Company Can Win A Place In It]]

## 核心证据校准

> **[1:59]** "let's sort of conceptualize this more as an ecosystem play as opposed to a single model or even a single platform"

> **[2:15]** "a platform is defined by fundamentally its ability to create more value about the platform versus what's captured in the platform."

> **[2:33]** "participate as a first-class participant where they can point to AI they create."

> **[4:37]** "Not just as a generalist, but to create their own specialist by building this hill climbing scaffold around it"

> **[4:45]** "Most importantly, you'll have private eval"

> **[6:38]** "the true eval is when people out there are able to do unique things that they only can value."

> **[9:56]** "you kind of want the harness to define the models, the the data, uh and the tools."

> **[10:30]** "the amount of work you need to do to prep the context layer uh such that your plan can execute in the most efficient way is where the magic is."

> **[13:07]** "every company having private E valves may be the biggest IP"

> **[13:18]** "If you can, then you're in control. If you can't, you're not in control."

> **[13:49]** "having an open harness, letting all models come in, having your evals, your contacts, your tools help you hill climb"

> **[14:39]** "can everybody operate at the frontier with their frontier intelligence"

> **[15:41]** "why have a developer conference? I can just come and have you all sort of just worship at the altar of one model."

> **[16:39]** "a bunch of agents doing work and a bunch of humans doing work and the traces between those, that is really important context"

> **[16:58]** "train not a generalist model, but to train the train the company veteran agent."

> **[20:33]** "we have exposed what was perhaps the most important database in a company that never got used as a database"

> **[22:25]** "most people love outcomes until they have an outcome."

> **[25:04]** "what software do I really want to generate? What software do I want to use from others?"

> **[27:01]** "the ability to inspect things, learn things, see things."

> **[28:49]** "built up a new discipline called full stack builder"

> **[30:01]** "the generalist role is going to be the most exciting"

> **[32:55]** "Our job is to build the agentic system does that does Azure networking."

> **[33:38]** "They basically took their work and made it meta."

> **[35:05]** "unless we as an industry are very principled about ensuring that the benefits of all the stuff we're talking about are felt in real ways at the community level"

> **[39:12]** "The future is going to be glorious."

> **[41:23]** "the way to get to information, way to educate yourself, way to continuously keep yourself updated has changed so much."

## 概述

这场 No Priors 与 Latent Space 在 Microsoft Build 期间的交叉访谈，表面上是在问微软的 AI 平台战略、SaaS 会不会被 agent 重写、工程师角色如何变化；真正的主线是 Nadella 在重定义“平台”本身。微软不想把开发者大会变成单模型朝圣，也不把企业 AI 的未来理解成“所有人调用同一个最强 API”。他的回答是：企业必须拥有自己的 eval、trace、context、tooling 和 harness，才能在 frontier model 持续更替时仍保有控制权。

> **[1:59]** "let's sort of conceptualize this more as an ecosystem play as opposed to a single model or even a single platform"

这个判断比“微软要做生态”更具体。Nadella 说平台的定义不是平台本身捕获多少价值，而是平台之外能创造多少价值。

> **[2:15]** "a platform is defined by fundamentally its ability to create more value about the platform versus what's captured in the platform."

所以他真正反对的是模型中心主义：如果 AI 时代只剩少数模型公司和一堆调用方，那么企业没有 terminal value，开发者生态也没有意义。微软要卖的不是“微软自己的智能”，而是让每家公司“operate at the frontier with their frontier intelligence”。

> **[14:39]** "can everybody operate at the frontier with their frontier intelligence"

## 私有 eval 不是评测工具，而是企业控制权

Nadella 对 MAI 模型的解释很克制。他没有把它包装成微软要正面击败 OpenAI 或 Anthropic，而是把 MAI 放进一个更大的企业能力链条：干净 lineage 的预训练模型、hill climbing scaffold、RLE、trace 收集、private eval。

> **[4:37]** "Not just as a generalist, but to create their own specialist by building this hill climbing scaffold around it"

> **[4:45]** "Most importantly, you'll have private eval"

这说明他眼里的“企业智能”不是微调一个专用模型，而是建立一套可以持续爬坡的系统。公开 benchmark 已经会被刷满，真正有价值的是企业自己定义的任务、数据和验证标准。

> **[6:38]** "the true eval is when people out there are able to do unique things that they only can value."

最关键的是他把 private eval 变成了控制权测试：你能不能从 model A 切到 model B，并继续沿着自己的 eval hill climb。

> **[13:18]** "If you can, then you're in control. If you can't, you're not in control."

这句话其实是在给企业采购 AI 平台一个非常实用的判断标准。供应商锁定不再只是 API、数据导出或合同条款问题，而是你的 eval、trace、tool、context 是否被绑定在某个模型生态里。能迁移，说明你的能力在自己手里；不能迁移，说明你只是把公司的未来能力外包给了模型供应商。

## Harness 是微软第三幕：模型、数据、工具的可替换循环

访谈里最值得拆的概念是 harness。主持人把 coding agent 外面的环境、上下文和工具称为 harness，Nadella 立刻把这个概念推广到企业。

> **[9:56]** "you kind of want the harness to define the models, the the data, uh and the tools."

这个定义很重要：harness 不是 prompt wrapper，也不是普通工作流编排器，而是模型、数据、工具之间的循环结构。微软的 Copilot、Security Copilot、M dash、科学发现工具，本质上都是多模型 harness。

真正的难点不在模型，而在 context layer 的准备。

> **[10:30]** "the amount of work you need to do to prep the context layer uh such that your plan can execute in the most efficient way is where the magic is."

这解释了微软为什么天然适合押这个位置。Windows 时代的微软掌握应用生态入口，Azure 时代掌握云基础设施，AI 时代它试图掌握企业 context、identity、tool access、workflow 和 eval loop 的连接层。Nadella 明说 open harness 很关键：

> **[13:49]** "having an open harness, letting all models come in, having your evals, your contacts, your tools help you hill climb"

这里的战略含义是：如果模型层持续商品化，平台价值会转向“谁能组织上下文并让不同模型可替换地完成任务”。这也是微软与纯模型公司的错位竞争：它不一定要拥有最强单模型，但要成为企业把模型变成生产力的操作系统。

## SaaS 不会简单消失，但会被拆成可重组资产

Nadella 对“软件终结”的回答没有走极端。他承认 SaaS 过去的包装方式会被重审：数据模型、业务逻辑、UI 被垂直堆叠成一个工作流应用。AI agent 出现后，这个堆栈要被拆开重组。

他认为 durable 的部分首先是数据模型和业务逻辑。总账 schema 不需要被重新发明，Power BI 里沉淀的语义模型也不是废物；真正变化的是这些资产不再只服务原来的 UI，而会被 agent 调用。

> **[20:33]** "we have exposed what was perhaps the most important database in a company that never got used as a database"

Work IQ 的例子很好地说明了这个重组方向：邮件、Teams、Word、Excel、PowerPoint、SharePoint 过去只是应用里的内容，现在变成 agent 可以查询、综合、执行的企业数据库。Nadella 举的 GitHub repo 例子，本质上是把会议记录、设计讨论和代码修改计划连成一条 agentic workflow。

因此 SaaS 的问题不是“买还是自建”的二元选择，而是：

> **[25:04]** "what software do I really want to generate? What software do I want to use from others?"

这比“AI 会杀死 SaaS”更接近企业现实。企业会短期经历 agent euphoria，尝试重建大量内部软件；但一个预算周期后，维护、安全、token 成本、责任边界都会重新进入计算。未来更像是采购稳定数据模型和业务逻辑，再用 agent 重组 workflow，而不是每个团队都重写一个小型 SaaS。

## 定价会从订阅制走向订阅加用量，但 outcome pricing 没那么简单

Nadella 对商业模式的判断也很务实。他认为 per-user pricing 不会消失，因为它本质上是预算确定性的产物。

> **[22:07]** "The per user pricing is really an artifact of someone creating a budget needing certainty."

但 agent 使用强度起来后，订阅必须叠加 consumption meter。GitHub Copilot 原来按人收费，是因为那时使用形态还是 code completion 或互动式任务；当用户能启动成千上万个 agents 全天运行，单纯按人收费就会失真。

> **[23:42]** "It is not like oh, I launched 10,000 sort of agents that are going on all day"

他对 outcome pricing 的判断尤其真实：

> **[22:25]** "most people love outcomes until they have an outcome."

客户嘴上喜欢按结果付费，但当供应商真要分享 outcome，就会变成让渡 royalty。这个判断说明 AI 产品定价会长期混合：订阅负责预算确定性，用量负责成本归因，少数可明确归因的场景才可能 outcome-based。所谓“按结果收费”不是终局答案，而是买卖双方重新分配风险和收益的谈判工具。

## Full-stack builder 的重点不是人人写代码，而是人人能检查和触达更多系统

主持人问未来工程角色是否会收缩到 agent manager、FDE、安全工程师和基础设施工程师几类。Nadella 没有直接确认，但给了 LinkedIn 的组织实验：把设计、产品、前端工程放到一个新角色里，叫 full stack builder。

> **[28:49]** "built up a new discipline called full stack builder"

这不是取消专业边界，而是扩大每个人的作用域。设计师仍有设计 edge，前端仍有前端 edge，但角色不再被单一职能困住。Nadella 说 generalist 会获得最大杠杆：

> **[30:01]** "the generalist role is going to be the most exciting"

更准确地说，AI 让 generalist 可以跨过以前“碰不到”的 artifact。Nadella 作为 CEO 用 Copilot 读代码库、理解系统、构建 long-running Foundry agents，并不意味着 CEO 应该亲自写生产代码，而是说明高层管理者、产品经理、运营负责人都能直接检查以前依赖工程团队转译的系统。

> **[27:01]** "the ability to inspect things, learn things, see things."

对个人 IP 和产品工作来说，这个判断很重要。未来的高杠杆人才不是“会不会写代码”的二分，而是能不能把业务判断、产品意图、系统理解和 agent 协作连起来。full-stack builder 的本质是把以前分散在 PM、设计、前端、数据、运营之间的反馈回路压缩到一个人或一个小队里。

## 真正的 agent 化不是多几个自动化工具，而是把工作变成元工作

Nadella 最有洞察的组织案例是 Azure 网络团队。微软过去 15 个月建出的 Azure 容量超过前 15 年，同一个团队如果只是“更努力做网络运维”，显然撑不住。他们重新定义了自己的工作：

> **[32:55]** "Our job is to build the agentic system does that does Azure networking."

这不是普通自动化。普通自动化是把某个流程脚本化；这里是团队把自己的职责从执行层提升到系统设计层。Nadella 的总结是：

> **[33:38]** "They basically took their work and made it meta."

这句话是整场访谈最值得企业吸收的管理判断。AI 时代的组织升级，不是把员工替换成 agent，而是让团队重新问：我们的工作到底是完成这些任务，还是构建、监督、改进一个能完成这些任务的 agentic system？一旦工作变成元工作，团队的核心能力会从执行经验转向任务建模、工具接入、权限治理、异常处理、评估标准和 token 预算管理。

这也解释了为什么 Nadella 不把 AI 看成简单降本。他引用 Kevin Scott 的框架：让困难的事情变容易是一种杠杆，但真正的野心是让不可能变为可能。

> **[31:54]** "true ambition is about making the impossible possible."

## 社会许可是 AI 基础设施的硬约束

访谈后半段，Nadella 对数据中心和社会影响的表达非常审慎。他没有用“技术会自然惠及所有人”的叙事，而是说社区有理由怀疑，行业必须交付真实利益。

> **[35:05]** "unless we as an industry are very principled about ensuring that the benefits of all the stuff we're talking about are felt in real ways at the community level"

他说得很具体：能源价格、长期电网改善、水循环、培训、就业、税基。如果这些不能真实发生，行业就不会获得 permission。

> **[36:02]** "If it is not, we won't have permission."

这不是公关语言，而是基础设施扩张的政治经济约束。AI 数据中心消耗能源、水、土地和公共信任，如果收益只体现在少数科技公司的估值和模型能力上，社会反弹会变成部署瓶颈。Nadella 对“trust us”的否定很直接：

> **[39:12]** "The future is going to be glorious."

这句在逐字稿里是他说技术公司会讲的承诺，而他的意思恰恰是世界不会再接受这种承诺。AI 太大、占经济比重太高，必须用可见的社区收益换取继续建设的合法性。

## 教育机会在于把学习、认证和就业重新接起来

访谈结尾的教育部分不是附带话题。Nadella 认为信息获取、自我教育和持续更新的方式已经变了：

> **[41:23]** "the way to get to information, way to educate yourself, way to continuously keep yourself updated has changed so much."

但教育体系的激励、证书、就业机会还没有同步变化。他没有说传统基础概念不重要，反而提到仍然要理解 softmax，而不是只让 AI “fix my training run”。真正的创业机会，是把 AI 辅助学习转化为可靠课程、可信 credential 和经济机会。

> **[41:47]** "or a new um pedagogy even of how to get someone to go through a curriculum and find economic opportunity"

这与 full-stack builder 的判断相互呼应：AI 提高了个人触达复杂系统的能力，但社会还缺一套把这种能力校准、认证并连接到工作机会的机制。教育创业如果只做“AI tutor”，可能只是更好的内容界面；真正大的机会在于重建学习到就业的制度连接。

## 关键判断

- 微软的 AI 战略不是押单一 frontier model，而是押企业能自建 frontier intelligence 的生态和 harness。
- Private eval 是企业 AI 时代的新 IP，也是判断供应商锁定的控制权测试。
- Harness 的核心价值在于组织模型、数据、工具和 context layer，而不是简单封装模型 API。
- SaaS 不会简单死亡；数据模型和业务逻辑会被保留，UI 和 workflow 会被 agent 重组。
- AI 定价会走向订阅加用量，outcome pricing 只会在少数收益可归因场景成立。
- Full-stack builder 不是“人人变工程师”，而是高杠杆 generalist 能直接检查、理解和构建更多系统。
- 真正的组织 agent 化，是把执行工作升级为构建和管理 agentic system 的元工作。
- AI 基础设施扩张需要社区层面的可见收益，否则社会许可会成为硬瓶颈。
- 教育创业的关键不是更聪明的 tutor，而是重新连接学习路径、认证标准和经济机会。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Satya 把 Evans 的模型商品化判断转化为平台路线
**← [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Nadella 认为企业要用 open harness、private eval、context 和 tools 在不同模型间 hill climb，能切换 model 才说明控制权在自己手里 [13:18, 13:49]。
- 对方论点：Evans 认为基础模型缺少可持续差异化和定价权，价值会向应用、工具和专用工作流逃逸。
- 关联逻辑：Evans 从产业经济层面说明“为什么模型层会商品化”，Nadella 给出平台公司应该怎样顺势而为：不赌单模型垄断，而是占据模型可替换之后的企业控制层。两者合起来看，AI 平台护城河会从模型能力转向 eval、context、tool access 和 workflow ownership。

### Satya 为 Karpathy 的 agentic engineering 补上企业组织形态
**← [[Karpathy- Skill Issue — Code Agents, AutoResearch, and the Loopy Era]]**
- 本文件论点：Nadella 用 Azure 网络团队说明，团队职责会从“做网络运维”变成“构建做网络运维的 agentic system”，工作被提升为元工作 [32:55, 33:38]。
- 对方论点：Karpathy 认为工程师要从直接写代码转向分派、约束、审查和移除自己这个 bottleneck，工作单位从代码行变成 agent 宏观动作。
- 关联逻辑：Karpathy 描述的是个人工程师如何获得 agent 杠杆，Nadella 描述的是大型组织如何把这种杠杆制度化。二者相互具体化：个人层面的 agentic engineering 如果要进入企业生产系统，必须变成权限、评估、预算、异常处理和组织职责的重新设计。

### Satya 的 private eval 与 Brown 的 budgeted capability 共同重写评估范式
**← [[Noam Brown- Test-Time Compute Changes Benchmarks, Safety and Research]]**
- 本文件论点：Nadella 认为公开 eval 会被 max out，真正的企业 IP 是 private eval，以及基于 trace 和 scaffold 的持续 hill climb [4:45, 13:07]。
- 对方论点：Brown 认为模型能力不再是静态属性，而是 test-time compute、预算、scaffold 和任务类型的函数，评估必须说明预算轴。
- 关联逻辑：Brown 说明“能力评估必须预算化”，Nadella 说明“评估必须私有化和业务化”。结合后可以看到，下一代 eval 不会只是公开 benchmark，而是企业围绕自身任务、预算和工作流构建的长期能力曲线。

### Satya 与 Dylan Patel 在不同层面描述同一个 co-design 时代
**← [[Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x]]**
- 本文件论点：Nadella 认为企业 AI 的核心是 models、data、tools、context layer 与 harness 的循环设计，magic 在 context layer 的准备 [9:56, 10:30]。
- 对方论点：Dylan Patel 认为 AI 效率跃迁来自模型、kernel、硬件、网络和数据中心资本结构的跨层协同，而不是单层优化。
- 关联逻辑：Patel 讲的是 AI 基础设施层的 co-design，Nadella 讲的是企业应用层的 co-design。两者镜像同一趋势：AI 栈的抽象边界正在变软，未来优势来自跨层联合优化，而不是在既有边界内采购“最好的一层”。

---

**元信息**
- 标题：We Need An Ecosystem in AI, And Every Company Can Win A Place In It
- 频道：No Priors: AI, Machine Learning, Tech, & Startups
- 嘉宾：Satya Nadella
- 发布时间：2026-06-04
- 时长：42:26
- YouTube链接：https://www.youtube.com/watch?v=RQE8OS392dU
