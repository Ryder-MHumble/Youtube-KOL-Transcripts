---
name: kol-quote-research
description: Retrieve evidence-backed viewpoints from the kol-transcripts repository. Use when a user wants to compare a thesis with KOL opinions, find who expressed a similar or opposing view, recover exact original wording from transcript Markdown files, or cite a video URL and timestamp. Especially useful for strategy research, market analysis, literature reviews, and claim verification across English or Chinese queries.
---

# KOL Quote Research

Find relevant transcript passages, verify them in context, and return exact quotations with traceable sources.

## Workflow

1. Locate the repository root containing `catalog.jsonl` and `transcripts/`.
2. Rewrite the user's claim as a neutral research question.
3. Expand the query into both Chinese and English search terms. Add synonyms, named concepts, and one opposing formulation. English expansion is required when the transcripts are English.
4. Run the bundled search script two or three times with different formulations:

```bash
python3 skills/kol-quote-research/scripts/search_transcripts.py \
  "implementation cost execution becomes cheap scarce judgment taste strategy" \
  --limit 12 --json
```

5. Open the highest-scoring transcript files and read the quoted passage plus adjacent timestamps. Search results are candidates, not final evidence.
6. Keep only passages that directly support, qualify, or contradict the user's claim.
7. Preserve the exact source wording. Put translations or summaries in a separate field.

## Attribution Rules

- Treat `speaker_attribution: contextual` as an explicit warning: the transcript has timestamps but no diarized speaker labels.
- Name a person only when the title, nearby dialogue, or metadata makes the speaker clear.
- Otherwise attribute the quote to the publishing account and label the speaker as unverified.
- Never turn a channel description, chapter title, interviewer question, or paraphrase into a KOL quote.
- Never invent a timestamp. If no timestamp exists, state that limitation.

## Required Output

Return a compact evidence table with these fields:

- Relationship to the user's claim: aligned, qualified, or opposed
- KOL or account
- Exact original quote
- Optional Chinese translation when the quote is not Chinese
- Source video and clickable timestamp
- One-sentence context
- Attribution confidence: high, medium, or unverified

After the table, synthesize agreements and disagreements. Separate evidence from interpretation. If no direct evidence exists, say so instead of filling the gap with general knowledge.

## Resources

- Use `scripts/search_transcripts.py` for ranked passage retrieval.
- Read `references/schema.md` when metadata, links, or attribution fields are unclear.
