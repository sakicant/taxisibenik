# /metrics-review — Metrics Review

Pull and analyze key metrics to support decisions.

## Workflow

1. **Identify sources** — Check context files, connected tools (analytics, CRM, project management), and local data files
2. **Pull data** — Gather metrics for the requested time period
3. **Analyze** — Calculate trends, comparisons, and anomalies
4. **Present** — Structured report with insights

## Report Format

### Key Metrics
| Metric | Current | Previous | Change | Status |
|--------|---------|----------|--------|--------|
| ... | ... | ... | +/-% | 🟢/🟡/🔴 |

### Trends
- [What's improving and why]
- [What's declining and why]
- [What needs attention]

### Recommendations
1. [Action based on data]
2. [Action based on data]

## If data is unavailable
- Check if MCP tools are configured for the data source
- Ask the user to provide data manually (paste or file path)
- Document which metrics couldn't be pulled and why

Usage: `/metrics-review [scope: weekly|monthly|quarterly] [area: marketing|sales|product|all]`