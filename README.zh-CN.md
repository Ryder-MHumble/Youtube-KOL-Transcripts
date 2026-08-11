<p align="center">
  <img src="assets/banner-zh-CN.png" alt="YouTube KOL 旁听席" width="100%">
</p>

# 别再让真正有价值的观点，埋在两小时的视频里

[English](README.md)

**把数小时的 YouTube 深度访谈，变成可搜索、可引用、可持续积累的决策情报。**

真正影响市场、产品和技术走向的判断，往往最先出现在一两个小时的深度访谈里。全部看完太耗时间，看完以后很难重新找到原话，依赖二手总结又容易丢失关键上下文。

这个项目持续追踪一批高信号 YouTube KOL 账号，把最新长视频整理为完整、带时间戳的逐字稿，并组织成可被 Obsidian 和 AI Agent 直接使用的知识库。

它不是另一个摘要合集，而是一套记录“谁说了什么、在哪里说、不同观点如何关联”的可迁移原话资产。

## 在线检索入口

- 网页检索：[GitHub Pages 索引](https://ryder-mhumble.github.io/Youtube-KOL-Transcripts/)
- 机器可读数据：[`catalog.jsonl`](catalog.jsonl) 和 [`site/data.json`](site/data.json)
- Agent 入口：[`llms.txt`](llms.txt) 和可安装的 [`kol-quote-research`](skills/kol-quote-research/SKILL.md) Skill

网页索引支持按 YouTube 账号、KOL/人物名称、标题、视频 ID 和导入状态检索。Pages 部署时会通过 [`scripts/rebuild_indexes.py`](scripts/rebuild_indexes.py) 重新生成索引数据。

## 核心价值

| 核心价值 | 你能得到什么 |
| --- | --- |
| **内容完整** | 保留完整逐字稿，而不是只摘几条结论，重要的限定条件、争论和上下文不会被摘要抹掉。 |
| **持续更新** | 跟踪精选 KOL 账号的最新发布，通过一次 `git pull` 即可同步新增逐字稿和观点。 |
| **引用精准** | 每条有价值的观点都可以回到原视频、原话和时间戳，适合研究、汇报、写作与事实核验。 |
| **使用简单** | 复制一句话就能让 Agent 完成安装和迁移，也可以克隆后直接作为 Obsidian 知识库打开。 |
| **自由迁移** | 全部内容采用 Markdown 和 YAML，不绑定任何笔记软件、模型服务或封闭平台，知识资产始终属于你。 |

## 复制这句话，让 Agent 帮你配置好

把下面整段复制给 Codex、Claude Code 或其他具备本地文件能力的 Agent：

```text
请帮我安装并配置这个开源项目：https://github.com/Ryder-MHumble/Youtube-KOL-Transcripts 。自动定位我本地的 Obsidian Vault，把仓库克隆到一个独立子目录中，不要覆盖任何现有笔记；将仓库内的 kol-quote-research Skill 安装到当前 Agent；运行项目校验并完成一次示例观点检索；最后告诉我以后如何通过 git pull 获取最新逐字稿。请直接执行，不要只给我操作教程。
```

配置完成后，你可以直接提出这类问题：

- 我的战略判断与哪些 KOL 的观点接近？谁持反对意见？
- 帮我找到某位创始人谈论“AI 取代软件席位”的原话。
- 对比 Jensen Huang、Satya Nadella 和 Dario Amodei 对 AI 基础设施的判断。
- 同一个 KOL 在不同访谈中的观点发生了什么变化？
- 给我可以直接用于报告的原话、视频链接、时间戳和上下文。

## 它适合解决什么问题

- **战略与行业研究：** 用一手观点验证假设，不再依赖无法追溯的网页摘要。
- **投资研究：** 追踪创始人、投资人和产业操盘者的叙事变化、分歧与长期判断。
- **产品与创业：** 快速找到关于用户需求、定价、分发、组织和技术趋势的真实讨论。
- **内容创作：** 不用重看数小时视频，也能找到有来源、有上下文的引用材料。
- **AI Agent 研究：** 给 Agent 一套结构化证据库，减少凭记忆回答和编造引用。

## 直接作为 Obsidian 知识库使用

```bash
git clone https://github.com/Ryder-MHumble/Youtube-KOL-Transcripts.git
```

在 Obsidian 中选择“打开本地仓库”，选中克隆后的仓库根目录即可。建议从 [索引.md](索引.md) 开始浏览。账号、人物和逐字稿之间已经建立双向链接，Obsidian 完成索引后即可直接查看和扩展知识图谱。

无需转换格式、导入数据库或安装专用笔记应用。

<p align="center">
  <img src="assets/obsidian-knowledge-graph.png" alt="YouTube KOL 逐字稿在 Obsidian 中形成的知识图谱" width="100%">
</p>

<p align="center"><sub>账号、人物、逐字稿和你自己的研究笔记，可以在同一张 Obsidian 关系图谱中持续连接。</sub></p>

## 当前收录

目前知识库包含：

- **223 份逐字稿文件 / 185 个去重 YouTube 视频 + 16 个 source_id 归档记录**，均保留来源链接和时间戳
- **21 个发布账号页**，覆盖 AI、科技、商业与战略领域
- **72 个人物节点**，可以跨访谈追踪同一人物的观点
- **228 篇 KOL 深度分析文件**（`analysis/`），包含每个访谈的结构化要点、推理链和交叉引用
- **16 份 AI 行业知识图谱**（`knowledge-graph/`），按公司维度的事件时间线（OpenAI、Anthropic、Google DeepMind、DeepSeek、Meta AI、Mistral AI）
- **深度分析报告**（`deep-reports/`），基于全量数据生成的多维度交叉洞察报告
- **77 份外部迁移逐字稿**，来自公开 KOL 归档项目，统一标记为 `imported`，不冒充本地 canonical 捕获
- 可安装的 **`kol-quote-research` Skill**，用于观点匹配和原话检索

项目可以在不改变使用习惯的前提下持续增长：拉取最新版本，把自己的研究笔记写在旁边，继续在同一张 Obsidian 知识图谱上积累。

## 证据可信度

每份逐字稿都保留原始视频链接和时间戳。由于多数来源没有完成说话人分离，项目会明确记录归因置信度。当上下文无法确认具体发言人时，Skill 会标注不确定性，而不是把主持人的提问错误归给受访者。

字段说明见[元数据规范](docs/metadata-schema.zh-CN.md)，转载或二次使用逐字稿前请阅读[内容权利说明](RIGHTS.zh-CN.md)。

<details>
<summary><strong>项目结构</strong></summary>

```text
accounts/                         发布账号索引
people/                           主要人物索引
transcripts/<account-slug>/       完整逐字稿
analysis/                         KOL 深度分析文件（要点、推理链、交叉引用）
knowledge-graph/                  AI 行业事件时间线（按公司）
deep-reports/                     多源交叉洞察报告（PDF/MD）
skills/kol-quote-research/        可安装的 AI 研究 Skill
site/                             GitHub Pages 静态检索页
.github/workflows/pages.yml       GitHub Pages 部署工作流
scripts/rebuild_indexes.py        目录、账号页和站点数据生成器
llms.txt                          面向 Agent 的项目入口
catalog.jsonl                     机器可读的逐字稿目录
Index.md                          英文 Obsidian 入口
索引.md                            中文 Obsidian 入口
```

</details>

## 参与贡献

欢迎提交错字修正、时间戳补充、说话人归因、新的追踪账号和新的公开来源逐字稿。提交前请阅读 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

## 许可证

本项目原创代码与项目文档采用 MIT License。第三方逐字稿内容不包含在 MIT 授权范围内，其权利仍归原始发言人、发布方和平台所有。详见 [RIGHTS.zh-CN.md](RIGHTS.zh-CN.md)。
