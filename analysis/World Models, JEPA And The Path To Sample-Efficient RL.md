---
title: "World Models, JEPA And The Path To Sample-Efficient RL"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=qz4GQ0zUFRw"
transcript: "[[World Models, JEPA And The Path To Sample-Efficient RL]]"
tags:
  - kol情报
  - world-models
  - sample-efficiency
  - RL
  - JEPA
status: canonical
created: 2026-07-23
---

世界模型这条路线的核心价值，不是给机器人多加一个视频预测模块，而是把 AI 学习从“真实环境里昂贵试错”改写为“在内部模型里预演后果”；它直接攻击的是当前 LLM/RL 范式最深的样本效率和信用分配问题。

对应逐字稿：[[World Models, JEPA And The Path To Sample-Efficient RL]]

## 样本效率不是数据量问题，而是有没有可用的世界模型

这期 YC Decoded 一开始就把问题定义得很硬：AI 当前剩下的两个核心约束，一个是 intelligence per watt，一个是 intelligence per sample。前者是算力效率，后者才是学习机制本身。Francois 把“完美样本效率”的极限推到零样本：如果你已经有一个足够好的世界模型，就不需要向环境采样。

> **[2:53]** "model then I should never go to the environment to go and collect samples to train on"

他的例子不是抽象类比，而是牛顿力学和航天轨迹规划。NASA 不需要发射一百万艘飞船去试错，因为它已经有一个可微、稳定、可外推的世界模型。

> **[3:14]** "That is an example of a perfect world model we've built where we're then just letting that world model act."

这也是整场视频最重要的技术判断：样本效率差，不是因为模型还没读够互联网，而是因为它缺少一个能预测“采取动作之后世界如何变化”的结构。自回归 LLM 预测 token，model-free RL 从状态直接学动作；二者都绕开了中间的 transition function。世界模型要补上的，正是这个中间层。

Francois 把这种能力延伸到人类直觉和产品 taste。创业者判断客户会不会喜欢一个产品，本质上是在脑中运行一个社会世界模型。这个判断对个人 IP 和产品工作尤其关键：AI 生成能力越便宜，人的价值越集中到“预演别人如何反应”的模型质量上。

> **[4:19]** "And so we've built this world model over years of entrepreneurship, 10 years of like getting it wrong, right?"

这解释了为什么“多生成几个版本再筛”只能解决低阶问题。真正稀缺的是你是否有一个足够准的内部模型，能在发布前预测用户、客户、领导、投资人会如何反应。世界模型不是机器人专属议题，它也是产品判断、组织判断和传播判断的底层形式。

## 牛顿力学是理想态，真实世界的难点是不可微

视频从无人机控制例子切入，讲清楚世界模型在控制问题里的位置：state transition function 就是 dynamics function，也就是 world model。只要它可微，控制问题可以被优化器求解。

> **[7:46]** "And so this is my state transition or dynamics function or a world model."

但现实世界一旦引入其他行动者，问题立刻坏掉。你无法对另一个人的大脑反向传播，也无法假设股票市场、风险投资、交通环境的规则固定不变。

> **[12:53]** "And I can't like back prop through your brain to tell say what you're going to do with your little drone controller, right?"

这句话是世界模型路线的边界条件：物理对象可以被建模，其他智能体和开放环境不能被简单建成牛顿力学。自动驾驶、机器人、企业 agent 的困难都在这里。它们不是单纯“状态空间大”，而是环境会根据你的动作反应，且这种反应不可微、非平稳、很难重放。

这也解释了为什么很多 AI agent 在网页、办公系统、真实组织流程里不稳定。它们面对的不是静态 puzzle，而是不断变化的人和系统。没有可重放环境、没有稳定 transition function，就只能依赖昂贵 rollout 和后验纠错。

## AlphaGo 的成功不能直接迁移到机器人，因为动作空间会爆炸

Francois 对 AlphaGo 的拆解很有价值：棋类可解，不是因为状态空间小，而是因为动作空间小。国际象棋每步合法动作平均只有十个左右，围棋是 361 个，MCTS 还能勉强覆盖。但如果把围棋扩展成 1000 x 1000 的棋盘，一步就有约一百万个动作，搜索成本立刻失控。

> **[33:16]** "In this case, you know, this still feels somewhat tractable though because the action space is small enough where this like kind of works."

> **[35:19]** "To me, there's one uh the cardality of the action space must be extremely small."

自动驾驶看起来只有方向盘、油门和刹车，但离散化之后动作空间已经远超棋类；机器人手臂的自由度更高，teleop 数据又昂贵，远没有 Tesla 车队那种天然数据飞轮。

> **[40:48]** "your action space cardality, right, is 365,000."

所以“AlphaGo 证明强化学习可以解决真实世界控制”是一个危险外推。AlphaGo 的工程条件是小动作空间、规则稳定、环境可模拟、结果可验证；机器人和企业 agent 刚好相反：动作空间宽，环境非平稳，采样贵，错误代价高。

对技术选型的含义很直接：凡是动作空间宽、真实环境采样贵的任务，都不应该把希望押在 model-free RL 或暴力 rollout 上。更合理的路线是先缩窄动作空间、构建可重放模拟器、引入中间状态预测，再谈强化学习。

## Dreamer 的意义：把真实采样替换成想象 rollout

世界模型真正开始进入工程可行区，是 Dreamer 系列。Francois 描述的核心路径是：先在大量无动作标注的视频或环境数据上训练世界模型，再用少量 action-conditioned 数据把动作注入进去，最后在合成 rollout 上训练 policy。

> **[51:23]** "Um where he basically does the same thing and he focuses on Minecraft."

> **[51:40]** "it did it all on synthetic data, which is kind of crazy."

这个点的价值不在 Minecraft 本身，而在训练范式：如果你能在内部世界里生成足够可信的状态转移，真实环境数据就从“每一步都必须采”变成“少量动作条件 + 大量想象训练”。这是机器人、自动驾驶和 computer use agent 都想要的东西。

> **[52:19]** "we have YouTube we have like flicker we have all these data sets online of like you know people doing things we'd like to use it"

视频扩散和 flow matching 被放在这里，不是因为它们“能生成视频”，而是因为它们可能成为世界模型的底座。Sora、SeaDance、Gaia 这类模型如果再加入 action conditioning，就能从“预测下一帧”转向“预测我采取动作后的下一状态”。

> **[53:26]** "let's do a small amount of action conditioning on them to get to this uh this world model and then we can sample from it a bunch and then train"

这条路线对行业的信号比大多数机器人 demo 更强：机器人短期突破不一定来自更灵巧的硬件，而可能来自“公开视频预训练 + 少量具身动作数据 + 合成 rollout 训练”的组合。谁能把无动作视频变成可行动作模型，谁就能把机器人数据瓶颈打穿一部分。

## 但视频世界模型仍可能只是分布插值，不是物理外推

Francois 没有把 Dreamer 路线讲成银弹。他明确指出一个开放问题：模型可能在分布内看起来很对，一旦被放到训练数据没有覆盖的状态，就会把世界“修正”回数据分布里常见的样子。

> **[1:04:28]** "What's going to happen is because almost all the data is like looks like this driving down the road."

> **[1:04:52]** "This will just turn magically into like a highway and it just like boom."

这对自动驾驶和机器人是根本风险。一个视频扩散模型可能很会生成“像道路的视频”，但这不等于它懂“车撞上房子会发生什么”。它学到的可能是视觉分布，不是物理因果。分布外状态越关键，模型越可能用漂亮但错误的像素掩盖真实风险。

这也是为什么世界模型不能只用视觉逼真度评估。真正该评估的是反事实外推：没见过的摩擦系数、没见过的碰撞、没见过的人类反应、没见过的工具组合，模型是否仍然能预测后果。否则它只是在更高维空间里复刻“看起来合理”的训练集。

## JEPA 是更便宜的潜在空间路线，但短期成熟度不足

JEPA 的吸引力在于不再预测像素，而是在 latent space 里预测下一个状态。这样可以避开高维像素重建，把世界模型压缩到更接近“意义”的空间。

> **[57:55]** "you basically are just going to compress that state into some lower dimensional state space."

但 Francois 对 JEPA 的成熟度很谨慎。直接预测 latent 会 collapse，模型学会输出零向量，必须靠 VICReg、Siamese 等技术补救。

> **[1:00:00]** "now this doesn't work this collapses hard"

他更直接的判断是：自监督学习方向很有潜力，但目前效果还不够好。

> **[1:00:54]** "however, to be completely frank, the this this is self-supervised learning super great."

JEPA 真正值得跟踪的地方，是它可能迁移到 LLM 训练损失上：不用 cross entropy head 预测 token，而是用 hidden state 去预测下一个 token 的 embedding。这个方向如果成立，影响的是训练成本结构，不只是视觉世界模型。

> **[1:02:19]** "And a lot of people are playing with this idea and getting rid of the cross entropy loss entirely."

> **[1:02:25]** "the cross entropy head is actually very expensive."

所以这里的技术判断应当分层：今天要做机器人，Dreamer + diffusion/action conditioning 是更接近可用的路线；要押基础研究，JEPA 代表更深的压缩方向，但还没有达到可直接工程化的稳定程度。

## 世界模型更像大脑，但还少了“睡眠”这个离线训练循环

访谈后半段最有洞察的是 squint test：如果眯着眼看世界模型架构，它确实比自回归 LLM 更像大脑，因为它有状态预测、动作策略和测试时规划。但 Francois 随即提出一个更强的限制：大脑不是模型，大脑是优化器。

> **[1:09:57]** "I think that the brain is the optimizer, not the model"

他把睡眠看作当前 AI 架构缺失的关键机制。所有有智能的物种都睡眠，而睡眠有巨大的进化代价；如果它被保留下来，说明离线重放和长期记忆固化可能是智能系统不可缺的一部分。

> **[1:10:28]** "There's no intelligent species that we're aware of that have any amount of intelligence that don't sleep."

> **[1:11:25]** "And if you don't sleep, then you don't up you don't have long-term memory."

这把 Dreamer 的意义进一步抬高：合成 rollout 不只是机器人训练技巧，它可能是“睡眠/做梦”的工程近似。白天收集经验，晚上压缩、重放、更新权重，这才是持续学习的闭环。当前 LLM 最大的问题之一，是部署中学到的东西困在 context window，不能稳定回流到权重；世界模型 + dreaming 可能是这个问题的一个具体方向。

## 最后的硬瓶颈不是算力，而是高保真感知和快速适应

Francois 最后列出的开放问题非常具体：世界模型的保真度、测试时适应、实时规划速度，以及机器人传感。尤其是触觉这一段，直接指出了具身智能常被低估的数据瓶颈。人类皮肤同时感知触觉、剪切力、温度和摩擦，机器人通常只有稀疏触觉传感器。

> **[1:13:21]** "Our tactile. We can detect sheer force. We can detect temperature and it's everywhere."

> **[1:13:42]** "If I numb your hands, like you actually can't tie your shoes."

这说明“多看视频”无法完全替代 embodiment。很多动作技能的关键反馈不在视觉里，而在触觉、力、温度、微小摩擦变化里。没有这些传感，世界模型再大也会缺输入维度。

对机器人创业和投资判断来说，这意味着只看大模型能力曲线是不够的。真正需要追踪的是三件事：是否有低成本 teleop 数据管道，是否有跨 embodiment 的 action-conditioned world model，是否有足够好的触觉/力觉传感闭环。缺任意一项，demo 都可能停留在“看起来会动”，无法进入开放环境可靠控制。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 世界模型把稀疏 reward 变成中间状态预测
**← [[Karpathy- We're summoning ghosts, not building animals]]**
- 本文件论点：Francois 把 world model 定义为 state transition function，并认为它是 AGI 所需结构；Dreamer 在合成 rollout 上训练 policy，让 agent 在真实行动前先预测下一状态 [7:46, 44:45, 51:40]。
- 对方论点：Karpathy 认为 RL 是“sucking supervision through a straw”——一分钟 rollout 只从最终 reward 拿到一点监督信号，并广播到整条轨迹 [43:19]。
- 关联逻辑：具体化。Karpathy 诊断的是信用分配太稀疏，Francois 给出的是让信号变密的架构路径：如果模型能预测每一步动作后的状态变化，就不必等终点 reward 才知道方向。世界模型不是替代 reward，而是把“最终对错”拆成一串可预演的中间后果。

### 样本效率百万倍鸿沟的根源可能不是参数量，而是缺少内部模拟器
**← [[Dwarkesh Patel- The data black hole at the center of AI]]**
- 本文件论点：Francois 用牛顿力学和人类 taste 说明，高样本效率来自可用世界模型；完美世界模型甚至能做到零真实采样 [2:53, 3:14, 4:19]。
- 对方论点：Dwarkesh Patel 认为当前 AI 的强大主要来自数据黑洞，GRPO 通过数百到数千条 rollout 暴力解决信用分配，人类和 AI 处在完全不同的样本效率缩放曲线上。
- 关联逻辑：补充。Patel 量化了症状：AI 需要海量 rollout，人类少样本学习。Francois 定位了一个可能病因：人类不是靠更多样本，而是靠内部世界模型预演后果。两篇合起来指向同一决策：继续扩大数据管道能摊薄白领自动化成本，但要跨入具身智能和持续学习，必须补上内部模拟器。

### Dreamer 是“部署经验回流权重”的训练时预演
**→ [[Dwarkesh Patel- What does the next training paradigm look like]]**
- 本文件论点：Dreamer 先学习世界模型，再注入少量 action conditioning，并在 synthetic rollouts 上训练 policy；Francois 又把睡眠解释为经验压缩和长期记忆固化 [51:40, 1:10:28, 1:11:25]。
- 对方论点：Dwarkesh Patel 认为当前 AI 部署中学到的知识困在 context window，OPSD 和 dreaming 可能成为下一条 scaling 轴，让经验回流到权重。
- 关联逻辑：预演。Dreamer 已经在训练阶段展示了“想象经验生成训练信号”的工程形态；Dwarkesh 追问的是如何把这件事搬到部署后持续发生。Francois 的睡眠论点连接了两者：智能系统可能需要一个离线 replay/压缩周期，把白天经验转化为长期模型更新。

### 动作空间基数是分支因子在控制问题中的物理化
**← [[Adam Brown- General Relativity from First Principles]]**
- 本文件论点：Francois 认为 AlphaGo 不可直接扩展到机器人，因为 MCTS 依赖小动作空间；一旦动作空间变宽，搜索成本会爆炸 [33:16, 35:19, 40:48]。
- 对方论点：Adam Brown 认为科学发现能否靠 AI 并行搜索，取决于理论空间的 branching fraction；高分支领域必须依赖实验剪枝。
- 关联逻辑：镜像。Brown 讨论理论搜索树，Francois 讨论动作搜索树。二者都说明：搜索能否 work，不取决于“模型是否聪明”这个笼统变量，而取决于每一步会分裂出多少可行动作/候选理论，以及环境能否快速剪枝。机器人难，不只是因为状态复杂，而是因为动作树太宽且真实世界不可微。

### Sutton 的经验流范式给了世界模型更严格的目标定义
**← [[Richard Sutton- Father of RL thinks LLMs are a dead end]]**
- 本文件论点：Francois 认为 world model 是预测下一状态的结构，也是 human brain approach 中接近 AGI 的必要部件 [44:45]。
- 对方论点：Sutton 批评 LLM 只有“人类会说什么”的模型，没有“世界会发生什么”的模型；真正智能来自感知、行动、奖励和世界模型构成的经验流。
- 关联逻辑：补充。Francois 更偏工程路径，展示如何用 video diffusion、action conditioning 和 synthetic rollout 建出世界模型；Sutton 给出更严格的智能定义：模型必须从行动后的世界反馈中学习。两者合起来提醒：只做视频预测仍不够，世界模型最终必须嵌入持续经验流，否则仍可能停在“看起来懂世界”的模仿系统。

**元信息**
- 标题：World Models, JEPA And The Path To Sample-Efficient RL
- 频道：Y Combinator
- 发布时间：2026-07-17
- 时长：1:14:26
- YouTube 链接：https://www.youtube.com/watch?v=qz4GQ0zUFRw
- 处理时间：2026-07-23
