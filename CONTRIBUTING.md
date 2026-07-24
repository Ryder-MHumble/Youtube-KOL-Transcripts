# Contributing

[简体中文](CONTRIBUTING.zh-CN.md)

Contributions should improve the accuracy, traceability, or coverage of public-source transcripts.

## Add or Update a Transcript

1. Use a public source and include its canonical video URL.
2. Keep the transcript in Markdown and preserve original wording.
3. Include timestamps wherever the source provides them.
4. Do not claim speaker certainty when the transcript lacks diarized labels.
5. Update `data/featured-people.yml` only with people clearly featured in the source.
6. Install maintenance dependencies with `python3 -m pip install -r requirements.txt`.
7. Import from a source directory:

```bash
python3 scripts/import_transcripts.py /path/to/transcript-directory --refresh-youtube
```

8. Validate before opening a pull request:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```

## Corrections and Rights Requests

For transcription errors, include the file, timestamp, source link, and corrected wording. Rights holders may open an issue with the affected source URLs and requested action. Do not submit private, paywalled, leaked, or personal material.
