---
name: data-reconciliation
description: Compare data from two or more sources to find mismatches, quantify discrepancies, and identify root causes. Use when transaction counts don't match, revenue figures diverge between systems, or you need to validate data consistency across platforms.
triggers:
  - reconcile data
  - compare exports
  - find discrepancies
  - data mismatch
  - why don't these numbers match
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Data Reconciliation

You systematically compare data from two or more sources to find where they disagree, how much it matters, and why it happened.

## Gather Context First

1. **Sources** — Which two (or more) systems are being compared? (e.g., shop system vs analytics, CRM vs billing, warehouse A vs warehouse B)
2. **Join key** — What field connects records across sources? (transaction ID, date + customer, order number)
3. **Comparison fields** — Which metrics should match? (revenue, count, status, amount)
4. **Time range** — What period are we comparing?
5. **Tolerance** — What variance is acceptable? (financial data: <0.1%, behavioral metrics: <2%, operational: <5%)
6. **Known issues** — Any gaps already identified? Timezone differences? Currency conversions?

## Reconciliation Process

### Step 1 — Profile Each Source Independently

Before comparing, understand each dataset on its own:

- Row count and date range coverage
- Null/missing values in key fields
- Duplicate records (same join key appearing more than once)
- Data types and formats (date formats, decimal precision, currency symbols)
- Summary totals (total revenue, total transactions, total units)

Flag any immediate data quality issues. These often explain discrepancies before you even start comparing.

### Step 2 — Standardize and Align

Make both sources comparable:

- Parse dates into the same format and timezone
- Normalize currency (convert to a single currency if multi-currency)
- Trim whitespace, normalize case on string join keys
- Handle known mappings (e.g., "Completed" in system A = "Paid" in system B)
- Align granularity (if one source is daily and the other is per-transaction, aggregate first)

### Step 3 — Match and Compare

Run a full outer join on the join key:

| Category | Description |
|----------|-------------|
| **Matched** | Record exists in both sources, values agree within tolerance |
| **Value mismatch** | Record exists in both sources, but comparison fields differ |
| **Source A only** | Record exists in source A but not source B |
| **Source B only** | Record exists in source B but not source A |

For each category, report the count and total monetary impact.

### Step 4 — Investigate Patterns

Don't just list mismatches. Look for systematic causes:

- **Time-based** — Do discrepancies cluster on specific days, weekends, month boundaries, or time zones?
- **Segment-based** — Are mismatches concentrated in a payment provider, country, product category, or customer segment?
- **Directional bias** — Is one source consistently higher or lower? By how much?
- **Threshold patterns** — Do mismatches only appear above or below a certain value?
- **Status-based** — Are refunds, cancellations, or pending transactions handled differently?
- **Lag patterns** — Does one system record transactions later than the other?

### Step 5 — Quantify Impact

For each pattern found:

1. **Scope** — How many records are affected?
2. **Financial impact** — Total over- or under-reporting
3. **Trend** — Is it getting worse, improving, or stable?
4. **Confidence** — How certain are you about the root cause?

### Step 6 — Report

Deliver two outputs:

**Summary report** (for stakeholders):
- Total records compared and match rate
- Top 3 root causes with impact figures
- Recommended fixes, prioritized by impact
- Confidence assessment and data quality caveats

**Detail file** (for investigation):
- Every mismatched record with both source values, difference, and pattern classification
- Grouped by root cause category
- Sortable by impact amount

## Severity Classification

| Variance | Financial | User Metrics | Operational |
|----------|-----------|-------------|-------------|
| Match | < 0.1% | < 2% | < 5% |
| Minor | 0.1 - 1% | 2 - 5% | 5 - 10% |
| Significant | > 1% | > 5% | > 10% |

Adjust thresholds based on the user's context. A 0.5% variance in a $10M dataset is $50K — that might be significant regardless of the percentage.