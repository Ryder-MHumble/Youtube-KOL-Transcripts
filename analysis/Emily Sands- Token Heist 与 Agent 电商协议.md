---
title: "Emily Sands- Token Heist 与 Agent 电商协议"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=6opo7LnZajM"
transcript: "[[Emily Sands- Token Heist Wiping Out AI Startups]]"
tags:
  - kol情报
created: 2026-07-21
status: canonical
dedup_note: "基于独立KOL逐字稿目录中的canonical transcript重校"
---

> 如果说 Agent 电商的协议层（AEP）是 commerce 版 MCP、shared payment token 是全新支付原语，那么 token theft 就是这个新经济地基上最快增长的犯罪形态——Emily Sands 赌的是：谁先建好 agent 经济的支付+欺诈+微支付基础设施，谁就定义下一个互联网经济周期。
> —— Emily Sands, MAD Podcast, 2026-07-09

视频链接：https://www.youtube.com/watch?v=6opo7LnZajM

对应逐字稿：[[Emily Sands- Token Heist Wiping Out AI Startups]]

**概述**：2026年7月9日，The MAD Podcast with Matt Turck，Stripe 数据与 AI 负责人 Emily Sands 二度回归。对话者 Matt Turck。核心赌注不是"agent 会不会买东西"，而是"agent 经济的整套金融基础设施——协议、支付原语、钱包、微支付、欺诈防御——正在从假设变为已部署的现实"。Sands 从 Stripe 处理全球约2% GDP 的数据视角，给出了 agent 电商协议（AEP）、shared payment token、Link Wallet、stablecoin 微支付、token theft 欺诈、vibe deployment 的完整技术栈。这场75分钟访谈的信息密度极高，几乎每一句话都是一个可独立追踪的产业信号。

**主题脉络**：
1. Agent 电商的谱系——从"AI 里发现产品"到"agent 自主交易"
2. Agent E-Commerce Protocol（AEP）——commerce 版 MCP 的诞生
3. Link Wallet 与 shared payment token——给 agent 钱但不给钥匙
4. Stablecoin 微支付——agent 场景首次让5美分交易经济可行
5. Token theft——AI 经济增长最快的犯罪，"超过六分之一注册是滥用"
6. Vibe deployment——代码生成已解决，部署成为新瓶颈
7. SaaS 定价瓦解——推理边际成本击穿 per-seat 模型
8. Solopreneur 爆发——美国500万人年收入超$10万，全球化顺序反转
9. 12个月预测——agent 作为端到端微型企业运行

---

## 一、Agent 电商不是单一场景，而是一条从"发现"到"自主交易"的谱系

Sands 开场就纠正了一个常见误解：人们想到"agent commerce"时往往只想到"agent 完全自主地发现、决策、购买"这一极端场景。但她指出，现实是一条完整谱系，一端是人类在 AI 界面里发现产品然后自己点购买按钮，另一端是 agent 全自主交易，中间有大量过渡形态。

> **[2:36]** "So at one end, and this is where our machine payments protocol lives, but basically you have agents that are out autonomously discovering a service and deciding to buy it and handling the transactions like entirely on their own, right? Like no human in the loop. And that's maybe what people think of when they say agent commerce, but that's just one end of the spectrum."

> **[2:56]** "There's also the whole other end of the spectrum where like people are looking for shoes for flatfooted runners inside an AI surface and the AI surface gives you an answer and increasingly um you know that was true also in sort of traditional search but now increasingly that answer comes with a buy button."

这条谱系的现实含义是：无论落在哪一端，都需要同一套新基础设施——商家要能向 agent 暴露产品目录/库存/价格，消费者要能授权 agent 代为支付，agent 要能安全执行交易。Stripe 已与 Google/Gemini、Microsoft/OpenAI、Meta 合作部署：Google AI Mode 和 Gemini App 里直接内嵌商家结账，ChatGPT 和 Copilot 里让产品可被发现，Meta 的广告里直接由 agent 执行结账。

> **[3:54]** "Meta is another example, a little bit of a different flavor, but we're powering checkout right inside ads."

品牌侧的早期采用者包括 Best Buy、Coach、URBN、Kate Spade、Quint、Fanatics、JD Sports；平台侧 Wix、Shopify、Big Commerce、Commerce Tools 全部接入。Sands 特别指出当前消费者大多停留在"level two"——让 AI 帮忙找产品但仍自己决策，level three（推荐+一键购买）已落地（如 ChatGPT instant checkout），但"一句话搞定暑假旅行"的 level five 还很远。

> **[6:29]** "we're not in the world where you're booking your summer vacation oneshotting it with an LLM."

这套"自动驾驶等级"框架的价值不在于精确分类，而在于它暴露了一个真实矛盾：消费者对"agent 替我买"的信任建设需要时间（"humans just need reps"），但基础设施已经跑在前面——技术已就绪，瓶颈在信任和用户体验的演进。

---

## 二、AEP 是 commerce 版 MCP——一次暴露目录，所有 agent 都能发现

当 Matt Turck 问"AEP 是不是就像 commerce 版的 MCP"时，Sands 直接确认。AEP（Agent E-Commerce Protocol）的核心设计是：商家只需暴露一次产品目录/库存/价格，然后选择性接入所有遵循该协议的 agent。商家不需要为每个新 agent 重新注册目录。

> **[8:31]** "agentic commerce protocol lets them um expose their product catalog once um and then opt in to um all of the agents uh who who uh work with with that protocol."

这里的隐含立场极为重要：Stripe 在协议层选择开放（platform agnostic、payment processor agnostic），AEP 可以与 OpenAI 合作但也支持其他 provider，可以跑在 Stripe 上也可以把 shared payment token 传给 Adyen 或任何其他 PSP。但协议的"开放"和"接入"本身由 Stripe 定义——商家暴露目录的标准、agent 接入的协议，都是 Stripe 的产品。这是"协议开放、标准封闭"的经典平台策略：谁能定义 commerce 与 agent 交互的标准协议，谁就占据了 agent 经济的协议层位置。

> **[9:10]** "it's uh, platform agnostic, payment processor agnostic. So all this works uh, you know, you mentioned that we co-created with OpenAI. It works with OpenAI but also other providers. It works if Stripe processes your payments, but you can also pass on that that shared payment token uh, to any other uh, PSP."

Sands 没说但可以反推的：Stripe 之所以能成为这个协议的定义者，不是因为它的模型或 agent 能力，而是因为它已经连接了买卖两端——商家侧（Best Buy、Coach、Shopify 等）和消费者侧（3亿 Link 用户）都在 Stripe 上。协议的开放性是结果而非起因；Stripe 的双边网络密度才是它定义协议的底气。这一点在后面 Radar 部分会更明确。

---

## 三、Shared payment token——给 agent 钱但不给钥匙

AEP 的第二个核心组件是 shared payment token，Sands 把它定义为"全新支付原语"。核心设计是：消费者授权 agent 代为支付，但 agent 从不接触底层凭证。token 编码了 agent 被允许做什么——哪些商家、多少金额、什么币种、多长时间窗口。agent 在结账时把 token 交给商家，商家凭 token 执行交易。

> **[28:06]** "It's a new payment primitive. We built it u maybe six months ago specifically for agent commerce. Um it is a way for a consumer to authorize an AI agent to pay on their behalf um without handing over their actual card details. So the token encodes um exactly what the agent is allowed to do, right? Which merchants can be charged up to what amount, in what currency, for how long."

Shared payment token 覆盖多种支付方式（包括 Affirm、Klarna 等 BNPL），不止是卡。它是 Link Wallet for agents 的底层原语，也驱动 Stripe 的 machine payments 协议（MPP）。Sands 明确区分了三个层次：一次性虚拟卡（v1，非常受限）→ shared payment token（全新原语，wallet agnostic、PSP agnostic）→ Link Wallet（消费者端体验层，基于 shared payment token 但更完整）。

> **[29:01]** "one-time use virtual cards were like a useful backs stop as we went and built the shared uh payment token. Shared payment token is a new payments primitive that is wallet agnostic and by the way also payment processor agnostic."

> **[29:24]** "think of like link wallet as the consumer experience, the consumer wallet for agents um that leverages that same uh shared payments token primitive um but is more um fully featured for the consumer and it's software so it's fully programmable."

消费者可以在 Link Wallet 里设置精细控制——限制特定商家类别、限定地理范围、限定单笔/累计金额上限，甚至要求每笔交易都需人工确认。这套可编程的"护栏"是 agent 支付在消费者侧成立的前提。

这里有一个被 Sands 轻描淡写但极为重要的设计原则：**商家始终是 merchant of record**。Agent 交易在商家侧的表现要与人类交易一致——agent 不需要像人类一样受约束，但从商家视角，"sale facilitated through an agent but the business is still the business"。

> **[31:59]** "businesses have to remain the merchant of record. Like that's a core design principle for us."

> **[32:13]** "we see our job as having agentic transactions behave the way human transactions do. Now that doesn't mean that agents need to behave like humans or be constrained in the same way humans do."

这个设计原则的隐含立场是：Stripe 拒绝把 agent 变成独立的"交易主体"（那会引入 agent 法律人格问题），而是让 agent 始终作为消费者的代理执行者，商家关系不变。这与 Brian Armstrong 的 Base 协议"每个 agent 有自己的银行账户"路径形成根本分歧——Sands 让 agent 作为工具（代理执行），Armstrong 让 agent 作为主体（独立账户）。两条路径的法律后果完全不同：Sands 的方案里 agent 出错时责任仍在消费者和商家之间分配，Armstrong 的方案里 agent 的交易没有可追溯的人类责任人。

---

## 四、Stablecoin 微支付——agent 场景首次让5美分交易经济可行

Sands 在这里给出了一个产业信号级别的判断：stablecoin + agent 场景的组合，首次让微支付在经济学上成立。历史上微支付不成立有两个原因——人类不愿为5美分文章输入信用卡，处理5美分信用卡交易的成本是负边际。但当 agent 执行交易时，人类不参与操作（不输凭证、不导航网页），成本摩擦消失；stablecoin 结算成本极低，微支付终于可行。

> **[30:23]** "Agents are very you know microtransactions never actually really made that much sense even in the context of content because nobody wanted to put in even if it was only 5 cents no one wanted to put in their credit card to buy a 5 cents article like that was just too much friction. A and B, nobody wanted to process a credit card for 5 cents because you would have negative margins. But I think we enter a world where like the human is not doing any work to execute the transaction."

> **[30:56]** "And you pair that with okay and now it's you know uh burning down some stable coin balance. And we can talk about the work we're doing with Tempo there. um suddenly microtransactions become very viable and I think we're going to quickly move to a world where especially in buying inference or tokens or um sort of AI sassy products um there's going to be you know you are going to be using"

Tempo 是 Stripe 与 Metronome 共建、专为支付优化的区块链。Metronome 负责实时计量 token 消耗，Tempo 负责即时低成本的 stablecoin 微支付结算。两者组合让 AI 公司可以在 agent 消费 token 的同时实时收费——不必在月底才寄账单（那时 agent 可能已烧掉天量成本）。

> **[1:03:00]** "What you actually want to do especially when the agents are the buyers is you want to um track the tokens as they're consumed. And you mentioned the infrastructure. You want to track them in real time at sub substantial scale. And then as importantly, you don't just want to track them as they're consumed. You actually want to like collect payments as they're consumed."

这个信号的含义远超支付技术本身：它指向一个"流式经济"——agent 时代的计费从"月度批次"变成"实时流"。这对 AI 公司的会计系统、营收确认系统、财务团队的工作方式都是结构性冲击。Sands 在后面提到，传统 spreadsheet 会计在微交易洪流面前完全崩溃，AI 公司的会计已是"hybrid accountant-engineer"角色，职责从"关账"扩展到"发现异常、识别欺诈、诊断产品故障"。

> **[48:51]** "traditional accounting in spreadsheets like does not work when \[laughter\] you have this just like like proliferation of rows because these are like microtransactions are are truly happening."

> **[49:23]** "they were like a hybrid accountant engineer, which they needed to be because of the scale of the data they were dealing with."

---

## 五、Token theft——"AI 领域最被低估的话题"

Sands 把 token theft 称为"AI 领域最被低估的话题，可能差很多"（"maybe by a lot"）。这不是夸张——她给出的数据是：超过六分之一的 AI 公司注册属于滥用。这不是传统凭证或支付欺诈，而是"第一方滥用"：欺诈者不偷钱也不偷凭证，只偷 token，因为 token 有真实价值——可以用来构建、在市场转售、包装新产品零成本转卖。

> **[50:51]** "fraudsters have figured out that in AI um you actually don't really need to steal money or credentials. Uh you can just steal tokens. And tokens have real value, right? You can use them to build things. Um you can resell them on marketplaces."

> **[51:20]** "for AI companies, maybe this is implied by our earlier conversation on SAS, but like the risk is existential, right? If someone stole a little bit of your SAS, like didn't matter because it didn't really cost you anything on the margin. um when someone steals your tokens, if your fraud rate is high enough, the economics of your product actually um break really fast."

Sands 拆解了三种当前主要欺诈形态：

**1. 多账户滥用**：同一批人反复注册新账户以获取新用户 credit。六分之一的 AI 公司注册属此类。对公司的成本极高——少量人在大量账户上消耗大量 token。

**2. 免费试用滥用**：欺诈者用一次性虚拟卡（24小时过期）创建免费试用、耗尽 credit、永不转化。过去6个月在 Stripe 上翻倍，增量主要来自 AI 业务。已有完整地下产业链在推销"免费试用卡"。

> **[52:32]** "Another example I think is interesting is is free trial abuse. So these are like fraudsters come in, they create a free trial, they put down a payment method, um they they drain through like all of the credits, but they never have any intent to convert."

**3. 用量后逃单（dine and dash for tokens）**：积累数千美元用量后月底不付。由于是 AI 不是 SaaS，公司已承担了 token 成本。

被偷的 token 如何变现？Sands 描述了一条黑暗产业链：以折扣价在暗网市场转售（"用 Cursor/Lovable 只要$2，我的成本是零"）；批量生成音乐上传 Spotify/Apple Music 再用假播放量收版税；直接克隆 AI 公司的网站（vibe code 一个前端，后端全是偷来的服务）以更低价格卖产品。

> **[55:13]** "there's a dark like a dark web of marketplaces where you say like use a cursor or lovable for $2 but my my cost is zero therefore I make money."

> **[55:46]** "we see people going in and like mass generating music tracks and then uploading them to Spotify and Apple Music and then getting fake streamers and then collecting royalties."

> **[55:59]** "rather than just resell the subscription on places like Telbal, they'll like literally clone the AI company, right? You can just like vibe code a website. The back end is just like spitting out exactly what you got from the service that you're stealing from and then you like sell the product as yours. Uh but cheaper."

Sands 的核心洞察是：这些欺诈形态在传统 SaaS 里不构成存在性威胁，因为 SaaS 边际成本接近零——偷一点 Salesforce 不伤筋动骨。但 AI 公司每次 prompt/API 调用都有真实边际成本，欺诈率够高就"经济模型很快崩坏"。这意味着 token theft 不是支付欺诈问题，而是 AI 商业模式的存在性威胁。

> **[57:53]** "It's like what we would historically have called like firstparty abuse, right? like resale abuse or account sharing or multi-accounting or free trial. It's like first party abuse."

Stripe 的应对是 Radar——已有十多年的欺诈防护产品，从交易欺诈扩展到全客户生命周期的端到端滥用检测。Radar 的核心优势是网络密度：Stripe 处理全球约2% GDP，在 AI 领域份额更高（"basically all AI buyers and all AI sellers are on link and on Stripe"），因此"没有好的 AI 买家我们没见过，没有坏的 AI 买家我们没见过"。

> **[1:00:14]** "Yeah, it's real time, it's AIdriven. And then I actually like most importantly here uh for its like differentiation, it just looks across the stripe network."

> **[1:00:26]** "we haven't seen before and there are very few bad AI buyers we haven't seen before and so uh that combination um you know it's it's yes the size of the network and this 2% of global GDP uh flowing through Stripe but really when it comes to AI it's the density of the network"

Lovable 的数据印证了这种密度——58% 的 Lovable 交易量流经 Link。Radar 评分已内嵌在 shared payment token 中，商家在结账时就获得买家和 agent 的双重可信度评分。这是一个关键的结构性优势：Stripe 不是在卖一个独立的反欺诈工具，而是把反欺诈能力编织进支付原语本身。

---

## 六、Vibe deployment——代码生成已解决，部署成为新瓶颈

Sands 在这里给出了两个让全场访谈最具"第一手数据"质感的信号。第一个：agent 对 Stripe 文档的流量自一年前增长超过10倍，现在占 Stripe 文档总流量的约40%——意味着 agent 已经是 Stripe 文档的主要"读者"之一，编码者中 agent 的比例在某些领域已超过人类开发者。第二个：Stripe CLI 的 API 资源请求中70%来自 agent——"CLI 的主要使用者已经不是人了"。

> **[38:07]** "So like agent traffic to Stripe's documentation grew more than 10x since we talked a year ago. uh agent traffic is now about 40% of all our docs traffic"

> **[38:38]** "and another example actually is is our CLI our command line interface which historically was like a pretty niche tool used by like a pretty small group of developers. Um it now it just like exploded and we were like what is happening? And it's now um 70% of its API resource requests are from agents."

这两个数据点的含义是：vibe coding 已经是现实，不再是预测。但 Sands 的核心判断是：代码生成本身已解决，真正的瓶颈迁移到了部署——agent 能在20分钟内写出完整应用，但要让它上线，需要创建数据库账号、auth 服务、hosting 账号，在多个 dashboard 间复制粘贴 API key——每一步都还是为人类设计的 onboarding 流程。

> **[39:24]** "you've still got this pretty big friction before that app is actually live, right? So you got to go like I don't I mean it depends what you're doing, but you got to probably create an account with your database provider, then your off provider, then your hosting service, and you're like bouncing around."

> **[39:55]** "every one of them just like the payments flows was designed for like you and me as humans sitting down and clicking through this like weird setup wizard thing. Um, and I don't think it really bothered any of us that much because we weren't doing it that much because the hard part was the coding part. But now that like the app could be built in coded in 20 minutes like okay the long pole is deploying the thing."

Stripe 的回应是 Stripe Projects——让 agent 能从命令行直接注册、配置、集成部署所需的所有服务（Vercel、Supabase、Cloudflare、Twilio、Clerk 等），近期又新增16个合作伙伴。Sands 坦率承认 Stripe 做这件事的原因：部署摩擦是互联网经济增长的瓶颈，而 Stripe 的使命是"increase the GDP of the internet"——如果有人能部署但卖不了东西，Stripe 就收不到钱。

> **[41:27]** "I'm the the honest answer is we care because it was becoming the bottleneck. like the barrier to building is gone, but the barrier to deploying is like a real friction."

> **[42:20]** "we were like looking at the developers trying to get the thing live and we were looking at the businesses trying to get the thing like used by developers and we're like, okay, I think we can we can make this market uh a little bit smoother."

隐含立场：Stripe 进入部署编排不是因为它想做 DevOps，而是因为部署摩擦直接卡住了 Stripe 的核心商业模式——更多人部署更多应用 = 更多交易 = 更多 Stripe 收入。这是"使命驱动"和"利益驱动"完全对齐的案例。但 Stripe 把自己定位为"orchestration only"——如果别人能做这个编排，Stripe 也乐意。这个声明的真诚度存疑：一旦 Stripe 成为 agent 部署编排的事实标准，它就占据了 agent 应用生命周期的入口，这与它在支付协议层的策略如出一辙。

---

## 七、SaaS 定价瓦解——推理边际成本击穿 per-seat 模型

Sands 从 Stripe 视角给出了 AI 公司定价模型迁移的第一手数据。传统 SaaS 的经济模型很简洁：产品建一次，多一个客户的边际成本接近零，所以固定费订阅或 per-seat 授权成立。AI 打破了这个模型——每次 prompt、每次 API 调用、每个任务都有真实边际成本，推理不免费。

> **[44:00]** "you now have all these businesses where how your customers use your product directly determines uh whether you make or lose money."

Sands 的判断很硬：她几乎没看到"仍在增长或已规模化"的 AI 公司还在用纯订阅或纯 per-seat。"经济学上不成立"——有人用得多（成本高），有人用得少（成本低），没有用量计量就无法区分定价。

> **[44:34]** "I see very few scaling or scaled AI companies that are still exclusively subscriptions or seatbased."

但她观察到的主流不是纯 usage-based，而是 hybrid：固定费订阅 + 超阈值后按用量计费。Lovable 是典型案例——起步用纯订阅（Stripe Billing），随着成本增长转向 hybrid：固定$25或$100/月包含一定 credit，超出后按 token 消耗精确计费。11 Labs 走了完全相同的路径。

> **[45:32]** "So like a great example is lovable. When they launched, they had like a simple subscription through Stripe billing makes total sense."

这个 hybrid 模式的设计意图是双重的：用订阅的熟悉感降低用户进入门槛（尤其非技术用户对"token/credit"概念不适应），同时在任何有意义的用量级别上让收入与成本同步增长。Sands 把它总结为"customers pay only for what they get and you make sure you monetize for the underlying cost that you're going to have to bear"。

Agent 作为买家时，计费逻辑进一步变化：agent 以机器速度消费，月底寄账单已经来不及——agent 可能在一个月内烧掉天量成本。因此 agent 时代需要实时计量 + 实时计费（streaming payments），Metronome + Tempo 让这成为可能。

> **[48:20]** "agents are happy to just like pay as they go in a very literal way. Plus, businesses need them to be paying as they go so that they don't uh rack up a bunch of spend and then and then go dark."

---

## 八、Solopreneur 爆发——美国500万人年收入超$10万，全球化顺序反转

Sands 从宏观层面给出了一个被严重低估的信号：美国企业注册数据在疫情后先飙升再平台期，最近几个季度再次加速，但增量全部来自"非雇主企业"（non-employer firms）——即 solopreneur。美国已有500万人靠经营单人公司养家，其中数十万人年收入超过$100万。Sands 把这归因于 AI——vibe coding + vibe deployment 让"构建"变容易，垂直 AI agent 让"运营"（客服、会计等）变可行，单人公司结构性地可持续了。

> **[15:09]** "the incremental growth is coming entirely from uh non-employer firms is the literal language that the Census Bureau uses, but you and I would just call them solopreneurs. And so, you know, the number of people, solarpreneurs, who are earning more than $100,000 a year, um, has just gone like this since 2022. And now there's in America alone 5 million people making their living running solo companies."

> **[15:37]** "Not like, oh, I just said I was a solarreneur. Like literally, that is my income supporting my family. Um, and there are hundreds of thousands that are clearing a million a year."

这不是美国独有——Sands 给出全球数据：荷兰新企业注册增40%，芬兰70%，法国80%。Stripe 的视角更直接：新企业上线速度自一年前翻倍。2026年 Atlas（Stripe 的企业注册产品）初创企业 cohort 在同等月数下的收入是去年 cohort 的五倍。

> **[1:05:05]** "new business registrations are up basically around the world at least for advanced economies they're up um like 40% in the Netherlands and 70% in Finland and 80% in France."

> **[1:05:32]** "Atlas startups from the 2026 cohort and you know it's only June so it's early in their life cycle but they're tracking to like five times the revenue of last year's class at at these same um number of months."

更反直觉的是全球化的顺序反转：过去"先做大了再全球化"，现在"第一天就全球运营，靠全球化来做大"。Emergent Labs（2024年美国成立的 AI 全栈应用平台）70%收入来自国际，在16个国家有实质业务。

> **[1:06:33]** "you literally go global from it doesn't lit necessarily literally mean every country, but it's like you're in dozens of countries on day one like your launch day. And that is how you get big. You get big by being global."

Sands 对"AI 是否会导致少数巨头垄断"的判断是反共识的：她承认大公司（"everyone knows them"）在爆炸式增长，但同时看到了大量小公司的涌入和快速规模化——这对竞争和经济成长是好信号。她对 AI 经济乐观的根源不只在消费效率，更在于"business dynamism"——一个有想法的人能从想法到产品到市场。

> **[1:08:15]** "I think one of the reasons I'm bullish on the AI economy is at least so far for sure there are big guys who have things that are highly complimentary to AI."

隐含立场：Sands 作为 Stripe 高管，自然有动力强调新企业增长（Stripe 的 TAM 就是互联网 GDP）。但数据本身——5倍收入增长、500万 solopreneur、全球化反转——不太可能是纯粹的叙事包装。关键在于：这种"一人公司爆发"有多少是 AI 驱动 vs 疫情后结构性变化？Sands 倾向于归因 AI（vibe coding + vibe deployment + AI agent 运营），但承认"how much of that is AI or not"仍是开放问题。

---

## 九、12个月预测——agent 作为端到端微型企业

Matt Turck 最后让 Sands 预测一年后的状态。Sands 没有给出具体"等级"预测，而是指向一个更根本的变化：agent 将从"买家"演变为"多面手经济参与者"——同时购买、销售、配置基础设施、端到端运行企业。她明确这不是普及化场景，但"会看到一些例子"。

> **[1:12:10]** "all of that's just going to continue to demand more purpose-built infrastructure including financial infrastructure versus just the sort of old um human centric commerce stack."

Stripe Directory 刚进入公开预览——让 agent 轻松发现 provider，通过 Stripe Projects 直接集成，然后 agent 可以把发现+集成+购买+组合的东西变成一个新服务去卖。这就是"agent as a micro firm"的雏形。

> **[1:12:10]** "all of that's just going to continue to demand more purpose-built infrastructure including financial infrastructure versus just the sort of old um human centric commerce stack."

Sands 把真正的范式变化与渐进改良做了区分："把现有流程提升5-10%效率"不是有趣的事——有趣的是重新想象系统如何运作。她的愿景不是"Emily 授权 agent 代她买东西"，而是"Emily 有一个 agent 被委派运营一家企业，包括买一些东西、卖一些东西、赚取利润"。

> **[1:14:05]** "But like where it actually gets interesting is where um we start to reimag like how the system works."

这个愿景的赌注是：agent 电商的终局不是"人类更方便地买东西"，而是"agent 成为经济主体"。Stripe 赌的是谁能提供这套 agent 经济主体所需的金融基础设施。但 Sands 回避了一个关键问题：如果 agent 成了"微型企业"，它的法律人格、税务责任、跨司法管辖的合规义务如何解决？这正是 Brian Armstrong 的 Base 协议试图绕过（no KYC）而 Sands 的 Link Wallet 试图锚定在人类用户上的核心分歧所在。

---

## 深度关联
> 以下关联基于论点级分析

### Token 定价击穿 SaaS——从企业侧诊断到支付侧实证
**← [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]]**
- 本文件论点：Sands 从 Stripe 数据证实，几乎没有仍在增长/已规模化的 AI 公司还用纯 per-seat 定价；hybrid（订阅+超阈值用量计费）成为 Lovable、11 Labs 等的主流路径；agent 买家需要实时计量+实时计费 [44:34][46:33][47:20]
- 对方论点：Levie 从企业侧诊断 token 账单击穿旧定价——$20/月/用户的 per-seat 在 agent 烧 $1000/任务时物理不成立，前沿 token 价格不降反升，企业进入 seat+consumption 双轨时代 [11:13][12:42]
- 关联逻辑：Levie 从 CIO 视角给出了"为什么旧定价不成立"的诊断，Sands 从支付基础设施视角给出了"新定价正在如何落地"的实证。Levie 说"经济学不成立"，Sands 用 Lovable/11 Labs 的迁移路径验证了"不成立之后变成了什么"。两人从企业采购侧和支付处理侧描述同一迁移的两个端点：Levie 看到 token 成本溢出 IT 预算进入业务线预算，Sands 看到 hybrid billing + streaming payments 成为 AI 公司的标准计费栈。合在一起才完整：token 定价击穿不只是企业预算问题，它正在重写从企业采购到支付结算的整条链路。

### 机器流量超越人类——从流量层到支付层的同一断裂
**← [[Matthew Prince- The Internet's Business Model Is Dead]]**
- 本文件论点：Sands 证实 agent 已成为 Stripe CLI 的主要用户（70% API 请求来自 agent）、文档流量的40%来自 agent；agent 电商协议（AEP）正在为"机器对机器"交易建新基础设施 [38:07][38:38][7:35]
- 对方论点：Prince 诊断2026上半年机器人流量正式超越人类流量，"bots don't click on ads"使广告商业模式物理性断裂；Pay-per-Crawl 和微支付是机器对机器互联网的新经济地基 [01:20][03:30]
- 关联逻辑：Prince 从流量层（Cloudflare 处理全球20%互联网流量）诊断了"消费者从人类变机器"的断裂，Sands 从支付层（Stripe 处理全球约2% GDP）给出了同一断裂的支付侧实证。Prince 看到 agent 一次购物触发5000次站点访问（vs 人类5次），Sands 看到 agent 以机器速度消费 token 需要实时计费而非月度账单。两人从基础设施的两端描述同一转变：互联网正从"人类对人类"变成"机器对机器"，Prince 在建流量定价机制（Pay-per-Crawl），Sands 在建交易定价机制（AEP + streaming payments）。两者共享的判断是：旧的计量单位（点击/曝光/月度账单）在机器消费场景下全部失效。

### 模型层价值捕获的支付侧验证——协议开放但入口封闭
**← [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Sands 的 AEP 协议层 platform agnostic、PSP agnostic，但消费者关系锁定在 Stripe Link Wallet；shared payment token 是全新支付原语；stablecoin 微支付在 agent 场景首次经济可行 [9:10][28:06][30:56]
- 对方论点：Evans 用电信运营商类比论证模型层注定商品化——流量涨2000倍但股价横盘20年，建管道的不收水费；价值向上层应用逃逸 [12:04]
- 关联逻辑：Evans 在模型层诊断了"谁建管道谁不收水费"的结构性困境，Sands 在支付层给出了一个具体的"收水费"路径——不是在模型层建护城河，而是在 agent 经济的协议层和消费者入口层建护城河。Sands 的策略是对 Evans 问题的直接回应：AEP 协议开放（任何 agent/商家/PSP 可接入）但 Link Wallet 消费者入口封闭（3亿用户、可编程护栏、Radar 网络密度）。这验证了 Evans "价值不在管道层"的判断——Stripe 不在"模型管道"层建护城河，而在"支付协议+消费者钱包+欺诈网络"层建护城河。但张力在于：Sands 的 stablecoin + Tempo 路径引入了去中心化结算层，Evans 的"商品化"逻辑是否也适用于支付原语本身？如果 shared payment token 真的 PSP agnostic，Stripe 的入口优势能否长期维持？

### Agent 金融的两种哲学——协议即身份 vs 协议开放入口封闭
**← [[Brian Armstrong- 每个 AI Agent 都有自己的银行账户]]**
- 本文件论点：Sands 的 Link Wallet + shared payment token 让 agent 作为消费者的代理执行者，agent 不接触底层凭证，商家始终是 merchant of record——agent 是工具不是主体 [28:06][31:59]
- 对方论点：Armstrong 的 Base 协议提供 no-KYC self-custodial wallet，让每个 AI agent 拥有自主金融账户，绕过人类身份验证体系——agent 是主体不是工具 [01:17]
- 关联逻辑：两条路径代表 agent 金融基础设施的两种根本哲学。Sands 选择"协议开放、入口封闭"——AEP 协议层 platform agnostic，但消费者关系绑定在 Stripe Link Wallet 内，agent 始终锚定在人类用户凭证上。Armstrong 选择"协议即身份"——Base 协议本身就是 agent 的金融身份，完全去中心化、无 KYC，agent 自主注册自主交易。前者赌的是消费者体验控制权和现有法律框架的连续性（agent 出错时责任仍在人类用户和商家间分配），后者赌的是去中心化基础设施会吸引所有 agent 自主接入（但 agent 交易没有可追溯的法律责任人）。Sands 在访谈中明确说"businesses have to remain the merchant of record"是核心设计原则——这直接否定了 Armstrong 的"agent 作为独立交易主体"路径。两人共享的盲区是：agent 金融身份的法律基础悬而未决。当 Sands 说"agent 作为微型企业端到端运行"时，她没有回答这个微型企业的法律人格和税务责任问题；当 Armstrong 说"no KYC"时，他没有回答反洗钱和制裁合规问题。Agent 经济的法律基础设施远未跟上技术基础设施。

---

**元信息**

| 字段 | 值 |
|------|-----|
| 标题 | The "Token Heist" Wiping Out AI Startups \| Emily Sands (Stripe) |
| 频道 | The MAD Podcast with Matt Turck |
| 发布日期 | 2026-07-09 |
| 时长 | 75min |
| YouTube链接 | https://www.youtube.com/watch?v=6opo7LnZajM |
| 分析时间 | 2026-07-17 |
