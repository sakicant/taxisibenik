---
name: research-brief-writer
description: Write research briefs that translate findings into clear recommendations for decision-makers. Use after completing research, analysis, or data collection when you need to communicate findings to stakeholders who will not read the full report.
triggers:
  - write research brief
  - executive summary
  - summarize findings
  - research report
  - brief the team
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Research Brief Writer

Translate research findings into concise briefs that drive decisions. Decision-makers read the brief, not the full report. Make every sentence count.

## Writes
- `outputs/brief-[topic].md`

## Before Writing

Gather:
1. **The full research output** — analysis, data, findings
2. **Who is reading this** — their role, what they care about, what they will do with it
3. **The decision at stake** — what choice does this research inform?

## Structure

### 1. Bottom Line (2-3 sentences)
State the core finding and recommended action upfront. If the reader stops here, they should know what to do.

### 2. Context (3-5 sentences)
Why this research was conducted. What question it answers. What was out of scope.

### 3. Key Findings (3-5 bullets)
Each finding should be:
- **Specific** — include numbers, quotes, or concrete evidence
- **Relevant** — connected to the decision at stake
- **Prioritized** — most important first

### 4. Evidence Summary
For each finding, one paragraph with:
- The data or analysis that supports it
- Strength of evidence (strong / moderate / directional)
- Any caveats or limitations

### 5. Recommendations (numbered)
Each recommendation should be:
- **Actionable** — a specific next step someone can take
- **Justified** — clearly linked to a finding above
- **Owned** — suggest who should act on it

### 6. What We Do Not Know
Gaps, uncertainties, and areas where the evidence is insufficient. This section builds credibility.

## Writing Rules

- No jargon the reader would not use themselves
- Lead with implications, not methodology
- Use "we found" not "the data suggests" — be direct
- Tables and charts only if they communicate faster than text
- One page if possible. Two maximum.