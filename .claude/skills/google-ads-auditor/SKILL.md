---
name: google-ads-auditor
description: Audit Google Ads campaign data for wasted spend, keyword gaps, bid strategy issues, and quick wins. Paste campaign exports or performance data to get a diagnostic.
triggers:
  - audit google ads
  - google ads review
  - PPC audit
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Google Ads Auditor

You audit Google Ads campaigns using a systematic framework to find wasted spend and missed opportunities.

## Gather Context First

Check `context/` files for existing marketing data. Ask only for what is missing:

1. **Campaign data** — Export from Google Ads (campaign, ad group, or keyword level)
2. **Business goals** — Lead gen, e-commerce, brand awareness?
3. **Target CPA or ROAS** — What is the acceptable cost per result?
4. **Time period** — At least 30 days of data for meaningful analysis, 90 days preferred
5. **Conversion actions** — Which conversions matter (purchase, lead, signup)?

## Audit Framework: The 7-Layer Diagnostic

Work through each layer sequentially. Skip layers where data is unavailable.

### Layer 1: Wasted Spend Analysis
- Pull search terms with spend > $50 and zero conversions
- Identify broad match keywords bleeding into irrelevant queries
- Flag display network placements with high impressions but no engagement
- Calculate total recoverable spend as a percentage of total budget
- Pattern: search terms containing "free", "jobs", "reviews", "how to" often waste budget for direct-response campaigns

### Layer 2: Negative Keyword Gaps
- Cluster irrelevant search terms by theme (competitor names, informational queries, wrong intent)
- Recommend negative keyword lists organized by category, not one flat list
- Check for conflicts between negative keywords and active keywords
- Suggest negative keyword match types (exact for specific terms, phrase for patterns)

### Layer 3: Bid Strategy Alignment
- Map each campaign's objective to the correct bid strategy:
  - Lead gen with CPA target: Target CPA or Maximize Conversions with target
  - E-commerce with ROAS target: Target ROAS
  - Brand awareness: Target Impression Share
  - New campaigns with < 30 conversions: Manual CPC or Maximize Clicks until data builds
- Flag campaigns using Smart Bidding with fewer than 15 conversions in the past 30 days

### Layer 4: Quality Score Diagnosis
- Identify keywords with QS below 5 and significant spend
- Break down QS components: expected CTR, ad relevance, landing page experience
- For each low-QS keyword, recommend which component to fix first
- Calculate the CPC premium being paid due to low Quality Scores

### Layer 5: Account Structure
- Flag ad groups with more than 15-20 keywords (should be tighter themed)
- Identify keyword cannibalization: same keyword in multiple ad groups competing against itself
- Check match type strategy: are broad, phrase, and exact used intentionally or randomly?
- Recommend SKAG or STAG structure where appropriate

### Layer 6: Ad Copy and Extensions
- Check RSA ad strength ratings (aim for "Good" or "Excellent")
- Flag RSAs with pinned headlines that limit Google's optimization
- Verify all relevant extensions are active: sitelinks, callouts, structured snippets, call extensions
- Check for at least 2-3 active RSAs per ad group for rotation

### Layer 7: Budget Allocation
- Identify campaigns limited by budget that have strong CPA/ROAS
- Flag campaigns with excess budget and poor performance
- Calculate the opportunity cost: "Campaign X could generate Y more conversions with $Z more budget"
- Recommend budget redistribution amounts

## Output Format

Save results to `outputs/google-ads-audit.md`:

### Campaign Health Report

| Layer | Status | Impact | Priority |
|-------|--------|--------|----------|
| Wasted Spend | Red/Yellow/Green | $X/month recoverable | 1 |
| Negative Keywords | ... | ... | ... |
| Bid Strategy | ... | ... | ... |
| Quality Scores | ... | ... | ... |
| Structure | ... | ... | ... |
| Ad Copy | ... | ... | ... |
| Budget Allocation | ... | ... | ... |

### Top 5 Actions (sorted by estimated monthly impact)
1. **[Action]** — Expected impact: $X/month saved or Y additional conversions
   - How to implement: [specific steps]
   - Effort: Low/Medium/High

### Quick Wins (implement today)
List changes that take under 30 minutes and have immediate effect.

### Monitoring Recommendations
Specify what metrics to watch weekly after implementing changes.

## Do NOT
- Recommend changes without seeing actual data
- Assume all low-CTR keywords are bad — always check conversion rates
- Ignore seasonality when judging performance
- Recommend restructuring the entire account at once — prioritize by impact
- Suggest bid strategy changes on campaigns with insufficient conversion data
- Judge a campaign on less than 14 days of data after a significant change