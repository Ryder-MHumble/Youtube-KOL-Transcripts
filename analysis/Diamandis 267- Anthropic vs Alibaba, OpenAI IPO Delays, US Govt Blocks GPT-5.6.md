---
title: "Diamandis 267- Anthropic vs Alibaba, OpenAI IPO Delays, US Govt Blocks GPT-5.6"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=-H7J_-zr7pA"
transcript: "[[Diamandis 267- Anthropic vs Alibaba, OpenAI IPO Delays, US Govt Blocks GPT-5.6 逐字稿]]"
kol: Peter Diamandis
channel: Peter H. Diamandis
duration: "2:17:58"
upload_date: 2026-06-30
tags:
  - kol情报
status: canonical
---

> 这期圆桌真正揭示的不是“政府已经控制超级智能”，而是前沿 AI 的控制对象正在从模型权重扩展到客户身份、harness、代码供应链和信任认证。只限制新模型发布并不能封住系统级能力，下一阶段的竞争将围绕谁能证明一套 model + harness + tools 组合值得被允许执行。

**视频链接**：https://www.youtube.com/watch?v=-H7J_-zr7pA  
**对应逐字稿**：[[Diamandis 267- Anthropic vs Alibaba, OpenAI IPO Delays, US Govt Blocks GPT-5.6 逐字稿]]

## 概述

Moonshots #267 用两小时讨论美国政府限制前沿模型访问、中国开放模型与蒸馏、harness、网络安全、OpenAI IPO、量子与光子计算、UBI 和后人类形态。旧稿的问题，是把节目中的新闻转述和嘉宾推演直接写成已经确认的制度变化，并只覆盖了视频前半段。

完整逐字稿支持一个更谨慎、也更有价值的判断：模型访问正在被主权化，但能力并不只存在于最新权重。嘉宾所称的 GLM 5.2 案例发生在 `Frontier SWE` 和特定 harness 上，不能证明旧模型在所有任务上普遍超越受限模型；它真正说明的是，评估和治理若只盯模型版本，会漏掉模型外部编排带来的能力增益。

安全问题也因此改变。企业不能只问“允许哪个模型”，还要问谁提供 system prompt、工具权限、模型路由、生成代码、审计日志和最终合并责任。模型认证会逐渐变成系统认证。与此同时，IPO、蒸馏和量子计算部分都需要区分证据强度：资本充足可以解释延迟上市，蒸馏是否构成间谍行为尚待法律判断，AI 能否发现经济上有用的量子算法仍是条件性预测。

## 政府进入模型发布流程，但“同步机制”仍是嘉宾解释

节目称美国政府把 Mythos 5 的早期访问限制在 100 家公司，并把 GPT-5.6 的早期访问限制在 20 家公司。可以从逐字稿确认的是节目如何报道此事，无法仅凭这场圆桌确认全部政策文件、模型名称和客户数量。

> **[7:15]** "In a parallel story, 2 days ago, just as OpenAI was about to release their newest model, GPT 5.6, the White House struck again and asked them to slow down and only release the model to 20 select companies. Bottom line, the US government is now in the release loop for the most capable models, customer by customer selecting who gets access to the latest models. Part of our discussion here, someone else is controlling whether you got access to frontier models, and maybe that's a good thing."

Alex 将这一变化解释为前沿实验室长期设想的协调机制终于由政府强制实现：不是企业自愿同步减速，而是国家通过准入权让领先实验室按相近节奏释放能力。

> **[11:41]** "And it turns out that the same old coordination mechanism that we've had for thousands of years, government, localized geographic monopoly on force, is more than capable, it appears, of being that coordination mechanism for getting the the final two, at least as of this point in time, the duopoly of Frontier Labs, OpenAI, and Anthropic, to synchronize the release of their capabilities out to the first few dozen customers or users that the government is going to gatekeep."

> **[12:10]** "So, in terms of the raw performance, roughly comparable, and I think what's even more interesting than the fact that 5.6 Sol is head and shoulders in terms of cyber capabilities and other capabilities, also efficiency, versus 5.5, is that basically the government, the US government, has functioned as a synchronization mechanism for helping 5.6 Sol reach essentially some form of parity or near parity with Mythos/Mythos Preview 5. That's extraordinary."

“同步机制”是有解释力的框架，但不是已验证因果。模型能力接近可能来自训练周期、人才流动、共同 benchmark 和技术扩散，政府干预只是其中一种解释。更可靠的产业信号是：前沿模型正在从普通 API 变成按身份、地域、组织和用途分配的受控供应。

对产品团队而言，这意味着模型可用性必须被当作供应链变量。关键工作流需要保存任务状态、允许模型降级或替换，并明确哪些能力可以在本地开放模型上运行，哪些能力需要经过许可的前沿模型。不能继续把单一厂商 API 当成永远可用的基础设施。

## Harness 让能力脱离模型版本，权重级管制因此不完整

Imad 提供了本期最重要的技术信号：在 `Frontier SWE` 这一特定编码评估中，GLM 5.2 配合他们的 harness 位居前列。这里必须保留边界：这是嘉宾对尚待发布测试的陈述，且只涉及一个 benchmark 和一套 harness。

> **[15:33]** "Frontier SWE is asking you to build novel kernels and things, and GLM 5.2 is at the top with that harness. With the normal harness, it's like number four or five, but now you've seen actually with the right harness, open models already can be at the top, and that's crazy when you consider GLM 5.2 is maybe $25 million worth of code of compute, sorry."

Peter 随后把这个局部结果外推为“政府太迟了”，认为已发布模型可以通过优秀 harness 超越被限制的新模型。逐字稿只支持这是 Peter 的推论，不支持它已经在所有用例成立。

> **[16:55]** "on Hold on China. Hold on Hold on on China for one just a second. Just what he might just said is so insanely important that I want to be sure everybody gets it. The The finish to that sentence would be Therefore, the government is too late. You can already take 5.5 or Opus 4.8 and put enough of a brilliant harness around it to make it better than Mythos or better than 5.6 GPT 5.6."

Alex 对 harness 的定义更可靠：它是模型权重之外的能力层，负责注入提示、解析输出、编排工具和混合多个模型。

> **[18:13]** "Well, so a harness typically refers to non-weight capability improvements. So, when you're building machine learning model, there are many phases. Typically consists of a neural network of some sort. Neural network is composed of weights. Neural network has some intrinsic behavior. It goes through pre-training, mid-training, post-training. These all impact the weights directly. Now you have a model and you want to on the fly change its behavior."

> **[19:31]** "So, there are it it's now quite possible as Imad mentioned as many others including myself do to create lots of what Andrej Karpathy might call software 1.0 harnesses that live outside the model that orchestrate the models that feed common system prompts and other prompts to the models that parse the outputs that mix different sorts of models from different vendors in order to achieve super performance. That's what a harness is."

这改变了治理与采购的最小单位。比较模型 A 和模型 B 已经不够，真正部署的是 `模型 + system prompt + memory + tools + router + verifier + budget`。同一个基础模型在不同 harness 中可能拥有完全不同的能力、成本和风险。

因此，模型管制若只按版本号或权重能力分级，会出现三个缺口：旧模型通过更长运行和更强工具提高能力；多模型编排产生单模型没有的组合能力；本地开放模型绕开中心 API 的身份控制。更合理的控制对象是任务能力与执行权限，例如能否访问生产系统、持续运行多久、是否允许自动合并代码，以及结果由谁验证。

## 网络安全的瓶颈从发现漏洞转向信任生成代码

节目用 Mythos 在政府系统中发现漏洞的报道解释模型限制，并讨论 GPT-5.5 Cyber/Daybreak 从寻找漏洞转向自动修复。即使不接受所有新闻细节，问题本身成立：当 AI 生成和修改代码的速度超过人工审查，安全控制不能继续依赖逐行人工阅读。

> **[26:17]** "So, the Associated Press reports Anthropic's Mythos model running red team exercises with the US intelligence agencies under Anthropic's Project Glass Wing, if you guys remember that from 3 weeks ago, has identified vulnerabilities in highly sensitive classified US government computer systems."

> **[34:52]** "85.6 is the highest single model score ever posted. Sam Altman said, quote, the real prize isn't finding the holes, it's automatically writing and testing the fixes across web browsers all the way down to the Linux kernel effectively turning the threat into a cure. So, gents, AI is shifting from offense to defense at scale potentially closing holes faster than attackers can find them. The question is going to be about trust."

Emad 指出基础设施原本就缺少足够的人力审查，随后推演政府可能要求只有认证模型才能合并代码。

> **[38:58]** "So, I think that, you know, there needs to be a massive push for all essential apparatus, government and otherwise, to be hardened by these models, and then that makes it incredibly difficult to attack. The final thing that I think we will see is that you will see probably claims that Chinese models will be introducing backdoors and other things inherently in the code. Because now, this is what you were saying, Peter. Who controls who merges the code? Those thousands of lines of code now that you have."

> **[41:06]** "Yeah, this idea of ISO-certified trustworthy AI stamp of approval imminent and critically important. Then the question is, okay, but what entity is the trustworthy entity giving that stamp of approval? Is it a US entity? Is it a US plus Europe entity? Is it some new NATO type entity? And I I think it'd be very healthy for America to reach out to a much bigger chunk of the world to decide, you know, these issues. It'd be a lot better for global confidence in what we're doing."

认证模型本身仍然不够。安全结果取决于模型版本、harness、依赖来源、工具权限、上下文和部署时配置。真正需要的是可验证的软件供应链：固定模型与 harness 版本、生成内容溯源、沙箱执行、差异测试、独立 verifier、分阶段合并、回滚和责任主体。

这也暴露出新的权力中心。谁能签发“可信 AI”认证，谁就可能控制哪些模型可以进入企业代码库。若认证规则不可审计、只承认单一国家或供应商，安全标准会同时成为市场准入工具。

## OpenAI 延迟 IPO 更像治理与资本选择，不是奇点证据

圆桌对 OpenAI 延迟 IPO 给出多种解释：已融资约 1220 亿美元、管理层不想承担公开披露、业务结构仍在变化、Codex 企业收入尚需扩大，以及团队认为一年后的世界会不同。逐字稿并未证明 SpaceX 股价波动是决定性原因，也未证明递归自我改进让资本失去作用。

> **[46:26]** "Yeah, I agree with Dave's points. I would also say OpenAI screwed up. They focused too long, too early on the consumer assuming that the consumer would be the source of the revenue engine that would power their path to an IPO, and that bet was probably incorrect. They should have focused on enterprise. They're now trying to become Anthropic faster than Anthropic can become OpenAI. That seems to be working."

> **[49:33]** "No, I I I I think that they can manufacture insane amounts of wealth and revenue very, very quickly. Uh as to the extent that they have access to compute. Um I don't think the the revenue visibility and the CFO are a big part of the decision. I I think they genuinely believe the world a year from today doesn't look anything like the world today."

> **[52:37]** "Yeah, well also the employee shares, the vested options, people will buy those from you too. So you don't need the you know, normally people are racing to the IPOs so they can get some personal liquidity, maybe buy a house or a car or something. Here they have tons of secondary liquidity. So what is the purpose of the IPO then? Like you're right, altruistically giving everyone in the world access to your stock would be a really nice thing. Um but putting that aside, like they don't need anything and and then you look at the regulatory overhead."

更深的信号是，超级私营公司可以通过大规模私募和二级市场同时获得公司资本与员工流动性，从而延后公开市场纪律。IPO 不再是融资和员工变现的唯一出口，却仍承担三项不可替代功能：公开披露、广泛所有权和市场化治理。

因此，延迟上市同时提高了战略自由和治理集中度。公司可以避开季度压力，但普通投资者被排除在主要增值阶段之外，利益冲突、关联投资和模型治理也更少暴露。判断这种选择是否合理，应看现金消耗、收入质量、资本需求和治理透明度，而不是用“身处奇点”替代财务分析。

## 蒸馏争议正在把知识产权从复制问题变成能力来源问题

节目转述 Anthropic 指控 Alibaba 通过大量虚假账号蒸馏 Claude。Alex 首先指出其中的法律与立场张力：Anthropic 自身也因预训练使用版权材料面临诉讼，而模型输出蒸馏与语料训练是否应适用同一规则尚未解决。

> **[1:20:35]** "Well, I first I have to point out the irony that Anthropic itself has been the target of multiple suits arguing that it took copyrighted material and maybe not using the term distillation, which is usually reserved for model-to-model training versus corpus-to-model training or pre-training. So, but I I would say the shoe is on is is ironically on the other foot."

他进一步区分了违反服务条款与间谍行为。代理服务可能用折扣访问换取用户放弃推理轨迹隐私，再把这些轨迹用于训练；这会违反平台规则，但是否构成 espionage 仍是待诉问题。

> **[1:22:03]** "The reason for it is the proxies reportedly are gathering all of the reasoning traces you agree to give up any notion of privacy in the reasoning traces. The proxies gather those reasoning traces using you basically as a sock puppet. And now those proxies can be used in principle for distillation or or other efforts. I think it's an interesting question that I'm I'm certain is going to be heavily litigated, whether distillation constitutes espionage or not."

Imad 给出的技术判断是，高质量模型输出可以部分替代昂贵专家标注；但一旦模型和数据改进形成循环，继续追赶未必永久依赖美国模型。

> **[1:23:45]** "But we have reached a plateau and we've reached another level. So if you actually look at why GLM 5.2 is better than GLM 5.1, and you look at what they've said, which I think is actually true, and I also think that Alibaba probably did have these sock puppets as AWG kind of said, using the Claude code spec capacity."

> **[1:24:28]** "But at the same time, you could have this recursive loop where you don't even need to have anyone's data anymore. Again, I think it's very difficult for us to conceptualize, but this is that takeoff scenario where you can't guarantee that if today China could never use any of the US models again, the existing data set they have, the techniques they have are not good enough to keep up with frontier capability. And so that's the difficulty here."

Peter 认为 AI 会让产品被快速重做，因此企业不能只依赖历史 IP 防守；Alex 则提出相反方向：AI 也会增强专利撰写、取证和诉讼，知识产权可能被强化而非消失。

> **[1:26:39]** "Uh because if you're dependent upon IP to protect yourself uh you're just off because AI's going to just reinvent the product much better than you ever did iteratively very much faster and so it's just going to be you need to be constantly innovating not trying to protect what you did years ago. Uh and we can see it happening right here right now."

> **[1:29:10]** "Alex I'll sound maybe just a a different note here, which is I think there are striking parallels between the defense versus offense divide on software vulnerabilities and defense versus offense on IP litigation and IP protection. So one might say superficially, oh yes, sure. IP is over because AI will, for any patent, be able to find a way to route around it. That's the the AI will will overwhelm via offense argument. But at the same time, AI can also strengthen defense. AI can draft better patent claims."

新的产品问题不是简单判断“蒸馏合法或非法”，而是识别能力来源：哪些来自公开数据，哪些来自付费输出，哪些来自用户推理轨迹，哪些来自专家反馈。模型供应商需要更清晰的输出许可和可审计访问机制；使用方则需要避免把低价代理服务当成无条件便宜的 API，因为支付差额的可能是数据与推理轨迹。

## 量子计算的短板可能是算法，光子计算是更近的系统赌注

Alex 对政府量子计划保持克制。他指出，量子计算过去被承诺用于蛋白质折叠等科学问题，但 AlphaFold 以经典计算解决了核心任务。国家建设量子计算机并不自动产生经济价值。

> **[1:34:18]** "The problem as I've mentioned on the pod in the past is quantum for science acceleration just hasn't worked that well. Uh quantum computing was supposed to give us protein folding. Turns out protein folding problem was solved by arguably AlphaFold 3 purely classically without use of any quantum computing."

Imad 的条件性判断是，更强 AI 可能帮助人类向量子计算机提出正确问题。Alex 将瓶颈进一步收窄为：尚未找到同时具有量子优势和经济价值的算法。

> **[1:35:31]** "The most interesting thing is this for me. With super Mythos-level models, we will be able to ask the quantum computers the right questions."

> **[1:37:04]** "So, I think I I have to jump in on this one. I I think it there's a latent assumption in in this scenario that we see some sort of complexity hierarchy collapse. Right now, one of the reasons why quantum computers arguably haven't been that useful is because it's actually really difficult for humans without superintelligence to identify algorithms that are both economically useful and also achieve some sort of quantum advantage. We found a number of quantum advantage algorithms. They're not that useful, at least not economically transformatively useful."

Dave 把更近期的赌注放在高度量化神经网络和光子计算，声称光子硬件可以显著降低轨道计算的质量与能耗。但这些时间表和 `1/100` 质量估计属于嘉宾预测，不能写成已经兑现的产业事实。

> **[1:40:42]** "So, you'll be able to store insane amounts of information in tiny tiny spaces, but the the photonics You know, I've been working for 9 months now on this quantum AI um and working on the algorithm side, but it's almost a certainty now that highly quantized neural nets can perform just as well as floating point 32 neural nets, which opens the door to massive amounts of photonic computation efficiency."

> **[1:41:19]** "Instead of launching uh Nvidia chips and the huge power they consume, get the terrafab started on the photonic compute at about 1/100 the mass for the same amount of computation. And it could be even more than that. 1/100 is a conservative estimate. And so the stepping stone to the discontinuity that Ammar was talking about is clearly photonic computing, not quantum computing the way it's currently defined. But it's still quite it's quantum photonic. It's not quantum quantum."

技术雷达应分三层观察：量子硬件是否达到可靠规模；AI 是否找到具有实际量子优势的算法；光子计算是否在训练精度、制造良率、内存、互联和可编程性上形成完整系统。单一器件效率或行政投资都不足以证明范式迁移。

## UBI 叙事首先过不了财政规模测试

节目末尾对 UBI 给出一个重要反证。Imad 计算，仅依赖政府持有 AI 公司黄金股分红，很难支撑基本生活水平；Peter 又估算美国居民每月 `3000 美元`需要约 `12 万亿美元`年度支出，高于节目所述联邦预算。

> **[1:53:04]** "Like Uh, if you look at how big the AI companies would need to be to get a basic living level of UBI from dividends assuming 5%, it's about $10 trillion and you'd have to own like half of them to get to like halfway there. They'd have to literally be the biggest companies in the world and it would only be to the US, which is question four."

> **[1:53:48]** "Yeah, I did the math, right? If you imagine UBI of 3K a month uh, for just US citizens, US residents alone, that's $12 trillion per year. Uh, and the US budget 7.4 trillion per year. So, um, there's a lot of capital to be made up there."

Diamandis 随后把 UBI 定义为“自由分红”，但价值观定义不能替代资金来源、覆盖范围和通胀效应设计。

> **[1:58:05]** "Why should people give up autonomy to accept UBI if unemployment is not going to be a problem? So, uh JB, I think you've got the premise backwards. UBI isn't a trade for autonomy. It's a foundation for more of it. You know, you can think about it, you know, uh it's less of a welfare uh cage and more like the Alaska Permanent Fund, which I've spoken about before, where every citizen gets a dividend check, and you can do with it what you want, right?"

政策讨论应先回答四个问题：支付来源是什么，谁有资格领取，是否替代现有福利，AI 财富集中在哪些国家。若前沿模型与资本收益集中在美国和中国，单国 UBI 甚至可能扩大国家间不平等。丰裕叙事只有在财政、税制和跨境分配机制成立后，才是政策方案。

## 关键判断

1. **模型访问正在主权化**：身份、地域和用途可能共同决定能力供应，关键产品必须具备模型降级与业务连续性。
2. **治理单位应从模型版本升级为任务系统**：harness、工具、预算和 verifier 会显著改变同一模型的能力与风险。
3. **GLM 5.2 案例是 benchmark 信号，不是普遍能力证明**：它支持“外部编排重要”，不支持“旧模型已在所有任务超越前沿模型”。
4. **AI 代码安全需要系统认证**：模型认证必须覆盖 harness、依赖、执行环境、审计和合并责任。
5. **延迟 IPO 不证明技术脱离资本**：大规模私募和二级市场减少上市必要性，同时加剧所有权与治理集中。
6. **蒸馏争议的核心是能力来源与许可**：违反服务条款、版权侵权和间谍行为是不同法律问题，不能混写。
7. **AI 同时增强 IP 进攻与防守**：产品更容易被重建，专利撰写和诉讼也会更强，结果可能是更密集的动态博弈。
8. **量子价值取决于经济算法，光子价值取决于完整系统**：行政投资、器件效率和乐观时间表都不是商业兑现证据。
9. **UBI 必须先通过财政算术**：黄金股分红无法自动覆盖全民收入，跨国财富分配比单国口号更难。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 从突然下线到逐客户放行：治理从中断权变成分配权
**← [[Peter Diamandis- SpaceX IPOs at $2.89T Market Cap, US Govt Suspends Fable & Mythos 5, Altman Delays OpenAI IPO 265]]**
- 本文件论点：节目称政府把 Mythos 5 和 GPT-5.6 的初期访问限制给少数客户，Alex 将其解释为政府替前沿实验室同步能力释放（[7:15]、[11:41]）。
- 对方论点：#265 记录模型突然下线与外国用户访问中断，并强调政府和 Anthropic 对通知过程存在争议（[29:27]、[34:17]、[34:49]）。
- 关联逻辑：#265 展示政府拥有关闭供应的中断权，#267 展示这种权力进一步细化为客户级分配。新的治理问题不再只是模型能否发布，而是谁被允许使用、按什么标准升级、如何申诉和恢复。产品连续性必须同时应对全面下线与选择性放行两种政策状态。

### Harness 把“不可 contained”从扩散判断推进到系统架构
**← [[Diamandis #266- Large Earth Models, Orbital Compute & AI Personhood]]**
- 本文件论点：GLM 5.2 在特定 Frontier SWE harness 下位居前列，说明能力可以由模型外编排显著放大；但节目对普遍超越的外推尚无证据（[15:33]、[16:55]、[19:31]）。
- 对方论点：#266 用 GLM 5.2 的低价多 token 路线支持“智能不可被 contained，只能被 steered”，质疑长期封锁开放模型的有效性。
- 关联逻辑：#266 给出扩散方向，#267 给出机制：即使新权重受控，旧模型、开放权重、工具与多模型编排仍能重组能力。由此产生的新判断是，steer 不能只做模型对齐，还要设计任务权限、工具边界和系统审计；否则“接受扩散”会退化为没有执行约束的口号。

### Harness 的能力杠杆与策略杠杆是同一控制面的两层
**→ [[Katelyn Lesse & Angela Jiang- Anthropic 的策略层赌注（token 工作分配与开放生态）]]**
- 本文件论点：harness 是权重外能力层，通过提示、解析、模型混合和工具编排让较旧或开放模型在特定任务上获得更强表现（[18:13]、[19:31]）。
- 对方论点：Lesse 与 Jiang 将 harness 进一步拆成执行层与策略层，认为 token 可以分别承担执行、建议、反思和记忆，真正 alpha 来自 token 工作分配（[11:35]、[27:47]）。
- 关联逻辑：#267 证明 harness 改变能力上限，Lesse/Jiang 解释 harness 如何改变单位 token 的回报。两者合并后，模型治理和采购都应比较完整策略栈：不仅评估模型能做什么，还要评估系统把多少 token 用于验证、记忆和建议。更强 harness 既可能绕过模型级限制，也可能以更低成本实现同等能力。

### 可信模型认证与互联网信任结算面临同一种控制面集中
**→ [[Matthew Prince- The Internet's Business Model Is Dead]]**
- 本文件论点：当 AI 自动生成并合并代码，圆桌预测将出现可信模型认证；谁签发认证，谁就控制模型进入关键基础设施的资格（[38:58]、[41:06]）。
- 对方论点：Prince 认为 Agent 时代的访问许可、身份、模型路由和机器支付可能汇聚到 Cloudflare 等网络控制面，同时提醒承载、计量和结算集中会形成新的守门人。
- 关联逻辑：代码认证和内容结算表面属于安全与商业模式，底层却是同一问题：谁定义机器身份、许可和可审计行为。新的基础设施机会是开放的机器信任协议；新的垄断风险是单一平台同时成为流量入口、认证机构、执行环境和结算方。可信 AI 标准必须支持可携带身份、多方认证和透明审计。
