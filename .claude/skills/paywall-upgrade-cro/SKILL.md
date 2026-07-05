---
name: paywall-upgrade-cro
description: Optimize in-app paywalls, upgrade screens, feature gates, and plan-switching UX. The audience is already inside the product; the job is conversion to paid or higher tier. Distinct from page-cro (marketing) and signup-flow-optimizer (acquisition).
triggers:
  - paywall optimization
  - upgrade screen
  - feature gate
  - upgrade flow
  - plan upgrade
  - in-app monetization
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Paywall & Upgrade CRO

Optimize the moment when a user inside the product encounters paid value. Paywalls fail in three patterns: bad timing, bad framing, bad friction.

## Gather context

Ask if not provided:

1. **Trigger moment** — when does the paywall appear? (Feature attempt, usage limit hit, free trial ending, manual upgrade click)
2. **User state** — free user, trial user, lapsed paid user?
3. **Plans** — pricing tiers, feature gates per tier?
4. **Current performance** — paywall view rate, upgrade conversion rate, dismissal rate?
5. **Brand voice** — playful, professional, urgent? Affects copy.

## The three failure modes

### 1. Bad timing
The paywall appears before the user has experienced enough value to want to pay.

Fix:
- Trigger paywalls AFTER the user has succeeded with the free product, not at first use.
- Usage limits should kick in once the user is dependent (e.g., "you've created 3 projects this month, upgrade for unlimited") rather than artificially low.
- For trial-end paywalls: ensure trial length is long enough to form habit (typically 7-14 days for B2B SaaS, 7 days for consumer).

### 2. Bad framing
The paywall describes features instead of outcomes.

Fix:
- Lead with what the user gains, not what they unlock.
- "Unlock unlimited projects" -> "Keep building without limits"
- Show, don't tell — preview the locked feature where possible (e.g., grayed-out screenshot of the dashboard you'd get).
- Anchor to value the user has already created in the free version.

### 3. Bad friction
Too many steps from "yes I'll upgrade" to "thank you for your payment."

Fix:
- Single click to upgrade for users with payment on file.
- Pre-fill billing details from existing account info.
- Stripe / payment-processor checkout instead of custom form.
- Confirm upgrade in <60 seconds.
- For team plans: don't require admin approval if user is admin. Don't require IT approval at the paywall — handle that separately for enterprise.

## Plan-switching UX

Beyond the upgrade moment, plan switching should be:
- Self-serve (no contact-sales required for standard up/down moves).
- Pro-rated immediately or at next billing cycle (state which clearly).
- Reversible — let the user downgrade easily. Friction on downgrade builds resentment, not retention.

## Trial-to-paid specifically

Trial-end is the highest-stakes paywall.

- **Show the user what they built** during the trial. Loss aversion is the best motivator.
- **Email cadence**: T-7 days, T-3 days, T-1 day, expiration day, T+1 day. Each email different angle.
- **Don't auto-charge** at trial end without explicit confirmation, unless the user opted in upfront and you remind them clearly.
- **Soft churn**: when trial ends, downgrade to free tier instead of full lockout where possible. Re-engage them later instead of losing them entirely.

## Upgrade prompts during normal usage

The "you hit a limit" prompt:
- State the limit hit clearly.
- Show what upgrading enables, with specifics ("upgrade to Pro for unlimited projects + advanced analytics").
- Offer "remind me later" option (not just upgrade-or-leave).
- Track click-through but don't penalize dismissal.

## Workflow

### Step 1: Audit the current paywall(s)
List every place a user encounters a paywall:
- Feature gates (clicking on locked features).
- Usage limits.
- Trial expiration.
- Upgrade nudges in product.
- Plan-comparison page.

For each: trigger, copy, conversion rate, dismissal rate.

### Step 2: Identify the highest-leverage one
The one with highest view volume × lowest conversion rate. Fix that first.

### Step 3: Apply the framework
- Timing: is it appearing too early?
- Framing: outcome-led copy?
- Friction: minimum clicks to upgrade?

### Step 4: A/B test
Paywall changes are some of the highest-impact tests in SaaS. Common test ideas:
- Headline framing (feature vs outcome).
- Trial length (7 vs 14 days).
- Pricing display (monthly vs annual primary).
- "Most popular" badge placement.

## Output format

Save audit to `outputs/paywall-cro/<paywall-slug>-<date>.md`:

```
## Paywall audit: <which paywall>
- Trigger: ...
- Audience: ...
- Current performance:
  - View rate: <%>
  - Click-to-upgrade rate: <%>
  - Completion rate (click to paid): <%>

## Findings
- Timing: ...
- Framing: ...
- Friction: ...

## Recommended changes
1. <change> — <expected lift>

## A/B test plan
[Variant A vs B with hypothesis]
```

## Common mistakes

- Showing paywalls too early. User hasn't experienced enough value yet.
- Listing features instead of outcomes.
- Hiding pricing until late in the upgrade flow.
- Long upgrade flows with re-asking for billing info already on file.
- Auto-charging at trial end without clear opt-in.
- Friction on downgrade. Resentment > retention savings.

## Cross-references

For first-time signup conversion, use `signup-flow-optimizer`. For lead-capture forms, use `form-cro`. For modals and popups, use `popup-cro`. For pricing strategy underneath the paywall, use `pricing-strategist`. For onboarding-flow CRO that comes between signup and the first paywall, use `onboarding-cro`.
