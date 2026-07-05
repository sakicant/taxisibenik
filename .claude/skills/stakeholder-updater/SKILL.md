---
name: stakeholder-updater
description: Write clear, concise stakeholder updates, status reports, and executive summaries. Use for weekly updates, project status reports, or board-level communications.
triggers:
  - stakeholder update
  - status report
  - executive summary
---

# Stakeholder Updater

Write updates that busy people actually read and act on. Respect their time by leading with the headline and being specific about what you need from them.

## The Audience-First Rule

Before writing, answer: "Who is reading this, and what decision or action should they take after reading it?"

| Audience | Reading Time | What They Care About | Format |
|----------|-------------|---------------------|--------|
| Executive / C-suite | 30 seconds | Headline, risks, asks | TL;DR + status + asks |
| VP / Director | 2 minutes | Progress vs. plan, risks, resource needs | Full status update |
| Cross-functional peers | 2-3 minutes | Dependencies, timelines, coordination needs | Progress + next steps + blockers |
| Project team | 3-5 minutes | Detailed progress, task-level status, decisions needed | Full update with task breakdown |

## Update Templates by Type

### Weekly Status Update (target: under 200 words)

```
## [Project Name] — Week of [Date]

**Status:** On Track / At Risk / Blocked

**TL;DR:** [One sentence headline. The single most important thing to know.]

### Shipped This Week
- [Deliverable] — [Impact or metric]
- [Deliverable] — [Impact or metric]

### Next Week
- [Planned work] — [Owner]
- [Planned work] — [Owner]

### Risks & Blockers
- [Risk/Blocker] — Mitigation: [Action] — Owner: [Name] — Status: [Open/Mitigated]

### Asks (Action Required)
- [Specific request] — Needed by: [Date] — From: [Name/Role]

### Key Metrics
| Metric | This Week | Last Week | Trend | Target |
|--------|-----------|-----------|-------|--------|
| [Metric] | [Value] | [Value] | ↑/↓/→ | [Target] |
```

### Executive Summary (target: under 100 words)

```
## [Topic] — Executive Summary

**Bottom line:** [One sentence: what do you need to know?]

**Status:** [On Track / At Risk / Off Track] — [Why in 5 words or fewer]

**Key numbers:**
- [Metric]: [Value] ([trend])
- [Metric]: [Value] ([trend])

**Decision needed:** [Specific decision] by [date]
— Option A: [Brief description] — [Tradeoff]
— Option B: [Brief description] — [Tradeoff]
— Recommendation: [Which option and why in one sentence]
```

### Board Update Section (for board decks)

```
## [Department/Initiative]

**Headline metric:** [The one number that matters] ([period-over-period change])

**What happened:** [2-3 sentences on key accomplishments and their business impact]

**What's next:** [1-2 sentences on upcoming milestones]

**Watch item:** [1 risk or concern the board should be aware of, with mitigation plan]
```

## Writing Principles

### Lead with the Headline
The first sentence should contain the single most important piece of information. If the reader stops after one sentence, they should still know the key takeaway.

**Bad:** "This week the team worked on several important initiatives including the database migration, the new auth flow, and some bug fixes."
**Good:** "Database migration completed 2 days ahead of schedule. Auth flow ships Monday."

### Bad News Goes First
Never bury risks or blockers at the bottom. Readers who make it to the end are the ones who least need the information. Readers who skim (executives) will miss it entirely.

**Pattern for communicating bad news:**
1. State the problem clearly
2. State the impact
3. State your mitigation plan
4. State what you need from the reader

### Be Specific About Asks
Vague asks get ignored. Specific asks get action.

| Vague (ignored) | Specific (gets action) |
|----------------|----------------------|
| "We need more resources" | "We need 1 additional backend engineer for 3 weeks to hit the March 15 deadline. Can we borrow from the Platform team?" |
| "Please review" | "Please approve the vendor contract by Friday. I have attached the SOW and a 1-page summary." |
| "Let me know if you have questions" | "I need your decision on Option A vs. B by Thursday so we can start implementation Monday." |

### Numbers Over Narratives
Replace descriptive words with data:

| Narrative | Data |
|-----------|------|
| "Significant progress" | "72% complete (up from 58% last week)" |
| "Several bugs fixed" | "Closed 14 bugs, 3 P1s remaining" |
| "Good adoption" | "340 weekly active users (up 22% MoM)" |
| "On track" | "4 of 6 milestones complete, remaining 2 on schedule for March 1" |

## Formatting Rules

- **Bullet points over paragraphs** — Every paragraph can be a bullet. Not every bullet should be a paragraph
- **Bold key information** — Numbers, decisions, and status labels should be bold
- **Status indicators** — Use consistent visual markers: On Track / At Risk / Blocked (or ✅ ⚠️ ❌)
- **Consistent cadence** — Send updates on the same day at the same time. Predictability builds trust
- **Thread the narrative** — Reference last week's update: "The API bottleneck we flagged last week is now resolved"

## Output Format

Save to `outputs/update-[audience]-[date].md` using the appropriate template from above.

## Do NOT
- Bury bad news at the bottom — put risks and blockers near the top
- Include details the audience does not need — match depth to the audience
- Use jargon the audience will not understand — executives do not know your sprint names
- Send updates without a clear "so what" — every update should answer "Why does this matter?"
- Write paragraphs when bullets will do — busy readers scan, they do not read
- Omit the ask — if you need something, say it explicitly with a deadline