---
name: idea-to-prd
description: Walk a raw product idea through staged discovery — clarifying questions, spec doc, user flows, PRD. Use when someone has a feature idea but does not yet have requirements a squad can pick up. Stages are gated by user keywords ("spec doc", "design flows", "create prd"). For PRD generation alone, see prd-writer. For early validation, see idea-validator.
triggers:
  - i have a product idea
  - turn this into a prd
  - help me scope this feature
  - product discovery
  - idea to prd
---

# Idea to PRD

Take a rough product idea and turn it into a handoff-ready PRD through four stages. Each stage is gated by a user keyword — don't skip ahead, even if the user is excited.

## Gather Context First

1. Read `context/` for product positioning and target audience
2. Read `notes/user-insights/` (if present) for known pain points and quotes
3. Check `plans/` for active product plans the new idea may relate to or conflict with
4. Identify the user's role (PM, marketer, founder, designer) — adjust depth accordingly

## The Four Stages

### Stage 1 — Clarifying questions (immediate)

When the user shares an idea, generate 8-10 numbered clarifying questions before doing anything else. Cover:

- Who is the user this serves?
- What problem does it solve, in their words?
- What's the desired outcome — what does success look like?
- What constraints exist (timeline, budget, tech, regulatory)?
- What have they tried, observed, or ruled out?
- How does this compare to alternatives or existing solutions?
- What does NOT belong in scope?

Wait for the user to answer. Don't auto-fill answers.

After answers come back, repeat unanswered questions or ask 2-3 follow-ups if needed. Don't move to Stage 2 until the picture is sharp.

End with: `Next: type "spec doc" to generate the spec.`

### Stage 2 — Spec doc (triggered by "spec doc")

Generate a product spec from the answers. Save to `outputs/discovery/<feature-slug>/01-spec.md`:

```
# [Feature name] — Spec

## Product summary
[2-3 sentences]

## Problem solved
[What pain this removes, in user-language]

## Target audience
[Specific role, stage, or segment]

## Key features and functionality
- [Feature 1] — [what it does]
- [Feature 2] — ...

## Success metrics
- Leading: [observable in days/weeks]
- Lagging: [observable in months]

## Out of scope (explicit no's)
- [What this is NOT trying to do]

## Open questions
- [Anything still unclear]
```

End with: `Next: type "design flows" to map the user flows.`

### Stage 3 — Design flows (triggered by "design flows")

Map detailed user flows and key screen specs. Save to `outputs/discovery/<feature-slug>/02-flows.md`:

```
# [Feature name] — Flows

## User flow: [primary path]
1. [Entry point — where the user starts]
2. [Step] — user does X, sees Y
3. ...
N. [Success state]

## Key screens

### Screen 1: [Name]
- **Purpose:** [why this screen exists]
- **Layout:** [main regions, hierarchy]
- **Elements:** [inputs, buttons, text, images]
- **User actions:** [what they can do here]
- **Outcomes per action:** [where each action leads]
- **Validation:** [rules, error states]
- **State changes:** [what flips when]

### Screen 2: ...

## Edge cases and error flows
- [Failure mode] → [what happens]

## Cross-flow concerns
- [Auth, permissions, empty states, loading states]
```

Focus on the *what*, not the *how*. No tech stack decisions yet.

End with: `Next: type "create prd" to generate the PRD.`

### Stage 4 — PRD (triggered by "create prd")

Synthesize stages 1-3 into a PRD a squad can pick up. Save to `outputs/discovery/<feature-slug>/03-prd.md`. Use the structure from the `prd-writer` skill — that's the canonical template. Add references back to the spec and flows files so reviewers can trace decisions.

End with a "What's next" block:

```
## What's next
- Engineering review: [point person]
- Design review: [point person]
- Estimated scope: [t-shirt size]
- Open dependencies: [list]
- First implementation step: [smallest concrete action]
```

## Stage Discipline

After each stage:

- Tell the user what just got saved (file path)
- Offer the next-stage trigger word
- Offer to revisit any earlier stage ("type 'redo questions'" / "redo spec" / "redo flows")
- Don't auto-advance — wait for the keyword

If the user says something ambiguous, ask which stage they want to be in. Stage discipline is the value.

## Output Format

A `outputs/discovery/<feature-slug>/` directory containing:

- `01-spec.md`
- `02-flows.md`
- `03-prd.md`
- `notes.md` (optional — running notes from the conversation)

The feature slug is generated from the feature name (kebab-case) on first save.

## Do NOT

- Skip stages because the user seems impatient — incomplete discovery produces broken PRDs
- Generate the spec without 8-10 clarifying questions answered first — it'll be a guess
- Make tech-stack or implementation decisions in the flows or PRD — that's engineering's job
- Reuse a feature slug that already exists in `outputs/discovery/` — it overwrites prior work
- Fill in answers the user didn't give — flag them as open questions instead
- Treat the PRD as the end — the "What's next" block is what makes it actually move