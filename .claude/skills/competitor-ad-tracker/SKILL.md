---
name: competitor-ad-tracker
description: Track competitor advertising activity systematically. Pull from Meta Ad Library, Google Ads Transparency Center, LinkedIn Ad Library, TikTok Ad Library. Output: weekly digest of what competitors are running and what changed. Distinct from competitor-researcher (general competitive intel).
triggers:
  - competitor ads
  - ad library
  - ad spy
  - what are competitors running
  - meta ad library
  - google ads transparency
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Competitor Ad Tracker

Build an ongoing intelligence loop on competitor paid advertising. Public ad libraries make this possible without paying for tools — but it's labor-intensive without a workflow.

## Gather context

Ask if not provided:

1. **Which competitors?** — list of 3-10 competitors to track. Direct + 2-3 indirect.
2. **Which platforms?** — Meta (Facebook + Instagram), Google, LinkedIn, TikTok. Match competitor presence.
3. **Cadence** — weekly is standard; monthly for low-velocity markets.
4. **Existing tooling?** — third-party tools (SocialPeta, BigSpy, Adbeat) save time but cost money. Manual via libraries works.

## Sources by platform

### Meta Ad Library (Facebook + Instagram)
URL: `https://www.facebook.com/ads/library`
- Search by Page name. Returns all ads currently running.
- Shows: ad creative, when it started running, platforms, runtime.
- Doesn't show: spend, audience targeting, performance.
- Limitation: only "active" ads, no historical archive (except for political/issue ads).

### Google Ads Transparency Center
URL: `https://adstransparency.google.com`
- Search by advertiser name (often the legal entity, not the brand).
- Shows: text ads, image ads, video ads, regions, format.
- Doesn't show: keywords, spend.

### LinkedIn Ad Library
URL: `https://www.linkedin.com/ad-library`
- Search by company. Shows currently running ads.
- Shows: ad creative, sponsored content vs. message ads, runtime.
- Doesn't show: spend or targeting.

### TikTok Ad Library
URL: `https://library.tiktok.com`
- Available in select regions (mainly EU due to DSA requirements).
- Shows: ad creative, advertiser, runtime.

### LinkedIn organic posts as ads proxy
Sponsored content is amplified organic. Watching what a competitor's company page posts (even non-sponsored) signals what they'll likely amplify.

## Workflow

### Weekly cadence

1. **Monday — pull active ads** for each tracked competitor across all platforms (15-30 min).
2. **Tag the changes** — what's new since last week, what's still running, what stopped (10-15 min).
3. **Categorize by theme** — what message, audience, offer is each ad pushing? (15-30 min).
4. **Annotate insights** — what does this tell us about their strategy? (15-30 min).
5. **Distribute** — share with marketing, sales, leadership in their preferred channel (5-10 min).

Total: ~90 min weekly for 5 competitors. More tracked competitors scales.

### Tagging schema

For each ad, capture:
- Platform.
- Competitor.
- First seen / last seen.
- Headline + brief description of creative.
- Inferred audience (what the targeting seems to be).
- Theme: pricing, feature, social proof, comparison, retargeting, etc.
- Strategic signal: launching feature X, doubling-down on segment Y, defending against company Z.

## Output format

Save weekly digest to `outputs/competitor-ads/<week>.md`:

```
## Competitor ad digest — week of <date>

## Headline observations
- <competitor X> launched a new ad campaign around <theme>
- <competitor Y> stopped running their <theme> ads after 3 months
- <competitor Z> shifted budget from <platform> to <platform>

## By competitor

### <Competitor 1>
- Active ads: <count> across <platforms>
- New this week: <description>
- Still running: <description>
- Stopped: <description>
- Inferred strategy: <interpretation>

### <Competitor 2>
[same structure]

## Cross-cutting themes
- <theme>: now appearing in <N> competitors
- <theme>: declining

## Recommendations for our paid program
- <observation>: counter / match / ignore?
- <gap they're not exploiting>: opportunity for us?
```

Maintain a long-form record at `outputs/competitor-ads/archive/<competitor-slug>.md` — running history per competitor for pattern-spotting over months.

## Common mistakes

- Tracking too many competitors. 3-5 deeply > 15 shallowly.
- Reacting to every change. Most ad changes are tactical noise; only patterns matter.
- Confusing presence with success. A competitor running ads doesn't mean they're working — many ads run for months at low ROAS.
- Not sharing with sales. Sales reps benefit from knowing what competitors are pitching.

## Cross-references

For broader competitive research (product, positioning, customer signals), use `competitor-researcher`. For battlecards built from competitive intel, use `sales-battlecard-builder` and `competitive-battlecard-builder`. For the ad-creative side of our own program, use `ad-copy-writer`. For platform-specific audits of our ads, use `google-ads-auditor`, `meta-ads-auditor`.
