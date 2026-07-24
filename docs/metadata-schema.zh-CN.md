# 元数据规范

每份逐字稿都是带 YAML Frontmatter 的 UTF-8 Markdown 文件。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `title` | 字符串 | 原始视频标题 |
| `source_url` | URL | 原始视频链接 |
| `video_id` | 字符串 | 稳定的 YouTube 视频标识 |
| `account` | 双向链接 | 发布账号节点 |
| `account_name` | 字符串 | 发布账号名称 |
| `account_url` | URL | 可用时记录发布账号主页 |
| `featured_people` | 双向链接列表 | 视频中主要出现的人物 |
| `published` | 日期 | 原始视频发布日期 |
| `created` | 日期 | 本地逐字稿创建日期 |
| `language` | 字符串 | 逐字稿语言代码 |
| `speaker_attribution` | 枚举 | `explicit`、`contextual` 或 `unattributed` |
| `description` | 字符串 | 来源描述或摘要 |
| `tags` | 字符串列表 | Obsidian 标签 |

`contextual` 表示文件有时间戳，但没有完成说话人标注。正式引用时必须结合相邻对话和原视频核验归因。

逐字稿段落通常以 `**H:MM:SS** ·` 或 `**M:SS** ·` 开头。内置 Skill 会将其转换为可点击的 YouTube `t=` 跳转链接。
