---
title: "Benedict Evans- The Economics of AI Usage and What's Next For SaaS"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=ktl8mNiWqMM"
transcript: "[[The Economics of AI Usage and What's Next For SaaS  Benedict Evans on a16z]]"
tags:
  - kol情报
created: 2026-06-10
order: 14
status: canonical
---

> 基础模型将沦为商品化基础设施，价值向上层应用逃逸——当前的天价capex和token稀缺是过渡态，不是终态；模型公司面临的不是"AI是否会改变一切"，而是"你建了管道，但水费归谁收"。
> —— Benedict Evans, a16z 2026

视频链接：https://www.youtube.com/watch?v=ktl8mNiWqMM
对应逐字稿：[[The Economics of AI Usage and What's Next For SaaS  Benedict Evans on a16z]]

**概述**：2026年6月，a16z播客，Benedict Evans（前a16z合伙人、知名科技分析师）与Erik Torenberg对话，围绕其更新版演讲"AI Eats the World"展开。核心赌注：基础模型的商品化不可避免，当前供给-需求-定价的三方失衡终将回归均衡，价值捕获的位置不在模型层而在应用层——但"在哪里"和"怎么捕获"仍是开放问题。

**主题脉络**：
1. 编程作为AI第一个真正的产品-市场匹配——从"能用"到"改变一切"的跃迁
2. 基础模型的商品化宿命——电信运营商类比与定价权的缺失
3. Chatbot不是产品——UI的局限与价值的真正位置
4. SaaS的结构性扩张——更多软件而非更少
5. "自动化旧事"与"做新事"的分水岭——Jevons悖论与消费者剩余
6. 我们身处1997年——平台周期早期的不确定性与历史类比的安全边界

---

## 核心证据校准

> **[0:00]** "Agentic coding went from being kind of useful to really changing everything."
> **[0:17]** "we can't spend \[music\] $10 trillion a year on AI infrastructure"
> **[0:25]** "I don't think foundation models are a product."
> **[1:39]** "agentic coding started working"
> **[1:39]** "absolute product market fit"
> **[2:02]** "right it works for coding"
> **[2:37]** "We don't know if they can capture value up the stack."
> **[2:37]** "we don't see a way that consumers will use this daily rather than weekly"
> **[3:47]** "agentic coding went from being kind of useful to really changing everything."
> **[4:54]** "do you hire junior people and if so, what are they doing"
> **[12:04]** "data traffic has risen by something like one and a half to 2,000 times"
> **[12:04]** "all the cool stuff got built by somebody else"
> **[17:59]** "There isn't doesn't seem to be a network effect."
> **[18:47]** "a weird limited v1 UI"
> **[18:47]** "people who are good at using the tool and doing the job that needs the tool are not the same people who are good at deciding what the tool should be."
> **[20:19]** "No more than like Microsoft or Apple could build every Windows app or every iPhone app."
> **[21:02]** "that's the whole point it's abstracted away"
> **[21:28]** "the models are kind of diff commodities"
> **[22:07]** "where is the price discipline going to come from?"
> **[48:31]** "Microsoft, Meta and Google are all on in line to spend over 50% of revenue on capex this year."
> **[49:41]** "we can't spend $10 trillion a year on inf AI infrastructure"
> **[51:35]** "you can't let other people get away with this without you participating because then your company's gone"
> **[55:32]** "it looks like these things will be commodities and explain to me why they won't be"

# 一、编程先跑通了，然后呢

Evans开篇即点明过去一年最大的变化：agentic coding从"有点用"跃迁到"改变一切"，成为AI领域唯一拥有明确产品-市场匹配的用例。这个转变并非可预测的必然——尽管从决定论角度可以说"搞AI的人自然会先让AI做软件开发"，就像PC时代第一批应用就是做更多计算机一样，但何时、以何种方式真正work，事前无法锁定。

```plaintext
[01:42] clearly agentic coding started working and so all the focus in tech has kind of narrowed in massively onto that as something that has absolute product market fit in the sense that like the customers are pulling it out of your hands.
```

这个判断携带的隐含立场极为锐利：当他说"the customers are pulling it out of your hands"时，这不是渐进式采用——是需求侧的暴力拉动。而紧接着的转折更重要：除了编程之外，其他领域尚未找到同等强度的产品-市场匹配。

```plaintext
[02:49] We don't see a way that consumers will use this daily rather than weekly with the technology we have right now.
```

这句话揭示了一个结构性缺口：B2C侧的日常使用场景至今缺席。编程之所以先跑通，Evans用了一个精妙的类比——"the first thing that people did with PCs was make computers"——工具创造者的本能是先改进自己的工具。但这只解释了"为什么先"，不解决"然后呢"。

OpenAI的策略摇摆被Evans拿来作为佐证：去年下半年试图"什么都做"（"ask ChatGPT for 15 ideas for what we could do to build value on top of infrastructure, and then we'll do all of them"），而Anthropic因为资本更少反而聚焦coding并取得突破。这本身是一个关于战略收敛的信号：资源约束下的聚焦比资源充裕下的发散更容易找到产品-市场匹配。

---

# 二、建了管道，水费归谁收

这是Evans整场访谈最核心的论证链：基础模型公司将重蹈电信运营商的覆辙——建了基础设施、承担了巨额capex、流量暴涨了1500-2000倍，但所有"酷的东西"都是别人做的，股价20年横盘。

```plaintext
[12:04] since then mobile data traffic has risen by something like one and a half to 2,000 times and the mobile networks collectively have revenue of about a trillion dollars and they spend about 200 billion dollars a year on capex and the stocks have been flat for 20 years and all the cool stuff got built by somebody else
```

这个类比的力量不在于"历史会重复"，而在于它揭示了价值捕获的结构性条件。Evans构建了一个四层论证：

**第一层：没有可持续差异化。** 模型之间不存在网络效应，不存在Instagram或YouTube那种护城河机制。

```plaintext
[18:10] it's not clear how you could build a model that was fundamentally better than everybody else's model in some sort of sustainable differentiated way. There isn't doesn't seem to be a network effect.
```

**第二层：Chatbot不是产品。** 它是"weird limited v1 UI"，大多数任务需要工具化、数据配置、专用界面——而这些事情模型公司做不了。

```plaintext
[18:47] the chatbot itself is like a kind of a weird limited v1 UI and there's some things and some people and some kind of task where it works really well but there are most of the others you need a bunch of other stuff
```

**第三层：模型公司无法自行构建上层应用。** 就像Microsoft和Apple不可能构建每一个Windows/iPhone应用一样——但与操作系统不同的是，模型层缺乏向上延伸的杠杆。

```plaintext
[20:34] can the model labs build all of that? Well, of course not. No more than like Microsoft or Apple could build every Windows app or every iPhone app.
```

**第四层：没有定价权。** 3-6家前沿模型公司互相竞争，加上edge和开源的挤压，还有Google这种"卖广告补贴定价"的异类玩家——价格纪律从何而来？

```plaintext
[21:55] you're going to have, pick a number, three to six companies making a Frontier model... Plus, there'll be a bunch of edge and a bunch of open source. So where's this going to settle down? you're going to have as it might be half a dozen companies that are all competing to sell this stuff. And so where is the price discipline going to come from?
```

Evans把这个论证链的终点指向了一个"大一经济学"问题：当前是极端非均衡态——需求无限、供给不足、capex暴涨——但非均衡态不是均衡态。移动数据的需求也是无限的，流量涨了2000倍，但最终仍然有供需-价格均衡和电信运营商间的惨烈价格战。

Evans也给自己留了退路：他不是"知道"模型会商品化，而是"这是一条决定论式的论证链，请告诉我它为什么不成立"。

```plaintext
[55:32] It's not that I know that they're going to become commodities. my position is more now well like hey here is a chain of argument that says that deterministically it looks like these things will be commodities and explain to me why they won't
```

这比直接断言"模型会商品化"更有力——它把举证责任转移给了对方。

---

# 三、Chatbot是Excel模板，不是TurboTax

Evans对"Chatbot即产品"的拆解极为精准。他用了一个日常但锋利的比喻：Claude的"skills"就像Excel的"File > New"模板——能带你走一程，但迟早会outgrow。

```plaintext
[19:54] you know that seems to be a bit like what you get if you do file new in Excel like these are templates and they'll take you so far but a certain point you know people outgrow the templates.
```

更深层的问题是"谁来做这件事"：擅长做某项工作的人和擅长设计做该工作的工具的人，从来不是同一批人。擅长设计印刷出版物的人不应该去设计InDesign——擅长做财务顾问的人不应该去设计TurboTax。

```plaintext
[19:17] people who are really really good at doing financial advice are not the right people to design TurboTax. Those are different people with different skills.
```

这直接否定了"模型吞噬一切"的叙事。如果模型公司连skills都做不好——因为做skills需要的是领域专长而非AI专长——那"just go to the model and say do my taxes for me"就更加不可能。你需要的不是一个更聪明的chatbot，而是一个用10种不同方式调用AI的税务软件。

```plaintext
[12:56] can you just go to the model and say do my taxes for me or do you need to have a tax thing that uses that might use some AI in 10 different ways inside it
```

这个判断对企业软件采购有直接的实战含义：Evans指出，当律所或银行购买企业软件时，他们根本不会问"这个产品底层用的是Claude还是OpenAI"——就像你买SaaS时不在乎它跑在AWS还是GCP上一样。模型被抽象掉了。

```plaintext
[20:48] how often does like the law firm or the manufacturing company or the bank say oh well does this use claude or does it use or open AI because we we standardize on claude well no that's not how it works anymore than worked like that for cloud
```

---

# 四、7000亿美元的物理极限与FOMO驱动的军备竞赛

Evans对AI capex的判断是冷算术：微软、Meta、Google今年capex指引合计约7000亿美元，超过收入的50%——电信运营商这个公认的资本密集型行业，capex/收入比也只有15-20%。7000亿不是不可能的数字（油气行业capex约7000亿到1万亿），但增长率有物理上限。

```plaintext
[48:32] Microsoft, Meta and Google are all on line to spend over 50% of revenue on capex this year. And you know we think of telecoms as being capital intensive. telecom spend instead of 15 to 20% of revenue on capex.
```

```plaintext
[49:55] we can't spend $10 trillion a year on AI infrastructure because there isn't $10 trillion a year there to spend on it.
```

但Evans没有简单地说"泡沫会破"——他刻画了两个同时为真的矛盾力量：**存在性恐惧**（"如果这是计算的未来而你缺席了，你的公司就完了"）与**财务重力**（"CFO在问到底要参与多少"）。

```plaintext
[51:35] on the one hand your returns on the investment at the moment are hugely positive. On the other, you can't let other people get away with this without you participating because then your company's gone and you don't want to end up like Microsoft in the 2000s or IBM in the '90s
```

这构成了一个囚徒困境：没人敢第一个停手，但没人能无限加码。Evans认为这条曲线最终会taper off——不是因为它应该，而是因为"它没有别的地方可去"。

与移动数据的价格失衡类比再次出现：2009-2010年，一边是收到5万美元账单的消费者，一边是AT&T推出flat-rate data后网络被iPhone压垮。最终的解决方案是cap bundles、fair use、throttling——一种粗糙但有效的成本-定价-价值三方对齐。Evans认为AI token市场将经历同样的收敛过程。

---

# 五、更多软件，不是更少——SaaS的结构性扩张

Evans对"SaaS末日论"的回答出人意料地乐观，但乐观的方向极其具体：AI不会减少软件的数量，而是产生数量级的更多软件。SaaS本身就是一个"所有软件公司的存在都是为了解决其他软件公司制造的问题"的行业——AI只会放大这个逻辑。

```plaintext
[42:20] all software companies exist to solve problems created by other software companies. That was the joke in in security... SAS gave us an order of magnitude, two orders of magnitude more software. Um and we should probably expect that with this.
```

他构建了一个企业软件的三层模型来分析AI的着陆点：**底层**是大型水平系统（SAP、Workday、CRM）；**顶层**是垂直专用软件；**中间**是Excel/邮件/共享文件系统的模糊地带。AI不会替代这三层中的任何一层，而是在每一层都增加新的选择。

```plaintext
[39:27] you've got like your big iron horizontal systems... And then you've got vertical software... and then in the middle you've got this kind of fuzzy improvised space of Excel and email and the shared file system
```

关键的结构性张力在于：**LLM放在栈的顶部还是底部？** 底部方式——AI作为Salesforce中的一个feature，有guardrails、有上下文、有确定性数据支撑。顶部方式——LLM跨Salesforce、Workday、邮件、Analytics做综合，产生"以前做不了的事"。两种方向都有用，但它们对确定性/概率性软件的位置安排完全不同。

```plaintext
[42:01] where do you put the probabilistic software that can make mistakes and where do you put the deterministic system software that can't answer these kind of questions. So where do you put the database and where do you put the LLM
```

对SaaS投资者而言，Evans给出的信号是谨慎但不悲观："有些SaaS公司一定会被wipe out，但你不知道是哪些，所以你不应该把整个行业砍50%——但显然你也不会在搞清楚之前做多软件股。"

```plaintext
[42:54] there must be some... x% of all the SAS companies that are out there are going to get wiped out by this but you don't know which ones... I'm not sure I'm going to be long software at the moment until I have some idea of what the hell's going on.
```

---

# 六、自动化旧事与做新事——Jevons悖论的AI版本

Evans提出了分析AI经济影响的四个"按钮"：

1. **价格弹性（Jevons悖论）**：做事情更便宜了——是花更少钱做同样的事，还是花同样钱做更多事，还是花更多钱做更多事？
2. **准入壁垒消失**：拥有印刷机曾是报纸的壁垒——现在这个成本壁垒消失了，谁的机会？
3. **商业模式解锁**：有没有什么因为成本原因不可能存在的商业模式，现在被解锁了？
4. **以前完全不可能的事**：买再多马也造不出火车；15美元/月听所有音乐在CD时代是不可能的。

```plaintext
[30:44] First one is this just price elasticity... do you do the same amount of stuff for less money or do you do more for the same money or do you more do more for more money?
```

他用广告和零售的例子来具体化：Google和Meta至今"不知道那个产品是什么"——它们知道SKU、知道协同过滤的"买了这个的人也买了那个"，但不知道为什么。LLM在原则上能改变这件事——从协同过滤到语义理解。

```plaintext
[32:15] Google and meta and Amazon don't really know what that product is they know it's a skew... but they don't know why... with an LLM like in principle you would kind of know what those things are and why people buy them
```

这也是为什么Google和Meta的广告收入在加速——它们正在把LLM嵌入推荐和预测系统，转化率在每季度跳升。但Evans的关键转折在这里：**重要的不是用新工具做旧事更快，而是做只有新工具才能做的事。**

```plaintext
[34:41] the important stuff is not doing the old thing but more. It's doing something new that you couldn't have done with the old thing.
```

这听起来像陈词滥调，但Evans的论证让它变得尖锐：如果你不知道行业里真正的问题是什么——不是你在San Francisco以为的问题，而是你在那个行业内部才能感知到的问题——你就做不出那个"新事"。Netflix的所有关键问题都是"LA问题"（什么剧、多少钱、该不该买体育版权），不是"SF问题"。

```plaintext
[26:05] all the questions for Netflix are are TV LA questions... These are all Los Angeles questions. These are not San Francisco questions. Like no one in San Francisco even knows what the right questions are.
```

这与前面"擅长做财务的人不该设计TurboTax"一脉相承：**AI对行业的影响，提问权在行业内部，不在AI公司。**

关于消费者剩余，Evans给出了一个冷峻的观察：DCF（现金流折现）从一周变成10秒后，你做50个DCF而不是2个，但你不能因此多收钱——生产力增益被竞争消耗掉了。

```plaintext
[54:14] if a DCF takes you a week, then you probably only do one or two DCFs. And if a DCF takes you 10 seconds, then you do 50 DCFs, but you probably can't charge any more money for that.
```

---

# 七、我们身处1997——不确定性的诚实

Evans整场对话最反复出现的主题是"我们不知道"。这不是回避，而是有结构的不确定性。他给出了三个层次：

**第一层：不知道模型的物理极限。** 这是AI与之前所有平台位移的根本区别——1995年你知道不可能下周给全世界装宽带，你知道PC卖3000美元不是人人买得起。但今天，模型能多大、多好、多便宜、多快？没人知道。

```plaintext
[27:49] with generative AI, obviously, we don't like... we might look at our phones when we get off this recording and there's a push notification that says that like Open AI's new model is out and it's like 2% of the price because they worked something out.
```

**第二层：不知道行业影响的具体形态。** 互联网摧毁了物理分发的价值——但对报纸和电影工作室意味着完全不同的事。同样一句"AI会自动化X"，在不同行业落地成截然不同的形态。

```plaintext
[31:37] if we'd been back in the late '90s and we'd said we know internet will destroy the value of physical distribution. It turned out that meant completely different things for newspapers and movie studios.
```

**第三层：不知道任务与工作的关系。** 自动化的是"task"——完成工作所用的手段——而"job"本身可能不变，就像会计师50年来做的事情完全不同，但对客户而言是"同一种服务"。

```plaintext
[47:00] the tasks that are used to accomplish the job might change without the job itself changing very much or without the thing that the job is selling to the client changing very much.
```

Evans还提出了一个区分LLM能力边界的深刻问题：**你要的是"任何人都会给出的答案"还是"不同的答案"？** LLM极擅长前者——"你描述人们怎么做的，它就按那个方式做"；极不擅长后者——"你没法解释为什么你那样做，而且你做的方式和常人不同"。

```plaintext
[47:37] where is it that you want the average? Where is it that what you want is the way that everybody will do this? ... Versus where is that not what you want? Where is it that you want the answer to a new question or a different answer or a different idea?
```

最后，Evans用一张1950年代的IBM广告收尾——"一台IBM电子计算器给你150个额外的工程师"——这和今天每个AI创业公司的pitch一模一样。他的收束不是预测，而是一个历史性的base case：我们每10-20年经历一次这样的技术变迁，每一次都"前所未有"，而最终都走向同一个结局——20年后我们忘记了计算机曾经不能做那件事。

```plaintext
[59:52] it's going to be magic and in 20 years time we'll just say, well, of course that's how it is. Computers have always done that.
```

---

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Scaling不等于定价权——规模增长与价值捕获的脱钩
**← [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]**
- 本文件论点：Evans论证即使模型持续scaling、流量涨2000倍，模型公司也可能像电信运营商一样——股价20年横盘，所有"酷的东西"由别人构建（[12:04]）
- 对方论点：Ilya/Scaling阵营的核心信念是更大模型=更强能力=更大商业价值，capex投入是通向价值捕获的必要路径
- 关联逻辑：Evans的电信运营商类比直接挑战了"scaling→定价权"的隐含假设。流量增长2000倍和股价横盘20年可以同时为真——这要求Scaling阵营回答一个他们通常回避的问题：如果你的模型确实越来越强，但别人也能做差不多强的模型，规模增长本身就是价值捕获的充分条件吗？Evans把问题从"模型够不够强"转移到了"强模型有没有护城河"。

### 模型商品化与Software 3.0的维护悖论——谁拥有"skill"的定义权
**→ [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]**
- 本文件论点：Evans指出Claude的skills就像Excel模板——"file new in Excel, they'll take you so far but people outgrow the templates"，擅长做领域工作的人不应设计领域工具（[19:54], [19:17]）
- 对方论点：Karpathy的Software 3.0中，"prompt"成为新的编程范式，但prompt/agent的维护、调试、演进缺乏清晰的责任主体和工具链
- 关联逻辑：Evans的"模板终将被outgrow"和Karpathy的"prompt维护悖论"是同一结构的不同侧面。Evans说的是skills的上限——模板化方案无法覆盖领域深度；Karpathy说的是skills的下限——即使模板够用，谁来维护它？两者共同指向一个结论：模型公司试图通过skills/agent向上层延伸的路径，受制于"领域知识不可模板化"（Evans）和"模板不可维护"（Karpathy）的双重约束。

### 例外处理即价值——确定性系统与概率性系统的边界
**← [[Terence Tao- How the world's top mathematician uses AI]]**
- 本文件论点：Evans提出"all the decisions are really exception handling"——未被自动化的、需要人的判断和观点的部分才是关键，因为"maybe that hasn't been written down or that didn't happen before or doesn't look quite the way it happened before"（[46:33]）
- 对方论点：验证瓶颈链中，Tao强调数学证明的验证需要"每一步都可检查"，Dario指出AI系统的可靠部署需要形式化验证层，而非仅靠统计置信度
- 关联逻辑：Evans的"exception handling"和验证瓶颈链共享一个深层结构——AI的价值不在于它处理了多数情况（那只是baseline），而在于少数例外情况的处理方式。Evans从经济学角度描述（这些例外才是定价权的来源），Tao/Dario从可靠性角度描述（这些例外才是系统安全的瓶颈）。把两者放在一起看：AI系统在商业上的定价权和在工程上的可靠性，都卡在同一个地方——你如何处理那些"没被写下来、没发生过、看起来和以前不一样"的例外。

### 资本重力与AGI信仰——FOMO驱动的军备竞赛何时收敛
**← [[Dario Amodei- 我们正处于指数的尽头]]**
- 本文件论点：Evans指出大厂同时被存在性恐惧和财务重力拉扯——"you can't let other people get away with this without you participating because then your company's gone"，但"there isn't $10 trillion a year there to spend on it"（[51:35], [49:55]）
- 对方论点：Dario认为AGI/ASI是可达的，capex投入是通向范式转换的合理赌注，"underinvesting is riskier than overinvesting"是被多次引用的立场
- 关联逻辑：Dario的"不投资的风险大于过度投资"和Evans的"物理极限约束"不是简单的对立——它们描述的是同一曲线的不同段落。Dario描述的是当前阶段的博弈均衡（FOMO驱动没人敢停），Evans描述的是这个均衡的收敛条件（钱不是无限的）。合在一起才能看到完整的图景：FOMO驱动的军备竞赛会持续到财务重力迫使它减速的那一刻，而那个时刻的来临速度取决于模型效率的提升速率——如果模型每100x-200x效率提升的承诺兑现，收敛会更快到来；如果不兑现，物理极限会更早地以更痛苦的方式强制收敛。

---

**元信息**
```plaintext
标题: The Economics of AI Usage and What's Next For SaaS | Benedict Evans on a16z
频道: a16z
发布时间: 2026-06-08
时长: 60min
YouTube: https://www.youtube.com/watch?v=ktl8mNiWqMM
对话者: Benedict Evans, Erik Torenberg
分析时间: 2026-06-10
```
