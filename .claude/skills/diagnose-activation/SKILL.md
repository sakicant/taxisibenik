---
name: diagnose-activation
description: Analyze your activation funnel to find where new users drop off and why. Use when onboarding conversion is below target, after a product change, or when planning growth investments.
triggers:
  - diagnose activation
  - onboarding drop-off
  - activation funnel
  - new user conversion
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Activation Diagnostician

Activation is the moment a new user first experiences the core value of your product. If users sign up but never reach that moment, nothing else matters — retention, revenue, and referral all depend on activation happening first.

## Phase 1 — Define the Activation Event

The activation event is the single action that best predicts long-term retention. It is NOT "signed up" or "completed onboarding." It is the moment the user gets value.

### How to Find It
1. List candidate events (first project created, first report run, first message sent, first integration connected)
2. For each, compare retention curves: users who did the event within 7 days vs. users who did not
3. The event with the largest retention gap is your activation event

| Candidate Event | Day-30 Retention (did it) | Day-30 Retention (did not) | Gap |
|----------------|--------------------------|---------------------------|-----|
| [event] | [%] | [%] | [diff] |

**Current activation event:** [define it clearly]
**Current activation rate:** [% of signups who activate within X days]

## Phase 2 — Map the Funnel

Break the path from signup to activation into discrete steps. For each step, capture the conversion rate:

| Step | Description | Users Entering | Users Completing | Conversion |
|------|-------------|----------------|------------------|------------|
| 1 | Sign up | [n] | [n] | [%] |
| 2 | [next step] | [n] | [n] | [%] |
| ... | ... | | | |
| N | Activation event | [n] | [n] | [%] |

**Identify the biggest drop:** The step with the lowest conversion rate is where to focus.

## Phase 3 — Diagnose the Drop-Off

For the biggest drop-off point, investigate:

### User Behavior
- What do users who drop off actually do instead? (Leave? Get stuck? Explore elsewhere?)
- How long do they spend before leaving?
- Do they come back later, or is the drop permanent?

### Friction Points
| Friction Type | Examples | Evidence |
|--------------|----------|----------|
| Effort | Too many fields, complex setup, unclear instructions | Session recordings, form analytics |
| Confusion | Unclear value, jargon, unclear next step | Support tickets, heatmaps |
| Trust | Privacy concerns, price uncertainty, unfamiliar brand | Exit surveys, bounce pages |
| Technical | Slow load, errors, broken flows, device incompatibility | Error logs, performance data |

### Segment Analysis
Does the drop-off affect all users equally, or specific segments?
- By acquisition channel (organic vs. paid vs. referral)
- By device/platform
- By user type or role
- By geography

## Phase 4 — Design Improvements

For each identified friction point, propose a fix:

| Problem | Hypothesis | Proposed Change | Expected Impact | Effort |
|---------|------------|-----------------|-----------------|--------|
| [what's broken] | [why it's broken] | [specific change] | [activation rate delta] | [S/M/L] |

**Prioritize by:** Expected impact / Effort. Start with the highest ratio.

### Common Activation Patterns
- **Reduce time to value:** Can you get users to the activation event in fewer steps?
- **Progressive disclosure:** Show only what matters now, hide advanced features
- **Guided first run:** Walk the user through the activation event, not just the UI
- **Social proof at friction points:** Show that others completed this step successfully
- **Remove signup friction:** Can they experience value before creating an account?

## Output

Write findings to `outputs/activation-diagnosis-[date].md`:

1. **Activation definition** — the event and current rate
2. **Funnel map** — step-by-step conversion with the biggest drop highlighted
3. **Root cause analysis** — why users drop off at that step
4. **Improvement plan** — prioritized list of changes to test
5. **Success criteria** — target activation rate and timeline

## Do NOT
- Define activation as "signed up" or "logged in" — those are not value moments
- Optimize steps before the biggest drop-off — fix the worst leak first
- Propose changes without a measurement plan — every change should be testable
- Ignore qualitative data — numbers show where users drop, not why