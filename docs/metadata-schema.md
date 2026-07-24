# Metadata Schema

Every transcript is a UTF-8 Markdown file with YAML frontmatter.

| Field | Type | Meaning |
| --- | --- | --- |
| `title` | string | Original video title |
| `source_url` | URL | Canonical source video |
| `video_id` | string | Stable YouTube video identifier |
| `account` | Wikilink | Publishing account node |
| `account_name` | string | Publishing account display name |
| `account_url` | URL | Publishing account URL when available |
| `featured_people` | Wikilink list | Curated people prominently featured in the video |
| `published` | date | Source publication date |
| `created` | date | Local transcript creation date |
| `language` | string | Transcript language code |
| `speaker_attribution` | enum | `explicit`, `contextual`, or `unattributed` |
| `description` | string | Source description or summary |
| `tags` | string list | Obsidian tags |

`contextual` means that timestamps exist but speaker labels do not. Quote attribution must be checked against nearby dialogue and source video context.

Transcript paragraphs normally begin with `**H:MM:SS** ·` or `**M:SS** ·`. The bundled search skill converts these values into clickable YouTube `t=` links.
