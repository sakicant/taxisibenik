---
name: icp-workshop
description: Define or refine your ideal customer profile through a structured interview. Use when starting outreach, repositioning, or when your ICP feels stale.
triggers:
  - define ICP
  - ideal customer profile
  - who should we target
  - customer persona
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# ICP Workshop

## Writes
- `outputs/icp.md`

## Mode Selection

Check if `docs/icp.md` exists.

- **If it exists:** Enter Refinement mode. Read the file, summarize the current ICP, then probe for what has changed.
- **If it does not exist:** Enter Discovery mode. Start the interview from scratch.

## Discovery Mode

Ask one question at a time. If the user gives a vague answer, push back and ask for specifics before proceeding.

Walk through these topics in order:

1. **Industry and vertical** — What industry are your best customers in? Are there sub-verticals that convert better?
2. **Company size** — Headcount range and revenue range. Where is the sweet spot?
3. **Job titles and roles** — Who initiates the purchase? Who approves it? Who uses the product daily?
4. **Pain points and the job they hire you for** — What specific, measurable problems do they face? Frame in Jobs-to-be-Done terms: what progress are they trying to make? Reject generic answers like "they want to save time." Push for: save time on what? How much time? What does that cost them?
5. **Buying triggers (switching events)** — What event makes them start looking for a solution right now? (New hire, lost deal, regulation, tool sunset, budget cycle). This is the JTBD "switching moment" — capture the trigger, not just the search.
6. **Current solutions** — How do they solve this today? Spreadsheets, competitor, agency, manual process, or ignoring it?
7. **Disqualifiers** — Who is NOT a fit? Too small, too large, wrong industry, wrong tech stack, wrong buying stage?

## Refinement Mode

Read `docs/icp.md` and summarize each section. Then ask:

1. Have you closed any deals recently that surprised you (outside the current ICP)?
2. Have you lost deals you expected to win? What was different about those prospects?
3. Has your product changed in ways that open new segments?
4. Are any current ICP segments underperforming?

Update the ICP based on answers. Mark what changed and why.

## Output Format

Save to `outputs/icp.md`:

### Primary ICP
- Industry, company size, roles, budget authority

### Secondary ICP
- Who else buys, and why they are secondary

### Scoring Rubric
| Signal | Strong Fit (+2) | Moderate Fit (+1) | Weak Fit (0) | Disqualifier (-5) |
|--------|----------------|-------------------|--------------|-------------------|
| Company size | [range] | [range] | [range] | [range] |
| Role | [titles] | [titles] | [titles] | [titles] |
| Pain evidence | [signal] | [signal] | [signal] | [signal] |

### Buying Signals
Ranked list of triggers that indicate a prospect is ready to buy now.

### Disqualifiers
Hard stops. If any of these are true, do not pursue.

## Common Mistakes
- Do not accept "everyone" as a target. Every business has a best-fit customer. Push until you find specifics.
- Do not skip disqualifiers. Knowing who to avoid saves more time than knowing who to pursue.
- Do not assume pain points without evidence. "They probably struggle with X" is a hypothesis, not an ICP.

## Succeeds when
- The ICP is specific enough to disqualify real prospects on the spot
- Pain points are framed as jobs to be done, with measurable cost of inaction
- Switching triggers are named events, not generalized motivations
- The scoring rubric drives actual sales and marketing prioritization
- Disqualifiers are written down, not assumed

## Fails when
- The ICP is firmographic only (industry plus size) with no behavioral signal
- Pain points are generic ("they want efficiency") without measurable cost
- The doc lists who you want as customers rather than who you actually win
- No one uses the rubric to make routing or prioritization decisions