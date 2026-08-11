---
title: "Brian Armstrong- 每个 AI Agent 都有自己的银行账户"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=5gWxjh47GeQ"
transcript: "[[Brian Armstrong- 每个 AI Agent 都有自己的银行账户 逐字稿]]"
channel: "Peter H. Diamandis"
published: 2026-07-13
duration: "1min 31s"
tags:
  - kol情报
  - AI-agent
  - payments
  - coinbase
  - base-protocol
status: canonical
created: 2026-07-13
---

> Brian Armstrong 的核心赌注不是让 AI 更方便地操作人类账户，而是让机器直接拥有可注册、可持有资产、可交易的金融账户；Base 的 no-KYC 钱包解决了机器如何开户，却把谁为机器交易负责的问题留在了系统之外。

视频链接：https://www.youtube.com/watch?v=5gWxjh47GeQ

对应逐字稿：[[Brian Armstrong- 每个 AI Agent 都有自己的银行账户 逐字稿]]

## 概述

这段 1 分 31 秒的 MOONSHOTS 短片只回答一个问题：Coinbase 是否会从面向人类的交易所，变成面向 AI 的支付轨道。Armstrong 明确回答，这是 Coinbase 战略的一部分，并把 AI 与金融账户的关系拆成三个阶段：LLM 读取并操作人类账户、AI 内嵌于 Coinbase 账户、每个 AI agent 拥有自己的金融账户。

真正的战略跳跃发生在第三阶段。前两阶段仍然以人类账户为中心，AI 只是查询和执行工具；第三阶段则要求金融系统接受一种没有政府身份证件、却能自行开户和交易的新账户主体。Armstrong 给出的工程答案是 Base 上的 self-custodial wallet，并以 no KYC 作为机器即时开户的条件。

## 从连接人类账户到机器自主开户

第一阶段解决的是上下文缺失。用户已经向 ChatGPT、Claude 询问金融问题，但模型看不到用户持仓，也不能直接调整账户。

> **[0:08]** "They're asking a lot of financial questions to those LLMs, but the LLMs don't have context about what's in their financial account, their portfolio, and they don't have the ability to make changes in there or make trades, for instance."

第二阶段把 AI 放进 Coinbase 产品内部，用于 portfolio rebalance、tax loss harvesting 等具体操作。此时 AI 的权限仍然来自人类账户，责任边界也仍然可以追溯到人类用户。

> **[0:37]** "a lot of people are going to want to just have something like this right in right inside the Coinbase account. And it can kind of help you with things like rebalance my portfolio, you know, tax loss harvesting."

第三阶段改变了账户所有者。Armstrong 不再讨论 AI 如何操作 Brian 的账户，而是讨论 AI agent 自己如何拥有账户。

> **[0:37]** "I don't want to just use AI to control my own existing Brian's financial account. Every AI agent's going to have its own financial account, right? And it has to be able to sign up for that."

这不是同一条产品路线的自然延伸，而是身份模型的变化：系统不再只识别人类用户及其代理工具，而要识别能够持有资产和发起交易的机器账户。

## Base 解决开户摩擦，没有解决责任归属

Armstrong 识别到现有 KYC 体系与机器账户之间的直接冲突：AI agent 没有政府签发、带照片的身份证件。Base 的 self-custodial wallet 绕开了这个入口限制。

> **[1:08]** "An AI agent doesn't have a piece of paper issued by the government with your photo on it or something. How are they going to go sign up for these accounts?"

> **[1:08]** "we have like a self-custodial wallet that any AI agent can sign up for instantly with no KYC."

这个方案的价值很具体：机器不需要等待银行、交易所或企业账户系统为 agent 新建身份类型，就能创建地址、持有资产并参与支付。但它只解决了**技术可进入性**，没有回答以下问题：

- 谁创建和控制这个 agent；
- agent 错误付款后由谁承担损失；
- agent 是否被制裁名单、反洗钱和交易限额约束；
- agent 的密钥丢失、被劫持或被复制时，哪个实例才是账户主体。

因此，no KYC 不能直接等同于 AI 获得法律人格。它只证明加密钱包可以在不验证人类身份的情况下，为软件进程提供资产控制能力。

## Coinbase 的真实战略位移

主持人的提问把 Coinbase 的定位变化说得很直接：从 exchange for humans 转向 payment rails for AIs。Armstrong 没有回避，而是明确把成为 AI 的金融账户列为战略方向。

> **[0:00-0:08]** "do you think Coinbase might be known as payment rails for AIs rather than exchange for humans?" / "Yeah, so that's definitely part of our strategy is to become the financial account for AI."

这意味着 Coinbase 的竞争对象不再只是其他交易所或钱包。它开始争夺 agent economy 的账户层：谁负责创建机器钱包、保存状态、提供结算资产，并让 agent 在应用和协议之间持续交易。

但这段短片没有提供交易量、客户数量、支付频率或具体应用案例。Armstrong 只说 agentic payments 已经开始出现。因此可以确认的是方向和基础设施已经存在，不能从这 92 秒进一步推导市场规模已经成立。

> **[1:08]** "that's what they're using to then transact right now in these um agentic payments that are starting to show up."

## 关键判断

- Coinbase 正把 AI agent 从账户操作工具升级为潜在账户持有者，产品边界由交易界面延伸到机器支付基础设施。
- Base 的 self-custodial wallet 为机器开户提供了低摩擦路径，但 no KYC 同时移除了传统金融体系用于追责和风险控制的入口。
- Agent wallet 的核心未解问题不是能不能创建，而是身份、授权、审计和责任如何绑定。
- 这段短片能证明 Coinbase 已把 agent 金融纳入战略，也能证明 agentic payments 开始出现；它不能证明 AI 已成为法律上的独立经济主体。

## 深度关联
> 以下关联基于论点级分析：不是都提到了 Agent，而是具体论点之间的逻辑关系。

### 金融自由与企业可审计身份的正面冲突
**← [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]]**
- 本文件论点：Base 允许 AI agent 在 no-KYC 条件下即时创建 self-custodial wallet（[1:08]）。
- 对方论点：企业 Agent 必须拥有独立身份和受限权限，不能借用人类凭证，也不能拥有超过发起人的访问权（[26:24]-[28:42]）。
- 关联逻辑：Armstrong 优化的是机器进入金融系统的自由度，Levie 优化的是机器进入企业系统后的可审计性。前者通过移除身份门槛提高采用速度，后者通过强化身份和权限边界控制风险。企业 Agent 真正进入支付环节时，两种架构必须合并：钱包可以 self-custodial，但资金来源、授权人、限额和审计链不能匿名。

### 钱包协议与支付授权解决的是不同层次
**← [[Emily Sands- Token Heist 与 Agent 电商协议]]**
- 本文件论点：Armstrong 用 Base wallet 解决 agent 如何拥有和控制资产的问题（[1:08]）。
- 对方论点：Sands 关注 agent 如何在不暴露底层支付凭证的情况下获得有限支付授权，并把 token theft 视为系统性风险。
- 关联逻辑：Base 提供资产容器，Stripe 路线提供授权与商户支付协议。只有钱包没有授权边界，agent 被劫持时可能直接失去资产；只有授权 token 没有机器原生账户，agent 仍依赖人类支付身份。Agent 金融栈需要同时具备资产所有权、可撤销授权和责任追踪，而不是在去中心化与平台托管之间二选一。
