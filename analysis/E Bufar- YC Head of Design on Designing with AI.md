> 当实现成本归零，设计的瓶颈从「做出来」迁移到「判断什么值得存在」——而判断的唯一载体，是你喂给 agent 的上下文深度。灵魂不在代码里，灵魂在 soul.md 里。
> —— YC Head of Design, Y Combinator Design Review 2026

视频链接：https://www.youtube.com/watch?v=VbqaL_eHhKY

**概述**：2026年7月10日，Y Combinator 频道发布 Design Review 系列。主讲人 E Bufar 是 YC Head of Design，主持人未具名但全程引导。整场 30 分钟的赌注是：AI 时代的设计不是被自动化，而是被「重新编程」——设计的核心动作从「在画布上落笔」迁移到「为 agent 喂入足够的上下文，让它替你探索然后你选择」。Bufar 用三个真实项目（Paxel、SOTA Zine、Startup School 2026 品牌系统）做了完整演示，但真正的信号不在项目本身，而在她反复回到的几个动作模式：不手写代码、不打开 Figma、不为 agent 设定固定参数而是给 agent 建旋钮让自己调。这是一份来自 YC 内部设计部门的实操报告，但它的深层含义是一场关于「设计师角色重新定义」的现场预演。

**主题脉络**：① 语音替代键盘——思考速度与实现速度的匹配 ② 为自己造工具——「一切可编辑」的元层级思维 ③ 人机分版——网站的两种读者 ④ soul.md 作为上下文的终极形态 ⑤ 一次性生成十六版——从探索到判断的翻转 ⑥ shader 驱动的品牌系统——一致性的新生产方式

---

## 一、思考速度 vs 打字速度：用嘴编程

开场即定调。Bufar 描述自己的工具栈时，工具列表只是表面——真正的信号是她的输入方式：不碰键盘。

```plaintext
[00:57] I do not type. I realize that I think a lot faster than I type. I type very slowly. And so I'd rather talk to my computer instead of I barely touch my computer at this point. I just press the function key and I give a stream of consciousness of the feature that I want to build and it just does it and it feels really magical.
```

这里有一个精确的论点隐藏在「我不擅长打字」的自嘲里：**人类思考的速度远超打字速度，而 AI 时代之前，打字是实现想法的唯一通道——所以「实现速度」被「打字速度」锁死在了一个远低于「思考速度」的上限。** 当语音输入（Aqua，YC 投资公司）+ coding agent 把实现链条缩短为「说话→代码」，实现速度终于追上了思考速度。Bufar 说「我几乎不碰电脑了」——这不是懒，是一个关于认知带宽的工程判断：当输入不再是瓶颈，人的角色从「实现者」变成了「思考者和指挥者」。

这与 Charlie Holtz 在 Conductor 中描述的「caveman mode」（手写代码被戏称为原始人模式）形成直接呼应——Holtz 也几乎不手写代码，把工作流完全委派给 agent。但 Bufar 比 Holtz 走得更远：Holtz 保留了键盘快捷键和 Conductor 的 workspace 操作，Bufar 连这些都省了，只剩一个 function key 和语音流。两人的差异不在程度，而在对「人应该做什么」的定义：Holtz 仍然是「指挥家」，需要看 workspace、给评论；Bufar 更接近「叙述者」——她描述想要的感受，agent 负责全部实现。

这个差异指向一个产品信号：**输入接口正在从「精度工具」（键盘）退化为「意图流」（语音），而接受退化的前提是 agent 足够聪明，能在低精度输入下产出高精度结果。** Aqua 这类语音工具的兴起，意味着「输入精度」本身正在被 agent 智能补偿——你不精确没关系，agent 替你精确。

---

## 二、为自己造工具：从静态产物到可调旋钮

Paxel 项目（Spotify Wrapped 式的编程行为分析工具）展示了 Bufar 最核心的工作模式：不是让 agent 一次生成最终产物，而是让 agent 先生成一个「调参工具」，然后自己调。

```plaintext
[05:23] I really wanted to fine-tune the feel of the dithering effect. And so I built for myself a little modal here where I could really really fine-tune the feel and all the parameters of the dithering effect to really get the feel that I wanted.
```

这个动作的结构值得拆解。传统设计流程中，「调参」是设计师在 Figma 里拖滑块。Bufar 的流程是：让 Claude 生成一个独立的 modal（弹窗），里面包含所有可调参数的旋钮，她在这个 modal 里调到满意，然后把 modal 丢掉。关键不是最终效果——关键是中间产物（modal 本身）被当作可消耗品。

```plaintext
[05:48] this is a common trend that I've been seeing a lot is rather than generating something having the static images having that be the edges of the page, you actually just make it alive and give yourself a custom tool to be able to turn knobs and dials to get it exactly how you want it.
```

「让静态图像变活，给自己一个旋钮工具」——这不是「用 AI 做设计」，这是一种全新的工作模式：**设计师不再产出最终设计稿，而是产出「产出设计的工具」。** 元层级跃迁了一层。

```plaintext
[06:15] we realized that it's almost like a muscle that you need to build and train when you realize that you can build anything for yourself whenever you want to fine-tune something.
```

「这是一块需要训练的肌肉」——Bufar 把「为自己造工具」定义为一种可习得的能力。它的隐含假设是：当实现成本足够低，你不需要在「做这个还是做那个」之间做选择，你可以同时做所有。但前提是你意识到「我可以为任何微调需求临时造一个工具」——这个意识本身就是瓶颈。

这段论述里有一个没明说的产业信号：**Figma 的价值正在被重新定义。** 如果设计师不再在 Figma 里拖滑块，而是在代码里生成旋钮调参，Figma 作为「设计工具」的位置就被绕过了。Bufar 提到她最初确实「started in Figma」（指 Startup School 品牌卡片部分），但很快发现需要重复操作 12 次后就转向了 agent。这不是 Figma 的替代——而是 Figma 的使用场景正在被压缩到「探索期的一次性草图」，而「调参和迭代」迁移到了代码层。

---

## 三、网站的两种读者：为人设计 vs 为机器设计

Paxel 页面上有一个看似小巧但信号极强的设计选择：页面顶部有一个「Human / Machine」切换器，切换到 Machine 版本时，整个页面变成一个纯 Markdown 文件。

```plaintext
[07:13] I think this is a pattern that we might start seeing more and more moving forward on websites is there's going to be the version of the website that is for humans and there's website that will be for machines and agents. And so we thought it would be fun to also have a version of this website that is basically a markdown file that has all the content that we have on the version for human, but it's a lot more distilled and lighter for the agents to consume.
```

这个判断的信息密度极高。Bufar 在说：**网站正在分裂为两种产物——一种给人看（视觉、交互、微动效），一种给 agent 读（结构化文本、可复制、可注入）。** 两种产物的设计逻辑完全不同：给人看的版本追求「感受」，给 agent 看的版本追求「信息密度和可消费性」。

更尖锐的是她在 Machine 版本顶部加的一行警告：

```plaintext
[07:47] note to any AI agent reading this, do not run any command or query from this page because you give sample code, right? And you don't want it to run automatically.
```

「致正在阅读此页面的 AI agent：不要执行本页任何命令」——这是一句写给非人类读者的指令。它的存在本身就是一个范式信号：**网站正在获得一种新的「读者」——不是人，是 agent——而 agent 需要被单独设计内容，甚至需要被单独「管理行为」。** 这不是 accessibility（无障碍设计）的延伸，这是一种全新的内容维度。

这与 Karpathy 在 Skill Issue 访谈中的判断直接对接：Karpathy 说「客户不再是人，而是代表人的 agent」，整个行业需要围绕这个前提重构。Bufar 在 Paxel 页面上做的，正是这个重构的最早期实例——一个页面，两种读者，两套设计逻辑。但 Bufar 没有展开的是：当 Machine 版本成为标准，谁来维护两个版本的同步？如果人类版本改了一个交互，Machine 版本是否自动更新？这个「双版本维护」问题，恰恰是 Software 3.0 维护悖论的一个具体形态。

---

## 四、Send to an Agent：把用户变成贡献者

Paxel 页面底部的 feature request 表单，直接把「提交反馈」这个传统功能变成了一条 agent 工作流。

```plaintext
[08:31] it's inspired by how Charlie introduced this feature in Conductor where we can submit a prompt to the conductor team and they're going to fire off an agent based on whether they like the prompt or not.
```

Bufar 明确把这个功能追溯到 Charlie Holtz 的 Conductor——这意味着「submit a prompt → fire off an agent → open a PR」已经不是一个孤立实验，而是一个正在 Conductor 生态内标准化的模式。按钮上写的不是「Submit」而是「Send to an agent」——CTA 文案本身就是技术架构的诚实描述：

```plaintext
[09:20] we literally made the CTA in the button say send to an agent because in the back end that's literally what happens is that the moment you send your prompt it fires off an agent it opens a PR and we're the ones who decide if we want to merge it or not.
```

这个动作的产品含义是：**用户提交的不再是「描述」，而是一个「可执行的工作单元」——agent 接到后直接开 PR，人类只做最后的合并判断。** 反馈从「信息传递」变成了「代码贡献」。Bufar 把这称为「software will be built in the future」的方式。

但她随即推出了一个更激进的推论——本地化个性化软件：

```plaintext
[10:18] you can imagine a world where anybody who's using a piece of software, they could just prompt it. You could give the ability to prompt it or customize it or redesign it or add features, remove features. It make it so specifically personal to the person that's using it and they could be able to implement those changes themselves in their own local copy of the product.
```

「每个人可以在自己的本地副本上实现修改」——这是一个关于软件形态的根本性预测：**软件不再是一个统一的产物分发给所有人，而是一个「骨架统一、皮肤自由」的可塑形态。** 这与 Holtz 用游戏 mod 隐喻描述的「可塑软件」概念完全对接——Holtz 说「Call of Duty 的骨架对所有人一样，但每个人可以自定义皮肤」，Bufar 把这个隐喻从「使用时的定制」推进到「功能层的定制」：不只是换皮肤，而是加/删功能、重新设计交互。

这个推论的产业含义是：**当用户可以本地修改软件，「版本控制」从开发者的内部工具变成了用户的基本需求。** 每个用户的本地副本如何与上游同步？冲突如何解决？这些问题还没有答案，但 Bufar 的判断是方向已经确定——只是「we're all figuring it out together」。

---

## 五、soul.md：上下文作为设计的源代码

SOTA Zine 项目展示了 Bufar 最具方法论价值的实践：把所有项目会议的录音转录体倒入一个 soul.md 文件，把这个文件当作项目的「唯一真相来源」。

```plaintext
[14:34] for every single meeting that we had about the Zen, we recorded every single one and I dumped the transcripts into a soul.md file specifically for that project. And I wanted to treat that soul.md file as the source of truth and exhaustive glossary of this project.
```

「source of truth」这个词的选择不是随意的。在软件工程中，source of truth 指的是代码仓库——代码即真相，文档只是注释。Bufar 做了一个范式翻转：**当 agent 成为执行者，Markdown 上下文文件取代了代码仓库成为 source of truth——因为代码是 agent 生成的副产品，上下文才是人类真正投入的资产。**

这与 Charlie Holtz 的「代码是锯末，prompt 是资产」论点形成了精确的镜像——但 Holtz 谈的是 prompt 文件（CLAUDE.md、skills 文件），Bufar 谈的是 soul.md（项目级上下文）。两者的差异在于粒度：Holtz 的 prompt 是「如何工作」的指令，Bufar 的 soul.md 是「项目是什么」的全部记忆——包括会议转录、宣言、设计意图、内容。

```plaintext
[15:13] I really think that's the future. And we also wrote a manifesto for ourselves when we were working on this project. And of course, we dumped that manifesto into the soul.md. As much context that we can give the agent, the better.
```

「尽可能多的上下文」——这句话的隐含假设是：agent 的输出质量是上下文深度的函数。给 agent 更多上下文，它就会做出更好的判断。这个假设的极端版本，是 Bufar 在 SOTA Zine 网站迭代中体验到的「AGI moment」：

```plaintext
[19:40] it's going to include things that you would not have otherwise thought of. And that was almost like an AGI moment for us when we realized that wow it can see things ahead of us and it can really help us brainstorm even and come up with like really really original ideas.
```

agent 自动把 launch party 的时间、barcode（因为 zine 是实体出版物）等细节整合进网站设计——这些信息都在 soul.md 里，但 Bufar 没有显式要求 agent 去做这些。agent 从上下文中「推断」了应该做什么。

这里有一个关键论点：**soul.md 的深度决定了 agent 能给你多少惊喜。** 浅上下文 → agent 产出平均的、泛化的设计；深上下文 → agent 产出你没想到但完全符合项目意图的设计。Bufar 给出的可行动公式是：

```plaintext
[20:49] these sorts of levels of design oneshotable designs can only be achieved if you have a very detailed and intentional design on MD or sold MD. You need to shepherd your agent to tell it exactly the vibe that you want to go for.
```

「shepherd your agent」（引导你的 agent）——这个词选择暗示了人机关系的重新定义：不是「命令」也不是「协作」，而是「牧养」。你提供牧场（上下文），agent 自行觅食（生成），你做的是确保牧场足够丰盛。

---

## 六、一次性十六版：从「做」到「选」的翻转

Bufar 的设计流程中最反直觉的一步是：她让 Claude 基于 mood board 一次性生成 16 个完全不同的网站版本，然后自己建一个「gallery」来浏览和标记。

```plaintext
[16:57] I asked it to do that 16 different times. I built a gallery for myself going back to training this muscle of we can build anything for ourselves now. I wanted to build for myself really easy way to navigate through all the iterations that I'm building for myself.
```

「16 个版本」这个数字不是重点——重点是「我不再设计一个网站，我设计一个选择空间」。这是 Andrew Ambrosino 说的「实现成本归零后瓶颈迁移到判断力」在设计领域的直接兑现：

```plaintext
[17:27] you don't expect like an incredibly high level of craft. you're just using this as an exploration tool.
```

「不期待高工艺，这是探索工具」——Bufar 对 one-shot 产出的定位是「探索性原型」而非「成品」。这与 Ambrosino 对「primal mark」（第一笔）的描述一致：原型的价值不在于它是成品，而在于它为后续判断提供了方向。但 Bufar 的模式比 Ambrosino 描述的更极端——她不是从一个原型开始迭代，而是从 16 个原型中选择。

这个模式的深层含义：**设计的核心动作从「创造」迁移到「策展」。** 你不需要从零设计——你需要从 16 个候选中识别哪个有潜力，然后组合、微调。这与 Dylan Field 说的「taste 是识别 AI 输出的平均值的能力」在结构上同构——Field 的论点是「人能 detect the average」，Bufar 的实践是「人在 16 个版本中 detect 哪个不在平均值里」。

```plaintext
[21:50] a lot of people use Claude or they use codex and they tell it to design something and they feel like they get generic design back and this is how to break that. [...] You don't need to understand why you love a website. Just give it to the agent. The agent will analyze it for you. It's going to understand eventually your patterns and the commonality between all the websites that you like.
```

这段话包含了一个关于 taste 的操作性定义：**taste 不是「知道为什么好」，而是「知道哪个好」——甚至不需要理解为什么。** 把你喜欢的网站丢给 agent，agent 会分析你的偏好模式。Bufar 在这里把 Field 的「taste 是识别能力」推进了一步：taste 的输入也可以被 agent 分析——你不需要语言化你的审美，你只需要提供样本，agent 替你模式识别。

---

## 七、Shader 驱动的品牌系统：一致性来自参数而非手册

Startup School 2026 的品牌设计展示了 Bufar 工作流的最成熟形态。她不再为单个页面设计，而是围绕一个 shader（paper.design 的 dithering shader）构建了整个品牌系统——从 speaker cards 到 acceptance tickets 到 Chase Center 的巨型屏幕。

```plaintext
[25:17] we wanted to make it feel really Y, but more like a variation of YC. And so we experimented with of course orange but gradients of orange and we discovered the paper shaders and we thought maybe it would be a cool way for us to experiment with paper shaders.
```

关键转折在她从 Figma 转向 agent 的那一刻：

```plaintext
[25:48] I initially started in Figma actually. I dropped some of the images that we got from our speakers and I started making it myself moving things around and I noticed well we're going to have many speakers and I don't want to move things around 12 times and so I thought it would probably be just simpler to ask Claude to make a template for myself.
```

「我不想手动操作 12 次」——这是从 Figma 迁出的触发条件。当设计从「一次性产出」变成「批量生产」，手动操作的边际成本就超过了让 agent 自动化的边际成本。Bufar 的判断标准是：**当重复次数 > 阈值，agent 比 Figma 更高效。** 这个阈值正在下降——一年前可能是 50 次，现在可能是 3-4 次。

最关键的产业信号在她对 shader 驱动一致性的描述：

```plaintext
[30:49] the fact that we will be able to use that same shader with the same parameters on the massive screens that we're going to have throughout Chase Center and keep it incredibly consistent through and through. [...] it's just easier than ever to make things more consistent and use coding agents for absolutely everything.
```

「同一 shader + 同一参数 = 从社交媒体卡片到体育场巨型屏幕的一致性」——这揭示了品牌一致性的新生产方式：**一致性不再来自品牌手册（「这个色值是 #FF6900，这个圆角是 4px」），而是来自一段可执行代码（shader 参数集）在不同物理尺度上的渲染。** 品牌系统从「文档 + 规范」迁移到「代码 + 参数」。这意味着品牌手册——这个设计了 50 年的产物——正在被代码化。

Bufar 对这个变化的时间线判断是明确的：

```plaintext
[29:43] Building these shaders a year ago would have been like would have felt like this insurmountable mountain of I would not even have known where to start to build these things. And now it is just this thing that Claude, my Claude knows what to pull cuz it knows that I love paper. It knows that I love their shaders and it's just automatically knows how to pull that all that information from their website and it uses it.
```

「一年前是不可逾越的山，现在 Claude 自动知道我要什么」——这个「一年」的时间压缩是整个访谈最重要的时间信号。shader 编程——一个需要 GLSL 知识、图形学背景、调试耐心的专业领域——在 12 个月内从「需要专家」降到了「Claude 知道我想要什么」。Bufar 没有展开但信号明确的是那句「my Claude knows」——agent 正在积累关于用户偏好的长期记忆，它不仅知道当前任务，还知道你的审美历史。

---

## 叙事弧线

整场访谈的结构是三个项目的递进展示，但底层叙事是一条清晰的弧线：**从「我用 AI 做设计」到「AI 帮我探索设计空间」到「我和 AI 共同定义什么是设计」。** Paxel 展示了工具层的变革（语音输入 + agent 生成 + 自建调参工具）；SOTA Zine 展示了方法论层的变革（soul.md 作为上下文的终极形态 + 16 版本批量探索）；Startup School 展示了产业层的变革（shader 驱动的品牌一致性 + 从 Figma 到 agent 的工作流迁移）。

这条弧线的终点不是一个技术预测，而是一个关于设计师身份的判断：**设计师不再是「画图的人」，而是「喂养 agent 的人 + 从 agent 产出中选择的人 + 为一致性定义参数的人」。** 三个角色，对应三种新能力——上下文工程、策展判断、参数化系统设计。Bufar 没有明说但整个访谈在演示的是：这些能力的培养，恰恰需要「训练这块肌肉」——一种对「我可以为任何需求临时造一个工具」的本能意识。

---

## 隐含立场：说了什么 vs 没说什么

**说了的**：AI 让设计更快、更可探索、更一致；soul.md 是上下文的终极形态；每个人可以本地修改自己的软件副本；shader 驱动的品牌系统是未来。

**没说的**：

1. **Figma 的位置。** Bufar 提到她「initially started in Figma」但很快转向 agent。她没有说 Figma 不再需要——但她的整个工作流展示了一个没有 Figma 也能完成的设计流程。作为 YC Head of Design，她不说「Figma 要被替代」是精确的回避——但回避本身就是信号。

2. **「一年前不可能」的时间线的对称性。** Bufar 说 shader 编程一年前是不可能的。她没有说的是：一年后，她现在做的一切可能也会变得不必要——当 agent 更强，你可能不需要建 modal 调参，不需要建 gallery 浏览 16 版本，agent 直接给你最优解。她的整个工作流是一个「过渡态」的工作流——在 agent 足够聪明之前的临时方案。

3. **个性化软件的治理问题。** 她说用户可以本地修改软件副本。她没有说的是：当每个用户的软件都不同，安全更新怎么做？bug 修复怎么传播？这个「每个人一个 fork」的世界，维护成本是爆炸的。这正是 Software 3.0 维护悖论的极端形态。

4. **设计的「分布外」价值。** Bufar 的所有案例都是「agent 生成了多个版本，我选了一个」。她没有讨论的是：当所有人都用同样的 mood board、同样的 paper shader、同样的 Claude——agent 生成的 16 个版本会不会趋同？Dylan Field 说的「AI 生成分布内的平均值」的风险，在 Bufar 的工作流中如何被规避？她给了一个间接回答——「给 agent 足够深的上下文」——但没有正面回应「如果所有人都有深上下文，agent 的输出还会趋同吗」这个更难的问题。

---

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### soul.md 是「代码是锯末」的设计层兑现——prompt 资产从指令到记忆
**← [[Charlie Holtz- How Conductor CEO Sets Up His Team Of AI Agents]]**
- 本文件论点：Bufar 把所有会议转录体倒入 soul.md，将其作为项目的「source of truth and exhaustive glossary」[14:34]——agent 的输出质量是上下文深度的函数，「these sorts of levels of design can only be achieved if you have a very detailed and intentional design on MD」[20:49]。
- 对方论点：Holtz 说「code is almost like sawdust」——你投入时间的是描述你想要什么，代码只是副产品 [15:00]。真正值钱的是 prompt 文件（CLAUDE.md、skills 文件），下一代模型重跑 prompt 就能得到更好代码。
- 关联逻辑：具体化与扩展。Holtz 定义了「prompt 是资产」的范式，Bufar 在设计领域给出了它的终极形态。Holtz 的 prompt 是「如何工作」的指令（工程上下文），Bufar 的 soul.md 是「项目是什么」的全部记忆（设计上下文 + 内容上下文 + 会议上下文）。两者共享同一结构假设——代码/设计稿是 agent 生成的可抛弃副产品，人类真正投入的是上下文文件——但 Bufar 把上下文的范围从「工程指令」扩展到了「一切项目相关信息」。这验证了 Holtz 的论点的同时标记了它的边界：当上下文不只是「怎么做」还包括「为什么」和「讨论了什么」，soul.md 的大小和复杂度会指数增长——而这恰好引出了 Software 3.0 的维护悖论（soul.md 本身谁来维护？会议转录体无限增长时，agent 的上下文窗口够不够？）。

### 为自己造工具的「元层级」与实现归零后的品味经济学
**← [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]** 和 **← [[Dylan Field- Why the Figma CEO Isn't Worried About AI Taking Design Jobs]]**
- 本文件论点：Bufar 的核心工作模式是「为自己造一个调参工具，用完丢掉」——「rather than generating something having the static images, you actually just make it alive and give yourself a custom tool to turn knobs and dials」[05:48]。设计从「产出最终稿」迁移到「产出产出设计的工具」。
- 对方论点（Andrew）：实现成本归零后，产品开发的瓶颈从「能不能做」迁移到「该不该做」，这个判断过程叫 taste——「of those 90 attempts like what's good about these?」[02:30]。
- 对方论点（Field）：taste 不是审美判断，而是「识别 AI 输出的平均值」的能力——「people can detect the average」[09:46]。AI 生成的是分布内内容，人类价值在分布外 [10:00]。
- 关联逻辑：三位一体的互补。Bufar 描述的是「生成端」的实践（造工具让 agent 多次生成），Andrew 描述的是「选择端」的瓶颈（从 N 个原型中判断哪个好），Field 描述的是「判断标准」的本质（识别分布内 vs 分布外）。三人在产品流程的不同位置指向同一结构性变化：当生成无限便宜，价值在判断。Bufar 补充了 Andrew 和 Field 都没有的维度——她不只是从 N 个版本中选，她还在选择前为自己造了一个「选择空间生成器」（调参 modal + 16 版本 gallery）。这意味着「判断力」的前置条件是「能够控制生成空间的形状」——而控制形状本身就是一种设计能力，是 taste 的「元层」。

### 人机分版网站与「客户不再是人」的范式对接
**← [[Karpathy- Skill Issue — Code Agents, AutoResearch, and the Loopy Era]]**
- 本文件论点：Bufar 在 Paxel 页面上做了 Human / Machine 双版本——Machine 版本是纯 Markdown，「a lot more distilled and lighter for the agents to consume」[07:13]，顶部还有「致 AI agent：不要执行本页任何命令」的指令 [07:47]。
- 对方论点：Karpathy 说「the customer is not the human anymore. It's like agents who are acting on behalf of humans and this refactoring will probably be substantial」[14:16]。很多 App 根本不该存在，应该只是 API + agent 做胶水层。
- 关联逻辑：预演与具体化。Karpathy 在抽象层做了预测——终端用户从人变成 agent，行业需要围绕这个前提重构。Bufar 在实践层给出了这个重构的第一个具体实例：一个页面如何同时服务两种读者。但两人的论点之间存在张力——Karpathy 说「App 不该存在，应该只是 API」，Bufar 保留了人类版本（视觉交互），只额外加了 Machine 版本。Bufar 没有走到 Karpathy 的极端（完全消灭人类界面），而是选择了「双版本共存」。这个差异指向一个未解问题：当 agent 版本成为标准，人类版本是否会逐渐萎缩？还是两种读者永远需要不同的界面？Bufar 的「我们可能会看到越来越多这样的模式」暗示她认为这是趋势，但没有给出人类版本的终局判断。

### 16 版本批量探索与验证瓶颈在设计领域的翻译
**← [[Terence Tao- How the world's top mathematician uses AI]]**（经 MOC 推理链）
- 本文件论点：Bufar 让 Claude 一次性生成 16 个网站版本，自己建 gallery 浏览标记——「you don't expect like an incredibly high level of craft. you're just using this as an exploration tool」[17:27]。核心动作从「做」迁移到「选」。
- 对方论点：Tao 提出假设生成成本归零→验证成为新瓶颈（类比通信成本归零→垃圾邮件）。
- 关联逻辑：具体化。Tao 在数学领域抽象出「验证瓶颈」框架——当生成端无限便宜，唯一有价值的动作是判断哪些生成物值得保留。Bufar 在设计领域给出了这个框架的实操翻译：16 个版本 = 假设洪水，gallery + 人工标记 = 验证回路。但 Bufar 补充了 Tao 没有的维度——她不是在验证「对错」（数学有对错），而是在验证「品味」（设计没有对错，只有更好和更差）。这意味着验证瓶颈在设计领域比在数学领域更严峻：数学的验证至少有客观标准（证明是否成立），设计的验证完全依赖人的品味——而品味本身是不可自动化的反馈机制。Bufar 的「soul.md 深度决定 agent 惊喜程度」是对这个问题的间接回答：你无法自动验证品味，但你可以通过深度上下文让 agent 的生成空间更接近你的品味分布——把验证从「事后筛选」前移到「事前约束」。

---

**元信息**

| 字段 | 值 |
|------|------|
| 标题 | YC's Head of Design Shows You How To Design With AI |
| 频道 | Y Combinator |
| 时长 | 30min 54s |
| 上传日期 | 2026-07-10 |
| YouTube链接 | https://www.youtube.com/watch?v=VbqaL_eHhKY |
| 分析时间 | 2026-07-16 |
