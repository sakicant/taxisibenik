---
name: cmo-advisor
description: CMO-level strategic counsel. Brand vs demand allocation, marketing org design, go-to-market strategy at exec level, marketing leadership. For tactical marketing skills use the marketing role. This is the leadership layer.
triggers:
  - cmo strategy
  - marketing leadership
  - brand vs demand
  - marketing org
  - cmo advisor
  - gtm strategy at exec level
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# CMO Advisor

CMO-level advice for the marketing leader. The CMO operates one layer above tactical execution: choosing which fights to fight, structuring the org, and connecting marketing investment to business outcomes.

## Gather context

Ask if not provided:

1. **Stage** — pre-PMF, growth ($1M-$10M ARR), scale ($10M-$100M), mature?
2. **Sales motion** — PLG, sales-led, hybrid?
3. **Current state** — marketing team size, structure, current focus?
4. **Decision** — brand investment, demand investment, hiring, agency vs in-house, channel bets?
5. **Constraints** — budget, runway, leadership expectations?

## Brand vs demand allocation

The CMO's signature question. There's no universal right answer; it depends on stage and motion.

**Pre-PMF**: 0% brand, 100% demand (and even demand is constrained — most spend should validate ICP and message).

**Growth ($1M-$10M)**: 80% demand, 20% brand. Brand investment is mostly content marketing that compounds.

**Scale ($10M-$100M)**: 60-70% demand, 30-40% brand. As CAC rises, brand investment lowers it indirectly.

**Mature**: 50/50 or even brand-heavy. At maturity, brand is the moat.

These are guidelines. Adjust based on:
- **Channel saturation** — when paid channels saturate, brand becomes higher-leverage.
- **Buyer behavior** — long-cycle B2B (12+ month) needs more brand to be present in the consideration window.
- **Competitive intensity** — well-funded competitors raise the brand bar.

## Marketing org design

Stage-appropriate org structure:

### Pre-PMF (1-2 marketers)
- Generalist marketer + content/copywriter.
- CMO is often the founder.

### Growth (3-10 marketers)
- Director of marketing (+) running 2-3 streams.
- Streams: demand gen + content + product marketing.
- No agency needed for most things; specialist contractors fine.

### Scale (10-30 marketers)
- VP marketing.
- Sub-functions: demand gen (own paid + lifecycle), content (own brand + organic), product marketing (own messaging + sales enablement), brand/communications, marketing ops.
- 1 manager per sub-function.

### Mature (30+ marketers)
- CMO with VPs reporting.
- VPs of: demand, brand, product marketing, content, marketing ops.
- Sub-specialists in each.

Common mistakes in org design:
- Too many specialists too early (low utilization).
- Demand generation reporting to product marketing (different optimization functions).
- Marketing operations underbuilt (kills attribution and measurement).
- Customer marketing missing entirely (huge expansion lever ignored).

## GTM strategy at exec level

CMO drives the GTM narrative. Three components:

### Positioning
What category we're in, who we're for, why us. See `positioning-generator` for the tactical work; the CMO owns the answer.

### Messaging hierarchy
The 3-5 messages we lead with, in priority order. See `messaging-hierarchy`. CMO holds the line against constant message dilution.

### Channel mix
Where we play and where we don't. Marketing teams that try every channel become mediocre at all of them. The CMO's job is saying no to channels that don't fit.

## Reporting up

The CMO owes the CEO and board:
- **Monthly**: pipeline contribution by channel, top-of-funnel health, customer cohort behavior.
- **Quarterly**: brand health metrics, share of voice, NPS shifts, narrative alignment.
- **Annually**: strategic narrative refresh, channel mix evolution, org changes.

Marketing accountability is hard because lag time is long. The CMO must build leading indicators (search volume, content engagement, brand search) that predict lagging revenue impact.

## Reporting in

Marketers report to the CMO. Common pitfalls:
- VP of demand who's actually a campaign manager (no strategic input).
- VP of brand without measurable impact (just creative output).
- Performance marketers without business context.
- Content team disconnected from product marketing.

The CMO connects them.

## Output format

Save advisory notes to `outputs/cmo-advisor/<topic>-<date>.md`:

```
## CMO advisory: <topic>
- Stage: <stage>
- Sales motion: <type>

## Current state
[What's working, what's not, where the gaps are]

## Recommendation
[Specific direction with reasoning]

## Resourcing implications
[Hiring, budget shifts, agency vs in-house]

## Measurement
[How we'll know this is working]

## Watchouts
[Risks, dependencies, time-to-impact realism]
```

## Common mistakes

- Optimizing for short-term pipeline at the cost of brand decay.
- Hiring specialists before generalists have proven the function.
- Saying yes to every channel; building five mediocre programs.
- Marketing ops underbuilt; can't measure what's working.
- Avoiding the "kill the program" decision when something isn't working.

## Cross-references

For tactical marketing skills, see all the marketing-tagged skills (positioning-generator, messaging-hierarchy, brand-voice-builder, etc.). For demand generation specifics, use `marketing-funnel-mapper` and `paid ads` skills. For content strategy, use `launch-playbook` and content-related skills. For board reporting on marketing, use `board-deck-builder`.
