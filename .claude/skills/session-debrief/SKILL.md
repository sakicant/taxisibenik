---
name: session-debrief
description: Capture session progress, decisions, and carry-forward items through a structured interactive debrief. Use at the end of a work session.
triggers:
  - debrief
  - session summary
  - wrap up session
  - what did we do today
allowed-tools:
  - Bash
  - Read
  - Glob
---

# Session Debrief

## Writes
- `outputs/session-debrief-{date}.md`

## Process

Ask these 4 questions one at a time. Do not batch them. If the user gives a vague answer, push back and ask for specifics before proceeding.

### Question 1: What did we accomplish?
Ask: "What did we get done this session?"

After the user answers, run `git log --oneline -20` to see what actually changed. Cross-reference the git history with the user's answer. If there are commits the user did not mention, ask about them. If the user claims something that has no matching commit, note it as unverified.

### Question 2: What decisions were made?
Ask: "Were any decisions made during this session? Technical choices, process changes, strategic calls?"

For each decision, capture: what was decided, why, and what it affects. If the user says "none," check the git log for architectural changes that imply a decision.

### Question 3: What is unfinished?
Ask: "What did we start but not finish? What is still in progress?"

Look for uncommitted changes (`git status`) and unmerged branches to supplement the user's answer.

### Question 4: What should the next session start with?
Ask: "If you come back to this tomorrow, what should you pick up first?"

This is the most important section. Be specific. Not "continue the feature" but "finish the validation logic in src/lib/validators.ts, then write tests."

## Output Format

Save to `outputs/session-debrief-{date}.md`:

# Session Debrief — [date]

## Accomplishments
- [What was done, with file paths or commit references where relevant]

## Decisions
| Decision | Rationale | Affects |
|----------|-----------|---------|
| [what] | [why] | [scope] |

## Open Items
- [ ] [Unfinished task with current status and location]

## Next Session: Start Here
1. [First thing to do, with specific file paths and context]
2. [Second thing, if applicable]

## Git Summary
- Commits this session: [count]
- Files changed: [count]
- Uncommitted changes: [yes/no, list if yes]

## Common Mistakes
- Do not just echo back what the user said. Cross-reference the git log with claimed accomplishments and flag discrepancies.
- Do not produce a debrief without checking git history. The log is objective evidence of what happened.
- Do not skip the "next session" section. It is the most valuable part of the debrief and saves 10 minutes of context-loading in the next session.