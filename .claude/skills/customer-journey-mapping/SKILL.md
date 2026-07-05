---
name: customer-journey-mapping
description: Map the customer lifecycle — awareness through renewal — with stage definitions, entry/exit criteria, signals to monitor, and owner per stage. The foundation document for designing CS playbooks, support tiers, and lifecycle marketing. Use when user mentions customer journey, journey map, lifecycle stages, or stages of adoption.
triggers:
  - customer journey
  - journey map
  - lifecycle map
  - lifecycle stages
  - cs playbook foundation
  - stages of adoption
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Customer Journey Mapping

Build a customer journey map covering awareness through renewal. The map is a working document that defines stages, signals, and ownership. CS playbooks, lifecycle marketing emails, support routing, and feature priorities all reference it.

## Gather context

Ask if not provided:

1. **Product type** — self-serve SaaS, sales-led SaaS, enterprise platform, marketplace, services.
2. **Sales motion** — PLG (product-led), sales-led, hybrid.
3. **Touchpoints** — what channels exist today (website, in-app, email, support, calls, community).
4. **Roles** — who's involved (marketing, sales, CS, support, product, exec sponsor for enterprise).

## Default lifecycle stages

For most B2B SaaS, the lifecycle has six stages. For self-serve/PLG, collapse stages 2-3.

| Stage | What happens | Owner | Key signal |
|---|---|---|---|
| Awareness | Customer encounters the brand | Marketing | First touch (web visit, social, referral) |
| Evaluation | Customer compares options | Marketing/Sales | Pricing/demo page visit, content engagement |
| Acquisition | Customer commits | Sales (or self-serve flow) | Closed-won, trial signup, paid conversion |
| Onboarding | Customer reaches first value | CS / Support | First key action completed |
| Adoption | Customer integrates the product into work | CS | Steady-state usage pattern |
| Expansion / Renewal | Customer grows or renews (or churns) | CS / AM | Renewal date hit; expansion deal opened |

Some products add: Advocacy (post-renewal customer recommends, refers, gives testimonial). Worth a stage if the program is mature.

## For each stage, document

- **Definition** — one sentence.
- **Entry criteria** — what specifically gets a customer into this stage (no ambiguity).
- **Exit criteria** — what gets them to the next stage (or out — churn).
- **Owner** — single named role (not "marketing and CS").
- **Signals to monitor** — leading indicators that a customer is healthy or stuck in this stage.
- **Plays** — what the owner does (touchpoints, communications, interventions).
- **Time-in-stage benchmark** — typical duration; flag accounts that exceed it.

## Stage detail templates

### Awareness
- Definition: Customer is aware of the brand.
- Signals: web visit, content view, social engagement.
- Plays: SEO content, paid ads, brand campaigns.
- Time benchmark: variable; not actionable.

### Evaluation
- Definition: Customer is actively comparing options.
- Signals: pricing page visit, demo request, multiple product page visits, competitor comparison.
- Plays: nurture sequence, sales outreach, free tool / lead magnet.
- Time benchmark: 7-30 days for SMB; 30-90 days for enterprise.

### Onboarding
- Definition: Customer has paid/signed up and is setting up.
- Signals: completing setup steps, first key action.
- Plays: onboarding email sequence, in-app tutorial, kickoff call (enterprise).
- Time benchmark: 7-14 days SMB; 30-60 days enterprise.
- Critical metric: Time-to-First-Value (TtFV).

### Adoption
- Definition: Customer is actively using the product as part of their work.
- Signals: weekly active usage, breadth of features used, multiple users per account.
- Plays: usage health monitoring, feature education, expansion suggestion.
- Time benchmark: should be reached by day 30-60.

### Expansion / Renewal
- Definition: Customer is up for renewal or could expand (more seats, higher tier, additional product).
- Signals: usage growth, new use cases, exec engagement.
- Plays: renewal-orchestration (90/60/30/0-day), expansion conversation, exec QBR.

## Output format

Save to `outputs/journey-map/<date>-journey-map.md` with:
- Visual diagram (markdown table or mermaid flow).
- Per-stage detail (definition, entry/exit, owner, signals, plays, time benchmark).
- Cross-stage handoffs documented (marketing-to-sales, sales-to-CS).
- Metrics dashboard pointing to stage health.

If onboarding-specific, also produce `outputs/journey-map/onboarding-playbook.md` with the day-by-day sequence.

## Common mistakes

- Designing the journey from the company's perspective ("our funnel"), not the customer's.
- Skipping exit criteria. Customers get stuck in stages indefinitely without it.
- Multiple owners per stage — accountability dies.
- Not measuring time-in-stage. The biggest CS lever is identifying customers stalled in onboarding.
- Treating the map as static. Update quarterly as the product and market change.

## Cross-references

For the renewal motion specifically, see (when added) `renewal-orchestration`. For onboarding design specifically, see `onboarding-designer`. For per-account scoring against this map, see (when added) `value-realization-scorer` and existing `health-score-builder`. For lifecycle email automation, see `email-sequence-builder` and `marketing-funnel-mapper`.
