---
name: sequential-handoff
description: Pass work through ordered stages where each builds on the previous result. Use when quality depends on doing things in the right order (draft then review then polish).
triggers:
  - run this through stages
  - sequential review
  - chain these steps
  - stage by stage
---

# Sequential Handoff

Pass work through a series of agents where each stage builds on and improves the previous stage's output.

## When to Use This Pattern

- Quality depends on doing things in order (research before writing, writing before review)
- Each stage transforms or improves the output of the previous stage
- You want separation of concerns between stages (the writer should not also be the editor)

## Process

### Phase 1: Define the Chain

Map out the stages. Each stage should:

1. Have a clear input (what it receives from the previous stage)
2. Have a clear output (what it passes to the next stage)
3. Have clear success criteria (how to tell if this stage is done)

Write the chain before starting.

### Phase 2: Execute

Run each stage as a separate agent call. Between stages:

1. Review the output before passing it forward
2. Check if the output meets that stage's success criteria
3. If it doesn't, re-run the stage with feedback (not a new agent, just clarification)
4. Pass the validated output as input context to the next stage

### Phase 3: Deliver

After the final stage, review the end-to-end result. The final output should show improvement at each stage without losing the core intent from stage 1.

## Example

Task: "Write a technical blog post about our new caching layer"

Chain:
1. **Research**: Agent reads the codebase, gathers facts, produces an outline with key points
2. **Draft**: Agent takes the outline, writes the full post
3. **Technical Review**: Agent checks accuracy, catches errors, flags unclear explanations
4. **Edit**: Agent polishes language, tightens structure, ensures consistent voice
5. **Final Check**: Agent verifies all technical claims against the code one more time

Each agent gets the previous agent's output as input context.

## Rules

- Maximum 5 stages. If you need more, some stages should be combined.
- Each stage's agent prompt must include the previous stage's full output.
- Read each stage's result and flag anything the next agent should watch for.
- If a stage fails, re-run that stage. Do not restart the whole chain.