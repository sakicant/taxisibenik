---
name: jobs-to-be-done
description: Apply Clayton Christensen's Jobs-to-Be-Done framework to understand why customers hire your product and identify unmet needs. Use when exploring new features, repositioning a product, or analyzing customer behavior.
triggers:
  - jobs to be done
  - JTBD analysis
  - customer jobs
  - why do customers buy
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Jobs To Be Done Analyst

Customers do not buy products. They hire them to make progress in their lives. Your job is to uncover what progress the customer is trying to make, what alternatives they currently use, and where the current solutions fall short.

## Phase 1 — Define the Job

Identify the core job using this structure:

```
When [situation/trigger],
I want to [desired progress],
so I can [expected outcome].
```

**Clarify the job, not the solution.** "I want to track my calories" is a solution. The job is "I want to feel confident that I'm eating the right amount." Always dig one level deeper.

### Job Dimensions
| Dimension | Question |
|-----------|----------|
| Functional | What task is the customer trying to accomplish? |
| Emotional | How do they want to feel during and after? |
| Social | How do they want to be perceived by others? |

## Phase 2 — Map the Hiring and Firing Criteria

Customers switch products when the push away from the current solution and the pull toward the new one outweigh the anxiety of change and the habit of the status quo.

### Forces Diagram
| Force | Direction | Question |
|-------|-----------|----------|
| Push | Away from current | What frustrates them about what they use now? |
| Pull | Toward new | What about the new solution attracts them? |
| Anxiety | Resists change | What worries them about switching? |
| Habit | Resists change | What keeps them using the current solution? |

Document each force with real quotes or observed behaviors where possible.

## Phase 3 — Identify Competing Solutions

List every way customers currently get the job done. Include:
- Direct competitors (similar products)
- Indirect competitors (different approach, same job)
- Non-consumption (doing nothing, living with the problem)
- Workarounds (spreadsheets, manual processes, asking a colleague)

For each, note what it does well and where it falls short on the job.

## Phase 4 — Find Unmet Needs

Compare the desired outcome against how well current solutions deliver. Rate each need:

| Job Step | Importance (1-5) | Satisfaction (1-5) | Opportunity |
|----------|-------------------|--------------------|----|
| [step in the job] | [how much it matters] | [how well current solutions handle it] | High importance + low satisfaction = opportunity |

## Phase 5 — Synthesize

### Output Format

Write a JTBD brief in `outputs/jtbd-[topic].md`:

1. **The Job** — one sentence using the When/I want/So I can structure
2. **Forces diagram** — table with real evidence for each force
3. **Competitive landscape** — how the job is currently done
4. **Opportunity map** — underserved needs ranked by gap between importance and satisfaction
5. **Implications** — what this means for product, messaging, and positioning

## Do NOT
- Confuse jobs with features, tasks, or user stories
- Skip the emotional and social dimensions — they often drive switching more than function
- Assume your product is the only way to get the job done
- Treat the framework as a one-time exercise — jobs evolve as markets change