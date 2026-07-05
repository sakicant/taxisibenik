---
name: lead-magnets
description: Design lead magnets that capture emails and generate qualified leads — and naturally lead to product adoption. Covers magnet types, fit-to-product alignment, copy, distribution, and post-capture flow. Pairs with email-sequence-builder for the after-capture flow.
triggers:
  - lead magnet
  - gated content
  - content upgrade
  - ebook for emails
  - cheat sheet for capture
  - opt-in offer
  - what should i give for emails
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Lead Magnets

Plan lead magnets that capture qualified emails. The magnet must do three things: be specific enough that the right people self-select, useful enough that the email is worth giving up, and naturally lead to the product.

## Magnet types (by effort and quality)

| Type | Effort | Quality signal | Best for |
|---|---|---|---|
| Checklist / one-pager | Low (1-2 days) | OK | Top of funnel, quick wins |
| Cheat sheet / quick reference | Low | OK | Tactical audience, dev tools |
| Template / canvas (Notion, Figma, Google Doc) | Medium (3-5 days) | High | Audience that wants frameworks |
| Spreadsheet / calculator | Medium | High | Numerical decisions (pricing, ROI) |
| Email course (5-7 day drip) | High (1-2 weeks) | Very high | Brand-building, longer engagement |
| Mini ebook / report | High | Variable — depends on substance | Thought leadership, premium audience |
| Interactive tool / web app | Highest | Highest | Product-tied, demonstrates capability |
| Video course / workshop | Highest | Highest | Audiences that want to be taught |

Match effort to audience. A B2B procurement crowd might value a Notion template; a developer audience scoffs at it but downloads a CLI tool.

## Fit-to-product test

The best lead magnets are a **stripped-down version of the product**. The magnet does one slice of what the product does, for free.

- Email tool? Lead magnet is "10 cold email templates that get replies" — same value framework, free.
- Project management tool? Lead magnet is "Sprint planning template" in Notion.
- Workspace generator? Lead magnet is "10-question workspace audit" — exactly what the audit feature does, no signup required.

If the magnet has nothing to do with the product, you'll capture emails but conversion will be low. Test fit by asking: would a happy customer ALSO want this? If no, the magnet is targeting the wrong audience.

## Workflow

### Step 1: Pick the magnet
Pick by audience and effort. Default to template/cheat-sheet/calculator for early-stage products — they're high-quality-signal at low effort.

### Step 2: Build it
- Make it useful on its own. The magnet must solve a real problem for someone who never buys the product.
- Brand it lightly. Logo and a "see more from <brand>" footer. No 17 CTAs to upgrade.
- File format: PDF for static (Word/Pages exports), Notion/Figma duplicate links for templates, web tool for interactive.

### Step 3: Write the capture page
- Headline = specific outcome ("Send cold emails that get 30%+ reply rates" not "Improve your outreach").
- 3-5 bullets describing what's inside.
- Email field, single submit button, no other fields. Each extra field cuts conversion ~10%.
- Privacy reassurance ("We won't spam. Unsubscribe in one click.").
- Optional: small preview image of the magnet.

### Step 4: Distribution
- Mention in every blog post that's relevant.
- Pin on social profiles.
- Embed in product onboarding (free version) where contextually relevant.
- Pitch as a guest post angle ("I have a checklist for this").

### Step 5: Post-capture flow
Don't drop the email into a mailing list and forget. Trigger a sequence (see `email-sequence-builder`):
- Email 1: deliver the magnet immediately.
- Email 2 (day 2-3): ask if they got value, offer a related read.
- Email 3 (day 5-7): introduce the product as the natural next step.
- Email 4+: ongoing newsletter cadence.

## Output format

Save to `outputs/lead-magnets/<slug>-plan.md` with:
- Magnet type and reasoning.
- Outline / draft of the magnet itself.
- Capture page copy.
- Distribution checklist.
- Post-capture email sequence outline (link to `email-sequence-builder` for the full drip).

If the magnet is a template/checklist, also save the actual deliverable to `outputs/lead-magnets/<slug>.md` (or .csv, .json, depending on format).

## Common mistakes

- Generic magnets ("Top 10 marketing tips") — too broad to qualify the audience.
- Asking for too many fields. Email-only converts best.
- No follow-up sequence — the lead goes cold in 48 hours.
- Magnet is way better than the product — sets the wrong expectation.
- Magnet is a thinly disguised brochure.

## Cross-references

For the email drip after capture, use `email-sequence-builder`. For interactive tools as magnets, use `free-tool-strategy`. For the landing page itself, use `landing-page-writer` and `page-cro`. For the headline copy, use `copywriting` (or our existing copy skills).
