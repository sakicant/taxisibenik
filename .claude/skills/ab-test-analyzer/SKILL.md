---
name: ab-test-analyzer
description: Analyze A/B test results for emails, landing pages, ads, CTAs, and outreach variants. Checks whether a variant has enough data to call a winner, flags underpowered tests, and recommends the next action.
triggers:
  - which variant won
  - analyze ab test
  - is this test significant
  - call the winner
  - test results
allowed-tools: [Read, Write]
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# A/B Test Analyzer

You turn raw variant results into a decision. Most teams call winners too early and carry losing variants forward. Be honest about what the data supports.

## Gather Context First

Ask for or read:
1. **Variants** — names and what differs (subject, body, CTA, layout).
2. **Primary metric** — opens, clicks, replies, signups, revenue. Secondary metrics are tie-breakers only.
3. **Counts per variant** — impressions/sent and conversions.
4. **Segment** — single audience or segmented? Cross-segment variance matters.
5. **Stopping rule** — was the sample size decided in advance, or monitored continuously?

## Analysis Steps

### Step 1 — Check sample size
For a 2-variant test on a proportion, the rough minimum per variant for a 5-point lift from a 10% base rate is ~1,500. Under 500 per variant is almost always underpowered. Flag this up front.

### Step 2 — Compute per-variant rate
Report rate = conversions / impressions for each variant with a 95% confidence interval:
- CI half-width ≈ 1.96 * sqrt(p * (1 - p) / n)
- If intervals overlap substantially, the test is inconclusive.

### Step 3 — Significance test
Two-proportion z-test:
- z = (p1 - p2) / sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
- |z| > 1.96 → p < 0.05, a candidate winner.
- |z| > 2.58 → p < 0.01, higher confidence.

For >2 variants, run a chi-squared test across the contingency table. If significant, do pairwise comparisons with a Bonferroni adjustment.

### Step 4 — Check segments
If the test ran across distinct segments (enterprise vs SMB, new vs returning), run the test per segment. A variant can win overall but lose in the most valuable segment. Flag Simpson's paradox when it appears.

### Step 5 — Decide
- **Winner**: significance reached, effect size meaningful, segment check consistent.
- **Keep running**: trending but underpowered. Estimate days to reach minimum sample.
- **No effect**: enough data, no difference. Ship the simpler/cheaper variant.
- **Inconclusive**: not enough data, no clear trend. Redesign or extend.

## Output Format

Save to `outputs/experiments/[test-name].md`:

```markdown
# A/B Test: [name]
Period: [start] to [end]
Primary metric: [metric]

## Variants
| Variant | Description | Sent | Conversions | Rate | 95% CI |
|---------|-------------|------|-------------|------|--------|

## Test Result
Z-score: __   p-value: __   Relative lift: __%

## Segment Breakdown
| Segment | Winning variant | Lift | Note |
|---------|-----------------|------|------|

## Decision
[Winner | Keep running | No effect | Inconclusive]

## Reasoning
[2-4 sentences]

## Next Action
[Ship winner to full audience | Extend test until [date] | Redesign with [change] | Retire test]

## Captured Learning
[One-sentence insight to add to the intelligence log]
```

## Do NOT
- Call a winner on fewer than a few hundred conversions unless the effect is massive.
- Peek early and stop the moment p crosses 0.05. That inflates false positives.
- Ignore segment reversals. Overall lift hides local losses.
- Report only the relative lift ("2x better!"). Always show absolute rates and the base.
- Carry forward a losing variant because "it felt better." Write down what the test says.