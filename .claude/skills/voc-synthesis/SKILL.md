---
name: voc-synthesis
description: Synthesize transcripts, surveys, reviews, support tickets, and CRM notes into structured buyer language patterns. Surfaces the exact words buyers use, what they care about most, and where their stated needs contradict their behavior. Use after interviews, after a batch of reviews comes in, or when your messaging feels disconnected from how buyers actually talk.
triggers:
  - synthesize feedback
  - voice of customer
  - buyer language
  - voc analysis
  - what are customers saying
  - analyze transcripts
  - review synthesis
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# VoC Synthesis

## Writes
- `outputs/voc-synthesis.md`

## Context Scan

Check `context/` and `reference/` for:
- Existing ICP definitions
- Prior VoC analyses
- Brand voice guidelines
- Messaging frameworks

## Input

Ask for one or more of:

1. **Interview or call transcripts** — paste or point to files
2. **Survey responses** — raw text answers, not just scores
3. **Reviews** — G2, Capterra, App Store, Trustpilot, etc.
4. **Support tickets or CRM notes** — recent customer interactions
5. **Social mentions** — LinkedIn comments, Reddit threads, community posts

Accept whatever format the user has. Partial data is fine. More sources give better triangulation.

**Related skill:** For deep review-only analysis with quality scoring and transformation tracking, use review-miner instead.

## Step 1 — Extract Raw Language

Read every source. Extract exact phrases and sentences where the buyer describes:

- **Pain** — what is not working today
- **Desire** — what they wish they had
- **Value** — what they got from the product
- **Objection** — what held them back or concerns them
- **Trigger** — what event made them look for a solution

Quote directly. Do not paraphrase at this stage. Buyer language is the asset. Your interpretation of it is not.

## Step 2 — Frequency Map

Group the extracted quotes by theme. Count how many sources mention each theme.

| Theme | Sources | Frequency | Example Quote |
|-------|---------|-----------|---------------|
| [Pain/desire theme] | [Which sources] | [Count] | "[Exact quote]" |

Sort by frequency. The themes that appear across multiple sources and multiple people are the strongest signals.

## Step 3 — Echo Language

From the frequency map, extract the specific words and phrases buyers repeat. These are your "echo words" — the vocabulary your audience actually uses.

| Echo Phrase | Context | Frequency | Implication for Messaging |
|-------------|---------|-----------|--------------------------|
| "[Exact phrase]" | [Pain/desire/value] | [Count] | [How to use this in copy] |

Echo language is gold for headlines, subject lines, ad copy, and sales emails. When buyers see their own words reflected back, trust increases immediately.

## Step 4 — Contradiction Map

Look for places where what buyers say contradicts what they do:

| What They Say | What They Do | Implication |
|---------------|-------------|-------------|
| "[Stated preference]" | [Actual behavior] | [What this means for positioning] |

Common contradictions:
- "Price is the most important factor" → but they chose the more expensive option
- "We need something simple" → but they use the most complex features
- "We evaluated 5 tools" → but they signed in 2 weeks (impulse, not evaluation)

Contradictions reveal the real buying criteria that surveys miss.

## Step 5 — Buyer Brain Summary

Synthesize everything into a structured profile:

### What Keeps Them Up at Night
Top 3 pains by frequency, with echo language.

### What They Actually Want
Top 3 desires, distinguished from what they say they want vs. what they actually buy.

### How They Describe the Problem
The exact language they use. Not your language. Theirs.

### What Triggers Action
The events that move them from "thinking about it" to "looking for a solution." This is the **switching trigger** in Jobs-to-be-Done terms — the moment the job becomes urgent enough to hire a new solution for. Capture the trigger event itself, not just the resulting search.

### What They Fear About Switching
Objections and concerns, ranked by frequency.

### Words They Use vs. Words They Don't
A vocabulary guide: terms that resonate vs. terms that fall flat or create confusion.

## Do NOT
- Paraphrase buyer quotes before analysis. The exact words matter. "They want efficiency" is your interpretation. "I waste two hours every morning just finding the right file" is their language.
- Weight all sources equally. A 30-minute interview has more signal than a one-line review. Note source quality alongside frequency.
- Ignore small-sample contradictions. Even one contradiction can reveal a pattern worth investigating.
- Produce a report and stop. The output should directly feed into messaging, positioning, and content. End with specific recommendations for how to use each finding.

## Succeeds when
- Echo language is specific enough to drop directly into headlines, ads, and sales emails
- Switching triggers (JTBD) are captured as events, not as abstract motivations
- Themes are ranked by triangulated frequency across sources, not by source enthusiasm
- Contradictions between stated preferences and actual behavior are surfaced
- Output ends with concrete copy or positioning changes, not a stand-alone report

## Fails when
- Quotes are paraphrased into your interpretation before analysis
- All sources are weighted equally regardless of depth
- The report identifies themes without naming the words buyers actually use
- Findings sit in a doc without changing any downstream messaging