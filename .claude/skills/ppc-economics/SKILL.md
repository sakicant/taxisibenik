---
name: ppc-economics
description: Build PPC financial models — LTV, CAC, payback period, target CPA, target ROAS — to set defensible ceiling bids and channel budgets. The unit-economics layer underneath ad-spend-allocator. Use when user mentions PPC economics, ad math, ad payback, target CPA, target ROAS, or ad unit economics.
triggers:
  - ppc economics
  - ad math
  - ad payback
  - target cpa
  - target roas
  - ad unit economics
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# PPC Economics

Build the financial model under your paid advertising. Without it, ad spend allocation is guessing. With it, every channel and campaign decision has a defensible ceiling.

## Gather context

Ask if not provided:

1. **Business model** — SaaS subscription, transactional / e-commerce, marketplace?
2. **Pricing** — average order value (transactional), ARPU (subscription), take rate (marketplace)?
3. **Customer lifetime metrics** — gross margin, churn rate, expansion rate?
4. **Cohort data available?** — actual LTV from historicals, or just modeled?
5. **Goal** — set channel budgets, set max bid per channel, justify ad spend to leadership?

## Core formulas

### Lifetime Value (LTV)
For SaaS:
```
LTV = ARPU × Gross Margin × (1 / (Monthly Churn Rate))
```

For transactional:
```
LTV = AOV × Gross Margin × Orders Per Customer Lifetime
```

Watch out:
- Use **gross margin**, not revenue. A $1000 ARPU at 30% gross margin is $300 of contribution.
- Use **honest churn**. Customer churn (logos) and revenue churn (dollars) differ; use whichever the metric is for.
- Cap LTV at a realistic horizon (typically 24-36 months). Pure-math LTV with low churn is infinite and not useful.

### Customer Acquisition Cost (CAC)
```
Blended CAC = (Total Sales + Marketing Spend) / New Customers Acquired
Paid CAC = (Paid Ad Spend) / Customers Acquired Through Paid Channels
```

Use **paid CAC** for ad-channel decisions. Blended is for board reporting.

### CAC Payback Period
```
Payback (months) = CAC / (ARPU × Gross Margin)
```

Healthy ranges:
- SMB SaaS: under 12 months payback.
- Mid-market: 12-18 months.
- Enterprise: 18-24 months.
- Transactional / e-commerce: should be paid back on first or second order.

### LTV:CAC Ratio
```
LTV : CAC = LTV / Paid CAC
```

Healthy: >3:1. Anything under 1:1 means you're losing money on every customer.

### Target CPA (Cost Per Acquisition)
For ad bidding, the maximum you can pay for a conversion:
```
Target CPA = LTV / Desired LTV:CAC Ratio
```

If LTV is $3000 and you want 3:1 LTV:CAC, target CPA is $1000.

### Target ROAS (Return On Ad Spend)
For e-commerce / transactional:
```
Target ROAS = Revenue / Ad Spend
```

Set Target ROAS as: 1 / (Gross Margin × (1/Desired Markup)). For a 30% gross margin business with a 3x markup target, Target ROAS is roughly 11x.

## Workflow

### Step 1: Compute the inputs
Pull from the finance system, CRM, and ad platforms:
- ARPU (or AOV).
- Gross margin.
- Churn rate (monthly customer + revenue).
- Paid spend by channel.
- New customers by channel.

### Step 2: Build the model
Save to a spreadsheet (use `xlsx-handler` if working in code). Layout:
- Sheet 1: Inputs (named cells, blue text).
- Sheet 2: Calc (formulas referencing inputs).
- Sheet 3: Output (the LTV, CAC, payback, ratio, target CPA / ROAS by channel).

### Step 3: Validate against actuals
For each channel, check:
- Actual CAC vs. target CPA — over or under?
- Cohort retention vs. churn assumption — is your LTV model holding up against real cohorts?
- Adjust assumptions where reality diverges.

### Step 4: Set channel budgets
For each channel:
- Channel-specific target CPA = Target CPA × channel quality factor (some channels yield lower-LTV customers).
- Monthly budget = Target volume × Target CPA.
- Daily cap = Monthly / 30.

### Step 5: Decision triggers
- If channel CPA exceeds target by 25% for two weeks, pause/reduce budget.
- If channel CPA is under target by 25% for two weeks, increase budget.
- If LTV:CAC drops below 2:1, escalate.

## Output format

Save the model to `outputs/ppc-economics/model-<date>.xlsx` plus a narrative at `outputs/ppc-economics/model-<date>-summary.md`:

```
## PPC economics — <date>

## Inputs (cited)
- ARPU: $X (source: <link>)
- Gross margin: N% (source: <link>)
- Monthly churn: N% (source: <link>)

## Computed
- LTV: $X (capped at <horizon>)
- Target LTV:CAC: <ratio>
- Target CPA: $X
- Target payback: <months>

## Per channel
| Channel | Paid CAC | vs Target | Action |
|---|---|---|---|
| Google Search | $X | over/under | <pause/grow> |
| Meta | $X | ... | ... |
| LinkedIn | $X | ... | ... |

## Recommendations
- <budget allocation>
- <channels to scale>
- <channels to pull back>
- <metric drift to monitor>
```

## Common mistakes

- Using revenue instead of gross margin in LTV. Inflates the number.
- Using infinite-horizon LTV. Theoretically valid; practically dangerous.
- Treating blended CAC as if it can guide channel-level decisions. It can't.
- Setting target CPA once and never refreshing as cohorts mature.
- Ignoring channel quality — a $X customer from one channel may have very different LTV than from another.

## Cross-references

For ad-spend allocation across channels, use `ad-spend-allocator`. For platform-specific audits, use `google-ads-auditor`, `meta-ads-auditor`. For SaaS metrics generally, use `saas-metrics-coach`. For the underlying financial model, use `financial-model-builder`. For landing pages tied to PPC, use `ads-landing-audit`.
