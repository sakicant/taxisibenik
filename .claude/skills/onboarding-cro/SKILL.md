---
name: onboarding-cro
description: Optimize the post-signup onboarding flow — first-run experience, activation, time-to-value, "aha" moment. Distinct from signup-flow-optimizer (signup itself), onboarding-designer (longer-term human program), and paywall-upgrade-cro (monetization moment).
triggers:
  - onboarding flow
  - first-run experience
  - time to value
  - activation
  - aha moment
  - new user activation
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Onboarding CRO

Optimize the period from signup to first meaningful value. The single highest-leverage CRO area for most products — bad onboarding wastes acquisition spend, good onboarding compounds retention.

## Gather context

Ask if not provided:

1. **Product type** — B2B SaaS, consumer app, marketplace, dev tool?
2. **Current onboarding** — what does it look like? Tour, checklist, empty state, free-form?
3. **Activation metric** — is there a defined "activated" state? What is it (key action, multi-action, time-based)?
4. **Current activation rate** — % of signups that activate within target window?
5. **Drop-off pattern** — where in the flow do users churn?

## Define activation first

Before optimizing onboarding, the team must agree on what "activated" means. Without this, you can't measure improvement.

Good activation definitions:
- **Single key action** — "user invites teammate" / "user creates first project" / "user makes first AI request."
- **Multi-action threshold** — "user logs in 3 days in week one AND completes first project."
- **Time-bound retention proxy** — "user is still active on day 7."

Bad activation definitions:
- "User completes onboarding tour." (Tour completion ≠ value experienced.)
- "User is satisfied." (Unmeasurable.)

## The four onboarding patterns

Pick the one matching the product type. Don't mix.

### 1. Guided tour (legacy, mostly bad)
Sequential tooltips that walk through features. Most users skip. Avoid unless the product is genuinely complex and the tour is short (<30 seconds).

### 2. Empty state with prompts
Default state of every screen has "what to do here" guidance plus a primary CTA. Best for products where the user can immediately try something.

### 3. Setup checklist
List of 3-5 actions to complete. Visible progress. Best for B2B products with required setup (connect tools, invite team, configure).

### 4. Single-task funnel
Push the user toward ONE high-value action before opening the rest of the product. Best for products with a clear "wow" first action.

## The aha-moment principle

Identify the single action that, when a user takes it, retention dramatically improves. That's the aha moment. Onboarding's job is to get the user there as fast as possible.

To find it (if not yet defined):
- Pull retention curves segmented by feature usage in week 1.
- Find the feature(s) where users who use it have 2x+ retention.
- That's the aha.

Examples (illustrative):
- Slack: send 2000 messages.
- Dropbox: install on 2 devices.
- Facebook: 7 friends in 10 days.

These are post-hoc; find yours through your data.

## The friction audit

Walk through the actual flow as a new user, on mobile and desktop:
- Email verification — required? Why?
- Profile fields — required? Cut what's not.
- Setup steps — can defaults handle them?
- Time-to-first-action — count seconds from clicking the welcome email to doing the first meaningful thing.
- Empty states — does the user know what to do, or stare at a blank screen?

Cut every step that doesn't drive activation.

## Workflow

### Step 1: Define / confirm activation metric
If undefined, define it (see above).

### Step 2: Measure baseline
Activation rate, time-to-activation, drop-off points.

### Step 3: Walk through the flow yourself
Sign up as a new user. Note every friction point. Time it.

### Step 4: Pick highest-leverage fixes
- Friction: cut steps and required fields.
- Empty states: add prompts.
- Wrong path: re-sequence the flow.
- Missing first-action push: add a strong CTA toward the aha moment.

### Step 5: A/B test
Onboarding A/B tests are slow because activation is measured over days/weeks. Plan for 4-6 weeks of runtime per test.

## Day-2 to day-30 retention tactics

Onboarding extends past the first session. Email cadence:
- Day 0: welcome with a single clear CTA (the aha-moment action).
- Day 1: re-engagement if user hasn't activated.
- Day 3: feature highlight relevant to their use case.
- Day 7: check-in / NPS-style ("How's it going?").
- Day 14: tips or community invite.
- Day 30: graduation / power-user invitation.

Each email should be tied to user state — don't send "great job activating!" to users who didn't activate.

## Output format

Save audit / plan to `outputs/onboarding-cro/<product>-<date>.md`:

```
## Onboarding CRO audit: <product>
- Activation metric: <definition>
- Current rate: <%>
- Time to activation: <duration>
- Pattern: <tour / empty state / checklist / funnel>

## Drop-off map
[Each step with completion rate]

## Findings
1. <issue> — <fix>
2. ...

## Recommended changes
- Cut: <steps removed>
- Add: <prompts / CTAs added>
- Resequence: <if applicable>

## A/B test plan
- Variant A: current
- Variant B: <change>
- Metric: activation rate within <window>
- Sample size needed: ...
```

## Common mistakes

- No activation metric. Can't optimize what you can't measure.
- Overproducing the welcome experience (long tour, big setup) at the cost of time-to-value.
- One-size-fits-all. Different user segments often need different paths.
- Stopping at session 1. Onboarding extends 30+ days.
- A/B testing too aggressively. With slow-to-measure outcomes, you'll get false signals.

## Cross-references

For signup form/flow itself (not the post-signup experience), use `signup-flow-optimizer`. For paywalls during onboarding, use `paywall-upgrade-cro`. For email sequences supporting onboarding, use `email-sequence-builder`. For broader onboarding-as-program (humans, not just product), use `onboarding-designer`. For activation diagnosis, use `diagnose-activation`.
