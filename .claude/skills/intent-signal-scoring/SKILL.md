---
name: intent-signal-scoring
description: Build a scoring model that combines first-party (web, content, in-app) and third-party (G2, Clearbit, 6sense) signals into a buying-intent score per account. Tells sales WHEN to reach out, not just WHO to target. Use when user mentions intent data, intent scoring, buying signals, when to reach out, or sales triggers.
triggers:
  - intent signals
  - buying intent
  - intent score
  - when to reach out
  - sales triggers
  - signal scoring
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Intent Signal Scoring

Build a model that scores accounts by buying intent so sales spends time on accounts that are actually in-market right now, not on every name in the database.

## Gather context

Ask if not provided:

1. **Available signals** — what first-party data exists (web analytics, content engagement, product trial activity, in-app behavior)?
2. **Third-party intent sources** — G2, Clearbit, Bombora, 6sense, Common Room, ZoomInfo, Apollo intent, others?
3. **Sales motion** — outbound SDR-led? Inbound-routed? PLG with motion?
4. **CRM** — where the score lives and what triggers it can fire (route to SDR, alert AE, etc.).
5. **Resource cap** — how many "in-market" accounts can sales actually work in a week? This sets the threshold.

## The signal taxonomy

Group signals into three buckets:

### Surge / spike signals (real-time, transient)
Most predictive when fresh. Decay quickly.

| Signal | Source | Decay |
|---|---|---|
| Pricing page visit (multiple in 7 days) | Web analytics | 7 days |
| Demo request or "contact sales" form | Forms | 30 days but treat as immediate |
| Multiple stakeholders from same company on the site | Reverse-IP / Clearbit Reveal | 14 days |
| Comparison page visit ("us vs competitor") | Web analytics | 14 days |
| 3rd-party intent surge (Bombora, 6sense category spike) | Vendor | 30 days |

### Identifier signals (durable, accumulate)
Less time-sensitive but stack into a clearer picture.

| Signal | Source | Persistence |
|---|---|---|
| Job change in target role at target account | LinkedIn / Apollo / vendor | 90 days |
| Funding event (Series A/B) | Crunchbase | 180 days |
| Hiring spree in target function | Job boards | 90 days |
| New tooling adoption visible in tech stack | BuiltWith / Wappalyzer | Ongoing |
| Public roadmap or earnings mention of relevant initiative | Press / earnings | Quarterly refresh |

### Engagement signals (warm, ongoing)
Direct interaction with your brand. Cumulative.

| Signal | Source | Weight |
|---|---|---|
| Content downloaded | Marketing automation | Low (single touch) |
| Webinar attended | Marketing automation | Medium |
| Repeated email opens / clicks (3+ in 30 days) | Marketing automation | Medium |
| Community / Discord participation | Custom | Medium-high |
| Free tool used | Product analytics | Medium-high |
| Trial signup | Product analytics | High |
| Reply to outbound email | CRM | High |

## Scoring math

Two approaches:

### Simple (start here)
Assign points per signal. Sum within a rolling 30-day window:

- Surge signal: 10-30 points each.
- Identifier signal: 5-15 points each.
- Engagement signal: 1-10 points each.

Set thresholds:
- Under 20: not in-market. Marketing nurture.
- 20-49: warming up. Light SDR touch.
- 50-99: in-market. Active SDR + AE pursuit.
- 100+: hot. Multi-thread immediately.

Calibrate thresholds against historical conversion data after 8-12 weeks of running the model.

### Weighted multivariate (when you have data)
Once you have 100+ scored opportunities-to-closed-won outcomes, regress signal-types on conversion to find optimal weights. Use a simple logistic regression — fancier models don't help with this small a feature set.

## Triggering action

Score isn't useful unless it routes work. Per threshold:

- **20-49**: monthly nurture email; light SDR check-in if they hit two consecutive periods at this level.
- **50-99**: SDR assigned within 48 hours, target outreach within 1 week.
- **100+**: alert AE within 24 hours, multi-thread within 1 week, ABM-tier treatment.

Build the routing in the CRM with explicit SLAs. Track them — SLA misses are a leading indicator of pipeline shortfall.

## Output format

Save the scoring model design to `outputs/intent-scoring/<date>-model.md`:
- Signal taxonomy with sources and weights.
- Threshold definitions and routing rules.
- SLA per threshold.
- Weekly accounts-by-threshold dashboard structure.
- Calibration plan (how and when to revisit weights).

For the operational dashboard: `outputs/intent-scoring/dashboard-template.md` with the rollup view sales/marketing leadership reviews weekly.

## Common mistakes

- Equal weights to all signals. A demo request and a content download are not the same.
- Scoring stays static. Decay isn't enforced; ancient signals stay in the score forever.
- No threshold action. Score exists, sales ignores it.
- Over-engineering the model before having data to validate it. Start simple.
- One score for all account sizes. SMB and enterprise have different signals worth different weights.

## Cross-references

For the broader ABM context, use `abm-orchestration`. For the sales-marketing alignment that makes the score actionable, use existing `revops-analyst`. For pipeline review against the resulting accounts, use `sales-pipeline`. For the cold outreach triggered by high scores, use `cold-email-writer` and `sales-outreach-writer`.
