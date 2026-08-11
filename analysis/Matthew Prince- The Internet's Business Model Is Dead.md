---
title: "Matthew Prince- The Internet's Business Model Is Dead"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=UN47z_opfmo"
transcript: "[[Matthew Prince- The Internet's Business Model Is Dead 逐字稿]]"
upload_date: "2026-06-25"
duration: "1:28:14"
tags:
  - kol情报
status: canonical
updated: 2026-07-21
---

> Agent 互联网的核心矛盾不是流量不足，而是机器把一次人类决策放大为数千次请求，却绕过了广告、页面访问和品牌记忆构成的旧支付链；Cloudflare 正试图把自己从流量基础设施升级为访问控制、算力路由、审计和微支付的结算层。

视频链接：https://www.youtube.com/watch?v=UN47z_opfmo  
对应逐字稿：[[Matthew Prince- The Internet's Business Model Is Dead 逐字稿]]

**概述**：Cloudflare 联合创始人兼 CEO Matthew Prince 用 88 分钟讨论机器流量、边缘推理、AI Gateway、Agent 计算、网络安全、内部组织重写和内容微支付。最重要的判断是，Agent 让网络请求量与人类注意力脱钩：基础设施成本上升，但广告点击和页面曝光不再随请求增长。Cloudflare 因为位于访问、网络和安全层，既能观察变化，也有机会定义访问许可和支付协议。报告必须同时看到两面：Prince 的数据具有基础设施视角的稀缺性，但他对危机和解决方案的描述也与 Cloudflare 扩大控制面直接利益一致。

**论证脉络**：Cloudflare 可见流量中机器请求超过人类 → Agent 将单次任务放大为数千次访问 → 广告无法为机器消费结算 → 品牌从人类认知捷径转向机器可验证数据 → Cloudflare 用边缘、Gateway 和 isolate 承接算力与治理 → Agent 先制造安全暴露再提高软件质量 → 内部工作流平台压缩测量和管理岗位 → 内容访问控制制造稀缺 → Pay-per-Crawl 尝试建立机器对机器支付。

---

## 机器流量交叉点是重要信号，但测量边界必须写清楚

Prince 表示，Cloudflare 可见的 HTTP 请求中，机器人流量在 2026 年上半年超过了人类流量。这个时间点比团队此前预测明显提前。

> **[2:44]** "we actually had bot traffic pass human traffic online uh in the first half of 2026."

Cloudflare 覆盖大量且多样的站点，因此数据具有代表性，但它仍是 Cloudflare 网络上的 HTTP 请求样本，不等于互联网全部活动、用户数量或经济价值。一个 Agent 可以在一分钟产生数千请求，一个人类一次页面访问只产生少量请求，所以请求占比不能直接解释谁在创造或获得价值。

Prince 进一步预测五年后机器流量会达到人类的千倍，并愿意押注更高。

> **[3:47]** "you'll see a thousand times more bot traffic than human traffic"

这是基于当前增长率的外推，不是已发生事实。模型成本、站点反爬、缓存、内容授权和 Agent 架构都可能改变请求倍率。真正应持续监控的是机器请求占比、每个用户任务的请求数、缓存命中率、被拒绝访问比例和每次任务的基础设施成本，而不是只保留千倍预测。

## Agent 的效率来自把成本外部化给整个互联网

Prince 在基础设施层不区分 agent、bot 和 crawler，它们都是机器访问资源，只是不同称呼携带不同情绪。

> **[4:11]** "agent, bot, crawler are all synonyms."

他用购买相机说明请求放大：人类可能访问五个站点，Agent 可能访问五千个。

> **[5:17]** "I might visit five sites uh if I'm, you know, personally trying to figure out what digital camera to to buy, whereas my agent might visit 5,000."

对用户来说，Agent 节省时间并扩大比较范围；对网站、网络和模型提供方来说，它把一次决策的搜索成本分散到成千上万个资源请求。所谓 Agent 效率并非总成本下降，而是人类时间成本下降、机器和内容提供者成本上升。

这要求产品团队按完整任务核算成本：模型 token、搜索请求、网页渲染、反爬失败、第三方 API、缓存、重试和人工接管。只看最终回答的模型费用会系统性低估 Agent 的真实边际成本。

## 死亡的不是整个互联网商业模式，而是流量到广告收入的旧映射

Prince 的核心经济判断是，机器请求需要更多网络、CPU、GPU 和内存，但广告无法对不看页面、不点击广告的机器收费。

> **[6:15]** "the business model of the internet historically has been ads and bots don't click on ads."

> **[6:36]** "over the next 5 years the business model of the internet's going to change radically and what it changes to um is is is totally undefined"

标题中的商业模式已死过于绝对。广告仍会存在于人类消费、品牌建设和娱乐内容中，订阅、电商佣金和企业授权也不会消失。真正断裂的是旧映射：更多抓取和回答使用不再自动带来更多页面访问、广告曝光和出版商收入。

品牌也不会简单消失。Prince 认为品牌是帮助人类快速判断体验的认知捷径，而机器有无限耐心比较所有选项。

> **[7:22]** "the thing about bots is they have infinite amount of patience in order to discover you know everything"

机器采购会降低纯记忆型品牌的价值，却提高结构化信誉的价值：可验证规格、历史履约、退货率、价格稳定性、来源证明和权限政策。品牌将从人脑里的快捷方式，部分迁移为 Agent 可以读取和验证的信任数据层。

## Cloudflare 的优势来自观察和控制同一位置，这也是利益冲突来源

Cloudflare 位于大量请求的路径上，能观察流量变化、拦截访问、部署计算并参与内容支付。Prince 明确表示公司正在参与定义未来互联网商业模式。

> **[13:15]** "we're increasingly sort of playing a role in figuring out what's that business model of of the internet of the future."

其网络效应包括性能、安全情报和全球部署。攻击一个客户产生的模式可以帮助保护其他客户，Prince 将其比作免疫系统。

> **[21:22]** "we we act almost like an immune system and so an attack against any one of our customers um benefits all of the customers"

同时 Cloudflare 强调基础服务五分钟加入、十秒离开，客户没有强锁定。

> **[20:37]** "It takes about, you know, 10 seconds to leave."

低退出成本并不能消除平台权力。随着访问控制、Agent 运行、模型路由和支付结算汇聚到同一平台，迁移的不只是 CDN 配置，还可能包括策略、审计日志、身份和结算关系。评价 Cloudflare 的新业务时，应区分当前产品切换成本和未来控制面集中风险。

## 边缘推理的机会不是训练，而是延迟、辖区和模型路由

Cloudflare 很早就在边缘部署 GPU，但当时市场没有反应。其分布式网络不适合需要高带宽互联的大规模训练，却适合靠近用户的推理、区域合规和短时任务。

> **[40:47]** "put um GPUs at the edge of our network in order we said to be able to do a bunch of interesting things including inference."

> **[43:51]** "you have some sort of regulatory jurisdictional reason why why you want it to run, you know, in a particular region"

AI Gateway 承担另一层控制：统一记录 prompt 和响应、注入企业规则、限制预算并根据任务选择模型。

> **[45:07]** "it allows you to audit uh as if you're the CIO or CTO audit all of the sort of um the prompts that have gone off to various AI systems and then all the responses that you get back."

> **[46:12]** "you need to control costs"

> **[46:29]** "you don't need the latest frontier model in order to do that"

这是企业 Agent 的关键基础设施：模型不是固定供应商，而是按任务价值、延迟、隐私和失败风险动态选择的计算资源。Gateway 的价值不只是代理 API，而是形成可审计的任务级经济账本。但集中记录 prompt 和响应也创造高敏感数据资产，需要明确保留周期、访问权限和跨境边界。

## Agent 计算瓶颈可能先出现在 CPU 和隔离开销，而非 GPU

Prince 估算，如果每个知识工作者只有一个 Agent，并按传统容器方式运行，CPU 需求就可能达到当前年产量的四十倍；而现实中每人可能拥有多个 Agent。

> **[48:15]** "times the current annual CPU production that's out there."

该数字是模型化估算，访谈没有给出假设明细，但它指出了容易被忽略的成本：Agent 不只做模型推理，还需要浏览器、代码执行、状态、文件和工具连接，这些大量消耗通用计算。

Cloudflare Workers 以浏览器 tab 类似的 isolate 替代完整 VM 或容器，为短生命周期 Agent 提供更轻的沙箱。

> **[48:47]** "workers said what's the next step beyond that that's even more efficient"

Agent 平台的竞争因此不只在模型质量，还在冷启动、隔离密度、状态恢复、工具权限和任务完成后的资源回收。对企业采购而言，单位 token 价格只是成本的一部分，完整任务的运行时成本和失败重试更重要。

## 安全会先经历能力暴露，再进入持续机器审计

Prince 预测未来两年可能每周出现一次 Log4j 级别漏洞，因为模型会大规模发现遗留软件中的问题。

> **[52:48]** "you're going to see a log 4j like vulnerability every single week"

这是强烈预测，不应当作事实。但其机制合理：漏洞发现成本下降速度可能快于修复和升级速度，长期未维护的软件会集中暴露。

Cloudflare 的应对是让 Agent 检查每次代码发布和配置变更，并使用十年事故数据训练判断。

> **[54:05]** "we actually built an agent that not only reviews every code release that we we send out, but every configuration change."

Prince 认为 AI 的独特价值还包括偏差与团队不完全相关，因此适合作为第二意见。但不相关不等于无偏，Agent 可能共享训练数据和工具链造成的新型共同失效。可靠设计应让机器审计与人类评审、静态分析、测试、渐进发布和快速回滚相互独立。

## Cloudflare OS 最值得复制的部分不是 Agent，而是发现真实工作的方法

Cloudflare 先在研发中采用 AI，随后为财务、法务、营销和销售建设内部 Agent 平台。关键难题不是接模型，而是员工描述工作时会遗漏大量隐性步骤。

公司的解决方法是假装提供一个万能 Agent 邮箱，背后先由约二十人的团队全天候处理请求，观察员工真正想完成的任务，再把重复需求沉淀为技能。

> **[1:02:01]** "in reality, behind the scenes, it was a team of about 20 people that staff this 247."

这是典型的 Wizard-of-Oz 产品发现：先用人工确保服务成立，再自动化高频、稳定、可验证流程。它比让每个部门自己写 prompt 更可靠，因为能收集真实请求、缺失上下文、权限和异常路径。

Prince 举例称，投资者关系团队的财报准备从两周缩短到三分钟，并发现了过去文档中的小错误。

> **[1:02:30]** "we went from what used to be a two-week process down to what is now a threeinut process."

这类数字仍需区分自动生成时间和完整审核时间。高风险披露不能因为生成快就取消责任人签字。可复用的模式是先自动化资料收集和一致性检查，把人类时间移向判断、沟通和最终责任。

## 裁员不是 AI 采用率指标，测量岗位也不等于不创造价值

Prince 把组织角色分为 builders、sellers 和 measurers，认为 AI 尤其擅长持续测量。Cloudflare 将过去每季度抽样审计少数风险，推进到持续审计全部风险。

> **[1:05:16]** "AI systems are much better measurers than than than any humans"

随后他披露公司裁减超过 20% 团队，重点减少中层管理和测量岗位，并把管理跨度从约 6:1 推向 12:1。

> **[1:06:42]** "We laid off more than 20% of our of our team."

> **[1:09:51]** "I think 12 to one is right."

这里需要抵抗过度归因。Cloudflare 的裁员是管理层主动组织设计选择，不能证明所有公司的测量岗位都会消失，也不能把裁员规模当作 AI 生产率的直接证据。审计、合规、质量、规划和管理不仅测量，还承担解释、责任、冲突协调和例外处理。

更有价值的信号是高级员工重新成为 individual contributor，以及公司开始调整薪酬来承认个人产能提高。

> **[1:11:55]** "the power of an individual contributor and the amount of of of work that they can do is is extraordinary."

组织应先用任务数据证明哪些协调层被工具替代，再调整岗位；同时建立再培训、内部转岗和生产率收益分享。否则 AI 会成为已有降本计划的解释语言，而不是可验证原因。

## Pay-per-Crawl 的第一步不是支付，而是让内容拥有拒绝权

机器消费内容而不带来广告收入时，市场建立的前提是出版商能控制谁可以访问。Prince 将其称为制造稀缺。

> **[1:16:19]** "What you actually need to have is scarcity of supply and demand."

> **[1:16:48]** "we need to create controls that allow the people who have content online to be able to say who can access it and who who can't."

这一步改变出版商与模型公司的议价关系，但最大出版商和小创作者的能力仍不对称。Pay-per-Crawl 试图将每次机器访问变成微支付，使小站点不必单独谈判授权。

> **[1:17:56]** "There should be some basically a micro payment. every time we access a site and get information"

工程挑战极大。Cloudflare 估计系统初期需要每秒一千万笔交易，最终达到一亿，而 Visa 每秒不足十万笔。

> **[1:18:40]** "support day one, call it 10 million financial transactions per second"

> **[1:19:01]** "Visa, which is the largest payments network in the world, does fewer than 100,000 transactions per second."

微支付不只需要吞吐量，还要处理身份、去重、缓存、价值归因、退款、恶意抓取和多个 Agent 共同使用同一内容。按请求收费也可能奖励低效抓取，合理结算单位更可能是经过授权的内容片段、任务贡献或最终价值，而不是每个 HTTP 请求。

## 新内容经济可能奖励稀缺知识，也可能把 Cloudflare 变成新的分配者

Prince 希望 AI 公司识别知识模型中的空白，奖励填补新知识的人，而不是继续奖励制造点击的重复内容。

> **[1:24:39]** "what they want is highly reputable sources that are filling in the holes in the cheese."

他称自己购买的地方报纸今年从 AI 授权获得的收入可能超过展示广告，因为本地活动、酒店和雪况是通用模型缺少的稀缺信息。

> **[1:25:54]** "I think we will make more this year off AI licensing deals than we do off display ads."

这是单一自报案例，不能证明地方媒体已找到普遍商业模式，但它指出有价值的内容方向：原创、本地、持续更新、难以从其他来源重建的信息。AI 时代最弱的是可被无损复制的通用总结，最强的是拥有事实采集能力和更新时间优势的原始信源。

同时必须追问由谁评估高信誉和净新增知识。若访问、质量评分、支付和流量都由少数基础设施平台控制，旧的广告平台权力可能被新的知识结算平台权力替代。健康协议需要可携带身份、透明费率、可审计归因和多家结算方，而不是把内容经济重新集中到一个守门人。

## 关键判断

1. **机器请求超过人类是请求结构变化，不是价值结构结论**：必须注明 Cloudflare 测量范围，并持续验证千倍预测。
2. **Agent 把人类时间成本转移为全网计算和内容成本**：任务 ROI 应包含抓取、浏览器、工具、重试和第三方资源。
3. **广告不会立即消失，但流量与收入映射正在断裂**：机器消费需要授权、交易或结果级的新结算方式。
4. **Cloudflare 正从网络基础设施扩展为 Agent 控制面**：边缘推理、Gateway、沙箱和支付形成协同，也扩大集中风险。
5. **企业 Agent 平台的难点是隐性工作发现和权限继承**：人工 concierge 收集真实任务，再逐步自动化，比先造万能助手更有效。
6. **裁员是管理决策，不是 AI 效果的充分证据**：应以任务数据、质量和组织结果证明岗位变化，并处理再培训与收益分配。
7. **Pay-per-Crawl 的基础是内容拒绝权，终点不应是按请求收费**：结算需要避免奖励低效抓取，并保护小创作者议价能力。
8. **稀缺原始信息比通用总结更有价值**：地方新闻、实时事实和专业数据可能从 AI 授权获得新收入，但评分和分配机制必须开放可审计。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 管道流量与结算权：Prince 回答了 Evans 的谁收水费问题
**← [[Benedict Evans- The Economics of AI Usage and What's Next For SaaS]]**
- 本文件论点：Agent 将一个人类任务放大为数千请求，网络成本暴涨但广告无法对机器消费收费；Cloudflare 尝试用访问控制和微支付重建结算（[5:17]、[6:15]、[1:17:56]）。
- 对方论点：Evans 用电信运营商说明流量增长和基础设施投资不自动产生定价权，真正价值往往被上层应用获取。
- 关联逻辑：Evans 解释建管道不等于收水费，Prince 则尝试把管道升级为水表和结算网络。新的判断是 Cloudflare 的机会不在承载更多流量本身，而在定义机器访问的身份、许可和价值归因；风险也正来自这里，一旦同一平台同时承载、计量和结算，它可能从低利润管道变成新的互联网收费站。

### Agent 消费定价的基础设施版本：从 token 账单扩展到完整任务账单
**← [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]]**
- 本文件论点：Gateway 按任务选择模型、控制 token 成本，而 Agent 还产生 CPU、浏览器、网络和第三方访问成本（[46:12]、[46:29]、[48:15]）。
- 对方论点：Levie 认为企业软件将从单一 seat 进入 seat 与 consumption 双轨，Agent 需要状态、身份和业务价值对应的资源治理。
- 关联逻辑：Levie 在采购和软件定价层提出 consumption，Prince 展示消费账单必须覆盖的不只是 token。一个 Agent 任务可能同时调用模型、网页、代码沙箱、存储和付费内容。新的产品机会是 task economics：把完整任务成本、成功率和业务价值归集到同一身份，而不是让每个基础设施供应商分别输出无法对账的调用量。

### 从个人品牌回归到机器信誉读取：媒介基础设施的第二次迁移
**← [[a16z- The Media Game Has Changed]]**
- 本文件论点：机器有耐心比较所有信息，传统品牌作为人类认知捷径的作用下降，内容收入也从页面流量转向机器授权（[7:22]、[1:15:22]）。
- 对方论点：a16z 认为中央化媒介瓦解后，品牌从抽象公司回归长期在场的个人，真实和有趣成为人类注意力过滤器。
- 关联逻辑：a16z 描述机构分发转向个人分发，Prince 描述人类注意力转向机器代理。两次变化连续发生：个人品牌先替代抽象机构成为人类信任接口，随后 Agent 又要求把这种信誉翻译为机器可验证数据。未来品牌既需要人格叙事，也需要可被 Agent 读取的履约、价格、来源和权限证明。

### 中间层是否消失：Cloudflare 的裁员案例挑战 Levie 的分工延续论
**→ [[Aaron Levie- State of Enterprise AI 2026 Tokenmaxxing and AI-Proofing Your Job]]**
- 本文件论点：Prince 将 builders、sellers 与 measurers 分开，认为持续机器审计减少中层管理和测量岗位，并把管理跨度从约 6:1 推向 12:1（[1:05:16]、[1:06:42]、[1:09:51]）。
- 对方论点：Levie 认为 Agent 不会取消分工，只会改变分工边界；验证责任和新瓶颈会产生新的专业岗位。
- 关联逻辑：两者构成真实分歧。Prince 展示单家公司如何主动压缩协调层，Levie 则预测需求扩张和责任边界会重新创造分工。判断谁更接近长期结果，需要跟踪 Cloudflare 在裁员后的事故率、决策质量、员工负荷和新增岗位，而不是只看短期成本和管理层级。组织变平可能提高速度，也可能把协调和责任隐性转移给 IC。

---

**元信息**
- 标题：Cloudflare CEO: The Internet's Business Model Is Dead
- 频道：The MAD Podcast with Matt Turck
- 嘉宾：Matthew Prince
- 发布时间：2026-06-25
- 时长：1:28:14
- YouTube：https://www.youtube.com/watch?v=UN47z_opfmo
- 逐字稿：[[Matthew Prince- The Internet's Business Model Is Dead 逐字稿]]
- 重写时间：2026-07-21
