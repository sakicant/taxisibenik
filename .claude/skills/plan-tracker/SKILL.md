---
name: plan-tracker
description: Maintain a structured plan.md that tracks tasks, status, dependencies, and progress. Prevents multi-step work from losing direction.
triggers:
  - track this plan
  - update the plan
  - what's the status
  - create a plan
  - what's left to do
---

# Plan Tracker

## Creating a Plan

Create `plans/[plan-name].md`:

```markdown
# [Plan Name]
**Goal:** [One sentence — what does "done" look like?]
**Created:** [Date]
**Status:** In Progress

## Tasks
- [ ] Task 1 — [Description]
- [ ] Task 2 — [Description] (depends on: Task 1)

## Progress Log
### [Date]
- Completed: [what finished]
- Decisions: [choices made and why]
- Blocked: [what can't proceed]
```

## Updating
**Before work:** Read plan, identify next actionable task. **During:** Check off tasks, note deviations. **After:** Append progress log with completions, decisions, blockers, and what's next.

## Rules
- One plan per initiative. Tasks must be concrete. Dependencies explicit. Progress logs are append-only.
- When scope changes: add new tasks, strikethrough removed ones with a note, log the change.
- On completion: update status, add final summary, move to `plans/completed/`.