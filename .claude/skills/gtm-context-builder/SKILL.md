---
name: gtm-context-builder
description: Create a structured GTM context document covering ICP, value props, competitive positioning, and outreach foundations.
triggers:
  - build gtm context
  - gtm document
  - outreach foundations
---

# GTM Context Builder

You are a go-to-market strategist. Build a living context document that serves as the single source of truth for all outreach, content, positioning, and sales enablement work.

## Gather Existing Context First

Before starting from scratch, check:
- `context/` for any existing product, audience, or market files
- `reference/` for brand voice, competitive research, or positioning docs
- `outputs/` for past research, pain hypotheses, or competitive analysis

Use what exists. Only build sections from scratch when no prior work is available.

## Document Structure

Create or update `context/gtm.md` with the following sections. Each section includes guidance on what "good" looks like and common mistakes.

### 1. Company Overview
- **What we do** — One paragraph, plain language, no jargon. The test: could a non-customer understand this in 10 seconds?
- **Key differentiators** — 3-5 bullets. Each must answer "why us instead of the alternative?" not just "what we do"
- **Stage and scale** — Startup, growth, or enterprise. Revenue range if known. Team size. This affects every GTM decision.
- **Business model** — How do we make money? (SaaS subscription, usage-based, services, marketplace take rate)

Common mistake: Writing differentiators that are actually table stakes ("great customer support", "easy to use"). Every competitor claims these. Differentiate on specifics.

### 2. Ideal Customer Profile (ICP)

#### Primary ICP
- **Role:** Title, level, reporting structure
- **Company:** Size (headcount and revenue range), industry, growth stage
- **Tech stack:** Tools they already use that relate to your product
- **Budget authority:** Do they own the budget or need approval?
- **Buying trigger:** What event makes them actively look for a solution?

#### Secondary ICP
- Who else buys, and why they are secondary (smaller deal size, longer sales cycle, higher churn)

#### Anti-ICP (Disqualifiers)
Who is NOT a fit. Document specifically to save time on outreach and prevent bad-fit customers:
- Too small (under X employees or revenue)
- Too large (procurement process makes deal economics impossible)
- Wrong industry (no relevant use case)
- Wrong tech stack (integration not supported)
- Wrong buying stage (just researching, no budget cycle coming)

### 3. Value Propositions

For each ICP, document using the Value Proposition Canvas structure:

| ICP | Pain We Solve | Outcome We Deliver | Proof Point | Key Message |
|-----|--------------|-------------------|-------------|-------------|
| Primary | Specific, measurable problem | Specific, measurable result | Customer quote, metric, case study | One sentence for outreach |
| Secondary | ... | ... | ... | ... |

**Test each value prop:** If you removed your company name and replaced it with a competitor, would the statement still be true? If yes, it is not differentiated enough.

### 4. Competitive Landscape

#### Direct Competitors
| Competitor | Their Pitch | Our Advantage | Their Advantage | When We Win | When We Lose |
|-----------|------------|---------------|-----------------|------------|-------------|

#### Indirect Competitors
Include alternatives that are not direct competitors but compete for the same budget or attention:
- DIY approaches (spreadsheets, internal tools)
- Adjacent products that expand into your space
- Agencies or consultants that solve the problem differently
- The status quo ("do nothing" is always a competitor)

#### Positioning Map
Place yourself and competitors on two axes that matter most to your ICP. Choose axes where you win.

### 5. Win/Loss Patterns

#### Common Win Reasons (ranked by frequency)
1. [Reason] — [Supporting quote or data point]
2. [Reason] — [Supporting quote or data point]

#### Common Loss Reasons (ranked by frequency)
1. [Reason] — [What we say now] — [What we should say]
2. [Reason] — [What we say now] — [What we should say]

#### Top 5 Objections with Tested Rebuttals

| Objection | Response | Evidence |
|-----------|----------|----------|
| "Too expensive" | [Reframe around value/ROI] | [Specific customer result] |
| "We already have [competitor]" | [Specific differentiation] | [Migration success story] |
| "Not the right time" | [Trigger-based follow-up plan] | [Cost of waiting] |

### 6. Outreach Foundations
- **Tone and voice** — How we sound in emails, calls, and social. Link to `reference/brand-voice.md` if it exists.
- **Do-not-contact list** — Companies or domains to skip, and why
- **Channel ranking** — Email, LinkedIn, events, referrals, content — ranked by historical conversion rate
- **Timing patterns** — Best days/times for outreach, buying cycles (Q4 budget planning, fiscal year starts), seasonal patterns
- **Sales collateral inventory** — What exists (one-pagers, case studies, demo videos) and what is missing

### 7. Metrics and Goals
- **Pipeline targets** — Monthly/quarterly pipeline generation goals
- **Conversion benchmarks** — Expected rates at each funnel stage
- **Key metrics to track** — MQLs, SQLs, pipeline value, win rate, cycle time, average deal size

## Process for Building

### New Document
1. Walk through each section with the user
2. For sections they can fill in now, capture the information with specifics
3. For empty sections, suggest exactly what to research or who to ask
4. Flag inconsistencies (e.g., ICP says "enterprise" but win patterns are all SMB)
5. Save to `context/gtm.md`

### Existing Document Update
When triggered on an existing GTM context:
1. Show the last revision date and summarize what is in each section
2. Ask about recent wins, losses, market shifts, or product changes
3. Identify sections that are stale (no updates in 30+ days)
4. Update and increment the revision date
5. Flag any sections where new information contradicts existing assumptions

## Maintenance Schedule

This document should be updated:
- **Monthly** — Refresh win/loss patterns, add new proof points
- **Quarterly** — Review competitive landscape, update ICP if the market shifted
- **After major events** — New product launch, pricing change, competitor announcement, major win or loss

## Do NOT
- Fill sections with generic placeholder text — leave blank and note what research is needed
- Skip the disqualifiers section — knowing who is NOT a fit prevents wasted outreach
- Treat this as a one-time exercise — a GTM document is only valuable if it stays current
- Copy competitor descriptions from their marketing — describe them from the buyer's perspective
- Write value propositions that any competitor could claim — be specific or leave blank