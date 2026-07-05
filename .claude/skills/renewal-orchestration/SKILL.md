---
name: renewal-orchestration
description: Design and run a multi-step renewal program — 90/60/30/0-day playbook with structured touchpoints, value-realization meetings, executive sponsor outreach, and contract logistics. Distinct from renewal-strategist which handles a single deal. Use when user mentions renewal program, renewal motion, 90-day renewal cadence, or designing the renewal playbook.
triggers:
  - renewal program
  - renewal motion
  - 90 day renewal
  - 60 day renewal
  - renewal cadence
  - renewal playbook
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Renewal Orchestration

Design a renewal program that gets activated 90 days before each customer's contract date and runs through contract execution. Single-deal tactical work (e.g., negotiate one specific renewal) belongs in `renewal-strategist` — this skill is the program design.

## Gather context

Ask if not provided:

1. **Customer segments** — segments by ARR or tier (SMB, mid-market, enterprise) often need different cadences.
2. **Renewal type** — auto-renew with opt-out, opt-in, or active negotiation. Different economics.
3. **Contract length** — annual, multi-year, monthly. Annual is the default this skill covers.
4. **Owner** — CSM-driven, dedicated renewals manager, AM, or hybrid.
5. **Tooling** — CRM with renewal-date triggers? Automation?
6. **Current state** — last 12 months: gross retention, net retention, churn reasons.

## The 90/60/30/0 cadence

For an annual contract with renewal date D:

### Day -90 (start of renewal cycle)
- Owner: CSM.
- Action: review the account's value-realization scorecard. Run any value-realization-scorer or health-score-builder workflows.
- Decision: green/yellow/red track.
- Internal: brief renewal manager + AM if applicable.
- Customer-facing: optional check-in if any signal is yellow.

### Day -60 (value review)
- Owner: CSM (with AM if expansion possible).
- Action: structured value-realization meeting with the customer's primary contact.
- Agenda: review intended outcomes from deal-close, status against each, plans for next year.
- Output: agreed renewal scope (same, expand, contract).
- If red track: escalate. Bring in exec sponsor or product input.

### Day -45 (contract terms)
- Owner: AM or renewals manager.
- Action: send the formal renewal proposal.
- Include: proof of value (specific outcomes), pricing for next term, optional expansion, multi-year discount if applicable.
- Customer-facing: meeting to walk through the proposal, not email-only.

### Day -30 (executive engagement, enterprise tier only)
- Owner: exec sponsor on your side.
- Action: outreach to customer's exec sponsor or champion+1.
- Goal: confirm continued strategic alignment, surface any blockers.
- Skip for SMB.

### Day -14 (close mode)
- Owner: AM or renewals manager.
- Action: lock contract terms, route paperwork.
- Internal: weekly review with leadership on at-risk renewals in this window.

### Day 0 (renewal date)
- Owner: AM.
- Action: confirm execution. If unsigned, escalate immediately — every day past renewal date is a churn risk.
- Customer-facing: if signed, send a "thank you, here's what's next" note.
- Internal: log the result, capture the learning (won/lost reason).

### Day +30 (post-renewal)
- Owner: CSM.
- Action: post-renewal check-in. Reinforce the value, set the year's outcomes (feeds back into the value-realization model for the next cycle).

## Tier the cadence

- **SMB** ($/year): collapse 60/30 into one touchpoint; skip the exec sponsor step.
- **Mid-market**: full cadence as above.
- **Enterprise** (top 10% by ARR or strategic): add a Day -120 strategic review and Day -75 exec dinner / on-site.

## Tooling minimum

- CRM with a renewal-date field that triggers tasks at -90, -60, -45, -30, -14, 0.
- Dashboard of every account in renewal window with traffic light status.
- Templates for the value-review meeting agenda, renewal proposal email, exec outreach.

## Output format

Save the program design to `outputs/renewal-orchestration/<date>-program.md` with:
- Cadence per tier.
- Trigger setup (CRM fields and automations).
- Email and meeting agenda templates (4-6 stock items).
- Escalation paths (when CSM hands off, when exec sponsor steps in).
- Reporting: monthly view of upcoming renewals with predicted outcome.

For each active renewal, save `outputs/renewals/<account>-<renewal-date>.md` tracking the cadence executed.

## Common mistakes

- Starting the cadence at -30 instead of -90. Too late to influence anything.
- Using the same cadence for SMB and enterprise. Different economics, different process.
- Treating renewal as paperwork instead of a value conversation.
- No exec sponsor engagement on enterprise. Champion-only renewals collapse if the champion leaves.
- Skipping post-renewal capture. The next year's program improves by knowing why this one won or lost.

## Cross-references

For tactical single-deal renewal work, use `renewal-strategist`. For the value scoring that drives the renewal cadence, use (when added) `value-realization-scorer` and existing `health-score-builder`. For QBRs delivered during the cadence, use `qbr-builder`. For expansion conversations during renewal, use `expansion-opportunity-analyzer`.
