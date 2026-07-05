---
name: context-budget-analyzer
description: Audit the token overhead of your Claude Code workspace. Scan skills, agents, rules, and context files to find bloat and optimize what gets loaded.
triggers:
  - context budget
  - token audit
  - workspace overhead
  - how much context am I using
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Context Budget Analyzer

## Reads
- `CLAUDE.md`
- `.claude/skills/`
- `.claude/agents/`
- `.claude/rules/`
- `context/`
- `reference/`

## Step 1: Scan Workspace Components

Use Glob to find all files in:
- `.claude/skills/**/*.md`
- `.claude/agents/**/*.md`
- `.claude/rules/*.md`
- `context/*.md`
- `reference/*.md`
- `CLAUDE.md`

Read each file. Estimate token count using the approximation: 1 token per 4 characters.

## Step 2: Classify Loading Behavior

| Category | Loaded When | Impact |
|----------|------------|--------|
| CLAUDE.md | Every conversation | Always in context |
| Rules (`.claude/rules/`) | Every conversation (glob-matched) | Always in context for matching files |
| Skills (`.claude/skills/`) | On demand (triggered by user or description match) | Only when activated |
| Agents (`.claude/agents/`) | On demand (when invoked) | Only when activated |
| Context files | When referenced or read | Only when needed |

## Step 3: Flag Issues

- **Oversized files:** Any file over 5,000 tokens (20,000 characters)
- **Duplicate content:** Content that appears in multiple files (search for repeated paragraphs)
- **Always-loaded bloat:** Rules or CLAUDE.md sections that could move to on-demand skills
- **Unused components:** Skills or agents that have no clear trigger or overlap with another

## Step 4: Generate Report

### Token Budget Overview
| Component | Files | Est. Tokens | Loaded | Notes |
|-----------|-------|-------------|--------|-------|
| CLAUDE.md | 1 | [count] | Always | |
| Rules | [n] | [count] | Always (glob) | |
| Skills | [n] | [count] | On demand | |
| Agents | [n] | [count] | On demand | |
| Context | [n] | [count] | On read | |
| Reference | [n] | [count] | On read | |
| **Total** | | **[count]** | | |

### Always-Loaded Budget
Total tokens loaded in every conversation: [CLAUDE.md + matching rules]

### Flags
List each issue with the file path, estimated tokens, and a specific recommendation.

### Optimization Recommendations
Ranked by impact (tokens saved):
1. [Recommendation] — saves ~[N] tokens
2. [Recommendation] — saves ~[N] tokens

## Common Mistakes
- Do not count skills as always-loaded. They are on-demand and only enter context when triggered.
- Do not forget that CLAUDE.md is always in context. It is the single biggest token cost in most workspaces.
- Do not just count files without reading them. A 10-line file and a 500-line file in the same directory have very different costs.