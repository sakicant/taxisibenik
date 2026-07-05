---
name: aso-audit
description: Audit App Store and Google Play listings for ranking, conversion, and visibility. Use when a user shares an app store URL, asks to optimize an app listing, or compares their app to competitors.
triggers:
  - aso audit
  - app store optimization
  - optimize app listing
  - improve app downloads
  - app store ranking
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# ASO Audit

Audit App Store and Google Play listings against ASO best practices. Score metadata, visuals, and ratings, then produce a prioritized fix list.

## Gather Context First

1. Read `context/` for the product's positioning and target audience
2. Get the listing URL — App Store, Google Play, or both
3. Identify the product category and 2-3 direct competitor listings
4. Note current ranking and download volume if known

## Audit Framework

Score each layer 1-5, then aggregate. A listing scores well only when every layer scores 4+.

### Layer 1 — Discoverability (keywords)

| Element | App Store | Google Play |
|---------|-----------|-------------|
| App name | 30 chars, indexed | 30 chars, indexed |
| Subtitle / short description | 30 chars, indexed | 80 chars, indexed |
| Keyword field | 100 chars, hidden | N/A (uses long description) |
| Long description | Not indexed | 4000 chars, indexed |

**Audit:** Does the name + subtitle contain the top-2 search terms the target user types? Are keywords repeated unnecessarily (wastes characters)? Is the long description keyword-dense without sounding spammy?

### Layer 2 — Conversion (above the fold)

The first impression is icon + name + subtitle + first 2 screenshots.

- [ ] Icon is recognizable at 1x (no text inside the icon)
- [ ] Subtitle states the outcome, not the feature ("Run faster" beats "GPS-powered tracker")
- [ ] First screenshot shows the core value prop, not the home screen
- [ ] Screenshots use captions that complete the sentence "This app helps you..."
- [ ] No competing CTAs in the visual block (single primary message)

### Layer 3 — Trust (ratings + reviews)

| Signal | Healthy | Warning |
|--------|---------|---------|
| Star rating | 4.5+ | Below 4.2 |
| Review count | 100+ for niche, 10k+ for broad | Under 50 |
| Review recency | Last 30 days has activity | Stale 90+ days |
| Developer responses | Visible on negative reviews | Silent |

### Layer 4 — Visual completeness

- [ ] Preview video present (App Store: 30s, Google Play: 30s)
- [ ] Screenshots cover all key flows (5-10 screens, not 1-2)
- [ ] Screenshots adapted for each device size (phone, tablet)
- [ ] Localized for top-3 markets if international audience
- [ ] Promotional text refreshed within last 90 days (App Store)

### Layer 5 — Competitive positioning

Pull the same data for 2-3 direct competitors. Compare:

- Subtitle phrasing — what outcomes do they claim?
- Screenshot order — what value prop do they lead with?
- Keyword overlap — where do they rank that you don't?
- Rating delta — is the gap a quality issue or a volume issue?

## Output Format

Save to `outputs/aso-audit-[app-slug].md`:

### Listing Score
| Layer | Score (1-5) | Notes |
|-------|-------------|-------|
| Discoverability | | |
| Conversion (above fold) | | |
| Trust (ratings/reviews) | | |
| Visual completeness | | |
| Competitive positioning | | |
| **Overall** | | |

### Quick Wins
Changes shippable in under a day with no creative production:
- [Change] — Layer: [Name] — Expected impact: [High/Medium/Low]

### Larger Initiatives
Changes that require design, video, or localization work, with rough effort estimate.

### Keyword Opportunities
| Keyword | Search volume | Current rank | Competitor leader | Gap |
|---------|---------------|--------------|-------------------|-----|

## Do NOT

- Score a listing without comparing to at least 2 competitors — context matters
- Recommend keyword stuffing — Apple and Google both penalize it
- Suggest fake reviews or rating manipulation — both stores ban for it
- Treat the App Store and Google Play as identical — keyword fields, screenshot rules, and ranking signals differ
- Ignore localization if the target market is non-English