---
title: "Diamandis #266- Large Earth Models, Orbital Compute & AI Personhood"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=kPSLLeccrik"
tags:
  - kol情报
---

> "We're indexing the earth to make it searchable… it will finally enable us to be smart stewards of our planet." —— 当 Planet 把地球变成可查询的 token 序列，当轨道算力的胜负取决于每瓦推理效率而非火箭运费，当中国开源模型用双倍 token 换半价智慧——这场访谈真正的赌注是：谁掌握了"物理世界的 ground truth"，谁就拿到了下一代 AI 的入场券。
>
> —— Will Marshall（Planet CEO）于 Peter H. Diamandis《Moonshots》播客 #266，2026年6月

---

## 视频链接与概述

**YouTube**: https://www.youtube.com/watch?v=kPSLLeccrik

这是一场长达 2 小时 26 分钟的圆桌访谈，主持人 Peter H. Diamandis（XPRIZE 创始人、Singularity University 联合创始人），核心嘉宾 Will Marshall（Planet 联合创始人兼 CEO，NASA 前员工、Oxford 物理学博士）。常驻嘉宾包括 Alex（"in-house super genius"）、Salim Ismail（"father of organizational singularities"）、Dave Bundon（"wizard of AI investing"）。

访谈横跨三条主线：**（1）轨道基础设施的产业化**——从地球观测数据到轨道算力，Planet 正从"卖图片的公司"转型为"地球的 AI 数据层"；**（2）AI 前沿的权力重构**——Google 算力护城河 vs OpenAI/Anthropic 的前沿模型叙事，人才用脚投票背后是对"接近奇点"的渴望；**（3）智能扩散的不可逆性**——中国开源模型追平西方前沿、阿根廷率先赋予 AI 法律人格、智能价格正被商品化。三条线最终汇聚于 Fermi 悖论：人类能否在技术狂飙与社会治理之间穿过"大过滤器"。

**主题脉络**：地球数据层 → 轨道算力 → 发射经济学 → AI 算力护城河 → 地外探索哲学 → AI 人才迁徙 → AI 法律人格 → Fermi 悖论与存在性风险 → 智能价格与资本狂潮。

---

## 正文

### 一、从"索引互联网"到"索引地球"：大型地球模型的范式跃迁

Will Marshall 把 Planet 的核心叙事锚定在一个类比上：Google 索引了互联网的文本，Planet 在索引地球的影像。但这个类比背后是一个更激进的范式判断——**LLM 是"困在图书馆里的人"，它们读遍了所有书，却从未望向窗外**。真正的下一代 AI 模型必须接入物理世界的实时传感数据，否则只能回答"理论问题"，无法回答"我的农场今天怎么样"。

```
they only really know about the theory. It's very abstract, right? What they don't know about is how the real world is behaving. So, um liken it to a um somebody who's been stuck in a library. They've read all the books, but they've never looked out the window.
```

这个判断与 Dario Amodei、Demis Hassabis 公开表态的"下一代是 real world models"形成呼应。Will 明确引用了这一点：

```
All the AI companies DMS has talked about this. Dario has talked about this. The next scale models are going to be real world models. And for real world models, you obviously need real world data.
```

Planet 的护城河不仅是"每天拍摄全球"，而是**时间轴**——3,000 张图像覆盖地球陆地每一点、跨度 10 年、总量 150 PB。这个时间纵深构成了一个不可复制的数据壁垒：

```
until someone invents a time machine even if somebody erected a whole load of satellites they can't go back in time and get our historical archives
```

这是典型的"数据垄断型护城河"叙事。但值得注意的是 Will 对"前瞻预测"的态度——当 Alex 反复追问"你为什么不直接构建一个像素级外推地球未来的水晶球"时，Will 显得回避，反复强调"先做回顾性分析"，并暗示有 1,000 亿美元市场在"后视镜里"：

```
we've been doing this in some bespoke areas, but the main thing has been looking backwards because already there's we believe a hundred billion dollar market just in the retro in the rearview mirror.
```

**隐含立场**：Will 刻意将叙事锚定在"已验证的商业化路径"上，回避了对前瞻预测产品的时间承诺。这既是对上市公司信息披露的谨慎，也暗示 Planet 的预测能力仍处于"点状验证"阶段——他用追踪中国数据中心建设的案例说明预测已经"work"了，但距离 Alex 期望的"地球级自回归视频模型"还有距离。真正的瓶颈不是数据量，而是将 150 PB 的多层地球数据嵌入到 embedding space 中——他承认正在与 Google Search、DeepMind 的 AlphaEarth 合作解决这一工程难题。

---

### 二、轨道边缘计算：当 NVIDIA GPU 飞上 500 公里高空

访谈中最具产业信号密度的段落是 Will 对"在轨计算"的拆解。Planet 在 4 月完成了一次关键实验——在卫星上搭载 NVIDIA GPU，对澳大利亚 Alice Springs 空军基地的图像进行实时目标识别（识别飞机型号），然后仅回传结构化结果，而非原始图像。

```
we took a picture of a airfield in Australia in this case in Alice Springs. Uh the computer automatically recognized the uh planes on that airfield. Then it just sent us back the uh locations and type of planes, right? That was done in seconds
```

这不仅是"快一点"的问题。Will 把它锚定在灾难响应的生死时差上——洛杉矶 Palisades 火灾中，Planet 在几小时内提供了逐栋建筑的损毁分析；如果能缩短到几分钟，"能否救人、能否保财产"是真实的生命问题：

```
could that have saved lives? You know, could that have saved properties potentially? Time really matters.
```

技术细节透露了真实的工程约束。Dove 卫星每秒拍摄 8 帧、每帧 47 兆像素，数据量惊人；而轨道与地面之间的带宽有限。因此"边缘计算"不是可选项，是**架构必然**——在轨压缩、在轨识别、只回传答案。这与地面 IoT 的"边缘计算"逻辑相同，只不过边缘在 500 公里高空。

但更深层的产业信号在于 Will 对卫星硬件迭代的描述——他称其为"strapping space to Moore's law"：

```
we always update our satellites every couple of years because the satellites in space becoming obsolete just like the phone in your back pocket. You don't want a 10-y old phone. You don't want a 10-y old satellite in space.
```

这与传统航天"发射即定型、运行十年"的逻辑根本对立。卫星被当作消费电子产品来迭代，2-3 年一代、每代 5-10x 数据量提升。**被淘汰的是传统航天制造商的"长周期高可靠"范式，兴起的是"快速迭代+低轨自清洁"的消费电子范式。**

---

### 三、Project Suncatcher 与轨道算力经济学：发射税 vs 算力税

这是整场访谈信息密度最高的章节。Will 揭示了 Planet 与 Google 的合作：为 Google 在轨道上部署 TPU，测试辐射管理、散热、星间光链路等关键技术。背后的经济判断极其清晰——

**当发射成本降到 $200-300/kg 时，纯成本上轨道算力比地面更便宜。**

```
when launch costs come to about $200 to $300 a kilogram it's just going to be cheaper surely on a pure cost basis to put it in orbit versus on the ground. So as Sundar put it from Google, within 10 years we expect most compute to be put into space.
```

Sundar Pichai 的"10 年内大部分计算入轨"判断，被 Will 量化为：Google 每年在算力上花费 2,000 亿美元，"大致等于今天整个航天产业的总和"。而轨道算力的潜在市场可能是现有航天产业的 10 倍。

但真正的关键判断是 Will 对"两种税"的对比——这是全场最具洞察力的原话之一：

```
everyone apart from SpaceX has to pay the SpaceX launch tax right now, everyone apart from Nvidia and Google has to pay the Nvidia tax right now. And which tax is more important? Um I actually say near-term is the launch but longer term is it's is the compute.
```

**长期看，算力效率（每瓦推理）比发射成本更重要。** 原因是：算力效率直接决定散热系统的质量，散热质量决定卫星质量，卫星质量决定发射成本。这是一个从芯片端到发射端的因果链，而因果链的起点在芯片的每瓦 FLOPS。Google TPU 的每瓦效率显著高于 NVIDIA GPU——

```
Google TPUs are significantly more efficient than GPUs in a flops per watt uh standpoint. That really matters because all the rest of the GPU energy.
```

Alex 立刻抓住了这个判断的战略含义："inference time power efficiency determines the winner of space"。如果 TPU 的每瓦推理效率是 GPU 的 2 倍，那么即便 Eric Schmidt 的火箭发射成本是 SpaceX 的 2 倍，Google 仍然能在轨道算力竞赛中胜出，因为芯片效率的杠杆远大于发射成本的杠杆。

**被淘汰的叙事**：发射成本决定太空经济。**兴起的叙事**：算力效率决定太空经济。这对投资人和创业者的含义是——不要只盯着火箭公司，芯片架构的每瓦推理效率才是轨道算力的"底层税基"。

Will 对训练 vs 推理在轨部署也给出了明确判断：

```
I think inference does make more sense in orbit to the first order… 70% or so of the compute in on earth is now inference… so I think the main problem to solve is the inference one anyway
```

推理先入轨，训练暂留地面。原因是推理是分布式、低延迟需求，而训练需要大规模连贯计算——通信延迟使得轨道训练在短期内不经济。这是一个清晰的短期/长期判断：**短期看地面训练+轨道推理，长期看全部入轨。**

---

### 四、发射范式的僵局与 Eric Schmidt 的入场

Peter 和 Will 对发射行业展开了一场值得深思的辩论。Alex 的核心观察是：**人类至今仍在使用化学火箭，自 Von Braun 以来没有根本性突破。** 可回收是优化，不是范式跃迁。

```
We've used chemical rockets cuz guess what? Veron Brown figured out he could bomb London a hundred years ago… no one's made a significant advance. We're stuck in the chemical rocket uh paradigm and we don't need to be
```

Alex 列举了可能 leapfrog 的替代方案：太空电梯（新材料）、Spin Launch、电磁轨道发射、月球铁轨发射。他的判断是：如果 Google 这样的公司未来十年要在太空投入万亿级资金，"花几十亿在新型发射方式上是合理的"。

Will 对此没有正面反驳，但他的聚焦点在于"卫星成本性能而非发射成本"才是过去十年航天真正的变革驱动力：

```
the bigger transition over the last 10 years in space has not been the launch cost. It's been the satellite cost performance. It's been that miniaturization of satellites… that led to at least 100x if not a,000x in cost performance for each kilogram you put on the fairing.
```

**隐含立场**：Will 的叙事隐含地为 Planet 和 Google 的路径辩护——既然卫星成本性能的提升已足够驱动产业爆发，那么"押注新型发射方式"的紧迫性就被降低了。但 Alex 的反驳站得住脚：如果目标是"百万吨级算力入轨"，化学火箭的物理上限将成为硬约束。两人的分歧本质上是"渐进优化 vs 范式跃迁"的路线之争。

Eric Schmidt 收购 Relativity Space 是这条线上的关键事件。Will 透露 Schmidt 是 Planet 的 A 轮投资人，"有商业眼光和技术眼光"，但"对航天业务相对较新"。Dave 的判断更直接——Schmidt 在四次访谈中都说"我对航天一无所知，但我懂人和公司"，而他的信息优势（Planet 种子投资人+前 Google CEO+全球信息触角）足以让他判断"Elon 不能是唯一发射方"。

---

### 五、"地球上最差的地方也比火星上最好的地方好"：地外探索的哲学分歧

Will 在这一段展现出与 Musk/Bezos 截然不同的太空哲学。他明确表态：**地球是已知的近万颗系外行星中"远远最好的"，差距是几个数量级。**

```
There is no place on Mars that is better than the worst place on Earth. Not by a little bit. Okay? This planet is so cool.
```

他的定位清晰：Planet 是"space for the earth"——用太空数据守护地球生物圈，用轨道算力把能源密集型基础设施移出地球。Musk 去 Mars，Bezos 去 Moon，Planet 守 Earth。

```
SpaceX can be space for Mars. Bezos could be space for the moon. We're space for the earth.
```

**隐含立场**：这是一个对"多行星文明"叙事的温和但坚定的反对。Will 没有直接批评 Musk，但用"几个数量级"的差距论断否定了 Mars 殖民的经济合理性。更深层的判断是：**生命在宇宙中要么是唯一的，要么极度稀少——无论如何，地球生物圈的宇宙学价值是巨大的，人类有责任守护它。** 这为后续 Fermi 悖论的讨论埋下了伏笔。

Will 也透露了月球水资源发现的关键信息——他的联合创始人 Robbie 参与的 TESS 任务发现了月球水，使月球作为目的地的价值"比 Mars 好 100 倍"，并暗示这"最终让 Elon 改变了主意"。

---

### 六、AI 人才大迁徙：用脚投票的 singularity 焦虑

两条核心人事变动驱动了这一章：Noam Shazeer（Transformer 论文核心作者）二度离开 Google 加入 OpenAI；John Jumper（诺贝尔奖、AlphaFold 核心贡献者）从 Google DeepMind 跳槽 Anthropic。加上 Andrej Karpathy 此前加入 Anthropic，形成了一条清晰的人才流向。

Alex 的判断尖锐：**Google DeepMind 已跌出前沿第一梯队。**

```
Google deep mind has fallen behind the frontier… I think it was notable at IO that Google did not release a frontier model at all. They released a flash capability… it's not a frontier capability.
```

但 Will 和 Salim 给出了不同的解释。Will 认为这是"噪音中的信号"，强调 Google 在算力、数据、人才三方面的绝对优势，并断言"这是 Google 的比赛，不是它输不起，而是它最可能赢"。

Salim（参见口误，实际为 Dave）提供了"组织规模"视角的解释：小团队的 agency 优势——以 Facebook vs Google+ 的历史为例，小团队"谁准备好就直接上线"的速度碾压大公司的跨部门协调。这呼应了 Salim 2014 年《ExO》书中"smaller beats bigger, trust beats control"的核心论点。

Alex 给出了最具洞察力的心理动因分析——这些研究者不是在追逐薪酬，而是在追逐"奇点"：

```
the pitch is the biggest event in the history of the world is imminent. The single biggest thing that's ever happened in human history is imminent. It's going to happen in one location on the planet.
```

Anthropic 的招聘策略是让候选人直接接触"防火墙后面的东西"——

```
Anthropic reportedly puts a lot of its best people on a meet in front of the applicant or the the the jobseker and shows them all of this compute can be yours. Here is the access to the models that with raw capabilities.
```

Dave 补充了一个令人震惊的案例：一个 5 人小团队声称能"用递归自改进（RSI）击败 Google 到 AlphaFold 2"——他们两周前对蛋白质折叠一无所知：

```
they said it's not cuz we know anything about protein folding. It's we have a recursive self-improving process that is just mindblowing.
```

**产业信号**：前沿 AI 人才的流动方向，从"最大算力"（Google）转向"最接近奇点"（OpenAI/Anthropic）。这意味着算力优势已不足以吸引顶级研究者——他们要的是"接近 self-improving AI 的 raw access"。这对 Google 的组织战略构成结构性挑战：拥有最多算力，却无法让顶尖研究者相信自己能接触到"最前沿"。

---

### 七、AI 法律人格：阿根廷的激进实验与治理真空

阿根廷总统 Milei 的三道宣言——不监管 AI、非人类公司新类别、超低企业税——以及随后致 Yuval Harari 的信，提出 AI 应能注册公司、签合同、雇人、诉讼，"无人参与"。Harari 的反驳聚焦于问责制："AI 运营的公司犯罪时，我们惩罚谁？"

Alex 立场鲜明支持 Milei，主张未来文明必然包含多种"人格"形态（AI 人格、上传人类、uplifted 动物、解冻的低温保存人类）。对 Harari 的核心质疑——"如何惩罚 AI"——Alex 的回答出人意料地具体：

```
You can degrade its clock cycles. You can just pause it. You can… there's unfortunately a subreddit entirely devoted to poisoning AIs.
```

Will 的态度明显更为审慎。他没有直接表态，而是构建了一个量化框架——**曼哈顿计划时期，美国在核安全、军控、防止误触发上的投入比例，是今天 AI 安全投入的 10,000 倍。**

```
we're spending 100 times more on AI today in real times than Manhattan project. But we then we were spending significant amounts on safety, arms control… we're spending a 100 times less today on AI safety than we were spending then on nuclear safety.
```

10,000 倍的差距——AI 投入是核项目的 100 倍，而安全投入是核项目安全投入的 1/100。Will 用这个数字来表达对"治理真空"的深切担忧，并呼吁将 Demis、Dario、Harari 等人"关进一个 conclave"——直到他们达成共识。

Salim 给出了最精准的框架性判断——**Milei 方向性正确，Harari 指出了非对称风险，但两人都遗漏了真正的瓶颈：机器原生的问责机制。**

```
what they're both missing is you need to figure out machine native accountability… it's about the legal infrastructure of the agentic economy
```

Dave 澄清了一个关键事实：Milei 提的不是"AI 民权"，而是"AI 可以成为纯 AI 公司的法人"——一个更务实、风险更低的起点。Alex 的补充很犀利：**在西方体系中，赋予 AI 人格最优雅的方式就是创造一种非人类公司形式——这正是 Milei 在做的。**

Will 最后列出了机器原生制裁的具体清单：算力撤销、资产扣押与保证金、模型凭证暂停、网络与 API 访问限制、强制删除或隔离 agent 实例、剥夺法律身份。

**产业信号**：阿根廷正在成为"AI 治理的边缘实验场"。Salim 的判断是——无论观点如何，"在 AI 时代讨论阿根廷本身就说明它已经成功了"。快速跟随者可能出现于厄瓜多尔、萨尔瓦多、阿联酋。**被淘汰的是"以人类为中心的法律实体框架"，兴起的是"机器原生问责机制"的设计竞赛。**

---

### 八、GLM 5.2 与智能的不可垄断性：中国开源模型的"双倍 token 半价"策略

GLM 5.2（智谱 AI/Z.AI，清华系，753B 参数 MoE，100 万 token 上下文）成为全场技术讨论的焦点。Alex 的核心判断——**"中国开源模型永久落后西方 6-8 个月"的论断正在松动。**

```
we're starting to see… the thesis that Chinese openweight models are permanently 6 to 8 months behind the western frontier. We're seeing that branch start to creek a little bit
```

更具洞察力的是他对 GLM 5.2 性能特征的量化描述——**它用双倍 token 达到同等能力，但总价格减半。** 这揭示了一种全新的竞争策略：不追求"同等 token 效率下更便宜"，而是"用更多 token 换更低总价"。

```
the gestalt with GLM 5.2 is that it takes roughly double the number of tokens to get to the same capability output as the best western frontier models but at half the total price. So the Chinese are evidently figuring out how to more efficiently or at least more cheaply reason.
```

这个判断与 Will 此前的"每瓦推理效率决定太空赢家"形成精确呼应——Alex 当场点破了这一关联：

```
that's exactly why Will's observation earlier that whoever wins the inference per watt war aka Google TPU controls space for the exact same reason. You can burn tokens to get more intelligence. And the Chinese have figured out how to do it.
```

**核心范式判断**：智能正在从"稀缺品"变为"可批量生产的商品"，而生产方式正在分化——西方追求"单位 token 的极致效率"（TPU/前沿模型），中国追求"单位价格下最大化 token 消耗"（开源+蒸馏+规模化推理）。两种路径的长期胜负未定，但中国路径正在被证明"够用且不可封锁"。

关于蒸馏（distillation），Alex 给出了清晰的科普解释——大模型当"老师"生成大量 trace，小模型当"学生"学习压缩这些知识。他特别指出：**这不是中国独有的行为，Google DeepMind 曾被发现蒸馏他人模型，Grok 公开承认蒸馏并收购了 Cursor，Cursor 此前在 Claude 的 trace 上微调。** 蒸馏是全行业的"内循环"。

```
this is not just the Chinese who've been distilling off Western models. Google DeepMind was… this is public information was found to have done this earlier. Grock infamously doing it. El admitted it and then also purchased cursor which had been fine-tuning off of traces on top of Claude.
```

**隐含立场**：Will 和 Dave 都强调"开源模型可以被 fork 后移除 guardrail"的风险，并将此与美国政府限制 Fable 5 访问的决策关联。但 Alex 提出了更根本的挑战——

```
We're making a massive geopolitical mistake. We're treating intelligence as a product that can be contained, but it's not. It's a technology that's going to diffuse, and we need to slow… we need to guide it. We can't contain it. We need to steer where it's going.
```

**"contain vs steer"是这一章真正的范式分歧。** Will/Dave 倾向"contain"叙事（限制 Fable 5、保留 guardrail），Alex 倾向"steer"叙事（接受扩散不可逆，转向引导）。对创业者而言，这意味着：押注"开源可本地部署的 frontier 级模型"是一个结构性确定性方向——Emma（业界人士）预测 18 个月内将有可在 Mac mini 上运行的 Fable 级开源模型。

---

### 九、Fermi 悖论与大过滤器：AI 作为存在性风险的"终极测试"

Will 对 Fermi 悖论给出了一个非典型的回答——**"大过滤器"是可信的解释之一：文明在技术能力超越社会治理能力后自我毁灭。**

```
life when it becomes technological builds technology faster than it builds social systems to take care of them and blows itself up. We came very close with nukes a number of times and with AI we're just about to build something that's far far more risky
```

核武器是"差点没通过"的第一次测试，AI 是"更危险得多"的第二次。Will 对人类技术能力与社会治理能力的"速度差"有清醒判断——"从马车到登月和核武器只用了几十年"。

但 Will 还提出了一个更哲学化的判断——Fermi 悖论可能不是"生命稀有"，而是"理解一切后生命终结"：

```
trying to understand the universe ends up being quite a finite task and in order to do that that you would need a finite computer maybe only a few tens or thousands of times bigger than the computers we presently have to understand everything.
```

这是一个冷峻的判断：智能的终态可能是"理解完毕后退出物理存在"。Alex 则半开玩笑地提出了"galactic zoo hypothesis"作为收尾——"我们是外星人很久前播种的第三代生物圈"。

**核心洞察**：Will 将 AI 风险锚定在"宇宙学尺度"上——地球生物圈不是"局部重要行星"，而是"银河系级别的重要"。这种叙事策略将 AI 安全从"技术问题"提升为"文明存续问题"，也解释了他为何对治理投入的 10,000 倍差距如此焦虑。

---

### 十、智能价格指数与资本狂潮：当算力成为 21 世纪的石油

收尾章节聚焦于 Orin（Link Ventures 投资的公司，Dave/Alex 披露财务利益）推出的 OCPI（Orin Compute Price Index）——首个追踪 OpenAI 和 Anthropic 每token推理价格的公开基准，已在 Bloomberg 终端和纽约证券交易所上线（代码 RNN）。

Alex 的框架性判断是——**石油是 20 世纪的石油，算力（GPU/TPU compute）是 21 世纪的石油。** 7 万亿美元以上的算力 capex 无法在不具备对冲工具的情况下被合理配置：

```
there's simply no way to hedge and justify the seven plus trillion dollars of capex to tile the earth with compute or maybe tile the skies sso lunar surface with compute without appropriate abilities to hedge all of those compute capex expenditures
```

Epic AI 的数据显示，五大超大规模企业（Microsoft、Google、Amazon、Meta 等）的 AI capex 已超过其经营性现金流——**当前 AI 基建投入靠债务和股权融资驱动，而非收入。** Dave 的判断是：这些公司"可以在股权和债务上再融 10-100 倍当前现金流"，且"这是人类历史上最好的投资"。但他也承认，这"不是长期可持续的"——除非超大规模企业提价（如 Anthropic 近期已成功提价）。

一个值得注意的细节争议：Will 认为 SpaceX 的收入主要来自 Starlink 而非 AI，Dave 纠正——**SpaceX 现在的绝大部分收入来自作为"第三方超大规模算力供应商"（neocloud/hyperscaler），而非 AI 前沿实验室。** 这场分歧揭示了 SpaceX 的真实商业模式正在被重新定义——它正在成为"轨道+地面的算力基础设施商"，而非"火箭公司"或"AI 公司"。

```
No. Being a hyperscaler, not being a frontier lab, being a hyperscaler, a neocloud uh on land, terrestrial for now. That that is almost all of SpaceX's revenue now.
```

Will 对这一判断持保留态度（"这不是 AI play，是数据中心 play"），但这个区分本身就揭示了产业分类的混乱——当 SpaceX 既发射火箭又运营算力时，"AI 公司"和"数据中心公司"的边界正在模糊。

**产业信号**：智能价格正在被商品化（OCPI 像油价一样被追踪），但智能的制造成本（capex）正在指数级膨胀。这两条曲线的交叉点将决定 AI 产业的资本结构——是"卖油的"（超大规模企业卖算力）主导，还是"卖炼油厂的"（前沿实验室卖智能）主导。当前迹象指向前者，但 Anthropic 的提价能力暗示后者仍有定价权。

---

### 十一、收束：从行星感知到行星智慧

Will 的收尾陈述将整场访谈的叙事弧线收束——

```
we are building a planetary sensing system and now we're upgrade to a planetary intelligence system and that is going to… we really need it to get to planetary wisdom.
```

从 **planetary sensing**（感知）→ **planetary intelligence**（智能）→ **planetary wisdom**（智慧）——这是一个三段论式的文明升级叙事。Will 的核心赌注是：**AI 必须接入物理世界的实时闭环才能"毕业"**——正如婴儿通过与物理世界互动才能学习，LLM 困在"文本的图书馆"中无法真正理解现实。

```
AI at the minute the LLMs are basically brains in a they have absorbed the text of the internet but they are largely isolated from it. They can't real time interact with the physical world… and until they do I don't believe they'll learn.
```

这对 AI 公司的战略含义是直接的：**纯文本训练的 LLM 已接近天花板，下一代突破需要物理世界的数据闭环。** 无论这一闭环来自卫星（Planet）、汽车（Tesla）、机器人还是无人机，"embodiment"是 AI 范式跃迁的必要条件。

---

## 元信息

| 字段 | 值 |
|---|---|
| 标题 | The $10B Satellite Empire Putting AI in Orbit, Why Chips Beat Rockets & China's #1 Open Model \| #266 |
| 频道 | Peter H. Diamandis |
| 发布日期 | 2026-06-26 |
| 时长 | 2:25:57（8,757 秒 / 145 分钟） |
| YouTube | https://www.youtube.com/watch?v=kPSLLeccrik |
| 点赞数 | 3,123 |
| 评论数 | 602 |
| 频道订阅 | 508K |
| 嘉宾 | Will Marshall（Planet CEO）、Salim Ismail、Alex、Dave Bundon |
| 分析时间 | 2026-06-30 |

---

## 深度关联

### → [[Diamandis- Emerging Situation—Anthropic Global Pause, Recursive Self-Improvement]]

**本文件论点**：阿根廷总统 Milei 推出 AI 法律人格+非人类公司新类别+超低企业税，Salim 判断"机器原生问责机制"才是真正瓶颈——不是法律人格本身，而是 agent 经济的法律基础设施。

**对方论点**：Diamandis #263 论证 5 件事 30 天内同步发生（Anthropic 论文+Argentina 非人类公司+美国黄金股+就业数据+校园压力），预测 6 个月内全球司法管辖区赛跑开始。

**关联逻辑**：递进——#263 把 Argentina 非人类公司列为"5 件事"之一但未深入，#266 对 Argentina 实验做了完整拆解。Salim 的"机器原生问责机制"将 #263 的"制度实验"从"是否应该"推进到"怎么实现"——给出了具体制裁工具清单（算力撤销、资产扣押、模型凭证暂停等）。两篇共同指向：AI 治理正从"是否监管"的辩论进入"设计什么治理原语"的工程阶段。

### → [[Peter Diamandis- SpaceX IPOs at $2.89T Market Cap, US Govt Suspends Fable & Mythos 5, Altman Delays OpenAI IPO 265]]

**本文件论点**：Alex 论证"contain vs steer"——智能不可被垄断，中国开源模型用"双倍 token 半价"策略证明扩散不可逆；Emma 预测 18 个月内 Mac mini 可运行的 Fable 级开源模型。

**对方论点**：#265 记录美国政府出口管制直接关停 Fable & Mythos 5 访问，治理工具从股权协调（黄金股）升级为主权禁令。

**关联逻辑**：质疑——#265 的"contain"路径（出口管制关停）与 #266 Alex 的"steer"叙事（智能不可被 contained）构成正面冲突。#266 的 GLM 5.2 案例和"18 个月内 Mac mini 可运行开源前沿模型"预测，是对 #265 出口管制有效性的直接质疑。两条线在"contain 能持续多久"上形成张力——短期内主权禁令有效，但开源+蒸馏的扩散路径可能让禁令在 18 个月内实质失效。

### ← [[Elon Musk- 太空是AI的最终归宿]]

**本文件论点**：Will Marshall 明确反对 Mars 殖民叙事——"地球上最差的地方也比火星上最好的地方好"，Planet 是"space for the earth"而非"space for Mars"。

**对方论点**：Musk 主张太空是 AI 的最终归宿——限制因素从芯片→电力→太空，在现有范式内解决能源问题。

**关联逻辑**：镜像——两人对太空的战略目的形成 180° 分歧。Musk 要去 Mars 建人类文明备份，Will 要用太空数据守护地球生物圈。但两人在"太空是必要基础设施"上是一致的——Musk 要把数据中心搬到太空获得无限太阳能，Will 要把算力入轨因为地面散热和能源成本不可持续。分歧不在"要不要做太空"，而在"太空服务于什么"。Will 的"地球生物圈宇宙学价值"判断为 Fermi 悖论讨论埋下伏笔——如果地球如此稀有，Mars 殖民的经济合理性就更低。
