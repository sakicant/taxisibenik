---
name: launch-metrics-planner
description: Define the measurement plan for a product launch including UTM conventions, KPIs, dashboards, and retrospective criteria. Use when planning a launch, setting up tracking, or preparing a launch retrospective.
triggers:
  - launch metrics
  - UTM setup
  - launch KPIs
  - launch measurement
  - launch retrospective
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Launch Metrics Planner

Every launch should be measurable. Define what success looks like before the launch, not after.

## Phase 1 — Define Success

| Question | Answer |
|----------|--------|
| What is being launched? | [name and description] |
| Launch date | [date] |
| Primary goal | [awareness / signups / revenue / activation / engagement] |
| Success metric | [specific number within specific timeframe] |
| Minimum viable outcome | [the floor — below this, the launch underperformed] |

### KPIs by Launch Phase

| Phase | Timeframe | KPIs | Target |
|-------|-----------|------|--------|
| Pre-launch | T-14 to T-0 | Waitlist signups, social impressions, email open rate | [targets] |
| Launch day | T+0 to T+1 | Page views, signups, activation rate, press mentions | [targets] |
| Week 1 | T+1 to T+7 | Sustained traffic, conversion rate, retention of new users | [targets] |
| Month 1 | T+7 to T+30 | Retention, expansion, word-of-mouth referrals | [targets] |

## Phase 2 — UTM Convention

Standardize UTM parameters so attribution is clean:

### UTM Structure
```
utm_source    = [platform] (linkedin, twitter, hackernews, email, discord, partner-name)
utm_medium    = [type] (social, email, referral, paid, organic)
utm_campaign  = [launch-name]-[date] (beta-launch-2026-04, feature-x-launch)
utm_content   = [variant] (post-a, post-b, thread-hook-1, email-subject-v2)
```

### Pre-Built Links
Create tagged links for every distribution channel before launch day:

| Channel | UTM Source | UTM Medium | UTM Campaign | UTM Content | Full URL |
|---------|-----------|-----------|-------------|------------|---------|
| LinkedIn personal | linkedin | social | [campaign] | [variant] | [url] |
| X/Twitter | twitter | social | [campaign] | [variant] | [url] |
| Email blast | email | email | [campaign] | [variant] | [url] |
| Discord | discord | community | [campaign] | [variant] | [url] |
| HN post | hackernews | social | [campaign] | [variant] | [url] |
| Partner | [partner] | referral | [campaign] | [variant] | [url] |

## Phase 3 — Dashboard Setup

Define what to monitor during and after launch:

### Real-Time (Launch Day)
- Page views and unique visitors (by UTM source)
- Signup/conversion events
- Error rates and performance metrics
- Social mentions and engagement

### Daily (Week 1)
- New users by channel
- Activation rate (new users who complete key action)
- Funnel drop-off at each step
- Support tickets and feedback volume

### Weekly (Month 1)
- Retention curve for launch cohort
- Channel quality (signups that activate by source)
- Revenue impact (if applicable)
- Net Promoter Score or satisfaction signal

## Phase 4 — Retrospective Framework

Run the retrospective at T+7 and T+30:

### Data Review
| Metric | Target | Actual | Delta | Verdict |
|--------|--------|--------|-------|---------|
| [metric] | [target] | [actual] | [+/- %] | Hit/Miss |

### Channel Performance
| Channel | Traffic | Signups | Activation | Cost | Quality Rank |
|---------|---------|---------|------------|------|-------------|
| [channel] | [n] | [n] | [%] | [$] | [1-5] |

### Qualitative Review
- What feedback did users give?
- What surprised us?
- What would we do differently?
- What should we double down on?

## Output

Write to `outputs/launch-metrics-[campaign-name].md`:

1. **Success criteria** — KPIs with targets by phase
2. **UTM link table** — all tagged links ready to use
3. **Dashboard spec** — what to monitor at each cadence
4. **Retrospective template** — pre-built tables for T+7 and T+30 review

## Do NOT
- Launch without UTM links prepared — retroactive attribution is unreliable
- Track vanity metrics only — page views without conversion data tell you nothing
- Skip the retrospective — the learning is as valuable as the launch itself
- Set targets after seeing the data — that is not a target, it is a rationalization