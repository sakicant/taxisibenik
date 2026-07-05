---
name: workspace-optimizer
description: Audit a Claude Code workspace for structural issues, bloat, gaps, and optimization opportunities. Use when a workspace feels slow, cluttered, or incomplete.
triggers:
  - optimize workspace
  - workspace audit
  - check my workspace
  - workspace health
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Workspace Optimizer

## Reads
- `CLAUDE.md`
- `.claude/` directory (skills, agents, rules, commands)
- `context/`
- `reference/`
- `.claude/settings.json`

## Step 1: Scan Workspace Structure

Use Glob to map the full workspace:
- `CLAUDE.md` — exists? How long?
- `.claude/skills/**/*.md` — count and list
- `.claude/agents/**/*.md` — count and list
- `.claude/rules/*.md` — count and list
- `.claude/commands/**/*.md` — count and list
- `context/*.md` — count and list
- `reference/*.md` — count and list
- `.claude/settings.json` — exists? Has hooks?

## Step 2: Check for Issues

### Oversized Files
Read each file. Flag anything over 200 lines. Long files dilute focus and waste context tokens.

### Missing Recommended Configs
Check for common gaps:
- No CLAUDE.md (critical)
- No rules directory (high impact — rules enforce consistency)
- No context files (medium — Claude lacks project knowledge)
- No settings.json or no hooks configured (low — hooks are optional but powerful)

### Unused or Redundant Components
- Skills with overlapping triggers (search for duplicate trigger phrases)
- Rules that repeat content from CLAUDE.md
- Context files that have not been updated in 90+ days (check git log)
- Agents with identical tool restrictions

### Missing Coverage
Based on the project type (infer from package.json, tech stack, or ask):
- Development projects: code review, testing, debugging skills?
- Content projects: voice guide, quality gate, SEO skills?
- Operations projects: process docs, decision tracking, meeting prep?

## Step 3: Score Workspace Health

Rate each category 0-20, totaling 0-100:

| Category | Score | What It Measures |
|----------|-------|-----------------|
| Structure | /20 | CLAUDE.md quality, directory organization, file naming |
| Context Quality | /20 | Relevance and freshness of context and reference files |
| Tool Coverage | /20 | Skills and commands for the project's common tasks |
| Rule Coverage | /20 | Rules that enforce project standards and prevent mistakes |
| Hook Coverage | /20 | Hooks for automation, safety, and workflow integration |
| **Total** | **/100** | |

## Step 4: Generate Recommendations

Prioritize by impact. For each recommendation:
- What to do (specific action)
- Why it matters (the problem it solves)
- Effort level (quick fix, moderate, significant)

Limit to 10 recommendations. Rank by impact descending.

## Output Format

Save to `outputs/workspace-audit.md`:

# Workspace Audit — [date]

## Health Score: [X]/100

| Category | Score | Summary |
|----------|-------|---------|
| Structure | [X]/20 | [one line] |
| Context Quality | [X]/20 | [one line] |
| Tool Coverage | [X]/20 | [one line] |
| Rule Coverage | [X]/20 | [one line] |
| Hook Coverage | [X]/20 | [one line] |

## Issues Found
| # | Issue | Severity | File |
|---|-------|----------|------|
| 1 | [issue] | High/Medium/Low | [path] |

## Recommendations
| Priority | Action | Impact | Effort |
|----------|--------|--------|--------|
| 1 | [what to do] | [what it fixes] | Quick/Moderate/Significant |

## Detailed Findings
[One section per category with specifics]

## Common Mistakes
- Do not recommend adding everything. A workspace with 50 skills and 30 rules is not better than one with 10 of each that are well-chosen.
- Do not flag project-specific content as "missing." A design agency does not need a code review skill.
- Do not count optional files as required. Hooks, agents, and commands are useful but not mandatory for a healthy workspace.