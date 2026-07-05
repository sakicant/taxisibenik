---
name: directory-submissions
description: Plan and run directory submissions across SaaS, AI, no-code, MCP, and B2B review directories. Builds the backlink and AI-citation foundation. Sequenced — readiness gate first, destination pages before submissions, positioning varied per directory type.
triggers:
  - directory submissions
  - submit to directories
  - product hunt launch prep
  - get backlinks
  - ai directory listing
  - mcp registry
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Directory Submissions

Plan and run a directory submission program. Three things directories do well: pass dofollow backlinks (raises domain authority), create discovery surface area (in-market browsers find the product), and feed AI engines that pull from high-DR directories when answering "best [category]" queries.

Directories alone don't generate leads. They pass authority into pages that DO generate leads. Build destination pages first, then submit.

## Three rules

### 1. Foundation before submission
Don't submit to anything until the landing page is live, indexed, and has:
- Single H1, sequential heading hierarchy.
- Real pricing page (even "free while in beta").
- Privacy policy + terms.
- Logo assets in PNG + SVG + 1024x1024 square + favicon.
- 5-8 real screenshots at 1920x1080.
- 60-90s demo video.
- FAQ schema markup.
- Organization, Product, SoftwareApplication structured data.

### 2. Destination pages before directories
Directories are the source of link equity. You need destinations to convert the resulting traffic. Minimum:
- 3-5 competitor alternative pages (`/alternatives/[competitor]`).
- 3-5 use-case pages (`/for/[audience]` or `/use-cases/[case]`).
- A "best of" blog post about your category that includes honest competitor coverage.

### 3. Positioning varies by directory type
Don't copy-paste the same description everywhere. AI engines penalize duplicate content; each directory audience responds to different framing. See `references/positioning-variations.md` for the full variant library.

## Workflow

### Step 1: Readiness assessment
Ask the 9 readiness questions above. If anything fails, help the user build the missing piece before continuing.

### Step 2: Pick directories per tier
Use `references/directory-list.md`. Tier 1 directories (Product Hunt, BetaList, AlternativeTo, G2, Capterra) are high-DR but slow review. Tier 2 (TAAFT, Futurepedia, niche aggregators) are fast and cumulatively meaningful. Tier 3 (long tail) are diminishing returns — submit selectively.

### Step 3: Draft positioning variants
For each tier-1 directory, write a short positioning variant per the table in `references/positioning-variations.md`. Don't reuse copy.

### Step 4: Stagger submissions
Don't submit to 30 directories in one day. Stagger over 2-3 weeks. Track in a CSV (template at `references/submission-tracker.csv`).

### Step 5: Track results
Weekly check on referrer logs and DR changes. Some directories nofollow links — note them but still submit if the discovery value is real.

## Output format

Save the submission plan to `outputs/directory-submissions/<date>-plan.md` with:
- Readiness gate result.
- Selected directories (tier 1 / 2 / 3) with rationale.
- Positioning variant per directory.
- Submission schedule.
- Tracker CSV referencing the template in this skill's references/.

## Cross-references

For Product Hunt launch specifically, see `launch-playbook`. For competitor comparison/alternative pages (the destination pages), see `competitor-comparison-writer`. For programmatic SEO landing pages behind directory traffic, see `programmatic-seo-builder`. For AI citation optimization of those pages, see `ai-seo-optimizer` and `geo-citability-scanner`.
