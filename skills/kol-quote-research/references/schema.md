# Transcript Schema

Each transcript lives under `transcripts/<account-slug>/` and contains YAML frontmatter followed by the original transcript text.

Required metadata:

- `title`: Original video title.
- `source_url`: Canonical source video URL.
- `video_id`: YouTube video identifier.
- `account`: Obsidian link to the publishing account node.
- `account_name`: Human-readable publishing account.
- `featured_people`: Curated Obsidian links to people prominently featured in the video.
- `published`: Source publication date.
- `speaker_attribution`: `explicit`, `contextual`, or `unattributed`.

`featured_people` identifies likely participants, not the speaker of every line. Most imported transcripts use `contextual` because the source text has timestamps but no speaker labels. Verify the surrounding dialogue before naming a speaker.

The root `catalog.jsonl` repeats the searchable metadata without duplicating transcript text. Account notes and person notes provide Obsidian backlinks for graph navigation.
