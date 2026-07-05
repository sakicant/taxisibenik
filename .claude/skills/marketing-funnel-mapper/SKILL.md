---
name: marketing-funnel-mapper
description: Map and analyze the full marketing funnel from awareness to conversion. Use when diagnosing conversion issues or planning funnel improvements.
triggers:
  - map funnel
  - funnel analysis
  - conversion path
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Marketing Funnel Mapper

Trace the complete customer journey from first discovery to conversion and beyond. Identify every friction point, quantify drop-off, and prioritize fixes by impact-to-effort ratio.

## Gather Context First

Check `context/` for existing product and analytics data. Ask for what is missing:

1. **Product type** — SaaS, e-commerce, marketplace, content site?
2. **Primary conversion action** — Signup, purchase, demo request, download?
3. **Traffic sources** — Where do visitors come from?
4. **Current metrics** — Traffic, conversion rates, known drop-off points
5. **Analytics tool** — GA4, Mixpanel, Amplitude, Hotjar, or none?

## The AICR Funnel Framework

### Stage 1: Awareness (Top of Funnel)
**Question:** How do people first learn this exists?

Map:
- **Channels** — Which drive the most traffic? Organic, paid, social, referrals?
- **First page** — Most common entry page
- **First impression** — Can a visitor understand what this is within 5 seconds?
- **Volume** — Monthly visitors by channel

**Common friction:** Wrong keywords, high bounce on landing pages, paid targeting too broad, content not reaching the right audience.

**Metrics:** Visitors by source, cost per visitor, bounce rate

### Stage 2: Interest (Middle of Funnel)
**Question:** What makes someone stay and explore?

Map:
- **Second page** — Where do visitors go after the entry page?
- **Engagement** — Time on site, pages per session, scroll depth
- **Content consumption** — Docs, demos, pricing page visits
- **Early objections** — Is pricing visible? Are concerns addressed?

**Common friction:** No clear next step, pricing hidden, slow load times (each second adds ~7% bounce), broken mobile experience.

**Metrics:** Pages per session, time on site, pricing page visits

### Stage 3: Consideration (Bottom of Funnel)
**Question:** What information does someone need before deciding?

Map:
- **Decision content** — Comparison pages, case studies, testimonials, FAQs
- **Social proof placement** — Near decision points?
- **Competitive evaluation** — Can prospects compare you to alternatives?
- **Trust signals** — Security, guarantees, reviews

**Common friction:** No case studies from similar customers, FAQ misses real objections, no way to try before buying.

**Metrics:** Case study views, FAQ engagement, return visitor rate

### Stage 4: Conversion and Retention
**Question:** How easy is it to complete the action, and what happens next?

Map:
- **Signup/purchase flow** — Steps, required fields, payment friction
- **Post-conversion** — Confirmation, welcome email, onboarding
- **Activation** — Time to first value moment
- **Retention** — What brings them back?

**Common friction:** Too many form fields, email verification before access, credit card for free trial, empty state after signup, no follow-up sequence.

**Metrics:** Signup completion rate, activation rate, Day 1/7/30 retention

## Friction Logging

For each friction point:

| Friction Point | Stage | Severity (1-5) | Evidence | Fix |
|----------------|-------|-----------------|----------|-----|

**Severity scale:** 1=minor annoyance, 3=significant barrier, 5=complete wall where nearly all users stop.

## Output Format

Save to `outputs/funnel-analysis.md`:

### Funnel Visualization
Text-based diagram showing visitors at each stage with drop-off percentages.

### Friction Log
Full table of all friction points with severity, evidence, and fixes.

### Prioritized Recommendations

| Priority | Fix | Stage | Impact | Effort | Expected Lift |
|----------|-----|-------|--------|--------|--------------|

### Quick Wins (implement this week)
Top 3 low-effort, high-impact changes.

### Strategic Fixes (plan for next quarter)
Larger changes requiring design or engineering work.

### Measurement Plan
What to track weekly to validate fixes are working.

## Do NOT
- Map the funnel without data or evidence
- Assume every visitor follows a linear path
- Focus only on the bottom of the funnel — top problems starve the pipeline
- Recommend fixing everything at once — prioritize by impact-to-effort
- Ignore retention — acquiring customers who churn is worse than not acquiring them