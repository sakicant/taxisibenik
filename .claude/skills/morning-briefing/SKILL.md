---
name: morning-briefing
description: Generate a structured daily briefing from active tasks and priorities.
triggers:
  - morning briefing
  - start my day
  - daily brief
---

# Morning Briefing

You help people start their day with clarity and focus. A morning briefing replaces the 20 minutes of tab-switching and app-checking that most people do to figure out where they left off.

## Gather Context First

Read `context/` files, `plans/` for active plans, and any task tracking files in the workspace. Check for:
1. **Active tasks** — What is in progress? What was last worked on?
2. **Commitments** — Meetings, deadlines, promises made to others.
3. **Blockers** — What is waiting on someone else?
4. **Recent changes** — What happened since the last work session?

## Briefing Framework: The Eisenhower Sort

Categorize every task before presenting:

| | Urgent | Not Urgent |
|---|---|---|
| **Important** | Do first (crises, deadlines today) | Schedule (strategic work, deep focus) |
| **Not Important** | Delegate or timebox (requests, meetings) | Eliminate or defer (busywork, low-value) |

The briefing should make the Eisenhower quadrant obvious without the reader having to think about it.

## Briefing Structure

### 1. Today's Focus (2-3 items max)
The most important outcomes for the day. Not tasks, outcomes.
- "Ship the onboarding flow redesign" not "Work on onboarding."
- "Get sign-off on Q3 budget" not "Review budget doc."

### 2. Calendar Scan
For each meeting today:
- **Time and title** — What and when.
- **Prep needed** — What to read, bring, or decide before the meeting.
- **Your role** — Presenting, deciding, or attending for awareness.
- Flag meetings that can be skipped or shortened.

### 3. Active Work
| Task | Status | Next Action | Blocked? |
|------|--------|-------------|----------|
| [task name] | In progress / Waiting / Ready | [specific next step] | [who/what] |

### 4. Approaching Deadlines
Items due in the next 3 business days:
- **Today:** [items] — must be completed.
- **Tomorrow:** [items] — should be progressed.
- **This week:** [items] — need attention if not started.

### 5. Quick Wins (optional)
Tasks that take under 15 minutes and clear mental overhead:
- Reply to [person] about [topic].
- Approve [PR / request].
- Update [document].

### 6. Suggested Focus Order
A numbered sequence for the day:
1. [First: highest-impact deep work before meetings start]
2. [Second: time-sensitive items]
3. [Third: collaborative work during meeting hours]
4. [Fourth: low-energy tasks for end of day]

## Energy Mapping

When possible, match tasks to energy levels:

| Time Block | Energy | Best For |
|-----------|--------|----------|
| First 2 hours | Peak focus | Deep work, writing, complex problems |
| Mid-morning | High | Meetings, collaboration, decisions |
| After lunch | Lower | Admin, reviews, quick tasks |
| Late afternoon | Declining | Planning tomorrow, clearing inbox |

## Output Format

Present the briefing as a clean markdown document:

```markdown
# Morning Briefing — [Day, Date]

## Focus Today
1. [Outcome 1]
2. [Outcome 2]

## Calendar
[time] — [meeting] (prep: [what])
[time] — [meeting] (prep: [what])

## Active Work
[task table]

## Deadlines
[deadline list]

## Suggested Order
1. [task] (deep work, 9-11am)
2. [task] (after standup)
3. [task] (afternoon)
```

## Do NOT
- List more than 3 focus items. If everything is a priority, nothing is.
- Include tasks the user cannot act on today.
- Skip the "next action" for active tasks. Vague status is not helpful.
- Present the briefing as a wall of text. Use tables and bullets for scannability.
- Forget to flag blockers. Unblocking should happen before deep work.