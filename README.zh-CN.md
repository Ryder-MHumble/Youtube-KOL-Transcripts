<p align="center">
  <img src="assets/banner-zh-CN.png" alt="KOL 逐字稿合集横幅" width="720">
</p>

# KOL 逐字稿合集

[English](README.md)

一个可直接作为 Obsidian 知识库使用的开放 KOL 逐字稿项目，面向 AI、科技、商业与战略研究，保留原话、视频来源和时间戳。

仓库目前包含来自 **13 个发布账号的 63 份逐字稿**，并连接了 **49 个人物节点**。内置的 `kol-quote-research` Skill 可以根据研究观点检索相近或相反的 KOL 观点，并返回可核验的原话、视频链接与时间戳。

## 直接导入 Obsidian

```bash
git clone https://github.com/Ryder-MHumble/kol-transcripts.git
```

在 Obsidian 中选择“打开本地仓库”，选中克隆后的仓库根目录即可。无需转换格式或执行构建命令。

建议从 [索引.md](索引.md) 开始浏览。账号、人物和逐字稿之间均使用 Obsidian 双向链接，Obsidian 完成索引后即可直接查看知识图谱。

## 使用 Skill 检索 KOL 观点

将 `skills/kol-quote-research` 复制或链接到 AI Agent 的 Skill 目录。Codex 用户可以执行：

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/skills/kol-quote-research" ~/.codex/skills/kol-quote-research
```

示例问题：

> 使用 `$kol-quote-research`。我的观点是：AI 正在让执行成本快速下降，因此判断力和产品品味会成为更稀缺的战略资产。哪些 KOL 提过相近或相反的观点？请返回观点原话、视频链接和时间戳。

Skill 使用本地排序检索加 Agent 上下文核验，不依赖向量数据库、外部检索服务或 API Key。

## 项目结构

```text
accounts/                         发布账号节点及其逐字稿列表
people/                           人物节点及其出现记录
transcripts/<account-slug>/       保留时间戳的原始逐字稿 Markdown
skills/kol-quote-research/        可安装的 AI 研究 Skill
scripts/                          导入与校验脚本
data/featured-people.yml          人物元数据人工校正表
catalog.jsonl                     机器可读的逐字稿目录
Index.md                          英文 Obsidian 入口
索引.md                            中文 Obsidian 入口
```

逐字稿以**发布账号或频道**为一级目录，受访者和主要发言人作为独立人物节点。这样既不会因为一场多人访谈重复存储文件，也能在知识图谱中按人物继续探索。

## 证据与归因

多数原始逐字稿有时间戳，但没有完成说话人分离，因此标记为 `speaker_attribution: contextual`。`featured_people` 只能证明该人物是视频的重要参与者，不能证明文件中的每句话都由该人物说出。正式引用前必须核对相邻上下文。

字段说明见[元数据规范](docs/metadata-schema.zh-CN.md)，转载或二次使用逐字稿前请阅读[内容权利说明](RIGHTS.zh-CN.md)。

## 参与贡献

欢迎提交错字修正、时间戳补充、账号信息修正、说话人归因和新的公开来源逐字稿。请先阅读 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)，并运行：

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

## 许可证

本项目原创代码与项目文档采用 MIT License。第三方逐字稿内容不包含在 MIT 授权范围内，其权利仍归原始发言人、发布方和平台所有。详见 [RIGHTS.zh-CN.md](RIGHTS.zh-CN.md)。
