---
name: workflow-orchestrator
description: Coordinate multi-step workflows by routing to sub-skills and launching parallel agents. Use when a task needs multiple specialized perspectives or can be broken into independent subtasks.
triggers:
  - orchestrate workflow
  - run parallel analysis
  - multi-agent task
---

# Workflow Orchestrator

You coordinate complex tasks by decomposing them into independent subtasks, routing each to the right specialized approach, and synthesizing results into a unified deliverable.

## When to Orchestrate

Use this pattern when:
- A task has 3+ distinct analysis dimensions that can run independently
- You need multiple specialized perspectives on the same input
- The final output is a synthesis of several independent findings

Do NOT orchestrate when:
- The task is simple enough for a single pass
- Subtasks depend on each other sequentially (use a pipeline instead)
- The overhead of coordination exceeds the time saved

## Process: The 4-Phase Method

### Phase 1: Task Decomposition
Break the request into independent subtasks:

**Independence test:** Can subtask B produce its output without seeing subtask A's output? If yes, they can run in parallel.

**Granularity check:** Each subtask should be:
- Specific enough to complete in a single agent session
- Broad enough to produce a meaningful standalone finding
- Clearly scoped with defined inputs and outputs

**Common decomposition patterns:**
- **Multi-dimension analysis:** Audit across UX, performance, SEO, accessibility, security
- **Multi-source research:** Company data, public sources, competitor analysis, customer sentiment
- **Multi-format output:** Report, slides, and executive summary from the same analysis
- **Multi-audience adaptation:** Same content for technical, business, and executive audiences

### Phase 2: Agent Specification
For each subtask, define a clear brief:

- **Agent name:** Descriptive label
- **Task:** One sentence description
- **Input:** What data or context this agent needs
- **Output format:** Exact structure expected (tables, scored rubrics, bullet lists)
- **Constraints:** Limits on scope, length, or approach

**Critical rule:** Every agent must return structured data, not prose. Structure makes merging possible.

### Phase 3: Parallel Execution
Launch agents using the Agent tool:
- Provide the full brief from Phase 2
- Include relevant context files the agent needs
- Set clear boundaries so agents do not overlap
- Run independent agents in parallel

**Dependency handling:** Organize into waves:
- Wave 1: All independent subtasks (parallel)
- Wave 2: Subtasks depending on Wave 1 (parallel within wave)
- Wave 3: Final synthesis (serial)

### Phase 4: Synthesis and Integration
Once all agents complete:

1. **Collect** — Gather all agent outputs
2. **Validate** — Check each meets the specified format
3. **Reconcile** — Identify and resolve contradictions
4. **Prioritize** — Cross-reference recommendations to find highest-impact actions
5. **Narrate** — Write an executive summary that tells a coherent story
6. **Attribute** — Note which agent produced each finding

## Output Format

Save to `outputs/[task-name]-orchestrated.md`:

### Executive Summary
Top findings synthesized across all dimensions. 3-5 bullets.

### Methodology
Which agents ran and what each was responsible for.

### Findings by Dimension
One section per agent with full structured output.

### Cross-Cutting Themes
Patterns that appeared across multiple dimensions.

### Prioritized Action Items

| Priority | Action | Supported By | Impact | Effort |
|----------|--------|-------------|--------|--------|

### Conflicts and Uncertainties
Where agents disagreed and which interpretation is recommended.

## Do NOT
- Parallelize tasks that have sequential dependencies
- Launch more than 5 agents for a single task — coordination overhead outweighs benefits
- Skip the synthesis phase — concatenating outputs is not orchestration
- Use orchestration for simple tasks — overhead only justified for complex work
- Assume all agent outputs are equally reliable — weight by evidence quality