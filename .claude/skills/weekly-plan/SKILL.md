---
name: weekly-plan
description: Plan the upcoming week by reviewing last week's progress, active priorities, and calendar commitments. Use at the start of each week to set 3-5 focused priorities and schedule the work. For daily planning, see morning-briefing. For quarterly planning, see quarterly-plan.
triggers:
  - weekly plan
  - plan my week
  - week ahead
  - what should i work on this week
---

# Weekly Plan

Set the focus for the week ahead. Pull from quarterly goals, last week's carry-forward, and the calendar — produce 3-5 priorities with a realistic schedule.

## Gather Context First

1. Read `outputs/cadence/quarterly-current.md` (or the latest `outputs/cadence/quarterly-*.md`) for active quarterly priorities
2. Read the most recent `outputs/cadence/weekly-review-*.md` for carry-forward items
3. Read `context/roadmap.md` or equivalent for project priorities
4. Check the calendar for the week (commitments, meetings, blocked time)
5. Check `plans/` for active implementation plans

## The Planning Sequence

Run these in order. Skipping a step leads to a plan that drifts mid-week.

### Step 1 — Pull from Quarterly Goals

For each quarterly priority, ask: "What would have to happen this week for this to stay on track?" If a quarterly priority has no movement scheduled this week, flag it.

### Step 2 — Carry Forward

From the latest weekly review:
- What got pushed? Why?
- What's still relevant? What can be dropped?
- What needs a different approach?

Carry-forward items don't get a free pass. Each one needs justification or it's cut.

### Step 3 — Calendar Reality Check

| Calendar reality | Implication |
|------------------|-------------|
| 4+ hours of meetings on a day | No deep work that day |
| Travel or PTO | Subtract from capacity, don't pretend |
| External deadline | Block time backwards from the deadline |
| Recurring rituals | Fixed cost, plan around them |

If the calendar shows under 10 hours of focused time across the week, flag it. The plan must fit reality.

### Step 4 — Pick 3-5 Priorities

A priority is a specific outcome, not a topic.

| Weak (topic) | Strong (outcome) |
|--------------|-----------------|
| "Work on launch" | "Ship the launch announcement to the email list" |
| "Catch up on customers" | "Complete 3 onboarding calls and capture transcripts" |
| "Improve metrics" | "Identify the top friction step in signup flow" |

If you can't say "I'll know it's done when [X]," it's not a priority — it's a topic.

### Step 5 — Schedule the Work

Block specific calendar time for each priority. Unscheduled priorities don't ship.

- Pair each priority with at least one specific calendar block
- Leave 20% slack — unplanned work always arrives
- Front-load the highest-leverage priority — energy fades by Friday

## Output Format

Save to `outputs/cadence/weekly-plan-YYYY-WW.md`:

```
# Week of [Monday date]

## Quarterly priorities being moved this week
- [Quarter goal] → [this week's contribution]

## Carry-forward from last week
- [Item] — [why it's still in scope, or dropped with reason]

## This week's priorities (3-5)

### 1. [Outcome statement]
- Why it matters this week:
- Done when:
- Time blocked:
- First step:

### 2. ...

## Calendar reality
- Total focused hours available: [X]
- Major meetings/travel:
- Hard deadlines:

## Not doing this week
- [Item explicitly deferred — keeps scope honest]
```

## Do NOT

- Set more than 5 priorities — every priority above 5 is a wish, not a plan
- Confuse topics with priorities — "marketing" is a topic, "publish 2 case studies" is a priority
- Plan the week without checking the calendar — capacity comes first
- Roll over carry-forward items without justification — that's how plans rot
- Skip the "not doing" list — it's the most honest part of the plan