---
description: Fetch tasks from your task management tool, rank them, and start working
disable-model-invocation: true
---

# /work — Daily Task Execution

Fetch tasks from your connected task management tool, rank them, and route to the right skill.

**Configured tool:** (injected at generation time)

---

## Workflow

1. **Fetch tasks** — Query your task management tool via MCP for active/in-progress tasks assigned to the user
2. **Rank** — Sort by deadline urgency, then priority, then recent activity
3. **Present** — Show top 5-7 tasks in a numbered list with status, deadline, and summary
4. **Select** — User picks a task number (or use `/work next` for highest-priority, `/work [keyword]` to filter)
5. **Route** — Match the task to the best available skill and start working
6. **Document** — After completing work, update the task in the tool with a summary of what was done

## Usage

- `/work` — show top tasks, pick one
- `/work next` — start highest-priority task immediately
- `/work 3` — start task #3 from the list
- `/work [keyword]` — filter tasks by keyword

## Fallback

If no task-tool MCP is responding yet, don't block. In order:
1. Ask the user to paste their current task list (or just describe what they need to get done today)
2. If they haven't run `/hatch` yet, gently suggest it so the integration gets set up properly
3. Work with whatever they share, then offer to write tasks back to the tool once it's connected