---
name: meeting-prep-brief
description: Prepare a one-page brief before any meeting. Adapts structure based on meeting type. Use before discovery calls, demos, negotiations, renewals, or standups.
triggers:
  - prep for meeting
  - meeting brief
  - before my call
  - meeting prep
allowed-tools: []
---

# Meeting Prep Brief

## Writes
- `outputs/meeting-prep-{date}.md`

## Step 1: Identify Meeting Type

Ask: What type of meeting is this?

- **Discovery** — First call with a prospect
- **Demo** — Showing the product to a potential buyer
- **Negotiation** — Pricing, terms, or contract discussion
- **Renewal** — Existing customer renewal or expansion
- **Standup** — Internal team sync
- **Other** — Describe the meeting and the brief will adapt

Ask one question at a time. If the user gives a vague answer, push back and ask for specifics before proceeding.

## Step 2: Gather Context

Check `context/` for existing ICP, product, and customer data. Then ask:

1. **Who is in the meeting?** Names, roles, company
2. **What do you want to get out of this meeting?** One specific outcome
3. **What do you already know about them?** Prior conversations, their situation, any signals

## Step 3: Build the Brief (by Type)

### Discovery Brief
- Company snapshot: size, industry, recent news, tech stack
- Hypothesis: why they might need your product (based on ICP and signals)
- 5 open-ended questions to validate the hypothesis
- Potential objections and how to handle them
- Clear next step to propose at the end

### Demo Brief
- Pain points to address (from discovery or research)
- 3 features to highlight, mapped to their specific pains
- Stories or proof points for each feature
- Questions they are likely to ask
- Proposed next step after the demo

### Negotiation Brief
- Your ideal outcome, acceptable outcome, and walk-away point
- Their likely priorities and pressure points
- BATNA (best alternative to negotiated agreement) for both sides
- Concessions you can offer and what to ask for in return
- Anchoring strategy for the opening

### Renewal Brief
- Account health: usage data, support tickets, NPS, expansion signals
- Value delivered since last renewal (specific metrics)
- Expansion opportunities: new seats, features, or tiers
- Risk factors: competitor mentions, declining usage, open issues
- Proposed terms and justification

### Standup Brief
- Status of each workstream (pulled from recent activity)
- Blockers to raise
- Decisions needed from the group
- Action items to assign

## Output Format

Save to `outputs/meeting-prep-{date}.md` where {date} is today's date:

### Meeting: [Company/Person] — [Type]
**Date:** [date and time]
**Attendees:** [names and roles]
**Objective:** [one sentence]

### Key Context
[3-5 bullet points of relevant background]

### Agenda / Talk Track
[Structured by meeting type, see above]

### Questions to Ask
[5-7 specific, open-ended questions]

### Potential Objections
| Objection | Response |
|-----------|----------|

### Desired Outcome
[What success looks like for this meeting]

## Common Mistakes
- Do not dump everything you know about the company. Filter for what is relevant to this specific meeting.
- Do not skip the "what do you want to get out of this meeting" question. A brief without a goal is just research.
- Do not prepare generic questions. Every question should be specific to this person, company, and situation.