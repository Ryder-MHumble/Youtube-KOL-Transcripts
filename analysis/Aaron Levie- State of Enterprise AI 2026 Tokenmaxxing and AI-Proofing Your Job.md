---
title: "Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=Gs2styCcwro"
transcript: "[[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job 逐字稿]]"
tags:
  - kol情报
status: canonical
created: 2026-06-25
---

> 技术突破的速度已经超过客户的消化能力——这场 AI 落地之战的真正赌注不是模型够不够强，而是谁来把模型变成企业里真正能跑的工作流，以及在这条桥上谁能活下来。
> —— Aaron Levie, Box CEO, 2026

视频链接：https://www.youtube.com/watch?v=Gs2styCcwro
对应逐字稿：[[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job 逐字稿]]

**概述**：2026 年 5 月，FirstMark 的 MAD Podcast 邀请 Box CEO Aaron Levie 二度回归。对话者 Matt Turck（主持人 Aitor 代班）给 Levie 一个独特定位：一手是硅谷 agent-pilled 的信仰者，另一手是把产品卖给 P&G、Morgan Stanley、GE 这类 Global 2000 的上市公司 CEO。Levie 今年已经跟数百位 Fortune 500 CIO 聊过，这场 73 分钟对话的核心赌注是——当技术每 12 个月就翻新一次、客户连标准架构都还没搭稳，企业 AI 的真正瓶颈不在模型，而在**桥层**：数据、权限、预算、人才、工作流改造。Levie 把这场落地的真实时间线拉到了 10 年量级。

**主题脉络**：
1. 能力过剩反而拖慢落地——突破快于消化的悖论
2. Token 账单击穿旧定价模型——从 IT 预算到业务线预算的迁移
3. 编码 agent 能跑通、知识工作 agent 跑不通的五个结构性原因
4. 内部 FDE 与桥层岗位的兴起
5. Headless 不会消灭界面——双模式定价与 agent 座位问题
6. Jevons 悖论信徒——为什么 doomers 和 accelerationists 都错了

---

## 一、能力过剩反而拖慢落地——突破快于消化的悖论

Levie 开场就抛出了一个反直觉判断：技术进步不是在加速企业部署，而是在拖慢它。原因不是模型不够好，而是太好了——每一次突破都让上一轮刚刚铺好的架构变得过时，导致企业根本没有一个稳定环境可以 rollout。

> **[32:15]** "The problem is is the breakthroughs keep happening faster than the customer can implement any kind of standard architecture. And and those breakthroughs often times basically undo or make obsolete the last thing you implemented."

> **[32:37]** "the technology is getting so advanced that it makes obsolete the the prior thing that you implemented, which actually means that the rollout takes longer because we have no stable there's no stable environment to roll things out in."

这段话是整场访谈的底层操作系统。Levie 用 **capability overhang**（能力过剩）形容现状——如果今天把 GPT-5.5 或 Opus 的能力线固定在这里，整个生态两三年就能消化完。但模型不停往前跑，每个客户的 reference architecture 就不停被推翻。结果是 CIO 面对同一个客户入职审核问题，能拿到 10 到 15 套不同的参考架构方案，每家 lab、每家 startup、每家 workflow 厂商都在推销自己的版本：

> **[32:53]** "I could probably lay out up to 10 to 15 reference architectures to all solve that problem."

这直接导致销售周期拉长、决策复杂度上升，而不是缩短。一个配套信号：行业内现在没人愿意跟 lab 签超过一年的合约，因为下个季度的模型可能就把这一季的赌注清零了。

> **[34:05]** "one of the memes is nobody's signing up for more than like one-year deals with the labs. And and part of that is because of the the pace of innovation that's happening."

这条线索颠覆了硅谷的默认叙事。硅谷的逻辑是**模型越强 → 落地越快**，Levie 的田野观察给出的却是**模型越强 → 客户越无所适从 → 落地越慢**。这不是技术问题，是变革管理问题。被淘汰的不是落后企业，而是等模型稳定后再上车的等待心态——因为稳定永远不会来。

---

## 二、Token 账单击穿旧定价模型——从 IT 预算到业务线预算的迁移

从 [9:40] 开始，对话切入了 2026 年企业 AI 最烫手的话题：token 成本。Levie 给出的数字非常具体——在他与客户的对话中，token 成本和预算规划至少占 AI 相关最热议题的三分之一，有时甚至并列第一。

Levie 拒绝了行业一直在补贴这个流行解释。他承认早期 Cursor 这类产品确实把 token 用量打包进订阅费，但他认为真正的转折点是 agent 能力的跃迁：上下文窗口变大、参数变多、单任务可以烧掉上千美元的推理算力，旧的 20 美元/用户/月定价模型在物理上就不成立了。

> **[10:41]** "we've just gone from, you know, like the a pricing model of a chatbot or like type ahead functionality in get up co-pilot to a to that pricing model no longer working when when one, you know, agent could be consuming, you know, a thousand dollars of of compute on a single task."

> **[11:09]** "So, clearly like you can't lump that all into a twenty dollar per user per month fee."

更关键的是，前沿 token 的单价不降反升——这跟过去两三年硅谷反复讲的 token 成本永远下降叙事完全相反。Levie 的解释不是补贴退潮，而是结构性供需：硬件不便宜、算力短缺、数据中心和 lab 有定价权，10 年的 rollout 被压缩进 18 个月，所以看不到正常的成本下降曲线。

> **[12:13]** "the data center providers, the labs, etc. have pricing power. They they don't need to lower the prices on anything. So you're not seeing the the typical things that drive down the cost of compute."

但 Levie 把真正深远的判断留给了预算归属的迁移。他指出企业 IT 预算通常只占营收的 3-7%，而企业 60-80% 的营收消耗在 opex 上。AI 一旦真正带来生产力，就不可能被塞回 3-7% 的 IT 预算笼子里——它会溢出到市场、销售、制造等业务线预算里去。

> **[13:57]** "IT spend is basically somewhere between like three to seven percent of corporate revenue in a in a company."

> **[14:10]** "So then the question is like well where is the other 60 70 80% of of revenue in an organization? It's it's opex and it's just like general purpose opex across the business."

> **[14:10]** "It's going to it's going to escape that and it's going to move to the line of business budgets."

这带来一个全新的治理难题：市场团队没有 finops 能力，CMO 要在一百万美元算力和一百万美元线下活动之间做资源分配，财务、IT、业务线三方要重新博弈。Levie 直言目前没人有解决方案，并随手抛出一个 startup idea：AI compute 的 ERP。他甚至用了一个非常具象的类比来描述 ROI 测量的真空：

> **[16:10]** "there are some things I could do on my computer right now that would cost the same amount of money as as the lunch that my company provides me."

一个写错的 prompt 等于一个月的员工福利——这就是当下企业 AI 的成本不可见性。被淘汰的是 **per-seat 包打天下**的 SaaS 定价幻觉；正在兴起的是 seat + consumption 双轨制，以及围绕 token ROI 的一整层新软件品类。

---

## 三、编码 agent 能跑通、知识工作 agent 跑不通的五个结构性原因

这是整场访谈信息密度最高的一段（[23:36]–[28:13]）。Levie 把**为什么 Claude Code 能让工程师起飞、但同样的 agent 在市场部跑不动**拆成了五到六个结构性变量，而不是笼统归结为模型还不够好或人不会用。

**1. 用户类型不同**：编码 agent 的用户是技术人，agent 出错时用户自己能修；知识工作的用户不是。

> **[24:58]** "the moment the agent does something stupid or runs into a problem, the user themselves know how to go fix it and get it back on track."

**2. 模型在编码上被 hyper-trained**：代码是结构化、可验证的语言，模型在这上面的训练密度远超任何业务领域。

**3. 工作可验证性不同**：代码要么跑要么不跑，有测试和 QA；知识工作的产出没有这种二值校验。

**4. 上下文分布不同**：编码的上下文几乎全在代码库里，agent 可以一次性吃掉；知识工作的上下文散落在 20 个数字和非数字媒介里。

> **[25:26]** "the code base has so much of the context in coding, whereas in the rest of knowledge work, the context lives across like 20 different things, some digital and some very not digital, you know, kind of mediums."

**5. 权限模型不同**——Levie 反复强调这是最重要也最无聊的一条。工程团队通常对自己负责的代码块有完整访问权；知识工作里，Bob 总是有过多权限、Sally 总是有过少权限，agent 一接入要么撞 entitlement 墙、要么越权读取不该看的数据。

> **[25:50]** "you go to knowledge work and and like you constantly are running into either like, "Oh, like Bob actually had too much access to something." Or Sally had too little access to something."

Levie 把 chat 时代和 agent 时代做了一个干脆的对比：chat 只做两件事——检索 + LLM，两者都没有权限问题；agent 要接 MCP server、要拉 Salesforce 数据，**blast radius** 完全是另一个量级。

> **[27:50]** "chat chat was like basically it could do two things. It could it could access search and it could access the LLM. And that and that was amazing. And but guess what? Neither of those things has a permission problem."

这套分析的政策含义很硬：知识工作 agent 的瓶颈不在模型智商，而在企业 IT 的 **blocking and tackling**——数据治理、权限矩阵、工作流定义。这是 20-30 年没解决好的老问题，现在被 agent 重新逼到台面上。语义层即使被重新包装成 contextology，本质仍是那个 20 年的老问题。

---

## 四、内部 FDE 与桥层岗位的兴起

承接上一节的诊断，Levie 给出的解法不是等模型变好，而是催生一个新岗位——internal FDE（Field Deployment Engineer，现场部署工程师）。这个角色要懂业务流程、懂技术、能把 agent 焊接到具体工作流上，并且持续维护（因为模型一升级就要重做脚手架）。

> **[38:41]** "To do that, that's where the kind of internal FTE motion comes in."

> **[39:08]** "but I do think this is a highly technical skill. It's a highly technical role, which is do you have technical people in your organization that you can say, "I'm going to have you go sit next to the business or within the business"

Levie 对这个岗位的持久性给出了一个非常 Levie 式的论证：它既不证明技术不行（doomers 的胜利），也不证明落地失败（accelerationists 的耻辱），而是企业采用 agent 时必然出现的实施层——因为模型再强，它有固定内存、固定上下文窗口、固定数据访问边界，必须有人帮它把这些边界接上。

> **[42:51]** "It like has, you know, a fixed amount of memory. It has a fixed amount of context it can work with. It It couldn't do totally dramatically crazy stuff with your data. Like so obviously it has to be like implemented by somebody hyper technical."

这里有一个被低估的隐含立场：Levie 把 internal FDE 定位为**持续型岗位**而非一次性部署。他明确说模型每次升级都要重新校准——上一版模型留下的 scaffolding 可能要拆掉、新能力要不要吃掉、ROI 要不要重新测。这等于宣判了实施一次就完事的传统 SI 模式在 agent 时代失效。

他甚至把这个逻辑延伸到招聘市场：Caterpillar、Eli Lilly、John Deere 这类非硅谷大厂过去根本抢不到顶尖工程师，因为工程师都去了 Google/Meta。现在 agent 让一个工程师的产出乘以 3-10 倍，这些工业巨头终于有理由签下更大的技术项目，反过来推高了对工程产能的需求——而不是消灭它。

> **[53:43]** "for the first time ever one of their engineers now has the capacity of three or five or or 10 or whatever metric you want. And so that's going to get them to sign up for way bigger projects than they would have been able to afford, which means that that they now are that have a greater demand for that engineering capacity."

被淘汰的是 agent 让我们少招人的线性思维；正在兴起的是 **agent 让企业敢做以前做不起的项目，于是增加工程需求**的 Jevons 循环。

---

## 五、Headless 不会消灭界面——双模式定价与 agent 座位问题

当主持人问 headless 软件是否必然取代 GUI 时，Levie 给了一个反线性预测：headless 和界面会并存，因为每一种新媒介出现时人们都以为它会消灭前一种，但现实中不同终端会承担不同任务。

> **[43:49]** "you always think that the next medium fully eradicates the prior medium. And and then you just like you're like, "Oh, no, actually I do have an iPad and a MacBook and an iPhone.""

真正发生的是体量分化：复杂跨系统查询（Box + Salesforce + Workday 数据室）会 headless 跑在 Claude/Codex 里；精细操作（建数据室、调合同权限）还是 GUI 快。按调用量算，headless 会是界面的 100 倍，但人类仍会是 **end user seat**。

> **[44:50]** "by volume agents are going to be banging on these systems far more than humans ever did."

> **[45:15]** "The human will probably land as a an end user seat, um you know, within that that piece of software and they'll get a certain amount of allocation of usage as that end user seat."

这引出了 2026 年企业软件定价的核心新命题——Levie 预测三年内所有活过 AI 转型期的企业软件公司都会有两条收入线：seat 模型（给人）+ consumption 模型（给 agent）。两者谁大谁小取决于品类。他甚至提到已经有客户在讨论 agent 是否也需要 Box seat，因为 agent 需要有状态地存储和治理数据，需要一个身份——但不一定按人头的价格收。

> **[45:40]** "it will have a seat business model assuming it has an end user component, and it'll have a consumption business model. And that consumption business model in some business might be bigger than the seat model, and some might be smaller"

Levie 拒绝把 agent 简单等同于更高级的 API 调用或另一种人头。他明确说 agent 是否需要 seat 取决于用例——需要 stateful 身份和长期治理的，像人；只是高频操作的，纯 consumption。这个区分对 SaaS 公司的 GTM、对 CIO 的采购清单、对创业公司的定价设计都是直接的行动指令。

被淘汰的是纯 seat 或纯 consumption 的单一定价幻觉；正在兴起的是 seat + consumption 的混合定价层，以及 **agent 身份治理**这个全新品类。

---

## 六、Jevons 悖论信徒——为什么 doomers 和 accelerationists 都错了

访谈后半段进入就业辩论。Levie 自称是 **complete Jevons paradox pill person**——即技术降低某项工作的成本后，对该工作的总需求反而上升。他用了三个层次来论证为什么 AI 不会像 doomers 担心的那样消灭岗位，也不会像 accelerationists 宣称的那样一夜全员失业。

**第一层：编码的特殊性误导了外推**。编码有个独特属性：代码只要能运行并满足要求，10 万行还是 1000 行不构成同样的验证障碍。这让编码成为最适合放手给 agent 的场景。但法律不行——合同的 2004 条款不能被 agent 微调一下责任比例就发出去，最终还是要律师签字背书。

> **[50:20]** "if I write code and and it's like super sloppy because the agent is writing this code, it kind of at the end of the day doesn't matter short of like a a security risk or maybe like, you know, it's using extra memory that it shouldn't use or or whatnot. If the software just runs, like if it's like I could throw I could I could have you know, an application that has 100,000 lines of code or 1,000 lines of code if it's doing the thing that it needs to do, it really doesn't matter."
>
> **[51:04]** "In legal you you can't do that. I can't have online, you know, 2004 uh of the contract it it sort of like adjust the liability rate, you know, slightly cuz cuz I had an agent go and write this thing whole cloth."

这导致**最后一公里**的人类背书在法律、合规、医疗等大部分知识工作里不会被消灭，agent 消除的是一个瓶颈，但马上撞上下一个瓶颈。

**第二层：Jevons 悖论的真实案例**。Levie 援引 Financial Times 三周前一篇报道——律师被客户用 ChatGPT 生成的合同和问题淹没，反而更忙了。他自己也举了一个亲身经历：用 Perplexity Computer 跑了一个深夜项目，发现结果价值很高，但自己不愿持续操作，反而想雇人专门运行这些 agent。

> **[1:05:40]** "my conclusion was man, I don't ever want to do that again personally. I'd rather hire somebody to go do that for me."
>
> **[1:06:00]** "you should hire more people because you're like, oh my god, this thing is spitting out, you know, incredible gold mine of value, but who's going to go and run with that?"

**第三层：Adam Smith 没有过时**。Levie 直接回击了 PM 能写代码所以不需要工程师、工程师能写 spec 所以不需要 PM 这类合并论。他认为分工逻辑没有变——你不会想让销售顺手做线索挖掘，也不会想让 PM 顺手做设计。agent 改变的是分工的边界，不是分工本身。

> **[59:37]** "Adam Smith, you know, figured this out a long time ago. Like division of labor is like a really powerful thing. Agents haven't fundamentally changed the concept of division of labor."

这套论证的隐含立场很清晰：Levie 同时反对两个极端。doomers 把单个任务的自动化直接外推成整个岗位消失；accelerationists 把一人十倍产能直接外推成公司裁掉其余九人。Levie 的判断是，agent 先消除一个瓶颈，随后暴露下一个瓶颈；企业也会因为单位产能上升而承接更大的项目。被淘汰的是 **agent → 裁员**的线性因果；正在兴起的是 **agent → 解锁更大项目 → 反向扩张招聘**的 Jevons 循环。

---

## 七、对个人和企业的行动指令——以及 Levie 没说的

访谈最后 15 分钟，Levie 从宏观赌注转向个人行动。他给出了一个非常具体的清单：花 5-10% 的时间练工具、每月花 50-100 美元订阅 Codex/Co-work/Perplexity Computer/Cursor，并充分利用当前由风险资本补贴的低价工具。

> **[1:02:23]** "as an employee, I would be spending, you know, 5% of my time, 10% of my time, whatever you can kind of carve out of just getting really good at this stuff."
>
> **[1:04:47]** "Please use the VC subsidies to your advantage as much as possible."

他强调这不需要 **insanely high agency**，不需要是 YC 创业者——每个知识工作者都做得到。他还提出一个心智模型：把 agent 当成无限的 chief of staff，反问自己会把什么任务交给它，这能逼出工作流改造的灵感。

但更重要的是 Levie 在这里嵌入的一个隐含立场——他认为公司对员工负有**技能升级的社会契约**义务。这段话在 agent 时代的 CEO 访谈里相当少见：

> **[1:01:55]** "So I do think companies owe owe their employees and the future employees a real shot at upgrading their skills and upgrading their talent. So like some percentage of this is on the company themselves for the upskilling, for the training, for the enablement, for all of that."

他甚至把这个逻辑推到政治层面：如果不关心社会影响和就业端，就会出现政治反弹，因为社会运转良好的前提是人们愿意去公司上班、能养家，不能为了一个百分点的运营利润率破坏这个基础。

> **[1:01:55]** "society works really well when like people want to work at companies and and and they and they can, you know, they can feed their families and and and you don't want to blow that up just because you wanted like one extra point of of operating margin."

最后，关于创业公司机会，Levie 对最终所有人都会变成 OpenAI/Anthropic 的员工或服务商这个悲观论调给出了反驳。他认为 lab 不可能为每个垂直、每条业务线建几百上千人的实施团队，所以**桥层**——把模型能力接到具体业务工作流里的那一层——会长期存在创业机会。但他也承认 lab 和垂直应用之间的 **peace treaty**（势力划分）还没定型，lab 既想做应用层抢账户控制权、又要靠生态带来 inference 量，这个张力短期内不会消失。

> **[1:08:10]** "unless the labs build out literally the equivalent of hundreds or thousands of people for every single vertical and every single line of business that means that there's actually a lot of opportunity in that in that kind of bridge area of of the work."

Levie 没说但可以反推的：Box 自己就是这家桥层公司之一——他整场访谈都在论证桥层的必要性和持久性，这本身就是 Box 的战略叙事。他对 internal FDE、headless + seat 双轨、数据治理老问题新包装的强调，每一条都恰好指向 Box 的产品定位（API-first、内容治理、企业级权限）。这不是偏见，是利益对齐下的真知——但读的时候要知道发言人的位置。

---

## 深度关联
> 以下关联基于论点级分析：不是都提到了 AI，而是具体论点之间的逻辑关系。

### 集成墙从静态债务变成动态移动目标
**← [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]]**
- 本文件论点：模型突破持续使上一轮架构过时，企业没有稳定 rollout 环境，扩散速度反而下降（[32:15]-[34:05]）。
- 对方论点：AI 不会自动完成遗留系统集成，企业的权限、系统边界和组织流程构成 Agent 无法绕过的集成墙（[12:03]-[19:34]）。
- 关联逻辑：本篇把上一场访谈的静态诊断具体化为动态机制。旧系统债务并非只等待被清理；模型能力每次跃迁还会改写目标架构，使企业同时承担遗留集成和新范式迁移两种成本。internal FDE 因此不是临时补丁，而是长期吸收架构变化的组织角色。

### 系统思维是 internal FDE 的组织能力版本
**→ [[Elizabeth Stone- Netflix 的系统思维与 AI 组织操作系统]]**
- 本文件论点：知识工作 Agent 落地需要技术人员贴近业务，理解流程、数据、权限和 human-in-the-loop，再把模型能力接入真实工作（[38:41]-[41:20]）。
- 对方论点：AI 带来的角色混乱只是 storming phase；Netflix 需要 systems thinkers、source of truth、guardrails 和责任归属把跨职能速度重新收束（[3:47]-[11:40]）。
- 关联逻辑：Levie 描述的是岗位形态，Stone 描述的是组织能力。internal FDE 如果只是会接 API 的工程师，会复刻旧式实施团队；只有具备系统思维、能识别责任和质量边界的人，才能把局部 Agent 自动化变成可扩展的组织能力。

### 实现成本下降把预算和判断同时推到前台
**→ [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]**
- 本文件论点：Agent 可以在单任务中消耗上千美元算力，企业必须从统一 seat 预算转向按业务价值分配 compute，并建立 token ROI 管理（[9:55]-[17:21]）。
- 对方论点：实现已经不再是产品工作的昂贵部分，真正稀缺的是从大量可实现方案中筛选什么值得做（[4:48]-[9:51]）。
- 关联逻辑：Andrew 解释了供给侧变化，Levie 补上企业资源配置后果。当实现变得充足，组织不能再用能否做出来作为立项门槛；计算预算必须与 taste、业务判断和责任绑定，否则低成本生成会转化为高成本推理和更大的治理负担。

---

**元信息**

| 字段 | 值 |
|------|-----|
| 标题 | State of Enterprise AI 2026: Aaron Levie on Tokenmaxxing, Rise of Headless, and AI-Proofing Your Job |
| 频道 | The MAD Podcast with Matt Turck |
| 发布日期 | 2026-05-28 |
| 时长 | 73min |
| YouTube链接 | https://www.youtube.com/watch?v=Gs2styCcwro |
| 分析时间 | 2026-06-25 |
