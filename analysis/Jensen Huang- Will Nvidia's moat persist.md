---
title: "Jensen Huang- Will Nvidia's moat persist"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=Hrbq66XqtCo"
transcript: "[[Jensen Huang – Will Nvidia’s moat persist?]]"
kol: Jensen Huang
channel: Dwarkesh Patel
duration: "1:43:12"
upload_date: 2026-04-16
tags:
  - kol情报
created: 2026-07-22
status: canonical
dedup_note: "103min英文完整版；基于 Obsidian 插件真实逐字稿重写"
order: 19
---

> Jensen 这场访谈真正捍卫的不是 GPU 的短期性能领先，而是 Nvidia 作为“从电子到 token 的产业协调层”的位置：它把供应链、CUDA、AI 实验室资本、云生态和地缘开发者网络绑成一个连续系统；最危险的竞争不是某颗 ASIC，而是美国政策或下游集中化把这个系统拆成两套不兼容生态。

**视频链接**：https://www.youtube.com/watch?v=Hrbq66XqtCo  
**对应逐字稿**：[[Jensen Huang – Will Nvidia’s moat persist?]]

## 主题脉络

1. Nvidia 的自我定义不是“卖芯片”，而是把电子转成 token 的系统工程
2. 供应链护城河来自需求侧信用：谁能卖掉未来产能，谁就能让上游提前扩产
3. TPU/ASIC 不是单点性能竞争，而是通用可编程性对模型结构变化的下注
4. CUDA 的锁定正在从“开发者 API”转向“可验证、可优化、可部署的全栈信任”
5. Anthropic 事件说明前沿 AI 实验室已经进入资本绑定阶段，算力供应商必须投资下游
6. 中国出口管制争论的核心不是芯片销量，而是全球开源模型会跑在哪个技术栈上
7. Groq 被纳入 CUDA 生态，预示推理市场从单一吞吐量转向高响应、高 ASP token 分层

## Nvidia 的边界：多做必要的，少做可由生态完成的

Dwarkesh 的开场质疑很尖锐：Nvidia 把 GDS2 交给 TSMC，HBM 来自 SK Hynix、Micron、Samsung，机架由 ODM 组装；如果软件被 AI 商品化，Nvidia 会不会也被商品化？Jensen 没有从“芯片性能”回答，而是把公司定义成电子到 token 的转化器。

> **[0:42]** "The transformation of electrons to tokens and making those tokens more valuable over time is hard to completely commoditize."

> **[1:05]** "Making that token is like making one molecule more valuable than another molecule, making one token more valuable than another."

他的公司边界判断是“必要才做”。Nvidia 不追求把全部环节内部化，而是控制没有它就无法完成的部分，其他交给生态伙伴。这解释了为什么它既不自建晶圆厂，也不直接做云，却要长期投入 CUDA、NVLink、CUDA-X 和各种领域库。

> **[1:50]** "The input is electrons, the output is tokens. In the middle is Nvidia."

> **[2:34]** "We have ecosystems across the entire five layers. We try to do as little as possible, but the part that we have to do, as it turns out, is insanely hard."

这不是谦虚叙事，而是资本效率叙事：Nvidia 的权力不来自占有每层资产，而来自定义各层之间的接口、节奏和可信运行方式。对其他 AI 公司更重要的启示是，护城河不等于“什么都自己做”，而是识别哪一段转化链条如果缺了你就不能高效率发生。

## 供应链护城河是需求侧信用，不只是锁定上游产能

访谈最容易被误读的部分，是把 Nvidia 护城河简化成“提前锁了 HBM、CoWoS、TSMC 产能”。Jensen 承认上游承诺很重要，但他的重点是：供应商愿意为 Nvidia 扩产，是因为 Nvidia 能证明自己有足够大的下游需求，可以消化这些投资。

> **[5:14]** "Some of it is implicit. For example, a lot of the investments that are upstream are made by our supply chain because I said to the CEOs, "Let me tell you how big this industry is going to be, let me explain to you why, let me reason through it with you, and let me show you what I see.""

> **[5:51]** "The reason for that is because they know that I have the capacity to buy their supply and sell it through my downstream."

GTC 在这里不是发布会，而是供应链同步机制。Jensen 说 keynote 像教育，是因为他需要让上游、下游、AI startup 在同一张未来需求曲线上达成共识。Nvidia 卖的不是单点芯片，而是“你今天为我扩产，未来我能替你把风险卖出去”的信用。

> **[6:48]** "I spend a lot of my time informing, directly or indirectly, our supply chain, partners, and ecosystem about the opportunity in front of us."

> **[7:22]** "Regarding the moat as you describe it, we're able to build for a future. If our next several years are a trillion dollars in scale, we have the supply chain to do it."

这也解释了他对 CoWoS、EUV、HBM 瓶颈的乐观。Jensen 认为多数硬件瓶颈只要有明确需求信号，二到三年内可以被产业“swarm”掉；真正结构性瓶颈反而在下游能源和政策。

> **[15:04]** "My point is that none of the bottlenecks last longer than a couple of years, two, three years, none of them."

> **[15:36]** "It's the stuff that's downstream from us. Energy policies that prevent energy from… You can't create an industry without energy."

这个判断要谨慎使用：它是 Jensen 的强立场，不是已经证明的产业定律。但它暴露了 Nvidia 的核心组织能力：提前几年预取瓶颈，并用需求叙事让上游为一个尚未完全到来的市场建设能力。

## TPU 的威胁被 Jensen 重写成“模型结构变化权”

Dwarkesh 对 TPU 的挑战是本场访谈最有价值的反方论证：AI 训练大量是矩阵乘法，TPU 这种 systolic array 似乎更适合主工作负载，GPU 的通用性可能是在浪费面积。Jensen 的回应不是否认矩阵乘法重要，而是把竞争对象从“今天的矩阵乘法”改成“明天的算法变化”。

> **[21:01]** "Matrix multiplies are an important part of AI, but they're not the only part."

> **[21:07]** "If you want to come up with a new attention mechanism, disaggregate in a different way, or invent a whole new type of architecture altogether—like a hybrid SSM—you want an architecture that's generally programmable."

他的核心押注是：AI 进步不会只来自 Moore's Law，而来自模型结构、算法、kernel、fabric、network、library 的联合变化。ASIC 的危险在于它优化了已知结构，但前沿模型的形状还没有稳定。

> **[22:00]** "The only way to really get 10x or 100x leaps is to fundamentally change the algorithm and how it's computed every single year."

> **[23:36]** "We could affect change across the processors, the system, the fabric, the libraries, and the algorithm simultaneously."

这里的深层洞察是：Nvidia 的可编程性不是“通用所以慢”的旧逻辑，而是“前沿还没收敛，所以必须保留跨层重写能力”。如果模型架构进入稳定期，TPU/ASIC 的专用效率会更强；如果模型架构持续突变，CUDA 的可编程性就是研发速度本身。

## CUDA 的新锁定：不是 API，而是可验证的全栈信任

Dwarkesh 继续推进到更难的问题：OpenAI、Anthropic、Google 这些最大客户有能力写自己的 kernel，甚至有 Triton、TPU、Trainium。那 CUDA 还算护城河吗？Jensen 的回答分成三层。

第一层是生态丰富度。开发者在不确定未来部署位置时，会优先选择最广泛、最稳定、最容易 debug 的基础设施。

> **[27:00]** "When something doesn't work, was it you or was it the computer? You would like it to always be you and to be able to trust the computer."

> **[29:01]** "The combination of the richness of the ecosystem, the expansiveness of the install base, and the versatility of where we are makes CUDA invaluable."

第二层是专家优化。Nvidia 把大量工程师派到 AI labs，不是服务姿态，而是价值捕获方式：如果优化让客户模型提速 2x，客户同一批 H100/Blackwell 资产就能产生更多 revenue。

> **[30:21]** "The number of engineers we have assigned to these AI labs is insane, working with them, optimizing their stack."

> **[31:18]** "It's not unusual that by the time we're done optimizing their stack or optimizing a particular kernel, their model sped up by 3x, 2x, 50%."

第三层是 TCO 公开挑战。Jensen 不只是说“CUDA 好”，而是要求 TPU、Trainium 到 InferenceMAX 和 MLPerf 上证明成本优势。这里他的强势也暴露了风险：如果竞争者真能在公开基准和实际大客户账单上稳定证明优势，Nvidia 的高毛利会被重新定价。

> **[32:24]** "Nobody can demonstrate to me that any single platform in the world today has a better performance-TCO ratio."

> **[32:46]** "I encourage them to use InferenceMAX and demonstrate their incredible inference cost."

所以 CUDA 护城河不能再被理解为“开发者离不开 API”。更准确地说，它是安装基数、全栈可调、工程专家、云可用性、性能账单可信度的组合。API 只是表层，真正的锁定在“出了问题能定位，优化之后能变成现金流”。

## Anthropic 不是趋势，而是 Nvidia 错过资本绑定窗口

Jensen 在 Anthropic 问题上的坦诚，比他的 TPU 技术辩护更重要。他把 Anthropic 选择 TPU/Trainium 解释成 unique instance，不是 ASIC 普遍趋势；但他也承认，原因不只是技术，而是 Google 和 AWS 在早期用大额投资绑定了算力承诺。

> **[36:57]** "Anthropic is a unique instance, not a trend."

> **[39:20]** "We just weren't in a position to make the multi-billion dollar investment into Anthropic so that they could use our compute."

这说明前沿 AI 实验室已经不是传统 VC 能支持的创业公司。算力供应商、云厂商和模型公司之间出现了资本-算力交换：谁提供数十亿美元资本，谁就能把未来计算路径嵌入模型公司的基础设施选择。

> **[39:56]** "I would say my mistake is I didn't deeply internalize that they really had no other options, that a VC would never put in $5-10 billion of investment into an AI lab with the hopes of it turning out to be Anthropic."

> **[40:33]** "I'm delighted to invest in OpenAI, and I'm delighted to help them scale, and I believe it's essential to do so."

这改变了 Nvidia 的风险结构。它不再只是卖铲子的中立基础设施，而开始成为下游 AI 实验室的资本参与者。Jensen 口头上坚持“不挑赢家”，但当单笔投资达到 OpenAI、Anthropic 级别，“支持所有人”本身也会变成一种主动塑造市场结构的力量。

## 不做云：Nvidia 用投资维护多极生态，而不是亲自吃掉客户

为什么 Nvidia 不直接成为 hyperscaler？Jensen 的回答延续了公司边界原则：云这件事如果 Nvidia 不做，也会有人做；但 CUDA、NVLink、CUDA-X、cuLitho 这些底层平台，如果 Nvidia 不做，就没人做。

> **[44:24]** "If we didn't take the risk that we take—if we didn't build NVLink the way we built it, if we didn't build the whole stack, if we didn't create the ecosystem the way we did, if we didn't dedicate ourselves to 20 years of CUDA while losing money most of that time—if we didn't do it, nobody else would have done it."

> **[45:41]** "However, the world has lots of clouds. If I didn't do it, somebody would show up."

但他同时承认，CoreWeave、Nscale、Nebius 这些 neocloud 如果没有 Nvidia 支持，很难存在。这不是消极“赋能”，而是主动维护下游多极化，避免算力租赁市场完全被 hyperscaler 把持。

> **[46:25]** "So we invest in our ecosystem because I want our ecosystem to thrive."

> **[49:19]** "Our goal is to focus on what we do, keep our business model as simple as possible, and support our ecosystem."

这也是 Nvidia 不直接做云的战略收益：它通过投资和供给支持让更多云成为买家，而不是把自己变成所有云的竞争者。表面上少拿一层利润，实质上是在保护长期需求侧多样性。

## 中国争论：Jensen 的真问题是美国技术栈会不会丢掉开源世界

中国出口管制段落中，Dwarkesh 代表安全派提出最强反方：如果 Mythos 级模型能发现零日，中国获得更多算力是否会增加美国国家安全风险？Jensen 的第一反应是把“是否给中国算力”改写成“他们是否已经具备足够算力、能源、人才”。

> **[58:26]** "The amount of capacity and the type of compute it was trained on is abundantly available in China."

> **[59:19]** "They have some of the world's greatest computer scientists. As you know, most of the AI researchers in all of these AI labs are Chinese."

他的核心不是否认中国是竞争者，而是否认“禁 Nvidia 就能让中国没有 AI 能力”。在他的五层蛋糕框架里，能源可以部分替代芯片效率，研究人才可以通过算法弥补硬件差距，开源模型会决定全球技术栈。

> **[1:03:00]** "It would be extremely foolish to create two ecosystems: the open source ecosystem, and it only runs on a foreign tech stack, and a closed ecosystem that runs on the American tech stack."

> **[1:07:04]** "So I think you misunderstand that AI is a five-layer cake, and at the lowest layer is energy."

最关键的战略场景是 DeepSeek。如果未来中国开源模型首先优化到 Huawei，而不是 Nvidia，美国失去的不只是芯片订单，而是开源 AI 的默认运行环境。

> **[1:10:19]** "DeepSeek is not an inconsequential advance. The day that DeepSeek comes out on Huawei first, that is a horrible outcome for our nation."

> **[1:19:30]** "The single most important thing to our company is the richness of our ecosystem, which is about developers. 50% of the AI developers are in China. The United States should not give that up."

但 Jensen 的盲点也在这里。他反复把边际安全风险转译成生态控制风险，对 Mythos 这类网络进攻能力的短期损害没有给出同等严肃的成本函数。他的论证更适合回答“长期技术栈竞争”，不完全能回答“短期能力扩散”。因此这段访谈的高价值结论不是“出口管制一定错”，而是：任何管制如果只看芯片层，不看开源模型、能源、开发者和全球南方部署层，都会低估反作用。

## Groq 信号：推理市场开始按 token 价值分层

结尾 Jensen 解释为什么把 Groq 纳入 CUDA 生态。这个动作不是为了“多一种芯片”，而是因为 token 价值已经分化。过去推理优化近乎单维度：吞吐量越高越好；现在软件工程师、agent 工具调用、交互式任务愿意为更快响应支付更高单价。

> **[1:38:00]** "We're doing that now because the value of tokens has gone up so high that you could have different pricing of tokens."

> **[1:39:00]** "Until now, higher throughput is always better. We think there could be a world where there could be very high ASP tokens, and even though the throughput is lower in the factory, the ASPs make up for it."

这意味着推理基础设施会从“每美元 token 数”转向多条产品曲线：批处理、低延迟、超高响应、长上下文 agent、工具调用缓存，每条曲线的经济学不同。对产品经理的直接含义是，不能只问模型调用单价，还要把用户任务的时间价值放进定价模型：高价值工作流里，1 秒响应差距可能比 10% token 成本更重要。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### CUDA 护城河从接口迁移到协同设计
**→ [[Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x]]**
- 本文件论点：Jensen 把 CUDA 的价值从 API 兼容上推到全栈协同，认为 Nvidia 可以同时改处理器、系统、fabric、library 和算法，形成 10x/100x 跃迁 [23:36]。
- 对方论点：Patel 进一步把护城河重构为模型形状与硬件协同设计，指出开源模型的数学结构可能天然适配 GPU，使下游被硬件形状锁定。
- 关联逻辑：Patel 对 Jensen 形成**重构**。Jensen 仍从 CUDA 生态讲护城河，Patel 则把护城河的载体继续下沉到模型结构本身。两者合在一起说明：Nvidia 的未来壁垒不只是开发者习惯，而是模型、kernel、网络拓扑和硅片一起演化后的路径依赖。

### 工程层拆解了 Jensen 的战略层叙事
**→ [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]]**
- 本文件论点：Jensen 说 Nvidia 的优势是让同一计算栈跨应用、跨云、跨行业可靠运行，并用工程专家把 AI lab 的实际模型提速 2x/3x [31:18]。
- 对方论点：Catanzaro 从 NVIDIA AI Lab 内部说明“芯片好但编译器差也没有价值”，加速计算是数千技术组合，任何一环失败都会摧毁整体价值。
- 关联逻辑：Catanzaro 对 Jensen 是**具体化**。Jensen 给出的是董事长视角的生态飞轮，Catanzaro 给出飞轮能运行的工程条件：编译器、库、网络、研究协作必须共同成立。它把“CUDA 生态”从商业口号落到系统工程责任上。

### GPU 资产化与 token 收入函数
**→ [[Stephen Balaban- The GPU Myth State of AI Compute 2026]]**
- 本文件论点：Jensen 把一吉瓦数据中心的目标定义为最大化 tokens per watt，并认为 Groq 代表高 ASP token 市场 [34:53] [1:39:00]。
- 对方论点：Balaban 论证 GPU 从未商品化，而是在缩放需求和 neocloud 租赁中变成可承销资产，算力现金流取决于模型能力持续增长。
- 关联逻辑：Balaban 对 Jensen 是**金融化延展**。Jensen 讲 token 产出和响应速度如何改变推理产品线，Balaban 说明这种 token 产出如何反过来支撑 GPU 租赁、资产承销和 neocloud 估值。两者拼起来，Nvidia 护城河不只是技术问题，也是 token 现金流贴现问题。

### “精确可复现”与凡人计算的正面冲突
**← [[Geoffrey Hinton 2022- 反叛自己]]**
- 本文件论点：Jensen 的 CUDA 飞轮依赖跨硬件、跨云、跨安装基数的可复现运行，开发者要能相信底层计算平台而不是怀疑电脑 [27:00]。
- 对方论点：Hinton 质疑现有数字计算的“不朽程序”前提，认为精确复现锁定高能耗、高精度制造和低生物相似性，凡人计算可能用不可迁移硬件换低能耗学习。
- 关联逻辑：Hinton 对 Jensen 是**根本性挑战**。Jensen 的护城河正建立在 Hinton 认为昂贵的前提上：同一程序在任意 GPU 上可靠运行。如果未来低能耗智能硬件转向不可完全复现的“凡人”路线，CUDA 的最大优势会变成能耗时代的历史负担。
