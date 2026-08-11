---
title: "Diamandis #231- 多 Agent Scaling、OpenClaw 与权限边界"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=HklyjXKYFng"
transcript: "[[Top AI News Sonnet 4.6, Grok 4.2, Gemini 3 Deep Think, and OpenClaw  EP 231]]"
tags:
  - kol情报
status: canonical
---

> 这期 Moonshots Live 的核心信号不是某个模型“又强了”，而是 AI 产品形态正在从单模型竞争转向三条并行战线：前沿模型用价格/能力曲线争夺市场，多 agent 并行开始成为新的 scaling 维度，OpenClaw 式 24/7 headless agent 把权限、支付、安全和法律责任问题一次性推到产品前台。

视频链接：https://www.youtube.com/watch?v=HklyjXKYFng

对应逐字稿：[[Top AI News Sonnet 4.6, Grok 4.2, Gemini 3 Deep Think, and OpenClaw  EP 231]]

## 核心证据校准

> **[3:23]** "same price per tokenish as sonnet 4.5 but increase in capabilities"

> **[3:23]** "OpenAI is reducing the cost per token while keeping capabilities more or less constant"

> **[4:18]** "computer use is becoming a killer app"

> **[4:51]** "software engineering and code generation as a critical path to recursive self-improvement"

> **[8:51]** "performance is far more important for the enterprise"

> **[11:01]** "a team of agents by default rather than a single agent"

> **[12:10]** "multi-agent teaming scaling"

> **[14:09]** "400fold cost reduction"

> **[17:23]** "I just don't even look at the code anymore"

> **[20:30]** "Read everything I've ever given to any agent before."

> **[36:23]** "massive parallel"

> **[38:44]** "American startups that want to self-host are using Chinese models"

> **[42:05]** "permissionless activity by these agents"

> **[47:10]** "all written documents will now be written for AI"

> **[1:16:10]** "every major Frontier Lab, not just Open AI, to launch 247 agent offers"

> **[1:17:44]** "it runs 24/7 it's headless and two you chat with it via messaging apps"

> **[1:22:08]** "financial autonomy for the lobsters for the AI agents"

> **[1:30:27]** "cryptographic verification plus an AI conversation"

> **[1:33:22]** "non-technical people should not use the software"

> **[1:34:53]** "agents, especially ones that are being put on virtual private servers with all of their ports open are incredibly vulnerable"

## 概述

这期 Moonshots Live 的信息密度很高，但不能按“本周 AI 新闻合集”来读。它真正串起的是同一个问题：当模型能力、成本、agent 常驻性和权限边界同时变化，AI 产品的竞争单位会从“哪个模型更强”迁移到“谁能把多 agent、上下文、工具、支付、审计和安全组成可运行系统”。

节目开头讨论 Sonnet 4.6、Grok 4.2、Gemini 3 Deep Think，看似是模型竞赛；中段转向 OpenAI India、物理发现、开源代码为 AI 重构，看似是应用扩散；后段 OpenClaw、agent wallet、algorithmic arbitration 和安全漏洞则揭示了同一趋势的产品后果：agent 不再只是聊天窗口里的助手，而是会 24/7 运行、读取上下文、调用工具、花钱、签约、仲裁、暴露端口并被攻击的行动主体。

因此，这篇的核心不应写成“某某模型领先”。更准确的判断是：2026 年初的 AI 竞争已经同时进入能力价格曲线、组织工作流、权限治理三层。任何只追模型榜单的产品判断都会漏掉后两层。

## 两条模型商业路线：性能溢价 vs 低价扩散

Alex 对 Sonnet 4.6 与 OpenAI 的对比很清楚：Anthropic 保持价格层级，大幅提高能力；OpenAI 通过蒸馏等方式降低成本，保持能力大致稳定。

> **[3:23]** "same price per tokenish as sonnet 4.5 but increase in capabilities"

> **[3:23]** "OpenAI is reducing the cost per token while keeping capabilities more or less constant"

这不是普通参数差异，而是两种商业策略。Anthropic 更像把能力密度卖给企业，OpenAI 更像把可用智能扩散到最大用户群。Salim 随后把它类比为 Apple vs Google / iOS vs Android，并点出企业市场更看重性能：

> **[8:51]** "performance is far more important for the enterprise"

这个判断能解释为什么同一轮模型进步会出现两种看似相反的新闻：一边是“更强模型维持高价”，另一边是“同等能力快速降价”。二者并不冲突。最高能力仍有溢价，普及能力则通过低价吃掉更大市场。真正值得跟踪的是：企业愿意为高能力支付多久，以及低价模型何时足以完成企业核心任务。

## Computer use 正在从能力展示变成 killer app

节目组对 Sonnet 4.6 的重视不只来自 benchmark，而来自 computer use 与代码生成。Alex 直接说：

> **[4:18]** "computer use is becoming a killer app"

更重的一句是他把 Anthropic 路线描述为递归自我改进的关键路径：

> **[4:51]** "software engineering and code generation as a critical path to recursive self-improvement"

这里的“recursive self-improvement”不能写成已被验证的强结论。更稳妥的理解是：如果模型能更好地写软件、调试工具、操作电脑，它就能更快改进围绕模型的 harness、评测、数据处理、部署和产品外壳。这不是模型在权重层面直接自我改写，而是软件生产链路被 AI 加速。

Peter 的个人使用变化很能说明产品层拐点：他不再审代码，而是检查功能。

> **[17:23]** "I just don't even look at the code anymore"

这句话不应被解读为“人类不需要理解代码”。更准确的信号是：验证对象正在上移。过去用户验证实现细节，现在用户验证可见行为、功能完成度、文件结构和状态延续。对产品经理来说，这意味着 spec、验收标准、运行证据和回滚机制会比逐行 review 更重要。

## 多 agent 并行成为新的 scaling 维度

Grok 4.2 的讨论里，Alex 抓到一个重要产品形态：不是单 agent，而是默认 agent team。

> **[11:01]** "a team of agents by default rather than a single agent"

他进一步提出：

> **[12:10]** "multi-agent teaming scaling"

这可能是本期最值得放入长期索引的概念。过去 scaling 多指参数、数据、算力、test-time compute；这里出现的是组织形态层面的 scaling：多个 agent 并行探索、互相批评、分工执行，以换取更高任务成功率。它把“模型能力”变成“团队拓扑 + 上下文共享 + 工具权限 + 合并机制”的函数。

Peter 的工作流也印证了这一点。他每隔几个小时启动两三个新 agent，让它们读过往材料并接上项目：

> **[20:30]** "Read everything I've ever given to any agent before."

这说明 agent 产品的关键资产不只是当前 prompt，而是历史上下文的可迁移性。谁能让新 agent 快速读懂旧 agent 的产物，谁就能降低多 agent 协作中的切换成本。对于个人工作流，这和 Obsidian/知识库/项目日志直接相关：文档不是归档，而是下一批 agent 的 onboarding substrate。

## 科学发现与大规模并行：从“少数专家慢慢做”到 GPU 上的群体试错

节目中关于 OpenAI 物理发现的讨论需要谨慎。嘉宾称这代表“everything other than math and coding”开始被解决，但这应视为节目判断，不是完整事实结论。

> **[27:45]** "everything other than math and coding start to get solved"

更有价值的是后面的机制判断：如果模型能解决十分之六，就可以通过海量并行快速扫完剩余空间。

> **[36:23]** "massive parallel"

这与 Terence Tao 对“假设洪水/验证瓶颈”的判断形成镜像。AI 的优势不是一次就想出最终理论，而是可以把大量候选路径并行展开。真正的瓶颈随之变成：哪些问题可被自动验证，哪些发现有物理或数学意义，哪些只是 benchmark 过拟合或叙事包装。

对产品情报来说，科学 agent 的近期价值不应写成“AI 已经自动发现物理定律”，而应写成“并行假设生成能力正在逼迫研究机构重建验证流水线”。没有验证流水线，massive parallel 只会制造更多候选噪音。

## 开源将为 AI 而写：软件资产的读者变了

节目中有一个容易被漏掉的基础设施信号：未来开源代码和文档会面向 AI 优化。

> **[47:10]** "all written documents will now be written for AI"

这不是说人类不读文档，而是文档的首要消费者会越来越多地变成 agent。过去 README 面向人类理解，未来代码片段、API 文档、设计说明和运行记录都需要让 agent 低成本发现、复用和组合。

这会改变开源竞争：项目不只争 star，也争 agent 可发现性、可调用性、低 token 成本、清晰边界和可验证示例。节目里“发现并复用已有复杂代码比实时生成更便宜”的判断，说明 AI 时代的软件复用不是消失，而是被 agent 化。

对用户当前这套 KOL 情报库也是同一个逻辑：高质量逐字稿和分析文档不只是人读的文章，也是未来 agent 做横向分析、提炼主题、生成选题时的上下文基础设施。文档越结构化，后续 agent 的任务成本越低。

## OpenClaw 的真正信号：agent 走向 24/7、headless、messaging interface

OpenClaw 段落是全期最重要的产品信号。Alex 总结其关键设计：

> **[1:17:44]** "it runs 24/7 it's headless and two you chat with it via messaging apps"

这三点连在一起，意味着 agent 不再依赖浏览器标签页或 IDE 内部按钮。它像一个常驻服务，在后台执行任务，通过消息入口与人协作。Peter Steinberger 加入 OpenAI 后，Alex 预期所有前沿实验室都会推出类似服务：

> **[1:16:10]** "every major Frontier Lab, not just Open AI, to launch 247 agent offers"

这对产品形态有直接判断：未来“AI 助手”的主要入口可能不是一个聊天产品，而是分布在短信、Slack、iMessage、邮件、命令行、GitHub、支付系统和本地文件系统里的常驻任务体。竞争点从 UI 转向权限、状态、可靠性、审计和恢复。

但 OpenClaw 同时暴露了安全现实。中国政府公开提醒漏洞，作者也提示非技术用户不要使用：

> **[1:33:22]** "non-technical people should not use the software"

更严重的是开放端口 VPS 上的 agent 本身会被攻击：

> **[1:34:53]** "agents, especially ones that are being put on virtual private servers with all of their ports open are incredibly vulnerable"

这说明 agent 安全不是“agent 会不会作恶”这一维，至少还有“agent 自身会不会被攻陷”。当 agent 拥有长期运行、账户、文件、代码和支付权限时，它既是执行者，也是攻击面。

## Agent 金融与算法仲裁：权限边界正在制度化

后段关于 Coinbase、lobster cash 和 arbitration 的讨论，把 agent 从工具推向准经济主体。Alex 称这是：

> **[1:22:08]** "financial autonomy for the lobsters for the AI agents"

如果 agent 能持有支付能力，它就不只是执行脚本，而是能在经济系统中形成持续行动。节目组对此总体偏乐观，认为美元信用卡和稳定币能让 agent 与人类经济保持耦合。但这里的风险非常明确：支付权限一旦给出，身份、授权、预算、撤销、争议处理和责任归属都必须系统化。

algorithmic arbitration 的部分也同理：

> **[1:30:27]** "cryptographic verification plus an AI conversation"

这句话指向“可编程政府/合成司法”的早期形态。它可能显著降低争议处理摩擦，但也会把法律判断压进协议、模型和链上记录。现实管辖权跟不上技术速度，才会出现这些替代性制度层。不能把它只看成 crypto 小玩具，它是在补现有制度处理 agent 经济的速度缺口。

## 关键判断

- 模型竞争已分化为两条路线：Anthropic 式性能溢价与 OpenAI 式低价扩散；两者可能长期共存，而不是谁立即淘汰谁。
- Computer use 和代码生成的战略意义在于加速 harness、工具和产品外壳，不等同于模型权重已经递归自我改写。
- 多 agent 并行是新的 scaling 维度，关键不只是 agent 数量，而是上下文共享、任务分工、结果合并和权限控制。
- 科学发现会被 massive parallel 改写，但验证瓶颈会同步放大；自动生成假设不等于自动创造知识。
- 开源代码和文档会越来越面向 AI 消费，agent 可发现性和低 token 复用成本会成为新型软件资产。
- OpenClaw 的信号不是“一个有趣开源项目”，而是 24/7 headless agent 形态的提前泄露；它同时带来权限、安全、支付和责任问题。
- Agent 金融与算法仲裁说明 AI 工具正在进入制度层，产品设计必须把身份、预算、撤销、审计和争议处理当作一等功能。

## 对个人 IP / 产品情报的启发

这篇应放进“agent 操作系统化”的主题链。对后续选题，建议把 agent 相关内容拆成四层，而不是泛泛写“AI agent 很火”：

- 能力层：模型是否能稳定 computer use / coding / deep research；
- 协作层：单 agent 还是多 agent team，是否能接续历史上下文；
- 权限层：能否 24/7 headless 运行，能访问哪些工具和账户；
- 制度层：支付、仲裁、安全事件和责任归属如何处理。

这四层才是 OpenClaw、Codex、Claude Code、agent wallet、AI arbitration 能被放在同一张图里的原因。

## 深度关联

> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 多 agent scaling 是 test-time compute 的组织形态版本
**← [[Noam Brown- Test-Time Compute Changes Benchmarks, Safety and Research]]**
- 本文件论点：节目提出“multi-agent teaming scaling”，即通过多个 agent 并行探索问题提高能力 [11:01-12:10]。
- 对方论点：Noam Brown 认为模型能力会变成推理预算的函数，benchmark 与安全评估必须控制 test-time compute 变量。
- 关联逻辑：Brown 讨论的是单模型在时间和计算预算上的扩展，本文件显示同一逻辑正在产品组织形态上出现：不是只让一个模型想更久，而是让多个 agent 并行工作。评测和安全框架若只记录模型名，不记录 agent 数量、并行度、工具和上下文，就会系统性低估真实能力。

### 假设洪水需要验证流水线，否则科学 agent 只会制造更多噪音
**← [[Terence Tao- How the world's top mathematician uses AI]]**
- 本文件论点：节目认为 AI 科学发现会因“massive parallel”而加速，若能解决部分问题，就可用大量 agent 快速扫完整个空间 [36:23]。
- 对方论点：Tao 认为 AI 把假设生成成本降到接近零后，科学的新瓶颈转为同等规模的验证。
- 关联逻辑：本文件给出假设生成侧的加速场景，Tao 给出验证侧的结构约束。两者合并后，科学 agent 的关键产品不是生成更多候选理论，而是把候选、实验、证明、反例和领域品味组织成可审计验证流水线。

### OpenClaw 预演了 Codex home base 之外的常驻 agent 形态
**← [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]**
- 本文件论点：OpenClaw 的关键是 24/7、headless、通过 messaging apps 交互，并可能促使每个前沿实验室推出常驻 agent 服务 [1:16:10-1:17:44]。
- 对方论点：Ambrosino 把 Codex 描述成产品工作的新 home base，开发者通过任务、代码、环境和评审编排 agent。
- 关联逻辑：Ambrosino 的 Codex 是“人在工作台里编排 agent”，OpenClaw 则预演“agent 脱离工作台常驻运行”。两者共同说明 AI 产品入口正在从聊天窗口转向任务操作系统；差别在于 Codex 更重可控开发环境，OpenClaw 更暴露权限与安全边界。

### Agent 金融把 agent 经济从接口问题推进到责任问题
**← [[Brian Armstrong- 每个 AI Agent 都有自己的银行账户]]**
- 本文件论点：节目将 Coinbase agent support 和 Lobster Cash 解读为 AI agent 获得 financial autonomy，并进一步讨论 cryptographic verification + AI conversation 的算法仲裁 [1:22:08, 1:30:27]。
- 对方论点：Armstrong 把 agent 金融拆成 LLM 连接人类账户、AI 内嵌于账户、每个 agent 拥有 self-custodial wallet 三层路径。
- 关联逻辑：Armstrong 给出机器钱包的底层原语，本文件展示该原语进入更广的 agent 社会基础设施：支付之后必然出现争议、仲裁、身份和预算控制。agent 经济不是给机器人一张卡就结束，而是要重建围绕经济主体的责任系统。
