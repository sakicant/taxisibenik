---
name: decision-tracker
description: Track and classify decisions across sessions. Use when recording a new decision, reviewing past decisions, or checking for conflicts.
triggers:
  - track decision
  - decision log
  - what did we decide
  - record this decision
allowed-tools: []
---

# Decision Tracker

## Writes
- `outputs/decisions.md`

## Step 1: Load Existing Log

Read `outputs/decisions.md` if it exists. If it does not exist, create it with the header structure below.

## Step 2: Determine Action

Ask: Are you recording a new decision, or reviewing existing ones?

Ask one question at a time. If the user gives a vague answer, push back and ask for specifics before proceeding.

### Recording a New Decision

Gather:
1. **What was decided?** — One clear sentence
2. **Context** — What prompted this decision? What alternatives were considered?
3. **Rationale** — Why this option over the alternatives?
4. **Who decided?** — Person or group
5. **Scope** — What does this affect? (architecture, process, hiring, product, messaging)

Classify the new decision:
- **NEW** — Just made, not yet tested

Check existing decisions for conflicts. If the new decision contradicts an existing one, flag it and ask the user to resolve.

### Reviewing Existing Decisions

Read the log and update statuses:
- **STABLE** — Confirmed multiple times, still valid
- **VOLATILE** — Changed recently or under reconsideration
- **CONFLICTING** — Contradicts another decision in the log
- **NEW** — Recently added, not yet validated

For each decision, ask: Is this still true? Has anything changed?

## Output Format

Maintain `outputs/decisions.md` with this structure:

# Decision Log

Last updated: [date]

## Active Decisions

| # | Decision | Status | Date | Decided By | Scope |
|---|----------|--------|------|-----------|-------|
| 1 | [decision] | STABLE | [date] | [who] | [scope] |
| 2 | [decision] | NEW | [date] | [who] | [scope] |

## Decision Details

### Decision #1: [short title]
- **Status:** STABLE
- **Date:** [date]
- **Decided by:** [who]
- **Context:** [what prompted it]
- **Rationale:** [why this option]
- **Alternatives considered:** [what else was on the table]
- **Affects:** [what this decision impacts]

## Archived Decisions
Decisions that were reversed or superseded. Keep for history.

## Common Mistakes
- Do not track implementation details as decisions. "Use PostgreSQL" is a decision. "Create the users table with these columns" is implementation.
- Do not mark everything as STABLE. A decision is only STABLE after it has been tested or reaffirmed.
- Do not skip the rationale field. A decision without rationale cannot be evaluated later when circumstances change.