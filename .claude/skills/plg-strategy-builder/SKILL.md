---
name: plg-strategy-builder
description: Build a product-led growth strategy covering free tier design, self-serve conversion, expansion mechanics, and the transition to sales-assist. Use when launching a PLG motion, redesigning pricing tiers, or adding self-serve to an existing sales-led product.
triggers:
  - product-led growth
  - PLG strategy
  - self-serve growth
  - free tier design
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# PLG Strategy Builder

Product-led growth means the product itself drives acquisition, activation, retention, and expansion. Users discover value through usage, not through a sales pitch. The product is the primary growth engine.

## Phase 1 — PLG Readiness Assessment

Not every product is suited for PLG. Evaluate fit:

| Criterion | Your Product | PLG Fit? |
|-----------|-------------|----------|
| Can users get value without talking to a human? | [yes/no] | [required] |
| Is the product understandable in under 5 minutes? | [yes/no] | [strong signal] |
| Can a single user start and later bring in their team? | [yes/no] | [required for expansion] |
| Is the value experienced, not just promised? | [yes/no] | [required] |
| Can you offer a meaningful free tier without bankrupting the business? | [yes/no] | [required for freemium] |

**PLG fit score:** Count the "yes" answers. 5/5 = strong fit. 3/5 = possible with investment. Below 3 = reconsider.

## Phase 2 — Design the Free Tier

The free tier is your acquisition engine. It must be genuinely useful, not a demo.

### Free Tier Principles
1. **Enough to deliver value.** Users should hit the "aha moment" without paying.
2. **Natural upgrade triggers.** Usage, team size, or feature needs should create organic upgrade pressure.
3. **No artificial crippling.** Disabled features that are visible but locked feel manipulative. Instead, limit by volume, usage, or scale.

### Tier Design
| Tier | Price | Who It's For | Key Limits | Upgrade Trigger |
|------|-------|-------------|------------|----------------|
| Free | $0 | [persona] | [what's limited] | [what makes them need more] |
| Pro | [$X/mo] | [persona] | [what's expanded] | [what pushes toward enterprise] |
| Enterprise | [custom] | [persona] | [unlimited + extras] | [sales-assist] |

## Phase 3 — Self-Serve Conversion

Design the path from free to paid without requiring human intervention:

### Conversion Triggers
| Trigger | Detection | Action |
|---------|-----------|--------|
| Usage approaches limit | Track usage metrics | Show usage bar, gentle nudge |
| Team growth | New invites sent | Show team plan benefits |
| Advanced feature needed | Feature gate interaction | Explain what's available on paid |
| Time threshold | Days since activation | Summary of value received, upgrade offer |

### Conversion Experience
- **In-product upgrade flow.** No redirect to a sales page. Credit card entry within the product.
- **Transparent pricing.** No "contact us" for standard tiers. Show the price.
- **Trial of paid features.** Let users try before committing. Time-limited access to paid tier.
- **Social proof at the decision point.** Show who else uses the paid tier and what they achieved.

## Phase 4 — Expansion Mechanics

How do existing customers grow their spend?

| Expansion Vector | Mechanism | Measurement |
|-----------------|-----------|-------------|
| Seat expansion | More team members added | Seats added per account per quarter |
| Usage expansion | More consumption of metered features | Usage growth per account |
| Tier upgrade | Move to higher plan | Upgrade rate per cohort |
| Cross-sell | Additional products or modules | Cross-sell attach rate |

### Product Qualified Leads (PQLs)
Define signals that indicate a free user is ready for sales outreach:

| PQL Signal | Threshold | Action |
|-----------|-----------|--------|
| [usage metric] | [threshold] | [sales touch type] |
| [team size] | [threshold] | [outreach approach] |
| [feature gate hits] | [threshold] | [upgrade offer] |

## Phase 5 — Metrics Dashboard

| Metric | Definition | Target | Current |
|--------|-----------|--------|---------|
| Free → Paid conversion | % of free users who become paid within 90 days | [%] | [%] |
| Time to paid | Median days from signup to first payment | [days] | [days] |
| Expansion revenue rate | MoM revenue growth from existing customers | [%] | [%] |
| Net Revenue Retention | Revenue from existing customers vs. same period prior year | [%] | [%] |
| PQL → Customer rate | % of PQLs that convert to paid | [%] | [%] |

## Output

Write to `outputs/plg-strategy-[date].md`:

1. **PLG readiness** — assessment and gaps to address
2. **Tier design** — free, paid, enterprise with limits and triggers
3. **Self-serve conversion** — triggers, experience, and expected rates
4. **Expansion playbook** — how customers grow their spend
5. **PQL definitions** — signals and sales handoff criteria
6. **Metrics** — dashboard with targets

## Do NOT
- Give away too much on free — you need natural upgrade pressure
- Gate features artificially — users can tell, and it erodes trust
- Skip the PQL definition — without it, sales and product will conflict
- Assume PLG means no sales team — PLG + sales-assist outperforms pure self-serve for most B2B products