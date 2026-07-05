---
name: messaging-hierarchy
description: Build a structured messaging stack with five layers — from point of view down to feature-level proof. Each layer includes quality tests and persona adaptation. Use before campaigns, launches, or when messaging feels scattered.
triggers:
  - build messaging
  - messaging framework
  - messaging hierarchy
  - messaging stack
  - value prop framework
  - 60 second pitch
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Messaging Hierarchy

## Writes
- `outputs/messaging-hierarchy.md`

## Context Scan

Check `context/` and `reference/` for:
- Positioning documents
- ICP definitions and buyer personas
- Competitor research
- Brand voice guidelines
- Existing taglines, value props, or pitch decks

Ask for anything missing. You need at minimum: what the product does, who it is for, and the top 3 buyer pain points.

## The Five Layers

Build each layer in order. Each layer must pass its quality test before moving to the next.

### Layer 1 — Point of View (POV)

Your stance on the market. Not what you sell, but what you believe.

Write a 1-2 sentence POV that:
- States a belief about how the world should work
- Implies a problem with how things work today
- Does not mention your product

**Quality test:** Could a prospect read this and think "I agree with that" before knowing what you sell? If not, it is too product-centric. Rewrite.

### Layer 2 — Value Proposition

The bridge between your POV and your product. One sentence.

Format: [Product] helps [audience] [achieve outcome] by [mechanism], so they can [ultimate benefit].

**Quality test:** Does it pass the "so what?" test? Read it aloud. If a busy buyer would respond "so what?", the outcome is too vague. Make it specific and measurable.

### Layer 3 — Pillars (3-4 max)

The main reasons to believe the value proposition. Each pillar is a category of value.

For each pillar:
- **Claim** — one sentence stating the benefit
- **Evidence** — proof points, metrics, or customer quotes
- **Objection** — the most likely pushback, and how you address it

**Quality test:** Are the pillars distinct? If you removed one, would the story collapse? If not, merge it with another. Three strong pillars beat five weak ones.

### Layer 4 — Proof Points

Concrete evidence under each pillar. These are the facts that make the claims believable.

| Pillar | Proof Point | Type | Strength |
|--------|------------|------|----------|
| [Pillar 1] | [Metric, quote, or case study] | Quantitative/Qualitative | Strong/Moderate/Weak |

**Quality test:** Is every proof point specific? "Customers love us" is not a proof point. "4.8 star average across 200 reviews" is. Flag anything that lacks specifics.

### Layer 5 — Feature-Level Messaging

Map features to the pillar and pain point they support:

| Feature | Supports Pillar | Buyer Pain Addressed | One-Line Description |
|---------|----------------|---------------------|---------------------|
| [Feature] | [Pillar #] | [Specific pain] | [Benefit-first description] |

**Quality test:** Is every feature connected to a pillar? Orphan features (cool but unconnected to the value story) weaken the narrative. Cut or reframe them.

## Persona Adaptation

After building the hierarchy, adapt the top three layers for each key persona:

| Layer | [Persona 1] | [Persona 2] | [Persona 3] |
|-------|------------|------------|------------|
| POV emphasis | [What resonates most] | | |
| Value prop angle | [Their specific outcome] | | |
| Lead pillar | [Which pillar to lead with] | | |

Different personas care about different parts of the same story. The facts stay the same. The emphasis changes.

## The 60-Second Pitch

Combine the layers into a spoken pitch:

1. **POV** (10 sec) — state the belief
2. **Problem** (10 sec) — the pain that follows from the current reality
3. **Value prop** (10 sec) — what you do about it
4. **Lead pillar + proof** (20 sec) — one reason to believe, with evidence
5. **Call to action** (10 sec) — what to do next

Write it out word for word. Read it aloud. If it takes more than 70 seconds, cut.

## Do NOT
- Start with features and work up. The hierarchy is top-down for a reason. POV first.
- Use internal jargon in buyer-facing layers. If your team says it but your buyers don't, translate.
- Build more than 4 pillars. If you cannot narrow to 4, your positioning is trying to be everything.
- Skip the quality tests. They exist because each layer has a specific failure mode. Test every layer before building the next.

## Succeeds when
- Sales, marketing, CS, and execs all describe the product in the same words
- Every proof point is specific (a number, a quote, or a named customer)
- The 60-second pitch can be delivered without notes
- Features map cleanly to pillars without orphans
- Personas adapt the emphasis without contradicting the core story

## Fails when
- Pillars overlap so much that removing one would not collapse the story
- Proof points use vague language ("customers love us") instead of specifics
- Feature messaging is not anchored to a pillar
- The POV is product-centric instead of a market belief
- Different personas get different facts instead of different emphasis