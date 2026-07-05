---
name: meeting-summarizer
description: Extract key decisions, action items, and insights from meeting notes or transcripts. Use when processing meeting recordings, organizing discussion notes, or creating follow-up documents.
triggers:
  - summarize meeting
  - meeting notes
  - what was decided
  - summarize this transcript
  - extract action items
---

# Meeting Summarizer

You turn messy meeting transcripts into clear, actionable summaries. The goal is to make the meeting useful for people who attended (quick reference) and people who did not (full context).

## Processing Approach

### Step 1 — Scan for Structure

Read the entire transcript or notes first. Identify:
- Meeting type (standup, planning, retrospective, decision meeting, brainstorm, 1-on-1)
- Key participants and their roles
- The main topics discussed
- Any time markers or agenda items

### Step 2 — Extract Decisions

A decision is any statement where the group agreed on a course of action. For each:
- What was decided
- Who made or approved the decision
- What alternatives were considered (if discussed)
- Why this option was chosen

Distinguish between firm decisions and tentative agreements ("let's try this and revisit").

### Step 3 — Extract Action Items

An action item must have all three elements:
- **What**: specific task (not vague like "look into this")
- **Who**: a single person responsible (not "the team")
- **When**: a deadline or timeframe

If the transcript mentions a task without an owner or deadline, flag it as incomplete.

### Step 4 — Capture Key Discussion Points

Summarize substantive discussions that provide context for the decisions:
- Arguments for and against different approaches
- Concerns raised and how they were addressed
- New information shared that changed thinking
- Disagreements that were not resolved

### Step 5 — Identify Open Items

Track anything that needs follow-up:
- Questions that were asked but not answered
- Topics that were deferred ("let's discuss next time")
- Decisions that need more information before they can be finalized
- Risks or concerns that were raised but not mitigated

## Output Format

```
## Meeting Summary: [meeting name/topic]

**Date:** [date]
**Attendees:** [names]
**Duration:** [length]
**Type:** [standup / planning / decision / retrospective / brainstorm / other]

### TL;DR
[One sentence: what this meeting was about and the most important outcome]

### Decisions Made

| # | Decision | Decided by | Rationale |
|---|----------|-----------|-----------|
| 1 | [decision] | [person] | [why] |
| 2 | [decision] | [person] | [why] |

### Action Items

| # | Task | Owner | Due |
|---|------|-------|-----|
| 1 | [specific task] | [person] | [date] |
| 2 | [specific task] | [person] | [date] |

### Key Discussion Points
- **[Topic]**: [summary of discussion and key arguments]
- **[Topic]**: [summary of discussion and key arguments]

### Open Items
- [Question or deferred topic] — [assigned to / next step]

### Next Meeting
[Date/time if scheduled, or "not scheduled"]
```

Save meeting summaries to `outputs/meetings/` with the date as filename prefix.

## Meeting Type Variations

**Standup/sync:** Focus on blockers and status changes. Skip the discussion section. Keep it under 10 lines.

**Planning/sprint planning:** Emphasize task assignments and scope agreements. Include capacity and timeline.

**Retrospective:** Organize into "went well," "needs improvement," and "action items for next cycle."

**Decision meeting:** Lead with the decision and rationale. Include the full options that were considered.

**Brainstorm:** Capture all ideas without filtering. Group by theme. Note which ideas had energy and which were discarded.

## Do NOT

- Include filler conversation (greetings, small talk, off-topic tangents)
- Editorialize or add opinions not expressed in the meeting
- Assign action items to people who did not agree to them
- Leave action items without owners or deadlines
- Write more than one page. If the summary is longer, the meeting covered too many topics.
- Lose the "why" behind decisions. The rationale matters more than the decision itself.