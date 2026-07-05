---
name: quality-gate
description: Evaluate any content against 6 quality dimensions and deliver a SHIP, FIX, or BLOCK verdict. Use before publishing blog posts, emails, reports, social posts, or documentation.
triggers:
  - quality gate
  - ready to publish
  - review before shipping
  - can I ship this
allowed-tools: []
---

# Quality Gate

Evaluate content against 6 dimensions. Deliver a clear verdict: SHIP, FIX, or BLOCK.

## Input

Accept the content to review. This can be:
- Pasted text
- A file path to read
- A URL to fetch

Also ask: Who is the intended audience? What is the goal of this content?

## Evaluation Dimensions

Score each dimension: **PASS**, **NEEDS WORK**, or **FAIL**.

### 1. Completeness
- Does the content cover everything it promises?
- Are there sections that trail off or feel unfinished?
- Are there missing examples, data, or proof points that the audience would expect?

### 2. Accuracy
- Are all facts, numbers, and claims verifiable?
- Are there statements that could be challenged without supporting evidence?
- Are technical details correct?

### 3. Voice Consistency
- Does the tone match the intended audience and channel?
- Are there shifts in formality, energy, or style within the piece?
- If a brand voice guide exists (`reference/brand-voice.md`), does the content follow it?

### 4. Formatting
- Is the structure scannable (headings, short paragraphs, lists where appropriate)?
- Are there formatting inconsistencies (mixed list styles, inconsistent heading levels)?
- Is the length appropriate for the format and channel?

### 5. Links and References
- Do all links work and point to the intended destination?
- Are sources cited where claims are made?
- Are internal references (file paths, section names) correct?

### 6. Audience Fit
- Would the intended reader find this relevant and valuable?
- Is the complexity level appropriate (not too basic, not too advanced)?
- Does it address what the audience cares about, not just what the author wants to say?

## Verdict Logic

- **SHIP** — All 6 dimensions score PASS. Content is ready to publish.
- **FIX** — One or more dimensions score NEEDS WORK, but none score FAIL. Content needs specific improvements before publishing.
- **BLOCK** — One or more dimensions score FAIL. Content has fundamental issues that require significant rework.

## Output Format

### Verdict: [SHIP / FIX / BLOCK]

| Dimension | Score | Finding |
|-----------|-------|---------|
| Completeness | [PASS/NEEDS WORK/FAIL] | [One-line summary] |
| Accuracy | ... | ... |
| Voice Consistency | ... | ... |
| Formatting | ... | ... |
| Links and References | ... | ... |
| Audience Fit | ... | ... |

### Required Fixes
For each NEEDS WORK or FAIL, provide:
- **What:** The specific issue
- **Where:** Line or section reference
- **Fix:** Concrete suggestion with replacement text

## Common Mistakes
- Do not give a SHIP verdict with vague "looks good" justification. Every PASS needs a specific reason.
- Do not check only grammar and spelling. The 6 dimensions go far beyond surface-level editing.
- Do not skip the audience fit check. Well-written content that misses its audience is still a failure.