---
description: Scan recent work for repeatable patterns and propose new skills
---

# /discover-skills — Skill Discovery

Scan recent sessions and workspace activity to find repeatable processes that should become skills.

## Step 1: Gather Session History

Look at the last 7 days of activity:

1. Read `outputs/` for recently created files — what kind of work happened?
2. Run `git log --oneline --since="7 days ago"` to see recent commits
3. Read `.claude/commands/` and `.claude/skills/` to know what already exists
4. If MCP tools are connected (Notion, Linear, Slack, etc.), scan recent activity there for repeated workflows

## Step 2: Identify Patterns

Look for processes that meet ALL of these criteria:

- **Repeated** — happened more than once in the past week
- **Multi-step** — involves 3+ distinct actions (not just a single command)
- **Consistent** — follows roughly the same steps each time
- **Not already a skill** — check existing skills to avoid duplicates

Common patterns to watch for:
- Files created with the same structure repeatedly
- The same sequence of tool calls across sessions
- Multi-file edits that follow a template
- Research-then-output workflows with consistent formats
- Review or audit processes with repeated checklists

## Step 3: Propose Skills

For each pattern found, present a skill candidate:

| Field | Value |
|-------|-------|
| **Name** | Clear, action-oriented name |
| **Trigger** | When would someone invoke this? |
| **Steps** | The repeatable process (3-8 steps) |
| **Input** | What does the user need to provide? |
| **Output** | What gets produced? (file, report, decision) |
| **Estimated time saved** | Per use, roughly |

## Step 4: Build Approved Skills

For each skill the user approves:

1. Create the skill file in `.claude/skills/` with proper frontmatter (name, description, triggers)
2. Write substantive instructions — not a skeleton, a complete skill that works immediately
3. Include output format and "Do NOT" guardrails
4. Show the user the file before writing it

## Do NOT

- Propose skills for things that happened only once
- Create overly broad skills ("do research") — be specific about the workflow
- Propose skills that duplicate existing commands or skills
- Include any sensitive data from the scanned sessions in the skill content
- Skip the approval step — always let the user decide which candidates to build