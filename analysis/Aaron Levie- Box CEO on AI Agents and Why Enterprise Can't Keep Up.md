---
title: "Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=dvVbA9OcBqs"
transcript: "[[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up 逐字稿]]"
tags:
  - kol情报
status: canonical
created: 2026-06-10
order: 13
---

> 企业 AI 的真正瓶颈不是模型能力，而是遗留系统的集成债务和组织的适应性鸿沟——把 Agent 当新员工入职而非软件来集成，才是穿越这道墙的唯一路径。
> —— Aaron Levie & Martin Casado, a16z 2026

视频链接：https://www.youtube.com/watch?v=dvVbA9OcBqs
对应逐字稿：[[Aaron Levie- Box CEO on AI Agents and Why Enterprise Can't Keep Up 逐字稿]]

概述：2026年4月28日，a16z的Steven Sinofsky和Martin Casado邀请Box CEO Aaron Levie进行了一场58分钟的圆桌对话。三人均有大型企业经历（Sinofsky前Microsoft Windows负责人，Casado前VMware/Nicira创始人，Levie运营Box二十年服务全球企业客户），这场对话的核心赌注是：硅谷对AI Agent的乐观与企业的现实之间存在一道结构性的鸿沟，而鸿沟的根源不在技术本身，在于遗留系统的集成债务和组织决策的中央化悖论。

主题脉络：
1. 硅谷与企业的工作流鸿沟——技术能力不是瓶颈，组织形态才是
2. Agent是软件还是人？——架构哲学的根本分歧
3. 遗留系统的集成墙——AI不帮集成任何东西
4. Headless SaaS的幻觉与Agent身份问题
5. 代码越多工程师越多——AI生产力悖论
6. 就业扩张而非萎缩——复杂性的自我繁殖

---

# 一、硅谷的工程师错觉与企业的工作流深渊

对话开篇就锚定了整场的核心张力。Aaron Levie形容自己的角色是"bring reality to the valley and then bring the valley to reality"——一个在两个世界之间穿行的信使。这个鸿沟不是观念分歧，而是工作方式的结构性差异。

硅谷工程师拥有五到十个让Agent天然有效的前提条件：技术素养极高、深度接入互联网、能自主选择和调试工具、模型擅长代码、工作成果可验证。而非工程领域的知识工作者面临的是碎片化的数据、老旧的系统、不可验证的输出。Agent在工程场景中成功，不代表它能自动迁移到其余90%的知识工作中。

> **[2:46]** "the technical aptitude of an engineer is just like insanely high. The level of wired-in-ness to what's going on on the internet is insanely high. The the ability to use your own tools and make your own choices is insanely high."

Martin Casado进一步指出，这个鸿沟被一个"中央化决策悖论"放大：AI作为技术趋势正在个人层面快速扩散，但大型企业习惯于中央化决策——董事会要AI，CEO请咨询公司，搞一个没人知道怎么运作的中央项目，然后失败。而那些在个人层面成功使用AI的人，根本不在这个决策链条上。

> **[5:15]** "Like that's clearly silly because I am sure everybody's using chat GPT very effectively. What what they really should be saying is you know, whatever. Like I Listen, I sit on these boards too. So the board goes to the CEO. What does the board say? We need more AI. And what does the CEO say?"

> **[5:29]** "Oh, okay. I'll get like a consultant to do more AI. And then they have some centralized project that nobody knows how it works. They haven't aligned their operations and those things will fail."

更微妙的是，AI的快速迭代本身就制造了企业架构层面的瘫痪——CIO们在三四种Agent部署范式之间犹豫不决，因为三年前选错路径的伤痕还在。技术变化的速度反而降低了技术向核心工作流扩散的能力。

> **[7:57]** "that actually creates a bit of paralysis because now as an enterprise architecture team in the real world you're like man like what what horse do I want to you know kind of get behind and and which architecture path do I want to get behind"

这里形成了一个残酷的循环：企业因中央化而失败 → 失败产生创伤 → 创伤导致犹豫 → 犹豫使扩散更慢。Casado称之为"bruising"——企业需要先克服第一轮AI失败的心理创伤，才能发起第二次尝试。

---

# 二、Agent是软件还是员工？一场架构哲学的根本分歧

这是本场对话中最尖锐的分歧点，也是最有思想密度的段落。

Martin Casado提出了一个颠覆性的架构原则：不要把AI当成软件来集成，把Agent当成用户。这意味着不是改造你的产品去融合AI能力，而是让你的产品可以被Agent以CLI/API的方式消费，Agent自己选择怎么用。Casado称之为"very very significant architectural and mental shift"。

> **[9:50]** "like just view it as a user. And so, instead like take your product, make it a CLI tool, and then have the AI be an agent that actually uses it. So, you're not fusing the two, you're just making it more useful for AI."

Casado随后把这个原则推到了一个更根本的"端到端论证"（end-to-end argument）：LLM是非确定性的、智能的、处理长尾复杂性的——这些恰好是人类的特点。而我们花了40年构建的界面、流程和设计，都是用来应对"混乱的人类"的。所以，如果Agent更像人，那就应该让人来借用我们为人而非为软件建立的机制。

> **[20:53]** "The end-to-end argument is these LLMs are non-deterministic. They are smart. They deal with the long tail of complexity. And it turns out those are all things humans do, too. And we've spent 40-years building interfaces, processes, and design to deal with messy humans."

Casado甚至提出了"Agent入职"的概念——Agent来了先去orientation，CEO给它讲企业文化，每个部门做pitch介绍自己的工作。这不是玩笑，而是对Agent治理框架的严肃提案：因为Agent有熵、有不可控性，所以必须用我们为人建立的流程来管理它。

> **[22:40]** "Hey, I listen, Aaron, I am all for agent onboarding. Like, you know, the agent comes, and it goes to orientation, and then the CEO gives it the culture discussion, and then every I'M NOT KIDDING. NO, YOU'RE PROBABLY RIGHT. I MEAN, THAT'S EVERY DEPARTMENT EVERY DEPARTMENT does their pitch, like this is what we do."

Levie部分同意，但指出了Agent相对人类的两个结构性不对称：优势是可以并行、无限规模地工作；劣势是"不知道该去拍谁的肩膀"——那些组织中未文档化的人际关系网络，Agent无法访问。

> **[22:28]** "You treat these as as people accessing systems and tools, but they are at a they're both at an a massive advantage that they can work in parallel in at you know, at infinite scale, and they're at a disadvantage in that they don't know who to tap on the shoulder."

Sinofsky用了一个绝妙的类比来支持Casado的论点：人形机器人为什么是最优形态的机器人？因为整个物理世界都是为人体设计的。CES上的Roomba式小机器人进不了电梯，因为没有API按电梯按钮——所以同一家公司专门发明了一个按按钮的装置。软件世界也一样：整个企业软件生态是为人类用户设计的，Agent最好的策略是直接借用这条路，而不是等所有系统都重新设计一个headless版本。

> **[23:24]** "it's the same argument that humanoid robots will will be the best kind of robot, which is we have a whole world designed for humans."

---

# 三、集成墙——AI不帮集成任何东西

Sinofsky在对话中反复锤击一个论点：Agent作为"用户"会遇到和人类用户完全一样的墙——权限边界。当你打电话给客服被转到另一个部门时，你碰到的不是技术问题，是组织边界。Agent如果只有你的权限，就会在每一个"嘿Sally，能把这个分享给我吗"的地方卡住。而且，Agent不像人类，它不知道该去找Sally。

> **[12:03]** "any enterprise of a thousand people or more or that's older than 10 years is just a massive stuff that's sitting there waiting to be integrated. And and you can't just say it's going to integrate. AI actually doesn't help to integrate anything."

Levie把这个观察推进了一步：这就是为什么OpenAI与Accenture、Deloitte的合作是最的公告——大型企业需要经过变更管理、系统实施、技术集成，Agent才能真正运作。硅谷对此的嘲讽（"我们需要人来实施那些将取代人的Agent"）恰恰暴露了对企业现实的隔膜。

> **[17:16]** "going to have to go through that the change management, the systems implementation, the integration of technology for these agents to be able to go and work."

Levie预判，这种集成工作将持续数十年，对新一代服务商来说是巨大机会。Sinofsky补充了一个关键的警告：不要在这些项目失败时庆祝，因为它们一定会失败——原因是企业总是从最棘手的问题开始，而最棘手的问题往往恰恰是最不适合用AI去解决的系统。

这场讨论揭示了一个反直觉的结论：Agent的价值路径不是从"最难的问题"开始，而是从"信息获取"开始——先让Agent帮人在企业内部跨系统查找信息（这是AI第一次让企业内部搜索产生即时价值的时刻），等信息流打通了，再逐步给Agent加"行动按钮"。

> **[19:34]** "In fact, AI might be the first time that inside a company search can actually provide immediate value."

---

# 四、Headless SaaS的幻觉与Agent身份

Salesforce宣布全面headless是一个标志性事件，Levie将其视为风向标——Salesforce怎么走，企业软件就怎么跟。但Sinofsky立刻指出了一个被忽视的问题：Agent就是另一个license。它必须有自己的身份、自己的权限。如果让Agent借用人类的凭证，那是糟糕的安全实践。而如果给Agent独立的身份和权限，它永远不会拥有比其发起人更多的权限——它是组织中的一员，不是超级用户。

> **[27:20]** "Like you might be able to look and see who is on the account, but you don't need the up-to-date quota of those sales people and stuff, and that might be HR sensitive, and you should probably have some other level to go see that. But as you go down the org, the agent is never going to have more permissions than the person who's getting it to go do something."

> **[27:40]** "And in fact, it's just going to be like a peer to somebody else in an organization."

这直接摧毁了"SASpocalypse"的叙事。Sinofsky说headless Salesforce让他觉得SASpocalypse比原来更蠢——原来觉得蠢，现在发现更蠢。因为Agent不会减少SaaS的席位数，反而会爆炸性地增加：每个员工可能有一个或多个Agent，每个Agent是一个独立的席位，而它的API调用量可能是人类的500倍。

> **[28:16]** "that whole discussion about headless for me made the SASpocalypse seem even dumber than it was already, and it was already dumb."

Casado在这个议题上提出了全场最大胆的反论：headless可能根本行不通。他举了OpenClaw的例子——人们用Mac mini跑OpenClaw，第一是为了iMessage（没有headless版本），第二是因为headless浏览器被网站的反爬虫机制挡住。模型是在人类使用真实应用的场景下训练的，不是在API上训练的。所以Agent最自然的交互方式不是调用API，而是像人一样使用界面。

> **[29:28]** "if you've tried to use headless browsers with agents, the problem is is all of the websites um have anti-scraping measures. So they don't work."

Levie试图调和两方：Agent会优先使用API（效率更高），在没有API时才回退到浏览器。但他承认这是一个时间维度的问题——今天的API和MCP还很不成熟，未来会演化出更面向Agent工作流的新型接口。

---

# 五、代码越多工程师越多——AI生产力悖论

Casado在讨论Agent对SaaS系统的500倍负载冲击时，提出了一个关于AI代码质量的尖锐观察：用AI写代码，代码质量会随时间显著劣化——你引入的问题和解决的问题一样多。而我们还不知道如何管理这种熵增。

> **[42:00]** "when you code um with AI, your code kind of gets worse over time pretty materially. And so, it's almost like you're introducing as many problems as you are solutions. And I don't think we've actually figured out how to manage that."

Sinofsky立即将这个观察与"大型企业的轮子随时要掉下来"的日常焦虑联系起来——大公司里的人每天醒来都觉得今天是系统崩溃的一天，所以到处都是约束。这些约束不是官僚主义的无聊产物，而是防止整个东西内爆的必要机制。而硅谷的"vibe coding"人群之所以觉得没问题，是因为他们从未生活在一个约束是为了防止全面崩塌的环境中。

> **[43:53]** "I'm getting fired by the 5:00 and we whatever started what I left yesterday thinking we were 3 months late and it's we're now 9 months late." And that's a typical day. And so, but the reason that that doesn't happen is because you put constraints all over the place. Exactly."

> **[44:11]** "Which is exactly why Gilfoyle can't work at a big company because he he thinks he knows and it's also why all the the one-shotting vibe coding kind of people have no problem saying it's fine because they've never had to live in an environment where the constraint was to prevent the whole thing from imploding."

Levie用Box自身的实践验证了这一点：AI构建了80-90%的功能代码，但发布被安全审查拖慢。所以Box不声称10倍生产力提升，而是务实的2-3倍——因为你仍然被审查流程限速。

> **[45:39]** "AI built probably 80 to 90% of the feature and the the thing that slowed down the release of it was we have to do a full security review"

Casado把这个逻辑推到了一个更深的层面：AI迎合的是人类"想要高效"的需求，但我们可能正在制造大量额外工作。这与"代码越多工程师越多"的悖论完美契合——AI写出更多代码，系统变得更复杂，就需要更多工程师来维护更复杂的系统。

> **[51:14]** "And computers actually only made it more complicated, more comprehensive, and thus created even more jobs because because of that complexity that that we introduced. And and you can just sort of see how easy this is to show up in so many areas of work is like we can just now we can afford to make things more complex. And so if if you make things more complex, then actually you eventually still run into now new constraints of who can understand that complexity. And and and and so like, you know, it's like to me it's like the funniest concept that the more code we write, the less we would need engineers."

> **[51:46]** "It'd be the opposite because because now your systems are even more complex than before, which means that you're going to be running into even more challenges of when you need to do a system upgrade or when there's downtime and you have to figure out like what Well, how do I fix that problem or when there's a security incident? Uh uh And so, yeah, I mean, this is this is uh this is like we're just getting started with the jobs on this front."

---

# 六、就业扩张而非萎缩——复杂性的自我繁殖

对话的最后部分，三人从代码扩展到了更广泛的就业讨论。Levie明确表达了对就业的乐观——不是因为他低估了AI的能力，而是因为他理解了复杂性的运作方式。人类仍然需要在流程的某个位置——也许抽象层级更高了，但你仍然需要人发起流程、审查流程、整合结果。

> **[47:52]** "we've gotten it wrong on on thinking you know all the places where you're going to remove humans from this because you still need a human in that you know somewhere in the loop."

Sinofsky拿出了他的视觉道具——Jeremy Rifkin 1995年的《工作的终结》（The End of Work），出版六个月后互联网爆发。整本书的论点是技术革命完全没带来生产力提升，但因为经济停滞，工作会消失。Sinofsky称之为"第一次听觉得蠢，回去想想发现更蠢"的典型案例。

> **[48:20]** "Um and so that creates just still a tremendous amount of opportunity in jobs across these organizations. Oh, let me I have to jump in cuz I I have I have a whole bunch of like visual aids I brought today to make it exciting. We got you got a bunch of comments um on the MTS live thing about people agreeing with you. So I don't want to let that slide because you know we complain about not agreeing with you but but like here to your point to your point this was a book in the 80s called the end of work. Yeah. And and I this so actually sorry it was in the 90s."

> **[48:51]** "It it it came out like six months before the internet hit."

他用律师行业的演变做了解剖：1981年《时代》杂志报道计算机将消灭纸张工作，律师曾经不亲自打字——由paralegal代劳。哈佛学生把电脑带进法学院被赶出去。而现在，律师数量比30年前多得多，每个律师都是"计算机化的律师"——引文来自互联网、用track changes修改合同。计算机没有消灭律师，而是让法律工作的复杂性扩张了，从而需要更多律师。

> **[55:54]** "And so this is I'm lowering it so you guys can see. Yeah, yeah, yeah, yeah. So they brought that's a original laptop in there in the early 1980s. And they brought they brought this computer into the classroom and then they got thrown out for using it and but they were literally they used to used to do law school and you'd write the essays in longhand in a book and then the professor would have to read them. And now of course you just type them and you have access to the database of all the citations, but that's exactly like nobody deals with a lawyer who isn't in track changes with their with your contract. Right."

> **[56:23]** "And and I last I checked there are way more lawyers today than there were 30 years ago. And they all are every human lawyer you talk to is a computerized lawyer. Their citations come from from the internet, their their information in the brief comes and they type the brief."

Levie把论点推到了最远处：AI原生公司正在疯狂招聘，基础设施公司业务飙升——因为软件比以往更多了。他特别指出硅谷的一个近视错误：把"工程工作"等同于"在Google或社交网络工作"。John Deere需要智能拖拉机算法，Caterpillar需要AI系统，Eli Lilly需要设计更多药物——AI让这些传统公司也能拥有大量软件，而每一块新软件都需要有人用Claude Code、Codex、Cursor来构建和维护。

> **[53:34]** "They're going to now have the next set of engineers that are going to use Claude Code and Codex and Cursor to be able to automate even more of of their businesses"

三人的共识清晰：我们处于一个扩张期，而非收缩期。AI不是在取代工作，而是在使复杂性成为可负担品——而复杂性一旦成为可负担品，就会自我繁殖，直到再次触及人类认知的新边界。

---

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### Software 3.0的维护悖论——AI代码的熵增是可管理的工程问题还是结构性无解？
**← [[Andrej Karpathy—从 Vibe Coding 到 Agentic Engineering]]**
- 本文件论点：Casado观察到"用AI写代码，代码质量随时间显著劣化，引入的问题和解决的问题一样多"（[42:00]），Levie补充Box的实践是2-3倍而非10倍提升，因为安全审查成为新瓶颈（[45:39]-[46:09]）
- 对方论点：Karpathy提出Software 3.0范式（用自然语言编程），代码的维护成本从"理解代码逻辑"转移到了"理解prompt意图"，而prompt的语义漂移比代码bug更难追踪
- 关联逻辑：两方都在描述同一现象的不同切面——AI生成的产物（代码或prompt）都引入了一种新的熵：不是传统意义上的bug，而是意图与执行之间的语义间隙。Casado从企业运营角度看到这种熵在组织层面的放大（审查流程成为瓶颈），Karpathy从开发者角度看到这种熵在个人层面的表现（prompt的不可版本化）。把两者叠放，可以看到AI生产力悖论的完整图景：AI在微观层面加速生产，但在宏观层面加速复杂性积累，而人类审查是当前唯一的熵减机制——这就是为什么"代码越多工程师越多"不是悖论，而是热力学必然。

### 验证瓶颈的三层递进——Agent的身份问题是最底层的验证困境
**→ [[Terence Tao- How the world's top mathematician uses AI]]**
- 本文件论点：Sinofsky论证Agent必须是独立license、独立身份、独立权限，不能借用人类凭证（[26:24]-[28:42]），否则"获得一个知道你所有不该知道的事情的超级Agent"成为安全灾难
- 对方论点：Tao指出数学验证的困难在于证明的正确性不能被简化为计算；Dario指出AI系统的验证需要新的"可解释性"范式；Sutton指出真正的验证瓶颈在于"我们没有足够的专家来验证AI的输出"
- 关联逻辑：三者的递进关系是：Tao描述的是逻辑层验证（证明是否正确），Dario描述的是系统层验证（AI行为是否可解释），而Sinofsky/Levie描述的是组织层验证（Agent是否被授权执行其行为）。Agent身份问题之所以是最底层的验证困境，是因为它先于所有其他验证——在你能验证Agent做了什么之前，你必须先确认Agent是谁。而当Agent的行为是非确定性的（Casado的end-to-end argument），传统的RBAC/ACL模型就失效了：你无法对"一段话里的一个数字"做行级权限控制。这意味着验证瓶颈从"我们能信任AI的输出吗"递进到了"我们能在组织结构中为AI分配可验证的身份吗"——后者是一个全新的问题域。

### Scaling天花板的具体机制——500倍负载是企业SaaS的涌现瓶颈
**→ [[Ilya Sutskever- 从 Scaling 时代回到 Research 时代]]**
- 本文件论点：Sinofsky提出如果每个员工有一个Agent，SaaS系统将面临500倍于人类的负载冲击，"那个SaaS产品会崩溃"（[39:38]-[40:38]）；Casado反驳说这是"标准计算机科学"问题，缓存和架构可以解决（[40:48]-[41:16]）
- 对方论点：Ilya认为scaling天花板来自数据墙（高质量数据耗尽）；Dario认为来自compute瓶颈和diminishing returns；Hassabis认为来自算法效率而非数据量
- 关联逻辑：Sinofsky描述的500倍负载冲击是scaling天花板在企业软件层的一个具体涌现形式——不是模型本身的scaling问题，而是模型能力向系统转化的scaling问题。当Agent从"偶尔使用"变成"持续并行运行"时，SaaS系统的架构假设（人类速度的API调用、人工操作间的自然间隔、一人一session）全部被打破。这与Ilya的数据墙形成有趣的对偶：Ilya的天花板是"训练数据不够"，Sinofsky的天花板是"推理负载太大"；一个是scaling的输入瓶颈，一个是scaling的输出瓶颈。Casado的"标准CS问题"反驳是否成立，取决于Agent调用的模式——如果是读多写少，缓存确实可以解决；但如果涉及可变共享状态（正如Casado自己承认的），那么500倍负载就不是缓存能消化的，而是分布式系统一致性的经典难题重新浮现。

### 凡人vs不朽的架构之争——Agent入职是人本架构的延续还是过渡形态？
**→ [[Geoffrey Hinton 2022- 反叛自己]]**
- 本文件论点：Casado的"Agent入职"框架（[22:40]）将Agent嵌入人类组织流程——orientation、权限、文化讨论——本质上是用"凡人架构"（有限权限、需要入职、受组织约束）来管理AI
- 对方论点：Hinton主张mortal computing（硬件即软件、权重即知识、断电即死亡），Jensen主张immortal computing（GPU集群上永恒运行的权重），Musk主张AI需要物理锚定（Neuralink脑机接口）
- 关联逻辑：Casado的"Agent入职"在组织架构层面复现了Hinton的mortal computing哲学：Agent不是一个不朽的全知系统，而是一个受限的、有边界的、需要被"社会化"的实体——它有自己的邮箱、自己的权限、自己的部门归属。这与Jensen的"不朽架构"形成直接对抗：在Jensen的世界里，AI是一个在GPU集群上永恒运行的超级智能；在Casado的世界里，AI是组织中一个需要参加orientation的新员工。两者不是技术选择，而是治理哲学：你到底想建造一个全能的Oracle，还是想雇佣一批受限的worker？把Casado和Hinton放在一起看，可以发现一个深层共鸣——他们都认为智能的有效性不来自于其"不朽性"，而来自于其"嵌入性"：mortal computing的价值在于硬件与知识的共生，Agent入职的价值在于AI与组织流程的共生。这暗示着企业AI的终局可能不是"一个超级Agent"，而是"一群入职了的受限Agent"。

---

**元信息**
```plaintext
标题: Box CEO on AI Agents & Why Enterprise Can't Keep Up | a16z
频道: a16z
发布时间: 2026-04-28
时长: 58min
YouTube: https://www.youtube.com/watch?v=dvVbA9OcBqs
对话者: Aaron Levie (Box CEO), Steven Sinofsky (a16z), Martin Casado (a16z)
分析时间: 2026-06-10
```
