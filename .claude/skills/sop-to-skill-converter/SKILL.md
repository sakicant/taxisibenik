---
name: sop-to-skill-converter
description: Convert team SOPs, process documents, and workflow descriptions into properly structured Claude Code skills.
triggers:
  - convert SOP to skill
  - turn process into skill
  - SOP to skill
  - process to skill
---

# SOP to Skill Converter

Turn existing team processes into Claude Code skills. Paste a process document and get back a SKILL.md ready to drop into `.claude/skills/`.

## Step 1 — Gather the Source

Accept any format: pasted text, a file path to read, a URL, or a verbal description.

## Step 2 — Analyze the Process

Break into: Purpose, Trigger conditions, Inputs, Steps (action + success criteria + common mistakes), Outputs, Quality checks, Edge cases.

## Step 3 — Generate the Skill

Create SKILL.md with: frontmatter (name, description, triggers), overview, When to Use, Inputs, Process steps with success criteria, Quality Checks checklist, Common Mistakes, Output Format.

## Step 4 — Review

Show the generated skill and ask: "Does this capture the process accurately? Any steps missing?"

## Principles
- Preserve expert knowledge — don't simplify away nuance
- Make implicit knowledge explicit — ask about gaps
- Add 3-5 natural language trigger phrases
- Include the "why" — helps Claude make judgment calls in edge cases
- Keep under 150 lines — split complex SOPs into multiple skills