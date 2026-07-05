---
name: ads-landing-audit
description: Audit a landing page that's the destination of a paid ad campaign. Focus is on ad-to-landing message match, promise alignment, mobile experience, tracking setup. Distinct from page-cro (general optimization). For organic landing-page work use page-cro.
triggers:
  - ad landing page
  - message match
  - ad-to-landing alignment
  - paid traffic landing
  - lp audit
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Ads Landing Audit

Audit a landing page where the source is paid traffic. The audit is opinionated about three things ad-driven landings get wrong: message match, promise alignment, and mobile.

## Gather context

Ask if not provided:

1. **The ad** — copy and creative for the ad(s) driving traffic.
2. **The landing page** — URL or screenshot.
3. **The campaign goal** — sign-up, demo request, purchase, lead capture?
4. **Performance baseline** — current CTR, conversion rate, cost-per-conversion?
5. **Traffic split** — desktop vs. mobile share?

## The audit dimensions

### 1. Message match (most failures here)
The first thing the visitor sees on the landing page must echo what the ad said. Visitors who see different language assume they clicked the wrong link.

Check:
- Headline: does it use the same key phrase as the ad copy?
- Value prop: same outcome promised?
- Audience: same audience targeted (B2B / consumer / specific role)?
- Visual: same product/feature shown?

If the ad says "AI workspace generator for marketing teams" and the landing page says "Build smarter workflows", that's a match failure.

### 2. Promise alignment
The ad promises X. Does the landing page deliver X within 5 seconds of arrival?

Check:
- Above-the-fold completes the promise (not buried below).
- CTA matches the ad CTA (don't ad "free trial" -> landing "request demo").
- Pricing visible if the ad implies free or low-cost.

### 3. Mobile experience
Ad traffic is mobile-heavy on Meta, TikTok, LinkedIn. Audit on actual mobile devices:

- Above-the-fold renders without scroll on a 5.5" screen.
- CTA button is tappable (44px minimum).
- Form is single-column with appropriate input types (email keyboard, tel keyboard).
- Page loads in under 3 seconds on 4G (use PageSpeed Insights for a real test).
- No popups blocking content immediately.

### 4. Form / conversion friction
- Single-column form.
- Minimum required fields. Email-only converts highest.
- Real-time validation, not validate-on-submit.
- Single CTA button, distinct color, action verb.
- Privacy reassurance for B2B / sensitive lead types.

### 5. Tracking and pixels
- Conversion event fires on the right action (form submission, button click, scroll-depth).
- Pixels installed and firing for every ad platform driving traffic.
- UTM parameters captured and stored.
- Consent banner doesn't block conversion tracking incorrectly.

## Output format

Save audit to `outputs/ads-landing/<campaign-slug>-<date>.md`:

```
## Audit: <landing page URL>
- Campaign: <name>
- Audit date: <date>

## Findings (severity-ordered)

### Critical (fixing changes conversion immediately)
1. <finding> — <evidence> — <fix>
2. ...

### High (fixing improves conversion in 1-2 weeks)
1. ...

### Medium / housekeeping
1. ...

## Quick wins (under 2 hours of work)
1. ...

## Bigger projects (over 1 day)
1. ...

## A/B test recommendations
1. <hypothesis> — <metric to track> — <minimum runtime>
```

## Common mistakes

- Auditing a landing page in isolation without the ad. Half the audit is the comparison.
- Ignoring mobile because the auditor's laptop renders fine.
- Recommending a full redesign when small changes would win.
- Missing tracking issues. Conversion data is wrong, every other decision is downstream.

## Cross-references

For general (non-ads-driven) landing-page conversion work, use `page-cro`. For the ad creative side, use `ad-copy-writer`, `google-ads-auditor`, `meta-ads-auditor`. For PPC unit economics underneath the campaign, use (when added) `ppc-economics`. For form-specific conversion, use `form-cro` (when added).
