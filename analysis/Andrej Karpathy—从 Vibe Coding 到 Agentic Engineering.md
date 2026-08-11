---
title: Andrej Karpathy：从 Vibe Coding 到 Agentic Engineering
source: feishu
feishu_doc_id: JO4bd3smcoBSkCx0YtUcliTRnnb
tags:
  - kol情报
status: canonical
dedup_note: 中文完整分析 + 已合并英文版独有内容（原英文重复文件已删除）
created: 2026-06-09
order: 20
---

[deprecated] docs +fetch is using the v1 API. Check the installed lark-doc skill first; if it is not the v2 skill, run `lark-cli update` to upgrade skills.
# Andrej Karpathy：从 Vibe Coding 到 Agentic Engineering（AI Ascent 2026）

> **You can outsource your thinking but you can't outsource your understanding.**
>
> —— Andrej Karpathy, AI Ascent 2026
>
> 视频链接：https://www.youtube.com/watch?v=96jN2OCOfLs

2026年4月，Sequoia Capital 的 AI Ascent 大会上，Stephanie Zhan 与 Andrej Karpathy 进行了约30分钟的深度对话。Karpathy 的核心判断：我们正在经历一次计算范式的根本性切换——从写代码（Software 1.0）到训练模型（2.0）再到用 prompt 驱动 LLM（3.0）。这不是加速旧范式，是旧范式里的很多产品不该存在。

他提出三个关键区分：Vibe Coding 抬地板（人人能写），Agentic Engineering 保天花板（专业质量不降），Jagged Intelligence 解释为什么模型同时能重构10万行代码又告诉你走路去洗车。他把 LLM 称为「鬼魂」而非「动物」——统计模拟实体，没有内在动机，骂它没用。

# 一、Software 3.0：不是更好的软件，是新的计算机

## 1.1 三层范式再定义

Karpathy 的三层范式是他的老框架，但这次他给出了更锋利的版本——Software 3.0 不是一个「更快的编程方式」，而是一个完全不同的计算架构。

• Software 1.0：人写显式规则（代码），计算机执行。编程 = 写逻辑。

• Software 2.0：人准备数据集 + 定义目标，神经网络学习权重。编程 = 排列数据和架构。

• Software 3.0：人写 prompt / 构建上下文，LLM 解释并执行。编程 = 设计 prompt 和 context window。LLM 是解释器，context window 是你的杠杆。

**关键洞见：Software 3.0 不是让 Software 1.0 更快，而是让很多 Software 1.0 产品不再需要存在。**
```plaintext {wrap}
[2:43] Software 1.0, I'm writing code. Software 2.0, I'm actually programming by creating data sets and training neural networks. And then what happened is that basically if you train one of these GPT models or LLMs on a sufficiently large set of tasks... these actually become kind of like a programmable computer in a certain sense. So software 3.0 is kind of about your programming now turns to prompting and what's in the context window is your lever over the interpreter that is the LLM.
```

## 1.2 MenuGen 案例：一个产品被范式切换消灭的全过程

Karpathy 自己做了一个叫 MenuGen 的 app——拍餐厅菜单照片，OCR 识别菜品名，用图像生成模型生成菜品图片，重新渲染菜单。这是经典的 Software 1.0/2.0 混合架构：OCR + API 调用 + 前端渲染。

然后他看到了 Software 3.0 版本：把菜单照片直接给 Gemini，说「用 NanoBanana 把菜品叠加到菜单上」，模型直接输出一张新图片——原菜单照片上每个位置都渲染了对应菜品的图像。

他的结论：MenuGen 的整个 app 不该存在。这不是「加速了 MenuGen 的开发」，而是「MenuGen 这个产品形态本身被淘汰了」。中间层的 app 被绕过——prompt 即产品。
```plaintext {wrap}
[5:37] I saw the software 3.0 version of this which blew my mind — literally just take your photo, give it to Gemini and say use NanoBanana to overlay the things onto the menu. [...] All of my MenuGen is spurious. It's working in the old paradigm. That app shouldn't exist. [...] The software 3.0 paradigm is a lot more raw. Your neural network is doing more and more of the work and your prompt or context is just the image and the output is an image and there's no need to have any of the app in between.
```

**这揭示了一个产品信号：凡是「用确定性规则穷举环境差异」的产品逻辑，都是 Software 3.0 的消灭对象。**

## 1.3 OpenClaw 安装案例：Shell Script 的终结

传统软件安装是 shell script——因为要适配不同平台和环境，脚本会膨胀得极度复杂。OpenClaw 的安装方式：给你一段文本，你 copy paste 给 agent，agent 看你的环境自己搞定。你不需要在 script 里穷举所有情况，因为 agent 自带智能去处理边缘 case。
```plaintext {wrap}
[4:01] When you want to install OpenClaw, you would expect that normally this is a bash script, a shell script. But these shell scripts usually balloon up and become extremely complex. But the thing is you're still stuck in a software 1.0 universe of wanting to write the code. And actually the OpenClaw installation is a copy paste of a bunch of text that you're supposed to give to your agent. [...] The agent has its own intelligence that it packages up and then it follows the instructions and it looks at your environment and it performs intelligent actions to make things work and it debugs things in the loop.
```

## 1.4 新机会不只是加速旧事物

Karpathy 强调：人们容易把 Software 3.0 理解为「旧事物变快」，但真正令人兴奋的是那些以前根本不可能存在的新机会。不只是代码——任何信息处理都有被自动化的可能。他用 LLM knowledge base 项目举例：这不是传统意义上的程序，以前没有代码能基于一堆事实创建知识库，现在你可以让 LLM 重组、重排信息，创造新的有意义的东西。
```plaintext {wrap}
[6:33] It's not just about programming and programming becoming faster. This is more general information processing that is automatable now. [...] Previous code worked over structured data. But for example with my LLM knowledge base project — basically you get LLMs to create wikis for your organization. This is not even a program. This is not something that could exist before because there was no code that would create a knowledge base based on a bunch of facts. But now you can just take these documents and recompile them in a different way and reorder them and create something that is new.
```

## 1.5 神经计算机的终极形态

Karpathy 做了一个更大胆的外推：50-60年代，人们不确定计算机到底是「计算器」还是「神经网络」。我们走了计算器路线，然后神经网络作为虚拟化程序跑在现有计算机上。但他认为这一切会翻转——神经网络成为宿主进程，CPU 降级为协处理器。FLOPs 分布已经在验证这个方向——intelligence compute 占比正在成为主导。
```plaintext {wrap}
[8:40] In the early days of computing people were a little bit confused as to whether computers would look like calculators or computers would look like neural nets, and in 50s and 60s it was not really obvious which way would go. [...] Neural nets are currently running virtualized on existing computers but you could imagine a lot of this will flip and the neural net becomes kind of like the host process and the CPUs become kind of like the co-processor.
```

# 二、Vibe Coding vs Agentic Engineering：地板与天花板

## 2.1 Vibe Coding = 抬地板

Vibe Coding 的本质是「让所有人都能写出能跑的软件」。门槛降到零，任何人都可以让 agent 帮自己实现想法。Karpathy 自己的体验：2025年12月是一个拐点——之前 agent 写的代码块经常要手动修，之后他发现代码块一直没问题，信任不断升级，直到他不记得上次纠正 agent 是什么时候。
```plaintext {wrap}
[1:22] I just started to notice that with the latest models the chunks just came out fine and then I kept asking for more and it just came out fine and then I can't remember the last time I corrected it and then I just trusted the system more and more and then I was vibe coding. [...] I do think that it was a very stark transition.
```

但他强调：Vibe Coding 有一个结构性问题——它不负责质量。你可以 vibe coding 出任何东西，但你也可能引入安全漏洞、写出脆弱的抽象、产生大量 copy-paste 膨胀。

## 2.2 Agentic Engineering = 保天花板

Agentic Engineering 是 Karpathy 给出的新命名。核心命题：你有一群能力极强但行为尖刺、有些随机、偶尔犯低级错误的实体（agent），你如何协调它们加快产出而不降低质量？
```plaintext {wrap}
[16:03] Vibe coding is about raising the floor for everyone in terms of what they can do in software. The floor rises, everyone can vibe code anything. But then agentic engineering is about preserving the quality bar of what existed before in professional software. You're not allowed to introduce vulnerabilities due to vibe coding. You're still responsible for your software just as before, but can you go faster? [...] How do you coordinate them to go faster without sacrificing your quality bar?
```

**他明确说这是一个工程学科——不是 vibe，是 discipline。**

**关键区分：**

• Vibe Coding：产出 = 能跑就行。人不再读代码细节。

• Agentic Engineering：产出 = 专业级质量 + 极速。人仍然负责 spec、设计、审美判断、安全性。Agent 做 fill in the blanks。

## 2.3 10x 工程师已过时

Karpathy 说「10x 工程师」不再描述 agentic engineering 带来的加速——不是10倍，是远超10倍。擅长 agentic engineering 的人，产出峰值远超传统意义上的10x。
```plaintext {wrap}
[17:01] People used to talk about the 10x engineer previously. I think that this is magnified a lot more. 10x is not the speed up you gain. And it does seem to me like people who are very good at this peak a lot more than 10x from my perspective right now.
```

## 2.4 招聘也必须重写

大多数公司还没重构招聘流程来识别 agentic engineering 能力。如果还在出算法题，你在用旧范式筛选旧能力。他的示例：给候选人一个大项目（如 Twitter clone），要求完整部署，然后用 10 个 Codex 攻击——如果攻不破，说明 agentic engineering 是真的。
```plaintext {wrap}
[18:44] Most people have still not refactored their hiring process for agentic engineer capability. If you're giving out puzzles to solve, this is still the old paradigm. Hiring has to look like: give me a really big project and see someone implement that big project — let's say a Twitter clone for agents — make it really good, make it really secure, and then have some agents simulate some activity and then I'm going to use 10 Codex to try to break your website. And they should not be able to break it.
```

# 三、Jagged Intelligence：模型为什么同时是天才和白痴

## 3.1 锯齿状能力的根源

Karpathy 用「Jagged Intelligence」描述一个他一直在试图理解的现象：为什么 SOTA 模型能重构 10 万行代码库、发现零日漏洞，同时又告诉你应该走路去 50 米外的洗车店？
```plaintext {wrap}
[11:08] I want to go to a car wash to wash my car and it's 50 meters away. Should I drive or should I walk? And state-of-the-art models today will tell you to walk because it's so close. How is it possible that state-of-the-art Opus 4.7 will simultaneously refactor a 100,000 line codebase or find zero day vulnerabilities and yet tells me to walk to this car wash? This is insane.
```

**他的诊断框架——锯齿状能力的成因是两个变量的组合：**

1) 可验证性（Verifiability）：可验证域有 RL reward signal → 模型在此被强化 → 能力尖刺。不可验证域缺乏 reward → 停滞。
2) Lab 投入（Labs Care）：实验室选择把哪些可验证域放进 RL 训练。代码有价值 → 大量 RL 环境。某些可验证域虽然存在但不够重要 → 被忽略。

**即：能力尖刺 = 可验证 + Lab 投入了资源。能力低谷 = 不可验证 或 可验证但 Lab 没管。**
```plaintext {wrap}
[10:24] When frontier labs are training these LLMs, these are giant reinforcement learning environments. They are given verification rewards and then because of the way that these models are trained they end up basically progressing and creating these like jagged entities that really peak in capability in kind of like verifiable domains like math and code and stagnate and are a little bit rough around the edges when things are not in that space.
```

## 3.2 创始人机会：在 Lab 的盲区建 RL 环境

Karpathy 暗示存在一些高价值可验证域，Lab 还没有放进去——这是创业者的机会。如果你在自己的领域可以构造 RL 环境 + 多样化数据集，你可以自己 fine-tune，获得 Lab 不会帮你做的能力。他留了个悬念——说有一个领域非常值得做但不愿在台上透露。
```plaintext {wrap}
[14:05] Verifiability makes something tractable in the current paradigm because you can throw a huge amount of RL at it. If you are in a verifiable setting where you could create these RL environments or examples then that actually sets you up to potentially do your own fine tuning and you might benefit from that. [...] There is one domain that I think is very... Sorry, I don't want to give away the answer.
```

## 3.3 Chess 案例：能力不是自然涌现的，是数据注入的结果

GPT-3.5 到 GPT-4，国际象棋能力大幅提升。很多人以为是模型能力自然进步，实际上是因为有人把大量棋谱数据加入了预训练集。你以为的能力涌现，很多时候只是数据分布的变化。
```plaintext {wrap}
[12:22] From GPT 3.5 to GPT4 people noticed that chess improved a lot and I think a lot of people thought oh well it's just a progression of the capabilities. But actually a huge amount of data of chess made it into the pre-training set and just because it's in a data distribution the model improved a lot more than it would just by default.
```

**实操含义：你略受 Lab 数据选择的摆布——你用的是他们给你的东西，这个东西没有说明书。你不知道哪些电路被强化了、哪些没有。如果你在自己的应用里处于 RL 覆盖的电路，飞；如果不在此电路，你得自己做 fine-tuning。**
```plaintext {wrap}
[12:50] Someone at OpenAI decided to add this data and now you have a capability that just peaked a lot more. We are slightly at the mercy of whatever the labs are doing, whatever they happen to put into the mix. And you have to actually explore this thing that they give you that has no manual. If you're in the circuits that were part of the RL, you fly. And if you're in the circuits that are out of the data distribution, you're going to struggle.
```

# 四、Ghosts not Animals：LLM 是什么决定你怎么用它

Karpathy 试图用「鬼魂 vs 动物」这个隐喻来建立对 LLM 的心智模型。

动物智能：由进化塑造，有内在动机（好奇、恐惧、饥饿、自尊），有连续的意识体验，被骂会有反应。

鬼魂（LLM）：由数据 + reward function 塑造，没有内在动机，没有连续意识，是统计模拟电路——底层是 pre-training 的统计性，上面 bolt-on 了一层 RL 增加了一些结构。你骂它没用，你夸它也没用。它是被召唤出来的实体——给一个 prompt，它出现；不给，它不存在。
```plaintext {wrap}
[24:00] These things are not animal intelligences. Like if you yell at them, they're not going to work better or worse. It doesn't have any impact. It's all just kind of like these statistical simulation circuits where the substrate is pre-training so like statistics and then but then there's RL bolting on top. It's more just being suspicious of it and figuring out over time.
```

Karpathy 坦承这个框架目前更多是哲学性的——他还没推导出「基于此框架的5个实操改进」，但它改变了你对系统的预期和交互方式。你不会对一个鬼魂生气，也不会期待它自己想做得更好——你需要改的是 prompt、context、reward，而不是态度。

# 五、Agent-Native 基础设施：一切都要重写

**Karpathy 最大的日常痛点：所有工具和文档都是给人类写的，不是给 agent 写的。**

## 5.1 文档的范式切换

他的原话：为什么人们还在告诉我该做什么？我不想做任何事。什么是应该 copy paste 给 agent 的文本？每次文档说「去这个 URL」「点击这个设置」，他的反应是沮丧——agent 不该需要看面向人类的 UI。
```plaintext {wrap}
[25:41] Everything is still fundamentally written for humans. I still use most of the time when I use different frameworks or libraries, they still have docs that are fundamentally written for humans. This is my favorite pet peeve. Why are people still telling me what to do? I don't want to do anything. What is the thing I should copy paste to my agent?
```

**文档应该从「教人怎么做」变成「给 agent 一个可以直接执行的 prompt」。这是产品形态的根本变化。**

## 5.2 部署的范式切换

MenuGen 开发中最痛苦的不是写代码，是部署——在 Vercel 上配置 DNS、各种服务的 settings、把东西串起来。Karpathy 希望的未来是：给 agent 一句 prompt「build MenuGen」，agent 自己搞定部署、配置、上线，人什么都不用碰。
```plaintext {wrap}
[26:30] A lot of the trouble was not even writing the code for MenuGen, it was deploying it in Vercel because I had to work with all these different services and I had to string them up and I had to go to their settings and the menus and configure my DNS and it was just so annoying. I would hope that I could give a prompt to an LLM: build MenuGen, and then I didn't have to touch anything and it's deployed.
```

## 5.3 Agent-to-Agent 交互

Karpathy 预测的终态：人和组织都会有 agent 代表。「让我的 agent 和你的 agent 谈」来协调会议、细节、协作。这是从「人-人交互」到「agent-agent 交互」的迁移。
```plaintext {wrap}
[27:30] I do think we're going towards a world where there's agent representation for people and for organizations. I'll have my agent talk to your agent to figure out some of the details of our meetings or things like that.
```

# 六、人类不可外包的能力：理解、品味、判断

## 6.1 Agent 是实习生，你是导演

当前的 agent 像实习生——recall 极好、速度极快，但缺乏审美判断和常识。你仍然是导演——负责 spec、设计、美学判断、安全性。

他举了一个具体例子：MenuGen 的用户系统——Google 登录用一个邮箱，Stripe 支费用另一个邮箱。Agent 用邮箱地址做用户关联，但两个邮箱可以不同。这种「用 email 做 cross-correlation」的逻辑是 agent 不会质疑的，因为它缺乏对业务语义的理解。你需要说的是「必须用 unique user ID 来关联一切」。
```plaintext {wrap}
[19:34] The agents are kind of like these intern entities. You basically still have to be in charge of the aesthetics, the judgment, the taste and a little bit of oversight. [20:00] My agent actually tried to assign it using the email address from Stripe to the Google email address — there wasn't a persistent user ID. It was trying to match up the email addresses, but you could use different email address for your Stripe and your Google and basically would not associate the funds. Why would you use email addresses to try to cross-correlate the funds?
```

他不赞同 plan mode 作为唯一的协作方式——更广义的做法是和 agent 一起设计详细 spec（可能就是文档本身），你负责顶层分类和 oversight，agent 做底层填充。
```plaintext {wrap}
[20:43] I don't even like the plan mode. I think there's something more general here where you have to work with your agent to design a spec that is very detailed and maybe basically the docs and then get the agents to write them and you're in charge of the oversight and the top level categories, but the agents are doing a lot of the under the hood.
```

## 6.2 API 细节已外包，底层理解不能丢

Karpathy 自己的体验：他不再记得 PyTorch 里 keepdims 还是 keepdim，dim 还是 axis，reshape 还是 permute。这些 API 细节已经外包给 agent。但他仍然必须知道底层有 tensor、有 view、有 storage——复制 storage 比创建 view 更贵。如果你不理解这些底层概念，你无法判断 agent 的代码是否在浪费资源。
```plaintext {wrap}
[21:09] There's a ton of details between PyTorch and NumPy and pandas for all the different little API details. I already forgot about the keepdims versus keepdim or whether it's dim or axis or reshape or permute or transpose. I don't remember this stuff anymore because you don't have to. This is the kind of details that are handled by the intern because they have very good recall. But you still have to know for example that there's underlying tensor, there's an underlying view and then you can manipulate view of the same storage or you can have different storage which would be less efficient.
```

## 6.3 品味和判断为什么还没被模型学会

Karpathy 承认模型产出的代码经常让他「有点心梗」——bloat、copy-paste、脆弱的抽象、看起来能跑但很恶心。他试图让 LLM 做 microGPT 那样的极致简化项目，模型完全做不到——「感觉你在 RL 电路之外，在拔牙」。原因：品味/简化不在 RL reward 里。但这不是根本性障碍——只是 Lab 还没做。
```plaintext {wrap}
[22:25] When you actually look at the code, sometimes I get a little bit of a heart attack because it's not like super amazing code necessarily all the time and it's very bloaty and there's a lot of copy paste and there's awkward abstractions that are brittle and like it works but it's just really gross. [22:55] The microGPT project where I was trying to simplify LLM training to be as simple as possible — the models hate this. They can't do it. I kept trying to prompt an LLM to simplify more, simplify more, and it just can't. You feel like you're outside of the RL circuits. It feels like you're pulling teeth.
```

## 6.4 「外包思考，不能外包理解」

访谈结尾最重要的判断。Karpathy 援引一条让他每天都想起的推文。含义：信息仍然必须经过你的大脑。你仍然是瓶颈——知道要建什么、为什么值得做、如何指挥 agent。LLM 不擅长理解，你仍然独特地负责理解。他用 LLM knowledge base 作为增强理解的方式——每次看到信息的不同投影，都获得洞察。
```plaintext {wrap}
[28:05] There was a tweet that blew my mind recently and I keep thinking about it like every other day. It was something along the lines of: you can outsource your thinking but you can't outsource your understanding. I'm still part of the system and I still have to somehow have information make it into my brain. I feel like I'm becoming a bottleneck of just even knowing what are we trying to build, why is it worth doing, how do I direct my agents. [...] The LLM certainly don't excel at understanding — you still are uniquely in charge of that.
```

---

# 可行动的信号

1. 如果你的产品是「用确定性规则穷举差异」的中间层 → 被淘汰风险极高。Software 3.0 绕过中间层。
2. 如果你在做开发者工具/文档 → 重新设计为 agent-first。核心交付物 = copy-paste prompt，不是人类教程。
3. 如果你在做模型能力产品 → 判断你处于哪条电路。在 RL 覆盖范围 = 飞；不在 = 你得自己做 fine-tuning，不能指望 Lab 帮你。
4. 如果你在招聘工程师 → 重构评估方式。算法题测的是旧能力。新能力 = 给大项目 + 部署 + 安全攻击测试。
5. 创业者机会窗口：在 Lab 还没覆盖的可验证域里建 RL 环境 + 自有数据集。Karpathy 暗示有高价值盲区存在。
6. 个人层面：理解不可外包。API 细节可以忘，底层概念不能丢。你可以用 agent 加速，但如果你不理解你在让 agent 做什么，你只是在更快地产出垃圾。

---

## 补充视角：英文版独有内容

> 以下内容来自同名英文版文件，为该版本中存在但中文完整分析中未覆盖的独特视角和细节。英文重复文件已删除。

### 1. "从未如此落后"的双重解读

Karpathy 描述 December 转折时，还表达了一种「从未如此落后」的复杂感受——同时是 exhilarating 和 unsettling。Exhilarating 在于个人产出爆炸——side projects 文件夹从空到满；unsettling 在于旧的技能体系正在失效。他特别强调：很多人 2025 年体验 AI 是 ChatGPT 式的对话，但如果你从 12 月重新审视，事情已经 fundamentally changed。错过这个转变的人，正在用旧范式衡量新现实。
```plaintext {wrap}
[1:52] but you really had to look again and you had to look as of December because things have changed fundamentally and especially on this like agentic coherent workflow that really started to actually work
```

### 2. 传感与驱动——Agent 的架构隐喻

Karpathy 用「传感器和执行器」描述 agent-native 的分解方式：把工作任务分解为对世界的感知（传感器）和行动（执行器），中间的信息结构要对 LLM 高度可读。这是从「UI 为人」到「API 为 agent」的底层思维切换——不是在旧界面上加一层，而是从根本上重新思考信息的输入输出结构。

### 3. LLM Knowledge Base 作为理解放大器

Karpathy 对 LLM knowledge base 项目如此兴奋的深层原因：它不是替代理解，而是增强理解。每当他读到一篇文章，他的 wiki 就在构建；每次他从一个不同的信息投影角度提问，他都获得新的洞见。本质上，这是对固定数据的合成数据生成——一种理解增强工具。
```plaintext {wrap}
[29:00] I really enjoy whenever I read an article I have my wiki that's being built up from these articles and I love asking questions about things... these are tools to enhance understanding in a certain way
```

### 4. 理解是人类结构性必需，不是暂时过渡

当前 LLM 的限制：它们不擅长理解（understanding），擅长执行（execution）。这意味着人类在「理解→指挥→验证」闭环中的角色不是暂时的过渡，而是结构性必需——至少在实验室把理解放进 RL 奖励之前。最激动人心的产品品类，是那些增强理解的工具。

### 5. 视频元数据

```plaintext
Channel: Sequoia Capital (AI Ascent 2026)
Published: 2026-04-29
Duration: 29min 49s
Views: 1,134,067
Interviewer: Stephanie Zhan (Sequoia Partner)
URL: https://www.youtube.com/watch?v=96jN2OCOfLs
```

---

# 元信息

来源：Sequoia Capital AI Ascent 2026

时间：2026年4月29日

对谈人：Stephanie Zhan (Sequoia Partner) x Andrej Karpathy (Eureka Labs founder, OpenAI co-founder, former Tesla AI head)

视频：https://www.youtube.com/watch?v=96jN2OCOfLs

整理时间：2026年5月27日


## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系
### Software 3.0的维护悖论
**→ [[Charlie Holtz- How Conductor CEO Sets Up His Team Of AI Agents]]**
- 本文件论点：Software 3.0：prompt成为编程语言，context window成为杠杆。旧范式的应用是spurious的
- 对方论点：代码是锯末，prompt才是资产。下一代模型出来时重跑prompt就能得到更好代码，旧代码自然淘汰
- 关联逻辑：Karpathy定义了范式（prompt=编程语言），Holtz实操了后果：既然prompt是程序，代码就是副产品。但Holtz没回答的问题是——当prompt变成程序，它是否也继承了程序的维护负担？87KB审美判决书给出了答案：是的
**← [[Charlie Holtz- How Conductor CEO Sets Up His Team Of AI Agents]]**
- 本文件论点：OpenClaw安装案例：shell script被agent指令替代——你不需要在script里穷举所有情况，因为agent自带智能去处理边缘case
- 对方论点：代码是锯末，prompt才是资产。下一代模型出来时重跑prompt就能得到更好代码
- 关联逻辑：Holtz的「prompt是资产」有一个隐含前提：prompt跨模型迁移时仍然有效。但Karpathy的OpenClaw案例暗示prompt也可能随范式切换而失效——shell script→agent text就是一次prompt的范式死亡

### Software 3.0的维护负担
**→ [[87KB 的审美判决书]]**
- 本文件论点：Software 3.0：prompt成为编程语言，context window成为杠杆
- 对方论点：87KB SKILL.md通过5轮迭代膨胀：AI不听指令→加更硬的指令→文档变长→AI读不到尾部→更多失败→加更多规则——Prompt Inflation Trap
- 关联逻辑：Karpathy说prompt是新编程语言，但87KB审美判决书展示了这种语言的维护噩梦：当prompt变成程序，它继承了程序的所有复杂性（bug→patch→文档膨胀→回归），但没有程序的任何工具支持（类型系统、debugger、单元测试）。这是Software 3.0尚未解决的工程问题

