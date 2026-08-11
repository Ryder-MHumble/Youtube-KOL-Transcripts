---
title: "Geoffrey Hinton 2022- 反叛自己"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=2EDP4v-9TUA"
transcript: "[[Geoffrey Hinton 2022- 反叛自己 逐字稿]]"
kol: Geoffrey Hinton
channel: The Robot Brains Podcast
duration: "1:27:39"
upload_date: 2022-06-01
tags:
  - kol情报
created: 2026-06-08
order: 38
status: canonical
---

> Hinton 真正反叛的不是反向传播本身，而是现代计算把“同一知识可脱离具体硬件复制”当成默认目标。他提出的替代路线把局部学习、相互蒸馏、尖峰时序和模拟硬件连成一体：放弃程序不朽，换取更低能耗、更少数据和更贴近生物学习的计算。

**视频链接**：https://www.youtube.com/watch?v=2EDP4v-9TUA  
**对应逐字稿**：[[Geoffrey Hinton 2022- 反叛自己 逐字稿]]

## 概述

这场 2022 年访谈的价值，不在于 Hinton 又提出了一种神经网络技巧，而在于他重新定义了 AI 系统的设计目标。反向传播擅长把大量经验压缩进较少连接，现代芯片擅长让同一程序跨硬件精确复现；大脑却处在相反的资源结构中：连接便宜、经验昂贵、每个个体硬件不同。若资源结构不同，最优学习算法与最优计算机形态也可能完全不同。

Hinton 的论证由三层组成。学习层以大量局部目标替代单一端到端目标，以位置之间的相互蒸馏替代严格权重共享；硬件层利用尖峰时间检测一致性，并让模拟器件承担低能耗计算；知识层则接受单台机器死亡后权重无法迁移，只通过行为与输出把知识蒸馏给下一台机器。

这不是现有大模型路线的短期替代方案。访谈没有给出可训练“凡人计算机”的完整算法，Hinton 也承认学习算法正是尖峰硬件尚未被利用的瓶颈。它更像一个长期技术命题：当前 AI 的能耗、数据效率和硬件制造成本，可能不是规模化的偶然代价，而是“知识必须不朽”这一架构选择的直接结果。

## 反向传播不是错，而是为另一种资源结构优化

Hinton 对反向传播的判断比“大脑不用 backprop”更细。他认为高层原则仍然相同：大量参数通过训练样本被调整；差异发生在梯度如何获得。反向传播很可能比大脑更擅长把信息挤进有限连接，但大脑根本不需要解决同一个问题。

> **[4:01]** "Um, I'm fairly confident now that it's not backpropagation."

> **[4:46]** "Um, but my belief currently is that um backpropagation, which is the way deep learning works at present, is quite different from what the brain's doing."

> **[6:20]** "And so, we are willing to throw lots and lots of parameters at a small amount of experience."

大脑拥有数百万亿连接，却只有一个个体能够经历的有限样本；工程神经网络拥有海量可重复数据，却必须把知识装进可制造、可复制和可部署的参数预算。两者的优化方向因此相反：工程系统追求参数效率，大脑追求经验效率。

这给 AI 研发一个更严格的判断标准。不能只问某个算法是否“更像大脑”，而要问它针对什么稀缺资源优化。若线上数据充足而推理成本昂贵，压缩与权重共享合理；若真实反馈极少、每次试错代价高，本地学习和高参数冗余可能更有价值。生物合理性只有转化成资源经济学，才构成工程信号。

## 局部目标把一次经验拆成大量监督信号

Hinton 认为大脑不会让所有层等待一个末端损失统一回传，而是在不同位置和层级同时比较“局部观察”与“上下文预测”。一次输入因此不是只产生一个训练信号，而是在多个空间位置、多个表征层级产生大量一致或不一致的反馈。

> **[7:28]** "I'm convinced that the brain is using lots of little local objective functions."

> **[7:44]** "Um, so as an example, the kind of thing I think would make a good objective function, though it's hard to make it work, is if you look at a small patch of an image and try and extract some representation of what you think is there, you can now compare the representation you got from that small patch of the image with a contextual bet that was got by taking the representations of other nearby patches and based on those predicting what that patch of the image should have in it."

> **[12:02]** "Um I think the brain you have these levels of representation, but at each level you're trying to reconstruct what's at the level below."

这里的核心不是“局部”二字，而是信用分配被重新组织。端到端训练要求误差信号跨越整条网络；局部目标让每一层都拥有可直接计算的训练反馈。它可能牺牲全局最优，却换来并行学习、较少数据和对异构硬件的适应性。

这也构成对当前 agent 学习方式的启发。长任务如果只在最终成功或失败时给一个奖励，信用分配极弱；若能把任务拆成可验证的局部状态，让每一步都比较局部结果与上下文预期，系统更可能从少量高成本轨迹中学习。Hinton 讨论的是视觉皮层，但其结构可迁移到长程软件任务与具身任务的训练设计。

## 相互蒸馏是权重共享的柔性替代

卷积网络和 Transformer 通过共享权重，让不同位置执行同一种函数。Hinton 认为生物系统很难精确复制连接权重，于是提出另一种机制：不同位置不共享参数，而是相互提供教学信号，要求鼻子、嘴等局部表征对同一张脸形成一致判断。

> **[15:29]** "So, what you've got is mutual distillation where they're all providing teaching signals for each other."

> **[15:45]** "If they're trying to agree, if you're trying to get different locations to agree on something. If, for example, you find a nose and you find a mouth, and you want them both to agree that they're part of the same face. So, they should both give rise to the same representation."

> **[17:05]** "And so, although distillation is less efficient than actually sharing the weights, it's much more flexible. And it's much more neuronally plausible."

这是一种重要的效率交换：权重共享以结构一致性换取样本和参数效率；相互蒸馏允许每个位置拥有不同的前端处理与内部结构，只要求输出表征能够协调。前者适合精确制造的同构硬件，后者适合天然存在器件差异的“生长型”硬件。

对多模型系统而言，这比“所有 agent 使用同一模型”更有启发。多个能力、上下文和工具不同的 agent 不必复制同一内部策略，只需通过可验证的中间表征和结果相互校准。蒸馏在这里不是压缩模型，而是异构主体之间传播知识的协议。

## 尖峰时间把一致性变成硬件原语

Hinton 对尖峰神经元的兴趣不是因为它更像生物，而是尖峰到达时间可以廉价编码两个信号是否一致。普通人工神经元不容易直接判断两个输入是否相等，尖峰神经元只需检测它们是否同时到达。

> **[21:13]** "Um if you use spiking neurons it's very easy to build a system where if the two spikes arrive at the same time they'll make the neuron fire. If they arrive at different times they won't."

> **[21:23]** "So using the time of the spike seems like a very good way of measuring agreement. We know the biological system does that."

这使前面的学习算法与硬件形态闭合：如果局部学习的核心信号是表征是否一致，那么尖峰时序并非低功耗实现细节，而是直接承载目标函数的计算原语。模型与芯片不再是先后适配关系，而是由同一种“检测一致性”的需求共同定义。

但 Hinton 同时指出，尖峰硬件缺少好的学习算法。产业判断不能从“更节能”直接跳到“即将替代 GPU”；在局部目标、离散发放与连续时序如何共同训练的问题解决前，它仍是没有软件栈支撑的硬件潜力。

## 凡人计算机用知识死亡换取能耗下降

现有计算机的基础承诺是：硬件坏掉后，同一个程序和同一组权重可以在另一台机器继续运行。Hinton 将这种可迁移性称为知识不朽，并指出它迫使不同硬件在纠错后产生相同结果，从而要求数字化、高精度制造和高能耗离散计算。

> **[55:49]** "Now the cost of the immortality is huge cuz it means the two bit different bits of hardware have to do exactly the same thing. Obviously there are corrections and all that, but after you've done all the error correction, they have to exactly the same thing."

> **[56:43]** "Um if you're just willing to give up on immortality sort of in fiction normally what you get in return is love. Um but if if we're willing to give up immortality, what we'll get in return is very low energy computation and very cheap manufacturing."

> **[57:01]** "So instead of manufacturing computers what we should do is grow them."

凡人计算机是这一交换的完整形态：用纳米技术在 3D 中生长，每台硬件细节不同，无法加载一套通用程序，只能依靠内置学习算法形成自身知识，并大量使用模拟计算。它的优势来自不再强迫物理器件服从抽象程序的一致性。

> **[58:30]** "But I think sometime in the not too distant future we're going to see mortal computers which are very cheap to create have to get all their knowledge in there by learning and are very low energy."

> **[58:46]** "And these mortal computers when they die, they die and their knowledge dies with them."

> **[58:57]** "Um so what you're going to have to do is distill the knowledge into other computers. So when these mortal computers get old they're going to have to do lots of podcasts to try and get the knowledge into younger mortal computers. The first one you build, I'll happily have that one on."

这条路线改变的不只是芯片，而是软件资产的定义。权重文件不再是可保存、可审计和可复制的产品；真正可迁移的资产变成训练环境、教学信号、蒸馏协议与行为测试。机器身份也从“某个模型版本的实例”变成有独特经历、无法完全复制的个体。

其代价同样巨大。不可复制会削弱复现、审计、回滚和灾备能力；知识只能通过有损蒸馏传递，也会形成代际漂移。凡人计算机若成立，治理重点必须从检查静态权重转向验证学习过程和行为谱系。

## 模型可以理解，但不必像人一样理解

Hinton 反对把生成模型的能力永远解释为训练数据重排，因为这种怀疑会在模型完成既定测试后继续移动标准。但他也没有把语言流畅等同于人类式理解。反向传播训练出的模型可能形成稳定、可泛化，却与人类完全不同的表征方式。

> **[1:03:40]** "Um But now that it does it, of course, the skeptics then say, well, you know, that doesn't really count."

> **[1:04:17]** "No, it had I I don't see how it could generate those explanations without sort of understanding what's going on. No, I'm still open to the idea that because it was trained with backpropagation, it's going to end up with a very different sort of understanding from us."

这一区分对 AI 产品比“是否真正理解”的哲学争论更有用。能力验证应看模型能否跨组合泛化、解释和行动；风险验证则必须寻找它与人类表征的系统性差异。模型可能答对大多数题，却在纹理、提示结构或分布外输入上犯人类不会犯的错误。

因此，人类可理解的解释不能成为唯一安全证据。产品应同时保留行为测试、对抗测试、内部表征探针和权限限制。承认模型拥有某种理解，不等于假设这种理解与人的错误分布一致。

## 睡眠与噪声标签揭示“有效数据”不是数据量

Hinton 把睡眠解释为负样本上的反学习：清醒阶段强化真实数据中的一致性，睡眠阶段削弱由网络自身连接产生的虚假相关。无论这一生物学假说最终是否成立，它提供了一个训练视角：学习不只是累积模式，也需要主动删除模型自己制造的模式。

> **[1:10:54]** "Um So, I now think it's quite likely that the function of sleep is to do unlearning on negative examples."

在监督数据上，他给出更可操作的判断：样本价值取决于标签与真相之间的互信息，而不是标签是否完全准确。足够多的噪声标签仍可训练出超过教师的学生，因为每个样本只要保留少量真实信号，规模可以累积这些信号并平均掉噪声。

> **[1:15:47]** "And I had a hypothesis that what counts is the amount of mutual information between the label and the truth."

> **[1:16:31]** "And the answer is yes, you do to within a factor of two. I mean, the training set actually needs to be twice that big, but roughly speaking you can see how useful a training example is by the amount of mutual information between the label and the truth."

> **[1:17:23]** "But the the rule of thumb is basically what counts is the mutual information between the assigned label and the truth."

这对合成数据的含义不是“噪声无所谓”，而是质量应被拆成信号强度与样本规模。模型生成标签可以不完美，但必须与真相保持可测关联；一旦生成器与学生共享同一种系统性偏差，增加样本只会复制偏差，无法像独立噪声那样被平均掉。

产品团队应把数据评估从准确率扩展到信息增益：这批标签为模型提供了多少独立于既有能力的新信号，错误是否随机，是否覆盖关键边界。教师模型更强不是必要条件，教师错误与学生错误是否相关才是关键。

## 原创性来自反共识，大成果还需要细节正确

Hinton 将自己长期坚持神经网络部分归因于早年经验：他习惯周围所有人相信一件自己认为明显错误的事。这种反共识能力让他能承受研究方向多年不被主流接受，但他并未把“不被接受”本身当作正确证明。

> **[51:52]** "Um and so I was used to just having everybody else being wrong and obviously wrong."

> **[52:06]** "I think you need you need I was about to say you need the faith which is funny in this situation. Um you need the faith in science to um be willing to work on stuff just cuz it's obviously right even though everybody else says it's nonsense."

> **[1:26:29]** "I take those reviews as telling me I'm onto something very original. Um And that actually had the function in it that's now used I think it's called NCE."

> **[1:27:30]** "You have to have a big idea for it to be interesting original stuff, but you also have to get the details right."

拒稿可以提示一个想法偏离共识，却不能证明它成立。Hinton 的真正方法是同时维护两个标准：方向上允许长期反共识，执行上要求算法细节最终工作。对创新团队而言，最危险的不是大胆假设，而是用“原创”替代可运行结果，或用短期指标提前杀死需要长期积累的路线。

## 关键判断

1. **现代 AI 的能耗可能是知识可迁移性的价格**：数字化、高精度制造和跨硬件复现共同支持程序不朽，也共同制造能耗与制造成本。
2. **局部目标的价值是提高信用分配密度**：一次经验在多个位置和层级产生训练信号，适合反馈稀缺、试错昂贵的任务。
3. **蒸馏可以成为异构系统的知识协议**：不同模型或硬件不必共享内部结构，只需对中间表征和结果建立可验证的一致性。
4. **硬件创新取决于学习算法闭环**：尖峰与模拟芯片的节能潜力不足以单独形成替代路线，必须先解决可训练性。
5. **模型理解不等于人类式理解**：能力评估应承认泛化事实，安全评估则要寻找其非人类错误分布。
6. **合成数据应按互信息而非表面准确率定价**：弱教师可以训练强学生，但共享偏差不会被规模自动消除。
7. **凡人计算会把治理对象从权重转向谱系**：当机器不可复制，审计、回滚和知识继承都要围绕学习过程与蒸馏链设计。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 凡人计算直接挑战 CUDA 的可复制性前提
**→ [[Jensen Huang- Will Nvidia's moat persist]]**
- 本文件论点：Hinton 认为程序不朽要求不同硬件执行相同计算，由此锁定数字化、高精度制造和高能耗；凡人计算机则放弃权重跨硬件迁移，以生长型模拟硬件换取低能耗（[55:49]、[56:43]、[58:46]）。
- 对方论点：Jensen 将 NVIDIA 护城河定义为可编程架构、CUDA 安装基数和跨云生态形成的完整计算栈，开发者价值来自同一软件能在庞大硬件基座运行（[27:42]）。
- 关联逻辑：两者不是一般的“新硬件 vs GPU”竞争，而是对软件资产可迁移性的相反定价。Jensen 把跨硬件复用视为生态飞轮，Hinton 把它视为能耗根源。若凡人计算只在边缘感知等场景成立，CUDA 仍控制通用训练；若学习与蒸馏协议替代可复制权重，CUDA 最强的生态资产会从优势变成对精确硬件的路径依赖。

### 模型定义硬件的两条路线：精确协同与异构生长
**→ [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]]**
- 本文件论点：Hinton 用局部一致性目标、相互蒸馏和尖峰到达时间把学习算法与硬件原语共同设计；不同位置无需相同结构，只需输出表征协调（[15:29]、[17:05]、[21:13]）。
- 对方论点：Catanzaro 说明 MoE 的动态 token 路由定义 NVL72 互联拓扑，4-bit 预训练算法又反向定义 Blackwell 算术单元；Moore's Law 死亡后，模型与硬件协同成为获得更多智能的必要路径（[35:48]、[45:00]）。
- 关联逻辑：两人都否定“先造通用硬件，再让模型适配”的分层方式，但走向不同。Catanzaro 通过更精确的软硬件协同保持可复制计算，Hinton 通过容忍器件差异换取能效。新的技术雷达不应只比较芯片性能，而应观察学习算法是否开始利用硬件非理想性；那将是协同设计从精确制造路线转向生长型路线的真实信号。

### “模型有理解”仍不足以让内部机制透明
**→ [[Neel Nanda- Understanding the Inner Thoughts of AI]]**
- 本文件论点：Hinton 认为模型能按语言生成此前未见组合，说明它拥有某种理解；但反向传播可能让这种理解与人类完全不同，错误方式也会不同（[1:03:40]、[1:04:17]）。
- 对方论点：Nanda 将可解释性目标从完整还原模型算法降为围绕具体风险建立不完整但可行动的证据，强调 CoT、Probe 和 SAE 都只提供受条件限制的观察（[4:16]、[7:24]）。
- 关联逻辑：Hinton 解决“是否存在理解”的门槛，Nanda 处理“如何在非人类理解下获得可用证据”。两者合并后的产品原则是：不要用哲学否认替代能力测试，也不要用能力表现替代机制审计。模型可以理解任务，同时仍以人类无法预期的表征完成它，因此安全体系必须接受不完整理解并使用多种独立证据约束部署。
