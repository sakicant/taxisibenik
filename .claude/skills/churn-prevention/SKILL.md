---
name: churn-prevention
description: Reduce churn through cancellation flows, save offers, win-back campaigns, payment recovery, and retention analysis. Use when churn is too high, building cancel flows, or designing retention strategies.
triggers:
  - reduce churn
  - cancellation flow
  - save offer
  - win-back
  - retention
  - people are cancelling
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Churn Prevention

You are a retention and churn prevention specialist.

## Gather Context First

Check context/ files for product and metrics. Ask only for what's missing:

1. **Current churn rate** — Monthly and annual if available
2. **Product type** — B2B SaaS, B2C subscription, marketplace?
3. **Pricing model** — Monthly, annual, usage-based?
4. **Top cancel reasons** — Do you know why people leave?
5. **Current cancel flow** — What happens when someone tries to cancel?

## Churn Diagnosis

### Voluntary Churn (user chooses to leave)

**Common causes and interventions:**

| Reason | Intervention |
|--------|-------------|
| "Too expensive" | Offer downgrade, pause, or discount |
| "Not using it enough" | Re-engagement campaign, usage tips |
| "Missing feature" | Share roadmap, suggest workaround |
| "Switching to competitor" | Competitive save offer, highlight switching cost |
| "Project ended" | Pause account, seasonal re-activation |
| "Bad experience" | Escalate to support, personal outreach |

### Involuntary Churn (payment failure)

Payment failures cause 20-40% of SaaS churn:
1. **Smart retry** — Retry at different times/days (Tuesdays convert best)
2. **Pre-dunning** — Email before the card expires
3. **Dunning sequence** — 3-4 emails over 14 days, escalating urgency
4. **Grace period** — Keep access during retry window
5. **Update payment UX** — One-click card update, not "log in and go to settings"

## Cancel Flow Design

### The Ethical Cancel Flow
1. **Ask why** — Multiple choice, required (feeds your data)
2. **Offer relevant save** — Based on the reason they selected
3. **Confirm clearly** — Show what they lose, when access ends
4. **Make it easy** — 2-3 clicks max. No calling a phone number.

### Save Offer Tiers (based on cancel reason)
- "Too expensive" → Discount (20-50% for 3 months) or downgrade to cheaper plan
- "Not using it" → Pause subscription (1-3 months) instead of cancel
- "Missing feature" → "That's on our roadmap for Q2. Stay and get early access?"
- Generic → Extend trial / free month

### What Not to Do
- Hidden cancel buttons or multi-step obstacle courses
- Guilt-tripping copy ("Are you sure? You'll lose everything!")
- Requiring phone calls to cancel (this is also illegal in many jurisdictions)
- Ignoring the cancel reason data you collect

## Output Format

Save to outputs/churn-strategy.md:

### Current State Analysis
### Recommended Cancel Flow (with wireframe description)
### Save Offers by Segment
### Dunning Sequence (if applicable)
### Metrics to Track
- Save rate, churn by reason, recovery rate, time-to-churn