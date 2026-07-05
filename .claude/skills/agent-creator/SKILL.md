---
name: agent-creator
description: Design and generate sub-agent definitions for the workspace's .claude/agents/ directory. Use when building a specialized agent from a description ("an agent that reviews PRs", "an agent that drafts customer replies"), or when you keep doing the same kind of delegation manually and want it codified. For skills (instructions Claude reads), see skill-creator.
triggers:
  - create an agent
  - design a sub-agent
  - new agent
  - i need an agent for
---

# Agent Creator

Design Claude Code sub-agents through a short interview, then generate the agent file. Agents are best when their job, tool restrictions, and context boundary are crisp.

## Gather Context First

1. Read `context/` for project conventions and existing agent patterns
2. Scan `.claude/agents/` for existing agents — avoid duplicates, match the file style
3. Identify the workspace's project type (software, marketing, sales, ops, etc.) — this shapes which tools the agent should have

## The Interview

Run these in order. Don't generate the agent until all five answers are clear.

### 1. What is the one job?

A good agent does one thing well. If the answer to "what does this agent do?" needs the word "and," push back.

| Weak (multi-job) | Strong (one job) |
|------------------|-----------------|
| "Reviews code and writes tests and documents APIs" | "Reviews code for bugs and security issues" |
| "Handles customer questions and updates the CRM" | "Drafts customer replies in our voice" |
| "Plans the week and tracks progress" | "Generates a weekly plan from quarterly priorities" |

### 2. What does the agent need to read?

List the files, directories, or external sources required. Be specific:

- Files in `outputs/transcripts/`?
- Active plans in `plans/`?
- The git diff?
- A specific reference doc?

Reading scope determines context size. Smaller scope means faster, more focused agents.

### 3. What does the agent produce?

The output should be one of:

- A specific file path (e.g. `outputs/reviews/<pr>.md`)
- A structured response shown to the user (markdown report, JSON)
- An action taken on the system (file moved, label applied)

If it's "a recommendation," push for the format — "a markdown checklist," "a 3-bullet summary."

### 4. Which tools does it need?

Default to the smallest tool surface that gets the job done:

| Agent type | Typical tools |
|------------|---------------|
| Read-only research / review | Read, Grep, Glob |
| Code writer | Read, Edit, Write, Bash, Grep, Glob |
| Auditor running commands | Read, Grep, Glob, Bash |
| External-API caller | Read + the relevant MCP tool |

Never grant Write or Edit to a read-only agent. Never grant Bash without a specific need.

### 5. What MUST the agent NOT do?

Every agent should have explicit boundaries — auto-commit, auto-push, modify shared infrastructure, send messages, delete files. Capture them as a "Do NOT" list.

## Output Format

Generate the file at `.claude/agents/<slug>.md`:

```
---
name: <slug>
description: <one sentence — what the agent does and when to use it>
tools:
  - Read
  - Grep
  - Glob
  # Add only the tools required, smallest surface
---

# <Agent Name>

<One paragraph: the agent's job, in the user's words>

## How to invoke

When this agent should be called by Claude Code (triggers, contexts, examples).

## What to read

- <Files / directories the agent needs>

## What to produce

<Specific output format and destination>

## Do NOT

- <Boundary 1>
- <Boundary 2>
```

After writing the file, update `.claude/agents/README.md` (if it exists) to list the new agent.

## Do NOT

- Generate an agent without completing all 5 interview steps — incomplete agents drift
- Grant tools the agent does not need — unused tools are a security and cost surface
- Create an agent that does what an existing one already does — propose extending the existing one instead
- Skip the "Do NOT" boundaries — agents without boundaries cause incidents
- Make the agent's job description longer than 2 sentences — if it can't be summarized, the scope is wrong