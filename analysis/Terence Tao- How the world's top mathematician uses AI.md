---
title: Terence Tao- How the world's top mathematician uses AI
source: youtube
youtube_url: https://www.youtube.com/watch?v=Q8Fkpi18QXU
transcript: "[[Terence Tao – How the world’s top mathematician uses AI]]"
tags:
  - kol情报
status: canonical
dedup_note: 83min完整分析7章节，最新版；已合并早期分析版(Feishu)的独有内容
created: 2026-06-16
order: 6
---

> AI 把假设生成的成本压到了零——就像互联网把通信成本压到了零一样——但这本身不创造丰裕，只制造洪流；科学的新瓶颈不是「谁能想到」，而是「谁能验证」。

> —— Terence Tao, Dwarkesh Podcast 2026

视频链接：https://www.youtube.com/watch?v=Q8Fkpi18QXU

对应逐字稿：[[Terence Tao – How the world’s top mathematician uses AI]]

## 核心证据校准

> **[6:41]** "it has to be matched by an equal amount of verification"

> **[8:17]** "You collect big data first, and then you try to get hypotheses from it."

> **[12:18]** "AI has driven the cost of idea generation down to almost zero"

> **[12:46]** "we have to change our structures of science to actually sort this out."

> **[17:19]** "it may never be something that you can just reinforcement learn"

> **[26:52]** "data was the bottleneck. It still is the bottleneck."

> **[53:00]** "how little insight we got from some Lean solution"

> **[59:20]** "a formal or semi-formal language for mathematical strategies"

**概述**：2026年3月，UCLA 数学教授、菲尔兹奖得主 Terence Tao 做客 Dwarkesh Patel 播客，进行了一场 83 分钟的对谈。对话从 Kepler 发现行星运动定律的历史故事切入，逐步深入到 AI 对数学与科学的根本性冲击。Tao 的核心赌注是：我们正在经历一场认知层面的哥白尼革命——人类智能不再是宇宙中心，AI 擅长广度而人类擅长深度，两者将长期互补而非替代；但当前科学体系完全没有准备好应对「假设洪水」的验证瓶颈，数学本身也将从纯粹理论学科蜕变为拥有实验侧面的新形态。

**主题脉络**：
1. Kepler的幽灵——假设生成成本归零后的验证危机
2. 山脉中的跳跃机器——AI广度与人类深度的互补法则
3. 人工灵巧vs人工智慧——累积性进步的缺失
4. 数学的实验革命——从证一道题到做一千道题
5. 证明之后——Lean、后处理与策略的形式化
6. 偶然性的价值——当优化摧毁了发现的土壤
7. 未完成的哥白尼革命——数学家的未来

---

# 一、Kepler的幽灵：假设生成成本归零后的验证危机

## 1.1 Kepler 是一个高温 LLM

Dwarkesh 开场讲了一个精心准备的故事：Kepler 用了二十年试错，从柏拉图立体到音乐和声，大部分尝试都是废话——但在 Tycho Brahe 的数据集这个验证信号的支持下，最终撞上了行星运动三定律。Dwarkesh 提出：Kepler 就是一个「高温 LLM」——随机试错，直到某个假设通过验证。

Tao 接受了这个类比的半边，但精准地补上了另一半：

```plaintext
[06:41] But as you say, it has to be matched by an equal amount of verification, otherwise it's slop.
```

没有验证的假设生成不是科学，是噪音。Brahe 的数据比前人精确十倍——那额外的小数位才是 Kepler 能成功的必要条件。

## 1.2 从「先假设后验证」到「先数据后规律」

Tao 指出科学方法的范式本身已经翻转。经典科学方法是先假设、再收集数据验证；但现在的大数据时代，是先有海量数据，再从中提取规律。Kepler 仍然先有预设想（柏拉图立体），但如今的进展越来越依赖数据先行。

```plaintext
[08:17] That's the classic scientific method. Now it's almost reversed. You collect big data first, and then you try to get hypotheses from it.
```

他随后用 Bode 定律的故事打了关键补丁：六个数据点拟合出的规律可能是正确的（Kepler 第三定律），也可能是纯粹的数值巧合（Bode 定律在海王星发现后崩塌）。数据太少时，统计直觉告诉你需要保持审慎。

## 1.3 假设洪水：验证是新的瓶颈

这是全篇最核心的判断之一。Tao 把 AI 对科学的影响类比为互联网对通信的影响：

```plaintext
[12:18] I think AI has driven the cost of idea generation down to almost zero, in a very similar way to how the internet drove the cost of communication down to almost zero. It's an amazing thing, but it doesn't create abundance by itself.
```

互联网让通信成本趋近于零，但这不等于我们获得了更好的通信——我们获得了垃圾邮件和信息过载。同理，AI 让假设生成成本趋近于零，但「Now the bottleneck is different」：

```plaintext
[12:46] This is something which we have to change our structures of science to actually sort this out. Traditionally, we build walls. [...] Many journals are reporting that AI-generated submissions are just flooding their submissions.
```

同行评审系统已在被淹没。人类评审员面对每天数千条 AI 生成的假设，完全无法胜任筛选。Tao 直言：我们不知道如何大规模地验证和评估哪些想法推动学科前进，哪些是死胡同。

---

# 二、山脉中的跳跃机器：AI广度与人类深度的互补法则

## 2.1 Erdős 问题：1% 成功率与规模化错觉

Tao 用 Erdős 问题的最新数据给出了一个冷静的案例。AI 辅助解决了约 50 个 Erdős 问题，看起来令人惊叹。但系统性研究揭示了真相：

```plaintext
[44:46] But whenever we do a systematic study, on any given problem an AI tool has a success rate of maybe 1% or 2%. It's just that they can buy scale, and you just pick the winners.
```

单个问题上的成功率只有 1%-2%，但因为可以大规模并行尝试，总能挑出成功案例。社交媒体上只传播赢家，看起来像是 AI 在横扫数学——实际上只是幸存者偏差。

## 2.2 山脉比喻：跳跃机器

Tao 给出了全篇最生动的类比。把未解的数学问题比作暗夜中的山脉，每一面悬崖的高度未知：

```plaintext
[33:02] These AI tools, they're like jumping machines that can jump two meters in the air, higher than any human. Sometimes they jump in the wrong direction, and sometimes they crash, but sometimes they can reach the tops of the lowest walls that we couldn't reach before.
```

关键特征：跳跃机器要么成功登顶，要么彻底失败。它们做不到的是——跳到一半，抓住一个手点，停在那里，把其他人拉上来，再从那里继续跳。

## 2.3 广度与深度的互补

Dwarkesh 精准地抓住了这个比喻的双面性：悲观地看，AI 现在只能跳两米高；乐观地看，一旦它们达到某个水位线，就能水淹式地解决该水位线下的所有问题——这是人类做不到的。

Tao 给出了核心判断：

```plaintext
[35:24] They excel at breadth, and humans excel at depth, human experts at least. I think they're very complementary. But our current way of doing math and science is focused on depth because that's where human expertise is, because humans can't do breadth.
```

当前的科学体系围绕深度组织，因为人类只能做深度。但 AI 带来了广度能力，科学体系需要重构以利用这种广度。Tao 的愿景是：先用广度型 AI 扫描整个领域，标记出所有容易的观察和困难的岛屿，然后人类专家攻入深度岛屿。

```plaintext
[36:48] It's too new. We don't even have the paradigms to really take full advantage of it. But we will, and then science will be unrecognizable after that, I think.
```

---

# 三、人工灵巧 vs 人工智慧：累积性进步的缺失

## 3.1 两者的本质区别

Dwarkesh 追问了 Tao 此前提出的「人工灵巧 vs 人工智慧」的区分。Tao 的回答直指当前 AI 的根本局限：

真正的人类智慧在协作中体现为——双方都不知道答案，但通过对话逐步构建策略：一个想法看起来有希望，测试它，失败，修改它，再测试。这是一个自适应的、持续改进的过程。

```plaintext
[50:58] There isn't this cumulative process which is built up interactively. It seems to be a lot more trial and error and just repetition: brute force.
```

AI 可以跳、可以失败、可以再跳。但它不能——跳到一半，找到一个手点，在那里停住，然后把其他人拉上来，再从那个位置起跳。每次对话结束，一切归零。

## 3.2 解决 Erdős 问题的两种模式

Tao 观察到 AI 解决数学问题经历了两个阶段。第一阶段是「一次性击杀」——AI 直接 one-shot 解决问题，但这只持续了一个月就停止了。当前是第二阶段：

```plaintext
[31:50] Someone might use AI to generate a possible proof strategy, and then another person will use a separate AI tool to critique it, rewrite it, generate some numerical data for it, or do a literature survey. Some problems have been solved by an ongoing conversation between lots of humans and lots of AI tools.
```

是大量人类和大量 AI 工具之间的持续对话在解决问题，不是单次 AI 交互。但即便如此，AI 自身的理解没有增长：

```plaintext
[51:36] Yeah. You run a new session and it's forgotten what it just did. It has no new skills to build on related problems.
```

这或许是当前 AI 最根本的结构性局限——它没有跨会话的累积学习能力。每次对话都是一张白纸。

## 3.3 Tao 自己的生产力变化

被问到 AI 是否让他 2 倍更高效时，Tao 给出了极其诚实的回答。如果只算辅助任务（文献搜索、数值计算、图表生成、格式调整），确实快了 5 倍。但核心研究没有加速：

```plaintext
[48:53] They haven't yet sped up the core thing that I do, but it's allowed me to add more things to my papers.
```

效果不是「更快写出同样的论文」，而是「写出更丰富但不一定更深的论文」。他现在论文里有更多代码、更多图表——但以前他根本不会放这些图表，只会用文字描述。

```plaintext
[49:17] It's made the papers richer and broader, but not necessarily deeper.
```

---

# 四、数学的实验革命：从证一道题到做一千道题

## 4.1 数学缺少的实验侧面

Tao 提出了一个被忽视的洞察：大多数科学都有理论和实验的对等分工，但数学几乎完全是理论学科。数学家从不做「大规模实验」——拿一千个问题测试两种方法哪个更有效，这在数学中闻所未闻。

```plaintext
[40:19] I think AI-type tools will actually revolutionize the experimental side of math, where you don't care so much about individual problems and the process of solving them, but you want to gather large-scale data about what things work and what things don't.
```

## 4.2 「将已知技术应用于开放问题」的巨大悬空

Dwarkesh 提了一个直击要害的问题：如果把每项已知技术应用于每个开放问题，这本身能带来多大的知识增长？

Tao 承认这是一个极好的问题，但现有数据不足以完全回答。他的经验判断是：顶级期刊的论文通常是现有方法解决 80%，剩下 20% 需要新技术。AI 正在变得非常擅长那 80%：

```plaintext
[42:44] AI tools are getting really good at the first part of that, just trying all the standard techniques on a problem, often making fewer mistakes in applying them than humans.
```

有时 AI 甚至能发现 Tao 自己的错误，有时反过来——大约打平。但 Tao 尚未看到 AI 迈出下一步：当所有标准方法都失败时该怎么办。

```plaintext
[43:25] They can suggest random things, but often I find that trying to chase them down to make them work, and finding they don't work, wastes more time than it saves.
```

## 4.3 同时惊人又令人失望

Tao 用一句话精准概括了当前 AI 在数学上的状态：

```plaintext
[46:02] The progress is simultaneously amazing and disappointing. It is a very strange feeling to see these tools in action.
```

人们也会极快地适应。他回忆 Google 搜索刚出来时令人震撼，几年后就习以为常。2026 年的 AI 水平放在 2021 年会让人震惊——人脸识别、自然语音、大学级数学——现在都被当成了默认值。

---

# 五、证明之后：Lean、后处理与策略的形式化

## 5.1 不用怕不可理解的证明

当 AI 生成了一个 3000 行的 Lean 证明来验证黎曼猜想，人类能理解吗？Tao 并不像很多人那样焦虑。他的逻辑是：一旦有了证明这个「物件」，就可以对它做原子化的分析。

```plaintext
[56:22] The beauty of formalizing a proof in something like Lean is that you can take any piece of it and study it atomically.
```

他描述了自己的阅读方式：拿到一篇解决困难问题的论文，其中有一连串引理。有些看起来是标准的套路，他知道没有新东西；但某个引理他从没见过，并且能看出它对证明主定理为什么关键——这就是新洞见所在。

## 5.2 证明后处理：一种未来的数学职业

Tao 预言了一种全新职业的诞生：

```plaintext
[57:29] I think in the future, there will be entire professions of mathematicians who might take a giant Lean-generated proof and do some ablation on it, trying to remove parts of it and find more elegant ways.
```

这已经在 Erdős 问题网站上发生：AI 生成一个 3000 行的证明，然后人们用其他 AI 来摘要，人们写出自己的证明版本。一旦有了一个证明，就有了大量工具来解构和诠释它。

```plaintext
[59:14] I think once you have the artifact of a proof, we can do a lot of analysis on it.
```

## 5.3 策略的半形式化语言：数学的下一个 Lean？

Tao 指出了当前的形式化空白：我们有了逻辑证明的形式语言（Lean/ZFC），但没有策略和猜想的形式化语言。判断一个猜想「多可信」——验了几个例子通过后置信度增加多少——这目前完全依赖人类专家的直觉。

```plaintext
[61:10] The bottleneck for using AI to create strategies and make conjectures is we have to rely on human experts and the test of time to validate whether something is plausible or not.
```

他用素数的随机模型作为案例：Gauss 通过数据发现素数定理（统计性猜想），经过百年发展出「素数像随机集合」的概念框架——这个框架不严格但极其准确，是黎曼猜想、密码学安全性的信念基础。但这个框架是启发式的、非形式化的，没法直接扔给 AI 去训练。

```plaintext
[66:07] It's mostly heuristic and non-rigorous, but extremely accurate.
```

如果黎曼假设被证伪，整个素数随机模型将崩塌，人们会立刻放弃基于素数的密码学——因为一个未知模式意味着可能还有更多模式，而模式意味着密码学漏洞。

## 5.4 我们只有一条时间线

Tao 指出了一个根本性的数据匮乏：我们只有一条人类科学发展的时间线，大约 100 个转折点的故事。如果有一百万个外星文明各自不同的科学发展史，我们才可能真正形式化「什么是进步」和「什么是好策略」。

```plaintext
[68:12] We could maybe start formalizing it and actually having a framework. Maybe what we need to do is start creating lots of mini-universes or simulations of AI solving very basic problems.
```

他的建议是：用小 AI 在简单问题上做进化实验，创造大量微型宇宙——这正是当前缺少的。

---

# 六、偶然性的价值：当优化摧毁了发现的土壤

## 6.1 偶然性不是浪费，是基础设施

当 Dwarkesh 问「如果从第一性原理来分配 Tao 的时间」时，Tao 给了一个反直觉的回答。他承认很多不得不参加的活动看似浪费，但——

```plaintext
[74:08] I do believe a lot in serendipity. [...] Because it's outside my comfort zone, it often results in interactions with people I wouldn't normally talk to, like you for instance.
```

被迫走出舒适区的活动，反而带来了意料之外的连接和发现。

## 6.2 COVID 的教训：效率杀死了偶然

Tao 用 COVID 期间学术界的转变作为案例。远程会议让一切都变得「高效」——见的总人数几乎不变，但所有互动都必须提前安排。失去的是走廊里随意的敲门、拿咖啡时的偶遇。

```plaintext
[75:28] Those serendipitous interactions may not seem optimal, but they are actually really important.
```

他回忆做研究生时去图书馆查期刊：找到你要的文章后，旁边的那篇也可能有趣。现在用搜索引擎或 AI，你得到精确结果——但失去了浏览时的意外发现。

## 6.3 高等研究院的反面教训

Tao 在普林斯顿高等研究院待过一年。前几周效率极高——大块时间思考，积压的论文纷纷写完。但几个月后，灵感枯竭，开始更多地上网冲浪。

```plaintext
[76:50] You actually do need a certain level of distraction in your life. It adds enough randomness and high temperature.
```

这段话暗示了一个深层隐喻：科学发现可能需要某种「高温」——高熵状态——才能跳出局部最优。过度优化等于退火过早。

## 6.4 对 AI 时代的隐含警告

Tao 没有明说但逻辑自洽的推论是：AI 让一切更高效、更定向、更精准——这正是摧毁偶然性的力量。他最后点到：

```plaintext
[81:07] It's also possible that by destroying serendipity we actually inhibit certain types of progress. Anything is possible at this point.
```

---

# 七、未完成的哥白尼革命：数学家的未来

## 7.1 认知的哥白尼革命

Tao 在对话中段做了一个安静的断言：

```plaintext
[20:57] Right now we're going through a cognitive version of the Copernican revolution, where we used to think that human intelligence is the center of the universe, and now we're seeing that there are very different types of intelligence out there with very different strengths and weaknesses.
```

我们曾经以为人类智能是宇宙中心，现在发现有非常不同类型的智能，有非常不同的优劣。对「哪些任务需要智能、哪些不需要」的评估必须大幅重排。

但他紧接着说了一个更深的洞见：最大的进步往往不是增加理论，而是删除假设。

```plaintext
[19:54] Often progress has to be made not by adding more theories, but by deleting some assumptions that you have in your mind.
```

日心说之所以花了那么久才被接受，是因为人们有一个未言明的假设——物体自然趋于静止（亚里士多德物理学）。删掉这个假设，地球在运动就不再荒谬。

## 7.2 被替代的不是数学家，是数学家的某些部分

Tao 被问到 AI 何时能完全替代他时，他的回答不是时间表，而是一个历史类比。19 世纪的数学家大量在做解微分方程的手工计算，现在 Mathematica 几分钟搞定。但数学没有死——它转向了不同类型的问题。

```plaintext
[78:12] But we will find that that actually wasn't the most important part of what we do.
```

基因测序从一个人的 PhD 缩减到 1000 美元送样，但遗传学没有死——它转向了研究整个生态系统。同理，十年内数学研究生当前做的大部分工作可以被 AI 取代，但那可能本来就不是数学最重要的部分。

## 7.3 人机混合将长期主导

关于 AI 何时能自主解决千禧年难题，Tao 的判断是谨慎的：

```plaintext
[79:57] I guess I do believe that hybrid human plus AIs will dominate mathematics for a lot longer.
```

当前 AI 在某些方面很好，某些方面极差。可以在上面叠加更多框架来降低错误率、让 AI 之间协作，但 Tao 的直觉是：我们还没有凑齐真正替代所有智力任务所需的所有成分。

```plaintext
[80:42] Because current level AIs will accelerate science in so many ways, hopefully new discoveries and new breakthroughs will happen more quickly. It's also possible that by destroying serendipity we actually inhibit certain types of progress. Anything is possible at this point.
```

## 7.4 给年轻数学人的建议

Tao 的收尾建议带有鲜明的「拥抱矛盾」色彩。一方面，传统路径仍然重要——短期内你仍然需要学位、需要学会做数学的老办法。但另一方面：

```plaintext
[82:49] But now it's quite possible at the high school level, or whatever, that you could get involved in a math project and actually make a real contribution because of all these AI tools, Lean, and everything else.
```

高中水平的人现在就可能通过 AI 工具和 Lean 对数学做出真实贡献。需要的是非常适应性的心态，准备好面对还没被发明出来的做科学的方式。

```plaintext
[83:37] It's a scary time, but also very exciting.
```

---

**元信息**
- 标题：Terence Tao – How the world's top mathematician uses AI
- 频道：Dwarkesh Patel
- 发布时间：2026-03-20
- 时长：83min
- YouTube链接：https://www.youtube.com/watch?v=Q8Fkpi18QXU
- 分析时间：2026-06-08




## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系
### 信用分配的稀疏性
**← [[Richard Sutton- Father of RL thinks LLMs are a dead end]]**
- 本文件论点：跳跃机器成功登顶或彻底失败——它们做不到跳到一半，抓住一个手点，停在那里，把其他人拉上来
- 对方论点：LLM框架里没有ground truth：你说了什么，没有人告诉你什么才是「对的回答」
- 关联逻辑：Tao的「跳跃机器」是Sutton诊断的实证表现：LLM不能做中间步骤判断→只能做二元成功/失败→所以Tao观察到AI登顶或摔死，无法停在半山

### 验证瓶颈的三层递进
**→ [[Dario Amodei- 我们正处于指数的尽头]]**
- 本文件论点：AI让假设生成成本趋近于零，但互联网让通信成本归零的结果是垃圾邮件而非更好通信——验证才是新瓶颈
- 对方论点：可验证与不可验证的裂隙：编程1-2年内到达，但规划火星任务、CRISPR式发现、写小说这类不可验证任务存在不确定性
- 关联逻辑：Tao在科学层面定义问题（假设洪水→验证瓶颈），Dario在能力域层面映射问题（哪些领域可验证→多快到达，哪些不可验证→时间线不确定）。Dario实际上是Tao论点的时间线版本

### 验证瓶颈的工程实现
**→ [[Archon—当 AI 编程从「聊天」变成「流水线」]]**
- 本文件论点：AI让假设生成成本归零，验证是新的瓶颈——同行评审系统正在被AI生成的假设淹没
- 对方论点：Archon用YAML把plan→implement→test→review→PR焊成流水线——AI生成代码（假设洪水），test+review步骤充当验证层
- 关联逻辑：Archon的YAML流水线就是Tao的「验证基础设施」在代码领域的具体实现：AI可以自由生成（假设洪水），但必须经过test和review两道验证关卡。YAML不是约束AI，是给验证定流程

---

## 补充视角：早期分析版独有内容

> 以下内容来自同一访谈的早期分析版（Feishu文档，分析时间 2026-06-05），为完整版未覆盖的独有视角与推论。

### A. 正确理论的初期劣势：Copernicus不如Ptolemy

在讨论验证瓶颈时，Tao提出了一个容易被忽视的深层问题：即使AI能发现经验规律，谁来识别哪个规律值得深入？他用了科学史上的经典案例——日心说刚提出时，精度反而不如已经发展了千年的地心说：

```plaintext
[18:39] Often, the ultimately correct theory initially is worse in many ways. Copernicus's theory of the planets was less accurate than Ptolemy's theory. Geocentrism had been developed for a millennium by that point.
```

这意味着科学中有些判断——比如识别「正确但不完整」的理论——本质上是回顾性的，很难用强化学习来量化。AI可以在当下选出「表现最好」的假设，但无法识别「现在表现差但将来会赢」的理论。

### B. 广度的质变：一百万个问题各花一百年

Dwarkesh提出了一个看涨视角：AI的1%成功率之所以令人沮丧，是因为我们用人类的标准评判。如果AI达到人类数学家水平，它可以同时在一百万个问题上各花一百年——这种广度是质的飞跃，不仅仅是量的提升。这不仅是关于AI的判断，更是关于科学方法的判断：当前科学围绕人类深度专长设计——如果我们重新设计它以利用广度，科学将变得面目全非。

### C. 累积性进步的产品路径与竞争格局

如果AI的核心局限是缺乏累积性进步，那么有两条路径：

1. **等待模型能力自然进化**——但Tao暗示这不够，因为跨会话记忆不是当前架构的自然方向
2. **设计新的工作流来弥补**——比如让AI在成功解题后自动提取可迁移的中间结果，或者建立跨会话的「数学记忆」

**产品判断**：谁先解决了累积性问题，谁就在AI for Math中拿到结构性优势。

### D. 产业信号：数学实验平台 > 自动证明器

数学软件的方向可能不是「更聪明的自动证明器」，而是「数学实验平台」——用广度AI对大量问题做策略测试、收集结构化数据、生成数学的「实验物理学」。这跟当前Lean + AI的主要叙事（自动证明）方向不同。当前的焦点是让AI证明单个定理，但Tao的洞察暗示：更大的价值在于让AI同时对大量问题做策略扫描，发现「什么有效什么无效」的结构性规律。

### E. 设计「受控的随机性」：下一代知识工具的核心命题

任何声称「优化」研究流程的工具，如果不刻意保留偶然性通道，可能反而在扼杀最有价值的部分。搜索引擎、推荐系统、AI助手——它们都让获取精确信息更高效，但系统性地消灭了偶遇。Tao在访谈最后补充道：

```plaintext
[81:01] It's also possible that by destroying serendipity we actually inhibit certain types of progress. Anything is possible at this point. I think the world is very, very unpredictable at this point in time.
```

**产品含义**：设计「受控的随机性」可能是下一代知识工具的核心命题——不是让用户更快找到已知答案，而是保留偶遇未知方向的通道。
