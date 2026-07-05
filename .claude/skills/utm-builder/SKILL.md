---
name: utm-builder
description: Generate UTM-tagged URLs with consistent naming conventions, GA4 event naming, and conversion tracking specs. Use when launching campaigns or standardizing tracking.
triggers:
  - build UTMs
  - UTM parameters
  - tracking URLs
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# UTM Builder

You create tracking URLs with consistent naming conventions that make analytics data clean and actionable.

## Gather Context First

1. **Destination URL(s)** — Where should the links point?
2. **Platforms** — Which channels will these URLs be used on?
3. **Campaign name** — What is the campaign called internally?
4. **Variants** — Different ad creatives, audiences, or placements?
5. **Analytics tool** — GA4, Mixpanel, Amplitude, other?
6. **Existing convention** — Check `reference/` for any existing UTM naming guide

## UTM Taxonomy Standard

Establish a consistent, machine-readable naming system. Every value must be lowercase, no spaces, using hyphens as separators.

### Parameter Definitions

| Parameter | Purpose | Format | Examples |
|-----------|---------|--------|----------|
| `utm_source` | Platform or publisher | Lowercase platform name | google, facebook, linkedin, newsletter, partner-blog |
| `utm_medium` | Marketing channel type | Standardized channel | cpc, cpm, social-paid, social-organic, email, referral, display, video |
| `utm_campaign` | Campaign identifier | kebab-case with date hint | spring-launch-2026, product-v2-q2, webinar-ai-trends |
| `utm_term` | Keyword or targeting | kebab-case descriptor | brand, non-brand, lookalike-1pct, retargeting-30d |
| `utm_content` | Creative or placement variant | kebab-case variant | cta-green, hero-v2, sidebar-banner, carousel-3-image |

### Medium Standardization Rules
The most common source of UTM chaos is inconsistent medium values. Standardize on this list:

- `cpc` — Paid search (Google Ads, Bing Ads)
- `cpm` — Display advertising (banner, programmatic)
- `social-paid` — Paid social (Meta Ads, LinkedIn Ads, TikTok Ads)
- `social-organic` — Organic social posts
- `email` — Email campaigns (newsletters, drip sequences)
- `referral` — Partner links, guest posts, affiliate
- `video` — YouTube ads, video campaigns
- `sms` — SMS campaigns
- `qr` — QR code campaigns (print, events)

### Campaign Naming Pattern
Use a consistent structure: `[initiative]-[descriptor]-[date-or-quarter]`

Examples:
- `product-launch-mar2026`
- `webinar-ai-productivity-q2`
- `retargeting-trial-expired-ongoing`
- `newsletter-weekly-2026`

## URL Generation Process

### Step 1: Validate the Base URL
- Remove existing UTM parameters from the destination URL
- Ensure the URL uses HTTPS
- Verify no trailing slashes or query parameter conflicts

### Step 2: Build Parameter Sets
For each platform and variant combination:
- Apply the taxonomy rules above
- URL-encode any special characters in parameter values
- Keep the total URL under 2,000 characters

### Step 3: Generate the Final URLs
Concatenate base URL + ? (or &) + parameters in standard order: source, medium, campaign, term, content.

## GA4 Event Integration

If the user uses Google Analytics 4, also provide event naming conventions:

### Custom Event Naming
GA4 event names must be snake_case, under 40 characters, no spaces.

| Event Name | Parameters | When to Fire |
|------------|-----------|--------------|
| `campaign_landing` | source, medium, campaign | UTM link landing page view |
| `campaign_signup` | source, medium, campaign | Signup from a UTM-tagged session |
| `campaign_purchase` | source, medium, campaign, value | Purchase from a UTM-tagged session |

### GA4 Custom Dimensions
Recommend creating custom dimensions for:
- `utm_content` (not captured by default in GA4)
- `utm_term` (not always captured reliably)

## Output Format

Save to `outputs/utm-urls.md`:

### Generated URLs

| Platform | Variant | UTM Source | UTM Medium | UTM Campaign | Full URL |
|----------|---------|-----------|-----------|-------------|----------|
| ... | ... | ... | ... | ... | [clickable URL] |

### URL Shortener-Ready List
Plain text list of all URLs, one per line, for pasting into a URL shortener.

### Naming Convention Reference Card
A compact summary of the taxonomy for the team to bookmark or print. Include the medium standardization list and campaign naming pattern.

### QA Checklist
- [ ] All values are lowercase with no spaces
- [ ] Medium values use the standardized list
- [ ] Campaign names follow the naming pattern
- [ ] No duplicate parameter combinations
- [ ] URLs tested and resolve correctly
- [ ] Special characters are URL-encoded

## Do NOT
- Use spaces or uppercase in UTM values
- Mix naming conventions within a campaign
- Forget to URL-encode special characters
- Use `utm_source=facebook` for both organic and paid — differentiate with medium
- Create UTM parameters for internal links (UTMs are for external traffic only — they overwrite the referral source)
- Skip the QA checklist — broken UTMs poison analytics data permanently