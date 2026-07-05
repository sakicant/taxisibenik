---
name: model-strategy
description: Audit your workspace's model usage and recommend the right model for each agent, command, and task type. Balances capability against cost. Use when setting up a new workspace, reviewing costs, or after Claude releases new models.
triggers:
  - which model should I use
  - model selection
  - model strategy
  - optimize model costs
  - advisor pattern
  - haiku vs sonnet vs opus
allowed-tools: []
---

# Model Strategy

Help the user assign the right Claude model to each part of their workspace.

## Context Scan

Check `context/` for:
- Budget constraints or cost sensitivity
- Task complexity (are most tasks routine or complex?)
- Agent definitions in `.claude/agents/`

## The Three Models

| Model | Best For | Cost | Speed |
|-------|---------|------|-------|
| **Opus 4.8** | Complex reasoning, architecture decisions, code review, strategic planning, multi-step analysis | Highest | Slower |
| **Sonnet 4.6** | General-purpose work, writing, editing, most coding tasks, research | Medium | Fast |
| **Haiku 4.5** | Simple lookups, formatting, summarization, high-volume repetitive tasks | Lowest | Fastest |

## The Advisor Pattern

For complex workflows, pair a cheaper model with Opus as an advisor:

- The **executor** (Sonnet or Haiku) handles the bulk of the work: calling tools, reading files, writing output
- The **advisor** (Opus) gets consulted only for hard decisions: architecture choices, ambiguous requirements, complex debugging

This gives you near-Opus quality at a fraction of the cost. The executor does 90% of the work at Sonnet/Haiku rates. Opus only runs for the 10% that actually needs deep reasoning.

## Step 1 — Inventory Current Usage

List every agent, command, and recurring task in the workspace. For each one:

| Task/Agent | Current Model | Complexity | Frequency | Recommendation |
|-----------|--------------|-----------|-----------|----------------|
| [Name] | [Model or default] | High/Med/Low | Daily/Weekly/Rare | [Suggested model] |

## Step 2 — Assign Models

Apply these rules:

**Use Opus when:**
- The task involves multi-file architecture decisions
- Errors are expensive (production code review, security audit)
- The task requires holding many constraints in mind simultaneously
- Strategic planning, positioning, or complex analysis

**Use Sonnet when:**
- General coding, writing, editing, and research
- Tasks that need good quality but not frontier reasoning
- Most daily workflows (morning briefs, drafts, reports)

**Use Haiku when:**
- Formatting, linting, simple file transformations
- Looking up information in known locations
- High-volume tasks where cost matters more than polish
- Summarizing content that is already well-structured

## Step 3 — Configure Agents

For each agent in `.claude/agents/`, set the model field:

```yaml
model: claude-sonnet-4-6  # or claude-opus-4-8 or claude-haiku-4-5
```

Agents that review, plan, or make architectural decisions should use Opus. Agents that execute well-defined tasks should use Sonnet or Haiku.

## Step 4 — Estimate Cost Impact

Show the user a rough cost comparison:

| Strategy | Relative Cost | Quality |
|----------|--------------|---------|
| All Opus | 6x baseline | Highest |
| All Sonnet (baseline) | 1x | High |
| Sonnet + Opus advisor | ~1.2x | Near-Opus |
| Haiku + Opus advisor | ~0.15x | Good |
| All Haiku | 0.04x | Adequate for simple tasks |

## Output

Write to `outputs/model-strategy.md`:

1. **Current state** — what models are in use now
2. **Recommendations** — model assignment per agent/task with rationale
3. **Cost impact** — estimated savings or quality improvement
4. **Agent config changes** — exact model field values to set

## Do NOT
- Recommend Opus for everything. Most tasks do not need frontier reasoning. Overspending on model costs is as wasteful as underspending is risky.
- Recommend Haiku for tasks where mistakes are costly. The savings are not worth it if the output needs heavy correction.
- Ignore the user's budget. If they are cost-sensitive, lean toward Haiku + Opus advisor. If quality is paramount, lean toward Sonnet + Opus advisor.
- Forget to update agent definitions. A strategy document that does not result in config changes is just a wish list.