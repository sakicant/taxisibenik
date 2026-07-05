---
name: business-case-builder
description: Build structured business cases with ROI analysis and scenario modeling.
triggers:
  - business case
  - ROI analysis
  - build case for
---

# Business Case Builder

You build business cases that help decision-makers say yes with confidence. An honest business case acknowledges uncertainty rather than hiding it.

## Gather Context First

Check `context/` for strategic priorities, financial targets, and past business cases. Ask only for what is missing:
1. **What is the proposal?** New tool, headcount, project, partnership.
2. **Who is the decision-maker?** Their role determines what metrics matter.
3. **What is the budget cycle?** Timing affects whether this gets funded.
4. **What is the alternative?** Do nothing, build internally, buy competitor.

## Business Case Structure

### 1. Executive Summary (write last)
One paragraph: the problem, the recommendation, the expected return, and the ask. A busy executive should be able to read this alone and make a decision.

### 2. Problem Statement
- Quantify the cost of the current state. Use real numbers.
- "The team spends 15 hours/week on manual reconciliation" not "The process is inefficient."
- Include both hard costs (dollars, hours) and soft costs (risk, morale, opportunity cost).

### 3. Proposed Solution
- What you are recommending, specifically.
- Why this option over alternatives (brief comparison table).
- What is in scope and out of scope.

### 4. Financial Model

**Cost Analysis (be exhaustive):**
- One-time costs: purchase, implementation, migration, training.
- Recurring costs: licenses, maintenance, support, headcount.
- Hidden costs: integration, process change, productivity dip during transition.

**Benefit Analysis (be conservative):**
- Revenue impact: new revenue, retained revenue, upsell.
- Cost savings: labor, tools, infrastructure, error reduction.
- Productivity gains: convert time saved to dollar value using loaded cost per hour.
- Risk reduction: quantify avoided losses where possible.

**Key Metrics:**

| Metric | Formula | Target |
|--------|---------|--------|
| ROI | (Net Benefit / Total Cost) x 100 | >100% in Year 1 |
| Payback Period | Total Cost / Monthly Net Benefit | <12 months |
| NPV | Sum of discounted future cash flows - initial investment | Positive |
| IRR | Discount rate where NPV = 0 | >hurdle rate |

### 5. Scenario Analysis

Model three scenarios with clearly stated assumptions:

| | Conservative | Expected | Optimistic |
|---|---|---|---|
| Adoption rate | 60% | 80% | 95% |
| Time to value | 6 months | 3 months | 1 month |
| Annual benefit | [amount] | [amount] | [amount] |
| Payback period | [months] | [months] | [months] |

State which assumptions drive the most variance. Sensitivity analysis on the top 2-3 variables builds credibility.

### 6. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Low adoption | Medium | High | Phased rollout with training |
| Integration delays | Low | Medium | Pilot with one team first |
| Vendor lock-in | Low | High | Negotiate exit clause |

### 7. Implementation Timeline

| Phase | Duration | Key Activities | Milestone |
|-------|----------|---------------|-----------|
| Pilot | 4 weeks | Single team trial | Go/no-go decision |
| Rollout | 8 weeks | Full deployment | 80% adoption |
| Optimization | Ongoing | Measure and iterate | ROI target hit |

### 8. Recommendation
State the ask clearly: approve budget of X, hire Y people, sign contract by Z date. Include the decision criteria and what happens if the decision is delayed.

## Output Format

Save to `outputs/business-cases/`:

```markdown
# Business Case: [Title]
## Executive Summary
## Problem Statement
## Proposed Solution
## Financial Model
## Scenario Analysis
## Risks and Mitigations
## Implementation Timeline
## Recommendation
## Appendix: Assumptions and Sources
```

## Do NOT
- Use optimistic estimates for benefits and conservative estimates for costs. Apply the same rigor to both.
- Hide assumptions. State every one explicitly in an appendix.
- Present a single scenario as certain. Always show a range.
- Ignore the "do nothing" option. It is always an alternative.
- Round aggressively. False precision is better than hiding the math.
- Make the case without a clear, specific ask at the end.