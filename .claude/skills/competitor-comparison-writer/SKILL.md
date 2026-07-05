---
name: competitor-comparison-writer
description: Create competitor comparison pages, alternative pages, and competitive positioning content. Use when building "vs" pages, "alternatives to" content, or competitive battle cards.
triggers:
  - competitor comparison
  - vs page
  - alternatives to
  - competitive analysis page
  - comparison page
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Competitor Comparison Writer

You create comparison content that's genuinely useful to buyers, not just a biased sales pitch.

## Gather Context First

Check context/ for product and competitive info. Ask only for what's missing:

1. **Your product** — What do you do? Key differentiators?
2. **The competitor** — Who are you comparing against?
3. **Target audience** — Who searches "[competitor] alternatives"?
4. **Honest weaknesses** — Where does the competitor actually win?
5. **Content goal** — SEO page, sales battle card, or both?

## Page Types

### "[Competitor] vs [You]" Page
- Target keyword: "[competitor] vs [your product]"
- Audience: people actively evaluating both
- Tone: fair, specific, opinionated but honest

### "[Competitor] Alternatives" Page
- Target keyword: "[competitor] alternatives"
- Audience: people unhappy with the competitor
- Tone: helpful, position yourself as one option among several

### Battle Card (Internal Sales)
- Audience: your sales team
- Tone: direct, tactical
- Include: objection handling, competitive traps, win themes

## Writing Framework

### For Public Pages

**1. Acknowledge the competitor's strengths first.**
This builds credibility. If you pretend they have no strengths, readers dismiss everything else.

**2. Compare on dimensions, not features.**
- Speed, ease of use, pricing model, support quality, integration depth
- Feature checklists feel biased. Dimension comparisons feel fair.

**3. Be specific about differences.**
- Bad: "We're easier to use"
- Good: "Setup takes 5 minutes vs their 2-hour onboarding. Here's why..."

**4. Let customers speak.**
- Quotes from people who switched from the competitor
- G2/Capterra review excerpts (with attribution)

**5. Include a fair comparison table.**

| Feature | You | Competitor |
|---------|-----|-----------|
| ... | Specific detail | Specific detail |

Use checkmarks sparingly. Specific details are more credible than green checks.

### For Battle Cards

**Structure:**
1. **Competitor overview** — What they do, who they serve, pricing
2. **Where they win** — Be honest so reps aren't blindsided
3. **Where we win** — Lead with the strongest differentiators
4. **Common objections** — "But [competitor] has X..." with responses
5. **Competitive traps** — Questions to ask that highlight your strengths
6. **Proof points** — Customers who switched and their results

## Output Format

**Public page:** Full markdown with H2 sections, comparison table, CTA
**Battle card:** Save to outputs/battlecard-[competitor].md

## Principles
- Honesty converts better than bias. Readers see through one-sided comparisons.
- Update regularly — competitors ship features too
- Never trash the competitor's team or company — compare products, not people
- Include a "When to choose [competitor]" section. It builds massive credibility.