---
name: supervisor
description: Monitor task execution with validation checkpoints and retry on failure. Use for error-prone workflows, multi-step deployments, or any process where you need to verify each step succeeded before continuing.
triggers:
  - supervise this
  - monitor and retry
  - run with checkpoints
  - careful execution
---

# Supervisor

Execute a multi-step process with validation at each step. If a step fails, diagnose and retry before moving on.

## When to Use This Pattern

- A process has steps that can fail (builds, tests, deployments, migrations)
- Failures at one step should not automatically abort everything
- You need a clear log of what succeeded, what failed, and what was retried

## Process

### Phase 1: Plan with Checkpoints

For each step in the process, define:

1. **Action**: What to do
2. **Validation**: How to verify it worked (a command, a check, a file exists)
3. **Retry strategy**: What to try if it fails (fix and retry? skip? abort?)
4. **Max retries**: How many attempts before escalating (default: 2)

### Phase 2: Execute with Monitoring

Run each step and immediately validate:

```
For each step:
  1. Run the action
  2. Run the validation check
  3. If passed: log success, move to next step
  4. If failed:
     a. Read the error output
     b. Diagnose the root cause (do not just retry blindly)
     c. Apply a fix
     d. Retry (up to max retries)
     e. If still failing: log failure with diagnosis, ask user whether to skip or abort
```

### Phase 3: Report

After all steps complete (or after an abort), produce a status report:

| Step | Status | Attempts | Notes |
|------|--------|----------|-------|
| Build | Passed | 1 | |
| Lint | Passed | 2 | Fixed missing import on retry |
| Tests | Failed | 3 | Flaky test in auth module, skipped with user approval |
| Deploy | Skipped | 0 | Blocked by test failure |

## Example

Task: "Run the full CI pipeline locally before pushing"

Steps with checkpoints:
1. **Install deps**: Validate that `node_modules` exists, no errors in output
2. **Type check**: Validate exit code 0
3. **Lint**: Validate exit code 0. Retry with `--fix` then re-check
4. **Tests**: Validate all pass. Retry by re-running failed tests only
5. **Build**: Validate `dist/` created, exit code 0

## Rules

- Never retry blindly. Read the error first. The same input produces the same failure.
- Always validate after each step. Do not assume success from lack of error output.
- Log every attempt, including failures. The log is the deliverable.
- Ask the user before skipping a failed step. Do not decide on your own.
- Cap retries at 3. If it fails 3 times, the problem is not transient.