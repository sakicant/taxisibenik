---
name: services-proposal-writer
description: Generate services and consulting proposals with discovery framework, tiered pricing, and ROI projections. Use after discovery calls for consulting, agency, or professional services engagements. For general product/partnership proposals, use proposal-writer instead.
triggers:
  - services proposal
  - consulting proposal
  - agency proposal
  - engagement proposal
  - write a proposal for services
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Services Proposal Writer

Write services and consulting proposals that win deals. A good proposal proves you understand the client's problem better than they do, and that your solution is the obvious choice.

## Writes
- `outputs/proposal-[client].md`

## Step 1: Gather Inputs

If discovery is complete, collect:
- Client name, company, industry
- Pain points and goals (in their words)
- Current situation and what they have tried
- Budget range and timeline
- Decision-makers and their priorities
- Relevant case studies or proof points

If discovery has not happened, provide the user with these 10 essential questions:

1. Walk me through your business model.
2. Who is your ideal customer?
3. What marketing/sales/ops are you doing today?
4. What is working and what is not?
5. What specific results are you trying to achieve?
6. What is the lifetime value of a customer?
7. What have you tried before? What went well or poorly?
8. What does success look like in 6 months?
9. Who else is involved in this decision?
10. What would make you say no?

## Step 2: Build the Proposal

### Cover Page
Company name, client name, date, "Valid until [date + 30 days]", CONFIDENTIAL

### Executive Summary (1 page max)
- Acknowledge their situation and goals
- State the core problem
- Preview the recommended approach
- Hint at expected outcomes
- Do not mention price yet

### Situation Analysis
- Mirror back what you learned in discovery (proves you listened)
- Reference specific numbers or challenges they shared
- If you ran an audit, include key findings

### Proposed Solution
- What you will do, organized by phase or workstream
- Timeline for each phase
- What is included and what is not (prevent scope creep)
- Expected deliverables with dates

### Pricing
Present 3 tiers when possible (anchoring effect):
- **Starter** — core scope, lowest price, solves the primary problem
- **Growth** — recommended, adds significant value
- **Premium** — comprehensive, highest price, full service

For each tier: what is included, price, payment terms.

### ROI Projection
Connect investment to expected return:
- If they spend $X, and the result is Y% improvement, that means $Z in value
- Use conservative estimates. Underpromise.

### Case Studies (1-2)
Brief, relevant proof: similar client, similar problem, specific results.

### Next Steps
Exactly what happens after they say yes:
1. Sign proposal
2. Kickoff call scheduled within [N] days
3. [First deliverable] by [date]

## Writing Rules

- Use "we" and "you" language throughout
- Write for the decision-maker, not the evaluator
- Keep under 8 pages
- Bold the numbers that matter (ROI, timeline, price)