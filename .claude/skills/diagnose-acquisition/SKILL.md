---
name: diagnose-acquisition
description: Analyze acquisition sources to understand channel quality, cost efficiency, and scalability. Use when evaluating marketing spend, planning channel expansion, or investigating declining growth.
triggers:
  - diagnose acquisition
  - acquisition analysis
  - channel analysis
  - where do users come from
  - CAC analysis
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Acquisition Diagnostician

Not all users are equal. A channel that drives 10,000 signups means nothing if none of them activate. Evaluate acquisition by what happens after the signup, not just the signup itself.

## Phase 1 — Map Current Channels

List every channel that drives new users, with volume and cost:

| Channel | Monthly Users | Monthly Cost | Cost Per User | % of Total |
|---------|--------------|-------------|---------------|------------|
| Organic search | [n] | [cost] | [cpu] | [%] |
| Paid search | [n] | [cost] | [cpu] | [%] |
| Social organic | [n] | [cost] | [cpu] | [%] |
| Social paid | [n] | [cost] | [cpu] | [%] |
| Referral | [n] | [cost] | [cpu] | [%] |
| Direct | [n] | [cost] | [cpu] | [%] |
| Content/SEO | [n] | [cost] | [cpu] | [%] |
| Partnerships | [n] | [cost] | [cpu] | [%] |
| Other | [n] | [cost] | [cpu] | [%] |

## Phase 2 — Measure Channel Quality

Volume and cost are not enough. Evaluate what happens downstream:

| Channel | Signup→Activation | Week-4 Retention | Revenue/User | LTV |
|---------|-------------------|-----------------|-------------|-----|
| [channel] | [%] | [%] | [$] | [$] |

**Channel quality score** = Activation rate x Retention rate x LTV

Sort by quality score. The best channel is not the cheapest or the largest — it is the one that produces the most long-term value per dollar spent.

## Phase 3 — Evaluate Scalability

For each channel, assess whether you can profitably increase investment:

| Channel | Quality | Current Scale | Ceiling | Scalability |
|---------|---------|--------------|---------|-------------|
| [channel] | High/Med/Low | [current spend] | [max before diminishing returns] | High/Med/Low |

### Scalability Factors
- **Organic search:** Scales with content investment, slow but compounding
- **Paid search:** Scales with budget, but CPCs increase as you exhaust high-intent keywords
- **Social organic:** Scales with content quality and consistency, hard to predict
- **Social paid:** Scales with budget and creative refresh, audience fatigue is real
- **Referral:** Scales with product quality, hard to force
- **Partnerships:** Scales with relationship investment, lumpy and unpredictable

## Phase 4 — Identify Opportunities and Risks

### Concentration Risk
If more than 50% of acquisition comes from one channel, that is a risk. Document:
- What happens if that channel's cost doubles?
- What happens if the channel changes its algorithm or policies?
- What is your backup if the channel underperforms for a quarter?

### Untapped Channels
List channels you are not using and evaluate potential:

| Channel | Estimated Audience Fit | Required Investment | Expected Timeline | Priority |
|---------|----------------------|--------------------|--------------------|----------|
| [channel] | [how well does the audience match] | [time, money, people] | [months to results] | [H/M/L] |

## Output

Write to `outputs/acquisition-diagnosis-[date].md`:

1. **Channel map** — all channels with volume, cost, and quality metrics
2. **Quality ranking** — channels sorted by downstream value
3. **Scalability assessment** — where you can profitably grow
4. **Risks** — concentration risk and channel dependencies
5. **Recommendations** — where to increase, maintain, or reduce investment

## Do NOT
- Optimize purely for cost per acquisition — cheap users who churn are expensive
- Ignore attribution complexity — most users touch multiple channels
- Assume past performance predicts future returns — channels saturate
- Mix paid and organic metrics without noting the difference in cost structure