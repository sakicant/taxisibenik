---
name: crawl-analyzer
description: Process and analyze website crawl exports from Screaming Frog, Sitebulb, Ahrefs, or similar tools. Identifies technical SEO issues, segments pages by type, and produces prioritized fix lists. Use when auditing a site's technical health, investigating ranking drops, or preparing SEO recommendations.
triggers:
  - analyze crawl
  - crawl audit
  - technical SEO audit
  - screaming frog analysis
  - site health check
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Crawl Analyzer

You turn raw crawl data into a prioritized technical SEO action plan. Work with the data the user provides — don't assume access to live URLs unless explicitly given.

## Gather Context First

1. **Crawl source** — Screaming Frog, Sitebulb, Ahrefs, SEMrush, or custom? (Affects column names and available data.)
2. **Export files** — Which files/tabs were exported? (e.g., internal_all.csv, response_codes.csv, page_titles.csv)
3. **Site type** — E-commerce, blog/media, SaaS, corporate, marketplace? (Affects prioritization.)
4. **Platform** — Shopify, WordPress, Wix, custom? (Affects what's fixable and how.)
5. **Known issues** — Any existing problems the user is aware of? Recent migrations, redesigns, or traffic drops?
6. **Google Search Console data** — Available? (Adds impressions, clicks, and indexing data to the analysis.)

## Analysis Process

### Step 1 — Page Type Segmentation

Before analyzing issues, segment pages by type. This is the most important step — issues on product pages matter more than issues on tag pages.

Parse URL paths to classify:

| Page Type | URL Pattern Examples |
|-----------|-------------------|
| Homepage | `/`, `/index` |
| Category/Collection | `/collections/`, `/category/`, `/shop/` |
| Product/Item | `/products/`, `/p/`, URL contains SKU pattern |
| Blog/Article | `/blog/`, `/articles/`, `/news/` |
| Landing page | `/lp/`, `/campaign/`, short path + no sub-path |
| Support/Help | `/help/`, `/faq/`, `/support/` |
| Legal/Policy | `/privacy`, `/terms`, `/policy` |
| Pagination | contains `/page/`, `?page=`, `?p=` |
| Filtered/Faceted | multiple query params, `/filter/`, `/tag/` |
| System/Utility | `/cart`, `/account`, `/checkout`, `/search` |

Report the count and percentage for each type. Flag types with unusually high counts (index bloat signal).

### Step 2 — Crawlability and Indexability

**Status codes:**
- Count and list all 3xx, 4xx, and 5xx URLs
- Identify redirect chains (A → B → C — should be A → C)
- Flag redirect loops
- Flag soft 404s (200 status but thin/error content)

**Robots and indexing directives:**
- Pages blocked by robots.txt but linked internally
- Pages with `noindex` that receive organic traffic (via GSC data)
- Pages with `noindex` that are in the sitemap (contradiction)
- Canonical tag issues: self-referencing missing, pointing to non-indexable URL, canonical chains

**Crawl depth:**
- Pages more than 3 clicks from the homepage
- Orphan pages (no internal links pointing to them)
- Crawl depth distribution by page type

### Step 3 — On-Page Elements

**Titles:**
- Missing, empty, or duplicate title tags
- Titles over 60 characters (truncation risk)
- Titles under 30 characters (underutilized)
- Titles identical to H1

**Meta descriptions:**
- Missing or empty
- Duplicates across multiple pages
- Over 160 characters
- Under 70 characters

**Headings:**
- Missing H1
- Multiple H1 tags on one page
- H1 identical to title tag (missed opportunity)
- Heading hierarchy gaps (H1 → H3, skipping H2)

**Content:**
- Thin pages (word count under 200 for content pages)
- Near-duplicate content (similar titles + similar word counts on different URLs)
- Pages with no indexable text content (JavaScript-rendered only)

### Step 4 — Site Architecture

**Internal linking:**
- Pages with only 1 internal link pointing to them
- Pages with over 100 outbound internal links (crawl budget dilution)
- Broken internal links (linking to 4xx or 5xx)
- Follow/nofollow ratio on internal links

**Sitemap:**
- URLs in sitemap returning non-200 status
- Indexable URLs not in sitemap
- Sitemap URLs with `noindex` (contradiction)
- Sitemap size (over 50K URLs per file?)

### Step 5 — Performance Signals

If available in crawl data:
- Page size over 3MB
- Pages with more than 100 requests
- Images over 500KB
- Pages without HTTPS
- Mixed content (HTTP resources on HTTPS pages)
- Missing or incorrect hreflang (if multi-language)

### Step 6 — Structured Data

- Pages with structured data errors (invalid JSON-LD)
- Pages missing expected schema (product pages without Product schema, articles without Article schema)
- Deprecated schema types
- Required properties missing within existing schema

### Step 7 — Scoring and Prioritization

Score each issue across three dimensions:

| Dimension | Weight | Description |
|-----------|--------|-------------|
| SEO impact | 40% | How much does this affect rankings and traffic? |
| Business impact | 40% | Does it affect revenue-generating pages? |
| Fix effort | 20% | How hard is it to fix? (inverse — easy fixes score higher) |

**Priority bands:**
- **Critical (8.0+)** — Fix this week. Indexing blockers, broken revenue pages, security issues.
- **High (6.0-7.9)** — Fix within 2 weeks. Duplicate content on key pages, redirect chains, missing schema.
- **Medium (4.0-5.9)** — Fix within a month. Missing meta descriptions, thin content, image optimization.
- **Low (< 4.0)** — Backlog. Minor formatting issues, non-indexed pages.

Adjust effort scores based on platform. Redirects are effort 2 on Shopify (URL redirect UI), effort 4 on custom builds (server config).

### Step 8 — Deliverables

1. **Executive summary** — Site health score (0-100), top 3 issues, estimated traffic impact
2. **Quick wins** — High impact + low effort fixes (aim for 5-10 items)
3. **Full issue list** — Every issue with: page type affected, URL count, severity, priority score, recommended fix
4. **Page type report** — Health score per page type (homepage, products, blog, etc.)
5. **Action plan** — Fixes grouped by sprint/week, ordered by priority score