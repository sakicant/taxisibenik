---
name: quarterly-plan
description: Set 3-5 strategic priorities for the quarter that align with longer-term goals. Use at the start of each quarter, or mid-quarter when starting fresh. For weekly planning, see weekly-plan. For roadmap-level planning, see roadmap-planner.
triggers:
  - quarterly plan
  - quarter goals
  - plan the quarter
  - q1 planning
  - q2 planning
  - q3 planning
  - q4 planning
---

# Quarterly Plan

Set the 3-5 priorities that will define the quarter. Anything more is a wish list. Anything less probably misses something.

## Gather Context First

1. Read `context/roadmap.md` (or equivalent) for longer-term direction
2. Read the prior `outputs/cadence/quarterly-review-*.md` if one exists
3. Scan the last 10-13 `outputs/cadence/weekly-review-*.md` for patterns and unfinished work
4. Check `context/project-vision.md` (or equivalent) for the north star
5. Identify any external constraints (funding runway, team changes, market timing)

## The Planning Sequence

### Step 1 — Connect to the longer arc

Before naming priorities, articulate:

- **Where we are** — current state in one paragraph
- **Where we're going** — desired state by year-end
- **What's missing** — the gap between the two

Quarterly priorities exist to close the gap. If a candidate priority doesn't help close it, it's not a quarterly priority.

### Step 2 — Generate candidates

List every plausible priority — 10-20 candidates. Don't filter yet.

Sources:
- Carry-forward from last quarter
- Patterns from the weekly reviews
- Strategic moves the roadmap implies
- Customer signals (transcripts, support, churn data)
- Team capacity and skill changes
- Market or competitor moves

### Step 3 — Apply the priority filter

Score each candidate against four lenses:

| Lens | Question | Weight |
|------|----------|--------|
| Strategic value | Does this move us materially toward year-end? | 3x |
| Feasibility | Can we actually deliver this in 13 weeks with current capacity? | 2x |
| Reversibility | If wrong, can we course-correct? | 1x |
| Cost of inaction | What breaks if we don't do this? | 2x |

Cut the candidate list to top 8-10 by score. Then pick 3-5 from there.

### Step 4 — Write priorities as outcomes

A priority is an outcome with a measurable definition of done.

| Weak (vision) | Strong (outcome) |
|---------------|-----------------|
| "Improve activation" | "Lift week-1 activation from 31% to 45%" |
| "Better content" | "Publish 12 long-form pieces with 2k+ avg views" |
| "Hire faster" | "Close 3 senior roles by [end-of-quarter date]" |

If a priority can't be measured, rewrite it. Unmeasurable priorities lose to measurable ones every time.

### Step 5 — Identify the leading indicators

For each priority, name 2-3 leading indicators visible weekly. Without these, you'll only know the priority failed at the end of the quarter.

### Step 6 — Name the explicit no's

The quarterly plan should include 3-5 things you're explicitly not doing this quarter. This is the most-skipped section and the highest-signal one.

## Output Format

Save to `outputs/cadence/quarterly-plan-YYYY-Q#.md` and update or replace `outputs/cadence/quarterly-current.md` to point at it:

```
# Q[N] YYYY Plan

## Where we are
[1 paragraph — current state]

## Where we're going (year-end)
[1 paragraph — desired state]

## The gap
[What's missing — the thing this quarter exists to close]

## This quarter's priorities (3-5)

### 1. [Outcome with measurable target]
- Strategic rationale:
- Done when (specific):
- Leading indicators (weekly visible):
- Owner / contributors:
- Major risks:

### 2. ...

## Explicit no's this quarter
- [Thing not being pursued, with reason]

## Capacity assumptions
- People-weeks available:
- Major time costs (hiring, travel, releases):
- Slack reserved for unknowns:
```

## Do NOT

- Set more than 5 priorities — the sixth one is the one that doesn't ship
- Confuse activities with outcomes — "run more experiments" is an activity, "ship 8 winning experiments" is an outcome
- Skip the explicit no's — they're how the plan stays honest
- Plan a quarter without checking last quarter's review — pattern blindness compounds
- Pick priorities the team can't actually deliver — heroic plans demoralize when they slip