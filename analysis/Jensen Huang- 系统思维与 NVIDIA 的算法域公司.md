---
title: "Jensen Huang- 系统思维与 NVIDIA 的算法域公司"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=I4B37S1dyQQ"
transcript: "[[Jensen Huang The Mindset That Built NVIDIA]]"
tags:
  - kol情报
status: canonical
created: 2026-07-27
---

> Jensen 在 YC Startup School 讲的不是一套创始人鸡血，而是 NVIDIA 的公司定义：它不是芯片公司，而是持续识别、加速并重构“算法域”的系统公司；AI 时代真正不会被自动化的能力，是把算法、计算栈、组织和市场缺口放在同一个系统里推演。

视频链接：https://www.youtube.com/watch?v=I4B37S1dyQQ

对应逐字稿：[[Jensen Huang The Mindset That Built NVIDIA]]

## 核心证据校准

> **[2:43]** "Well, it turns out the algorithm was exactly wrong and the technology that founded the company turned out to be exactly wrong."

> **[4:10]** "the the big lesson is that for me is technology is changing all the time and so long as you're able to confront the reality so long as you are able to learn the technology itself actually doesn't matter."

> **[5:57]** "we realized early on uh that it's not about building a great chip, it's about accelerating an algorithm domain."

> **[6:51]** "our realization is everything to do with algorithm, not the chip uh turns out to be exactly right."

> **[11:33]** "That alexNet was an approach with deep deep learning that allows you to learn any function."

> **[12:50]** "This is a way of doing software and the implications to the processor, the middleware, the algorithms, the applications, you know, what I now describe as the five layer cake."

> **[19:55]** "one of the most important things is systems understanding, systems awareness, system design, system organization, um, but systems thinking."

> **[23:47]** "agents is the new software and how is this new software processed matters a lot to computer architecture"

> **[35:43]** "physical AI. We started working on world foundation model um an AI that understands the laws of physics and how the world works"

> **[43:20]** "the better you are at systems thinking so that you could orchestrate millions of agents solving problems autonomously, the better off you are."

## 概述

这场 49 分钟的 YC Startup School 访谈表面上是 Jensen Huang 给创业者讲 NVIDIA 早期故事：错误的 3D 图形算法、Sega 救命合同、AlexNet 时刻、agent、机器人和年轻人应该学什么。但它真正有价值的地方，是 Jensen 把 NVIDIA 的长期经营逻辑讲得非常清楚：公司不是围绕某一项技术或某一代芯片建立，而是围绕“哪些算法域值得被加速”建立。

这使它和上一篇 Jensen/Axios 访谈不同。Axios 那篇强调开放模型、应用层监管和机器人扩散；这篇更底层，解释了为什么 NVIDIA 能持续跨越图形、深度学习、agent 和 physical AI：它把每次技术突变都还原成系统问题，然后提前 5-10 年重构处理器、中间件、算法、应用和组织。

## 主题脉络

错误算法与现实校准 → 算法域而非芯片 → AlexNet 被看成 universal function approximator → 五层计算栈同时重写 → CEO 作为一线学习者 → agent 是新软件 → 物理 AI 的 sim/eval/post-training 栈 → 系统思维成为 AI 时代的长期技能。

## 一、NVIDIA 的起点不是“看对趋势”，而是迅速承认自己看错

Jensen 没有把 NVIDIA 的早期故事包装成天才预判。他反复强调：公司一开始选择的技术路线“exactly wrong”。这不是小偏差，而是公司存在基础本身错误。

> **[2:43]** "Well, it turns out the algorithm was exactly wrong and the technology that founded the company turned out to be exactly wrong."

更关键的是下一步：他没有把错误归因于市场教育不足或执行不够，而是回到“我们不会正确算法”这个事实。Sega 项目失败时，他去日本告诉对方合同无法履行，同时请求对方继续付钱让 NVIDIA 活下去。这件事经常被讲成 founder resilience，但在这场访谈里，它更像 NVIDIA 方法论的原点：先承认现实，再学习新算法，再重构公司。

> **[4:10]** "the the big lesson is that for me is technology is changing all the time and so long as you're able to confront the reality so long as you are able to learn the technology itself actually doesn't matter."

这个判断和普通“技术选择很重要”相反。Jensen 的意思不是技术无关紧要，而是单项技术不会构成长期身份。真正的长期资产是面对技术错误时的学习速度和组织重构能力。对创业者而言，这比“选对赛道”更残酷：如果公司只能在最初假设正确时活下来，它不是系统公司，只是押注公司。

## 二、NVIDIA 的单位不是芯片，而是算法域

访谈里最重要的一句话，是 Jensen 直接重定义 NVIDIA：

> **[5:57]** "we realized early on uh that it's not about building a great chip, it's about accelerating an algorithm domain."

他举的不是单一市场，而是一组算法域：molecular dynamics、image processing、inverse physics、deep learning。GPU 只是这些算法域被加速时呈现出来的硬件形态。换句话说，NVIDIA 的真正产品不是“某颗芯片”，而是对“某类计算为什么会变重要、它的瓶颈在哪里、需要什么系统形态”的持续判断。

> **[6:51]** "our realization is everything to do with algorithm, not the chip uh turns out to be exactly right."

这解释了为什么 NVIDIA 的护城河不能只看 CUDA、供应链或客户锁定。那些都是真实护城河，但更深一层是“算法域雷达”：它比别人更早判断哪类算法会变成世界级负载，并且愿意围绕它改处理器、软件栈、数据中心和生态。

这也解释了 Jensen 为什么把 AlexNet 看得和很多人不同。别人看到的是一个图像识别模型；他看到的是可学习任意函数的软件范式。

> **[11:33]** "That alexNet was an approach with deep deep learning that allows you to learn any function."

AlexNet 不是 AlexNet。它是 universal function approximator 的早期信号。这个判断一旦成立，问题就不再是“做一个更快的训练卡”，而是“整个计算栈会发生什么”。NVIDIA 的强处恰好在于把这种抽象判断落成完整工业栈。

## 三、五层蛋糕：NVIDIA 提前重写的是计算栈，不是产品线

Jensen 把 AlexNet 的影响延展到 processor、middleware、algorithms、applications，称为 “five layer cake”。

> **[12:50]** "This is a way of doing software and the implications to the processor, the middleware, the algorithms, the applications, you know, what I now describe as the five layer cake."

这句话把 NVIDIA 和普通硬件公司的差别拉开。普通硬件公司响应工作负载，NVIDIA 试图从工作负载反推未来系统结构。它不只是问“模型需要多少 FLOPs”，还问：这种算法会不会改变软件写法？中间件如何组织？应用会不会迁移到新形态？数据中心互联、内存、并发和 sandbox 会不会变成核心瓶颈？

这与 Bryan Catanzaro 关于 Nemotron 的论证形成前后呼应。Catanzaro 说 NVIDIA 自建模型的第一个 job 是让 NVIDIA 继续存在，因为模型架构会决定未来硬件设计。Jensen 在这里给出更上游的 CEO 版本：一旦某个算法域变成世界级负载，整条计算栈都要同时改。

对个人 IP 和产品判断来说，这里有一个可迁移框架：不要把 AI 产品机会只理解成“把模型接进某个流程”。更高质量的问题是：这个任务背后有没有一个正在成型的算法域？它的输入、输出、并发、记忆、权限、验证、部署和商业结果分别是什么？如果这些问题无法回答，所谓 AI 产品很可能只是 UI 层包装。

## 四、CEO 的角色不是管理技巧，而是把一手理解压进组织

Jensen 对 “founder mode” 的解释没有停在风格层。他说自己的状态从 curiosity 开始，如果身边人的回答不能满足，就自己去追问题；一旦发现这个领域对公司重要，就尽可能学习并服务于公司。

这不是“CEO 事无巨细管一切”，而是 CEO 负责把外部快速变化的技术转成组织可行动的第一性原理。访谈中他说，如果没有对变化的 tactile sensation，技术世界会显得快到无法理解；但理解第一性原理后，一切会开始变得可读。

这和很多大公司失败的机制相反。大公司经常把技术变化交给专家层、战略层或咨询层做摘要，CEO 拿到的是二手图表。Jensen 的方法是反过来：最高负责人必须在足够底层的位置形成自己的判断，然后把判断变成组织能跟随的结构。

他用 F1 赛车比喻公司：创始人是在造自己要开的车。组织不是抽象最佳实践，而是要被持续调到驾驶者可以高速驾驶的形态。这里隐含一个强判断：高速技术周期里，所谓“可复制的管理制度”不一定是优势；如果制度让创始人失去一线感知，它会降低系统反应速度。

## 五、agent 是新软件，因此也会反过来定义计算机

当 Garry Tan 问个人是否应该拥有自己的 AI 时，Jensen 没有先讲隐私或主权，而是立刻转向计算架构：NVIDIA 必须理解 agent，因为 agent 是新软件，处理这种新软件的方式会决定计算机结构。

> **[23:47]** "agents is the new software and how is this new software processed matters a lot to computer architecture"

这句话把 agent 从应用层拉回基础设施层。很多人谈 agent，谈的是工具调用、MCP、自动化流程；Jensen 谈的是 workload：并发、sandbox、working memory、long-term memory、异步自治系统、agent 之间的网络。这些变量最终都会落实到数据中心架构、处理器设计、内存层级和调度系统。

这也解释了 NVIDIA 为什么要内部让多种 agent 工具“千花齐放”。它不是单纯提高员工效率，而是在公司内部观测未来 workload。谁在用 Claude Code、Codex、Cursor、Cognition，怎么失败，瓶颈在哪里，哪些 sandbox 模式可行，这些都是下一代系统设计的输入。

这里对产品经理的启发很直接：agent 产品不是“有没有工具调用”这么浅。真正决定产品形态的是 agent 的长期工作流：它需要什么记忆？哪些动作必须 sandbox？人与 agent 的可控粒度在哪里？输出如何验证？如果这些问题没有产品级答案，agent 只会变成带工具的聊天框。

## 六、OpenClaw 是 Linux moment，不是又一个开源项目

Jensen 谈 OpenClaw 时用了非常重的类比：他看到后觉得“we just designed the modern computer”，认为它像 Linux moment。原因不是 OpenClaw 本身解决了所有问题，而是它让每个人、每家公司都能构建自己的 AI。

这与他在 Axios 访谈中支持开放模型的立场一致，但这篇给出了更深理由：开放不是价值观装饰，而是算法域扩散的必要机制。移动云时代如果没有 Linux、Kubernetes、TensorFlow、PyTorch，就不会形成现代云和 AI；同样，agent 时代如果没有开放 harness、sandbox、模型和工具链，就不会出现足够多的 domain-specific AI。

这也是 NVIDIA 的商业悖论：它越支持开放生态，越可能加速模型和 agent 的商品化；但只要每一个自建 AI 都需要计算，NVIDIA 的下层价值捕获就增强。Benedict Evans 担心模型层会像电信运营商一样商品化；Jensen 的答案是，不要当模型层，要当所有模型扩散时都必须经过的算法域基础设施层。

## 七、AI 对就业的影响不是“岗位消失”，而是 backlog 被释放

Jensen 没有否认自动化。他明确说很多 cognitive tasks 会被自动化，尤其是信息完备、响应形式明确的任务。但他反对把任务自动化直接推成岗位消失。

> **[31:55]** "The narrative about AI destroying jobs is exactly backwards. AI eliminate tasks. AI automates tasks away, but it doesn't necessarily doesn't necessarily eliminate jobs."

他的核心机制是 backlog。软件工程、放射科、法律服务都有大量未满足需求；当某些任务被自动化，组织不是一定裁掉人，而是可能承接更多需求，扩大服务能力。

这个论证不是普遍保证“所有人都会更好”。他开头说 “obviously what I'm going to say is uneven”。它更像一个产业判断：在需求积压巨大、服务边际成本下降后能扩大吞吐的行业，AI 会先增加工作系统的总规模；在需求不足或岗位只由单一可自动化任务构成的行业，冲击会更硬。

对个人职业判断而言，关键不是问“我的岗位会不会被 AI 替代”，而是问：我的工作目的背后有没有足够大的 backlog？我能不能从执行单任务的人，迁移成组织更多任务和更大系统的人？Jensen 后面对系统思维的强调，正是这个答案。

## 八、physical AI 的拐点来自“生成视频”和“物理后训练”合流

Jensen 对机器人判断的逻辑，不是“人形机器人很酷”，而是从视频生成推导到 articulation，再推导到 world foundation model。

> **[35:43]** "physical AI. We started working on world foundation model um an AI that understands the laws of physics and how the world works"

当模型能生成手指移动、手抓杯子的视频时，问题就变成：怎样让机器人生成遵守物理规律的动作？这把机器人从机械控制问题改写为物理世界模型 + sim/eval/post-training 问题。

他随后给出三段式栈：real to sim、基于物理与生成式方法的 simulator、sim to real。这里和现有 KOL 知识图谱里的 World Models/JEPA、Applied Intuition、Isaiah Taylor 能接上：physical AI 不是“把 LLM 装进机器人”，而是把验证环境、物理约束、仿真和强化学习连接起来。

Jensen 对落地场景的选择也很务实：第一个大市场不是家庭通用机器人，而是自动驾驶，因为市场足够大、技术相对标准化、有真实经济价值，能形成飞轮。随后同一 autonomous navigation stack 才扩散到农业、配送、仓储 AMR 等较小市场。

> **[38:10]** "And the reason why we open sourced the self-driving car stack is because you need it for agriculture, you need it for mail delivery, you need it for warehouse AMRs."

这句话说明了 NVIDIA 的平台策略：先用大市场训练完整栈，再用开源把栈扩散到长尾实体行业。它不是垂直 SaaS 式逐行业定制，而是算法域平台化。

## 九、系统思维是“百万 agent 编排”的上层能力

访谈最后 Garry Tan 问年轻人应该学什么。Jensen 的回答不是“学 prompt”，也不是“学某个新框架”。他明确说，简单的软件编码会被自动化；不会消失的是 hard science、deep tech、交叉学科和系统思维。

> **[19:55]** "one of the most important things is systems understanding, systems awareness, system design, system organization, um, but systems thinking."

> **[43:20]** "the better you are at systems thinking so that you could orchestrate millions of agents solving problems autonomously, the better off you are."

这把“系统思维”从抽象软技能变成 AI 时代的生产组织能力。因为底层实现会越来越 agentic，人的价值就从“写代码”迁移到定义问题、设置约束、组织信息流、分配 agent、验证结果和连接市场缺口。

这与 Karpathy 的 “you can outsource your thinking but you can't outsource your understanding” 是同一个方向。Karpathy 从工程实践说人不能丢掉理解；Jensen 从产业和组织层说，人必须能编排百万 agent。两者共同指向一个新职业能力：不是会用 AI，而是能把 AI 放进一个有目标、有边界、有反馈、有经济结果的系统。

## 关键判断

- NVIDIA 的核心身份不是 GPU 公司，而是算法域加速公司；GPU、CUDA、数据中心和开源模型都是这个身份的不同实现层。
- Jensen 对 AlexNet 的真正洞察是“软件范式改变”，不是“图像识别市场变大”；因此他直接推演到 processor、middleware、algorithm、application 的五层栈重写。
- Agent 对 NVIDIA 的意义首先是 workload，不是应用：memory、sandbox、并发、异步自治和 agent 网络会反向定义下一代计算架构。
- Open source 是 NVIDIA 的需求扩散机制：模型与 agent 越多样，越需要底层计算；这让 NVIDIA 的价值捕获位置避开了 Evans 所说的模型商品化陷阱。
- Physical AI 的关键不是人形机器人演示，而是 real-to-sim、simulator、sim-to-real 和 physics-grounded RL 构成的后训练系统。
- 个人能力的长期防线不是 prompt 技巧，而是系统思维：定义问题、组织约束、编排 agent、验证输出并识别市场缺口。

## 对个人 IP / 产品情报的启发

如果要把这篇转化为自己的内容，不应写成“黄仁勋创业建议”。更有信息密度的角度是：

1. “NVIDIA 为什么不是芯片公司”：从算法域公司解释它如何跨过图形、深度学习、agent 和机器人。
2. “AI 时代最该学的不是 prompt”：系统思维为什么取代编码细节，成为百万 agent 编排能力。
3. “Open source 如何反而增强 NVIDIA”：模型层越开放，算力基础设施越容易捕获扩散价值。
4. “机器人 ChatGPT moment 已经发生了吗”：把视频生成、world foundation model、sim/eval/post-training 串成 physical AI 路线图。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 算法域公司补上了硬件-软件协同的经营层解释
**← [[Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x]]**
- 本文件论点：Jensen 在 [05:57] 和 [12:50] 把 NVIDIA 定义为加速算法域并重写五层计算栈，而不是制造单点芯片。
- 对方论点：Dylan Patel 认为 AI 真正的 100x 来自模型、系统、网络和硅片的协同设计，单层 2x 优化会困在局部最优。
- 关联逻辑：Patel 给出外部产业分析，Jensen 给出公司内部的经营方法论：协同设计不是某次技术优化，而是 NVIDIA 从 3D 图形到 agent 的组织身份。两者合在一起说明，硬件护城河正在从“性能领先”迁移到“谁能提前识别并塑形算法域”。

### Nemotron 的硬件反馈回路是“算法域公司”的具体落地
**→ [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]]**
- 本文件论点：Jensen 在 [23:47] 说 agent 是新软件，处理 agent 的方式会决定计算机架构。
- 对方论点：Catanzaro 说 Nemotron 的第一个 job 是让 NVIDIA 继续存在，因为 MoE、4-bit、multi-token prediction 会直接定义 NVL72、Blackwell 和推理系统。
- 关联逻辑：Jensen 给出战略命题，Catanzaro 给出工程证据。前者说明为什么 NVIDIA 必须亲自理解 agent workload，后者说明这种理解如何转成硬件形状。两篇共同证明 NVIDIA 自建模型不是模型层竞争，而是计算架构侦察。

### Open source 不是道德选择，而是价值捕获位置选择
**→ [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Jensen 在 [29:43] 鼓励每家公司构建自己的 AI，并把 OpenClaw 类比为 Linux moment。
- 对方论点：Evans 认为基础模型可能像电信运营商一样商品化，价值难以在模型层捕获。
- 关联逻辑：Jensen 的开放叙事可以视为 Evans 问题的一个答案：如果模型层会商品化，最优位置不是继续守模型稀缺性，而是站到所有模型扩散都需要的算法域基础设施层。开放越成功，NVIDIA 的底层需求越强。

### Physical AI 把世界模型从认知架构推向产业后训练栈
**→ [[World Models, JEPA And The Path To Sample-Efficient RL]]**
- 本文件论点：Jensen 在 [35:43] 说 NVIDIA 正在做理解物理规律的 world foundation model，并把机器人拆成 real-to-sim、simulator、sim-to-real 的 eval/post-training 系统。
- 对方论点：World Models/JEPA 把世界模型视为信用分配稀疏性的架构解法，让 agent 在合成 rollout 中预演后果。
- 关联逻辑：World Models 解释“为什么世界模型能改善学习效率”，Jensen 说明“它会在哪里形成产业栈”。两者连接后，physical AI 不再是机器人硬件叙事，而是可验证仿真环境、物理约束和后训练流水线的基础设施叙事。

### 系统思维与不可外包的理解构成同一条个人能力防线
**← [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]**
- 本文件论点：Jensen 在 [43:20] 把系统思维定义为编排百万 agent 的能力，认为简单编码会被自动化。
- 对方论点：Karpathy 认为可以外包 thinking，但不能外包 understanding；agent 像实习生，人仍负责 spec、品味、判断和底层理解。
- 关联逻辑：Karpathy 从工程协作层定义人的不可外包部分，Jensen 从组织和产业层把它扩展为系统编排能力。两者共同给出 AI 时代职业升级方向：不是成为更快的执行者，而是成为能定义系统、约束 agent 并验证结果的人。
