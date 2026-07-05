---
name: parallel-analyze
description: Run the same analysis or task across multiple targets in parallel, then merge the results into one report. Use when auditing many files, reviewing every module, comparing competitor pages, or processing a batch of items.
triggers:
  - audit all of these
  - review every module
  - check all files
  - parallel analysis
  - batch review
---

# Parallel Analyze

Split the same task across parallel agents (one per target), then merge their results into a single report.

## When to Use This Pattern

- The same task applies to multiple independent targets (audit 5 modules, review 8 files, analyze 12 endpoints)
- Each target can be processed independently
- You need a combined summary, not just individual results

## Process

### Phase 1: Map (Identify Targets)

List all targets. For each target, confirm:

1. It can be processed independently (no cross-dependencies)
2. The same prompt and criteria apply to all targets
3. The expected output format is consistent

### Phase 2: Map (Dispatch)

Spawn one agent per target (or per batch of small targets). All agents:

- Receive the same instructions and criteria
- Get their specific target(s) as context
- Use the same restricted tool set
- Return results in the same format

Launch all agents in parallel (multiple Agent calls in one message).

### Phase 3: Reduce (Merge)

When all agents return:

1. Collect all results
2. Deduplicate findings that appear across multiple targets
3. Rank by severity or importance
4. Produce a single summary with:
   - Overall assessment
   - Per-target highlights (only notable items, not everything)
   - Cross-cutting patterns (issues that appear in 3+ targets)
   - Recommended actions, prioritized

## Example

Task: "Security audit all API route handlers"

Map: 6 route files, each gets its own agent with the same security checklist.
Reduce: Merge into one report. Flag patterns ("4 of 6 routes missing rate limiting") over individual findings.

## Sizing Guide

| Targets | Strategy |
|---------|----------|
| 1-2 | Do not use parallel-analyze. Just do the work. |
| 3-6 | One agent per target. Ideal range. |
| 7-15 | Batch targets into 3-5 groups. One agent per group. |
| 15+ | Batch into 5-7 groups. Consider if the task scope is too broad. |

## Rules

- All map agents must use the same output format. Define it in the prompt.
- Cap at 7 parallel agents. More than that and the reduce phase becomes unwieldy.
- The reduce step is your job, not another agent's. You have the full picture.
- If one agent fails or returns poor results, re-run just that one.