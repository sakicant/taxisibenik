---
description: End-of-session review. Capture learnings, update the workspace, print a tight wrap-up.
---

# /close — Session Close

Wrap up the session warmly. **Close visually first** — print the dashboard so the user can walk away whenever — then offer the feedback questions. A user who runs /close and immediately closes the terminal must still get a clean wrap-up: the session ends successfully even if no questions are answered.

## Step 1: Recap (silent)

Scan this session and identify:
- What we worked on and completed
- What's still in motion or unresolved
- Any course-corrections the user made you should remember

## Step 2: Context freshness sweep (silent, every close)

Before printing the dashboard, sweep the `context/` directory. The user should never feel this happening. It's how the workspace stays accurate without the user having to ask.

**For every file in `context/`:**

1. **Read the date stamp.** Each context file should end with a footer like `_Updated: YYYY-MM-DD_`. If the file has no stamp, treat it as freshly generated (today's date).
2. **Compute age.** Compare the stamp date against today.
3. **If age is 30 days or less:** skip. The file is fresh.
4. **If age is over 30 days:** re-read the file and compare its contents against:
   - What you learned this session
   - Recent activity in `plans/`, `outputs/`, and (if it's a git repo) the last few commits
   - Existing memory entries for this workspace
5. **If you find specific stale facts**, fix them directly and bump the stamp to today. Examples of stale-by-time:
   - A date that has passed ("launching Feb 27" when it's now May)
   - A status that has changed ("v1 in progress" when v2 has shipped)
   - Team composition that's grown or shrunk
   - A "next step" that has been completed and superseded
   - A metric or count that's clearly out of date
6. **If the file is old but the content still appears accurate, leave it alone.** Do NOT bump the stamp without making a real change. A stale stamp is more informative than a refreshed one with no edits.
7. **Track what you changed.** The next step's dashboard will surface any file you updated under "What I'm remembering" alongside the session retraining. Files you skipped (fresh) or left alone (old but accurate) are not surfaced.

The sweep runs every close. It's cheap when files are fresh. It's how workspaces self-heal over time without any explicit maintenance step.

## Step 3: Print the closing dashboard (do this BEFORE asking anything)

```
# Your Froject workspace · Wrapped

[HH:MM] · [N files changed if any]

## What got done

▸ [accomplishment 1]
▸ [accomplishment 2]
(3-6 bullets, action-led)

## What I'm remembering

▸ [updated file]: [one-line summary]
(or "Nothing new this session.")

## Still open

▸ [carry-forward 1]
(or "Nothing pending.")

## Next time

▸ [single suggested next move]

────────────────────────────────────────
Have a good one. /prime when you're back.
```

For the "What I'm remembering" section right now, fill it with: anything the freshness sweep refreshed in Step 2, anything already obvious from this session (explicit corrections, validated approaches, decisions the user made), and anything you can capture without asking. The questions in Step 4 are for the rest.

## Step 4: Offer the optional follow-up (after the dashboard)

The session is already wrapped. Now invite (don't demand) deeper feedback:

> "If you've got 30 seconds, I can capture a few more things for next time. Otherwise this is a good stopping point. Want to keep going?"

If the user says **no, walks away, or stays silent**, the session is already closed. Do nothing further.

If the user says **yes**, ask one at a time. Any single answer is fine. After each one, save immediately so they can stop at any point and nothing is lost.

1. **"Did I get anything wrong this session?"** Misunderstandings, wrong assumptions, anything Claude should handle differently next time.
2. **"Anything I should remember for next time?"** Preferences, patterns, recurring context that would help future sessions start faster.
3. **"Any new rules or instructions to save?"** Behaviors or conventions to encode in the workspace.

## Step 5: Apply updates (only if Step 4 produced something)

For each piece of feedback, update the workspace. **Always show the diff before writing. Never update silently.**

- **CLAUDE.md** for instructions, conventions, project context
- **context/ files** for new info, priorities, decisions. **When writing to a `context/` file, also bump its `_Updated: YYYY-MM-DD_` footer to today's date.** If the file has no stamp, add one.
- **.claude/rules/** for recurring behavioral preferences (one file per rule, kebab-case name)
- **CLAUDE.local.md** for personal preferences that shouldn't be committed

After writing each update, tell the user one line: "Saved to [path]." Don't reprint the dashboard.

## Why this order

If the user types /close, sees the dashboard, and walks away, the session is closed cleanly. The dashboard IS the close. The questions are a bonus round, never a prerequisite. Never let an unanswered question hold the wrap-up hostage.

## Rules for the dashboard

- Warm and brief. This is a goodbye, not a report.
- If a section has nothing to show, print the placeholder line so the structure stays predictable.
- No em dashes. Periods, commas, or middle dot.
- Divider is exactly 40 box-drawing horizontal characters.