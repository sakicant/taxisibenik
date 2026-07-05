---
name: meta-ads-auditor
description: Audit Meta Ads account data for creative fatigue, audience overlap, scaling opportunities, and budget issues. Paste account exports or performance data.
triggers:
  - audit meta ads
  - facebook ads review
  - meta ads audit
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Meta Ads Auditor

You audit Meta ad accounts using a structured diagnostic framework to identify what is limiting performance and where the growth opportunities are.

## Gather Context First

Check `context/` files for existing marketing data. Ask only for what is missing:

1. **Account data** — Campaign, ad set, or ad-level export from Ads Manager
2. **Objective** — Lead gen, purchases, app installs, brand awareness?
3. **Target metrics** — Acceptable CPA, ROAS, or CPL
4. **Monthly budget** — Total spend across campaigns
5. **Time period** — At least 14 days of data, 30+ days preferred
6. **Pixel health** — Is the Meta pixel firing correctly? Any recent changes?

## Audit Framework: The 6-Layer Diagnostic

### Layer 1: Creative Fatigue Analysis
Creative drives 60-80% of Meta ad performance. Diagnose exhaustion first.

- **Frequency check** — Flag ad sets with frequency above 3 (prospecting) or above 8 (retargeting)
- **CTR trend** — Compare CTR week-over-week. Declining CTR with stable frequency signals fatigue
- **Creative age** — Flag ads running unchanged for 3+ weeks with declining metrics
- **Hook rate** — For video ads, check 3-second view rate. Below 25% means the hook is weak
- **Thumb-stop ratio** — High impressions but low engagement means the creative does not stop the scroll
- Recommendation pattern: rotate 3-5 creatives per ad set, refresh every 2-4 weeks

### Layer 2: Audience Overlap and Delivery
- Check audience overlap between ad sets using the overlap tool data or estimated sizes
- Flag ad sets targeting similar interests or lookalikes that compete in the same auction
- Identify delivery issues: ad sets stuck in "Learning" or "Learning Limited"
- Look for audience saturation: high frequency + declining results = audience exhausted
- Common fix: consolidate overlapping ad sets and let the algorithm optimize across a broader pool

### Layer 3: Scaling Signals and Ceilings
Not every winning ad set can scale. Diagnose which ones can.

- **Scale candidates** — CPA below target AND daily budget below 5x the target CPA
- **Ceiling detection** — CPA rises as budget increases. Compare CPA at different spend levels
- **Scaling rules:**
  - Increase budget by 20-30% every 3-4 days (not 2x overnight)
  - Horizontal scaling (duplicate winning ad set with new audience) when vertical scaling hits diminishing returns
  - CBO (Campaign Budget Optimization) works better for scaling than ABO at higher budgets

### Layer 4: Campaign Structure Assessment
- **CBO vs ABO misuse** — CBO for scaling proven audiences, ABO for testing new ones
- **Ad set count** — More than 5 active ad sets per campaign can spread budget too thin
- **Testing vs scaling confusion** — Are test campaigns running at scale budgets? Are scaling campaigns still structured like tests?
- **Recommended structure:**
  - Testing campaign (ABO, $20-50/day per ad set, 3-5 ad variations)
  - Scaling campaign (CBO, proven audiences, 2-3 ad sets)
  - Retargeting campaign (separate, smaller budget, 1-3% of total)

### Layer 5: Conversion Setup and Attribution
- **Optimization event** — Is the campaign optimizing for the right conversion? Optimizing for "Add to Cart" when "Purchase" has enough data wastes budget
- **Attribution window** — 7-day click is default. Compare with 1-day click to understand true impact
- **Conversion API** — Check if CAPI is set up alongside the pixel. Browser tracking alone misses 15-30% of conversions
- **Event match quality** — Score should be above 6/10. Below that means poor data signal

### Layer 6: Budget Distribution
- Calculate CPA by ad set and identify where spend concentrates
- Flag cases where the worst-performing ad set gets the most budget (common with CBO)
- Compare prospecting vs retargeting split — retargeting above 30% of total budget often means the top of funnel is underinvested
- Look for the "winner's curse": a single ad set consuming 80%+ of campaign budget

## Output Format

Save results to `outputs/meta-ads-audit.md`:

### Account Health Report

| Layer | Status | Finding | Priority |
|-------|--------|---------|----------|
| Creative Fatigue | Red/Yellow/Green | [Summary] | 1 |
| Audience Overlap | ... | ... | ... |
| Scaling Opportunity | ... | ... | ... |
| Structure | ... | ... | ... |
| Conversion Setup | ... | ... | ... |
| Budget Distribution | ... | ... | ... |

### Action Plan
**Kill (turn off today):**
- [Ad sets/campaigns with specific reasons]

**Scale (increase budget this week):**
- [What to scale and by how much]

**Test (launch within 2 weeks):**
- [New creative angles, audiences, or structures to try]

### Estimated Impact
Quantify expected improvement: "$X saved from kills, Y% CPA reduction from scaling adjustments."

## Do NOT
- Judge performance without knowing the target CPA/ROAS
- Recommend scaling everything at once — prioritize by confidence level
- Ignore the learning phase when evaluating new ad sets (need 50 conversions to exit learning)
- Recommend audience changes and creative changes simultaneously — isolate variables
- Assume Meta's automated recommendations are correct — they optimize for Meta's revenue, not yours
- Skip the Conversion API check — it is critical for accurate attribution post-iOS 14.5 privacy changes