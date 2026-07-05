---
name: maker-checker
description: One agent creates output, a separate agent validates against criteria, and they loop until the checker approves. Use for code that needs review, content that needs editing, or any output where quality must be verified independently.
triggers:
  - make and check
  - create then validate
  - build and review
  - write then verify
---

# Maker-Checker

Separate creation from validation. One agent builds, another checks. They loop until the output passes.

## When to Use This Pattern

- Output quality matters and self-review is not enough
- You have clear acceptance criteria that can be checked independently
- The creator should focus on building, not second-guessing

## Process

### Phase 1: Define Acceptance Criteria

Before any work starts, write down what "done" looks like:

- What must the output contain?
- What must it NOT contain?
- What quality bar must it meet? (compiles, passes tests, follows conventions, reads clearly)
- Maximum iterations before escalating to the user (default: 3)

### Phase 2: Make

Spawn the Maker agent with:
- The full task description
- All relevant context
- The acceptance criteria (so it knows what the Checker will look for)
- Write and edit tools as needed

The Maker produces the first version.

### Phase 3: Check

Spawn the Checker agent with:
- The Maker's output
- The acceptance criteria
- Read-only tools (the Checker never modifies the output directly)

The Checker returns one of:
- **PASS**: Output meets all criteria. Include a brief summary of what was verified.
- **FAIL**: Output does not meet criteria. List specific issues with line references.

### Phase 4: Loop or Deliver

If PASS: deliver the output. Done.

If FAIL: send the Checker's feedback back to the Maker as a new agent call. The Maker revises and resubmits. Repeat until PASS or max iterations.

If max iterations reached: present both the latest output and the remaining issues to the user for a decision.

## Example

Task: "Write a database migration to add user preferences"

Round 1:
- Maker writes the migration
- Checker reviews: "FAIL. Missing rollback function. No index on user_id foreign key."

Round 2:
- Maker revises with Checker's feedback
- Checker reviews: "PASS. Migration includes up/down, indexes, and matches existing naming conventions."

## Rules

- The Checker never edits the output. It only judges.
- The Maker receives the Checker's full feedback, not a summary. Specifics drive better revisions.
- Cap at 3 iterations. If 3 rounds of feedback cannot fix it, the task needs rethinking, not more loops.
- Keep the Checker's tool set minimal. Read and Grep only. Independence is the point.
- The acceptance criteria must be written before the first Make. Do not add new criteria mid-loop.