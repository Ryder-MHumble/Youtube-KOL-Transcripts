<p align="center">
  <img src="assets/banner-en.png" alt="YouTube KOL Roundtable" width="100%">
</p>

# Never Lose a Great Idea Inside a Two-Hour Interview Again

[简体中文](README.zh-CN.md)

**Turn hours of YouTube interviews into searchable, citable, reusable intelligence.**

The ideas that shape markets, products, and technology often appear first in long-form conversations. Watching every two-hour interview is expensive. Finding the exact quote later is even harder, and second-hand summaries frequently remove the context that made the idea valuable.

This project continuously follows a curated set of high-signal YouTube accounts, converts new long-form videos into complete timestamped transcripts, and organizes them as a knowledge base you can search with Obsidian or an AI agent.

It is not another collection of summaries. It is a portable archive of what influential people actually said, where they said it, and how their views connect.

## Why It Is Useful

| Core value | What you get |
| --- | --- |
| **Complete context** | Full transcripts instead of a few extracted bullet points, so important qualifications and disagreements are not lost. |
| **Fresh signals** | New releases from tracked KOL accounts can be added to the same library; `git pull` keeps your local research base current. |
| **Accurate evidence** | Original wording, source video, and timestamp links make every useful claim easy to verify and cite. |
| **Immediate use** | Ask an agent to configure everything with one prompt, or clone the repository and open it directly in Obsidian. |
| **Knowledge you own** | Plain Markdown and YAML keep the library portable, editable, and independent of any closed note-taking or AI platform. |

## Let Your Agent Set It Up

Copy this entire sentence into Codex, Claude Code, or another coding agent:

```text
Set up the YouTube KOL Transcripts project from https://github.com/Ryder-MHumble/Youtube-KOL-Transcripts: locate my local Obsidian vault, clone the repository into a separate folder without overwriting any existing notes, install the bundled kol-quote-research skill for this agent, run the repository validation and one example viewpoint search, then show me how to pull future transcript updates. Execute the setup instead of only explaining the steps.
```

After setup, you can ask questions such as:

- Which KOLs agree or disagree with my strategic thesis?
- Find the exact quote where a founder discussed AI replacing software seats.
- Compare how Jensen Huang, Satya Nadella, and Dario Amodei think about AI infrastructure.
- Show how one KOL's position changed across multiple interviews.
- Give me publishable evidence with the original quote, video, timestamp, and context.

## Built for Real Research Work

- **Strategy and market research:** test a thesis against first-hand expert views instead of generic web summaries.
- **Investment research:** trace narratives, disagreements, and changing convictions across founders, investors, and operators.
- **Product and company building:** recover concrete views on user needs, pricing, distribution, organization, and technology shifts.
- **Content creation:** find source-backed quotes and context without replaying hours of video.
- **AI agents:** give an agent a structured evidence base rather than asking it to rely on memory or untraceable answers.

## Open It in Obsidian

```bash
git clone https://github.com/Ryder-MHumble/Youtube-KOL-Transcripts.git
```

In Obsidian, choose **Open folder as vault** and select the cloned repository root. Start from [Index.md](Index.md). Account, person, and transcript links are already connected, so the library becomes a navigable knowledge graph after Obsidian indexes it.

No conversion, import pipeline, or proprietary database is required.

<p align="center">
  <img src="assets/obsidian-knowledge-graph.png" alt="YouTube KOL transcripts connected as an Obsidian knowledge graph" width="100%">
</p>

<p align="center"><sub>Accounts, people, transcripts, and your own research notes remain connected in one navigable Obsidian graph.</sub></p>

## Current Coverage

The library currently includes:

- **63 complete transcripts** with source links and timestamps
- **13 publishing accounts** across AI, technology, business, and strategy
- **49 featured-person nodes** for cross-interview exploration
- An installable **`kol-quote-research` skill** for thesis matching and exact quote retrieval

The project is designed to grow without changing how users work: pull the newest version, keep your own notes beside it, and continue building on the same Obsidian graph.

## Evidence You Can Trust

Every transcript keeps a direct source URL and timestamped passages. Most source transcripts do not include diarized speaker labels, so the repository records attribution confidence explicitly. When a speaker cannot be confirmed from the nearby dialogue, the skill reports that uncertainty instead of inventing an attribution.

See [the metadata schema](docs/metadata-schema.md) for field definitions and [the rights notice](RIGHTS.md) before reusing transcript content.

<details>
<summary><strong>Repository structure</strong></summary>

```text
accounts/                         Publishing-account indexes
people/                           Featured-person indexes
transcripts/<account-slug>/       Complete timestamped transcripts
skills/kol-quote-research/        Installable AI research skill
catalog.jsonl                     Machine-readable transcript catalog
Index.md                          English Obsidian entry point
索引.md                            Chinese Obsidian entry point
```

</details>

## Contributing

Corrections, timestamp improvements, speaker attribution, new tracked accounts, and new public-source transcripts are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## License

Repository-authored code and documentation are available under the MIT License. Third-party transcript content is excluded from that license and remains subject to the rights of the original speakers, publishers, and platforms. See [RIGHTS.md](RIGHTS.md).
