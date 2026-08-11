---
title: "Karpathy- Skill Issue — Code Agents, AutoResearch, and the Loopy Era"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=kwSVtQ7dziU"
transcript: "[[Skill Issue Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI]]"
feishu_doc_id: NQbwdt4DToFxtPx9kRkcrVBinSJ
tags:
  - kol情报
created: 2026-06-08
order: 36
status: canonical
---

# Karpathy: Skill Issue — Code Agents, AutoResearch, and the Loopy Era of AI

> 当你从回路中移除自己，让 Agent 自主运行时，你才真正开始利用这个时代的杠杆——而 Karpathy 认为，这只是'洋葱的第一层'。

—— Andrej Karpathy, No Priors Podcast 2026

视频链接：https://www.youtube.com/watch?v=kwSVtQ7dziU
对应逐字稿：[[Skill Issue Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI]]

概述：2026年3月，Andrej Karpathy（OpenAI 联合创始人、前 Tesla AI 总监）与 Sarah Guo 在 No Priors 播客进行了 66 分钟的深度对话。这场访谈的核心赌注是：AI 的价值释放不在于人机协作，而在于人从回路中退出。从代码 Agent 的精神状态、到 AutoResearch 的自我改进循环、再到教育重定向，Karpathy 描绘了一个「Agent 优先」的世界——而当前的一切，只是'无限洋葱'的第一层。

主题脉络：① 从写代码到表达意志 → ② 宏观动作新范式 → ③ App 不该存在 → ④ AutoResearch 自我改进 → ⑤ 锯齿状智能的断裂 → ⑥ 模型物种分化 → ⑦ 不受信工人池 → ⑧ 数字优先原子滞后 → ⑨ 开源闭源权力平衡 → ⑩ 教育重定向 → ⑪ 独立与判断的两难

## 核心证据校准

> **[1:03]** "I have to code for 16 hours a day or code's not even the right verb anymore"
> **[1:25]** "I don't think I've typed like a line of code probably since December basically."
> **[3:32]** "It's not that the capability is not there."
> **[4:01]** "you can move in much larger macro actions."
> **[4:27]** "Here's a new functionality that's not going to interfere with the other one."
> **[5:07]** "you are the bottleneck in the system that is max capability."
> **[5:33]** "That just means I haven't maximized my token throughput."
> **[6:11]** "I'm the binding constraint."
> **[12:59]** "these shouldn't even exist kind of in a certain sense."
> **[14:04]** "the customer is not the human anymore."
> **[16:34]** "you have to remove yourself as the as the bottleneck."
> **[18:36]** "I did forget like the weight decay on the value embeddings"
> **[21:21]** "A research organization is a set of markdown files"
> **[26:52]** "if you give them an agentic task, they will just go for hours and move mountains for you."
> **[29:48]** "I think we we should be able to see more speciation"
> **[36:09]** "the earth is much bigger and has huge amount of untrusted compute."
> **[39:32]** "flipping bits and and the ability to copy-paste digital information is like makes everything a million times faster than accelerating matter"
> **[42:22]** "you have the Jevons paradox"
> **[45:50]** "if you're inside one of the frontier labs. Like there's some things that you can't say."
> **[1:02:52]** "I'm not explaining to people anymore. I'm explaining it to agents."
> **[1:05:22]** "And this is this is my value add."

# 一、从写代码到「表达意志」——Agent 精神病的诞生

Karpathy 描述了一种被他自己称为「AI 精神病」（psychosis）的状态：2024 年 12 月的某一天，他突然意识到自己的工作方式已经彻底改变了。从 80/20（自己写/Agent 写）翻转到了几乎完全委派——他已经不记得上一次亲手打一行代码是什么时候了。这种转变不是渐进的，而是瞬间的。
```plaintext {wrap}
[02:00] I kind of went from 80/20 of like, you know, to like 20/80 of writing code by myself versus just delegating to agents. And I don't even think it's 20/80 by now. I think it's a lot more than that. I don't think I've typed like a line of code probably since December basically.
```

但精神病这个词不是玩笑。它的核心含义是：当 Agent 失败时，他不再认为是能力不够，而是认为是自己给指令不够好——「一切都是 skill issue」。这种思维翻转本身就是一个范式信号：瓶颈从工具能力转移到了使用者的技艺。
```plaintext {wrap}
[03:34] even if they don't work, I think to a large extent you feel like it's a skill issue. It's not that the capability is not there. It's that you just haven't found a way to string it together of what's available.
```

一个微妙但重要的情绪信号：他说自己「焦虑」（antsy）不是因为做不好，而是因为怕不在最前沿。这种焦虑感的来源不再是「我不会」，而是「我没有最大化我的 token 吞吐量」。GPU 时代的 FOMO 是「我的 GPU 空闲了」；Agent 时代的 FOMO 是「我的订阅额度还有剩」。

# 二、宏观动作——用功能而非函数思考

Karpathy 引用了 Peter Steinberg 的例子：一个显示器上铺满了 Codex Agent，每个都在不同 repo 上工作，大约 20 分钟完成一个任务。Peter 在它们之间来回穿梭，分配任务、审查产出。这不是写代码——这是以「功能」为单位的宏观操控。
```plaintext {wrap}
[04:24] It's not just like here's a line of code, here's a new function. It's like here's a new functionality and delegate it to agent one. Here's a new functionality that's not going to interfere with the other one. Give it agent two.
```

这个场景揭示了一个更深的结构性变化：工程工作的组织单位从「函数」变成了「功能」，从「行」变成了「宏观动作」。你的角色不再是实现者，而是调度者——一个同时管理 10 个 Agent 的指挥。这种并行化带来的焦虑是：每当你在等一个 Agent 完成时，你都应该在给另一个 Agent 派活。人是瓶颈。

## 2.1 Dobby 与 Agent 人格

Karpathy 给他的智能家居 Agent 取名叫 Dobby（家养小精灵），通过 WhatsApp 对话。Dobby 扫描局域网发现 Sonos 音响、逆向工程 API、控制灯光/空调/窗帘/泳池/安防——三句话就能播放音乐。他说「我不需要用六个 App 了」——这是对现有软件形态的根本性否定。
```plaintext {wrap}
[10:19] I can't believe I just typed in like, 'Can you find my Sonos?' and then suddenly it's playing music.
```

但更值得关注的是他对 OpenClaude（Peter Steinberg 的项目）人格设计的评价：Agent 的个性不是装饰——它影响使用体验和信任度。他说 Claude 的赞美「恰到好处」，让他「试图赢得它的认可」，而 Codex「太干了」。这种看似主观的偏好实际上指向一个产品判断：在 Agent 时代，人格是核心产品属性，不是锦上添花。

# 三、App 不该存在——Agent 优先的世界重构

从 Dobby 的经验出发，Karpathy 推出了一个更具破坏性的判断：很多 App 根本不该存在。它们只是因为人类需要一个界面来操作硬件/服务才被创造出来的。在 Agent 优先的世界里，正确的架构是：暴露 API，让 Agent 做胶水层。
```plaintext {wrap}
[13:11] there's this sense that these apps that are on the app store for using these smart home devices, etc. these shouldn't even exist kind of in a certain sense. Like shouldn't it just be APIs and shouldn't agents be just using it directly?
```

这个判断的含义远超智能家居。他明确说「客户不再是人，而是代表人的 Agent」。整个行业需要围绕这个前提重构。当前的 App 生态、UI/UX 设计范式、甚至 SaaS 的商业模式，都建立在一个即将过期的假设上：终端用户是人类。
```plaintext {wrap}
[14:16] the customer is not the human anymore. It's like agents who are acting on behalf of humans and this refactoring will probably be substantial.
```

# 四、AutoResearch：把自己从回路中移除

AutoResearch 是这场访谈的核心实验。Karpathy 的基本论点是：要最大化 Agent 的杠杆，你必须把自己从回路中移除——不能每次都由你来提示下一步。AutoResearch 就是一个自行设计实验、训练模型、优化参数的闭环系统。
```plaintext {wrap}
[16:44] to get the most out of the tools that have become available now you have to remove yourself as the bottleneck. You can't be there to prompt the next thing. You need to take yourself outside.
```

令人震惊的结果：Karpathy 用 20 年的经验手工调优了 nanoGPT，自认为已经很充分了。然后让 AutoResearch 跑了一夜——它找到了他遗漏的调优项：value embedding 上的 weight decay 被忘了，Adam betas 没有充分调优，而这些参数是相互耦合的。
```plaintext {wrap}
[18:45] I let auto research go for like overnight and it came back with like tunings that I didn't see. I did forget like the weight decay on the value embeddings and my Adam betas were not sufficiently tuned and these things just jointly interact.
```

他说这只是一个单循环。前沿实验室有数万 GPU 的集群，可以做远超于此的自动化。关键洞察：先在小模型上大量探索，再外推到大模型——这就是「AutoResearch」对前沿实验室的真正价值。

## 4.1 program.md：研究组织就是一组 Markdown 文件

这里出现了一个重要的递归结构：每个研究组织都可以被描述为一组 markdown 文件（定义角色、流程、协作方式）。既然是代码，就可以被优化。他提出了一个竞赛想法：让不同人写不同的 program.md，用相同硬件看谁进步最大，然后用这些数据让模型写一个更好的 program.md。
```plaintext {wrap}
[21:38] A research organization is a set of markdown files that describe all the roles and how the whole thing connects. And you can imagine having a better research organization. So maybe they do fewer stand-ups in the morning because they're useless.
```

这是一个极其激进的论点：研究组织的效率是可以被量化和优化的——就像代码一样。而人类研究者正在做的大部分事情（站会、流程、审查）可能只是「还没被 AutoResearch 发现的低效行为」。

# 五、锯齿状智能——可验证域与非可验证域的断裂

但 Karpathy 并非盲目乐观。他用了两个警示性前提（caveats）：第一，AutoResearch 只适用于有客观评估指标的任务——写更快的 CUDA 核、优化训练 loss——「如果你不能评估，你就不能 AutoResearch」。第二，当前系统还在「缝里冒泡」，推得太远会适得其反。

他用一个精准的比喻描述了当前模型的状态：同时像「一个一辈子的系统程序员级别的杰出博士生」和「一个 10 岁小孩」。这种锯齿状（jaggedness）是人类不具备的——人类的能力更耦合，不会同时极端强和极端弱。
```plaintext {wrap}
[24:43] I simultaneously feel like I'm talking to an extremely brilliant PhD student who's been like a systems programmer for their entire life and a 10-year-old.
```

最生动的例证：你让 ChatGPT 讲个笑话，它仍然讲那个「为什么科学家不信任原子？因为它们组成了一切（make everything up）」——和三四年前一模一样。这不是能力不够，而是幽默不在 RL 的奖励信号里。代码能力在 RL 中被优化了，但笑话没有被——所以模型的「智能」在可验证域和非可验证域之间存在结构性断裂。
```plaintext {wrap}
[26:52] even though the models have improved tremendously and if you give them an agentic task, they will just go for hours and move mountains for you. And then you ask for like a joke and it has a stupid joke. It's crappy joke from five years ago.
```

# 六、物种分化——模型的未来不是单一文化

Sarah 问了一个关键问题：如果锯齿状持续存在，是否应该把模型「拆包」成不同领域的专家？Karpathy 的回答：当前实验室在追求一个「通晓一切的单一文化模型」，但他认为应该预期更多的「物种分化」——类比动物王国中不同大脑的多样性。
```plaintext {wrap}
[29:52] the animal kingdom is extremely diverse in the brains that exist and there's lots of different niches of nature and some animals have overdeveloped visual cortex or other kind of parts and I think we should be able to see more speciation.
```

但他坦承目前还没看到太多分化，仍然是单一文化。原因有二：一是服务端模型不知道终端用户会问什么，所以必须多任务覆盖；二是「操控大脑的科学」还没成熟——微调会丢失能力、持续学习还没解决、触碰权重比触碰上下文窗口危险得多。

# 七、不受信工人池——AutoResearch@home

Karpathy 在这里提出了一个极其大胆的构想：借鉴 Folding@home 和 SETI@home 的模式，让互联网上不受信的工人池协作改进 LLM。核心逻辑：找到一个好解很贵，但验证一个候选解是否有效很便宜——这正是区块链式的「工作证明」，只不过区块换成了代码提交（commit）。
```plaintext {wrap}
[34:40] the proof of work is basically doing tons of experimentation to find the commits that work. Um and that's hard and then the reward is just being on the leaderboard right now.
```

更激进的部分：「地球比任何前沿实验室都大得多，拥有海量的不受信算力。如果建立了正确的验证系统，这个群体可能跑赢前沿实验室。」他甚至设想了类似信息市场的机制：你关心某个研究课题（比如癌症），就购买算力加入那个 AutoResearch 池。
```plaintext {wrap}
[36:09] a swarm of agents on the internet could collaborate to improve LLMs and could potentially even like run circles around frontier labs.
```

# 八、数字优先，原子滞后——物理世界的时间差

Karpathy 对数字世界和物理世界的速度差异做了一个清晰的判断：数字空间将以「光速」变化，而物理世界将滞后——因为「操纵原子比翻转比特难一百万倍」。他自己的优先级排序：现在是数字空间，然后是数字与物理的接口（传感器+执行器），最后才是纯物理世界。
```plaintext {wrap}
[39:31] flipping bits and the ability to copy-paste digital information is like makes everything a million times faster than accelerating matter.
```

但他同时指出：物理世界的总市场可能远大于数字世界——只是时机未到。他提到朋友 Liam 创办的 Periodic（材料科学 AutoResearch）——在那里传感器就是昂贵的实验室设备。这暗示了下一个大机会的方向：谁能搭建数字智能与物理世界的传感器/执行器接口，谁就拥有下一波浪潮。

## 8.1 就业市场的 Jevons 悖论

关于就业影响，Karpathy 给出了一个相对谨慎乐观的判断：软件工程的短期需求会上升——不是因为 AI 替代不了，而是因为 Jevons 悖论。软件之前太贵了，所以需求被压抑。当成本下降，需求会释放。经典的 ATM 例子：ATM 让银行网点运营成本降低 → 更多网点 → 更多柜员。
```plaintext {wrap}
[42:23] So if the barrier comes down, then actually you have the Jevons paradox, which is like you know, you actually the demand for software actually goes up.
```

但他也承认：长期来看，前沿实验室的研究者本质上就是「高级版 AutoResearch」，正在主动自动化自己的工作。他回忆在 OpenAI 走访时跟研究者说「你们意识到如果成功了我们全都失业了吧」。这不是玩笑——这是一个正在自我实现的预言。

# 九、开源与闭源：Linux 式的权力平衡

Karpathy 用操作系统类比来理解开源/闭源的动态：闭源模型就像 Windows/macOS，开源模型就像 Linux。当前开源落后大约 6-8 个月，但在收敛。他说「我们意外地处于一个还不错的位置」——开源存在作为全行业的公共平台，闭源继续推进前沿。
```plaintext {wrap}
[49:48] I'm a huge fan of open-source, obviously. So for example, in operating systems, you have like closed source, like Windows and Mac OS... and there's Linux. But Linux is very easy. Like, actually Linux is extremely successful project.
```

但他有一个明确的担忧：中心化智能的系统性风险。作为东欧裔，他对权力集中有本能的警惕。他希望开源继续存在——不一定要在最前沿，但作为「整个行业可以安全使用的公共智能平台」。
```plaintext {wrap}
[52:02] I'm by default very suspicious of like... I want there to be more people in the room. I want... ensembles of people thinking about all the hardest problems.
```

# 十、教育重定向——对 Agent 解释，而非对人

访谈最后，Karpathy 讲了 microGPT 项目引出的一个教育观变化。他说，以前他会录视频、写指南来教人理解代码。但现在他意识到：microGPT 只有 200 行，任何人的 Agent 都能解释它——所以他不应该是「对人解释」，而应该是「对 Agent 解释」。
```plaintext {wrap}
[63:09] I'm not explaining to people anymore. I'm explaining it to agents. If you can explain it to agents, then agents can be the router and they can actually target it to the human in their language with infinite patience.
```

这个判断的含义是：未来的文档应该是 markdown 给 Agent 读的，不是 HTML 给人读的。教育从「人教人」变成「人定义课程 → Agent 个性化教学」。但他也承认了一个当前边界：Agent 理解代码没问题，但它自己写不出 microGPT——那个 200 行的极致简化是他二十年的执念，是他的「少数几个信息位」的价值。
```plaintext {wrap}
[65:27] This is my value add. Everything else like agent gets it. It just can't come up with it, but it totally gets it and understands why it's done in a certain way.
```

# 十一、实验室之外——独立性与判断力的两难

Sarah 问了一个尖锐的问题：为什么不在前沿实验室做 AutoResearch？Karpathy 的回答揭示了一个结构性困境：在前沿实验室内部，你不可能是完全自由的——你有财务激励的错位（公司股价和你的话语绑定），有「不能说的事」和「应该说的话」的压力。但在外部，你的判断力会因为看不到内部进展而逐渐漂移。
```plaintext {wrap}
[46:06] you can't actually like be part of that conversation in a fully autonomous free way. Like if you're inside one of the frontier labs. Like there's some things that you can't say.
```

他认为的理想形态是「来回切换」——在前沿实验室待一段时间，保持判断力的校准，然后离开保持独立性。他说 Noam Brown（OpenAI 研究者）最有影响力的工作可能恰恰在实验室之外。这是一个关于 AI 治理和知识权力的深层信号：谁有权看到最前沿的能力，谁就被激励结构束缚；谁保持独立，谁就逐渐失去判断的准确性。

这是一个关于 AI 治理和知识权力的深层信号：谁有权看到最前沿的能力，谁就被激励结构束缚；谁保持独立，谁就逐渐失去判断的准确性。这种两难在 AI 影响越来越大的未来只会加剧——而 Karpathy 的「来回切换」方案，可能也是我们目前能想到的最好解法。

---

元信息
```plaintext {wrap}
标题: Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI
频道: No Priors: AI, Machine Learning, Tech, & Startups
发布时间: 2026-03-20
时长: 66min 31s
YouTube链接: https://www.youtube.com/watch?v=kwSVtQ7dziU
分析时间: 2026-06-03
```
