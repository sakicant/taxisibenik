---
name: watchdog
description: Run a background monitor agent that watches for specific conditions while the main workflow executes. Use when changes might break things (tests, types, lint) and you want continuous feedback rather than checking at the end.
triggers:
  - watch for problems
  - monitor while I work
  - background check
  - keep an eye on
---

# Watchdog

Run a background agent that monitors for problems while the main work happens. Get alerted immediately when something breaks instead of finding out at the end.

## When to Use This Pattern

- You are making changes that could break tests, types, or build
- A long-running process needs periodic health checks
- You want continuous feedback during a refactoring session

## Process

### Phase 1: Define What to Watch

Choose the monitoring targets:

- **Tests**: Run the test suite after each significant change
- **Type checking**: Run `tsc --noEmit` to catch type errors
- **Lint**: Run the linter to catch style regressions
- **Build**: Verify the project still compiles
- **Custom checks**: Any command that should stay green

For each target, define:
1. The command to run
2. What "healthy" looks like (exit code 0, specific output)
3. How often to check (after each file change, every N minutes, on demand)

### Phase 2: Set Up the Monitor

Launch the watchdog as a background agent or background Bash command:

- For simple checks: use `run_in_background` on the Bash tool with the check command
- For complex monitoring: spawn an Agent with read-only tools plus Bash, instructed to run checks periodically and report only failures

The watchdog should:
- Run checks silently when everything passes
- Report immediately when something fails
- Include the specific error output, not just "tests failed"

### Phase 3: Work with Confidence

While the watchdog runs:
- Make changes normally
- If the watchdog alerts, pause and fix the issue before continuing
- The watchdog catches regressions early, when the cause is obvious (the last change you made)

### Phase 4: Final Verification

When the main work is done, run a final comprehensive check:
- All watchdog targets, one more time
- Any checks that were too slow for continuous monitoring
- This is the "clean bill of health" before committing

## Example

Task: "Refactor the authentication module"

Watchdog setup:
- After each file save: `npm run typecheck`
- After each function change: `npm test -- --grep auth`
- On alert: stop refactoring, fix the break, then continue

Result: caught a type error 2 minutes into the refactor instead of 30 minutes later with 15 files changed.

## Rules

- Watchdog agents are read-only plus Bash for running checks. They never modify files.
- Keep checks fast. A watchdog that takes 5 minutes to run is not useful for continuous monitoring.
- Fix alerts immediately. The longer you wait, the harder it is to trace which change caused the break.
- One watchdog per concern. Do not bundle tests, lint, and types into a single slow check.
- Always run a final verification pass. The watchdog catches regressions, but the final check confirms everything is clean.