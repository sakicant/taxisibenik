---
description: Execute a plan step by step
disable-model-invocation: true
---

# /implement — Execute a Plan

Read the specified plan file and execute each step in order.

For each step:
1. State which step you're working on
2. Execute it
3. Verify the result
4. Move to the next step

After completing all steps:
- Run the verification checks listed in the plan
- Update CLAUDE.md if the workspace structure changed
- Summarize what was done

Usage: `/implement [path-to-plan-file]`
Example: `/implement plans/2026-01-15-add-auth.md`