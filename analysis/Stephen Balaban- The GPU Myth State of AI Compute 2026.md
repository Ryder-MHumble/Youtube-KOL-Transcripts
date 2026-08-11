---
title: "Stephen Balaban- The GPU Myth State of AI Compute 2026"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=0NttU4CbyVs"
transcript: "[[The GPU Myth State of AI Compute 2026  Stephen Balaban]]"
tags:
  - kol情报
status: canonical
created: 2026-06-25
---

> GPU 算力从来不是商品——它是一种从土地、电力到芯片、软件全栈垂直整合的复杂生意，只要缩放定律不终止，需求就会持续超出供给，而 2023 年的 H100 今天能以更高价格出租，就是这场赌注最好的证明。
> —— Stephen Balaban, Lambda co-founder/CTO, 2026

视频链接：https://www.youtube.com/watch?v=0NttU4CbyVs

对应逐字稿：[[The GPU Myth State of AI Compute 2026  Stephen Balaban]]

**概述**：2026 年 6 月，MAD Podcast 主持人 Matt Turck 与 Lambda 联合创始人兼 CTO Stephen Balaban 进行了 74 分钟深度对话。Lambda 是美国头部 AI neocloud 之一，年化收入接近 10 亿美元，正在从 GPU 租赁商转型为 GW 级 AI 工厂的垂直整合建造者。这场对话的核心赌注是：**算力市场的"商品化"叙事从一开始就是错的，而"持续低建"的判断在今天仍然成立**——只要缩放定律不被打破，算力需求就会不断扩张，GPU 资产的金融属性也在加速成熟。Balaban 同时提出了"神经软件"（neural software）的长期愿景：LLM 不是生成代码，而是直接成为软件本身。

## 核心证据校准

> **[1:49]** "cloud compute is not a commodity service."
> **[4:24]** "take a very large-scale GPU cluster and partition it up for our customers."
> **[5:30]** "innovation happening on every layer of the stack"
> **[6:06]** "there's room for multiple large winners and multiple large players."
> **[8:06]** "we continue to see no end to the scaling laws"
> **[9:33]** "everybody is able to process 10 times more tokens"
> **[11:10]** "the main bottleneck is basically land power shell"
> **[15:13]** "break it down from like a physics perspective into like the SI terms."
> **[17:23]** "the largest part of that cost structure is the depreciation"
> **[19:10]** "a lot of Neo Cloud are in that position where they they don't even have the infrastructure to be able to run a real Cloud service."
> **[24:18]** "the compute, the servers can be anywhere from 35 to 45 billion dollars a gigawatt"
> **[26:55]** "One of the big moats they've got is just the cuDNN stack."
> **[28:02]** "The other one is uh NCCL, which is their networking optimization library"
> **[35:11]** "vertical integration, where we are identifying land"
> **[38:12]** "this new fleet of AI applications are far less latency-sensitive"
> **[39:21]** "take your off-take agreement, you take this chunk of GPUs that you're deploying"
> **[42:00]** "The usable life is longer than the accounting depreciation schedule."
> **[59:37]** "what I call neural software."
> **[1:06:35]** "what I kind of call self-assembling software."
> **[1:08:32]** "It's a an AI factory, which is a basically land, data center, servers inside that is generating tokens."
> **[1:12:13]** "agentic workflows for things that are not software engineering I think tend to be overhyped"

**主题脉络**：① GPU 非商品化的底层逻辑 → ② 缩放定律与需求扩张的"锥形" → ③ 算力链路的物理学与成本结构 → ④ GPU 作为新兴资产类别 → ⑤ Nvidia 的真实护城河 → ⑥ 垂直整合与 AI 工厂 → ⑦ 神经软件与自组装软件 → ⑧ 一人一 GPU 的世代类比

---

## 一、GPU 从未商品化——被误读的"一层蛋糕"

Balaban 开场即否认了几年前硅谷的主流判断：neocloud 会被商品化、GPU 算力价格会持续走低。他的核心反驳是——云算力本身就不是商品服务，而是一个从土地到软件的垂直整合复杂系统。Hyperscaler（Amazon、Microsoft、Google、Oracle）之所以都在做云，恰恰因为这是一门极好的生意。

```plaintext
[01:53] The big thing is that cloud compute is not a commodity service. It is a very complicated highly vertically integrated type of service that spans everything from land land entitlement construction HPC high-performance computing design software virtualization cloud services on top
```

他进一步拆解了市场上"GPU 租赁价格下降"的错觉来源：Bloomberg 上的 H100 租赁价格指数混淆了两种费率——公共云按需费率（on-demand）和长期租赁费率（long-term rental）。实际情况是两种费率都在持平或上升，指数显示的"下降"只是因为长期合同在样本中的占比变化导致的方法学假象。

```plaintext
[03:32] what we're actually seeing is a very consistent if not increasing long-term rental rate and very consistent and increasing on-demand rental rates
```

这里有一个关键的隐含立场：Balaban 把"neocloud"重新定义为"为 AI 时代设计的云服务"，而不是传统云的变种。这个定义重塑了竞争框架——如果 neocloud 本质上就是云，那它的终局就不是被边缘化，而是与 hyperscaler 并列的多赢格局。他明确否定了"赢家通吃"：

```plaintext
[06:08] I think it's absolutely room for multiple very large players just like the traditional cloud business has shown that there's room for multiple large winners
```

他的论据是市场结构理论：技术和资本壁垒驱动的行业偏向寡头竞争（oligopolistic），而非网络效应驱动的单赢家格局。这等于在说——neocloud 的护城河来自重资产和重工程，不是来自用户网络效应，因此多个玩家可以并存。

## 二、缩放定律没有终点——"钱进去，软件出来"的赌注

Balaban 对"是否在过度建设"的回答极其坚定：**持续低建**。他的信心锚定在一个物理直觉式的判断上——缩放定律（scaling laws）至今没有出现边际收益递减的迹象。

```plaintext
[07:04] I think that we continue to be generally under building
[08:18] we continue to see no end to the scaling laws
```

他用 Opus 4/5 的发布作为拐点证据，认为"钱进去、软件出来"（money in, software out）已经从预测变成现实。这不再是 2017 年时少数人的信念，而是已被模型能力验证的事实。他进一步用"地址市场锥形"（cone of addressable market）的比喻解释需求扩张机制：早期 AI 的可替代市场只是客服和搜索替代品，现在已经扩展到软件工程的替代/增强，锥形还在继续扩大。

```plaintext
[09:01] originally the cone of the addressable market was, all right, this is going to be helpful for customer support... And then now it's like, well, this is a substitute for a lot of software engineering roles
```

当 Turck 追问"如果模型效率提升 10 倍怎么办"时，Balaban 给出了一个简洁的反驳逻辑：效率提升意味着每个人能处理 10 倍的 token，而世界上的总算力在任一时刻是固定的——所以需求只会膨胀，不会收缩。他回忆 2017 年时人们曾担心"随机森林"之类的轻量模型会颠覆 GPU 需求，但这种"邻近颠覆"（adjacent disruption）从未发生。

```plaintext
[09:39] if you do become 10 times more efficient, that just means that everybody is able to process 10 times more tokens and there's still the same fixed amount of compute in the world at any given point in time
```

这个判断的隐含立场值得注意：Balaban 把整个行业的基础设施投资押注在"缩放定律持续有效"这一前提上。他没有讨论如果缩放定律突然放缓的情景——这对一个正在融资数十亿美元建数据中心的 CTO 来说，是一个刻意回避的风险对冲话题。

## 三、从光子到 token——算力链路的物理学与经济学

Balaban 用一套 SI 单位制的物理框架描述了算力的完整链路，从左侧的能源输入到右侧的 token 消耗：光子或天然气分子 → 发电厂转化为焦耳/秒（瓦特）→ 数据中心 PUE 效率 → 服务器产出 flops/秒 → 模型训练/推理消耗 → 输出 token/秒 → 终端用户转化为"智能"。MFU（模型浮点利用率）是这个链路上端的效率指标，PUE 是数据中心层的效率指标。

```plaintext
[15:23] on the left-hand side is all of the energy production and then on the right-hand side is sort of tokens being consumed... The MFU percentage is kind of like an efficiency up on the higher end of that chain
```

在成本结构上，他给出了 GW 级 AI 工厂的具体资本分层：

| 层级 | 成本（每 GW） |
|------|-------------|
| 发电厂 | 20-30 亿美元 |
| 数据中心建筑 | 100-150 亿美元 |
| 服务器/算力 | 350-450 亿美元 |

```plaintext
[24:11] 2 to 3 million dollars a megawatt, 2 to 3 billion dollars a gigawatt for power plant. The data center is between 10 and 15 billion dollars a gigawatt... the compute, the servers can be anywhere from 35 to 45 billion dollars a gigawatt
```

服务器是绝对大头，而在服务器内部，HBM 内存的价格近期大幅上涨，供应商只有三星和 SK 海力士三家。这意味着算力成本的关键变量不在芯片本身，而在内存供应和网络互联。

对于"同芯片如何提取更多价值"的问题，Balaban 的回答指向了利用率——折旧是 GPU 小时成本的最大组成部分，利用率就是其乘数因子（1/utilization）。50% 利用率意味着每小时折旧费用翻倍。因此，neocloud 的核心竞争优势是构建能驱动高利用率的云软件，使按需零售定价成为可能。

```plaintext
[17:45] one over the utilization. So if you use your capital asset 50% of the time, you will have on a per hour basis twice... the amount of per hour depreciation expense
```

他直言，大多数 neocloud 根本没有能力运行真正的云服务——没有投入数千万到数亿美元的软件开发，就无法将集群切分给按需客户。这是 Lambda 的差异化所在：它的 one-click cluster 产品可以在网页上从 16 GPU 扩展到 4000 GPU，而竞品大多卡在 32 GPU。

## 四、GPU 作为资产类别——2023 年的 H100 今天租得更贵

整场对话中最反直觉的数据点是：Lambda 在 2023 年部署的 H100，现在的租赁价格比当初购买时还高。

```plaintext
[40:46] the chips that we deployed in 2023, H100s, we are now leasing those out at a higher rate now than we were originally in 2023
```

这直接打破了"GPU 三年贬值报废"的叙事。Balaban 指出，会计折旧周期约为 6 年，但经济使用寿命更长——Lambda 拥有业界唯一一批已完全折旧的 GPU 仍在服役。那些声称"5 年扔掉 GPU"的看空者"从头到尾都错了"。

```plaintext
[42:28] the people who are the naysayers, oh, this is going to be you're going to throw these GPUs out in 5 years, are completely wrong. They're completely wrong, and they've been wrong the entire time
```

这一事实正在重塑 GPU 的金融属性。私人信贷市场（private credit market）开始将 Nvidia 芯片视为一种可承销的资产类别——有可预测的现金流、易于风险评估。融资结构分为两类：按需云侧看 Lambda 自身信用质量；长期承购协议（off-take agreement）侧看终端客户信用质量。后者更成熟，因为投资级承购协议可以直接打包进 SPV（特殊目的实体）做资产抵押贷款。

```plaintext
[39:23] you take your off-take agreement, you take this chunk of GPUs that you're deploying, you take a lease or the property and you kind of put it into a box and you can go to the private credit markets
```

关于 GPU 衍生品市场（期货、复杂证券），Balaban 认为还太早——先要有成熟的现货市场，然后才能衍生。但他承认这个方向正在被探索。这隐含着一个信号：如果 GPU 真的成为可交易的金融资产类别，neocloud 的角色会从基础设施运营商向"算力做市商"延伸。

## 五、Nvidia 的护城河不是 CUDA——是 cuDNN 和 NCCL

Balaban 对 Nvidia 护城河的拆解比多数市场分析更精确。他明确指出，Nvidia 的真正壁垒不在 CUDA（"那只是我们游泳的水"），而在 cuDNN——一个高度调优的矩阵乘法引擎，内嵌了 Winograd 滤波等优化算法，以及 NCCL——网络拓扑感知的通信优化库。

```plaintext
[27:08] One of the big moats they've got is just the cuDNN stack. It's not just CUDA. It's... cuDNN has got so many matrix multiplication routine optimizations baked into it
[28:12] The other one is NCCL, which is their networking optimization library, where it will sense the topology and the connected nature of your network... and it will suggest an optimized sort of routine for doing reduce all and broadcast
```

这个判断的产业含义是：新芯片 entrant 要追赶的不是芯片性能本身，而是这套经过多年工程优化的软件栈。Balaban 同时指出，世界已经在多芯片并行——"最大的实验室已经在用多种不同芯片做推理和训练"，但 Nvidia 的平台优势（在所有主流云平台上的可达性 + 开发者生态）短期内难以被替代。

Lambda 的芯片栈覆盖了从 V100 到即将到来的 VR200 全系列 Nvidia 产品。Balaban 用一句"我们从未自己画过一块 PCB"来坦诚 Lambda 不是硬件公司——它的壁垒在软件编排层和数据中心工程层，而非芯片设计。

## 六、垂直整合——从租房客到 GW 级 AI 工厂建造者

Lambda 的战略轨迹是一条清晰的垂直整合路径：最初纯租用数据中心 → 开始自融资建设 → 现在进入全栈垂直整合（选址、设计、融资、建设、装服务器、对接终端客户）。Balaban 用"工程思维进入房地产主导的领域"来概括这一转型。

```plaintext
[35:13] we're going now into full vertical integration, where we are identifying land, coming to the table with a basis of design... financing and constructing that data center, putting the servers in, and then associating that with a long-term off-take agreement
```

在自建数据中心中，Lambda 是唯一租户，目前不打算对外分租。地理上聚焦北美（加拿大、美国、墨西哥），拒绝了向欧洲和亚洲扩张的诱惑——理由是美国市场就是机会所在。唯一的海外布局是首尔一个与 SK Telecom 合作的数据中心。

Balaban 对数据中心行业的一个尖锐观察是：传统数据中心房东对里面发生的事情一无所知——"我们是房地产人，外包给 GC，GC 也不懂，只有租户知道"。而 hyperscaler 建的数据中心是为传统云服务设计的（从卫星基站到磁带存储到人脸识别 API，数百种服务），与 AI 数据中心的优化目标完全不同。AI 数据中心甚至可以容忍更低的可用性/正常运行时间要求，因为推理工作负载的特性不同。

```plaintext
[58:14] the people who've been designing these data centers have really kind of been real estate people... grabbed by the scruff of their neck by a hyperscaler... they don't know anything about what goes inside of it
```

在社区反对声音上，Balaban 表现出明显的"信息纠正"姿态。他认为大量反对基于错误信息——比如"数据中心耗水"的说法，他指出新一代 Blackwell/Rubin 类 GPU 使用闭环直触芯片液冷 + 干冷器，几乎零蒸发，不耗水。数据中心还在为电网带来电力、储能和投资。他的隐含立场是：社区反对不是不可化解的障碍，而是沟通和信息透明度的问题。

```plaintext
[13:20] there's almost zero evaporation. It's not using evaporative cooling. It's using a dry cooler system that does not consume a lot of water
```

关于延迟，Balaban 给出了一个改变云架构假设的判断：AI 应用对延迟远不敏感。用户发出请求后回来取结果（研究报告、长期运行的 agent 工作流），唯一重要的是**每 token 成本**。这意味着 neocloud 不需要像传统云那样在全球布点做区域覆盖。唯一的地理约束来自数据治理——各国要求本国公民的 AI 算力在本国运行。

```plaintext
[37:53] latency doesn't matter at all. The only thing that matters is your cost per token
```

## 七、神经软件——LLM 不是生成软件，而是成为软件

Balaban 在访谈后半段抛出了他最具远见的框架："神经软件"（neural software）或"神经操作系统"。核心区别在于：vibe coding 生成的是静态代码（C/Python），经编译器/解释器执行，生成后不可变；而神经软件根本没有代码在运行——它是神经网络特征激活空间和上下文的实时修改。

```plaintext
[62:43] Neural software, there is no code that's running. It's just modifications of the feature activation space and the context in the mind of the neural network
```

他用一个可操作的实验来说明：让 ChatGPT 或 Claude 渲染一个 ASCII art 桌面界面，然后像操作电脑一样对它说"点击这个""打开那个"——LLM 就在模拟一个操作系统的行为。"不可能有 bug，只有对提示词的误解。"未来这会演进到多模态网络生成屏幕上的每一个像素和扬声器的每一个声波。

```plaintext
[60:44] it's not possible to have a bug, only a misunderstanding about the prompt and what you've asked for
```

他给的时间表是：10-15 年后才会看到大规模普及，但他声称 Lambda 已经有了原型，特斯拉端到端自动驾驶就是神经软件的早期形态。Balaban 自评"通常早 10-15 年"——这是一个审慎的自我校准信号，也暗示他不认为这是近期变现路径。

在 agent 话题上，Balaban 提出了"自组装软件"（self-assembling software）的概念：24/7 运行的 agent 舰队实时实现用户反馈，软件在发布后才开始真正开发，用户集体交互定制。最终 agent 会反向请求人类帮助（"给我插 1000 块 GPU""帮我注册一个 API key""帮我谈判这个合同"）。

```plaintext
[67:16] self-assembling software is because you kind of say, "Hey, this is what the software's for." But most of the development for it's going to happen after the software is launched
```

他同时给出了一个精确的 agent 局限性判断：agent 工作流在软件工程领域有效，是因为有自动化测试提供反馈闭环；但在"去买一个网站"这类无法快速验证的任务上，agent 缺乏迭代牵引力。CAD、有限元分析、计算流体力学等领域因为可模拟可验证，反而是 agent 的好场景。

```plaintext
[72:15] agentic workflows for things that are not software engineering I think tend to be overhyped... one of the ways that you get an agentic workflow working really well is it needs to have very concrete feedback mechanisms
```

## 八、一人一 GPU——半个世纪的类比

Balaban 用 Apple 的"一人一电脑"（one person, one computer）作为 Lambda 的使命锚点。他的论证不是空想——而是一套时间线对照：Apple 1976 年成立，1984 年 Macintosh 发布，但直到 2004 年才接近"一家庭一电脑"，2014 年才真正实现"一人一电脑"（含手机），2024 年才达到电商普及。**半个世纪**。

```plaintext
[70:53] 74, 84, 94, 2004, 2014. 40 years after one person, one computer, do we have probably truly one person, one computer
[71:56] it took Steve Jobs and Apple one of the best companies in the history of capitalism half a century to accomplish their goal
```

"一人一 GPU"的含义是：未来每个美国人日常工作和生活都需要一块 GPU 的算力。Balaban 同时借此传递了一个预期管理信号——这不是一夜之间的事，而是一个跨世代的基建工程。这也解释了 Lambda 为什么聚焦美国市场、为什么做垂直整合、为什么在建 GW 级工厂：这是为"一人一 GPU"铺物理基础。

在组织层面，Balaban 分享了引入 Michel Combes（前 SoftBank International CEO、Sprint CEO、Alcatel CEO）担任 CEO、自己转任 CTO 的决策。他坦率地表示自己从未有过"必须是 founder CEO"的执念，更关心技术和建设世代级公司。他现在的精力集中在"快速数据中心部署"上，目标是让 Lambda 成为全球仅有的两家能做高速部署的公司之一——另一家是 SpaceX。

```plaintext
[57:06] there's two companies in the world that can do high-velocity deployments. SpaceX and Lambda
```

Lambda 的起源故事本身就是一个关于"时机"的寓言：2012 年做人脸识别（AlexNet 同年）、2013 年帮 Perceptio 在 iPhone 上跑 convnet（后被 Apple 收购，成为 iOS 人脸识别功能的基础）、Lambda Hat 摄像头帽子（提前 10 年预见了 lifelogging 数据采集）、Dreamscope 风格迁移（2015 年百万用户，AWS 月账单 4 万美元 → 自建 6 万美元工作站集群，一个半月回本 → 发现"做算力比做应用更赚钱"）。从 2017 年 300 万美元到 2019 年 3000 万美元硬件收入，再到今天近 10 亿美元云收入，完全退出硬件业务。

```plaintext
[49:30] we thought, "Oh, this is like we're saving more money than we're making. Maybe we should be in the business of providing compute to other AI researchers"
```

---

**核心张力与未言之义**

整场访谈有几个刻意回避或未展开的点：

1. **缩放定律的风险对冲**：Balaban 把全部投资逻辑锚定在"缩放定律持续有效"上，但从未讨论如果它突然放缓会怎样。对一个正在建 GW 级工厂的人来说，这是一个不应该被忽略的尾部风险。
2. **Nvidia 依赖度**：Lambda 是纯 Nvidia 商店。Balaban 说"最大的实验室已经在用多种芯片"，但 Lambda 自身没有 diversified。如果 Nvidia 交货延迟或定价权施压，Lambda 的利润空间直接受影响。
3. **竞争格局的模糊化**：他说 neocloud 不会赢家通吃，但没有讨论 hyperscaler 自建 AI 算力对 neocloud 的挤压——Microsoft、Google、Amazon 都在自建 GW 级工厂。
4. **"神经软件"与 Lambda 商业模式的关系**：如果 LLM 直接成为软件，那么对 GPU 的需求结构会怎样变化？Balaban 把这放在 10-15 年后，但也暗示这可能改变算力消费的模式——从训练+推理变为持续的神经计算。
5. **地缘风险**：聚焦美国是清醒的选择，但也意味着放弃了全球算力需求的部分份额——尤其是在数据主权驱动的本地化趋势下。

---

## 深度关联

### → [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]
**本文件论点**：Balaban 把全部投资逻辑锚定在"缩放定律持续有效"上——"钱进去、软件出来"已从预测变成现实，持续低建 [08:18]
**对方论点**：Ilya 论证"Scaling"这个词塑造了5年集体思维方向，公司比想法多，现在需要回到 Research 时代
**关联逻辑**：质疑。Ilya 认为单纯 Scaling 作为唯一范式已走到尽头，需要算法创新；Balaban 作为基础设施建造者押注 Scaling 持续有效。两人的立场差异源于位置不同：Ilya 在模型层看到的是边际收益递减的信号，Balaban 在算力层看到的是需求仍在膨胀。但 Balaban 刻意回避了"如果缩放定律突然放缓"的尾部风险——这正是 Ilya 暗示的方向。

### ← [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]
**本文件论点**：GPU 从未商品化——2023 年的 H100 今天以更高价出租，GPU 正在成为可承销的资产类别，neocloud 有定价权 [40:46]
**对方论点**：电信运营商类比——流量涨2000倍但股价横盘20年，模型无网络效应、无定价权
**关联逻辑**：补充/张力。Balaban 从算力供给侧给出了 Evans "电信运营商类比"的精确反证——如果 GPU 是可承销资产（有可预测现金流、租赁价格不降反升），那算力层暂时不像电信运营商那样丧失定价权。但 Evans 的长期判断可能仍然成立：Balaban 也承认 GPU 衍生品市场"还太早"，意味着算力金融化尚在早期，定价权能否长期维持取决于缩放定律能持续多久。

### → [[Yann Dubois- Why AI Progress Suddenly Feels Real]]
**本文件论点**：Balaban 的"地址市场锥形"论证——AI 需求从客服扩展到软件工程，锥形还在继续扩大，效率提升 10x 反而增加总算力需求 [09:01]
**对方论点**：Yann 论证 AI 进步"突然感觉真实"是可靠性曲线穿过可用阈值的相变，正在从编码向所有垂直领域渗透
**关联逻辑**：镜像。Balaban 从算力需求侧看到的是"锥形扩大"——AI 渗透的行业越来越多；Yann 从模型能力侧看到的是"可靠性阈值越过"——模型从演示级进入可信任级。两人从不同方向指向同一现象：AI 正在从"偶尔有用"变为"系统性基础设施"，这既解释了算力需求为什么持续超出供给，也解释了为什么进步"突然感觉真实"。

### → [[Jensen Huang- Will Nvidia's moat persist]]
**本文件论点**：Balaban 拆解 Nvidia 护城河——不是 CUDA 而是 cuDNN（矩阵乘法优化）和 NCCL（网络拓扑感知通信优化库）[27:08]
**对方论点**：Jensen 的护城河建立在"精确可复现"上——CUDA 要求同一程序在不同 GPU 跑出相同结果
**关联逻辑**：具体化。Jensen 从战略层讲的是"CUDA 生态锁定"，Balaban 从工程层给出了更精确的拆解——开发者绑定的表层是 CUDA，但真正的性能壁垒在 cuDNN 的矩阵乘法优化和 NCCL 的网络优化。这意味着新芯片 entrant 即使兼容 CUDA API，也无法在性能上追赶——因为 cuDNN/NCCL 的优化是多年工程积累，不是 API 兼容就能复制的。

---

**元信息**

| 字段 | 值 |
|------|-----|
| 标题 | The GPU Myth: State of AI Compute 2026 \| Stephen Balaban |
| 频道 | The MAD Podcast with Matt Turck |
| 发布日期 | 2026-06-18 |
| 时长 | 74min |
| YouTube链接 | https://www.youtube.com/watch?v=0NttU4CbyVs |
| 分析时间 | 2026-06-25 |
