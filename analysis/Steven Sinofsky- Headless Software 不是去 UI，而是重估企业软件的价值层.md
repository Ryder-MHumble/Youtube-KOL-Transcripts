---
title: "Steven Sinofsky- Headless Software 不是去 UI，而是重估企业软件的价值层"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=Mxs4erDxOEE"
transcript: "[[The New Rules of Enterprise Software with Steven Sinofsky]]"
tags:
  - kol情报
status: canonical
---

> Sinofsky 与 a16z 这场讨论的核心不是“企业软件 UI 会消失”，而是 agent 迫使我们重新区分企业软件的三层价值：UI 捕获人类工作流，system of record 承载业务逻辑和权限，真正的新机会来自把组织里过去无法相互沟通的功能、文档和例外决策连接起来。

视频链接：https://www.youtube.com/watch?v=Mxs4erDxOEE

对应逐字稿：[[The New Rules of Enterprise Software with Steven Sinofsky]]

## 核心证据校准

> **[0:06]** "The data, the logic, everything stored below it is really where the value is."

> **[0:12]** "you could vibe code your way into enterprise software"

> **[0:31]** "Postgress database and APIs and then bam like you can replace SAP"

> **[2:34]** "traditional software had been built around humans accessing it"

> **[4:08]** "how they build themselves for the agentic world"

> **[5:40]** "how agents um access systems of record"

> **[8:18]** "you have to be impersonating a specific person"

> **[10:10]** "undocumented like you know what we call SOPs"

> **[11:53]** "the most sticky thing you could do is actually collect money from a customer"

> **[13:53]** "General Motors isn't going to displace like 600,000 seats because of the calendar"

> **[18:14]** "customized to the way that business actually operates"

> **[21:15]** "the difference between Ford and Toyota and General Motors and Daimler"

> **[21:56]** "We make more money from Excel than you do."

> **[25:52]** "the two most frequently used features exist in no enterprise software natively"

> **[27:11]** "ad hoc business processes are the ones that really become the most interesting"

> **[33:03]** "you can't even explain the process that you use to resolve a customer issue"

> **[35:13]** "permissioning is part of this"

> **[38:03]** "the long tail got no shorter"

> **[42:19]** "there's no API for that"

> **[44:08]** "expertise exists in this cloud in an organization"

> **[51:51]** "create a new system of record"

> **[59:42]** "a tool that enables two functions to talk together that couldn't before is golden"

## 概述

这场 a16z 对话围绕 Salesforce “Headless 360”展开，但真正有价值的不是 Salesforce 这次发布本身。Sema Amble 一开始就把它降级为“marketing announcement more than anything else”，更大的信号是：agent 正在改变企业软件被访问、被收费、被替换和被创业公司攻击的方式。

Sinofsky 的核心贡献是拆掉两个过度简化的判断。第一，不要以为企业软件就是数据库 + API。SAP、Salesforce、Outlook、Excel 的粘性来自业务逻辑、权限、例外处理、组织习惯和外部依赖，而不只是数据。第二，不要以为 agent 会让企业软件 UI 失去价值。UI 过去之所以粘，是因为它捕获了读写频率、肌肉记忆、SOP 和上下游流程；agent 出现后，UI 的相对价值会下降，但底层 system of record 和组织逻辑的价值会上升。

这篇适合放进“企业 AI 集成鸿沟”和“价值捕获层级”两条主线。它补充了 Benedict Evans 的问题：“模型商品化后，水费归谁收？”Sinofsky 的答案更企业级：水费不一定归最漂亮的界面收，而归掌握业务逻辑、例外、权限和跨部门连接的人收。

## Headless 不是无界面，而是 agent 改变访问路径

Sema 对 headless software 的定义很克制。她不是说 UI 消失，而是说企业软件过去围绕人类访问来设计：人用 workflow 输入数据、读取信息、触发动作。agent 出现后，访问路径发生变化。

> **[2:34]** "traditional software had been built around humans accessing it"

如果 agent 要访问 CRM 数据，它走 UI 还是 API？Salesforce 的 Headless 360 至少承认了这个变化：

> **[4:08]** "how they build themselves for the agentic world"

但这不等于传统 SaaS 一夜之间被替换。更准确的变化是：系统会分层。上层 workflow/UI 可能被 agent 部分绕过；下层 data、logic、permissions、audit trail 和 business rules 反而更重要。

> **[0:06]** "The data, the logic, everything stored below it is really where the value is."

所以，headless 的核心不是“没有头”，而是“头不再只能是人类 UI”。未来企业软件可能同时服务三类访问者：人、agent、其他系统。产品设计要从“让用户点击得更顺”扩展为“让不同主体以不同权限读、写、分析和解释同一套业务事实”。

## 不能用 Postgres + API 替代 SAP：业务逻辑不是数据表

这场讨论最直接打击的是 vibe coding 式企业软件替代论。

> **[0:12]** "you could vibe code your way into enterprise software"

Sinofsky 和 Sema 都反对这种低估。Sema 直接点名一种创业公司错觉：把 SAP 想象成 Postgres 数据库加一层 API。

> **[0:31]** "Postgress database and APIs and then bam like you can replace SAP"

问题在于，SAP 里封装的是业务如何真实运行。实施多年不是因为系统集成商慢，而是因为每个企业把采购、制造、库存、财务、权限和审批都按自己的方式嵌进去。

> **[18:14]** "customized to the way that business actually operates"

Sinofsky 用汽车行业说明这一点。Ford、Toyota、GM、Daimler 都在造车，都买钢、铝、线束、仪表盘和收音机，但它们的企业软件配置不同，因为它们选择了不同屏幕、不同流程和不同定制。

> **[21:15]** "the difference between Ford and Toyota and General Motors and Daimler"

这意味着“替代企业软件”的难点不是把数据迁出来，而是重建企业自己的操作语义。AI 可以更快写代码，但不能自动知道哪条流程是制度要求，哪条流程是历史包袱，哪条流程是某个关键客户的隐性例外。

## 企业软件粘性来自未文档化流程、收费关系和意外功能

Sema 解释企业软件粘性时，先提到 UI 频率、读写次数、下游工作流和 SOP：

> **[10:10]** "undocumented like you know what we call SOPs"

这比“用户习惯”更深。SOP 很多时候不是正式文档，而是部门间多年形成的操作约定。系统替换会同时破坏销售、财务、市场、客服、外部合作方的接口。

Sinofsky 补了一条更现实的粘性：收钱。

> **[11:53]** "the most sticky thing you could do is actually collect money from a customer"

只要软件已经在收钱，它就嵌入了采购、预算、合规和业务连续性。停止付款不是按下取消按钮，而是重新回答“停了以后谁负责、用什么替代、出了问题谁解释”。

他还用 Outlook Calendar 的例子说明，企业软件的护城河常常来自产品团队当初没意识到的功能：

> **[13:53]** "General Motors isn't going to displace like 600,000 seats because of the calendar"

这对 AI 创业公司是警告：不要只攻击 incumbent 的主叙事功能。真正让客户不敢替换的，可能是一个高频小功能、一组例外流程、一个导出按钮、一个外部审计链路，甚至是某个 VP 上任后默认要求的工具栈。

## Excel 是企业 AI 的原型：逃生口会长成下一代系统

整场最有迁移价值的历史类比是 Excel。Sinofsky 回忆推广 Excel 时，Goldman Sachs 的银行家说：

> **[21:56]** "We make more money from Excel than you do."

这句话说明，供应商卖的是通用工具，客户真正创造价值的是自己的应用。Goldman 的 Excel 不是简单表格，而是模型、插件、流程、判断和交易能力的载体。

这也解释了为什么企业软件最常用的功能往往不是系统原生能力，而是导出。

> **[25:52]** "the two most frequently used features exist in no enterprise software natively"

导出到 Excel、CSV、PDF 是 escape valve。它允许业务人员把系统无法表达的分析和流程带到另一个更灵活的环境里完成。过去 escape valve 通常停在个人/小团队层面；AI 出现后，这些 ad hoc process 有机会被重新观察、自动化、产品化。

> **[27:11]** "ad hoc business processes are the ones that really become the most interesting"

这给创业机会一个清晰方向：不要只去替代大系统，而要看大系统边缘有哪些反复导出的文件、手工拼接的表格、跨部门邮件和无法被原系统表达的决策。那往往是下一代 vertical workflow 的入口。

## 例外处理不是长尾杂务，而是企业本身

对 agent 来说，真正困难的不只是读数据，而是写入系统、修改状态、处理例外。Sema 在“do something”层面点出权限问题：

> **[8:18]** "you have to be impersonating a specific person"

一旦 agent 要修改 system of record，就必须回答：它代表谁？用谁的凭证？是否算一个 paid seat？能读什么、写什么、审批什么？这些不是 API 设计细节，而是企业治理结构。

Sinofsky 进一步说，很多业务流程连当事人自己都说不清。

> **[33:03]** "you can't even explain the process that you use to resolve a customer issue"

这不是员工能力差，而是例外处理本身就是经验、政策、历史承诺和组织判断的混合物。自动化一个流程后，新流程会产生新的例外，所以：

> **[38:03]** "the long tail got no shorter"

最尖锐的一句在 [42:19]。Sinofsky 说开发者不会认为修不修 bug 这种需要多人共识的事情应该有 API，却会轻易认为关账、收入确认、客户退款这些业务流程应该被 API 化。

> **[42:19]** "there's no API for that"

这里的深层判断是：企业不是一组可调用函数，而是一群人在不完整信息下做可解释决定。AI 可以辅助、记录、建议、执行部分步骤，但不能假装所有组织判断都有一个纯技术接口。

## 新机会：连接过去不能互相沟通的组织功能

Sinofsky 与 Sema 最后把机会落到“桥接”。企业里有大量 Word、Excel、PPT、邮件、会议、录音、转录和文档，它们包含组织 expertise，但难以判断哪个可信、哪个重要、哪个仍在被使用。

> **[44:08]** "expertise exists in this cloud in an organization"

Sema 认为 AI startup 可能先通过观察业务运行，创建新的 system of record：

> **[51:51]** "create a new system of record"

Sinofsky 则把最大机会定义为连接两个原本不能沟通的功能：

> **[59:42]** "a tool that enables two functions to talk together that couldn't before is golden"

这比“AI 替代 Salesforce/SAP”更务实。创业公司不必一开始替换整个后端系统，而可以先成为跨职能桥层：销售与财务、产品与设计、客服与工程、采购与合规、IT 与预算。只要它能把原先靠 Accenture、人肉 CSV 和会议协调的流程变成可追踪、可审计、可执行的系统，就有机会长出新的 system of record。

## 关键判断

- Headless software 不是 UI 消失，而是企业软件从只服务人类点击，转向同时服务人、agent 和系统调用。
- 企业软件的价值不只是数据表，而是业务逻辑、权限、例外、审计、收费关系和组织 SOP 的总和。
- “Postgres + API 替代 SAP”是典型 startup-scale 错觉；真正困难的是重建企业如何运行的语义。
- Excel/CSV/PDF 导出是企业系统的 escape valve；这些反复出现的 ad hoc process 是下一代 AI vertical workflow 的高价值入口。
- Agent 写入 system of record 的首要问题是身份和权限：它代表谁、能写什么、是否算 seat、如何审计。
- 自动化不会消灭长尾，长尾会换形态继续增长；例外处理本身就是企业价值的重要部分。
- 新创业机会更可能来自跨职能桥层，而不是正面替换 SAP/Salesforce。

## 对个人 IP / 产品情报的启发

这篇可以作为判断企业 AI 产品的“反 demo 模版”。以后看到声称“用 agent 替代 CRM/ERP/企业 SaaS”的项目，第一反应不应是看 UI 或生成能力，而是问：

- 它是否理解 system of record 里的业务逻辑，而不只是数据结构；
- 它是否有读/写/审批/审计/回滚的权限模型；
- 它是否处理了导出到 Excel 后的真实工作流；
- 它是否能把跨部门决策变成可解释状态，而不是强行 API 化；
- 它是否能从桥层逐步长成新的记录系统。

这比“AI 原生 SaaS 会不会取代旧 SaaS”更能筛出靠谱项目。

## 深度关联

> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Evans 提出价值上移问题，Sinofsky 给出企业层答案
**← [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Sinofsky/Sema 认为 headless 后真正有价值的是 data、logic、system of record、权限和例外处理，而不是可被 agent 绕过的表层 workflow UI [0:06, 2:34-5:40]。
- 对方论点：Evans 认为基础模型可能商品化，价值会逃向上层应用，但 Chatbot 只是有限 V1 UI，真正价值在领域工作流和例外处理。
- 关联逻辑：Evans 提出“模型层收不到水费”的宏观问题，Sinofsky 把水费位置具体化到企业软件内部：不是所有上层 UI 都能收费，只有掌握业务逻辑、权限和系统记录的一层能承接价值迁移。两者合起来反驳了“做一个 AI 界面即可替代 SaaS”的浅层判断。

### Agent 身份问题从 onboarding 进入 system of record 写入
**← [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]]**
- 本文件论点：当 agent 要“do something”时，它必须 impersonate 某个具体人，使用其凭证，并解决 paid seat、读写权限和审计问题 [8:18, 35:13]。
- 对方论点：Levie/Casado 把 agent 当作新员工而非软件集成对象，强调 agent 入职、组织权限和遗留系统集成墙。
- 关联逻辑：Levie 给出 agent 身份的组织类比，Sinofsky 给出它碰到 system of record 时的具体产品问题。两篇合并后，agent 企业落地的第一性问题不是 API 是否存在，而是组织是否承认这个行动主体，并能约束它代表谁行动。

### Token 账单之后，企业软件还要解决业务线责任归属
**→ [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]]**
- 本文件论点：企业软件自动化会让长尾变长，新的例外、权限和跨部门判断会继续出现；没有 API 能替代所有组织共识 [38:03, 42:19]。
- 对方论点：Levie 第二次访谈指出 agent 的 token 消费击穿 per-seat 定价，AI 成本会从 IT 预算迁移到业务线预算。
- 关联逻辑：Levie 解释“谁为 agent 付钱”，Sinofsky 解释“谁为 agent 改写业务状态负责”。企业 AI 的真实账本必须同时记录 token 成本和业务决策责任；只解决计费，不解决例外和审计，agent 仍无法进入核心流程。

### 策略层 harness 需要企业语义，否则只是在空转
**→ [[Katelyn Lesse & Angela Jiang- Anthropic 的策略层赌注（token 工作分配与开放生态）]]**
- 本文件论点：企业内最有价值的机会来自连接原本不能沟通的功能，并把 ad hoc process 逐步变成新的 system of record [27:11, 51:51, 59:42]。
- 对方论点：Anthropic 平台团队把价值从执行层推进到 strategies/meta harness，即给不同 token 分配建议、执行、反思、记忆等不同工作。
- 关联逻辑：Anthropic 解释 agent 如何在认知资源上变高效，Sinofsky 提醒这种策略层必须接入企业真实语义。没有 system of record、权限和跨部门上下文，strategies 只能优化模型内部步骤；接入企业语义后，它才可能成为业务流程的控制层。
