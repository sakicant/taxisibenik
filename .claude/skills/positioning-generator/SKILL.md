---
name: positioning-generator
description: Generate complete product positioning from scratch or audit existing positioning. Covers ICP definition, market segmentation, positioning statement, messaging hierarchy, and validation. Use when launching a product, entering a new market, or when current positioning feels stale.
triggers:
  - build positioning
  - positioning framework
  - audit positioning
  - positioning review
  - ICP definition
  - value proposition
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Positioning Generator

## Writes
- `outputs/positioning-[product-slug].md`

## Context Scan

Check `context/` and `reference/` for existing positioning docs, competitor research, ICP definitions, win/loss data, and brand guidelines. Ask for anything missing.

## Step 1 — Market Segmentation

Segment across four dimensions:

| Dimension | Segments |
|-----------|----------|
| **Role** | Who buys, who uses, who approves? |
| **Tech stack / tools** | What do they already use? |
| **Use case** | What problem triggers the search? |
| **Buying behavior** | Self-serve, sales-assisted, enterprise procurement? |

For each segment, estimate: market size, competition intensity, and your right to win.

## Step 2 — ICP (Ideal Customer Profile)

Define: **Demographics** (company size, industry, stage), **Technographics** (current tools, maturity), **Behaviors** (where they research, how they evaluate, buying timeline), **Pain points** (top 3 ranked by urgency, what they do today, why it fails, what it costs).

Write the ICP as a one-paragraph "day in the life" that captures the frustration. This becomes the emotional anchor for all messaging.

## Step 3 — Positioning Statement

Anchor on April Dunford's *Obviously Awesome* framework. Lock these five components before writing the statement:

1. **Competitive alternatives** — what the buyer would do if you did not exist (including status quo)
2. **Unique attributes** — capabilities only you (or very few) have
3. **Value** — the outcome those attributes deliver in measurable terms
4. **Target segment** — the buyer who cares most about that value
5. **Market category** — the comparison set the buyer puts you in

Then write the statement:

**For** [target buyer] **who** [key pain point], **[product]** is a **[category]** that **[primary differentiator]**. **Unlike** [primary alternative], **we** [key difference].

Classify: **Category leader** (you define it), **Category creator** (it doesn't exist yet), **Challenger** (clear "why switch"), or **Niche specialist** (own a segment).

## Step 4 — Problem Framing

Choose the variant that fits:
- **Category-anchored:** "[Category] is broken because [issue]. We fix it by [approach]."
- **Use-case-anchored:** "[Persona] spends [time/money] on [task] because [root cause]. [Product] eliminates that."
- **Alternative-anchored:** "Most [personas] use [current solution]. The problem is [limitation]. [Product] does it without [limitation]."

## Step 5 — Messaging Hierarchy (Pathos/Logos/Ethos)

Build three pillars:

**Pillar 1 — Emotional (Pathos):** What does the buyer feel? Lead with the feeling, connect to the product. Include mechanism, consequence, and proof.
**Pillar 2 — Logical (Logos):** ROI, time saved, risk reduced. Same structure.
**Pillar 3 — Credibility (Ethos):** Team expertise, customer logos, certifications. Same structure.

For each pillar write: one-line version, elevator version (2-3 sentences), and full version (paragraph with proof).

## Step 6 — Validation Tests

Run four tests. Rewrite until all pass:

**Duck test:** Read it to someone unfamiliar. Can they explain what you do back?
**Category test:** Can the buyer figure out what budget line this comes from?
**Swap test:** Replace your name with a competitor's. Does it still work? If yes, not differentiated.
**Consequence test:** Does it imply a measurable consequence of not using the product?

## Step 7 — Output

1. Market segmentation table
2. ICP profile
3. Positioning statement + type
4. Problem framing (chosen variant)
5. Three messaging pillars (one-line, elevator, full)
6. Validation test results
7. Differentiation summary (3 things only you can say)
8. Tagline candidates (3-5)
9. Terminology dictionary

## Do NOT
- Write positioning that fails the swap test
- Confuse features with positioning
- Skip the ICP
- Use jargon the buyer wouldn't use
- Suggest positioning you can't prove within 6 months

## Succeeds when
- The statement is specific enough that competitors cannot truthfully claim it
- Sales reps can deliver "what we do" and "why us" in under 30 seconds
- Prospects respond with "that's exactly what we need" rather than "tell me more about what you do"
- All five Dunford components are filled in with evidence, not aspirations
- Different teams describe the product the same way

## Fails when
- Positioning is so broad anyone in the category could claim it
- Different teams use different language to explain the product
- Prospects ask "how is that different from [competitor]?" after hearing the pitch
- The category choice cannot be defended with proof
- Positioning is aspirational rather than evidence-based