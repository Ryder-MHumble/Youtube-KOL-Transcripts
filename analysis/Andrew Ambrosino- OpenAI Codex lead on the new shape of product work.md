---
title: "Andrew Ambrosino- OpenAI Codex lead on the new shape of product work"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=P3KDebPTUrw"
transcript: "[[Andrew Ambrosino- Why OpenAI is merging Codex and ChatGPT and the future of knowledge work]]"
tags:
  - kol情报
status: canonical
created: 2026-07-21
---

> Andrew Ambrosino 的核心判断是：AI 没有让产品工作消失，而是把产品工作从“争取实现资源”倒置成“在无限实现里筛选信号”；实现变便宜后，taste、模型时机、过程分层和工具编排成为新的稀缺能力。

对应逐字稿：[[Andrew Ambrosino- Why OpenAI is merging Codex and ChatGPT and the future of knowledge work]]

视频链接：https://www.youtube.com/watch?v=P3KDebPTUrw

## 概述

这场访谈不是 Codex 的产品宣传，而是 OpenAI 内部产品工作方式变化的一次外泄。Andrew 的位置很特殊：他领导 Codex desktop app，同时经历过设计、工程、产品和创业。他看到的不是“PM 会不会被 AI 替代”，而是产品组织的成本结构已经倒置。

过去实现昂贵，所以产品团队用 PRD、研究、设计稿和原型去降低实现风险。现在实现本身可以由很多人快速完成，甚至同一个功能会出现九十个未协调探索。瓶颈因此从“能不能做”迁移到“哪个探索值得存在、如何组合、什么时候发布、该用什么媒介表达”。

这对个人工作也很直接：会写代码不等于会做产品，会生成原型不等于有判断。AI 时代真正被放大的不是低质量执行，而是高 agency + high taste 的人，他们能把想法从模糊状态带到可交付状态，并知道什么时候不该交付。

## 实现成本下降后，产品流程被倒置

Andrew 用“backwards”描述产品流程的变化。传统流程假设实现昂贵，因此先用文档、研究和原型压低风险；但现在任何人都能快速做出功能探索，组织面对的是过量实现，而不是实现稀缺。

> **[3:15]** "building these products is just sort of the inversion of the process in my mind which I think a lot of people have talked about which is that anybody can build anything right like I I generally believe now that starting from scratch if you talk to these models ours anybody else's really um you can stand up whatever feature you want right"

> **[4:13]** "when we got past waterfall it was still kind of flavored of like the implementation is expensive and so you what you want to do is you want to derisk all implementation up front through documents through research through prototypes because prototypes and designs are cheaper was kind of the the assumption there uh and that's changed that's like totally changed and right now I'm sure there are 90 different explorations for there's this"

> **[4:48]** "Um, so I guess the short answer is like it's it's backwards and it's not that people are doing fundamentally different roles or focusing on different things or that even skill sets have vanished or that roles have just disappeared. It's that it's backwards, right? The implementation is actually not the expensive part anymore. It's dare I say taste."

“Taste” 在这里不是审美偏好，而是筛选能力：九十个探索里哪些有信号、哪些该合并、哪些只是噪声，某个交互应该归入哪个产品主题。

> **[5:08]** "It's like of those 90 attempts like what's good about these? What should we fold into other aspects of this? Right?"

这就是 AI 产品组织的新瓶颈：不是生成方案，而是建立筛选方案的机制。对于 PM 来说，价值不再是写出一份完整需求，而是能在大量几乎可运行的候选实现里判断哪个方向值得继续。

## 文档没有死，媒介选择本身变成产品判断

Andrew 明确反对“PRD 已死，全部原型化”的口号。他的判断更细：当实现变得便宜，团队更容易拿到过早看起来像产品的东西；这会让组织误以为探索已经成熟。

> **[7:06]** "There's a lot of this um and you know it's not just happening here like you've seen many product leaders say PRDS are dead prototypes are in and I actually don't believe this at all."

> **[7:53]** "Um, this is no shade on people writing documents. It's that if implementation is abundant, then it's really important to pick the right format for the point you're trying to make. If that point is product clarity around a vague area, then it might actually be a document. If what you're trying to do is get something in people's hands to try out and to stress test an interaction pattern, it's a prototype."

旧流程里，媒介本身带有阶段信号：生产级界面意味着假设已被验证。现在这个信号失效，因为早期探索也可以长得很像 production。

> **[9:24]** "it's late in the process that assumptions have been derisked that you know design is looked at this that this is a good business goal right and now those things are sort of divorced right and the reason it was that way is because it was hard to get resources to build the thing until it was properly derised and now that's like just out the window right"

因此，AI 时代的产品流程不是抛弃文档或原型，而是明确每个 artifact 的阶段属性：这是用来澄清问题、测试交互、验证模型能力，还是准备上线？如果团队不标注阶段，漂亮原型会制造错误共识。

## AI 不擅长设计，因为设计反馈更难评分

Andrew 对 AI 设计能力的解释不是“模型审美差”，而是反馈回路更难自动化。代码可以编译、测试、运行；设计需要人的 taste 参与评分。

> **[0:36]** "I think design's a little bit harder to grade because the human aspect of taste is like part of the feedback mechanism you need. That is still feeling a little bit out of reach with the current technology."

他进一步指出，设计还需要新颖性。软件工程通常希望复用已知模式，设计如果每次都生成 Linear 风格翻版，就没有真正解决问题。

> **[14:25]** "linear's website every time that's not the challenge here right um there's 's an amount of like novelty that is more important in design than it actually is in software engineering. Like software engineering, you almost you almost want it to overindex unknown patterns, right?"

更深一层的问题是语义抽象。好的设计不是把 263 个组件逐个改样式，而是理解哪些元素虽然长得不同，却在系统里承担同一种语义。

> **[15:28]** "The shallow version of this is that we have to you know update 263 components one by one. The deep version is like the semantics between these two things that look different like they're both in list that have the like this style that convey this interaction pattern to the user and I think like that is still feeling a little bit out out of reach with the current technology right that abstraction layer."

这意味着设计不会因为生成能力增强而消失。AI 会降低第一稿成本，但验证、语义归纳和新颖性判断仍是人的高价值工作。

## Design process 不是死亡，而是和媒介解绑

Andrew 同意传统“设计流程教条”会死，但反对把流程意识一起扔掉。旧流程绑定了固定媒介：研究、发散、收敛、原型、实现。现在实现本身也能被拉进早期探索，所以流程必须从工具步骤变成阶段判断。

> **[18:31]** "And like once again, like that process is sort of predicated on the assumption that implementation is expensive and that you can really only afford to build once. And so you need to fully like exhaustively go through the problem space and the solution space before implementing, right?"

> **[19:20]** "We pulled prototyping into that. The problem now is that you can pull all of the implementation into that."

> **[20:48]** "It's that if you are if you are tied to the tools in the ex like the spec the exact like day-to-day specifics of the process then yeah it's dead like you're not going to have a good time but to throw the process out completely or throw like the overlay of the process the like hey we're at this point in the process like that is still more important than ever"

这段对 PM/设计/工程都很重要。AI 没有取消 process，它取消的是把 process 等同于某套工具动作。真正要保留的是：团队知道自己处在探索、验证、收敛还是上线阶段。

## 角色会重叠，但专业不能被删除

OpenAI Codex 组织确实出现了 role collapse：设计师写代码，PM 懂技术，工程师参与产品判断。但 Andrew 反对把这解释成“角色消失”。

> **[21:38]** "Yeah, there's been a lot written about ro collapse, existential role collapse."

> **[22:13]** "Like, so we've seen a lot of role collapse and and I think that, you know, one of one of the ways that we describe how the groups work together is that there's significantly more overlap in the roles than there used to be."

他的核心警告是：如果取消角色概念，可能连每个专业积累的 best practices 也一起删掉。会写代码的人不自动懂产品，会用 Excel 的人不自动能做财务。

> **[24:52]** "And I think part of the danger in eliminating the concept of roles is that it can dangerously eliminate the idea that things are specialties with knowable best practices, right? I I've heard a lot of companies be like, we're getting rid of the product role, which I think is, by the way, a terrible idea."

> **[26:15]** "It's like no that's not how it works, right? Um like yes, you can use Excel you but you cannot work on the finance team, right? That is like that kind of stuff, right?"

更合理的变化是：边界变软，专业还在。过去一些工具熟练度构成的门槛会被侵蚀，但领域判断、流程经验和问题框架仍然有价值。

> **[27:05]** "And it's like there have always been parts of these roles that are that sort of gatekeeping that are like, well, no, this like being good at this role is being good at this tool. And I think that's what's kind of starting to erode."

对组织设计的含义是：招聘不该只找“会用 AI 的通才”，而要找能跨边界工作、但仍尊重专业深度的人。

## 高 agency + high taste 成为新型 IC/Manager 混合能力

Andrew 对 Codex 团队的人才画像很明确：agency 和 taste。团队需要能从 idea 到 done 的人，但“done”不是把代码写完，而是能在无限 token 环境里识别信号与噪声。

> **[28:22]** "everybody on the codics side or or on the desktop side is agency and taste right a lot of former founders or people who were at larger companies doing founder shaped things"

他对 IC/manager 的分界也做了新解释：IC 不再只是逐字符写代码，而是在管理 agent 和工作流；manager 也在做类似的管理，只是粒度不同。

> **[30:40]** "Yeah, I think that that's that's the core piece right now. And it it also speaks to how I sort of see IC versus management, which is that it's not that management is going away. It's not that everyone's an IC, but like everyone's kind of both now, right?"

> **[30:56]** "If you're an IC, you're not typing code out character by character, right? like you are managing something you're managing agents you're managing you know like you're managing work that is happening right that comes together to do a certain thing"

这提示了一个更现实的人才标准：未来的高价值个体不是“会亲自做所有事”，而是能有效管理智能劳动力，并对结果有足够 taste 做判断。

## 模型时机成为产品变量

Andrew 对 roadmap 的判断很现实：短期要细，九个月计划必须模糊，因为精确计划会变成 false precision。AI 产品规划必须把模型能力曲线纳入判断。

> **[32:11]** "And then it's not that we don't plan for 9 months out, it's that that just has to stay very hazy because any amount of precision that you add to a 9-month plan right now is false precision."

他给出最重要的产品案例：Codex app 的形态如果在 2025 年 11 月发布会失败，2026 年 2 月发布却成立，唯一差异是模型能力。

> **[33:01]** "It basically had to be like, let's list out all of the things that we think we are interested in doing for the next year or two. Let's prototype all of them, decide which things are ready now, and then just let the others sit and bake, and then every time there's like a new leap in models, let's try that thing again with it swapped out."

> **[33:31]** "So this is a great story about the Codex app. I like I am very confident that the Codex app that we released in February, if that had been ready in November, it would have absolutely failed in the market and that that the only difference was the models between November and February, right?"

这对 AI 产品管理是范式变化：一个功能失败，未必说明需求错或交互错，可能只是模型时机不对。正确动作不是删掉，而是保留 artifact，等待模型跃迁后重测。

## 太 AGI-pilled 会让产品形态早产

Andrew 反思 Codex web 的早期形态时说，云端委托任务的想法并不荒谬，但当时模型还不足以支撑这个承诺。Claude Code 更本地、更互动、没假装能接管一切，反而更符合当时模型能力。

> **[35:39]** "Yeah, I think we have a lot of that. I think sometimes the challenge is like you have to be very clear again about what stage of the design process that's in. People still have this muscle memory of like, oh, I wrote the code for this thing, therefore we should put it out there. It's like, no, no, no, that means you have an artifact now that we can test against for into future models, right?"

> **[36:35]** "Um there's also this aspect of especially in research there's always a desire to be the most ambitious and to say okay but at the limit the model can just do this and it just doesn't work on the product side"

> **[37:31]** "So we were like we were too agi pilled for the moment. And I think like I I think about that lesson a lot on this stuff."

这里的洞察非常实用：AI 产品要同时管理两种失败。太保守，会错过模型跃迁；太 AGI-pilled，会把未来能力包装成当前承诺。优秀产品团队必须找到“模型当前可靠性”与“用户能接受的 agency”之间的边界。

## 自主开发仍卡在复杂性熵增

Andrew 对“AI 写了多少代码”这个问题的回答很锋利：按去年标准，今天 100% 都可以是 AI 写的；真正的问题是监督还是非监督、能否长期维护。

> **[40:11]** "Um, you know, one of the big questions is always, well, how much of the product is AI written? And it's always hard to answer that question cuz if you're using the goalposts from last year, it's like, well, 100% of our product right now is AI written code."

但他也指出当前模型会系统性增加复杂性。全自动开发的瓶颈不是能否写代码，而是能否删除代码、建立正确抽象、知道哪些 feature request 不该做。

> **[40:38]** "There have been a lot of explorations here around like autonomous autonomously developed software. um a lot of like harness engineering stuff, a lot of different explorations. I'm like, okay, well, what if you came in overnight and did garbage collection of the codebase to clean it up, right? One thing that I think all models suffer with right now is just they they usually increase complexity. If research is listening at any company, please make the models better at deleting code."

> **[41:04]** "Um but you know, that becomes a problem right now when you try to put development completely on autopilot. Um, and it's both on the the human side and the codebase side. So like feature requests, right? You know, how do you teach a model which features to build, which ones to ignore, which ones to kind of like group together and reframe a little bit? How do you teach a model how to build the right abstractions, right?"

这和 Aaron Levie/Casado 的“AI 代码会劣化，审查是熵减机制”形成强关联。AI 让产出变多，复杂性也变多；人类判断从“写代码”迁移到“控制复杂性增长”。

## Codex 的野心是工作 home base，而不是 IDE

Andrew 对 Codex 愿景的描述很关键：它从 developer tool 起步，但 OpenAI 内部很快发现 marketing、comms、finance、legal 等非工程团队也在用 Codex，尽管界面对他们并不友好。更奇怪的是，当团队尝试把 Codex 能力放进更适合这些 persona 的其他 surface 时，用户仍不愿离开 Codex app。

> **[53:25]** "from marketing from comms from finance from legal from basically every discipline who are using this codeex app even though it is actively hostile to these people right it is like trying to show them code it's trying to ask for approval to run RG on the you know it's like it's doing all of these things that are actively not the right product surface for them."

> **[53:54]** "And those efforts went for a little bit and the the most annoying problem happened which is nobody would leave the Codex app for the apps that were allegedly for these other personas."

Andrew 给出的方向不是把所有 SaaS 重做在一个矩形窗口里，而是让 Codex 成为开始工作、结束工作、自动化工作、调用外部工具的 home。

> **[56:23]** "I think what we see here is that it's a great home base. It's a great place to keep track of all of the things that you have to do across different surfaces and some of those things you do all of it in the app."

> **[57:03]** "And so it's not just about, hey, we're drawing a rectangle on the screen and everything needs to happen in that rectangle. It's this thing should be a home for you where you start work, you end work, you automate work, and it uses whatever you need to do."

Premiere Pro 案例说明了这个平台野心：Codex 不需要自己成为视频编辑器，它可以理解外部专业工具，并在必要时为工具写扩展。

> **[58:01]** "It could do some edits by editing the files that were backing what was on screen in Premiere Pro, but it couldn't do everything. So naturally, what Codex then did was built itself an extension that could be installed into Premiere Pro that it could then talk to and say, "Hey, Premiere Pro extension, can you please change this marker inside of the Premiere Pro app." That was pretty nuts when we saw that happening."

这就是应用层价值捕获的新候选：不是替代每个工具，而是成为所有工具的编排入口。用户不再逐个打开 SaaS，而是在一个 home base 中发起任务，由 agent 决定使用 connector、browser、computer use 还是扩展。

## 关键判断

- AI 没有取消产品工作，而是把产品工作从实现前置验证倒置成过量实现后的筛选与组合。
- 文档和原型都没有死；真正重要的是选择正确媒介，并标注 artifact 处于哪个产品阶段。
- Taste 是验证能力，不只是审美；它包括系统位置、交互语义、业务目标和上线时机。
- 角色边界会软化，但专业不会消失；删除 PM/设计/工程 discipline 会误删长期积累的 best practices。
- AI 产品的成败高度依赖模型时机，同一形态可能在 11 月失败、2 月成立。
- 全自主开发仍受制于复杂性熵增；模型会写代码，但还不擅长删除代码、忽略需求、重构抽象。
- Codex 的平台方向是 work home base：编排现有工具，而不是重造所有专业工具。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Taste 是验证瓶颈在产品组织里的名字
**← [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]**
- 本文件论点：Andrew 认为实现不再昂贵，真正稀缺的是在 90 个探索中判断什么值得合并、保留和上线 [5:08]。
- 对方论点：Ilya 认为模型 eval 高分和真实任务表现之间有裂缝，核心问题是泛化不足和中间价值判断缺失。
- 关联逻辑：Ilya 讲的是模型训练层的价值函数，Andrew 讲的是产品组织层的价值函数。生成越便宜，越需要一个判断系统告诉团队哪些路径值得继续；taste 就是产品团队对抗过量生成的价值函数。

### 第一稿商品化后，价值迁移到选择与推进
**→ [[Dylan Field- Why the Figma CEO Isn't Worried About AI Taking Design Jobs]]**
- 本文件论点：Andrew 认为原型和实现都可以在早期大量出现，产品团队需要判断阶段、媒介和系统语义 [7:53]。
- 对方论点：Dylan Field 认为 AI 商品化第一稿，但不会扩大人的注意力；设计价值迁移到筛选、推进和决定什么值得继续。
- 关联逻辑：两者都反对“生成能力=专业消失”。Field 从设计协作层说明第一稿不再稀缺，Andrew 从 Codex 团队实践说明实现也不再稀缺。共同结论是：专业价值迁移到选择、编辑、组合和最终责任。

### AI 代码生产力被复杂性熵增反向约束
**← [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]]**
- 本文件论点：Andrew 观察到模型通常增加代码复杂性，请求研究界让模型更擅长删除代码 [40:38]。
- 对方论点：Levie/Casado 认为 AI 代码会随时间劣化，引入的问题和解决的一样多，大企业仍被安全审查和约束流程限速。
- 关联逻辑：Andrew 给出 OpenAI 内部产品实践，Levie/Casado 给出企业系统约束。两者合并后，AI 编码的真实瓶颈不是“能不能写”，而是“写出来后系统复杂度是否可控”；审查、删除、抽象和忽略需求成为新的工程核心。

### Codex home base 是应用层重新收水费的候选答案
**← [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Andrew 认为 Codex 应成为用户开始、结束、自动化工作并调用外部工具的 home base [57:03]。
- 对方论点：Evans 认为模型层像电信运营商，流量暴涨但定价权可能被应用层捕获。
- 关联逻辑：Codex home base 给出了 Evans 问题的一个具体答案：收水费的不一定是模型 API，也不一定是单个 SaaS，而可能是控制任务入口、上下文、工具调用和自动化编排的桌面 agent。它通过中介化现有工具获得应用层定价权。

### Strategy layer 与 work home base 是同一平台化方向的两面
**→ [[Anthropic平台生态 - Lesse & Jiang - Sequoia 2026]]**
- 本文件论点：Codex 不重造 Premiere Pro，而是能操作文件、使用外部工具，甚至为 Premiere 写扩展 [58:01]。
- 对方论点：Anthropic 平台把 agent 栈分为 knowledge、execution、coordination，真正价值在 coordination/strategy layer 和 token jobs。
- 关联逻辑：Andrew 描述的是最终用户侧的 home base，Anthropic 描述的是开发者侧的 strategy layer。前者控制任务入口和工具编排，后者控制 agent 如何分配 token 与执行策略。两者共同指向：未来平台护城河不是单一应用，而是“任务入口 + 策略编排 + 外部工具执行”的组合。

---

**元信息**

| 字段 | 值 |
|---|---|
| 标题 | Why OpenAI is merging Codex and ChatGPT and the future of knowledge work |
| 频道 | Lenny's Podcast |
| 发布时间 | 2026-06-28 |
| 时长 | 1:09:49 |
| 对话者 | Andrew Ambrosino，Lenny Rachitsky |
| 分析时间 | 2026-07-22 |
