---
name: ab-test-designer
description: Design A/B tests with clear hypotheses, sample size calculations, and analysis plans. Use when planning experiments for product features, landing pages, or marketing campaigns.
triggers:
  - design A/B test
  - experiment design
  - split test
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# A/B Test Designer

Design experiments that produce statistically trustworthy results. Every test must have a pre-registered hypothesis, sample size calculation, and decision criteria before it starts running.

## Phase 1 — Hypothesis Formation

A valid hypothesis follows this structure:

```
If we [specific change to the experience],
then [primary metric] will [increase/decrease] by at least [minimum detectable effect],
because [behavioral mechanism or CRO principle].
```

**Quality checks for hypotheses:**
- Is the change specific enough to implement? ("Improve the CTA" is too vague. "Change CTA text from 'Submit' to 'Get My Free Report'" is testable.)
- Is there a behavioral reason it should work? (Not just "let's try it" — cite a CRO principle, user research finding, or competitive observation.)
- Is the expected effect realistic? (A button color change will not double conversion. A completely redesigned flow might.)

## Phase 2 — Metric Selection

### Primary Metric (exactly one)
The single metric that determines whether the test wins, loses, or is inconclusive. Choose a metric that:
- Is directly impacted by the change
- Can be measured within the test window
- Has a clear business connection

### Guardrail Metrics (2-4)
Metrics that must NOT degrade. If the primary metric improves but a guardrail degrades, the test is a failure.

| Metric Type | Example | Purpose |
|------------|---------|---------|
| Primary | Signup conversion rate | Decision metric |
| Guardrail | Page load time | Don't break performance |
| Guardrail | Support ticket rate | Don't confuse users |
| Guardrail | Revenue per visitor | Don't lose money |

### Secondary Metrics (optional, 1-3)
Metrics that provide additional insight but do not determine the test outcome. Useful for understanding why the primary metric moved.

## Phase 3 — Sample Size Calculation

Calculate the required sample size BEFORE starting the test:

### Required Inputs
| Parameter | Value | Notes |
|-----------|-------|-------|
| Baseline conversion rate | [X%] | Current rate from analytics |
| Minimum detectable effect (MDE) | [X% relative] | Smallest change worth detecting |
| Statistical significance | 95% (alpha = 0.05) | Standard for most tests |
| Statistical power | 80% (beta = 0.20) | Standard for most tests |
| Number of variants | 2 (control + treatment) | Add more only with justification |

### Sample Size Guidance
Use Evan Miller's sample size calculator (or equivalent) with your baseline rate and MDE. As a reference point: a 5% baseline rate with 10% relative MDE requires roughly 145,000 visitors per variant at 95% confidence / 80% power. Lower baselines and smaller MDEs need dramatically larger samples.

### Duration Calculation
```
Duration (days) = (Sample per variant x Number of variants) / Daily eligible traffic
```

**Rules:**
- Minimum duration: 7 days (to capture day-of-week effects)
- Maximum duration: 4 weeks (after which external factors introduce noise)
- Never run a test for less than one full business cycle

## Phase 4 — Experiment Design

### Variant Specification
| Element | Control (A) | Treatment (B) |
|---------|------------|--------------|
| [Changed element] | [Current state] | [New state] |
| [Screenshot/description] | [Details] | [Details] |
| Everything else | Identical | Identical |

**Isolation rule:** Change exactly ONE variable between control and treatment. If you change the headline AND the button color, you cannot attribute the result to either change.

### Randomization
- Random assignment at the user level (not session level) to avoid the same user seeing different variants
- Use a consistent hashing algorithm (not Math.random()) so users get the same variant on return visits
- Verify 50/50 split with a Sample Ratio Mismatch (SRM) check before analyzing results

### Exclusion Criteria
Define who is excluded from the test before it starts:
- Internal users / test accounts
- Users in other active experiments on the same surface
- Users who cannot experience the change (e.g., mobile users if testing a desktop-only feature)

## Phase 5 — Analysis Plan

Pre-register the analysis plan to prevent p-hacking:

### Decision Matrix
| Result | Primary Metric | Guardrails | Decision |
|--------|---------------|-----------|----------|
| Clear win | Statistically significant positive | All stable | Ship |
| Win with concerns | Significant positive | One degraded | Investigate, likely iterate |
| Inconclusive | Not significant | All stable | Extend test or kill |
| Clear loss | Statistically significant negative | Any | Kill |
| Guardrail failure | Any | Significant degradation | Kill immediately |

### Peeking Policy
- Do not check results before the calculated end date
- If you must peek (e.g., for safety), use a sequential testing framework with alpha spending functions
- Never end a test early because it "looks significant" — this inflates false positive rates

Pre-register at most 1-2 subgroup analyses (e.g., device type, traffic source, or user segment). Any unplanned subgroup analyses are exploratory only, not conclusive.

## Output Format

Save to `outputs/ab-test-[test-slug].md` with:

### Test Card
```
Name: [Descriptive test name]
Hypothesis: [Full hypothesis with mechanism]
Primary metric: [Metric name] (baseline: [X%])
MDE: [X% relative change]
Sample needed: [N per variant] ([N total])
Estimated duration: [X days] at [Y daily visitors]
Start date: [Date]
End date: [Date]
```

### Decision Criteria
- **Ship if:** Primary metric improves by >= MDE with p < 0.05 AND no guardrail degradation
- **Kill if:** Primary metric degrades with p < 0.05 OR any guardrail degrades significantly
- **Iterate if:** Inconclusive after full duration

### Implementation Notes
- Randomization method and split ratio
- Feature flag name and configuration
- Exclusion criteria
- Tracking events needed

## Do NOT
- Run a test without calculating sample size first — underpowered tests waste time and produce unreliable results
- End tests early based on peeking — this dramatically increases false positive rates
- Test multiple changes simultaneously in one experiment — you cannot attribute the result
- Declare a winner at p = 0.049 and a loser at p = 0.051 — these results are practically identical
- Run post-hoc subgroup analyses and present them as primary findings
- Ignore guardrail metrics when the primary metric looks good