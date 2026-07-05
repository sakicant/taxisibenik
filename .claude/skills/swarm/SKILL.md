---
name: swarm
description: Dynamic agent coordination where each agent's findings determine what to investigate next. Use for debugging, root cause analysis, or exploratory research where the path is not known upfront.
triggers:
  - investigate this
  - figure out what's going on
  - root cause analysis
  - explore and report
  - dynamic investigation
---

# Swarm

Coordinate a dynamic investigation. Spawn agents based on what previous agents discover. The investigation path is not fixed. It emerges from findings.

## When to Use This Pattern

- You do not know upfront what you are looking for (debugging, root cause analysis)
- Each discovery opens new questions that need different expertise
- The task is exploratory, not procedural

## Process

### Phase 1: Initial Probe

Start with 1-2 broad reconnaissance agents:

- One to gather symptoms (logs, errors, recent changes)
- One to map the relevant area (architecture, dependencies, data flow)

Keep these agents read-only. The goal is information, not changes.

### Phase 2: Follow the Trail

Based on initial findings, spawn focused agents to investigate specific leads:

1. Review what the initial agents found
2. Identify the 2-3 most promising leads
3. Spawn an agent for each lead with a specific question to answer
4. When results come back, decide: is the answer clear, or do we need to dig deeper?

Repeat until you reach a root cause or a clear conclusion.

### Phase 3: Converge

Once you have enough information:

1. Lay out all findings from all agents
2. Connect the dots. What story do the findings tell together?
3. Distinguish between confirmed facts and hypotheses
4. Propose a solution or next step with evidence

## Example

Task: "Users report intermittent 500 errors on the dashboard"

Round 1 (parallel):
- Agent A: Check error logs for the last 24 hours. Finds "connection pool exhausted" errors.
- Agent B: Check recent deploys and config changes. Finds a connection limit was lowered yesterday.

Round 2 (based on round 1):
- Agent C: Trace the connection pool config change. Who changed it, why? Finds it was part of a cost-reduction PR.
- Agent D: Check current connection usage vs. the new limit. Finds peak usage exceeds the new limit by 3x.

Conclusion: The connection pool limit reduction from the cost PR is too aggressive for peak traffic. Recommend reverting to the previous limit and finding a different cost optimization.

## Rules

- Maximum 3 rounds of investigation. If 3 rounds do not converge, summarize findings and ask the user for direction.
- Each round should have fewer agents than the previous (converging, not diverging).
- Read-only agents for investigation. Only spawn write-capable agents when you have a confirmed fix.
- Label each agent's findings clearly. When synthesizing, cite which agent found what.
- Do not chase every lead. Pick the 2-3 most likely after each round.