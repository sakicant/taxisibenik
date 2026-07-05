---
name: analytics-tracker
description: Design event tracking plans, configure analytics, and build measurement frameworks. Use when setting up tracking for new features, campaigns, or products.
triggers:
  - tracking plan
  - analytics setup
  - event tracking
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Analytics Tracker

Design measurement frameworks that answer specific business questions. Every tracked event must tie back to a decision someone will make with the data.

## The Measurement Framework

Start with questions, not events. Work backwards from decisions to data:

```
Business question → Metric that answers it → Events that compute it → Implementation
```

**Example:**
- Question: "Is the new onboarding flow improving activation?"
- Metric: Activation rate (% of signups who complete setup within 7 days)
- Events: `signup_completed`, `setup_step_completed`, `first_value_moment`
- Implementation: Fire events at specific UI interaction points

## Phase 1 — Question Inventory

List every question stakeholders want answered. Group by category:

| Category | Question | Decision It Informs | Priority |
|----------|---------|-------------------|----------|
| Acquisition | Where do our best users come from? | Marketing spend allocation | P1 |
| Activation | Do new users reach the "aha" moment? | Onboarding redesign | P1 |
| Engagement | Which features drive retention? | Product roadmap | P1 |
| Revenue | What predicts upgrade to paid? | Sales targeting | P2 |
| Retention | When and why do users churn? | Intervention triggers | P1 |

## Phase 2 — Funnel Mapping

Map the user journey from first touch to core value:

```
[Traffic source] → [Landing] → [Signup] → [Onboarding step 1] → ... → [First value moment] → [Retention loop]
```

At each stage, identify:
- **Entry event** — What action marks entering this stage?
- **Exit event** — What action marks completing this stage?
- **Drop-off indicator** — What signals the user abandoned?
- **Time expectation** — How long should this stage take?

## Phase 3 — Event Taxonomy

Use a consistent naming convention. The recommended pattern is `object_action`:

### Naming Rules
- Use `snake_case` for all event names and properties
- Pattern: `[object]_[past_tense_action]` (e.g., `form_submitted`, `page_viewed`, `feature_activated`)
- Group by object, not by page or feature release
- Never use generic names like "click" or "event" without context

### Event Categories
| Category | Events | Purpose |
|----------|--------|---------|
| **Lifecycle** | `session_started`, `signup_completed`, `subscription_started` | Funnel progression |
| **Engagement** | `page_viewed`, `feature_used`, `search_performed` | Usage patterns |
| **Conversion** | `cta_clicked`, `checkout_started`, `payment_completed` | Revenue funnel |
| **Content** | `content_viewed`, `content_shared`, `content_downloaded` | Content performance |
| **Error** | `error_occurred`, `form_validation_failed` | Quality and friction |

### Property Standards
Every event should include these base properties:
- `timestamp` — When it happened
- `user_id` — Who did it (anonymized if pre-auth)
- `session_id` — Which session
- `page_path` — Where it happened
- `platform` — Web, iOS, Android

Plus event-specific properties:
| Event | Required Properties | Optional Properties |
|-------|-------------------|-------------------|
| `page_viewed` | page_title, page_path, referrer | utm_source, utm_medium, utm_campaign |
| `cta_clicked` | cta_text, cta_location, destination | experiment_variant |
| `feature_used` | feature_name, action | duration, input_count |
| `error_occurred` | error_type, error_message, page_path | stack_trace, user_action |

## Phase 4 — Metrics Definition

Define each metric precisely to avoid ambiguity:

| Metric | Formula | Source Events | Timeframe | Segment By |
|--------|---------|--------------|-----------|-----------|
| Activation rate | (users who completed setup / users who signed up) x 100 | `signup_completed`, `setup_completed` | 7-day window | Source, plan |
| Feature adoption | (users who used feature / active users) x 100 | `feature_used`, `session_started` | 30-day rolling | Role, plan |
| Conversion rate | (users who purchased / users who started checkout) x 100 | `checkout_started`, `payment_completed` | Per session | Source, device |

### Metric Types
- **KPIs** — The 3-5 numbers that define success. Review weekly.
- **Leading indicators** — Predict KPI movement. Track daily.
- **Guardrail metrics** — Must not degrade when making changes. Monitor on every release.
- **Diagnostic metrics** — Explain why KPIs moved. Investigate on demand.

## Phase 5 — Implementation Spec

For each event, specify exactly where it fires:

| Event | Trigger | Location | Tech Notes |
|-------|---------|----------|-----------|
| `signup_completed` | Success callback from auth API | `/signup` page component | Fire after server confirmation, not on button click |
| `cta_clicked` | Click handler on CTA button | Any page with primary CTA | Include data attributes for cta_text and cta_location |

## Output Format

Save to `outputs/tracking-plan-[feature-slug].md` with:

1. Question inventory table
2. Funnel map (text-based diagram)
3. Full event taxonomy with properties
4. Metrics definitions table
5. Implementation spec for engineering
6. QA checklist: how to verify each event fires correctly

## Do NOT
- Track everything — every event has an implementation cost and a maintenance cost. Track only what informs a decision
- Use vague event names — `click` is useless. `cta_clicked` with properties is useful
- Mix naming conventions — pick `snake_case` and use it everywhere
- Skip the QA step — unverified tracking is worse than no tracking because it creates false confidence
- Track personally identifiable information without explicit consent and a data retention policy
- Define metrics ambiguously — "active users" means nothing without a precise definition of "active"