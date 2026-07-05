# /pipeline-battlecard: Competitive Intelligence Pipeline

Research a competitor, compare against previous intel, and produce a sales-ready battlecard.

## Inputs

Two things are needed before starting:

1. **Company profile** — Read `context/business-info.md` for your positioning, differentiators, and target buyers. If it doesn't exist, ask the user to describe their company in 2-3 sentences.
2. **Competitor target** — The user provides a competitor name and domain.

## Steps

### 1. Deep research

Gather competitive intel from every available source:

**Primary sources** (competitor's own content):
- Website and product pages
- Pricing and packaging pages
- Blog and changelog
- Press releases and newsroom
- Careers page (reveals priorities)
- Customer case studies

**Third-party sources:**
- G2 and TrustRadius reviews
- Analyst reports (Gartner, Forrester if available)
- Fintech/industry trade press
- Reddit and community discussions
- Funding and valuation data

**How it searches:**
- Start with the competitor's main site and map the structure
- Follow links to pricing, docs, changelog, blog
- Search for "[competitor] vs", "[competitor] review", "[competitor] alternatives"
- Fall back to web search if direct site access fails
- Log every URL and search query used

If Firecrawl MCP is available, use it for full-page scraping. Otherwise, use the built-in web search and fetch tools. Both work. Firecrawl is faster for large sites.

Save all raw research to `outputs/competitive-intel/[competitor-slug]-research.md` with source URLs.

### 2. Baseline diff

Check if a previous battlecard exists at `outputs/competitive-intel/[competitor-slug]-battlecard.md`.

**If it exists:** Compare new research against the previous version. Call out what changed: pricing shifts, new features, leadership changes, positioning pivots, new customers. Present the diff clearly before proceeding.

**If it doesn't exist:** Skip this step. This is the first run for this competitor.

### 3. Synthesize battlecard

Build the battlecard with these sections:

- **Overview** — What they do, who they sell to, how they position
- **Strengths** — Be honest. Reps lose credibility when battlecards pretend competitors have no strengths.
- **Weaknesses** — Where they fall short relative to us
- **Differentiators** — What we do that they can't or won't
- **Pricing comparison** — Side by side if available, estimated ranges if not
- **Talk track** — Sales language, not marketing copy. Numbers, timelines, named products. Every claim traceable to a source.
- **Objection handling** — Top 5 objections a prospect might raise based on this competitor's positioning, with specific responses
- **Win strategy** — How to position against them in a deal

Use sales language throughout. "20-30% lower TCO on sustained training runs" beats "better pricing." Reps lose credibility when battlecards read like press releases.

### 4. Human review

Present the complete battlecard for review. Do not save until the user approves.

Show:
- The full battlecard
- What changed since last version (if baseline existed)
- Source count and any gaps in coverage

### 5. Save and notify

On approval:

- Save the battlecard to `outputs/competitive-intel/[competitor-slug]-battlecard.md`
- Save the current research as the new baseline at `outputs/competitive-intel/[competitor-slug]-baseline.md`
- If Google Drive MCP is available: also save to a shared competitive intelligence folder
- If Slack MCP is available: post a summary to the team channel with a link

If no MCPs are configured, save locally and tell the user where the files are.

## How to use

Run: `/pipeline-battlecard [competitor name]`
Re-run monthly or after any major competitor event to keep cards current.