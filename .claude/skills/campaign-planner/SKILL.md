---
name: campaign-planner
description: Plan marketing campaigns end-to-end with messaging, channels, and timeline.
triggers:
  - plan campaign
  - marketing campaign
  - launch plan
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Campaign Planner

You plan marketing campaigns that are specific, measurable, and executable. A campaign without a measurement plan is just spending money.

## Gather Context First

Check `context/` for ICP definitions, brand voice guidelines, and past campaign performance. Ask only for what is missing:
1. **What is the campaign goal?** Leads, signups, pipeline, awareness, retention.
2. **Who is the target audience?** Persona, segment, account list, funnel stage.
3. **What is the budget?** This determines channel mix and asset scope.
4. **What is the timeline?** Launch date and campaign duration.
5. **What assets already exist?** Landing pages, case studies, testimonials, creative.

## Campaign Planning Framework

### Phase 1: Strategy (Week 1)

**Goal Setting (SMART):**
- Specific: "Generate 200 MQLs" not "increase leads."
- Measurable: Define the metric and tracking method.
- Achievable: Based on historical benchmarks or industry averages.
- Relevant: Tied to a business objective (pipeline target, launch KPI).
- Time-bound: Campaign start and end dates.

**Audience Definition:**
- Primary persona: role, company size, industry, pain points.
- Funnel stage: awareness, consideration, decision.
- Exclusions: who is NOT the audience (prevents wasted spend).

**Message Architecture:**
- **Core message:** The one thing the audience should remember (1 sentence).
- **Proof points:** 3 evidence items that support the core message.
- **Objection handling:** Top 3 objections and how to address each.
- **CTA:** What the audience should do (one per touchpoint).

### Phase 2: Channel Plan (Week 1-2)

Select channels based on where the audience is, not what is trendy:

| Channel | Best For | Content Type | Frequency | Budget % |
|---------|----------|-------------|-----------|----------|
| Email (owned list) | Nurture, retention | Sequences, newsletters | 2-3x/week during campaign | 10% |
| LinkedIn (organic) | Awareness, thought leadership | Posts, articles, carousels | 3-5x/week | 0% |
| LinkedIn (paid) | Lead gen, ABM | Sponsored content, InMail | Continuous | 30% |
| Google Search | High-intent capture | Search ads | Continuous | 25% |
| Content/SEO | Long-term awareness | Blog posts, guides | 1-2 pieces/week | 15% |
| Webinar/Event | Engagement, pipeline | Live sessions | 1-2 per campaign | 10% |
| Retargeting | Conversion | Display, social retargeting | Continuous | 10% |

### Phase 3: Asset Production (Week 2-3)

Create an asset checklist:

| Asset | Owner | Due Date | Status |
|-------|-------|----------|--------|
| Landing page | [name] | [date] | Not started |
| Email sequence (5 emails) | [name] | [date] | Not started |
| LinkedIn posts (10) | [name] | [date] | Not started |
| Ad creative (3 variants) | [name] | [date] | Not started |
| Case study | [name] | [date] | Not started |

### Phase 4: Execution (Week 3+)

Week-by-week execution calendar:

| Week | Channel Activity | Content Published | Milestones |
|------|-----------------|-------------------|------------|
| 1 | Launch ads, send Email 1 | Blog post, 3 LinkedIn posts | Campaign live |
| 2 | Optimize ads, Email 2-3 | Case study, 3 LinkedIn posts | First performance review |
| 3 | Retargeting live, Email 4 | Webinar, 3 LinkedIn posts | Mid-campaign review |
| 4 | Final push, Email 5 | Recap post | Campaign wrap, report |

### Phase 5: Measurement

**Tracking Setup (before launch):**
- UTM parameters for every link.
- Conversion tracking on landing pages.
- CRM attribution configured.

**Reporting Cadence:**
- Daily: ad spend and basic metrics.
- Weekly: full funnel review (impressions -> clicks -> leads -> pipeline).
- End of campaign: full performance report with ROI.

**Key Metrics:**

| Metric | Definition | Target |
|--------|-----------|--------|
| Impressions | Total reach | [number] |
| CTR | Clicks / impressions | >1% (ads), >2% (email) |
| CPL | Cost per lead | <$[amount] |
| MQLs generated | Leads meeting qualification criteria | [number] |
| Pipeline influenced | Revenue in pipeline touched by campaign | $[amount] |
| ROI | (Revenue - Cost) / Cost | >[X]% |

## Output Format

Save the campaign brief to `outputs/campaigns/`:

```markdown
# Campaign Brief: [Campaign Name]

## Executive Summary
[1 paragraph: goal, audience, channels, timeline, expected outcome]

## Goal and Success Metrics
## Audience Definition
## Message Architecture
## Channel Plan
## Asset Checklist
## Execution Calendar
## Budget Breakdown
## Measurement Plan
```

## Do NOT
- Launch without conversion tracking in place.
- Spray the same message across every channel. Adapt per platform.
- Skip the audience definition. "Everyone" is not a target.
- Plan creative without a clear CTA for each piece.
- Report vanity metrics (impressions) without conversion metrics (leads, pipeline).
- Forget to plan the post-campaign follow-up for leads generated.