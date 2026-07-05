---
name: feature-adoption-coach
description: Match newly-released Claude Code features to the user's actual workspace and propose specific adoption steps. Use after a /feature-watch report, after reading the Anthropic changelog, or when the user asks "what's new" or "what should I be using." For greenfield workspace setup, see workspace-onboarding.
triggers:
  - what new features should i use
  - feature adoption
  - what's new for me
  - audit my workspace for new features
  - claude code update
---

# Feature Adoption Coach

Connect new Claude Code features to the user's actual workspace. Generic "here's what's new" lists don't change behavior — workspace-specific adoption plans do.

## Gather Context First

1. Find recent feature reports in `outputs/feature-watch/` if present (most recent first)
2. If none, fetch the latest entries from the Anthropic Claude Code changelog
3. Inventory the user's workspace — what's currently in `.claude/` (skills, commands, agents, hooks, settings.json)
4. Read `CLAUDE.md` for project type and conventions
5. Identify which features the user is actively using (recent file edits in `.claude/` are a signal)

## The Adoption Sequence

### Step 1 — Inventory current state

For each Claude Code primitive, mark what exists:

| Primitive | Files present | Recent activity |
|-----------|---------------|-----------------|
| Skills | Count + categories | Modified in last 30 days? |
| Commands | Count + active ones | Modified in last 30 days? |
| Agents | Count + tool restrictions | Modified in last 30 days? |
| Hooks | Active vs disabled | Any new hooks since setup? |
| MCP servers | Configured count | Any unused? |
| Settings | Permissions, env vars | Custom or default? |

This baseline determines what adoption looks like.

### Step 2 — Score each new feature for fit

For every feature in the report, score 0-3 against three lenses:

| Lens | Question | Score |
|------|----------|-------|
| Fit | Does this solve a problem the user already has? | 0-3 |
| Effort | How long to adopt? (0=hours, 3=days) | 0-3 (lower = better) |
| Reversibility | If wrong, can the user back it out? | 0-3 |

Weight: `fit * 2 - effort + reversibility`. Highest scores are the picks.

### Step 3 — Categorize each feature

Sort matched features into:

- **Quick win** — high fit, low effort. Adopt now.
- **Medium investment** — high fit, multi-day effort. Plan for next week.
- **Speculative** — interesting but unclear fit. Bookmark for the next /feature-watch run.
- **Skip** — doesn't match the workspace or duplicates existing setup.

### Step 4 — Write adoption steps for the wins

For each quick win and medium-investment item, produce:

- **Why this fits** — 1 sentence tying it to the user's workspace or recent work
- **First step** — the smallest concrete action, copy-paste ready
- **What to add or change** — specific file path and edit
- **What it replaces** (if anything) — to prevent stacking redundant tools
- **Watch out for** — known caveats, gotchas, or migration concerns

### Step 5 — Identify deprecation risk

Some new features supersede older patterns. For each:

- Is the user using a deprecated pattern? (e.g. old hook event names, old settings format)
- Is there a migration path? Document it.
- What breaks if they don't migrate?

This is the highest-leverage section. Most people miss deprecations until something breaks.

## Output Format

Save to `outputs/feature-adoption/YYYY-MM-DD.md`:

```
# Feature Adoption Plan — [Date]

## Workspace baseline
| Primitive | Count | Last updated |

## Quick wins (adopt now)
### [Feature]
- **Why this fits:**
- **First step:**
- **What to add or change:** [file path + diff]
- **Watch out for:**

## Medium-investment (plan for next week)
[Same format]

## Speculative (bookmark for re-evaluation)
- [Feature] — [why unclear]

## Skip (doesn't fit this workspace)
- [Feature] — [why]

## Deprecation risk
- [Old pattern in use] → [new pattern] — [migration step]

## Suggested next steps
1. [The single most-leveraged action]
2. ...
```

Show the plan to the user. Wait for them to pick which items to actually implement before making changes.

## Do NOT

- Recommend a feature without checking whether it duplicates something the user already has
- Propose more than 3 quick wins per session — adoption fatigue is real
- Skip the "what it replaces" line — feature stacking creates configuration debt
- Make changes to `.claude/` files without confirmation — adoption is a user decision
- Treat the changelog as a backlog — most items are skip or speculative for any given workspace
- Ignore deprecation risk to make the report look exciting — that's where the real damage lives