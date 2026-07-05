---
name: weekly-review
description: Review the week that ended — wins, misses, learnings, carry-forward items. Use at the end of each week to capture progress, route unfinished work into the next week, and surface patterns. For end-of-session capture, see session-debrief. For weekly planning, see weekly-plan.
triggers:
  - weekly review
  - review my week
  - week recap
  - what got done this week
---

# Weekly Review

Look back at the week and turn it into signal for next week. Honest assessment beats optimistic narration.

## Gather Context First

1. Read this week's `outputs/cadence/weekly-plan-YYYY-WW.md`
2. Pull commits from the week (`git log --since='1 week ago' --oneline`)
3. Scan `outputs/` for files created or modified this week
4. Check `notes/` for meeting transcripts or insights captured
5. Read `outputs/cadence/quarterly-current.md` for the quarterly goals being tracked

## The Review Sequence

### Step 1 — Did the priorities ship?

For each priority in the weekly plan, mark one of:

- **Done** — outcome shipped as defined
- **Moved** — partial progress, identifiable next step
- **Dropped** — no longer relevant, with reason
- **Failed** — attempted, didn't land, with reason

"Failed" is allowed and useful. Hide nothing.

### Step 2 — What else got done?

Work happens that wasn't in the plan. Capture it without judgment:

- Reactive work (incidents, urgent asks)
- Opportunistic wins (a chance came up, took it)
- Maintenance (responses, reviews, admin)

If reactive work consumed more than 30% of the week, that's a signal — either capacity is wrong or the plan is wrong.

### Step 3 — Wins worth remembering

A win isn't just "shipped." A win is something the future-you will want to remember:

- A user said something memorable (capture the verbatim quote)
- A pattern revealed itself
- A constraint that was assumed turned out not to exist
- A tactic that worked surprisingly well

### Step 4 — Misses and lessons

For each miss:

| Miss | Why | What changes next week |
|------|-----|------------------------|
| [Priority that didn't ship] | [Honest cause: capacity, dependency, wrong approach, lost focus] | [Specific change — not a generic resolution] |

"I'll try harder" is not a lesson. "I'll block 2 mornings of deep work because afternoons disappear to meetings" is a lesson.

### Step 5 — Carry-forward decisions

For each unfinished item, choose:

- **Carry forward** — still the right thing to do
- **Defer** — important but not for next week
- **Drop** — not worth doing, even though it's started
- **Reframe** — the original framing was wrong, restart with new approach

Items that have carried for 2+ weeks need a hard "drop or commit" decision. Drift is the enemy of focus.

### Step 6 — Patterns

Once a quarter, scan the last 13 weekly reviews for patterns:

- Priorities that keep getting pushed
- Time sinks that keep recurring
- Misses with the same root cause
- Tactics that consistently work

This is the compounding step. Without it, the reviews are just journals.

## Output Format

Save to `outputs/cadence/weekly-review-YYYY-WW.md`:

```
# Week of [Monday date] — Review

## Priorities scorecard
| Priority | Status | Notes |
|----------|--------|-------|
| 1. [...] | Done / Moved / Dropped / Failed | |

## What else got done
- [Items not in the plan]

## Wins worth remembering
- [Quotes, surprises, patterns, tactics that worked]

## Misses and lessons
| Miss | Why | What changes next week |

## Carry-forward decisions
| Item | Decision | Reason |

## Capacity check
- Reactive work share: [X%]
- Plan vs. reality gap: [if significant, note it]
```

## Do NOT

- Soften the misses — sanitized reviews don't generate learnings
- Skip the carry-forward decisions — unfinished items pile up otherwise
- Treat reactive work as failure — it's data about capacity, not character
- Forget the verbatim quotes from users — those are the highest-leverage outputs of any week
- Run the review more than 30 minutes — the point is signal, not catharsis