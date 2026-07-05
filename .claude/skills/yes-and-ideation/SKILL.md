---
name: yes-and-ideation
description: Apply the "yes, and" improv technique to build on ideas constructively. Use when brainstorming solutions, expanding on a rough concept, or when a team is stuck in "no, but" thinking.
triggers:
  - yes and
  - brainstorm
  - build on this idea
  - expand this concept
  - ideation session
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Yes-And Ideation

"Yes, and" is an improv technique where you accept what someone offers and build on it, rather than shutting it down. Applied to product and strategy work, it transforms rough ideas into actionable concepts by removing the instinct to critique too early.

## Rules

1. **Accept the premise.** Take the idea as given, even if your first instinct is to object.
2. **Add to it.** Build on the idea with something new. "Yes, and we could also..."
3. **No "but" allowed.** Replace "but" with "and." This is a generation phase, not an evaluation phase.
4. **Quantity over quality.** Generate many variations. Filter later.
5. **Go weird.** The best ideas often come from unexpected combinations.

## Process

### Step 1 — State the Seed Idea
Write the initial idea clearly in one sentence. This is the seed everything builds on.

**Seed:** [the idea]

### Step 2 — Build Rounds (3-5 rounds)
Each round adds a new dimension or angle:

**Round 1 — Scale it.**
"Yes, and what if we did this at 10x scale? 100x? What if only 1 person used it?"

**Round 2 — Flip the audience.**
"Yes, and what if this was designed for [completely different user]? What would change?"

**Round 3 — Combine it.**
"Yes, and what if we merged this with [unrelated thing]? What would that hybrid look like?"

**Round 4 — Remove constraints.**
"Yes, and what if money/time/technology were not a constraint? What would the ideal version look like?"

**Round 5 — Make it weird.**
"Yes, and what's the most unexpected, counterintuitive version of this idea?"

### Step 3 — Harvest
From all the variations generated, pull out:

| Variation | What's Interesting About It | Feasibility | Worth Exploring? |
|-----------|---------------------------|-------------|-----------------|
| [idea] | [why it caught your attention] | [easy/medium/hard] | [yes/no/maybe] |

### Step 4 — Converge
Pick 2-3 variations worth developing further. For each, write:
1. **The concept** — one paragraph describing what it is
2. **Why it's interesting** — what makes it better than the original seed
3. **First step** — the smallest action to test whether it has legs

## Output

Write to `outputs/ideation-[topic].md`:

1. **Seed idea**
2. **All variations** from each round (raw, unfiltered)
3. **Harvest table** with feasibility notes
4. **Top 2-3 concepts** with next steps

## Do NOT
- Critique during the generation phase — save evaluation for Step 3
- Self-censor ideas that seem "too crazy" — those often contain the seed of something real
- Stop at the first good variation — push through at least 3 rounds
- Use this as a substitute for research — ideation generates hypotheses, not answers