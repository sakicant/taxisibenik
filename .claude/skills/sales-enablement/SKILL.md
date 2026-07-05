---
name: sales-enablement
description: Coordinate the creation of a complete sales enablement package — pitch decks, one-pagers, battlecards, objection docs, demo scripts, playbooks. Meta-skill that orchestrates existing skills (sales-battlecard-builder, objection-handler, sales-outreach-writer, presentation-builder). Use when user mentions sales enablement, sales playbook, sales materials, or "set up sales enablement."
triggers:
  - sales enablement
  - sales playbook
  - sales materials
  - rep collateral
  - sales kit
  - enablement package
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Sales Enablement

Plan and produce a complete sales enablement package. This skill coordinates several existing skills to deliver a coherent kit, not individual artifacts.

## Gather context

Ask if not provided:

1. **Sales motion** — SMB / mid-market / enterprise? Self-serve, sales-led, hybrid?
2. **Stage of go-to-market** — pre-launch (no reps yet), early sales team, scaling, mature?
3. **Existing collateral** — what already exists? Read it first; don't duplicate.
4. **Top three current pain points** — losing on price? Demo isn't landing? Reps re-create everything from scratch?
5. **Audience for the kit** — AEs, SDRs, partner reps, channel?

## Core principles

- **Sales uses what sales trusts.** Involve top reps in creation. If reps rewrite collateral before sending, you wrote the wrong thing.
- **Situation-specific over generic.** A CTO deck and a VP-Sales deck should differ. Build templates, not one-size-fits-all.
- **Scannable over comprehensive.** Reps need answers in 3 seconds, not 30. Bold, short bullets, visual hierarchy.
- **Single source of truth.** Collateral lives in one place; reps know where to find it.

## The standard kit

A complete sales enablement package contains:

| Asset | Skill that produces it | Audience |
|---|---|---|
| Master pitch deck (template + variants per persona) | `presentation-builder`, `pptx-handler` | All deals |
| One-pager / leave-behind | Generic content skill or `copywriting` | Every meeting |
| Objection handling doc | `objection-handler` | All deals |
| Battlecards (per competitor) | `sales-battlecard-builder`, `competitive-battlecard-builder` | Competitive deals |
| Demo script (per persona / use case) | (custom; build from product knowledge) | Demo phase |
| Discovery call guide | (custom; build from sales process) | First call |
| Email templates (cold + follow-up + nurture) | `cold-email-writer`, `sales-outreach-writer` | Outbound + nurture |
| Pricing one-pager | `pricing-strategist`, `pricing-guidelines` | Pricing conversations |
| Case studies | `case-study-writer` | Proof in deals |
| ROI calculator | `free-tool-strategy` (sometimes) | Mid-funnel |
| Security questionnaire master | `sales-engineer` | Enterprise / regulated |
| Mutual Action Plan template | `enterprise-sales` | Enterprise deals |

Don't build all of these at once. Prioritize by which gap is bleeding the most pipeline.

## Workflow

### Step 1: Audit existing collateral
List what exists. Score each on: still accurate? Used by reps? Tested in deals? Findable?

### Step 2: Prioritize gaps
Which 2-3 missing or broken assets would close the most deals over the next quarter?

### Step 3: Build, with rep input
For each priority asset:
- Draft the asset (using the appropriate skill).
- Test with 2-3 top reps. Ask: would you actually use this? What would you change?
- Iterate.
- Ship.

### Step 4: Distribute
- Single repository (Notion, Drive, Highspot, Seismic — whatever the company uses).
- Indexed by deal stage and persona.
- Searchable.
- Version-controlled — reps should know they're seeing the latest.

### Step 5: Measure usage
Track which assets get used (analytics on shared links, asking reps quarterly). Kill what no one uses; double down on what does.

### Step 6: Refresh on a cadence
Sales enablement decays fast. Pricing changes, competitors evolve, products ship. Quarterly refresh of all assets is the minimum.

## Output format

Save the enablement plan to `outputs/sales-enablement/<date>-plan.md`:

```
## Sales enablement plan — <date>

## Audit
- Existing assets: <list with status>
- Gaps: <list>

## Priorities (this quarter)
1. <asset> — owner — deadline — coordinated skill
2. ...

## Repository structure
- <how the kit will be organized>

## Refresh cadence
- <what gets reviewed when>

## Success metrics
- <how we'll know if reps are using and winning with this>
```

The actual assets get produced by the linked skills and saved per their conventions.

## Common mistakes

- Building in marketing without rep input. Reps reject what they didn't help shape.
- Generic decks. Different personas need different decks; one-deck-fits-all loses every meeting.
- No refresh cadence. Materials decay.
- Too many assets at once. Fewer, better, used.
- No measurement. Can't tell what's working without it.

## Cross-references

For each asset type, use the linked skill above. For pipeline-level review of where deals stall (informs which collateral to build), use `sales-pipeline`. For coaching reps on collateral usage, use `sales-coaching`. For RevOps that defines who hands off what, use `revops-analyst`.
