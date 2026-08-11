---
title: "Charlie Holtz- How Conductor CEO Sets Up His Team Of AI Agents"
source: feishu
feishu_doc_id: WIrmdslFHoCw3RxZpLqc9xC3n9e
tags:
  - kol情报
created: 2026-06-08
order: 30
---

[deprecated] docs +fetch is using the v1 API. Check the installed lark-doc skill first; if it is not the v2 skill, run `lark-cli update` to upgrade skills.
# Charlie Holtz: How Conductor CEO Sets Up His Team Of AI Agents

> 代码几乎是锯末——你投入时间的是「描述你想要什么」，代码只是那个过程的副产品。真正值钱的是你的 prompt，而不是生成的代码——下一代模型出来时，你重跑 prompt 就能得到新代码，旧代码根本不重要。
>
> —— Charlie Holtz, Conductor CEO/Co-founder, Y Combinator Full Stack 系列 2026

视频链接：https://www.youtube.com/watch?v=fQmlML9Lay4

概述：Y Combinator 新系列 Full Stack 第一集，Conductor CEO Charlie Holtz 展示他如何用多 agent 编排工作流来构建产品。Conductor 是一个 Mac 应用，让你同时编排多个编码 agent。Holtz 本人已经几乎不手写代码，通过语音指令 + 键盘快捷键同时管理 3-5 个 agent 工作区。核心赌注是：开发者角色从「编码者」转变为「指挥家」，代码是锯末，prompt 才是资产。

主题脉络：① 代码是锯末——从编码到描述 → ② 人机协作的边界设计 → ③ Token maxing 的实操 → ④ 可塑软件——游戏 mod 的隐喻

# 一、代码是锯末——开发者的新角色是指挥家

Holtz 的工作流是：Command+N 新建 workspace → 语音描述任务 → agent 开始执行 → 同时跳到另一个 workspace review → 给 agent GitHub 式评论反馈 → 再跳到下一个。他几乎不手写代码，Conductor 内部甚至把手动编辑文件的模式叫「原始人模式」（caveman mode）。这个命名本身就是一种文化宣言——手写代码已经退化为原始行为。
```plaintext {wrap}
[02:41] >> You still write code today? >> No. Yeah. No. Very occasionally I will like edit Tailwind classes or like open up an IDE to change like a ENV file. We actually added a mode that we call caveman mode which is uh you click this and you can actually type with your keyboard and like make changes in a file.
```

但他坚持一个关键区分：代码是锯末，但 prompt 不是。当下一代模型出来时，你重跑同样的 prompt 就能得到更好的代码，旧代码自然淘汰。这意味着 prompt 文件（CLAUDE.md、skills 文件）才是真正需要投资的资产——它们承载了团队的工作方式、工程哲学和产品品味。
```plaintext {wrap}
[15:00] Code is almost like uh sawdust now in that like it used to be that code was the thing you were building. It was like the structure. You were putting time into like crafting the code and now you're putting time into describing what you want and how you want it to be built. And the code is almost just like sawdust that comes out of that process.
```

# 二、人机协作的边界设计——slot-free zones 与架构主权

Holtz 引入了一个重要概念——「slot-free zones」（禁区）：代码库中某些部分必须由人类逐行审查，AI 可以贡献但每一行都必须经人眼。理由是 AI 会陷入恶性循环——看到烂代码就写出更烂的代码，反之亦然。他们甚至有些文件标注了「AI 禁入——仅供人类」。同时，架构决策和 UI 设计必须由人主导：「不要让 AI 做你的架构师。」workspace 概念本身、左侧面板布局、中间对话、右侧 review 区域——这些都是人类深思熟虑的设计决策，不是 AI 能做的。
```plaintext {wrap}
[07:06] Another thing we talk about is like don't let the AI be your architect. Even the concept of like a workspace here in the sidebar which in some ways is just like an abstraction around a work tree... like that concept of a workspace like we as a human had to like think that through.
```

这个边界设计思维可以提炼为一个通用原则：让代码库有「核心层」（人类写的 API 契约 + 架构）和「自由层」（AI 可以随便试错的区域），核心层不变，自由层快速迭代。当前 Conductor 的边界还「有点模糊」，但方向清晰。

# 三、Token maxing 的实操——$22K/月和高努力模式

Holtz 对 token 投入的态度毫不含糊：始终使用 fast mode、think extra hard、高 effort。Conductor 创建初期（2025 年 7 月）他单月花了 $22,000 在 token 上，月产代码数万行。但他特意区分了「token maxing」和「lines of code maxing」——代码行数必须控制，否则代码库会失控。他的模型选择也很有策略性：Claude（Opus）用于创意和合作，Codex 用于强力推进——前者是「伙伴」，后者是「工蜂」。
```plaintext {wrap}
[12:07] I think the highest spend was when we were starting out conductor like in July 2025. I spent $22,000 on tokens that month.
```

```plaintext {wrap}
[10:45] Codex is like the workhorse. it will power through like a specific problem... Cloud I'll reach for when I want a little more like back and forth. I feel like Opus is just like a little more creative, like a little more uh of a partner.
```

# 四、可塑软件——游戏 mod 的隐喻

Holtz 用视频游戏的 mod 文化来隐喻软件的未来：游戏的核心结构对所有人一样，但每个人可以自定义皮肤、装填速度等。同理，Conductor 的「prompt request」功能让用户可以定制工作流，同时保持核心体验一致。关键洞察是：人们需要的是「被精心设计过」的软件（crafted），但也需要让软件感觉像「自己的」（personal）。这两个需求看似矛盾，mod 文化提供了一个解决框架——骨架统一，皮肤自由。
```plaintext {wrap}
[15:46] the metaphor that I always think of when I think of malleable software is like video games and how like when you play like Call of Duty like the structure of the game is the same for everyone and like the skeleton is the same but each person can like use custom skins or like faster like reload speeds or whatever.
```

---

**元信息**
```plaintext {wrap}
标题: How Conductor CEO Charlie Holtz Sets Up His Team Of AI Agents
频道: Y Combinator
发布时间: 2026-06-04
时长: 16min 35s
YouTube链接: https://www.youtube.com/watch?v=fQmlML9Lay4
分析时间: 2026-06-05
```


## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系
### Software 3.0的维护悖论
**← [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]**
- 本文件论点：代码是锯末，prompt才是资产。下一代模型出来时重跑prompt就能得到更好代码，旧代码自然淘汰
- 对方论点：Software 3.0：prompt成为编程语言，context window成为杠杆。旧范式的应用是spurious的
- 关联逻辑：Karpathy定义了范式（prompt=编程语言），Holtz实操了后果：既然prompt是程序，代码就是副产品。但Holtz没回答的问题是——当prompt变成程序，它是否也继承了程序的维护负担？87KB审美判决书给出了答案：是的
**→ [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]**
- 本文件论点：代码是锯末，prompt才是资产。下一代模型出来时重跑prompt就能得到更好代码
- 对方论点：OpenClaw安装案例：shell script被agent指令替代——你不需要在script里穷举所有情况，因为agent自带智能去处理边缘case
- 关联逻辑：Holtz的「prompt是资产」有一个隐含前提：prompt跨模型迁移时仍然有效。但Karpathy的OpenClaw案例暗示prompt也可能随范式切换而失效——shell script→agent text就是一次prompt的范式死亡

### Prompt作为核心资产的两种形态
**→ [[OpenCLI—逆向工程的无限游戏与协议真空地带的套利者]]**
- 本文件论点：代码是锯末，prompt才是资产。下一代模型出来时重跑prompt就能得到更好代码
- 对方论点：OpenCLI的核心护城河是~/.opencli/sites/里的site knowledge——endpoints、field maps、fixtures。每个网站的逆向知识就是一份prompt资产
- 关联逻辑：Holtz的「prompt是资产」在OpenCLI中有了更精确的形态：不是通用的instruction prompt，而是site-specific的领域知识文件。但OpenCLI也暴露了这种资产的脆弱性——网站改版就失效（auto-healing adapter是最高价值但最难做的功能），而Holtz没讨论prompt资产的折旧问题

