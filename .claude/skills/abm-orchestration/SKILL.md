---
name: abm-orchestration
description: Design and run an Account-Based Marketing program — define the target list, build the multi-channel touch plan, score intent signals, and orchestrate sales-marketing alignment for named accounts. Tiered for 1:1 (top accounts), 1:few (clusters), 1:many (broad ABM) motions.
triggers:
  - account-based marketing
  - abm program
  - named accounts
  - target account list
  - 1:1 abm
  - 1:few abm
  - account orchestration
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# ABM Orchestration

Stand up an ABM program where marketing and sales work the same named accounts together. Three tiers: 1:1 for the top 10-30 accounts, 1:few for clusters of 30-200, 1:many for the broader segment. Pick the tier per account based on deal size potential.

## Gather context

Ask if not provided:

1. **Sales motion** — enterprise / mid-market / hybrid. ABM works best with $50k+ ACV.
2. **Current state** — outbound today? What channels (email, LinkedIn, calls, ads)?
3. **CRM and tools** — what's tracking accounts? Any intent data sources (G2, Clearbit, 6sense, Common Room)?
4. **Resources** — SDR + AE + marketer per account, or one team handling all?
5. **Goal** — pipeline coverage, expansion, specific named-account land?

## Step 1: Define target accounts

Two approaches:

**Top-down**: ICP filters (industry, size, tech stack, geo) -> filter database -> rank by fit + intent -> top N.

**Bottom-up**: sales picks named accounts they want -> verify ICP fit -> add intent layer.

Mix both for a realistic list. Cap initial program at 50-100 accounts so you can actually do depth.

For each account, capture:
- Account name + URL.
- Tier (1:1 / 1:few / 1:many).
- Primary contact role(s) and named individuals where known.
- Primary champion + economic buyer + technical evaluator.
- Use case hypothesis (why they'd buy).
- Current intent signal (none / lukewarm / warm / hot).

## Step 2: Multi-channel touch plan

Per tier, design the touch sequence:

### 1:1 tier (top accounts)
- Custom landing page per account.
- Personalized direct mail or gift.
- Multi-thread outreach (5+ contacts in the buying committee).
- 1:1 LinkedIn engagement from CEO / VP Sales / AE.
- Custom event invite (small dinner, exec roundtable).
- Cadence: 2-3 touches per week, 12-week sequence.

### 1:few tier (clusters)
- Cluster-themed content (vertical-specific case study).
- Personalized but template-based outbound.
- Targeted ads to logo-list audience (LinkedIn, Meta with company-list).
- Webinar invite tailored to the cluster pain.
- Cadence: 1-2 touches per week, 8-week sequence.

### 1:many tier (broad ABM)
- Industry-specific content marketing.
- Ads with intent layer (target accounts who match firmographic + showed signal).
- Email sequences with persona variation.
- Cadence: weekly, ongoing.

## Step 3: Intent signal scoring

Combine signals to decide which accounts to push harder:

| Signal | Weight | Source |
|---|---|---|
| Target ICP fit | base | CRM filters |
| Visited high-intent page (pricing, demo) | high | Web analytics |
| Engaged with content (downloaded, watched) | medium | Marketing automation |
| Job change in target role | high | LinkedIn / Clearbit |
| Funding event / hiring spree | medium | Crunchbase / job postings |
| 3rd-party intent (G2, 6sense, etc.) | medium-high | Vendor data |
| Prior contact with company | high | CRM history |

Score weekly. Move accounts up tiers when signals stack. Trigger sales tasks at score thresholds.

## Step 4: Sales-marketing alignment

ABM dies when sales and marketing don't work in sync. Daily/weekly rituals:

- **Daily standup** for the ABM SDR/AE pod (5 min): hot accounts, blockers.
- **Weekly review** (30 min): account list, signal changes, touches planned, content needs.
- **Monthly QBR** with marketing leadership: pipeline contribution, conversion rates per tier.
- **Shared dashboard**: every account's status visible to both teams.

## Step 5: Measurement

Track per tier:
- Pipeline created (opportunities x stage value).
- Multi-thread coverage (% of accounts with 3+ contacts engaged).
- Engagement breadth (% accounts with content engagement, ad impressions, outbound touches).
- Conversion rate (% accounts -> opportunity, opportunity -> closed-won).
- Time to first meeting / time to opportunity.

## Output format

Save the program design to `outputs/abm/<date>-program.md`:
- Account list with tier and intent score.
- Touch plan per tier (sequences and cadences).
- Intent scoring rubric.
- Alignment rituals + owners.
- Measurement dashboard structure.
- 90-day rollout plan.

For each 1:1 account: `outputs/abm/accounts/<account-slug>.md` with the personalized plan, contact map, and touch log.

## Common mistakes

- 500 accounts in tier 1:1. You can't do 500 accounts well; cap at 30.
- Marketing builds the list and hands it off. ABM requires shared ownership.
- No intent layer — just blasting through ICP without prioritizing the warm ones.
- Ads-only ABM. Multi-channel is the unlock.
- Skipping the 1:1 outbound layer. Ads + email isn't ABM, it's segmented marketing.

## Cross-references

For the cold outreach inside ABM sequences, use `cold-email-writer` and `sales-outreach-writer`. For competitor positioning in account playbooks, use `competitor-comparison-writer` and `competitive-battlecard-builder`. For the broader pipeline view, use (when added) `sales-pipeline`. For intent signal scoring specifically, use (when added) `intent-signal-scoring`. For enterprise multi-stakeholder selling, use (when added) `enterprise-sales`.
