---
title: "Anthropic's Katelyn Lesse & Angela Jiang: Building an Ecosystem, not a Walled Garden"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=vPnVTHYplrQ"
canonical_report: "[[Anthropic平台生态 - Lesse & Jiang - Sequoia 2026]]"
transcript: "[[Katelyn Lesse and Angela Jiang- Building an Ecosystem not a Walled Garden]]"
channel: "Sequoia Capital"
kol: "Katelyn Lesse & Angela Jiang"
duration: "48min 55s"
upload_date: "2026-07-14"
tags:
  - kol情报
created: 2026-07-15
status: supplementary
dedup_note: "同一访谈的旧版分析，canonical见[[Anthropic平台生态 - Lesse & Jiang - Sequoia 2026]]"
---

> 平台的护城河不在基础设施层，而在「策略层」——当你给每个 token 分配不同的工作（建议、执行、反思、记忆），你就拥有了比换更大的模型更高效的杠杆；Anthropic 赌的是把这种「元 harness」变成人人可组合的原语，同时把执行层全部打开让别人来跑。
> —— Katelyn Lesse & Angela Jiang, Sequoia Capital 2026

视频链接：https://www.youtube.com/watch?v=vPnVTHYplrQ

**概述**：2026 年 7 月 14 日，Sequoia Capital 播客。对话者 Katelyn Lesse 和 Angela Jiang 领导 Anthropic 的开发者平台团队——这个团队同时服务于外部开发者 API 和内部产品基础设施，是 Claude 生态的承重墙。整场访谈的核心赌注是：Anthropic 不打算拥有全栈，甚至不执着于让你把 agent 跑在自己的基础设施上；他们赌的是在三层抽象栈（知识→执行→协调）的顶端——「策略层」或「元 harness」——建立不可替代的杠杆。当每个 token 都可以被分配一个不同的「工作」，而这套组合方式只有 Anthropic 的平台能最好地支持时，谁拥有 sandbox 就变得无关紧要。

**主题脉络**：① 形态永恒流动——为什么不执着于任何一种产品形态 ② 三层蛋糕——从 messages API 到策略 harness 的攀登路径 ③ 开放不是让步而是架构——self-hosted sandbox 与 MCP tunnels ④ 界面是冰山一角——Claude Tag 的 org-level harness ⑤ 模型吞噬脚手架——从 steering harness 到 strategy harness 的迁移 ⑥ Token 理性化时代的第三根杠杆

---

## 一、形态永恒流动——为什么不执着于任何一种产品形态

Angela 在开场不久就抛出了一个贯穿整场访谈的底层判断：产品形态不是静态的，而是以年为单位持续颠覆的。两年前所有人是 chat，现在所有人是 agent，明年又会有新的形态。这个判断直接决定了平台的设计哲学——不押注任何单一形态，而是提供原语让市场自己涌现形态。

```plaintext
[04:41] I think two years ago we were all like everything's chat and now everyone's like forget chat and just like agents and like there's going to be another form factor, another form factor.
```

更关键的是她对 Anthropic 在这场形态演变中应扮演的角色的定位——不是唯一的形态发现者，而是形态涌现的赋能者：

```plaintext
[05:03] And I don't think we by any means feel like we're the only ones capable of figuring out that form factor like not at all. In fact, the more democratization we can do on that and help people and allow people to experiment, I think the more those form factors will actually kind of naturally come out of the market.
```

这段话的隐含立场极为重要：Anthropic 在这里主动放弃了「形态定义者」的垄断地位。这不是谦虚，而是一种有意识的平台策略——当形态变化速度超过任何单一团队的追赶能力时，开放原语比封装产品更能捕获价值。这与 Nadella 在 Build 大会上的「平台定义不在于你捕获了多少价值，而在于你让平台外创造了多少价值」的论断在结构上同构。

Katelyn 补充了一个实操维度——内部和外部用户的差异本身就是一种信号源。如果只做内部 dogfooding，就会过度索引内部用户的特定需求；如果只听外部客户，又可能脱离 Claude 自身产品线的真实压力。所以他们的做法是同步进行：

```plaintext
[05:50] So a lot of the time what we'll do is dog food something internally at the same time that we open up early access of some sort with external customers so that we can kind of get a range of feedback and bring those things back into the platform.
```

这构成了一种双重验证机制：内部团队提供了极限压力测试，外部开发者提供了形态多样性。当两者指向同一个抽象时，这个抽象才值得被平台化。

---

## 二、三层蛋糕——从 messages API 到策略 harness 的攀登路径

Angela 提出了整场访谈最核心的架构框架——三层蛋糕。这不是一个技术文档式的分类，而是一条路线图，指示 Anthropic 的资源投入方向正在从底层向顶层迁移。

**第一层：知识层。** 最底层是关于「模型需要知道什么」的原语——messages API 的形状和参数、tools 的标准化、skills 和 memory 的上下文注入。这些已经「baked」，趋于稳定：

```plaintext
[09:43] we still evolve them but they tend to be a little bit more baked. Like for example there's very specific shapes and parameters we put on the messages API
```

**第二层：执行层。** 当 Claude 从「回答问题」变成「执行工作」——编辑文件、调用系统、产出结果——就需要基础设施来支撑。这层是「low-level harness plus managed infrastructure」，对应产品是 Claude Managed Agents。Katelyn 特别指出这层要解决的痛点：

```plaintext
[07:17] how do you figure out spawning sandboxes that are going to have the right governance and security and like you know spin them up and spin them down when you need to or the storage around transcript sessions so that you can resume a session if you stop it and pick it back up later.
```

**第三层：协调层（策略层）。** 这是整场访谈的真正赌注所在——也是路线图的前沿。Angela 用一个极其精密的概念来描述它：「meta harness」或「strategies」。核心洞察是：tokens 不再是可互换的——不同的 token 可以被分配不同的工作。

```plaintext
[11:35] the true low-level harness is designed for execution. But the next one is about okay if tokens aren't really fungible and you need to give them different jobs like maybe some this token is advising versus this token is executing this token is dreaming versus this token's executing
```

这段话的密度极高。Angela 在这里提出了一个范式级的判断：agent 的效率提升不再来自更大的模型或更长的运行时间，而来自对 token 的「工作分配」——有的 token 负责建议（advising），有的负责执行（executing），有的负责反思过去并将学习写入记忆（reflecting + memory），有的负责「dreaming」（探索可能空间）。这不是简单的多 agent 编排，而是一种更底层的认知资源分配策略。

路线图的指向因此清晰可见：

```plaintext
[11:58] if you were to look at our road map and maybe kind of project forward a little bit where you kind of expect us to go. We'll move more and more from the knowledge layer to the execution layer and from the execution layer to the kind of coordination layer in terms of the abstractions that you can see us put out.
```

从底向上攀登——这不是一个产品发布计划，而是一个价值捕获的迁移路径。底层趋于商品化（messages API 人人都能做），中层正在被封装（Managed Agents 解决基础设施痛点），真正的杠杆在顶层（strategies 是 Anthropic 独有的认知工程）。如果这个判断成立，Anthropic 的平台策略本质上是：放弃底层和部分中层的垄断，在顶层建立不可替代性。

---

## 三、开放不是让步而是架构——self-hosted sandbox 与 MCP tunnels

当主持人直接问出「open ecosystem vs. walled garden」时，Katelyn 的回答展示了一种精巧的开放策略——在执行层放手，在架构层保持控制。

```plaintext
[16:10] we actually aren't precious about you should run these things on our infrastructure like it should be sandboxes that we control or it should be a storage layer that we control.
```

她随即给出了一系列具体案例来证明这不是空谈：

```plaintext
[16:22] we launched self-hosted sandboxes and we partnered with modal and versel and cloudflare and a bunch of other folks even like Amazon's new microVMs to have a first class offering where you can go plug any of those things in.
```

MCP tunnels是另一个信号——允许 agent 调用防火墙后的私有 MCP 服务器：

```plaintext
[16:38] we launched MCP tunnels so that you can call out to your MCP servers that are behind your firewall
```

但这里有一个极其重要的转折——Katelyn 明确划出了不开放的边界。Anthropic 不在乎你的 sandbox 跑在哪里，但他们在乎你如何把 agent 组合在一起的方式：

```plaintext
[16:53] the thing that's important to us is more that the architecture of how you put together these agents in a way that will be powerful, in a way that will be reliable and scalable. um we have strong opinions on that and you can kind of just conform to the interfaces that we put out there and plug those things in.
```

这就是整个开放策略的精妙之处：开放基础设施（sandbox 跑在哪），封闭架构接口（agent 如何组装）。当 Anthropic 控制了 agent 组装的接口规范时，sandbox 跑在 Modal、Vercel 还是 AWS 上就变成了一个执行细节而非架构决策。这是一种「接口层垄断」——你的数据可以留在你的基础设施里，但你的 agent 行为模式必须遵循 Anthropic 的规范。

Angela 补充了更深一层的安全维度——开放生态需要行业标准来处理安全，而 Anthropic 正在参与定义这些标准：

```plaintext
[14:06] there's also a bit around interoperability and standard setting around how do we all kind of like treat safety together
```

她用网络安全作为案例——没人希望自己的服务上有恶意行为者，因此安全标准的制定是一个跨行业协作的天然切入点。这构成了 Anthropic 开放策略的第二条暗线：通过安全标准制定，将自身嵌入生态的治理层。

---

## 四、界面是冰山一角——Claude Tag 的 org-level harness

当主持人问及 Claude Tag 被外界嘲笑为「just a Slack bot」时，Angela 的回应揭示了 Anthropic 对产品形态的核心判断——界面可替换，但界面之下的 context engineering 和 harness 架构才是不可替代的资产。

```plaintext
[23:47] the important part is all the kind of like context engineering and like architecture that we put underneath the hood. So that tag just works.
```

她引用了 Andrej Karpathy 的定义来强化这个判断：

```plaintext
[24:44] it's like an org level harness
```

这个概念——「org-level harness」——是整场访谈中信息密度最高的产品判断之一。Claude Tag 不是 Slack 里的一个机器人，而是一个横跨整个组织的 agent harness：它主动发现什么对你有用、它帮你完成跨系统的工作流、它像一个新入职的同事一样融入你的 channel。界面的选择（Slack）只是冰山露出水面的部分，水面之下是所有的 context 工程、proactivity 逻辑和 harness 组件。

更具前瞻性的是 Angela 对界面可替换性的判断——今天的 Slack、明天的 Teams、后天的 WhatsApp 或 email：

```plaintext
[25:24] the interface can actually constantly swap like today, right? Like Slack is a place where a lot of people collaborate [...] but also a lot of people collaborate in teams and some people collaborate by a WhatsApp group
```

```plaintext
[25:42] they're almost taking up the same form factors as humans have taken up
```

最后一句话是整场访谈最意味深长的判断之一。Angela 在说：agent 的终极形态不是一个新的 UI 范式，而是直接占据人类已有的协作界面。Agent 应该像一个同事一样出现在你的 Slack channel 里，而不是要求你打开一个全新的应用。这与 Karpathy 的「App 不该存在」论形成共振——当 agent 可以直接使用人类已有的沟通渠道时，专用 agent 界面的存在理由就被消解了。

Katelyn 在讨论垂直产品策略时补充了另一个关键维度——Anthropic 选择进入垂直领域的标准不是「这个市场有多大」，而是「这个领域的 token 消费模式是什么样的」。她区分了「token-heavy」和一次性任务两种模式：

```plaintext
[20:13] we do tend to have an orientation towards things that are more token-heavy. [...] you for spending once you spend a like call it like one turn you look at the end of that turn and you say like am I done or am I actually so glad that I did that thing I want to do more of that thing
```

Coding 是典型的 token-heavy 领域——每完成一轮你都想做更多。而有些领域完成一轮任务就结束了。Anthropic 的垂直化策略优先选择前者，因为 token-heavy 意味着更高的平台粘性和更大的杠杆。Finance 和 legal 被选中，不仅因为 TAM 大，更因为这些领域的验证逻辑——错误成本高，需要精密的 harness，而这恰好是 Anthropic 能提供独特价值的地方。

---

## 五、模型吞噬脚手架——从 steering harness 到 strategy harness 的迁移

Angela 在讨论 harness 演进时给出了一个关键的历史分期：两年前，harness 的核心功能是「steering」——给模型搭墙，让它从 A 走到 B 不跑偏。现在模型足够 steerable 了，这层 harness 可以被删除。

```plaintext
[28:54] if you look like two years ago, a lot of the harness was like a scaffold to kind of like tell the model to go from point A to point B. And you had to like you really had to like build in a lot. You practically build one wall here and one wall here. So like the thing would go in a straight line. And now the models are actually very very steerable.
```

```plaintext
[29:30] if you have harnesses that are designed to kind of do that kind of like steering, you can delete that part.
```

但模型变强不意味着 harness 消失——它意味着 harness 的重心从「steering」迁移到「strategy」。因为模型可以自己找到路径了，你不需要再搭墙；但你需要告诉它去哪、以什么策略去、花多少预算去。Angela 的判断是：

```plaintext
[29:51] what the harness needs to start doing is more allow it to run longer.
```

让模型跑更长——这直接呼应了 Noam Brown 的 test-time compute 论断（模型能力变成预算的函数）。但 Angela 和 Katelyn 的独特贡献在于：他们不只是让模型跑更长，而是让跑出来的 token 做不同的事。

Katelyn 把这个迁移讲得最为精确。她区分了两层 harness：低层 harness（prompt caching、context window 清理、evals）和高层「meta harness」或「strategies」。低层的最佳实践已经固化，榨不出太多汁了：

```plaintext
[28:46] I don't know that there's necessarily so much juice to squeeze in a lot of cases out of that layer as compared to a layer higher than that.
```

高层的策略才是真正的 alpha 所在——同一个 token 可以用来执行，也可以用来反思过去的 agentic session 并把学习写入记忆，也可以用来让大模型给小模型提建议，也可以在执行后让一个 grader 来判断做得好不好：

```plaintext
[27:47] you can take any given token and spend that token on just executing or you could take that same token and choose to actually reflect on your past agentic sessions and write learnings to memory so that the next agent does a good job or you could take that token and advise with a bigger model so that a smaller model can execute and do a better job.
```

这是一段范式级的论述。Katelyn 在这里实际上在说：token 的 ROI 不是固定的——同样的 token 花在执行上得到的回报，远低于花在反思+记忆上（因为后者让未来所有 agent 都受益），也远低于花在 advise 上（因为后者用小模型执行可以大幅降低成本）。策略层的创新就是找到 token 的最优工作分配。

在讨论垂直领域是否需要 task-specific harness 时，Angela 给出了一个更精细的判断——领域特异性真正重要的地方在「验证逻辑」：

```plaintext
[31:05] how you choose to kind of like handle sort of like errors between when you do something and you hand something off to the model. [...] in domains where you require like an extreme level of verification, that logic of how you handle that [...] will give you a ton of juice
```

但她同时认为 context engineering 被「过度炒作了」——任何 harness 都能处理大量 context，真正的差异化不在这里：

```plaintext
[32:10] the context bit is actually a little like overdone. Like yes, you're going to like throw in context and like that's but any harness can actually handle a lot of context
```

这构成了一个完整的 harness 价值地图：prompt caching / context 管理 = 商品化（低价值）→ 验证逻辑 = 领域特异性来源（中等价值）→ 策略 / token 工作分配 = 真正的 alpha（最高价值）。Anthropic 的路线图就是沿着这条价值链往上走。

---

## 六、Token 理性化时代的第三根杠杆

访谈后半段切入了企业 AI 的成本话题。Angela 给出了一个清晰的分期框架：当模型智能达到某个水位后，下一个竞争维度要么是成本要么是速度，你会沿着这个分布不断 hill climb。

```plaintext
[38:41] as these models get more and more capable you're going to hit like levels of intelligence maxing that are like there that then you want to do the next kind of dimension and the next dimension after intelligence will either be cost or it will be speed.
```

她的核心警告是：不要试图通过停止 AI 使用来控制成本。她描述了一个常见的场景——AI 通过 shadow IT 渗透进企业（员工自行安装 Claude Code），然后 IT 试图通过 cap 来控制：

```plaintext
[39:06] what you don't want to do is like stop AI usage, right? Like that's kind of the wrong move.
```

Angela 建议的路径是设计一种「策略」——本质上是一个 router，根据任务复杂度分配模型：

```plaintext
[39:49] given a task assesses level of complexity [...] if it's like a hard task you should probably route that to like a big super smart model and if it's not a hard task you can route that to like cheaper models
```

但这里有一个关键的边界声明——Angela 明确表示这种 routing 限于 Claude 模型家族内部，Anthropic 不打算支持跨模型厂商的路由：

```plaintext
[40:55] we are designing our platform for Claude and we want to make sure that Claude is great at like solving all these things. So we'll like restrict to that space
```

Katelyn 补充了更深一层的判断——harness 应该绑定模型家族，而非做成模型无关的通用层。她用 Vercel 的 harness agent 作为案例，说明行业正在从「插拔不同模型」转向「插拔整个绑定到模型家族的 harness + agent」：

```plaintext
[41:21] we have a strong belief that harnesses and and just like the agentic layer should be tuned to the model family that you use it with. [...] some of these players in the space like come up a layer of abstraction and say actually like plug in the whole harness and the whole agent that's tied to a model family
```

这个判断的含义极其深远：如果 harness 绑定模型家族，那么「模型商品化」的论点就需要被修正——不是模型本身不商品化，而是 model + harness 的组合不商品化。模型可以被替换，但替换的代价不仅是 API 调用的变更，而是整个 harness 和策略栈的重构。这恰好是 Anthropic 在执行层开放（不锁定基础设施）但在架构层封闭（锁定 agent 组装接口）策略的理论基础。

Katelyn 用她在 Stripe 的经历做了一个类比——AI 的成本治理正在走 AWS 成本治理走过的路：

```plaintext
[42:12] before working at Anthropic I was at Stripe and we were kind of in the very reasonable era of like we paid a lot of attention to our AWS bill
```

但她强调 AI 多了一个维度：不只是找到失控的 background job 并关掉它，而是要找到用更聪明的策略达到同样结果的方法——用 Opus 跑一整夜 vs 用策略组合在更低成本下达到同样结果：

```plaintext
[43:16] one is like you take Opus and you run it all night and you do something crazy. And another is maybe to get a little bit smarter with the strategies that you put together in order to create that same outcome within a lower cost.
```

这就是 token 理性化时代的三根杠杆：① 换模型（大→小）② 让模型跑更久 ③ 重新设计策略（给 token 分配不同的工作）。前两根杠杆是线性的——换模型有性能下限，跑更久有成本上限。第三根杠杆是非线性的——一个 best-of-n 策略或一个 reflect-and-memory 策略带来的提升，可能远超换大模型或跑更久的线性收益。这正是为什么 Anthropic 把路线图压在策略层。

Angela 在访谈末尾给出了这个方向最具体的案例——bug hunting agent。大多数人卡在两个杠杆上：换更大的模型或让 agent 跑更久。但实验证明，第三根杠杆（best-of-n 并行跑然后取最优）的回报远超前两者：

```plaintext
[44:43] actually if you were to like best of end the thing, it would like give you a lot more returns. [...] we're seeing like this is where the alpha is and it's hard
```

关键约束不是知道这个策略有效——论文里都有——而是把它工程化到生产环境并在真实用户上验证：

```plaintext
[44:56] to actually build that thing and put it into production so you can actually test it on users and see the results for yourself, that's like really really freaking hard.
```

这正是 Anthropic 要做的——把学术界已知但工程上极难的策略，变成平台原语让开发者可以直接使用。Angela 对这个方向的信念溢于言表：

```plaintext
[46:00] we can give you like five jobs off the top of our head and we'll probably like that's what we have internally. Um and if we give this out to the rest of the ecosystem there's probably going to be like 100,000 200,000 who knows what other combinations that people could put together.
```

Anthropic 内部已经有五种 token job 的原型——但开放给生态后，可能会涌现出十万、二十万种组合。这是一个从封闭优化到开放搜索的策略——Anthropic 赌的不是自己能找到最优策略，而是生态的组合搜索空间远大于任何单一团队的探索能力。

---

## 七、双面人格——企业级安全与周末开发者

Katelyn 在访谈最后区分了两类需要服务的用户画像。第一类是企业用户——他们的核心需求是「能不能用」而非「好不好用」：安全合规、模块化、可插入性。他们的 walled garden 要求恰恰是阻碍他们采用创新策略的门槛。

```plaintext
[46:56] I have this like walled garden and I need to figure out exactly how I can plug these solutions in
```

第二类是「周末开发者」——他们想要 hackable、开放的解决方案。Katelyn 承认对这两类人需要不同的策略：

```plaintext
[47:16] the like weekend developer who's like I want to go and build something useful for myself right
```

这个区分揭示了一个结构性张力：策略层的创新（Anthropic 的核心赌注）天然倾向于开放和 hackable——你需要自由组合 token jobs 才能发现最优策略。但企业用户需要的是封闭和可控——他们的 walled garden 恰恰阻碍了策略组合的实验。Anthropic 的平台必须同时服务这两种截然不同的需求，这意味着策略层的原语设计必须足够模块化——企业可以只取「model routing」策略而不开放「reflect-and-memory」策略，而周末开发者可以组合全部。

---

## 八、从客户身上看到的信号——连接层创新与旧系统突破

Angela 在分享客户洞察时给出了两个极具信号价值的观察。

**第一个信号：最有价值的创新不在产品形态层，而在 context 和连接层。** 她描述了一些团队如何巧妙地处理跨系统的 context——主动获取分散在不同地方的权限，然后喂给 agent：

```plaintext
[34:36] we've seen some teams be really clever about like how they do that and they are able to kind of think through like, okay, if I have all these contacts in a bunch of different places, how can I proactively go reach out to them?
```

这些创新「不表现为完全不同的产品形态，但对用户来说最有用」——这恰好验证了 Angela 的三层框架：底层的 knowledge 层和 execution 层趋于稳定后，真正的创新发生在连接这些层的方式上。

**第二个信号：最古老的系统反而是 AI 最先突破的地方。** Angela 描述了医疗公司面临的困境——他们使用的系统甚至没有 API：

```plaintext
[35:52] they're like the systems I'm working with they don't even have APIs. like that's that's a a dream.
```

Computer use 成为了连接这些古老系统的桥梁。这个信号的深层含义是：AI 的价值释放不是从最先进的系统开始，而是从最落后的系统开始——因为那些系统从来没有被数字化过，AI 直接跳过了 API 层用 UI 交互来桥接。

Katelyn 补充了一个 MCP 的 emergent use case——客户把不同平台上构建的 agent 通过 MCP 服务器互相调用：

```plaintext
[37:10] what if I expose an MCP server on top of this agent so that it can then go and like have this other agent call a tool on that agent
```

这是一个 agent-to-agent 互操作的信号——MCP 不只是「agent 调用工具」的协议，正在变成「agent 调用 agent」的协议。如果这个方向成立，MCP 的战略意义就从「标准化工具接口」升级为「标准化 agent 互操作」——而这恰好是 Angela 在前面提到的「transactability across the board」愿景的技术载体。

---

**元信息**

```plaintext
标题: Anthropic's Katelyn Lesse & Angela Jiang: Building an Ecosystem, not a Walled Garden
频道: Sequoia Capital
发布时间: 2026-07-14
时长: 48min 55s
YouTube链接: https://www.youtube.com/watch?v=vPnVTHYplrQ
分析时间: 2026-07-15
```

---

## 深度关联

### 1. Token 工作分配 vs Token 定价危机

**←** [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]]

Katelyn 提出 token 不再 fungible——同一个 token 可以用来执行、反思、建议或记忆，策略层的创新在于找到最优的 token 工作分配。Levie 从企业侧观察到 token 成本正在击穿旧定价模型——单任务可以烧掉 $1000 推理算力，$20/月的 per-seat 定价在物理上不成立。两人的论点构成一枚硬币的两面：Levie 诊断了 token 消费侧的定价危机（企业不知道怎么为 token 付费），Katelyn 给出了 token 供给侧的效率路径（不是用更少的 token，而是让每个 token 做更聪明的事）。Levie 的「AI compute ERP」需求与 Katelyn 的「strategies」原语本质上在解同一个问题——前者是成本可见性，后者是成本可优化性。如果 Anthropic 能把 strategies 变成平台原语，Levie 描述的企业「cap AI usage」困境就有了技术解而非行政解。

### 2. Harness 绑定模型家族 vs 模型商品化宿命论

**→** [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]

Evans 论证基础模型将商品化——电信运营商类比：建了管道但不收水费，没有网络效应、没有定价权。Katelyn 的 harness-binding-to-model-family 论点对 Evans 的论证构成了一个结构性修正：不是模型本身不商品化，而是 model + harness + strategies 的组合不商品化。当 Katelyn 说「harnesses should be tuned to the model family」时，她在说：替换模型的代价不是一次 API 调用的变更，而是整个 harness 和策略栈的重构——这构成了 Evans 所否认的网络效应的替代品。Evans 说「模型之间不存在 Instagram 式的护城河」，Katelyn 隐含的回应是：护城河不在模型层，在 harness-model 绑定层。两人对同一现象的判断方向相反——Evans 看到模型趋同，Katelyn 看到 model+harness 组合的差异化正在加深。Evans 的电信运营商类比因此需要被修正：运营商确实不收水费，但如果水管的铺设方式（harness）和水的使用策略（strategies）被一家公司垄断了接口标准，水费归谁收就变成了一个开放问题。

### 3. 元 harness 与 harness 瓦解管制的共振

**→** [[Diamandis 267- Anthropic vs Alibaba, OpenAI IPO Delays, US Govt Blocks GPT-5.6]]

Diamandis #267 的核心判断是「harness 瓦解管制」——Immad 证明 GLM 5.2 加 harness 在 Frontier SWE 上超越 Mythos，Alex 据此判断「猫已出袋」：已发布模型加 harness 能超越被封锁的新模型。Katelyn 的 strategies/meta-harness 论点与这个判断在方向上一致但层次不同。#267 说的是 harness 可以弥补模型能力差距（旧模型 + 好 harness > 新模型），Katelyn 说的是 harness 可以重新定义 token 的 ROI（同一批 token 做不同的事得到更高回报）。前者是 harness 作为「能力放大器」（让弱模型变强），后者是 harness 作为「资源优化器」（让同样的 token 做更聪明的事）。如果两个判断同时成立，结论是：harness 的杠杆不仅存在于能力层（#267），也存在于经济层（Katelyn）——harness 既能让旧模型超越新模型，又能让同样的 token 预算产出更多智能。这双重杠杆意味着：政府对前沿模型的管制（#267）和对 token 成本的行政控制（Levie）都可以被 harness 层的创新绕过。

### 4. 开放 harness 即平台护城河

**←** [[Satya Nadella- The Rise of the Full-Stack Builder]]

Nadella 提出「开放 harness 是新平台护城河」——平台的定义不在于捕获多少价值，而在于让平台外创造多少价值；私有 eval 是企业 IP，harness 是开放平台。Angela 和 Katelyn 的开放策略与 Nadella 的框架高度一致——self-hosted sandbox、MCP tunnels、标准化安全协议都是「让平台外创造更多价值」的具体实施。但两人之间有一个关键差异：Nadella 的 harness 是多模型的（让企业在不同模型间 hill climb），Katelyn 的 harness 是绑定 Claude 模型家族的（不支持跨厂商路由）。Nadella 赌的是 harness 的模型无关性成为平台价值，Katelyn 赌的是 harness-model 绑定成为差异化来源。这个分歧不是偶然的——它反映了微软（平台公司，需要兼容所有模型）和 Anthropic（模型公司，需要让 harness 放大自身模型价值）的结构性位置差异。Nadella 的「切换测试」（能用模型 A 也能切换到模型 B hill climb）恰好是 Katelyn 不愿意提供的——对 Anthropic 而言，让用户能无缝切换到其他模型等于自毁护城河。

### 5. Token job 与 taste 的互补

**←** [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]

Andrew 论证实现成本归零后，产品瓶颈从「能不能做」迁移到「该不该做」——taste 是在 90 个原型中区分信号与噪声的判断力。Katelyn 的 strategies 论点与这个判断在结构上互补但方向相反。Andrew 说的是人的判断力成为瓶颈（AI 能生成无限原型，但需要人判断哪个好），Katelyn 说的是机器的判断力可以被工程化（把 token 分配给「reflect」和「advise」工作，让 agent 自己判断做得好不好）。Andrew 的 grader 是人，Katelyn 的 grader 是另一个 token job。如果 Katelyn 的策略层足够成熟——agent 能自动反思、自动建议、自动验证——Andrew 所说的 taste 瓶颈就会被部分自动化。但这里有一个循环：谁来设计策略本身？谁来判断「reflect」token 写入记忆的东西是有价值的？答案仍然是人。因此 Andrew 的 taste 判断和 Katelyn 的 strategies 工程不是替代关系，而是递归关系——strategies 把 taste 从「判断每个输出」升级为「判断哪个策略能产生最好的输出」。
