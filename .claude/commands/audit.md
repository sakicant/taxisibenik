# /audit — Site Marketing Audit

Perform a quick marketing audit of a website or landing page.

1. Fetch and review the target URL
2. Score each dimension from 1 to 10 with a one-sentence finding:
   - **Messaging clarity** — is the value proposition obvious within 5 seconds?
   - **CTA effectiveness** — are calls to action visible, specific, and compelling?
   - **Social proof** — are there testimonials, logos, case studies, or usage numbers?
   - **SEO basics** — title tags, meta descriptions, heading structure, page speed
   - **Trust signals** — privacy info, security badges, contact details, professional design
   - **Mobile experience** — responsive layout, tap targets, load time on mobile
3. Summarize:
   - **Top 3 quick wins** (things fixable in under an hour)
   - **Top 3 deeper fixes** (things that need more effort but have high impact)
4. Print a quick scorecard to the terminal
5. Save the full detailed report to `outputs/site-audit.md`

Usage: `/audit [url]`
Examples:
- `/audit https://example.com`
- `/audit https://example.com/pricing`