---
name: competitive-battlecard-builder
description: Build competitive battlecards with feature matrices, positioning maps, and win/loss framing. Use when preparing sales battlecards, planning competitive positioning, or arming reps with differentiation talking points. For general competitor research, use competitor-researcher instead.
triggers:
  - competitive battlecard
  - build battlecards
  - competitive positioning
  - win loss analysis
  - competitive intelligence
  - how do we compare
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Competitive Battlecard Builder

Build structured competitive battlecards for sales teams and strategic planning. Goes beyond general research into actionable positioning, win/loss framing, and differentiation talking points.

## Context Scan

Check for existing competitive analysis, ICP definitions, or product positioning in `context/`, `reference/`, and `outputs/`.

## Writes
- `outputs/battlecard-[competitor].md`

## Step 1: Define the Competitive Set

Ask the user:
1. **Direct competitors** — same product category, same buyer
2. **Indirect competitors** — different approach, same problem
3. **Alternatives** — what buyers do instead (including "do nothing")

## Step 2: Profile Each Competitor

For each competitor, research and document:

**Basics:** Name, URL, founding year, funding, team size, stage
**Positioning:** How do they describe themselves in one sentence?
**Target buyer:** Who are they selling to? (role, company size, industry)
**Pricing:** Model (freemium, subscription, usage-based), price points, tiers
**Key features:** Top 5-10 features they promote
**Distribution:** How do they acquire customers? (PLG, sales-led, content, paid, community)
**Content strategy:** Blog frequency, topics, social presence
**Recent moves:** Last 6 months of notable changes (launches, pivots, funding, hires)

## Step 3: Feature Matrix

Build a comparison table:

| Feature | Us | Competitor A | Competitor B | Competitor C |
|---|---|---|---|---|
| [Feature 1] | Status | Status | Status | Status |

Use: Full, Partial, None, or specific capability notes.

## Step 4: Positioning Map

Place competitors on two axes that matter to buyers. Choose axes based on:
- What buyers actually evaluate (not what you wish they evaluated)
- Where your product has a defensible position

Common axis pairs:
- Ease of use vs. power/flexibility
- Price vs. feature depth
- Self-serve vs. sales-assisted
- Point solution vs. platform

## Step 5: Strategic Analysis

For each competitor:
- **Strengths** — where they genuinely beat you
- **Vulnerabilities** — where they are weak or exposed
- **Strategic direction** — where they appear to be heading based on recent moves
- **Threat level** — high / medium / low, with reasoning

## Step 6: Recommendations

1. **Where to compete** — features or positioning where you can win
2. **Where to avoid** — battles you will lose
3. **Differentiation opportunities** — gaps no one is filling
4. **Messaging implications** — how to position against each competitor

## Output

Complete report with feature matrix, positioning map (ASCII), and per-competitor profiles with strategic analysis.

## Succeeds when
- The positioning map axes reflect what buyers actually evaluate
- "Where to compete" and "where to avoid" are both explicit
- Each competitor profile names a clear strategic direction, not just a snapshot
- Differentiation opportunities are tied to gaps no competitor is filling
- Threat levels are defended with reasoning, not assigned by gut

## Fails when
- The map uses axes that flatter your product instead of axes buyers use
- Strategic analysis stops at feature comparison
- Every competitor is rated the same threat level
- Recommendations apply to "the competition" generally instead of named competitors