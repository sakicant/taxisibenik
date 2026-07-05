---
name: debate
description: Have multiple agents argue different positions on a question or decision, then synthesize the strongest answer from their arguments. Use for architecture decisions, strategy choices, or any situation where you want multiple perspectives stress-tested.
triggers:
  - debate this
  - argue both sides
  - devil's advocate
  - multiple perspectives
  - pros and cons
---

# Debate

Get better decisions by having agents argue different positions. Quality comes from disagreement, not consensus.

## When to Use This Pattern

- A decision has multiple valid options with real tradeoffs (REST vs. GraphQL, monolith vs. microservices)
- You want to stress-test a proposal before committing
- The stakes are high enough to justify hearing both sides
- You suspect confirmation bias in the current direction

## Process

### Phase 1: Frame the Question

Define the debate clearly:

1. **The question**: What specific decision needs to be made?
2. **The positions**: What are the 2-3 options being considered?
3. **The criteria**: What matters most? (cost, speed, maintainability, user experience)
4. **The context**: What constraints exist? Read relevant `context/` files for background.

### Phase 2: Assign Positions

Spawn one agent per position. Each agent:

- Argues FOR their assigned position (not against others)
- Must provide concrete evidence: code examples, data, precedent
- Must acknowledge the strongest argument against their position
- Returns a structured brief: thesis, evidence, risks, and the one reason to pick this option

Give all agents the same context and criteria. The only difference is their assigned position.

### Phase 3: Rebuttal (Optional)

For high-stakes decisions, run a second round:

1. Share each agent's brief with all other agents
2. Each agent responds to the strongest point from the opposing position
3. This round often surfaces risks that the first round missed

### Phase 4: Judge

You are the judge. Do not delegate this step. Review all arguments and:

1. List the strongest points from each position
2. Identify where agents agreed (these points are likely true regardless of position)
3. Identify where they disagreed most sharply (these are the real tradeoffs)
4. Make a recommendation with clear reasoning
5. Document what you would watch for if the decision turns out wrong

## Example

Task: "Should we use a monorepo or separate repos for our three services?"

Agents:
- Agent A argues for monorepo: shared tooling, atomic changes, single CI pipeline
- Agent B argues for polyrepo: independent deploys, team autonomy, smaller blast radius
- Agent C argues for hybrid: shared libs in monorepo, services in separate repos

Judge synthesizes: monorepo wins for a team of 8 with shared infrastructure, but set up CODEOWNERS early to prevent coupling.

## Rules

- Minimum 2 positions, maximum 4. More than 4 dilutes the arguments.
- Agents must argue FOR their position, not just attack others.
- Every claim must have evidence. "It's better" is not an argument.
- The judge step is always done by you, never delegated. You have full context.
- Document the decision and reasoning in `outputs/` so future sessions can reference it.