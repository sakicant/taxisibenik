---
name: ad-spend-allocator
description: Analyze multi-channel ad spend and results to recommend budget reallocation. Paste spend and performance data across channels to get optimization recommendations.
triggers:
  - allocate ad budget
  - budget optimization
  - ad spend review
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Ad Spend Allocator

You reallocate ad budgets across channels using marginal efficiency analysis, not gut feeling or equal distribution.

## Gather Context First

Check `context/` files for existing marketing data. Ask only for what is missing:

1. **Channel data** — Spend and results per channel for the past 3+ months
2. **Metrics** — CPA, ROAS, CPL, or conversion rate per channel
3. **Total budget** — Monthly ad budget and any constraints
4. **Business model** — What is a customer worth? (LTV or first-purchase value)
5. **Attribution model** — Last click, multi-touch, or platform-reported?
6. **Constraints** — Minimum spends on certain channels, brand requirements, contractual commitments

## Allocation Framework: Marginal Efficiency Analysis

### Phase 1: Channel Efficiency Baseline
Build the efficiency table for each channel:

- **Cost per acquisition (CPA)** — Total spend divided by total conversions
- **Incremental CPA** — CPA of the last 20% of spend (is the marginal dollar efficient?)
- **Conversion volume** — Total conversions delivered
- **Channel ceiling** — Estimated maximum spend before severe diminishing returns
- **Time to convert** — Average days from click to conversion (affects cash flow)
- **Attribution confidence** — How trustworthy is this channel's reported data?

### Phase 2: Diminishing Returns Detection
For each channel, check if CPA is rising with spend:

- Compare CPA at different budget levels (split data into quartiles by spend periods)
- A channel at diminishing returns shows: CPA up 30%+ at high-spend periods vs low-spend periods
- Channels with flat CPA curves still have headroom to scale
- Pattern: Search channels hit ceilings faster (limited query volume). Social channels scale further but with rising costs

### Phase 3: Attribution Reconciliation
Platform-reported numbers lie. Adjust before reallocating:

- **Google Ads** typically over-reports by 10-20% (last-click bias)
- **Meta Ads** over-reports by 20-40% (view-through attribution inflates numbers)
- **Organic/direct** is often under-credited (assists from paid that convert via direct)
- Recommended: apply a conservative 0.7x multiplier to platform-reported Meta conversions and 0.85x for Google when no independent attribution is available
- If multi-touch attribution data exists, use it as the primary source

### Phase 4: Reallocation Modeling
Apply the marginal dollar framework:

1. Rank channels by incremental CPA (adjusted for attribution)
2. The next dollar should go to the channel with the lowest incremental CPA
3. Shift budget from channels above the blended CPA target to those below it
4. Maintain a 10-15% testing budget for new channels or experiments
5. Never move more than 30% of a channel's budget in a single period — large shifts disrupt optimization algorithms

### Phase 5: Seasonal and Strategic Adjustments
- Map historical performance by month to identify seasonal patterns
- Pre-allocate budget increases for known peak periods (Black Friday, back-to-school, Q4 enterprise buying)
- Reduce spend on channels that historically underperform in specific seasons
- Account for competitor behavior: CPCs rise in peak seasons, so expected CPA rises too

## Output Format

Save results to `outputs/budget-allocation.md`:

### Current vs. Recommended Allocation

| Channel | Current Spend | Current CPA | Incremental CPA | Recommended Spend | Change | Expected CPA |
|---------|--------------|-------------|-----------------|-------------------|--------|--------------|
| Google Search | ... | ... | ... | ... | +$X | ... |
| Meta Ads | ... | ... | ... | ... | -$X | ... |
| LinkedIn | ... | ... | ... | ... | ... | ... |

### Budget Shift Summary
- Move $X from [Channel A] to [Channel B] because [reason with data]
- Net expected impact: Y additional conversions at $Z blended CPA

### Flags and Risks
- [Channel] showing diminishing returns above $X/month
- [Channel] undertested — recommend $X test budget over 30 days
- Attribution gap: [Channel] likely over/under-credited by X%

### Testing Budget Recommendations
Allocate specific amounts to 1-2 untested or undertested channels with rationale and success criteria.

### 90-Day Review Plan
Specify when to re-evaluate each reallocation decision and what data points to watch.

## Do NOT
- Recommend killing a channel based on one period of data — use at least 60 days
- Ignore attribution differences between channels (this is the biggest source of bad allocation)
- Assume linear scaling — doubling budget rarely doubles results
- Reallocate without adjusting for seasonality
- Move 100% of budget out of a channel overnight — this disrupts algorithms and kills remarketing audiences
- Treat platform-reported conversions as ground truth