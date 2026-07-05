# /launch-plan — Launch Runbook Generator

Generate a structured launch runbook for a product or feature.

1. Gather context from the user or context files:
   - What is launching and why it matters
   - Target audience and segments
   - Timeline and key dates
   - Available channels (email, social, blog, communities, paid)
   - Budget constraints if any
2. Build a week-by-week plan covering three phases:
   - **Pre-launch** — teaser content, list building, asset creation, internal alignment
   - **Launch day** — announcement sequence, channel-by-channel timing, response plan
   - **Post-launch** — follow-up content, metric review, iteration plan
3. For each phase, include:
   - Core messaging and positioning
   - Email sequence outline (subject lines, send timing, goals)
   - Social post outline (platform, format, key message per post)
   - Success metrics with specific targets
4. Save the complete runbook to `outputs/launch-plan.md`

Usage: `/launch-plan [product or feature description]`
Examples:
- `/launch-plan v2.0 release with new dashboard`
- `/launch-plan free tier launch targeting indie developers`