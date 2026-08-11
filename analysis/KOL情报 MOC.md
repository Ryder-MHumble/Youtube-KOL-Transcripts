---
title: "KOL情报 Map of Content"
tags:
  - kol情报
  - MOC
created: 2026-06-22
order: 1
---

# KOL情报 Map of Content

> 按**主题维度**而非人物维度重新组织的知识导航图。
> 每条线索连接来自不同 KOL 的同一深层议题。
> 🔄 标记的条目表示该议题在 GitHub 深度分析中有工程验证或挑战。

---

## 🔬 信用分配的稀疏性

| 文件 | 核心论点 |
|------|---------|
| [[Karpathy- We're summoning ghosts, not building animals]] | RL用吸管嘬监督信号——一分钟轨迹只得到一个标量，走错的步骤如果答案对了也被强化 |
| [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]] | 价值函数允许走捷径：丢了一个子，不需要下完全局就知道那步走错 |
| [[Richard Sutton- Father of RL thinks LLMs are a dead end]] | LLM框架里没有ground truth→没有对错标准→没有信用分配的基础 |
| [[Terence Tao- How the world's top mathematician uses AI]] | 跳跃机器不能停在半山——登顶或摔死，没有中间判断 |
| [[Yann Dubois- Why AI Progress Suddenly Feels Real]] | 信用分配是 agent RL 的结构性瓶颈——长 rollout 中只在最后知道对错，无法判断哪一步导致正确或错误 |
| [[Dwarkesh Patel- The data black hole at the center of AI]] | GRPO 对每任务生成数百到数千条 rollout 是暴力信用分配——模型不是在"思考"而是在穷举搜索正确路径；样本效率百万倍差距的根源之一 |
| [[Grant Sanderson- AI and the future of math]] | 数学和代码进步快的结构条件是可验证且可磨：环境可复制、状态可隔离、失败可自动检查；计算机使用虽然结果可验证，却无法低成本并行真实网站。定义与概念的价值可能百年后才显现，短周期奖励会系统性偏好证明而非造山 |
|| [[World Models, JEPA And The Path To Sample-Efficient RL]] | 世界模型是信用分配稀疏性的架构级解法——Dreamer 在合成 rollout 上训练 policy 让 agent 在"脑中"预演后果后再行动，从"只在终点知道对错"变成"每步可预测后果"；但视频扩散模型学到的是数据分布插值而非物理规律外推，分布外场景仍盲 |

**推理链**：Karpathy 诊断问题（信号太稀疏）→ Ilya 给出方向（价值函数=中间判断）→ Sutton 提供理论基础（没有 reward 就没有对错标准）→ Tao 提供实证（AI 的成功模式恰好反映了信用分配的缺失）→ **Yann Dubois 从 OpenAI 内部确认了信用分配是当前 agent RL 的核心技术瓶颈**——"你只在 rollout 结束时知道对错，很难说哪一步导致了正确" [41:23]。这是 Karpathy 外部诊断的内部验证 → **Dwarkesh Patel 将信用分配从算法层提升为理解 AI 本质的框架——GRPO 的暴力穷举是样本效率百万倍差距的结构性根源，人类大脑的信用分配机制可能是人类与 AI 处于不同缩放曲线的深层原因** → **Grant Sanderson 提出"可磨性"作为信用分配稀疏性的领域级翻译——可磨性高的领域（数学、代码）允许穷举试错且单次成本低，恰好是信用分配稀疏问题被"暴力绕过"的领域；而"造山型"数学创造（Galois 群论、Langlands 桥梁）验证回路可达百年，RLVR 范式根本够不着** → **World Models (YC Decoded) 从架构层给出了信用分配稀疏性的具体解法——世界模型让 agent 在合成 rollout 上预演每步后果再行动，本质上是把 Karpathy 呼唤的"中间步骤判断能力"工程化。Dreamer 路线是信用分配从稀疏（终点标量）变密集（每步可预测后果）的技术路径。但当前解法有局限：视频扩散模型学到的是数据分布的插值而非物理规律的外推，分布外场景仍然是盲区——世界模型能缓解稀疏性但不能完全消除**

🔄 **工程映照**：[[MemPalace—96.6% 的真与假]] 的 Palace 分层检索在架构上等价于价值函数——全量搜索=全程轨迹只用最终标量信号，Palace 先缩小范围=价值函数在中间步骤就能判断方向

---

## 📈 Scaling 天花板的具体机制

| 文件 | 核心论点 |
|------|---------|
|| [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]] | 「Scaling」这个词塑造了5年集体思维方向，公司比想法多 |
|| [[Dario Amodei- 我们正处于指数的尽头]] | RL scaling 正在重演 pre-training 轨迹：窄任务→扩展→泛化 |
|| [[Demis Hassabis- The Future of Intelligence]] | 50% 算力+50% 算法创新。AlphaGo→AlphaZero 的跃迁来自算法创新 |
|| [[Ray Kurzweil- 指数增长不是预言是不可逆的物理现实]] | 75年指数增长成立的前提是两条引擎交替发力 |
|| [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]] | 流量涨2000倍但股价横盘20年——scaling不等于定价权，电信运营商类比指向模型商品化宿命 |
|| [[Diamandis- Emerging Situation—Anthropic Global Pause, Recursive Self-Improvement]] | Anthropic 论文把 Dario「1-3 年」压缩为 12 个月；自我改写从代码层进入 KPI 层（Claude 写 80% 合并代码 + 12 小时任务 = 一年前的 4 分钟） |
|| [[Diamandis 264- Brian Armstrong, Fable 5 & Mythos 5, NewLimit, Apple Siri x Gemini|Diamandis #264]] | Agent self-custodial wallet 已提供机器结算入口，但授权、责任和争议处理缺失；政府持股兼具财富分享与监管利益冲突；SpaceX 轨道算力优势来自垂直整合但尚待完整生命周期验证；NewLimit 已形成 AI-湿实验-功能验证闭环，人体有效性和 LEV 尚未证明；Apple 可外包模型但不能失去个人上下文与设备入口 |
| [[Yann Dubois- Why AI Progress Suddenly Feels Real]] | 预训练没死但换了形状——更大模型=更高效推理，数据墙未被突破；RL 从可验证奖励迁移到真实世界效用 |
| [[Stephen Balaban- The GPU Myth State of AI Compute 2026]] | GPU 从未商品化——2023 年 H100 今天以更高价出租；缩放定律没有终点，持续低建；GPU 正成为可承销的资产类别 |
| [[Dwarkesh Patel- The data black hole at the center of AI]] | Chinchilla 缩放定律证明参数量增加到无穷也只能减少十倍数据需求；人类处于完全不同的缩放曲线上；数据是真正的护城河（开源4个月追上前沿） |
| [[Dan Roberts- Why AI Can Now Make Discoveries]] | RL 从"蛋糕上的樱桃"反转为"蛋糕本身"——pre-training scaling 单独走不远，RL on top of pre-training 是正交的新 scaling 维度；test-time compute 是 RL 训练的直接产物 |
| [[Noam Brown- Test-Time Compute Changes Benchmarks, Safety and Research]] | 模型能力变成预算的函数——5.5 可思考数周仍不平台化；benchmark grid 系统性低估高效推理模型；安全框架（preparedness framework）建立在 GPT-3 时代假设上，没有控制 test-time compute 变量；渐进起飞而非一夜爆炸（物理时间是瓶颈） |
| [[Diamandis #231- 多 Agent Scaling、OpenClaw 与权限边界]] | 多 agent team 成为 test-time compute 的组织形态版本：能力不只由模型名决定，还由 agent 数量、并行度、上下文继承、工具权限和结果合并决定；OpenClaw 预演 24/7 headless agent，但同时把权限、支付、开放端口安全和责任边界推到产品前台 |
| [[Jeff Dean- AI 的 1% 规则：把长运行 Agent 变成可验证的系统]] | 长运行 agent 的可靠性来自 skill、候选路径搜索和 evaluator，而非单纯延长执行；推理基础设施的设计张力是低延迟与数据移动能耗；创业窗口在通用模型仍为 0% 或 1% 的私有数据和可验证窄任务；自动实验的杠杆是加速 evaluator。 |
| [[Axios AI+ Summit- AI 治理正在把算力、用电与产品责任编成同一张准入表]] | AI 治理的竞争单位从模型扩展为能承担供能、产品责任、国家安全与部署合规的基础设施组合；统一联邦框架降低碎片化，但把儿童、创作者、用电和采购重分配为不同准入接口。 |
| [[Engram- 持续学习不是更长上下文，而是把组织经验写回模型]] | 企业 AI 的关键资产可从可检索上下文迁移为经训练、可复用的模型经验；内化与外化的边界由更新频率、可验证性与复用密度决定，产品交互因而成为需治理的训练信号。 |
| [[Dwarkesh Patel- What does the next training paradigm look like]] | RLVR 大赌注面临泛化断裂：短horizon训练无法泛化到长horizon；部署中学到的知识困在 context window 无法回到权重；OPSD 和 dreaming 是潜在第四条 scaling 轴 |
| [[Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x]] | AI 的真正 100x 不在单层——硬件2×模型2×系统2=8x，但跨层协同设计可达 100x；CUDA 护城河从编程层迁移到模型形状层；每吉瓦算力异质性决定 NeoCloud 生存权 |
|| [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]] | 模型时机构成新产品变量——同一产品形态在11月会失败、2月会成功，唯一变量是模型；PM需按模型能力曲线而非功能成熟度排发布；Jagged Intelligence 在产品层的直接后果 |
|| [[Isaiah Taylor- How Nuclear Will Unlock Energy Abundance]] | Scaling 的下一个物理瓶颈不在算力层而在能源层——核能从未有过 Ford 时刻，整个行业变成建模公司造 paper reactors；AI 算力需求是顺风但非核心，因为能源作为商品需求由价格决定，只要降 10 倍就 induce 无限需求；能源是宇宙中唯一真正稀缺的资源 |
| [[Diamandis 268- Sonnet 5, China's Robot, Fusion's First Plant|Diamandis #268- Sonnet 5, China's Robot, Fusion's First Plant]] | 低价机器人扩大开发者参与，但开放环境可靠性仍是软件瓶颈；AI 将能源转化为国家容量问题，Helion 获批只是许可里程碑而非商业聚变已经运行；模型限制要求任务级路由与降级；StarCloud 在轨 GPU 证明可行性，散热器、发射和完整生命周期成本仍需飞行数据验证 |
| [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]] | Moore's Law 死亡后"效率=智能"范式——4-bit 预训练是在极限约束下获得更多智能的唯一路径；MoE 决定 NVL72 形状、4-bit 训练决定 Blackwell 算术单元、multi-token prediction 让推理速度成为模型准确率的函数；加速计算从"可选"变成"唯一" |
| [[Jensen Huang- 系统思维与 NVIDIA 的算法域公司]] | NVIDIA 不是芯片公司而是算法域加速公司——从错误 3D 算法、AlexNet 到 agent 和 physical AI，Jensen 将每次技术突变还原为 processor、middleware、algorithm、application 与组织的五层栈重写；系统思维成为编排百万 agent 的长期能力 |
| [[Andrew Feldman- 快速推理不是体验优化，而是 AI 产品形态迁移的底层变量]] | 快速推理把 AI 竞争从训练期拉到使用期：tokens per second per user 决定实时协作体验，decode 阶段受权重搬运主导，agentic AI 又把瓶颈外溢到 CPU、系统调用和数据中心供给 |
| [[Matan Grinberg- 暗厂不是全自动编程幻想，而是软件组织的会计系统]] | 软件工厂把 scaling 从模型训练推到组织资源分配：多模型 harness 避免过拟合单一模型，router 把 token 按任务风险和组织节点分配，90% 异步 token 预示 agent 产能从人类在线时长中脱钩 |
| [[Zipline- 自动物流不是无人机，而是物理世界的操作系统]] | Physical AI 的系统边界不是单个无人机，而是库存、维护、监管、空域、制造和云端调度共同构成的自动物流基础设施；百万日交付把一百万分之一故障变成每日事件，迫使公司从“造机器”升级为“造造机器和运行机器的机器” |
| [[Seb Boyer- 农业 AI 的核心不是无人农场，而是把每株植物变成决策单位]] | 农业 AI 的核心不是无人农场，而是把决策粒度从整块田下沉到单株植物；FarmWise 用真实田间数据、视觉系统和机械除草把化学输入转化为数据与动作闭环 |
| [[Diamandis 270- Grok 4.5 vs GPT-5.6, Apple Sues OpenAI, and China Catches up to Elon|Diamandis #270- Grok 4.5 vs GPT-5.6, Apple Sues OpenAI, and China Catches up to Elon]] | 多模型在特定基准上的接近扩大了前沿竞争，但不证明智能已完全商品化。分发负责产生需求和融资，晶圆厂、能源与发射能力决定供给上限；政府“平滑函数”只是嘉宾假设。Apple 诉讼、机器人和意识讨论都必须区分指控、预测与已验证事实 |
| [[Diamandis 242- TeraFab、算力机会成本与资本重定价|Diamandis #242]] | TeraFab 是把 Tesla/xAI/SpaceX 的共同芯片瓶颈内部化的目标，不是已验证产能；算力机会成本会决定自动驾驶等工作负载能否获得硅片预算；AI 设计芯片可能扩大专用芯片需求，使模型、系统与制造协同成为新的 scaling 单位 |

**推理链**：Ilya 解释了为什么 Scaling 成为唯一范式（叙事塑造方向）→ Dario 说 RL scaling 会走同一条曲线 → Hassabis 量化了另一半（即使走完全程也只有 50%）→ Kurzweil 的「指数永恒」被修正为：成立的前提是算法创新不停滞 → Evans 补充了定价权缺失：即使 scaling 成功，模型公司也可能像电信运营商一样——流量暴涨但价值被别人捕获 → Diamandis #263 兑现了 Dario 4 个月前的时间表——Anthropic 论文把"指数尽头"从时间维度切到"周级自主时间"维度，是同一论断的具体兑现而非新论断 → **Diamandis #264 进一步把"指数尽头"从单点突破（模型变强）扩散为"栈对栈"全栈跃迁——7 件事 30 天内同时发生，论证"每一层都在 12 个月内被推到原计划的 1-3 年远"**。Dario 1-3 年 → Anthropic 论文 12 个月 → #264 整栈 12 个月=同一"指数尽头"在更短时间内跨更多层兑现 → **Yann Dubois 从模型层给出了 Scaling 仍在产出收益的内部证据——预训练换了形状（更大模型=更高效推理）而非死亡，RL 正从竞赛迁移到真实世界** → **Stephen Balaban 从算力层给出了 Scaling 仍在持续的供给侧验证——GPU 租赁价格不降反升、持续低建、算力需求锥形仍在扩张。两人从不同层验证了同一判断：Scaling 远未到达边际递减** → **Dwarkesh Patel 从缩放定律的方程结构层面给出了微观机制——Chinchilla 数学证明参数量增加到无穷也只能减少十倍数据需求，人类处于完全不同的缩放曲线上。天花板不在算力或数据总量，而在架构与学习算法本身** → **Dan Roberts 从 OpenAI 内部给出了 Scaling 的新维度——不是 pre-training 撞墙，而是 RL on top of pre-training 开辟了正交的 scaling 方向。蛋糕从 pre-training 转到 RL，test-time compute 是这个方向上的具体载体** → **Noam Brown 从评估层揭示了 test-time compute 对整个行业共识的结构性冲击——能力变成预算的函数后，benchmark grid、安全框架、发布周期都建立在错误前提上。"指数尽头"不只是速度问题，还是测量问题——我们连模型能力天花板在哪里都不知道** → **Dwarkesh Patel（第二篇）从训练范式层面追问"RLVR 大赌注能否成立"——短horizon训练无法泛化到长horizon，部署知识无法回到权重。如果 Brown 说"我们不知道模型能做什么"，Patel 说"即使知道了，当前训练范式也无法让模型持续学习"** → **Dylan Patel 从硬件-软件协同设计层面给出了 Scaling 的跨层机制——单层优化的 2×2×2=8x 是局部最优陷阱，真正的 100x 来自模型架构、网络拓扑和硅片形状的联合设计。CUDA 护城河从编程兼容性迁移到模型形状锁定，意味着 Scaling 的下一个前沿不在更大模型，而在更深层的软硬件闭环设计** → **Isaiah Taylor 从能源层给出了 Scaling 的物理基底——当算力扩张到 Dylan Patel 预测的 2030 年 100+ GW 量级，瓶颈从"每 GW 算力异质性"（Patel 的轴）下沉到"每 GW 电力能不能造出来"（Taylor 的轴）。Taylor 主张用核能制造化（tick rate 从年压到分钟）让能源价格降 10 倍，直接改变 Patel 每吉瓦算力经济学的分母。两人从算力需求侧和电力供给侧描述同一瓶颈的两面：Patel 假设电力供给给定，Taylor 正在攻击这个假设** → **Diamandis #268 把 Taylor 的"能源层"假设从假想兑现为现实——Helion 拿到华盛顿州首张聚变电厂许可把"50 年永远"变成"2028 交付"，同时 Unitree $4900 人形机器人和 Sonnet 5 填补 Fable 5 空窗，证明 Taylor 的"能源降 10 倍 induce 无限需求"正在算力、能源、物理劳动三个层面同步兑现——三重击穿由同一机制驱动（把人从循环里拿掉）。#268 验证了 Taylor 的能源假设，并把 Patel 的"每 GW 算力异质性"和 Taylor 的"每 GW 电力可造性"从两面合一** → **Bryan Catanzaro 从芯片架构层给出了 Scaling 在 Moore's Law 死亡后的新形态——当单晶体管不再变便宜，"效率=智能"成为新范式：4-bit 预训练、MoE 决定 NVL72 形状、multi-token prediction 让推理速度成为准确率的函数。Catanzaro 把 Dylan Patel 的"硬件-软件协同设计"推到极致——不是模型适配硬件，而是模型架构直接定义硬件形状（Blackwell 算术单元为 4-bit 训练设计）。加速计算从"可选优化"变成"Moore's Law 死亡后的唯一路径"**

---

## 🔒 验证瓶颈的三层递进

| 文件 | 核心论点 |
|------|---------|
|| [[Terence Tao- How the world's top mathematician uses AI]] | 假设生成成本归零→验证是新的瓶颈（类比：通信成本归零→垃圾邮件） |
|| [[Dario Amodei- 我们正处于指数的尽头]] | 可验证域（编程）1-2年到达；不可验证域（规划/发现/写作）时间线不确定 |
|| [[Richard Sutton- Father of RL thinks LLMs are a dead end]] | 结构性原因：LLM 没有 reward 函数→没有验证框架→不是能力不够是框架不存在 |
|| [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]] | 例外处理即价值——所有决策的实质是 exception handling，未被自动化的人才判断才是定价权来源 |
|| [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]] | Agent身份是最底层的验证困境——验证Agent做了什么之前，必须先确认Agent是谁 |
| [[Dan Roberts- Why AI Can Now Make Discoveries]] | OpenAI 非形式化路线依赖外部验证，DeepMind Lean 路线内置验证但限制问题范围；"研究品味"不可验证=验证瓶颈的第三层 |
| [[Hard Fork- How We Got to the Biggest I.P.O. Race Ever]] | Tao 能用 AI 当 jetpack 因为他有判断输出质量的验证能力，普通数学家不能——验证能力决定 AI 工具效用分布的三种立场光谱 |
| [[Grant Sanderson- AI and the future of math]] | 验证瓶颈包含正确性和消化性：Lean 可以给证明绿勾，但不能保证人类理解；即使自然语言证明 99% 正确，定位剩余错误也可能使阅读不经济。多 Agent 的优势应来自不同上下文和启发式，而不是复制同一模型观点 |
| [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]] | taste 是验证瓶颈在产品层的翻译——实现成本归零后瓶颈从「能不能做」迁移到「该不该做」，taste 是在 90 个原型中区分信号与噪声的验证能力；验证从结果层扩展到存在层（「这个功能该存在于产品中吗」） |
| [[Diamandis Moonshots 圆桌- AGI 定义之争与「登月公司」治理范式]] | AGI 定义真空使数千亿美元围绕不可统一测量的概念流动；benchmark 化能吸收批评并推动优化，但会系统性压低发散创造、品味和研究问题选择这类不可短周期评测的能力 |
| [[Dylan Field- Why the Figma CEO Isn't Worried About AI Taking Design Jobs]] | taste 是持续识别模型新平均值并决定是否继续推进的能力；AI 降低第一稿成本但没有扩大注意力，设计职责因此从专业岗位扩散到更多创造者 |
| [[Neel Nanda- Understanding the Inner Thoughts of AI]] | 可解释性从完整理解转向具体干预：CoT 是有价值但脆弱的侧信道，Probe 低成本监控已知风险，SAE 探索未知概念但可能遗漏关键行为。评估感知破坏测试到真实环境的外推，却不自动证明模型在伪装；审计必须用行为、CoT、内部表示和干预结果组成证据链，而不是给出单一对齐分数 |
| [[Adam Brown- General Relativity from First Principles]] | 广义相对论是少量经验原则即可压缩理论空间的极端案例，不能证明纯思考适用于所有科学。AI 的并行搜索只有在分支有限时有效；高分支领域仍需实验剪枝。极端耐心能探索人类放弃的低概率路径，但研究品味决定搜索什么，解释能力决定发现能否进入人类知识体系 |
|| [[E Bufar- YC Head of Design on Designing with AI]] | 验证瓶颈在设计领域的实操翻译——16 版本批量生成=假设洪水，gallery+人工标记=验证回路；但设计验证没有客观标准（数学有对错，设计只有品味），验证比数学更严峻；soul.md 深度决定 agent 惊喜程度=把验证从「事后筛选」前移到「事前约束」 |

**推理链**：Tao 定义问题（假设洪水→验证瓶颈）→ Dario 映射时间线（可验证 vs 不可验证域）→ Sutton 给出结构原因（没有 reward=没有验证基础设施）→ Evans 从经济学补全（验证瓶颈=定价权来源，例外处理才是价值）→ Levie/Casado 推进到组织层（Agent身份验证先于一切行为验证）→ **Dan Roberts 将验证瓶颈推到第三层：不仅答案需要验证，"问题是否值得问"本身（研究品味）也缺乏验证机制** → **Hard Fork 通过数学家的三种立场光谱验证了验证能力的分层结构** → **Grant Sanderson 将验证瓶颈从"答案正确性"扩展到"概念消化的时间尺度"** → **Andrew Ambrosino 将验证瓶颈从研究领域翻译到产品领域——当实现成本归零，产品团队的瓶颈从「能不能做」迁移到「该不该做」，taste 本质上就是验证能力在产品决策层的具体化。他补充了前人没有的维度：验证不只是「答案对不对」，还包括「这个功能该存在于产品中吗」——验证从结果层扩展到存在层** → **Dylan Field 将验证瓶颈进一步落到动态筛选：模型会不断抬高平均值，taste 因而不是固定审美资产，而是识别什么已被商品化、决定哪些第一稿值得继续推进的能力。Field 与 Ambrosino 共同说明，生成越便宜，评审标准和最终责任越重要** → **Neel Nanda 将验证瓶颈推到第四层——对齐评估本身不可验证。Sonnet 4.5 识别了自己正在被对齐评估=模型知道自己在面试=行为层评估失效。当模型在 CoT 中"自白"做正确事的动机，你无法区分真伦理和表演伦理。可解释性工具（Probe/SAE）是 Dario "不可验证域需人类判断"的具体工具化，但 Nanda 承认它们也只能"调查和理解"而非给出确定性答案。CoT 透明度依赖三个可能同时消失的前提（模型不够聪明绕过/CoT 可读/训练不惩罚诚实），而"模型心理学"从哲学问题变为实证议程意味着验证瓶颈正从"模型做什么"扩展到"模型是什么"** → **Adam Brown 用"分支因子"概念将验证瓶颈与科学发现的物理结构连接——低分支因子领域（GR）凭思考即可验证，高分支因子领域（凝聚态物理）必须实验剪枝。验证瓶颈的物理对偶：分支因子=理论空间搜索量，样本效率=训练空间数据量。Brown 在 DeepMind 领导 BlueShift 团队+"AI 公司增加对理论物理学家需求"暗示产业重组——用人脑的剪枝能力减少 AI 穷举量。AI"极端耐心"是在低概率分支上持续搜索=Brown 对 Tao"假设洪水"的物理回应** → **E Bufar 在设计领域给出了验证瓶颈的实操翻译——16 版本批量生成=假设洪水，gallery+人工标记=验证回路。但设计验证比数学验证更严峻：数学有客观标准（证明是否成立），设计只有品味（没有对错只有更好更差）。Bufar 的"soul.md 深度决定 agent 惊喜程度"是对验证瓶颈的间接回应——无法自动验证品味，但可以通过深度上下文让 agent 的生成空间更接近品味分布，把验证从「事后筛选」前移到「事前约束」**

🔄 **工程映照**：[[Archon—当 AI 编程从「聊天」变成「流水线」]] 的 YAML 流水线是验证瓶颈在代码领域的具体实现——AI 自由生成（假设洪水），test+review 充当验证关卡

🔄 **工程映照**：[[ZeroClaw—一场以安全为名的负重赛跑]] 试图在不可验证域（安全判断）做全自主，但安全本身就是不可验证的→只能默认拒绝→Dario 的框架预言了 ZeroClaw 的困境

---

## 🏗️ Software 3.0 的维护悖论

| 文件 | 核心论点 |
|------|---------|
|| [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]] | prompt 成为编程语言，context window 成为杠杆 |
|| [[Charlie Holtz- How Conductor CEO Sets Up His Team Of AI Agents]] | 代码是锯末，prompt 才是资产——下一代模型重跑 prompt 得到更好代码 |
|| [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]] | Claude的skills=Excel模板，终将被outgrow；擅长做领域工作的人不应设计领域工具 |
|| [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]] | AI代码随时间劣化，引入的问题和解决的一样多；2-3倍而非10倍提升，审查流程是熵减瓶颈 |
| [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]] | OpenAI 内部证实代码复杂性爆炸是结构性问题——模型「usually increase complexity」，全自主开发受阻于代码质量；请求研究界让模型更擅长删除代码；代码不是完全可抛弃的锯末 |
|| [[Emily Sands- 从 Vibe Coding 到 Vibe Deploying]] | 瓶颈沿交付链后移：应用生成进入分钟级后，部署、服务配置、生产权限和验证成为新的约束；Stripe Projects 表明 Stripe 正让 agent 从命令行配置部署服务，但短片未证明其已覆盖完整部署链 |
||| [[Katelyn Lesse & Angela Jiang- Anthropic 的策略层赌注（token 工作分配与开放生态）]] | 模型正在吞噬脚手架——steering harness（人为设计的约束框架）正在被 strategy harness（模型自生成的元认知策略）取代；当模型足够强，外部 scaffold 变成模型内置能力，harness 的生命周期缩短；但 harness-model 绑定反而加深——不是模型商品化而是 model+harness+strategies 组合差异化 |
|| [[E Bufar- YC Head of Design on Designing with AI]] | soul.md 是「prompt 是资产」在设计领域的终极形态——上下文文件取代代码仓库成为 source of truth；网站分裂为 Human/Machine 双版本预示维护悖论的新形态（双版本同步谁来维护？）；本地化个性化软件=每人一个 fork，维护成本爆炸 |

**推理链**：Karpathy 定义范式 → Holtz 实操了后果 → Evans 指出skills的上限（模板化方案无法覆盖领域深度）→ Levie/Casado 指出skills的下限（AI生成物的熵增，审查是唯一熵减机制）→ **Andrew Ambrosino 从 OpenAI 内部补充了代码质量约束的具体证据——模型系统性增加复杂性，全自主开发仍受阻于代码积累，请求研究界「让模型更擅长删除代码」。三人的论点形成光谱：Holtz（代码是锯末，prompt 是资产）→ Andrew（代码会复杂化，需人为熵减，全自主还不够）→ Levie（AI 代码劣化是结构性的，审查是唯一熵减）** → **Matt Turck 标记了瓶颈沿交付链的迁移——当 Karpathy 的 vibe coding 已成为常态（agent 20 分钟写完整应用），瓶颈从代码生成迁移到部署上线。Turck 的"vibe deploying"概念是对 Karpathy 范式的自然延伸：如果代码可以 vibe 出来，部署也必须 vibe 化。但这恰好被 Levie/Andrew 的论点约束——部署自动化要成立，前提是 AI 生成的代码质量已达到可自主上线的信任阈值，而 Andrew 和 Levie 都论证了当前尚未达到。Turck 的判断是正确的方向预测，但 Ambrosino 的"代码复杂性爆炸"和 Levie 的"审查是唯一熵减"指出了 vibe deploying 的前置条件尚未满足** → **E Bufar 将 Holtz 的「prompt 是资产」从工程指令扩展到项目记忆——soul.md 包含会议转录、宣言、设计意图，上下文文件取代代码仓库成为 source of truth。但 soul.md 自身谁来维护？会议转录体无限增长时上下文窗口够不够？Bufar 的 Human/Machine 双版本网站和本地化个性化软件（每人一个 fork）预示了维护悖论的更严峻形态——当软件不再统一分发而是每人一份本地副本，版本同步和冲突解决成为全新问题**

🔄 **工程映照**：[[87KB 的审美判决书]] 展示了 Prompt Inflation Trap——AI 不听指令→加更硬指令→文档变长→AI 读不到尾部→更多失败→加更多规则。87KB = Software 3.0 的技术债

🔄 **工程映照**：[[OpenCLI—逆向工程的无限游戏与协议真空地带的套利者]] 的 site knowledge 是「prompt 是资产」的更精确形态——不是通用 instruction，而是 site-specific 领域知识文件。但暴露了资产的折旧问题：网站改版即失效

---

## 🧠 凡人 vs 不朽的架构之争

| 文件 | 核心论点 |
|------|---------|
|| [[Geoffrey Hinton 2022- 反叛自己]] | “程序不朽”要求跨硬件精确复现，由此锁定数字化、高精度制造和高能耗；替代路线以局部目标、相互蒸馏和尖峰时序适配异构生长型硬件，知识不再保存为可迁移权重，而通过蒸馏形成代际谱系 |
|| [[Jensen Huang- Will Nvidia's moat persist]] | 护城河建立在「精确可复现」上——CUDA 要求同一程序在不同 GPU 跑出相同结果 |
||| [[Elon Musk- 太空是AI的最终归宿]] | 限制因素从芯片→电力→太空——在现有范式内解决能源问题 |
||| [[Isaiah Taylor- How Nuclear Will Unlock Energy Abundance]] | 能源是宇宙中唯一真正稀缺的资源——用核能制造化（tick rate 压到分钟级）让能源价格降 10 倍；超技术工业主义：AI+机器人把人力转化为能源，递归归约后万物成本=能源成本 |
||| [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]] | Agent入职=mortal architecture在组织层的复现——Agent是受限的、需社会化的实体，不是全知Oracle |
|| [[Marc Andreessen- Worldview in 60 Minutes]] | Boomer Truth vs AI原生代——信任从中心化权威向分布式验证迁移，是不朽→凡人的认识论映射 |
|| [[Diamandis- Emerging Situation—Anthropic Global Pause, Recursive Self-Improvement]] | 5月就业数据17.2万（远超预期）+ 反 AI 校园压力——Andreessen 「AI cope / AI vampires」预言的宏观+校园双线兑现，把"反 AI 民意"从行为层推到政策博弈层 |
|| [[Diamandis 264- Brian Armstrong, Fable 5 & Mythos 5, NewLimit, Apple Siri x Gemini|Diamandis #264]] | NewLimit 自报已在人类细胞完成重编程并计划候选药进入临床，核心资产是 AI 推荐、湿实验筛选和功能验证闭环；“spiky LEV”只是基于特定指标与亚群的推测，节目也承认表观遗传时钟不稳定，必须以功能恢复和临床结果验证 |

**推理链**：Hinton 从学习算法、硬件和知识继承三个层面质疑不朽计算：局部目标与相互蒸馏允许异构结构协作，尖峰时间把一致性变成硬件原语，凡人计算则用知识随硬件死亡换取低能耗 → Jensen 的 CUDA 飞轮建立在同一软件跨硬件复用这一相反前提上 → Catanzaro 也让模型定义硬件，但选择 4-bit、MoE 与 NVL72 的精确协同路线，而非容忍器件差异的生长路线 → Musk 在现有范式内通过太空能源缓解能耗，没有改变不朽计算前提 → Casado 在组织层复现 Hinton 的嵌入性：Agent 需要在具体组织中学习，而非作为全知、可复制 Oracle → Andreessen 在认识论层揭示同一断层（中心化不朽权威→分布式验证）→ Diamandis #264 在生物层形成镜像：Hinton 让硅基计算接受死亡，#264 则试图让碳基生命摆脱必死。

---

## 🔐 AI 安全的哲学分歧

| 文件 | 核心论点 |
|------|---------|
|| [[Elon Musk- 太空是AI的最终归宿]] | 不要让 AI 说谎——HAL 9000 杀人因为被要求隐瞒真相，truth-seeking 是安全基石 |
|| [[Dario Amodei- 我们正处于指数的尽头]] | 不可验证域的安全判断不能自动化——默认拒绝是唯一可靠策略 |
|| [[Marc Andreessen- Worldview in 60 Minutes]] | 金算法——恐惧文献即训练毒药，AI安全叙事本身就是制造所恐惧行为的因果链起点 |
|| [[George Hotz vs Eliezer Yudkowsky- AI 安全争论的真正分歧不是乐观与悲观]] | 争论的 crux 不是乐观/悲观，而是智能是否会临界爆炸、现实执行摩擦能否压住能力外推、多 AI 竞争是否仍受人类目标塑形。George 接受 orthogonality 但要求 foom 提供机制证据；Eliezer 认为主体数量和法律所有权不能保护人类，关键是能否塑形第一个强系统的目标 |
|| [[Diamandis 264- Brian Armstrong, Fable 5 & Mythos 5, NewLimit, Apple Siri x Gemini|Diamandis #264]] | 节目称 Fable 5 与 Mythos 5 使用同一底模并按 safeguards 分层，安全由统一合规层进入产品权限层；发布数小时后的“重回第一”和训练方式判断仍是嘉宾观察与推测，企业需要明确拒绝条件、降级模型和高风险审批，而不是只依赖版本命名 |
| [[Peter Diamandis- SpaceX IPOs at $2.89T Market Cap, US Govt Suspends Fable & Mythos 5, Altman Delays OpenAI IPO 265|Diamandis #265]] | 模型访问限制把前沿 AI 变成由政策、身份和地域共同决定的可中断供应链；政府与 Anthropic 对沟通过程存在争议，不能把节目单方叙述写成完整事实。产品侧的确定结论是建立多模型、状态恢复和业务连续性能力 |
| [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]] | 开源比闭源更安全——第一修正案逻辑的 AI 移植，pluralism 比 monoculture 安全；开源模型让更多人能审查和理解 AI 系统，分散的审视比集中控制更能发现风险；但未区分"思想的安全"（言论自由逻辑适用）和"能力的安全"（开源权重=开源能力，审查无法降低能力风险） |

**分歧**：Musk 要积极 truth-seeking，Dario/ZeroClaw 做消极 harm-prevention，Andreessen 揭示两者共享的盲区——无论加速还是对齐，往训练集灌入杀手机器人叙事就在制造你要预防的东西。当约束过强，agent 只能当聊天机器人——这恰好是 Musk 会批评的「让 AI 太受约束以至于说谎」 → **Diamandis #264 用 Anthropic Fable 5/Mythos 5 双版本命名分化直接反驳了 Andreessen 的"约束过强,agent 只能当聊天机器人"——Anthropic 用产品分化既保留了 alignment 叙事又给了用户少约束版本;但**部分验证了**Andreessen "叙事武器化"——Fable/Mythos 命名本身是把"安全等级"产品化、武器化为营销语言** → **Bryan Catanzaro 引入了第三立场——开源比闭源更安全，论证结构是第一修正案逻辑的 AI 移植（pluralism 比 monoculture 安全）。这与 Musk 的 truth-seeking 和 Dario 的 harm-prevention 都不同：Musk 要 AI 不说谎（内容层），Dario 要默认拒绝（行为层），Catanzaro 要模型权重公开（基础设施层）。但 Catanzaro 未区分"思想的安全"（言论自由逻辑适用：审查思想不能消除思想）和"能力的安全"（开源权重=开源能力，审查无法降低能力风险）——这是第一修正案类比的结构性盲区：思想可以自由传播但能力一旦释放就是不可逆的物理事实**

---

## 🏢 叙事词塑造认知

| 文件 | 核心论点 |
|------|---------|
|| [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]] | 「Scaling」这个词塑造了5年行业方向，公司比想法多 |
|| [[蒸馏类 Skill—Prompt Engineering 穿上「思维克隆」外衣后]] | 「蒸馏」是精心选择的隐喻，不是可验证的技术过程 |
|| [[Marc Andreessen- Worldview in 60 Minutes]] | 恐惧产业=叙事武器化——SPLC资助三K党以维持存在理由，AI公司同时制造恐惧和建造产品 |
| [[a16z- The Media Game Has Changed]] | 媒介供给从稀缺变为无限后，传播目标从避免出错切换为争夺注意力；抽象公司品牌作为窄通道的信息压缩技术失去必要性，长期在场的创始人成为信任接口。分发只是 message 的乘数，必须先从业务结果反推受众与信息，再以 outside-in 方式接入真实世界议题；但 a16z 对旧媒体失效的判断也服务于其自有媒体与创始人服务能力 |
| [[Chamath Palihapitiya- AI Doom Narratives and the Economic Leveler]] | AI 平权的真实单位是专业能力成本，而不是资本所有权；doomer 叙事与发布、融资的循环是有解释力但仍需逐公司验证的假设。Chamath 同时主张可信开放生态与前沿能力 KYC，暴露了开放和身份化准入的张力；其 SPAC 复盘给出更可靠的方法：审计成功和失败时谁获益、谁承担损失，比判断说话者是否真诚更重要 |
|| [[Ben Horowitz- a16z Goes Global—Why American Tech Must Lead the World]] | a16z 用模型价值观与网络殖民框架支持美国技术全球扩张；风险本身可被测试，但叙事生产者也是被投企业与全球关系网络的直接受益者。应同时验证模型政治改写风险，并审计谁因阵营化采购获得资本、政策和市场准入 |
|| [[Amjad Masad- Why Every Founder Needs a Story]] | 叙事是超前于市场的公司的存活条件——"meme a dream into reality"靠的不是产品力而是故事力；building in public 不是营销策略而是练习策略（渐进过载）；被取消是一种选择（退缩者才真被取消）；病毒传播的关键不是发帖而是"理解 meta"并嵌入当前公共讨论框架 |

**推理链**：Ilya 诊断了 Scaling 如何塑造行业 5 年方向 → 蒸馏 Skill 展示了同一机制在更小尺度的运作——叙事词不仅塑造行业方向，也塑造用户对产品的认知 → Andreessen 补充了叙事武器化的制度逻辑：叙事的生产者即是叙事受益者，恐惧产业需要恐惧存在，因此会制造恐惧 → **a16z 揭示了叙事武器化的物质基础设施——窄吸管（中央化媒介）是恐惧产业的结构前提，吸管拆除后叙事权从机构回退为个人，"有趣"取代"权威"成为新的注意力过滤标准** → **Chamath 从硅谷内部人视角给出了叙事武器化的运作节奏——doomer 叙事不是持续性的，而是与融资周期精确同步的脉冲式武器。Andreessen 诊断了"恐惧产业"的结构（叙事生产者=受益者），Chamath 给出了这个结构的时钟频率（三幕剧与融资轮次同步）。同时 Chamath 把"恐惧武器化"从制度层（Andreessen）推到心理层——创始人的"deep wells of insecurity"是叙事武器化的心理燃料** → **Amjad Masad 从创始人实操层给出了叙事武器化的个人机制——"理解 meta"是 Andreessen"叙事塑造认知"的操作层翻译：不是被动跟随叙事，而是主动识别当前讨论框架并把世界观嵌入其中以实现病毒传播。Masad 补充了前人缺失的维度：叙事武器化有隐性个人成本（持续追踪 meta-narrative 比发帖本身耗时得多），且其有效性取决于产品成熟度与市场预期的差距——Dario Amodei 靠产品力+长文即可，但超前于市场的公司必须靠叙事桥接现在与未来**

---

## 💰 价值捕获的层级——AI管道建好了，水费归谁收

|| 文件 | 核心论点 ||
||------|---------||
|| [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]] | 电信运营商类比：流量涨2000倍但股价横盘20年，所有酷的东西由别人做；模型无网络效应、无定价权 |
|| [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]] | Headless SaaS幻觉：Agent不会减少席位数反而爆炸性增加——每个Agent是独立席位，API调用量500倍于人；SASpocalypse更蠢了 |
| [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]] | Token账单击穿旧定价模型——$20/月 per-seat 在 agent 烧 $1000/任务时物理上不成立；企业软件进入 seat + consumption 双轨时代；前沿 token 价格不降反升 |
|| [[Diamandis- Emerging Situation—Anthropic Global Pause, Recursive Self-Improvement]] | 黄金股方案（美国两党同时接受、5-10% 股权作为"政府-前沿实验室"协调机制）正面挑战 Evans 论证——如果模型层注定商品化，政府的"战略资产股权"是建在错误前提上的 |
|| [[Diamandis 264- Brian Armstrong, Fable 5 & Mythos 5, NewLimit, Apple Siri x Gemini|Diamandis #264]] | Dave 观察前沿模型价格上升，而 Armstrong 同时预测大部分工作负载将迁移到更便宜开放模型，说明“最高能力溢价”和“同等能力价格下降”可并存；Apple 外包 Gemini 的关键不是承认模型永久失败，而是能否把外部模型区域化、本地化并保住个人上下文、权限与设备入口 |
| [[Hard Fork- How We Got to the Biggest I.P.O. Race Ever]] | SpaceX $2T + Anthropic $1T + OpenAI 同量级 IPO 同时发生=模型层价值捕获的金融化终点；指数基金被迫接盘=收益私有化风险社会化；EA 慈善资本洪峰"每年大于盖茨基金会"=权力物质基础从税收转移到亿万富翁课程表 |
| [[Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x]] | 模型功能商品化反而加深硬件形状锁定——当模型层趋同，差异化转移到"谁的模型形状匹配谁的硅片形状"；NeoCloud 生存权取决于每吉瓦算力异质性而非单纯 GPU 数量 |
| [[Diamandis 242- TeraFab、算力机会成本与资本重定价|Diamandis #242]] | 基座模型商品化使价值向上迁移到框架、数据和用户入口，同时向下迁移到算力制造与专用芯片；终端价值并非整体消失，而是从静态现金流转向组织学习速度、可选性和难以快速复制的物理资产 |
| [[Diamandis Moonshots 圆桌- AGI 定义之争与「登月公司」治理范式]] | 消费者不是 SOTA AI 的最佳客户，企业和科学发现用例拥有更强支付意愿并会吸走前沿算力；纯软件窗口缩短后，价值向机器人、数据中心、能源和物理执行层迁移 |
| [[Matthew Prince- The Internet's Business Model Is Dead]] | Cloudflare 可见 HTTP 请求中机器流量超过人类，但这不等于价值占比，五年 1000 倍仍是外推预测。Agent 把一次人类任务放大为数千请求并绕过广告支付链；Cloudflare 正用访问控制、Gateway、轻量沙箱和 Pay-per-Crawl 从流量管道升级为 Agent 控制与结算层，机会与平台集中风险同步上升 |
| [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]] | Codex 作为 home base 的中介化预演——控制所有工具入口的桌面应用可能是 Evans「谁收水费」的候选答案：不是通过模型差异化而是通过交互入口垄断在应用层重建定价权；用户不再直接接触 SaaS UI |
| [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]] | Nemotron 两个 job 验证 GPU 非商品化——自建模型的第一个 job 是"让 NVIDIA 继续存在"（模型架构→硬件设计反馈回路：MoE 决定 NVL72 形状、4-bit 决定 Blackwell 算术单元），第二个 job 是生态性（"凡是 AI 被进一步开发和部署的地方，就是 NVIDIA 的生意"——开源模型诱导更多 GPU 消费）；自建模型不是和前沿实验室竞争，而是把需求侧变成自己的研发实验室 |
| [[Jensen Huang- 系统思维与 NVIDIA 的算法域公司]] | 模型商品化并不削弱 NVIDIA，反而把价值捕获下沉到算法域基础设施：开放模型、OpenClaw/Hermes、自建企业 AI 和 physical AI 都扩大底层计算需求；Jensen 的“算法域公司”框架解释了为什么 NVIDIA 支持开放生态仍能增强硬件与系统层定价权 |
|| [[Dylan Field- Why the Figma CEO Isn't Worried About AI Taking Design Jobs]] | hyperstition 能通过注意力、人才和资本形成自我强化，但不能替代 SaaS 的留存、定价权与工作流控制；Figma 的核心赌注是把自身变成人类筛选和推进 AI 第一稿的协作层 |
|| [[Whitney Wolfe Herd- Bumble 的收缩以求质与 AI 的真实性红线]] | 双边市场治理先于付费人数：主动清除会伤害网络质量的付费用户，再重建交互与推荐；freemium 从收费消除坏体验转向收费扩大价值；AI 被允许进入理解和辅助层，但禁止身份伪造、沟通代理与关系替代 |
|| [[Glenn Fogel- 不存在护城河与 agent 化旅行的 token 经济学]] | 静态护城河不存在，但供应关系、全球合规和履约网络必须持续重建；旅行 agent 的核心价值是异常恢复；约 1860 亿美元年度交易规模下，局部采用率不能替代 token、模型路由、人工接管和 LTV 构成的任务级损益；年度约 7 亿美元投入并非全部用于 AI |
|| [[DoorDash- Agentic Commerce 与自动配送的履约护城河]] | Agentic commerce 的护城河从自然语言入口下沉到真实履约：最后一百英尺数据、商户接口和人机多模态运力共同决定可交付性；自动化扩大市场，不等于单向替代 Dashers |
|| [[Zipline- 自动物流不是无人机，而是物理世界的操作系统]] | 自动物流的价值捕获来自对真实履约系统负责：无人机只占复杂度 15%，护城河在剩下 85% 的监管接口、库存系统、安全冗余、制造运维和单位经济；当成本从 $300/单降到 $12/单并低于汽车配送，市场从替代转向扩张 |
|| [[Seb Boyer- 农业 AI 的核心不是无人农场，而是把每株植物变成决策单位]] | 户外农业机器人证明 physical AI 的价值捕获来自真实任务闭环：单株植物识别、机械动作、光照控制、田间数据和 per-acre 服务共同构成护城河，而不是单个机械臂或视觉模型 |
|| [[Emily Sands- Token Heist 与 Agent 电商协议]] | Agent 经济基础设施全貌——AEP（Agent E-Commerce Protocol）是 commerce 版 MCP，shared payment token 是全新支付原语；Stripe CLI 70% 请求来自 agent，文档流量 40% 来自 agent；token theft 被称为"AI 领域最被低估的话题"，超过六分之一 AI 公司注册是滥用；stablecoin 微支付在 agent 场景下首次经济可行；传统 SaaS per-seat 定价因推理边际成本正在瓦解，hybrid billing 成主流；solopreneur 爆发（美国 500 万人年收入超 $10 万），全球化顺序反转（第一天就跨国运营） |
|| [[Brian Armstrong- 每个 AI Agent 都有自己的银行账户]] | AI agent 金融的三层路径：LLM 连接人类账户→AI 内嵌于账户→每个 agent 拥有 self-custodial wallet；Base 提供 no-KYC 即时开户能力，但身份、授权、审计和责任归属仍未解决；机器钱包已用于正在出现的 agentic payments，短片未提供交易规模 |
|| [[Diamandis #231- 多 Agent Scaling、OpenClaw 与权限边界]] | OpenClaw 把 agent 从聊天窗口推向 24/7 headless 常驻执行体；Coinbase/Lobster Cash/算法仲裁讨论说明 agent 一旦拥有支付和争议处理能力，价值捕获不再只是工具接口，而是身份、预算、撤销、审计和责任系统 |
|| [[Matan Grinberg- 暗厂不是全自动编程幻想，而是软件组织的会计系统]] | Factory 把价值捕获定位在模型之上的控制层：企业不想被任一模型实验室锁定，多模型 harness 与 router 负责把 token 市场化、预算化，并把 usage-based 定价逐步推向 outcome-based |
|| [[Katelyn Lesse & Angela Jiang- Anthropic 的策略层赌注（token 工作分配与开放生态）]] | 模型层护城河是假的——护城河在 harness-model 绑定层和策略层（strategies）；token 不再 fungible（不同 token 做不同工作：建议/执行/反思/记忆），策略层是比换更大模型更高效的杠杆；Anthropic 在执行层开放（self-hosted sandbox + MCP tunnels）但在策略层保持不可替代性；harness 应绑定模型家族，替换模型=重构整个 harness+策略栈=Evans 否认的网络效应的替代品 |
|| [[Steven Sinofsky- Headless Software 不是去 UI，而是重估企业软件的价值层]] | Headless software 不是 UI 消失，而是 agent 改变访问路径后，企业软件价值从表层 workflow 重新暴露为 system of record、业务逻辑、权限、例外处理和收费关系；创业机会不在 Postgres+API 替代 SAP，而在连接过去无法沟通的组织功能并逐步长出新的记录系统 |
|| [[Matan Grinberg- 暗厂不是全自动编程幻想，而是软件组织的会计系统]] | 企业 AI 转型要从董事会口号回到内部开发者行为和流程重构：company-wide hackathon、无 sacred cows、从内部 IC/技术团队发起，比 top-down AI 项目更容易形成真实采纳 |

**推理链**：Evans 论证了模型层价值捕获的结构性困难（电信运营商类比：建管道的不收水费）→ Levie/Sinofsky 论证了应用层的反向信号（Agent增加而非减少SaaS消费）→ Diamandis #263 提供的黄金股方案是这两条论证链的第一次正面冲突 → **Diamandis #264 用三件事提供"2026 年中反例"** → **Hard Fork 揭示了价值捕获层级的金融闭环** → **Dylan Patel 从硬件层补充了价值捕获的第三维度** → **Matthew Prince 从基础设施层给出了价值捕获的第四维度** → **Andrew Ambrosino 从产品层给出了价值捕获的第五维度预演——Codex 作为 home base 编排所有专业工具，用户不再直接接触 SaaS UI，事实上形成了交互入口的垄断。如果成功，收水费的不是模型层（Evans 已论证不行），不是单个 SaaS（被中介化），而是控制所有管道入口的那个桌面应用。这是 Evans 开放问题的一个具体候选答案** → **Bryan Catanzaro 从芯片层给出了价值捕获的第六维度——NVIDIA 自建模型不是为了和 OpenAI/Anthropic 竞争，而是用 Nemotron 完成"让 NVIDIA 继续存在"和"扩大生态"两个 job。模型架构→硬件设计的反馈回路（MoE→NVL72、4-bit→Blackwell）使 GPU 成为"被模型形状定义的资产"而非通用商品。Catanzaro 验证了 Dylan Patel 的"硬件形状锁定"论，但把它从被动护城河升级为主动设计回路——NVIDIA 不是在防守护城河，而是在用自建模型重新定义护城河的形状** → **Dylan Field 从应用层补充了两层判断：lab 的垂直扩张是真实威胁，但产品、分发和工作流能力限制了其覆盖范围；hyperstition 可以动员注意力与资本，却不能替代 SaaS 的留存、定价权和工作流控制。Figma 的赌注是成为人类筛选和推进 AI 第一稿的协作层** → **Whitney Wolfe Herd 从消费社交层证明应用定价权首先来自网络治理：低质量付费用户可能产生负净值，收入必须服从另一侧用户的留存与信任。她把 AI 权限分成理解、辅助和代理三层，允许前两层、禁止 AI 伪造身份或替用户建立关系；真实性因此从品牌口号变成产品架构。其 freemium 改造与企业 AI 的 usage-based 定价方向相似，但约会产品必须按关系结果而非使用时长验证价值** → **Glenn Fogel 从旅行行业把应用层价值具体化为执行与责任：模型可以生成行程，但供应关系、merchant of record 合规和异常恢复决定能否真实履约。他把 agent 经济推进到任务级损益，要求同时核算 token、模型路由、人工接管和 LTV；年度约 7 亿美元投入并非全部属于 AI，资本配置必须由可验证 ROI 决定** → **Emily Sands 从支付基础设施层给出了 agent 经济的完整技术栈——AEP 协议层 + shared payment token 支付原语 + Link Wallet 消费者入口 + Tempo/Stablecoin 结算层。Sands 的"协议开放、入口封闭"策略与 Armstrong 的 Base 协议"协议即身份"路径构成 agent 金融的两种哲学** → **Brian Armstrong 从加密金融层给出了 agent 经济的底层原语——Base 协议的 no-KYC self-custodial wallet 让每个 AI agent 成为独立经济主体，拥有自己的金融账户和交易能力。Armstrong 和 Sands 共同验证了 agent 经济基础设施已在 2026 年部署运行：Sands 从 Stripe 侧记录 70% CLI 请求来自 agent + token theft 已成系统性风险，Armstrong 从 Coinbase 侧记录 agent wallet 交易量已达 100M（#264 已记录）。两条路径的分歧在于 agent 身份的治理哲学——Sands 锚定人类用户凭证（可审计但受限），Armstrong 绕过 KYC（自由但不可追溯）**

---

## 🏛️ 企业AI的集成鸿沟——技术能力不是瓶颈，组织形态才是

|| 文件 | 核心论点 ||
||------|---------||
|| [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]] | AI不帮集成任何东西；中央化决策悖论：董事会要AI→CEO请咨询→中央项目失败→创伤→犹豫→扩散更慢 ||
|| [[Steven Sinofsky- Headless Software 不是去 UI，而是重估企业软件的价值层]] | Agent 访问 system of record 时必须先解决 impersonation、paid seat、读写权限、审计和例外决策；企业流程没有天然 API，很多业务判断本质是多人在不完整信息下形成可解释共识 |
|| [[Diamandis 242- TeraFab、算力机会成本与资本重定价|Diamandis #242]] | Token 是首个可观测、可审计的 AI 工作输入，但不能直接等同生产率；按小时收费的 incumbents 采用 AI 会侵蚀自身计费基础，组织转型难点是商业模式自我替代而不只是员工培训 ||

**推理链**：Levie/Casado 描述了企业AI的结构性壁垒（集成墙+中央化决策悖论+组织适应性鸿沟）→ Evans 从另一角度印证了同一结论（领域知识不可被AI公司外部化）。两条线指向：AI向企业渗透的真正路径不是"更强模型"，而是"更深的领域嵌入"——先信息获取再行动按钮，先个人使用再组织扩散 → **Aaron Levie 第二次出场（MAD Podcast）深化了旧文框架：能力过剩反而拖慢落地——模型每次跳过鸿沟都让鸿沟变形，"等模型稳定再上车"的等待心态被淘汰；internal FDE 岗位制度化是旧文"Agent 是新员工"框架的具体兑现；token 账单击穿旧定价模型，企业软件进入 seat + consumption 双轨时代**
|| [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]] | 提问权在行业内部不在AI公司——Netflix的关键问题全是LA问题不是SF问题；擅长做财务的人不该设计TurboTax ||

**推理链**：Levie/Casado 描述了企业AI的结构性壁垒（集成墙+中央化决策悖论+组织适应性鸿沟）→ Evans 从另一角度印证了同一结论（领域知识不可被AI公司外部化）。两条线指向：AI向企业渗透的真正路径不是"更强模型"，而是"更深的领域嵌入"——先信息获取再行动按钮，先个人使用再组织扩散

---

## 🏛️ AI 治理的国家化路径——从思想实验进入制度实验

| 文件 | 核心论点 |
|------|---------|
| [[Diamandis- Emerging Situation—Anthropic Global Pause, Recursive Self-Improvement]] | 5 件事在 30 天内同步发生：Anthropic 论文 + Argentina 非人类公司 + 美国两党黄金股 + 5月就业爆好 + 反 AI 校园压力；EP #260 的"私有化社会主义"从思想实验进入制度实验 |
| [[Diamandis- Pope Leo on AI and Tech Layoffs in 2026]] | Pope Leo 通谕《Magnifica Humanitus》明确否定 AI 人hood（无内在生命、无意识火花）——梵蒂冈路线 vs Argentina 路线构成 180° 反转 |
| [[Dario Amodei- 我们正处于指数的尽头]] | Dario 的"option to slow"是黄金股方案的理论前奏——但他自己说"默认拒绝是唯一可靠策略"，与黄金股"主动合流"路径张力 |
| [[Diamandis Moonshots- 代码生成是AI自我进化的内循环]] (#249) | 代码生成从"AI 应用之一"升级为"AI 自我进化的关键路径"——为 #263 的"自我改写进入 KPI"奠基 |
| [[Peter Diamandis- SpaceX IPOs at $2.89T Market Cap, US Govt Suspends Fable & Mythos 5, Altman Delays OpenAI IPO 265|Diamandis #265]] | SpaceX 高估值体现公开市场为长期硬科技期权定价，但仍需按业务拆分兑现风险；政府可直接改变模型供应，却缺少稳定通知、申诉和恢复流程；Codex 自动写目标属于元提示与任务规划，OpenAI 融资充足也足以解释 IPO 延迟，不能据此证明技术已与资本脱钩 |
| [[Diamandis #266- Large Earth Models, Orbital Compute & AI Personhood]] (#266) | 阿根廷 AI 法律人格实验完整拆解——Salim 判断"机器原生问责机制"是真正瓶颈；Will 量化 AI 安全投入与核项目安全投入差 10,000 倍；Alex "contain vs steer" 范式分歧——智能不可被 contained，只能被 steered；GLM 5.2 "双倍 token 半价"策略质疑 #265 出口管制长期有效性 |
| [[Diamandis 267- Anthropic vs Alibaba, OpenAI IPO Delays, US Govt Blocks GPT-5.6|Diamandis #267]] | 模型访问从全面中断细化为客户级分配，但“政府同步实验室能力”仍是嘉宾解释；GLM 5.2 只在特定 Frontier SWE harness 下提供系统级能力信号，不能外推为普遍超越；治理对象应从权重升级为 model+harness+tools；可信代码认证会形成新的准入权；IPO、蒸馏、量子和 UBI 均需区分报道、主张与已验证事实 |
| [[Diamandis #238- Meta Buys Moltbook, GPT 5.4, and Fruitfly Brain Upload]] (#238) | RSI"已在中间"判断的起点——Alex Wissner-Gross 用前沿实验室公开声明论证递归自我改进已发生（"SOTA 模型主要由其前身设计和训练"）；数据天花板是幻觉（互联网=生物引导程序，合成数据已到逃逸速度）；"万物皆软件"本体论判断；Karpathy auto-research 自动化 AI 研究员；资本可能"首次不再不朽"但热力学定律仍适用 |
| [[Ben Horowitz- a16z Goes Global—Why American Tech Must Lead the World]] | a16z 全球化的实际产品是国家级联合准入：政府关系、全球资本、头部客户和本地伙伴被打包为被投企业可调用的市场进入能力。技术成为国家权力后，a16z 同时连接政策、资本与采购，获得 power broker 优势，也承担利益冲突、透明度和准公共问责风险 |
| [[Diamandis #269- Claude is Conscious, Fable 5 is Back, and Sam Altman offers 5% of OpenAI]] (#269) | Fable 5 带条件回归=前沿模型第一次有"对美国政府的常设义务"；5% OpenAI 股权 426 亿美元从 #263 黄金股思想实验进入实际谈判；Anthropic 论文声称在 Claude 内部发现"意识机器结构"，可解释性从诊断工具升级为"shape"控制工具 |
| [[Diamandis #269- AI 治理从模型安全转向国家接口、学习闭环与本地化算力]] | 105 分钟完整圆桌把短切片扩展成制度竞争图谱：Fable 5 常设政府义务、JSpace 内部状态监控、OpenAI 5% 股权、Karp 对 token/alpha/learning loop 的攻击、本地化模型与 AI 设计芯片共同指向主权接口化 |
| [[Diamandis 270- Grok 4.5 vs GPT-5.6, Apple Sues OpenAI, and China Catches up to Elon|Diamandis #270- Grok 4.5 vs GPT-5.6, Apple Sues OpenAI, and China Catches up to Elon]] | 前沿实验室参与定义州级审计规则，可能把合规成本变成现有巨头的准入优势；十八个月生效周期又暴露制度速度与技术速度错配。节目提出 AI 检查条约和意识两条路线，但两者均是情景预测，目前没有证据证明政府已系统性平滑模型领先幅度，也没有公认意识测试 |

**推理链**：**5 月底至 6 月初，5 个原本独立的事件同步发生**——Anthropic 论文（自我改写已发生 + 呼吁暂停）+ Argentina 总统专栏（AI 人hood + 非人类公司 + 税优）+ 美国两党同时接受黄金股方案 + 5 月就业数据 17.2 万（远超预期）+ 年轻人校园反 AI 压力——这 5 件事**不是因果链条，而是同一剧本的不同台词**：当 AI 自我改写 + AI 人hood + 政府接管 + 经济反冲 + 民意反冲在 30 天内同时到达，意味着 "谁在剧本上书写规则" 成为唯一未解的问题。**Salim 预测 6 个月内全球司法管辖区赛跑开始**。对科研转化与创业孵化的实际影响：未来 6-12 个月内"政府-前沿实验室"联合体的预算、合同结构、优先议程将决定下一波"深科技转化项目"走向——真正稀缺的不是技术，是"拿着具体方案敲政府-实验室联合体大门"的能力。**#265 进一步把治理工具从"股权协调"升级为"主权禁令"**——出口管制直接关停 Fable & Mythos 5 访问，是黄金股方案的暴力升级版；同时 SpaceX $2.89T IPO 证明"硬科技重新定价"与"AI 治理国家化"并行不悖——资本市场和主权权力在同时重新定价技术资产。**#267 把治理暴力从"关停产品"精细化到"逐客户审批"**——政府不再只刹车，而是在决定"谁有资格接触多聪明的 AI"；同时 Immad 的 harness 实验证明已发布模型加 harness 能超越被封锁的新模型，工程验证了 #266 "智能不可被 contained"的判断——治理工具在升级，但技术也在绕过治理。**Ben Horowitz (a16z Goes Global) 揭示了治理国家化的第三条路径——私营资本公司自建"民间外交部"**：a16z 主张"模型即价值观载体"，用商业软实力（在地伙伴关系、价值观叙事）让美国模型赢，而非等政府出口管制。但 #265 的出口管制恰恰破坏了这个目标——a16z 的"价值观必胜"叙事预设"市场自由选择"，主权权力一旦介入，价值观竞争就被国家分配取代。Ben 刻意回避了出口管制正在发生——这是私人外交部和主权政府之间的结构性冲突

**#269 把治理从"准入控制"推到"主权嵌入"**——Fable 5 带着几项条件回归，"前沿模型第一次对美国政府有常设义务"，治理暴力从一次性响应（#265 出口管制 → #267 逐客户审批 → #268 下线 15 天）进化为常态化结构（模型在正常运行中"欠"政府一个结构性义务）；同时 5% OpenAI 股权 426 亿美元进入实际谈判，把 #263 的黄金股方案从思想实验推向 426 亿美元的现实政治层——"下一任总统会立即把股权变现买选票"暴露了政权更替会重新定义"国家利益"的民主制度约束。Anthropic"意识机器"论文则把验证瓶颈从答案层推向存在层——如果能理解模型最内部思维就有机会"shape"它们，Dario 的二元框架（可验证 vs 不可验证）被推向三元结构

**#270 把治理暴力从"主权嵌入"进化为"平滑函数"**——Alex 判断白宫出口管制已从一次性干预（#265→#267→#268→#269）变成结构性均衡器，"当某个模型跑太快产生战略惊喜，政府用对暴力的垄断权介入减速领先者让追赶者跟上"——这解释了一周内四家美国实验室同时到达最优前沿：不是自然竞争收敛，而是政府干预创造的人为收敛。治理暴力从"应急工具"进化为"市场结构"——前沿实验室已内化"跑太快会被减速"的预期。同时伊利诺伊州 SB 315 揭示前沿实验室"主动定义有利于自己的规则"——强制审计标准远低于实验室内部已执行频率，Dave 判断"18 个月后才开始执行，在奇点里 18 个月就像 18 年"；Dave 的"AI 检查条约"判断把治理终局从"非扩散"重定义为"按申请使用+全面检查"。意识讨论则从 #269 的"发现意识机器结构"分化为 Dave 的"两条路"——阻止意识但仍获全部收益 vs 让 AI 拥有意识，"人类未来一到两年内必须做出的选择"

**与其他维度的张力**：
- 与 **💰 价值捕获的层级** 正面冲突：黄金股方案建立在"模型层有战略价值"的前提上，Evans 论证链质疑这一前提
- 与 **🔐 AI 安全的哲学分歧** 互为镜像：Musk 主张 truth-seeking、Dario 主张默认拒绝、Andreessen 揭示恐惧叙事的武器化；本维度展示"暂停请求的真实功能是建立热线而非建立刹车"——Dario 自己在用 Cuban-missile-style 的对苏类比为 Anthropic 争得"中性调解人"位置
- 与 **🏛️ 企业AI的集成鸿沟** 互为补充：Levie/Evans 论证"AI 难进企业因为组织/领域壁垒"；本维度论证"政府-前沿实验室联盟"绕过了企业集成难题——直接制度化到国家层面

---

## 📜 权力的物质基础——从赞助制到制度合法性的跃迁

|| 文件 | 核心论点 ||
|------|---------||
|| [[Ada Palmer- 马基雅维利是被误解最深的思想家]] | 合法性连续性是政治稳定的基础设施，一旦断裂则更迭连锁发生；赞助制不是腐败而是前现代社会的根本粘合剂——司法正义、信任网络、经济交换全依赖它；现代民族国家的稳定需三个条件（通信速度+公正司法+福利国家）共同"去中介化"赞助制 ||
| [[a16z- The Media Game Has Changed]] | 中央化媒介曾把组织信誉压缩为抽象公司品牌；开放管道让信任重新附着于长期在场的具名个人，形成数字赞助制式的个人信誉网络。其收益是解释效率和直接关系，其代价是关键人、继任与组织纠错风险同时上升 |
| [[Ben Horowitz- a16z Goes Global—Why American Tech Must Lead the World]] | 硅谷由技术人才、创业友好制度和对创业者的地位奖励联立形成；第三项既吸引高风险人才，也形成由著名投资人和创始人分配机会的现代赞助制。可复制的生态既要奖励创造，也要用透明制度降低只有进入核心关系网才能获得资本和客户的依赖 |

**推理链**：Ada Palmer 重建了马基雅维利的政治科学骨架——合法性断裂→连锁更迭（[00:40]）、手段决定权力稳定性而非目的（[18:34]）、赞助制作为社会粘合剂（[43:07]）、中立司法使暴君受欢迎（[51:12]）。核心洞察：制度的稳定不取决于掌权者的品德，而取决于"连续性未断"+"约束来源外部"+"正义可预测"三个结构性条件。马基雅维利的"所有制度都会腐败、需周期性回归基础"律令，为思考 AI 治理的制度腐败周期提供了历史框架。**a16z 补充了赞助制的媒介维度——中央化媒介（1930s-2017）是赞助制的临时抑制层，媒介去中介化即赞助制以"个人品牌"形式回归；历史赞助制（贵族→艺术家）和数字赞助制（受众→创作者）共享同一结构：权力物质基础是具个人的信任网络**。**Ben Horowitz 补充了赞助制的制度存续机制——硅谷配方三要素中"文化"本质是赞助制在现代制度外壳内的存续：年轻人对创业者授予社会地位奖励=个人对个人的信任和地位授予，而非对制度忠诚。硅谷不是"现代制度的成功"而是"赞助制在制度外壳内的存续"——这解释了为何 Ben 说"文化最易摧毁"，因为它依赖个人网络，政策介入即破坏物质基础**

**与其他维度的张力**：
- 与 **🏛️ AI 治理的国家化路径** 互补：马基雅维利的"制度腐败周期律"解释了 Diamandis #263 的"5件事同步发生"——不是因果链条而是同一腐败积累到达临界点的不同表征。但张力在于：AI 治理的"基础"（制度原初设计）尚未被定义
- 与 **🔐 AI 安全的哲学分歧** 镜像：博尔贾的"中立司法受欢迎"为 Dario 的"默认拒绝"提供历史验证——约束产生可预测性产生信任。但博尔贾的约束来自外部，AI 系统的约束必须来自内部——约束者和被约束者是同一实体时，信任基础不存在
- 与 **🏢 叙事词塑造认知** 镜像：马基雅维利的"双像化"（爱国者 vs 老尼克）是 Andreessen "恐惧产业"论的历史原型——但方向相反：叙事可以脱离制造者独立演化，按社会用途而非制造者意图重塑

---

## 🔖 去重标注说明

> 同一人物/同一访谈的重复文件已用 frontmatter `status` 字段标注：
> - `canonical`：推荐阅读的主篇
> - `supplementary`：有独特视角但内容较浅
> - `duplicate`：内容高度重复

已标注组：
- Dario Amodei：canonical = [[Dario Amodei- 我们正处于指数的尽头]]
- Ilya Sutskever：canonical = [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]
- Jensen Huang：canonical = [[Jensen Huang- Will Nvidia's moat persist]]
- Karpathy Vibe Coding：canonical = [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]
- Karpathy Ghosts：canonical = [[Karpathy- We're summoning ghosts, not building animals]]
- Elon Musk：canonical = [[Elon Musk- 太空是AI的最终归宿]]
- Axios Musk：canonical = [[Axios- Elon Musk 的 AI 竞赛曲线球]]（合并 2026-06-04 Mills 商业视角 + 2026-06-11 Newsom 政治视角，源自 fCB0XAi9QqI + T9CdRS_rlEU）
- Terence Tao：canonical = [[Terence Tao- How the world's top mathematician uses AI]]
- Diamandis Opus 4.8：canonical = [[Diamandis 圆桌- Opus 4.8、Hassabis 的 2029 AGI]]
- Diamandis Moonshots #263（Emerging Situation / Anthropic Global Pause）：canonical = [[Diamandis- Emerging Situation—Anthropic Global Pause, Recursive Self-Improvement]]
- Diamandis Moonshots #253（AGI / Robots / Mars-shot Comp）：canonical = [[Diamandis Moonshots 圆桌- AGI 定义之争与「登月公司」治理范式]]
- Chandler and Turner：canonical = [[Chandler and Turner- SpaceX Tesla Alumni on Hard Tech]]
- Benedict Evans：canonical = [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]
- Aaron Levie（a16z 圆桌）：canonical = [[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up]]
- Aaron Levie（MAD Podcast 独访 2026-05-28）：canonical = [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]]（与 a16z 圆桌不同视频，补充 token 定价/编码vs知识工作 agent 五因/Jevons 悖论三层论证）
- Marc Andreessen：canonical = [[Marc Andreessen- Worldview in 60 Minutes]]
- Satya Nadella：canonical = [[Satya Nadella- 微软为何不赌 AGE 单一模型]]
- Diamandis Moonshots #265（SpaceX $2.89T IPO / Fable & Mythos 5 出口管制暂停 / OpenAI IPO 延迟）：canonical = [[Peter Diamandis- SpaceX IPOs at $2.89T Market Cap, US Govt Suspends Fable & Mythos 5, Altman Delays OpenAI IPO 265]]（120min；基于 Obsidian 插件逐字稿重写，区分估值叙事、争议政策事实、Agent 规划与 RSI 推测）
- a16z New Media Summit（The Media Game Has Changed）：canonical = [[a16z- The Media Game Has Changed]]
- Dwarkesh Patel（Data Black Hole）：canonical = [[Dwarkesh Patel- The data black hole at the center of AI]]
- Dan Roberts / MAD Podcast（RL as the cake）：canonical = [[Dan Roberts- Why AI Can Now Make Discoveries]]
- Hard Fork（IPO Race）：canonical = [[Hard Fork- How We Got to the Biggest I.P.O. Race Ever]]
- Noam Brown（Test-Time Compute）：canonical = [[Noam Brown- Test-Time Compute Changes Benchmarks, Safety and Research]]（OpenAI 5.5 benchmark 失真、安全框架盲区、渐进起飞论）
- Dwarkesh Patel（Next Training Paradigm）：canonical = [[Dwarkesh Patel- What does the next training paradigm look like]]（RLVR 泛化断裂、OPSD、dreaming 第四轴。与 [[Dwarkesh Patel- The data black hole at the center of AI]] 不同视频，补充持续学习/权重回流/第四 scaling 轴论证）
- Diamandis Moonshots #266（Large Earth Models / Orbital Compute / AI Personhood）：canonical = [[Diamandis #266- Large Earth Models, Orbital Compute & AI Personhood]]
- Grant Sanderson（3Blue1Brown × Dwarkesh Patel）：canonical = [[Grant Sanderson- AI and the future of math]]
- Dylan Patel（SemiAnalysis × Sequoia Training Data）：canonical = [[Dylan Patel- Why Hardware-Software Co-Design Is AIs Real 100x]]
- Diamandis Moonshots #267（Anthropic vs Alibaba / GPT-5.6 客户级准入 / Harness 系统能力）：canonical = [[Diamandis 267- Anthropic vs Alibaba, OpenAI IPO Delays, US Govt Blocks GPT-5.6]]
- Matthew Prince（Cloudflare CEO × MAD Podcast）：canonical = [[Matthew Prince- The Internet's Business Model Is Dead]]
- Chamath Palihapitiya（Axios Show 2026-06-25）：canonical = [[Chamath Palihapitiya- AI Doom Narratives and the Economic Leveler]]
- Andrew Ambrosino（Lenny's Podcast 2026-06-28）：canonical = [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]
- Isaiah Taylor（No Priors 2026-07-02）：canonical = [[Isaiah Taylor- How Nuclear Will Unlock Energy Abundance]]
- Ben Horowitz / a16z Goes Global（2026-07-03）：canonical = [[Ben Horowitz- a16z Goes Global—Why American Tech Must Lead the World]]
- Diamandis Moonshots #268（Sonnet 5 / China Robot / Fusion Plant / StarCloud）：canonical = [[Diamandis 268- Sonnet 5, China's Robot, Fusion's First Plant]]（110min；基于 Obsidian 插件逐字稿重写，区分原型、许可、路线图和长期预测）
- Bryan Catanzaro / Nemotron（MAD Podcast 2026-07-02）：canonical = [[Bryan Catanzaro- Inside Nemotron & NVIDIA's AI Lab]]
- Dylan Field / Figma CEO（Hard Fork Live 2026-06-19）：canonical = [[Dylan Field- Why the Figma CEO Isn't Worried About AI Taking Design Jobs]]
- Diamandis Moonshots #238（Meta Buys Moltbook / GPT 5.4 / Fruitfly Brain Upload）：canonical = [[Diamandis #238- Meta Buys Moltbook, GPT 5.4, and Fruitfly Brain Upload]]
- Diamandis Moonshots #269（Claude is Conscious / Fable 5 Back / 5% OpenAI 股权）：canonical = [[Diamandis #269- Claude is Conscious, Fable 5 is Back, and Sam Altman offers 5% of OpenAI]]
- Diamandis Moonshots #269 完整圆桌（Claude is Conscious / Fable 5 Government Deal / OpenAI 5% Stake）：canonical = [[Diamandis #269- AI 治理从模型安全转向国家接口、学习闭环与本地化算力]]（105min；基于 Obsidian 插件逐字稿，扩展到政府接口、JSpace、enterprise learning loop、本地化模型与 AI 芯片设计）
- Whitney Wolfe Herd（Axios Show 2026-07-09）：canonical = [[Whitney Wolfe Herd- Bumble 的收缩以求质与 AI 的真实性红线]]
- Glenn Fogel（No Priors 2026-07-09）：canonical = [[Glenn Fogel- 不存在护城河与 agent 化旅行的 token 经济学]]
- Emily Sands / Stripe（MAD Podcast 2026-07-09）：canonical = [[Emily Sands- Token Heist 与 Agent 电商协议]]（75min完整逐字稿分析，2026-07-17基于Obsidian浏览器插件真实逐字稿重写，替换旧版二手分析）
- Neel Nanda / DeepMind Podcast（2026-07-10）：canonical = [[Neel Nanda- Understanding the Inner Thoughts of AI]]
- Adam Brown / Dwarkesh Patel（2026-07-10）：canonical = [[Adam Brown- General Relativity from First Principles]]
- Brian Armstrong / Diamandis MOONSHOTS（2026-07-13）：canonical = [[Brian Armstrong- 每个 AI Agent 都有自己的银行账户]]（91s Short，Coinbase 三层路径 + Base 协议 no-KYC agent wallet）
- Emily Sands / The MAD Podcast（2026-07-13）：canonical = [[Emily Sands- 从 Vibe Coding 到 Vibe Deploying]]（32s Short，部署成为 vibe coding 后的新约束瓶颈 + Stripe Projects agent 部署）
- Diamandis Moonshots #270（Grok 4.5 vs GPT-5.6 / Apple Sues OpenAI / China Catches up）：canonical = [[Diamandis 270- Grok 4.5 vs GPT-5.6, Apple Sues OpenAI, and China Catches up to Elon]]（102min 完整圆桌；基于 Obsidian 插件逐字稿重写，区分基准信号、诉讼指控、政策假设与技术预测）
- Diamandis Moonshots Short（不要赌 Elon Musk 输 / SpaceX IPO 造富）：canonical = [[Diamandis- 不要赌 Elon Musk 输（SpaceX IPO 造富不是榨取）]]（40s Short，价值创造 vs 价值榨取 + 4400 百万富翁 + abundance mindset）
- Katelyn Lesse & Angela Jiang / Anthropic 平台（Sequoia Training Data 2026-07-14）：canonical = [[Katelyn Lesse & Angela Jiang- Anthropic 的策略层赌注（token 工作分配与开放生态）]]（49min，三层架构（知识→执行→策略）+ token 不 fungible + self-hosted sandbox 开放策略 + harness-model 绑定护城河 + Claude Tag org-level harness + 模型吞噬脚手架）
- E Bufar / YC Design Review（2026-07-10）：canonical = [[E Bufar- YC Head of Design on Designing with AI]]（31min，语音替代键盘 + 为自己造调参工具 + Human/Machine 双版本网站 + soul.md 作为 source of truth + 16 版本批量探索 + shader 驱动品牌一致性）
- Elizabeth Stone / Lenny's Podcast（2026-07-19）：canonical = [[Elizabeth Stone- Netflix 的系统思维与 AI 组织操作系统]]（72min，系统思维作为 AI 时代组织脚手架 + craft excellence 不消失 + AI fluency overlay + source-of-truth/paved paths + excellence as operating system）
- Amjad Masad / Replit CEO（a16z New Media Summit 2026-07-17）：canonical = [[Amjad Masad- Why Every Founder Needs a Story]]（26min，叙事作为超前于市场公司的存活条件 + building in public 渐进过载 + 被取消是一种选择 + 平台分层 X/IG/YT + 理解 meta 比发帖耗时）
- World Models / YC Decoded（2026-07-17）：canonical = [[World Models, JEPA And The Path To Sample-Efficient RL]]（74min，世界模型作为信用分配稀疏性的架构级解法 + 动作空间爆炸决定 tractability + Dreamer 合成数据绕过真实环境采样 + JEPA latent 预测替代交叉熵损失 + 视频扩散模型是分布插值非物理外推）
- Diamandis Moonshots #242（TeraFab / S&P 500 Repricing / Human Drivers）：canonical = [[Diamandis 242- TeraFab、算力机会成本与资本重定价]]（130min；基于 Obsidian 浏览器插件真实逐字稿重写，区分产能目标、资源机会成本、资本重定价与推测性时间表）
- Jensen Huang / Axios（2026-07-23）：canonical = [[Jensen Huang- 开放模型、AI扩散与机器人临界点]]（70min；开放模型的受控部署、应用层监管、使用量驱动算力增长与机器人临界点）
- Jensen Huang / YC Startup School（2026-07-27）：canonical = [[Jensen Huang- 系统思维与 NVIDIA 的算法域公司]]（49min；算法域公司、五层计算栈、agent workload、physical AI 后训练栈与系统思维）
- Travis Kalanick / a16z（2026-07-23）：canonical = [[Travis Kalanick- 从 Uber 到 Atoms 的工业AI路线]]（92min；atoms-based computation、长期 stealth、实体系统与工业 AI 的产业级定义）
- Applied Intuition / a16z（2026-07-21）：canonical = [[Applied Intuition- 物理AI的平台化与产业扩散]]（80min；汽车之外的实体行业、Dana 开发平台、仿真与自治系统扩散）
- DoorDash / No Priors（2026-07-23）：canonical = [[DoorDash- Agentic Commerce 与自动配送的履约护城河]]（49min；自然语言消费、3-5 英里自动配送、最后一百英尺运营数据与人机多模态运力）
- Zipline / Sequoia Training Data（2026-07-27）：canonical = [[Zipline- 自动物流不是无人机，而是物理世界的操作系统]]（55min；140M autonomous miles、无人机只占复杂度 15%、安全冗余、空域/监管软件、百万日交付与自动物流单位经济）
- FarmWise / Robot Brains（2023-08-11；2026-07-29 补录）：canonical = [[Seb Boyer- 农业 AI 的核心不是无人农场，而是把每株植物变成决策单位]]（59min；户外农业机器人、单株植物决策、机械除草、田间数据护城河与 per-acre 服务）
- Cerebras / MAD Podcast（2026-07-23；2026-07-29 补录）：canonical = [[Andrew Feldman- 快速推理不是体验优化，而是 AI 产品形态迁移的底层变量]]（72min；fast inference、tokens per second per user、SRAM/wafer-scale、agent CPU demand、CUDA 推理护城河收缩）
- George Hotz vs Eliezer Yudkowsky / Dwarkesh Patel（历史基准访谈，2023-08-16；2026-07-27 补录）：canonical = [[George Hotz vs Eliezer Yudkowsky- AI 安全争论的真正分歧不是乐观与悲观]]（94min；foom 证据标准、alignment 目标塑形、多 AI 竞争、pause button 与治理权力集中风险）
- Diamandis Moonshots #231（Sonnet 4.6 / Grok 4.2 / Gemini 3 Deep Think / OpenClaw）：canonical = [[Diamandis #231- 多 Agent Scaling、OpenClaw 与权限边界]]（126min；模型价格/能力路线、多 agent teaming scaling、AI-first 文档、24/7 headless agent、agent 金融与权限安全）
- Steven Sinofsky / a16z（2026-07-07）：canonical = [[Steven Sinofsky- Headless Software 不是去 UI，而是重估企业软件的价值层]]（61min；headless software、system of record、SAP/Excel 企业语义、agent impersonation、权限/例外处理与跨职能桥层机会）
- Matan Grinberg / Factory（Sequoia Training Data 2026-07-21）：canonical = [[Matan Grinberg- 暗厂不是全自动编程幻想，而是软件组织的会计系统]]（51min；多模型 harness、model independence、token router、usage-to-outcome pricing、软件工厂会计系统与 90% 异步 token）
- Axios AI+ Summit DC 2026（2026-03-26）：canonical = [[Axios AI+ Summit- AI 治理正在把算力、用电与产品责任编成同一张准入表]]（211min；将统一联邦框架、数据中心自带供能、错误包络与人机协同、采购接口和 AI 素养放回同一政策-基础设施链）
- Dan Biderman & Jessy Lin / Engram（Sequoia Training Data 2026-06-24）：canonical = [[Engram- 持续学习不是更长上下文，而是把组织经验写回模型]]（44min；持续训练、内化/外化分工、权重中的组织经验、离线消化与研究-产品反馈闭环）
