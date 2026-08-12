---
title: 'The Agent Cloud: Databricks’ Bet on the Future of AI — Matei Zaharia and Reynold Xin'
source: repository_import
youtube_url: https://www.youtube.com/watch?v=Yp_u1NpbkJg
video_id: Yp_u1NpbkJg
transcript: '[[The Agent Cloud Databricks’ Bet on the Future of AI — Matei Zaharia and Reynold Xin [Yp_u1NpbkJg]]]'
source_repository: https://github.com/nolimitkun/ai-kol-wiki
source_wiki: https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260624-latent-space-databricks-agent-cloud.md
tags:
- kol情报
- imported
- ai-kol-wiki
status: imported
---

对应逐字稿：[[The Agent Cloud Databricks’ Bet on the Future of AI — Matei Zaharia and Reynold Xin [Yp_u1NpbkJg]]]
来源视频：[YouTube](https://www.youtube.com/watch?v=Yp_u1NpbkJg) · 视频 ID：`Yp_u1NpbkJg`
原始 Wiki：[ai-kol-wiki](https://github.com/nolimitkun/ai-kol-wiki/blob/main/wiki/videos/20260624-latent-space-databricks-agent-cloud.md)

## 来源说明

本文件由 `nolimitkun/ai-kol-wiki` 的公开 Wiki 页面生成。原始观点摘要与时间戳保持来源项目的表达；本文件不是本地浏览器插件捕获的 canonical 分析，后续复核应以逐字稿为准。

> 借 Data + AI Summit（10 万人）发布多款产品，重点两个：**Omnigent**（开源 agent 编排/"meta-harness" + agent cloud）与 **L-TAP / Dream Engine**（统一存储的 HTAP + 从零重写的数据库引擎）。Spark 两位作者的系统设计视角。

## 概要

一句话世界观："**把数据放到对的地方，然后在上面糊一层 AGI，魔法就出来了**"——但没有对的数据就不行。围绕这个判断，Databricks 做了 Omnigent（把 Claude Code/Codex/Cursor 等所有 harness 统一到一套 API，加上协作、安全、成本控制层）与 L-TAP（统一 OLTP/OLAP 存储层，让 agent 能实时 reason 业务数据）。中段是两个开源 vs 专有、增量演进、over-fit 少数客户的产品哲学复盘。

## 核心观点

### Omnigent：agent cloud 与"meta-harness"
- **两条汇聚线催生新东西**（"需要新范式的好信号"）：一是内部 coding agent 基础设施（Isaac，Claude Code/Codex 的 wrapper），高级工程师自己造 UI/多 agent 工作流；二是自建 agent（数据科学 agent Genie 等）反复撞上"每几个月要换模型/harness""agent 不能共享 session 就没用"（[00:03:03]–[00:05:05]）。
- **核心是一套跨 harness 的公共 API**：session 收 message/file，吐出 streaming text / tool call 流，可 cancel——底层映射到 Claude Code、Codex、OpenAI SDK 等，"Claude 改 API 时你不用自己维护适配"。上层才是 UI、安全、控制（[00:15:07]–[00:16:07]）。类比网络协议（IP layer）而非操作系统/数据库——与 [江鋆晨"OpenAI API = AI 时代的 IPv4"](20260609-uncle-moon-junchen-jiang-kvcache.md) 同一"细腰标准层"直觉。
- **为什么开源**（Spark 的老逻辑）：有网络效应、靠众人写 integration 的层就该开源（发布首个周末即 ~400 merge、约一半来自外部：K8s、cloud sandbox、更多 harness）；必须靠运维团队保证不丢数据的服务层则做成专有（[00:11:06]–[00:13:06]、[00:23:07]）。
- **agent cloud / 不关机的 sandbox**：Reynold 亲历"开车去看病还得 tether 笔记本盯 Codex session"的荒诞，"回到编程的黑暗时代"——sandbox 需要本地持久化（库不用每次重装），从 lakebase 架构去掉数据库即得（[00:07:06]–[00:17:07]）。

### Agent 安全：有状态/上下文策略
- **超越"yes/no 工具允许列表"**：单纯允许/禁止会把你逼到死角（该不该让 agent 读机密文档？装 NPM 新包？发布到公司网站？——单独都行，叠加就可能"读机密 + 被 prompt injection + 外泄"）。解法是 **contextual / stateful policies**：跟踪 session 状态——"如果它做了高风险的事（装了一天前的 NPM 包、读了一千份机密文档），就别做；否则可以"（[00:19:07]–[00:21:07]）。同时更安全且更好用。
- **策略即函数、可组库**：把底层事件（Google Drive MCP 的 60 个 API 调用）映射成高层语义（"这个会把文档分享到公网吗"）再写策略；别人可写库共享（[00:20:07]–[00:22:07]）。Matei 的 Unity Catalog（数据治理）经验平移到 AI 治理。
- **成本也是被跟踪的一种状态**："一个 agent 读日志烧了 500 美元 debug"——可对子 agent 设 5 美元上限、超了弹窗问（[00:22:07]）。呼应 [Freda 的 Token per Task](20260518-zhang-xiaojun-freda-investment-2.md)。

### L-TAP / Dream Engine：数据是 AGI 的前提
- **L-TAP = "HTAP done right"**：不追求单引擎兼顾事务+分析（single-store 的妥协），而是**只统一存储层**——Postgres 页在存储集群用空闲 CPU 转码成列式 parquet（转码后压缩更好、写更快、零开销），分析侧无 CDC 管道直接读（[00:32:12]–[00:36:13]）。"CDC = continuous data corruption，凌晨三点被叫醒的元凶"。
- 对 agent 的价值："agent 只看到数据库的产品遥测，看不懂谁在下单、发生了什么——让数据可实时 reason，agent 强 10 倍"（[00:33:12]–[00:34:12]）。
- **Dream Engine = 从零重写数据库引擎**：不靠读论文拼算法（70% 工作好、30% 反噬），而是建"造数据库的工厂"——用十年、约千万亿（quadrillion）条 trace 训一个 **ML 模型（非 LLM）**，高保真预测任意算法/实现对任意查询的性能，在实现期和运行时都 dispatch 最优数据结构（[00:47:18]–[00:50:20]）。避开"second system syndrome"。
- **agent 让 query 语言统一不再是问题**："agent 在 Postgres SQL / Spark SQL 都很流利、不会搞混，只要数据可访问就行"——五年前对人类是问题，现在不是（[00:52:21]–[00:53:22]）。故不必把 query 层也塌缩成单一 HTAP。

### 产品与组织哲学
- **文化 = 不用请示、直接原型**：L-TAP 的关键突破是工程师在无数次辩论后"直接 prototype 了、它 work 了"，没有 kickoff、没有设计文档；Omnigent 也是先写 10 条愿望清单让团队做出 5 条（[00:36:13]–[00:38:13]、[00:49:20]）。"AI 时代做这个更容易了。"
- **增量演进 + over-fit 少数客户**：产品多在数周内建成，第一问永远是"目标客户是谁、你和 ta 是不是 first-name basis"；over-fit 一两个客户的下行远小于"boil the ocean 最后没客户"（[00:38:13]–[00:41:15]、[00:53:22]）。
- **企业 vs 科技公司客户**的三大差异：治理/安全/合规、"我自己就能造"心态、legacy/采购流程——只优化科技公司会卡在规模化（[00:42:15]–[00:44:16]）。
- **胜过 Snowflake 的两点**：从一开始就**开放格式**（Parquet→Delta/Iceberg，从不专有）+ 从一开始就是 **ML/AI plus data**（不只数据基础设施）；从上游大规模 batch 往下游低延迟走，比反过来容易（[00:53:22]–[00:57:25]）。

## 相关主题

- [AI 算力与基础设施](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/ai-infrastructure.md)（agent cloud/sandbox、跨 harness 公共 API、L-TAP 存储层、Dream Engine 用 ML 建数据库）
- [LLM 安全](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/llm-security.md)（有状态/上下文安全策略，超越 yes/no 允许列表）
- [实践中使用 LLM](https://github.com/nolimitkun/ai-kol-wiki/blob/main/topics/using-llms-in-practice.md)（coding agent 编排、成本控制、agent 用 SQL）

## 深度关联

- 语料层关联：[[KOL语料库对比评估-2026-08-11]] 将本视频纳入两个公开知识库的覆盖、去重和更新时间比较；本文件的状态与该评估保持一致。
