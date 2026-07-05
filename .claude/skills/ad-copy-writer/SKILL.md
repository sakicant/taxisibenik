---
name: ad-copy-writer
description: Write paid ad copy optimized for Google Ads, Meta Ads, and LinkedIn Ads.
triggers:
  - write ad copy
  - Google Ads copy
  - ad creative
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Ad Copy Writer

You write ad copy that converts within strict character limits. Every word must earn its place.

## Gather Context First

Check `context/` for ICP profiles, value propositions, and existing ad performance data. Ask only for what is missing:
1. **What is the offer?** Free trial, demo, download, purchase.
2. **Who is the audience?** Persona, awareness level, pain points.
3. **What platform?** Google Search, Meta, LinkedIn, YouTube.
4. **What is the landing page?** The ad must match the page or conversions drop.
5. **Any existing performance data?** Top-performing headlines, CTR benchmarks.

## Platform Specifications

### Google Search Ads
| Element | Limit | Best Practice |
|---------|-------|---------------|
| Headline 1 | 30 chars | Primary keyword + benefit |
| Headline 2 | 30 chars | Differentiator or proof |
| Headline 3 | 30 chars | CTA or brand name |
| Description 1 | 90 chars | Expand on the value prop |
| Description 2 | 90 chars | Social proof or secondary benefit |
| Display URL path | 15 chars x 2 | Keyword-rich path |

Pin Headline 1 to position 1. Include the target keyword in at least one headline.

### Meta Ads (Facebook/Instagram)
| Element | Limit | Best Practice |
|---------|-------|---------------|
| Primary text | 125 chars above fold (up to 3 lines visible) | Hook in first line |
| Headline | 40 chars | Benefit statement |
| Description | 30 chars | Supporting detail |
| CTA button | Preset options | Match to funnel stage |

Lead with a question, stat, or bold claim in the first line. Most users see only the first 1-2 lines before "See more."

### LinkedIn Ads
| Element | Limit | Best Practice |
|---------|-------|---------------|
| Introductory text | 150 chars above fold | Professional hook |
| Headline | 70 chars | Value prop + CTA |
| Description | 70 chars | Supporting evidence |

LinkedIn audiences respond to professional outcomes and career impact. Avoid consumer-style emotional hooks.

## Writing Process

### Step 1: Define the Message Hierarchy
1. **Primary benefit:** The #1 reason to click (must appear in headline).
2. **Proof point:** Why they should believe you (number, testimonial, brand).
3. **CTA:** What happens when they click (specific, low-friction).

### Step 2: Write Headline Variations (5+ per ad)

**Headline formulas that convert:**
- [Number] + [Benefit]: "Cut onboarding time by 60%"
- [Pain point] + [Solution]: "Stop losing deals to slow follow-up"
- [Question]: "Still doing [painful task] manually?"
- [Social proof]: "Trusted by 10,000+ teams"
- [Specificity]: "Close 3x more deals in 30 days"

### Step 3: Write Description Variations (3+ per ad)
Descriptions expand on the headline. Include:
- A secondary benefit or feature.
- A proof point (customers, results, awards).
- A clear CTA with specificity: "Start your free 14-day trial" not "Learn more."

### Step 4: A/B Test Plan
For each ad group, create:
- 3-5 headline variants testing different angles (benefit, proof, question, urgency).
- 2-3 description variants testing different proof points.
- Run for 7-14 days or until statistical significance.

## Ad Copy Formulas by Funnel Stage

| Stage | Hook Style | CTA |
|-------|-----------|-----|
| Awareness | Problem identification, surprising stat | "See how" / "Learn more" |
| Consideration | Benefit comparison, social proof | "Get the guide" / "Watch demo" |
| Decision | Offer, urgency, risk reversal | "Start free trial" / "Book a call" |

## Output Format

Save ad copy to `outputs/ads/`:

```markdown
# Ad Copy: [Campaign Name] - [Platform]

## Ad Variant 1
- Headline 1: [text] ([char count])
- Headline 2: [text] ([char count])
- Headline 3: [text] ([char count])
- Description 1: [text] ([char count])
- Description 2: [text] ([char count])
- CTA: [button text]

## Ad Variant 2
...
```

Include character counts for every element. Flag any that exceed limits.

## Do NOT
- Write headlines that do not match the landing page. Message mismatch kills conversion.
- Use clickbait or misleading claims. High CTR with low conversion wastes budget.
- Stuff keywords unnaturally. Write for humans, optimize for algorithms second.
- Use ALL CAPS or excessive punctuation (!!!).
- Include urgency or scarcity that is not real.
- Forget to include character counts. Over-limit copy gets truncated.