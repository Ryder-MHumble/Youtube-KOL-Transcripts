<p align="center">
  <img src="assets/banner-en.png" alt="KOL Transcripts banner" width="720">
</p>

# KOL Transcripts

[简体中文](README.zh-CN.md)

An open, Obsidian-ready collection of timestamped KOL transcripts for evidence-based AI, technology, business, and strategy research.

The repository currently contains **63 transcripts from 13 publishing accounts**, organized by account and connected to **49 featured-person nodes**. Each transcript preserves the original wording, source video, and timestamps. The bundled `kol-quote-research` skill helps AI agents find viewpoints related to a thesis and return exact quotes with traceable links.

## Use It as an Obsidian Vault

```bash
git clone https://github.com/Ryder-MHumble/kol-transcripts.git
```

In Obsidian, choose **Open folder as vault** and select the cloned repository root. No conversion or build step is required.

Start from [Index.md](Index.md). Account notes, person notes, and transcript frontmatter use Obsidian Wikilinks, so Graph View works immediately after Obsidian indexes the files.

## Search KOL Viewpoints with the Skill

Install the bundled skill by linking or copying `skills/kol-quote-research` into your agent's skill directory. For Codex:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/skills/kol-quote-research" ~/.codex/skills/kol-quote-research
```

Then ask a research question such as:

> Use `$kol-quote-research`. My thesis is that AI makes execution cheap, so judgment and product taste become the scarce strategic assets. Which KOLs express similar or opposing views? Return exact quotes, video links, and timestamps.

The skill uses local ranked retrieval plus agent verification. It does not require an embedding service or API key.

## Repository Structure

```text
accounts/                         Publishing-account nodes and transcript lists
people/                           Featured-person nodes and appearance lists
transcripts/<account-slug>/       Original timestamped transcript Markdown
skills/kol-quote-research/        Installable AI research skill
scripts/                          Import and validation utilities
data/featured-people.yml          Curated participant metadata
catalog.jsonl                     Machine-readable transcript catalog
Index.md                          English Obsidian entry point
索引.md                            Chinese Obsidian entry point
```

Transcripts are grouped by the **publishing account or channel**. Featured interviewees and speakers are modeled separately, which avoids duplicating one interview across several folders while still supporting person-centered graph exploration.

## Evidence and Attribution

Most source transcripts contain timestamps but not speaker labels. Those files use `speaker_attribution: contextual`. The presence of a person in `featured_people` does not prove that every line was spoken by that person. Verify adjacent dialogue before publishing a quotation under an individual's name.

See [the metadata schema](docs/metadata-schema.md) for field definitions and [the rights notice](RIGHTS.md) before reusing transcript content.

## Contributing

Corrections, missing timestamps, account metadata, speaker attribution, and new public-source transcripts are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and run:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

## License

Repository-authored code and documentation are available under the MIT License. Third-party transcript content is excluded from that license and remains subject to the rights of the original speakers, publishers, and platforms. See [RIGHTS.md](RIGHTS.md).
