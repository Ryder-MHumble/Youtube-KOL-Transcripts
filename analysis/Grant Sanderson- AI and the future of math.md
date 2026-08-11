---
title: "Grant Sanderson- AI and the future of math"
source: youtube
youtube_url: "https://www.youtube.com/watch?v=TfyPshgMbug"
transcript: "[[Grant Sanderson- AI and the future of math 逐字稿]]"
kol: Grant Sanderson
channel: Dwarkesh Patel
upload_date: "2026-07-01"
duration: "1:33:36"
tags:
  - kol情报
status: canonical
---

> AI 在数学上进步快，不只因为答案可验证，更因为数学可以低成本并行试错；真正难以自动化的是提出定义、选择研究方向和创造新概念，因为这些工作的价值验证可能晚到几十年甚至一个世纪。

**视频链接**：https://www.youtube.com/watch?v=TfyPshgMbug  
**对应逐字稿**：[[Grant Sanderson- AI and the future of math 逐字稿]]

## 概述

Grant Sanderson 没有把“AI 解出著名猜想”直接等同于通用智能，而是追问解法形态、验证周期和人类理解。数学能力本身是锯齿状的：同一项竞赛中，几何可以被暴力求解，组合问题仍可能困难；同一个正确证明，也可能是瞬间建立跨领域连接、搭建全新理论，或一条无人能消化的超长推导。

整场访谈最关键的贡献，是把“可验证任务”进一步拆成“可磨任务”。数学和代码不仅能判断对错，还能在隔离环境中无限生成 rollout、复制状态、并行探索。计算机使用同样容易验证结果，却受真实网站、反爬虫和高交互成本限制，因此不可磨。

Grant 也把 AI 数学的边界从证明推进到概念与解释。群论的价值经历百年才被物理和密码学验证，无法被短周期奖励捕获；写作和阐释又要求持续模拟读者心智。未来人类角色可能不再是证明者或解释者，而是选择值得关注的人、概念和研究路线的策展者。

## 主题脉络

1. 数学 benchmark 内部仍是锯齿前沿
2. 重大概念的验证回路可能长达百年
3. 证明正确、解释清楚与创造新定义是三种能力
4. 数学进步快的结构原因是可验证加可磨
5. 多 Agent 的优势来自主动制造不同上下文和启发式
6. 写作需要心智建模，逐 token 预测天然受上下文牵引
7. AI 可以路由知识，但人类仍负责策展和长期价值判断

## Benchmark 被跨过后，真正被测量的能力才开始显形

Grant 认为 IMO 的“秘密”是很多题型可以通过专项训练覆盖。

> **[1:32]** "The dirty secret with the IMO is that you really can train for a lot of them."

这意味着金牌不是单一创造力指标，而是几何、代数、数论和组合等技能按当年题目权重形成的结果。AI 在几何上的暴力搜索优势，不能直接外推到组合直觉或研究品味。

他也承认，当更高 benchmark 被跨过时，观察者会继续移动目标。

> **[7:24]** "First of all, I do want to point out that I'm totally moving the goalpost here."

这并不必然是守门。很多 benchmark 只有被模型攻克后，人们才发现它依赖的技能比原先想象得窄。更稳健的评估不是寻找一个“AGI 终极考试”，而是记录能力在任务分解、领域迁移、错误恢复和现实影响上的覆盖范围。

Grant 对 AI 的真正惊讶，不是它知识不足，而是拥有跨领域知识后仍很少发现“闪电式”连接。

> **[3:35]** "It's bizarre to have something with this superhuman breadth that knows all the fields so well, and yet isn't finding those lightning bolts that connect them."

这把问题从知识检索推进到结构发现：模型是否能识别两个领域共享的隐藏对象，并提出值得继续研究的关系。

## 最重要的数学工作往往没有及时奖励

群论是否是一个有生产力的概念，无法在 Galois 写下它时立即验证。其价值需要后续数学、物理和密码学共同兑现。

> **[13:17]** "If you wanted to do a verification loop on whether group theory is an interesting concept—was something useful done here, or why is this proof better?—potentially that verification loop is a hundred years long."

短周期奖励系统会偏好快速证明已有问题，而系统性低估定义新对象、重构问题空间和建立未来才有用的语言。Galois 生前得到的学术反馈甚至可能是负向的，但这不代表概念没有价值。

Grant 尝试用概念规模或压缩度作为“优雅”的代理奖励。

> **[23:22]** "So I wonder the extent to which you can give some kind of verifiable reward around not just whether you solved it or what it is solving, but around the smallness of the concepts required to do it."

压缩度可以奖励用少量概念解释大量现象，但仍无法替代长期价值。一个短理论可能优雅却与现实无关，一个复杂框架也可能因打开新研究方向而重要。科学 AI 需要同时优化即时正确性、概念压缩和长期影响，而不能把三者压成一个 reward。

## 证明、解释和定义不会按同一速度被自动化

Grant 明确区分证明与解释。

> **[32:49]** "There is a difference between proof and explanation, and I think you're getting at the importance of that distinction."

一个形式证明可以保证结论，却不一定告诉人类为什么成立、哪些结构可复用、如何迁移到新问题。反过来，清晰解释也不代表产生了原创数学。

传统数学信用集中在定理证明，但证明往往依赖此前创造的定义和概念。

> **[30:13]** "The theorem-proving stuff is what gets all the credit, but it's really a parasite on the coming-up-with-the-definition stuff."

当 AI 自动化证明，信用分配可能转向问题选择、定义创造、解释和策展。但 Grant 也修正了自己过去的判断：AI 可能不仅擅长证明，也会成为优秀解释者。

> **[34:52]** "I used to think that AIs would become these automated theorem provers, but the role of mathematicians was going to shift towards my job, explaining these things. Now I suspect that actually they'll also be quite good at doing that, probably better than most humans are at explaining and distilling."

人类的稳定位置因此不是某一种固定技能，而是承担价值判断和责任：决定什么值得理解、什么解释可信、什么新概念值得进入共同知识体系。

## 可验证还不够，任务必须能够被大量并行磨出来

Grant 与 Dwarkesh 用计算机使用说明结果可验证不代表适合当前 RL 训练。包裹是否到达、日历是否创建都能检查，但真实网站无法低成本重复一千次。

> **[54:21]** "Is my Etsy package coming? Is my event booked? These are extremely verifiable things to survey. What computer use lacks is grindability."

数学和代码不同：环境可以复制、状态可以隔离、答案可以自动检查、失败不会破坏真实账户。当前模型样本效率低，需要大量 rollout，因而优先在可磨领域取得进展。

Lean 的独特价值，是允许程序长期运行并持续扩展 Mathlib，而不需要人类逐次检查。

> **[58:09]** "with Lean, you could imagine having a basically endlessly running program that's constantly trying to extend Mathlib."

> **[59:09]** "It might come up with its own conjectures. It might come up with its own theories and different definitions. Maybe many of them are useless, but it just has this infinite tree that it can grow out."

无限生成也会制造新的验证瓶颈。即使自然语言证明 99% 正确，数学家仍可能不愿花时间寻找那 1% 的错误。

> **[1:05:43]** "Even if 99 out of 100 are right, I don’t know if it’s worth my time because it's really labor-intensive to find what that error would be."

因此形式验证的价值不仅是正确率，而是降低人类审计的不确定性成本。

## 多 Agent 的优势不只是并行，而是主动制造认知差异

人类容易被竞赛背景、学派和既有启发式锁定。数字系统可以复制任务，并给不同 Agent 不同目标、偏见和上下文。

> **[49:27]** "Escape the context of being in the IMO. Escape the context of the way you've been trained to solve these contest math problems."

Grant 警告，不应让所有模型共享同一种“爱因斯坦式”启发式，因为生产力高的偏见也可能阻止其他领域进展。

> **[51:57]** "You want to make sure you don't accidentally have all your LLMs be Einstein, because you might halt progress on quantum mechanics. Which goes to show you that there's not a correct heuristic for science. You just need multiple independent research programs with their own heuristics."

这比简单增加 Agent 数量更具体。有效多 Agent 系统需要差异化假设、独立上下文、反方角色和最终证据汇合。如果所有 Agent 使用相同模型、提示和检索材料，并行只会快速复制同一种错误。

## Autoregression 擅长延续上下文，却可能被上下文绑架

Grant 认为逐 token 预测是一种奇怪的创作方式。

> **[41:51]** "Autoregression is actually a really weird way to produce stuff, if you think about it."

> **[42:40]** "In particular, what would probably happen is that you're a slave to your context."

跨领域连接往往要求生成低概率但结构上正确的下一步，而自回归训练天然奖励在当前上下文中合理延续。增加推理长度可以帮助搜索，却不自动改变问题表示和启发式。

可行动策略是周期性刷新上下文，让独立 Agent 从不同表述、反例和领域入口重启，再用形式验证或实验结果汇合，而不是让单一长上下文无限累积自身假设。

## 写作的瓶颈不是语法，而是持续模拟读者心智

Grant 认为写作和记忆卡片设计都要求预测未来读者在某一刻会如何理解和联想。

> **[1:11:56]** "The key constraint, it seemed to me, was that writing a good card is about projecting somebody's mind in three months."

模型可以清晰重述既有内容，却不一定能创造一个值得被重述的观察框架。

> **[1:10:23]** "Even if it's better at explaining a preexisting thing, what generated that book that you wanted distilled in the first place? It wasn't an LLM that generated it"

Grant 用面部肌肉镜像说明，人类理解情绪可能部分依赖具身模拟，而模型没有相同身体结构。

> **[1:14:43]** "They don't have face muscles. Their brain works completely differently."

这不是 AI 永远无法形成 theory of mind 的证明，但提示评价写作不能只看事实和流畅度。还要测试读者模型、叙事动机、信息顺序和对不同受众误解的预测。

## LLM 更像知识路由器，人类策展决定学习路径

Grant 把当前 LLM 解释类比为 Wikipedia：质量很高，但最有用的部分可能是参考文献。

> **[1:18:09]** "LLM explanations feel to me at the moment a lot like Wikipedia, which is to say, amazing."

他的实际用法是询问应该阅读谁。

> **[1:18:32]** "So often I like to just ask an LLM, "Who should I read?""

因此学习产品不应把生成答案作为终点。更高价值的设计是显示来源、观点谱系、前置知识和争议，让学习者进入经过策展的原始材料，并保留判断“为什么信任这个人”的社会信息。

Grant 对数学经济外溢保持克制。他预计未来五年会出现可归因于 AI 数学进展的经济改进，但拒绝给出确定预测。

> **[1:31:57]** "I'm not going to sit here and put a flag in the sand predicting that there will be. But it'd be a little bit disappointing and a little bit surprising if there weren't, over the next five years, economically valuable improvements made that were directly referable to the AI progress in math."

数学突破能否进入产业，取决于工程师、物理学家和材料科学家能否识别其相关性。知识生产速度提高后，跨领域翻译和应用策展会成为新瓶颈。

## 关键判断

- IMO、千禧年难题等 benchmark 内部由多种技能组成，跨过一个分数线不能证明能力均匀外溢。
- 概念创造的价值验证可能长达百年，短周期可验证奖励会系统性偏好证明而非定义。
- 证明、解释和创造概念是不同能力；AI 可能同时推进前两者，但长期价值判断仍需独立承担。
- 数学和代码进展快的关键是可验证加可磨，真实世界任务通常缺少低成本并行 rollout。
- 多 Agent 系统需要刻意制造不同启发式和上下文，否则只会复制同一种错误。
- 自回归模型容易延续既有上下文，科学发现系统应设计上下文刷新、反方搜索和证据汇合。
- 写作质量依赖读者心智建模，不能只用事实正确和语言流畅评估。
- AI 数学的产业外溢需要人类或 Agent 承担跨领域翻译、应用识别和策展。

## 深度关联
> 以下关联基于论点级分析：不是「都提到了X」，而是具体论点之间的逻辑关系

### 分支因子解释理论空间，可磨性解释训练空间
**→ [[Adam Brown- General Relativity from First Principles]]**
- 本文件论点：数学和代码能低成本复制环境、并行 rollout 并自动验证，因此比计算机使用更可磨 [54:21-59:09]。
- 对方论点：Brown 用分支因子解释纯思考何时有效；候选理论过多时必须用实验剪枝。
- 关联逻辑：两者描述两个不同空间。可磨性决定模型能否大量搜索训练轨迹，分支因子决定搜索后有多少自洽候选需要现实反馈。一个领域可能容易磨却分支巨大，也可能难磨但原则约束强；科学自动化必须同时评估两者。

### Test-time compute 扩大搜索，研究品味决定目标函数
**← [[Noam Brown- Test-Time Compute Changes Benchmarks, Safety and Research]]**
- 本文件论点：AI 可以无限扩展 Mathlib 和并行探索启发式，但提出定义和判断概念价值缺少短周期奖励 [13:17-23:22, 58:09-59:09]。
- 对方论点：Noam Brown 认为模型通过 scaffolding 和更多推理预算能解决未被开采的问题，却仍缺乏选择研究方向的品味。
- 关联逻辑：更多计算解决“搜得多深”，不能解决“哪棵树值得生长”。科学 Agent 需要将搜索预算与人类问题选择、长期价值代理和跨领域反馈结合，否则会产生大量正确但无关的定理。

### 假设生成成本下降后，验证瓶颈进一步变成消化瓶颈
**← [[Terence Tao- How the world's top mathematician uses AI]]**
- 本文件论点：即使 99% 自然语言证明正确，寻找剩余错误的成本仍可能让数学家拒绝阅读；新概念还可能需要百年才被理解 [13:17, 1:05:43]。
- 对方论点：Tao 判断假设生成成本下降后，验证能力成为稀缺资源。
- 关联逻辑：Grant 把验证瓶颈拆成正确性和消化性两层。形式系统可以给正确性绿勾，却不能保证证明带来理解；未来工具需要同时提供机器校验、概念压缩、依赖图和可迁移解释。

### Taste 从产品选择推进到研究定义
**← [[Andrew Ambrosino- OpenAI Codex lead on the new shape of product work]]**
- 本文件论点：自动证明后，稀缺工作转向提出定义、选择问题和策展学习路径 [30:13-34:52, 1:18:09-1:18:32]。
- 对方论点：Ambrosino 认为实现成本下降后，产品瓶颈从能不能做迁移到该不该做，taste 用于从大量原型中区分信号。
- 关联逻辑：产品 taste 与研究品味是同一验证结构的不同尺度：都不是判断产物是否可运行，而是判断产物是否值得存在。生成越便宜，定义目标、选择受众和承担最终责任越重要。

---

**元信息**
- 标题：Grant Sanderson (@3blue1brown) – AI disproved a famous math conjecture. Now what?
- 频道：Dwarkesh Patel
- 嘉宾：Grant Sanderson
- 发布时间：2026-07-01
- 时长：1:33:36
- YouTube：https://www.youtube.com/watch?v=TfyPshgMbug
- 逐字稿：[[Grant Sanderson- AI and the future of math 逐字稿]]
- 重写时间：2026-07-21
