---
name: skill-learnings-tracker
description: Maintain LEARNINGS.md files alongside skills that log what worked and what failed after each execution. Periodically review and graduate repeated patterns into permanent skill rules.
triggers:
  - update learnings
  - consolidate learnings
  - review skill learnings
  - graduate learnings
---

# Skill Learnings Tracker

Skills get better when they remember what worked and what didn't. This skill maintains a LEARNINGS.md file alongside each skill directory.

Every skill in `.claude/skills/` can have a LEARNINGS.md file next to it. After each time a skill runs, a short entry gets appended: what worked, what fell flat, and one thing to try differently. When the same lesson shows up three or more times, it graduates into a permanent rule in the skill itself.

## Mode 1 — Log a Learning

1. Identify which skill just ran
2. Create `.claude/skills/[skill-name]/LEARNINGS.md` if it doesn't exist with header: "# Learnings — [Skill Name]" and sections "## What Works" and "## What Fails"
3. Append a dated entry:

```markdown
## [YYYY-MM-DD] — [brief context]
**What worked:** [specific observation]
**What felt weak:** [what underperformed and why]
**Try next time:** [one actionable improvement]
```

Keep entries specific. "The output was good" teaches nothing.

## Mode 2 — Consolidate and Graduate

Run periodically (weekly is good). Read every LEARNINGS.md. For patterns appearing 3+ times:

1. Write a clear rule based on the pattern
2. Add it to the skill's SKILL.md in a "## Graduated Rules" section
3. Include a citation: `(Graduated from learnings: [dates])`
4. Move the pattern into the summary sections at the top of LEARNINGS.md

Cross-skill learnings go to `context/workspace-learnings.md`.

## Do NOT
- Log vague entries — every entry needs a specific, reusable observation
- Graduate a pattern after only one or two sightings — three is the minimum
- Delete old entries — they're the evidence trail for graduated rules