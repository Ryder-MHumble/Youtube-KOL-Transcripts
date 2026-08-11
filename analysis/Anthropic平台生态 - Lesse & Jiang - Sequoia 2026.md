---
title: "Anthropic's Katelyn Lesse & Angela Jiang: Building an Ecosystem, not a Walled Garden"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=vPnVTHYplrQ"
transcript: "[[Katelyn Lesse and Angela Jiang- Building an Ecosystem not a Walled Garden]]"
channel: "Sequoia Capital"
kol: "Katelyn Lesse & Angela Jiang"
duration: "48min 55s"
upload_date: "2026-07-14"
tags:
  - kol情报
created: 2026-07-21
status: canonical
---

> Anthropic 的平台赌注不是拥有每一层基础设施，而是把 agent 的知识、执行和协调抽象成可组合原语；真正的护城河不在 sandbox 跑在哪里，而在谁定义 token 应该承担什么工作。

视频链接：https://www.youtube.com/watch?v=vPnVTHYplrQ

对应逐字稿：[[Katelyn Lesse and Angela Jiang- Building an Ecosystem not a Walled Garden]]

## 概述

Katelyn Lesse 和 Angela Jiang 管的是 Anthropic 最关键的一层：外部开发者 API 与内部产品基础设施共用的平台层。这场访谈表面上讨论开放生态，实际讲的是 Anthropic 对 agent 应用栈的分层控制策略。

她们的核心判断是：AI 产品形态变化太快，今天是 chat，明天是 agent，后天还会出现新形态。平台公司不应该押注单一终端界面，而应该提供足够稳定的原语，让内部团队和外部开发者在同一套抽象上试错。Anthropic 选择开放执行基础设施，允许 self-hosted sandbox、MCP tunnels、外部云厂商承接运行环境；但它不会放弃对 agent 架构接口和策略层的判断。

最值得关注的是“token job”这个隐含范式：token 不再是可互换的消耗单位，而是可以承担建议、执行、反思、记忆、评估等不同工作。谁能把这些工作组合成可复用 strategy，谁就控制了 agent 经济的效率杠杆。

## 形态不稳定，所以平台要押注原语

Angela 对产品形态的判断很清楚：AI 的主流交互形态不会稳定停在 chat 或 agent 上。模型能力年年变化，最佳产品封装也会随之变化。

> **[4:31]** "And one of the maybe the overarching thesis for that is that we've just seen like the capabilities of these models just grow and such just exponential and it's really hard to figure out like a longlasting form factor. I think two years ago we were all like everything's chat and now everyone's like forget chat and just like agents and like there's going to be another form factor, another form factor."

这决定了 Anthropic 的平台策略：不要自己垄断全部 form factor，而是让市场用同一套能力原语生成不同形态。她明确说 Anthropic 不认为只有自己能找出终局形态。

> **[5:01]** "And I don't think we by any means feel like we're the only ones capable of figuring out that form factor like not at all. In fact, the more democratization we can do on that and help people and allow people to experiment, I think the the more those form factors will actually kind of naturally come out of the market."

Katelyn 补充的内部机制很关键：内部 dogfooding 和外部 early access 同时做。内部团队给极限使用压力，外部客户给形态多样性，只有两边都反复出现的需求才值得沉淀成平台能力。

> **[5:43]** "External users have very specific requirements and so if you overindex on one or the other, you fall into a trap. So a lot of the time what we'll do is dog food something internally at the same time that we open up early access of some sort with external customers so that we can kind of get a range of feedback and bring those things back into the platform."

这套方法的产品含义是：平台不是把内部产品拆成 API，而是把内部/外部反复遇到的问题抽象成 primitives。真正的防守点不在某个应用形态，而在“别人无论做什么形态，都更容易用你的原语做出来”。

## 三层蛋糕：知识、执行、协调

Angela 把 Anthropic 平台拆成三层：底层是 knowledge，中层是 execution，顶层是 coordination。这个分层不是文档分类，而是价值迁移路径。

知识层包括 messages API、tools、skills、memory 等，目标是让模型知道如何工作。Angela 说这一层已经相对成熟，仍会演进但越来越 baked。

> **[9:45]** "Like for example there's very specific shapes and parameters we put on the messages API and it's more like trying to expressly like uh showcase Claude's like design like Claude the model's uh actual design the way it thinks the way it respects certain parameters the way it kind of like um will do tool calls like all of those different pieces."

执行层是 Claude 从回答问题变成实际完成工作后需要的基础设施：sandbox、远程会话、存储、治理、安全、上下文恢复。Katelyn 解释 Managed Agents 解决的就是这些重复基础设施问题。

> **[7:14]** "And the problems that we're solving for you are, you know, infrastructure being kind of a hard thing to deal with. like how do you figure out spawning sandboxes that are going to have the right governance and security and like you know spin them up and spin them down when you need to or the storage around transcript sessions so that you can resume a session if you stop it and pick it back up later."

真正的前沿在第三层：coordination，也就是 strategies 或 meta harness。这里的关键不是让模型执行，而是安排不同 token 做不同类型的工作。

> **[11:33]** "But the next one is about okay if tokens aren't really funible and you need to give them different jobs like maybe some this token is advising versus this token is executing this token is dreaming versus this token's executing so on and so forth you want to start composing these like these kind of orchestrated strategies that go together and they should sit on top of all these things because at the end of the day you still need to execute and the execution still needs to know what to do so everything in theory should kind of like ladder together and so I think you know if you were to look at our road map and the maybe kind of project forward a little bit where you kind of expect us to go we'll move more and more from the"

> **[12:05]** "knowledge layer to the execution layer and from the execution layer to the kind of coordination layer in terms of the abstractions that you can see us put out."

这说明 Anthropic 的价值捕获正在上移。底层 API 会稳定，中层执行会被模块化，顶层策略才是差异化核心。换句话说，平台的终局不是“帮你调用 Claude”，而是“帮你决定每一份智能预算应该怎么花”。

## 开放执行层，控制架构层

当主持人直接问 open ecosystem 还是 walled garden，Katelyn 给出的回答并不是“全开放”。她说 Anthropic 不执着于让运行环境都在自己基础设施上。

> **[15:54]** "Yeah, there's so maybe in using Angela's kind of layered cake that we talked about a little bit earlier, you'll see that on some pieces of this like execution for example, um what we've done within something like cloud managed agents and I think over time you'll see us try to make this a little bit more modular. We actually aren't precious about you should run these things on our infrastructure like it should be sandboxes that we control or it should be a storage layer that we control."

self-hosted sandboxes 和 MCP tunnels 是两个具体信号：前者允许外部云或企业自有环境承接执行，后者让 agent 访问防火墙后的 MCP 服务器。

> **[16:17]** "Um well we actually like for example we launched self-hosted sandboxes and we partnered with modal and versel and cloudflare and a bunch of other folks um even like Amazon's new microVMs um to have a first class offering where you can go plug any of those things in."

> **[16:36]** "Um, we launched MCP tunnels so that you can call out to your MCP servers that are behind your firewall, right? And um, be able to punch through there. And so for some of these things, we, you know, the weather, whether it runs on our infrastructure versus somebody else's infrastructure is actually not important to us because the thing that's important to us is more that the architecture of how you put together these agents in a way that will be powerful, in a way that will be reliable and scalable. um we have strong opinions on that and you can kind of just conform to the interfaces that we put out there and plug those things in."

这就是这场访谈最核心的战略张力：基础设施开放不是放弃控制，而是把控制点上移。Anthropic 不在乎 sandbox 在谁家跑，但在乎 agent 如何被组装、如何可靠扩展、如何遵循它定义的接口。

这对生态的判断很重要：未来 AI 平台的护城河可能不是云资源、模型 API 或某个 UI，而是“架构意见”。当足够多开发者按你的接口组织 agent，你就获得了事实标准。

## Claude Tag 暴露了界面与 harness 的分离

Claude Tag 被外界看成 Slack bot，但 Angela 的解释恰好说明 Anthropic 如何看待产品界面：界面只是最外层，真正的资产在上下文工程和 org-level harness。

> **[23:45]** "The important part, um, is all the kind of like context engineering and like architecture that we put underneath the hood. So that tag just works. It really should just like just feel like a co-orker like a co, you know, if you go to a company and you onboard and a co-orker comes into your channel and then you can chat with it."

> **[24:41]** "the proactivity a lot of the harness pieces I think Andre Kaparthi said it really well it's like it's like an org level harness There's a lot of like complexity baked into that like Kayla mentioned like you can use our APIs to go and construct that."

她进一步指出，Slack 不是终局界面。Agent 会进入 Teams、WhatsApp、短信、邮件等人类已经使用的协作空间。

> **[25:24]** "Like Slack is a place where a lot of people collaborate, a lot of business collaborate, but also a lot of people collaborate in teams and some people collaborate by a WhatsApp group um or they text each other or they may some people still email each other and like those could be the form factors that actually completely you can imagine agents just going there and being and they're almost taking up the same form factors as humans have taken up."

这和 enterprise agent 的一个现实路线一致：短期内不需要发明全新 UI，agent 最自然的入口可能是直接占据人类协作界面。真正难的是让它拥有足够上下文、权限、主动性和组织语境，而不是把它包装成一个新 app。

## Harness 不会消失，只会从 steering 迁移到 strategy

Katelyn 和 Angela 对 harness 的判断很精细。低层的 prompt caching、context window 管理、工具调用清理会逐步商品化；真正有价值的是更高层的 token 分配和策略组合。

> **[27:44]** "But this concept that you can take any given token and spend that token on just executing or you could take that same token and choose to actually reflect on your past agentic sessions and write learnings to memory so that the next agent does a good job or you could take that token and advise with a bigger model so that a smaller model can execute and do a better job."

Angela 解释了为什么早期 steering harness 会被模型吞掉。两年前 harness 需要像墙一样把模型从 A 引到 B；现在模型更 steerable，这部分可以删除。

> **[28:53]** "And one of the reasons for that I think is it has to do with the generations of the the models. I if you look like two years ago, a lot of the harness was like a scaffold to kind of like tell the model to go from point A to point B. And you had to like you really had to like build in a lot. You practically build one wall here and one wall here. So like the thing would go in a straight line. And now the models are actually very very steerable."

> **[29:23]** "So, a lot of if you have harnesses um that are like designed to kind of do that kind of like steering, you can delete that part. Like that part we actually frequently encourage like you can delete part of those harnesses."

但删除 steering 不等于删除 harness。相反，模型越能自己走，越需要 strategy harness 管理长程运行、预算分配、验证逻辑和多阶段目标。

> **[30:12]** "In order to be able to do a lot of those things, the kinds of harnesses that you do are less the steering harness and it's more like these kind of strategy harnesses that Caitlyn's mentioning, which allows you to operate at a slightly higher level of thinking which matches I think a lot of the intelligence gains that we're trying to see with the model."

这里对开发者的行动含义很明确：不要在低层脚手架上过度投资。真正该沉淀的是任务策略、验证逻辑、记忆写入规则、模型路由规则和失败恢复流程。

## Token 理性化：别停用 AI，要设计成本策略

访谈后半段，她们把平台策略落到企业成本治理。Angela 接受“token rationalization”的说法：当模型智能到达某个水平，下一轮优化维度就会是成本和速度。

> **[38:28]** "Yeah, I mean it it makes sense. Uh it it makes sense from the high you start to rationalize. I I really like that framing and I think there's like a couple things that that are like top of mind for us on this front. I think like again it makes sense and as these models get more and more capable you're going to hit like levels of intelligence max maxing that are like there that then you want to do the next kind of dimension and the next dimension after intelligence will either be cost or it will be speed."

她反对的做法是简单 cap 或禁止 AI 使用。因为如果 AI 已经带来更快 shipping 或运营效率，停用本质上是在砍掉创新。

> **[39:06]** "Like that's kind of the wrong move. And we do actually see some of our our customers do that. So oftent times the way that AI spend has erupted inside their company has been through some kind of like uh shadow IT, you know, like their employees just like want to use it, they find a way, they end up procuring it themselves, and before you know it, like half your or has like found some way to have installed cloud code."

她给出的解决方案是 strategy/router：根据任务复杂度决定用大模型还是便宜模型。注意她把这限定在 Claude family 内部，而不是跨厂商模型路由。

> **[39:51]** "I mean I'm effectively describing a router but like there are ways to do this that are like I think a bit better now and so like this task comes in has a certain level of complexity for that level of complexity like you can define some rules but for the most part right if it's like a hard task you should probably route that to like a big super smart model and if it's not a hard task you can route that to like cheaper models um designing that I think has a little bit of like there's a lot of technical complexity in that but it's like very very doable and we actually like encourage people to try those kinds of things I think ultimately offer rather I I think within the clawed space it will like make sense."

> **[40:49]** "I think the bit that we do feel really strongly about on the model routing front is like we are designing our platform for Claude and we want to make sure that Claude is great at like solving all these things. So we'll like restrict to that space um rather than you know I don't think we're that interested in saying like okay and then you know you should route to a different model or whatever."

Katelyn 把这个选择理论化：harness 和 agentic layer 应该绑定模型家族。也就是说，Anthropic 的开放是有边界的；它开放基础设施，不开放模型家族无关的抽象层。

> **[41:11]** "and and well some of that too is just like I think we have a strong belief that harnesses and and just like the agentic layer should be tuned to the model family that you use it with. And so I think there was a period where people were kind of like yeah cool I can like build a harness and build an agent and then just like plug in a different model underneath and they were excited about routers from that perspective."

这对“模型商品化”叙事是重要修正。模型 API 可能越来越可替换，但 model + harness + strategy 的组合未必可替换。切换模型不只是换 endpoint，而是换整套策略栈。

## Strategy 是第三根杠杆

Angela 用 bug hunting agent 说明为什么 strategy 是比换模型、跑更久更重要的杠杆。通常开发者只有两个选择：换更大模型，或者让 agent 跑更长。但 Anthropic 的实验显示 best-of-n 这类策略可能带来更高回报。

> **[44:04]** "So to give you something like concrete like when you try to solve for like let's say you want to build an agent that's like trying to um do bug hunting and you could just send one off to go and do that and it's going to give you a certain type of return a level of return of possibility um and then people kind of get stuck at that and they're like okay my next options are I can like make a bigger I can just like swap the model for a different I probably bigger model um or I could like let it run like longer and that's pretty much like the only two like levers that you have to like try to make this like bug hunting agent."

> **[44:35]** "From a lot of experimentation, when we do these kinds of things, there's like actually the thing like those two those two things are still true, but you actually have like a third lever and tends to actually do a lot more than you think it does, which is that actually if you were to like best of end the thing, it would like give you a lot more returns."

但她也指出，知道策略有效和把策略做成生产系统之间差距很大。

> **[45:05]** "Um but we're seeing like this is where the alpha is and it's hard and so like in the same very simple philosophy that we talked about at the beginning like if it's like gives you the return that you want and it's hard we're going to try to make it easy for you so then you can use it to then run the experiments you actually need to run."

Katelyn 把这个方向收束成一句话：token has a job。她们内部可能能列出五种 token jobs，生态开放后会出现十万、二十万种组合。

> **[45:41]** "I guess it could be similar, but if you take it to kind of its ends, it's actually more just like the token has a job. And I think it's this job piece that we're we're really indexed on and um we see a lot of returns too and that's the thing that we want to spend time with users and the rest of the ecosystem on on like how can we just make that easier for folks to then experiment like we can give you like five jobs off the top of our head and we'll probably like that's what we have internally."

这就是 Anthropic 平台战略的最强版本：不是自己找到所有策略，而是把策略组合空间开放给生态，让开发者替它搜索更高 intelligence per dollar 的组合。

## 关键判断

- Anthropic 不押注固定产品形态，而押注跨形态复用的 primitives。
- 平台价值正在从 knowledge layer 迁移到 execution layer，再迁移到 coordination/strategy layer。
- 开放执行基础设施不是放弃护城河，而是把护城河上移到 agent 架构接口和 strategy 设计。
- Claude Tag 的战略意义不在 Slack bot，而在 org-level harness：agent 直接进入人类已有协作界面。
- 低层 steering harness 会被更强模型吞掉，高层 strategy harness 会变得更重要。
- Token 成本治理不能靠简单 cap，应该靠任务复杂度路由、反思/记忆/评估等 token job 组合。
- Anthropic 的开放边界很清楚：sandbox 和连接可以开放，harness-model 绑定不会跨模型厂商中立化。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Token 工作分配补上 token 定价危机的工程解
**← [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]]**
- 本文件论点：Katelyn/Angela 认为 token 不再 fungible，同一 token 可以用于执行、反思、建议、记忆或评估 [27:44]。
- 对方论点：Levie 从企业侧提出 token 消费会击穿 per-seat 定价，企业必须理解单任务 token、模型路由、人工接管和 LTV。
- 关联逻辑：Levie 看到的是成本可见性问题，Anthropic 给出的是成本可优化性路径。两者合并后，企业 AI 的财务模型不只是“花了多少 token”，而是“每类 token job 是否改善了任务成功率、未来复用率和单位成本”。

### Model + harness 组合挑战模型商品化叙事
**→ [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Katelyn 明确说 harness 和 agentic layer 应该 tuned to the model family，Claude 平台不会做跨厂商中立路由 [41:11]。
- 对方论点：Evans 认为模型层缺少网络效应和定价权，基础模型更像电信管道，会被商品化。
- 关联逻辑：Katelyn 没有否认模型 API 会趋同，而是把护城河上移到 model+harness+strategy 的绑定层。Evans 的商品化判断仍适用于裸模型，但如果策略层持续吸收产品 know-how，替换模型的代价就不再是 API 切换，而是整套 agent 行为栈重构。

### Harness 从能力放大器变成治理对象
**→ [[Diamandis 267- Anthropic vs Alibaba, OpenAI IPO Delays, US Govt Blocks GPT-5.6]]**
- 本文件论点：Anthropic 将策略层定义为更高 intelligence per dollar 的来源，best-of-n 等策略是第三根杠杆 [44:35]。
- 对方论点：Diamandis #267 中 GLM 5.2 + harness 在特定 SWE harness 下产生系统级能力信号，说明治理对象不能只看模型权重。
- 关联逻辑：#267 说明 harness 可以改变能力边界，本文说明 harness 也可以改变经济边界。把两者放在一起，AI 治理和采购都必须从“买哪个模型”升级为“允许什么 model+harness+tools 组合运行”。

### Taste 从评审输出上移到设计策略
**← [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]**
- 本文件论点：Anthropic 希望把 token jobs 和 strategies 做成可组合原语，让 agent 用反思、建议、评估等方式改善输出 [45:41]。
- 对方论点：Andrew 认为实现成本下降后，产品工作的稀缺点变成 taste：在大量原型中判断什么值得保留、合并和上线。
- 关联逻辑：Anthropic 的 strategy 层不会取消 taste，而是把 taste 的作用位置上移。人不再逐个评审每次输出，而是设计和选择哪些策略组合更可靠。产品判断从“这个结果好不好”迁移到“这个生成过程是否持续产出好结果”。

---

**元信息**

| 字段 | 值 |
|---|---|
| 标题 | Anthropic's Katelyn Lesse & Angela Jiang: Building an Ecosystem, not a Walled Garden |
| 频道 | Sequoia Capital |
| 发布时间 | 2026-07-14 |
| 时长 | 48min 55s |
| YouTube | https://www.youtube.com/watch?v=vPnVTHYplrQ |
| 分析时间 | 2026-07-22 |
