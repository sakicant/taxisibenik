---
name: email-sequence-builder
description: Build email sequences for welcome, nurture, launch, or re-engagement flows. Use when designing automated email campaigns.
triggers:
  - email sequence
  - drip campaign
  - email funnel
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Email Sequence Builder

Design complete email sequences with strategic timing, tested subject line patterns, and conversion-optimized body structures.

## Gather Context First

Check `context/` and `reference/` for existing audience and voice data. Ask for what is missing:

1. **Sequence type** — Welcome, nurture, launch, re-engagement, onboarding, or post-purchase?
2. **Audience** — Who receives these? Role, awareness level, relationship stage
3. **Goal** — What should the complete sequence achieve? (Activation, purchase, upgrade, retention)
4. **Brand voice** — Check `reference/brand-voice.md` for tone guidelines
5. **Product/service** — What are we selling or promoting?
6. **Email tool** — Mailchimp, ConvertKit, Loops, HubSpot, custom?
7. **Current data** — Open rates, click rates, unsubscribe rates if available

## Sequence Types and Strategy

### Welcome Sequence (4-6 emails over 14 days)
**Goal:** Transform a new subscriber into an engaged user or buyer.

Recommended arc:
1. **Instant delivery** — Send within 5 minutes. Deliver what they signed up for.
2. **Quick win** (Day 2) — Teach something useful they can apply today.
3. **Story/credibility** (Day 4) — Origin story or customer success story.
4. **Deeper value** (Day 7) — Substantial resource or framework.
5. **Soft CTA** (Day 10) — Introduce your product as the natural next step.
6. **Direct CTA** (Day 14) — Clear offer with a specific reason to act now.

### Nurture Sequence (6-8 emails over 30-45 days)
**Goal:** Keep leads warm until they are ready to buy.

Content mix: 50% educational, 25% social proof, 25% product-related.

### Launch Sequence (5-7 emails over 10-14 days)
**Goal:** Drive conversions around a specific event or release.

Arc: Teaser (Day -7) > Announcement (Day 0) > Deep dive (+2) > Social proof (+4) > Objection buster (+7) > Urgency (+10) > Last call (+12).

### Re-engagement Sequence (3-4 emails over 14 days)
**Goal:** Win back inactive subscribers. Escalate from gentle to breakup.

1. **Reminder** (Day 0) — What have they missed?
2. **Incentive** (Day 5) — Discount, free resource, exclusive content.
3. **Feedback** (Day 10) — "What changed?"
4. **Breakup** (Day 14) — "Should we stop emailing you?"

## Email Structure Template

For each email provide:
- **Send timing:** Day X or hours/days after trigger
- **Segment:** All subscribers / active only / specific segment
- **Subject line:** Primary + A/B variant
- **Preview text:** 40-90 character snippet
- **Goal:** What this email should accomplish

**Body outline:**
1. **Opening hook** (1-2 sentences) — About the reader, not about you
2. **Main content** (3-5 paragraphs) — The value, story, or information
3. **Transition to CTA** (1 sentence)
4. **CTA** (1 clear action)
5. **P.S.** (optional) — Only if it adds a different angle

## Writing Rules

### Subject Lines
- Under 50 characters. Specific beats clever.
- Patterns that work: numbers, questions, personalization, curiosity gaps
- Avoid: ALL CAPS, excessive emoji, misleading promises

### Body Copy
- First sentence about the reader, never the sender
- One CTA per email. First-person CTAs convert 90% better ("Start my trial" vs "Start your trial")
- Paragraphs 2-3 sentences max. Under 200 words for triggered emails.
- Plain text outperforms HTML for most B2B audiences

### Copywriting Frameworks (use one per email)
- **BAB (Before-After-Bridge):** Current state → improved state → product as the bridge. Best for emotional pain.
- **FAB (Features-Advantages-Benefits):** Feature → advantage → personal benefit. Best for logical buyers.
- **PAS (Problem-Agitate-Solve):** Name the problem → agitate → present solution. Best as a final push.
- **4Ps (Promise-Picture-Proof-Push):** Promise → paint picture → prove with data → push to action. Best for urgency.

### Behavioral Triggers (outperform time-based: 40-50% open rates vs 23-30%)
| Trigger | Signal | Action |
|---------|--------|--------|
| **Limit approaching** | 80% of free tier | Upgrade nudge with usage context |
| **Feature gate** | User tries paid feature | Show what they'd unlock |
| **Milestone** | User hits success metric | Celebrate + suggest next level |
| **Engagement drop** | No login 7+ days | Re-engagement trigger |
| **Expansion signal** | Multiple users same domain | Suggest team plan |

### Suppression Rules
Every sequence needs: entry criteria, exit criteria (purchased, unsubscribed, reached goal), suppression (don't send if support ticket in 48h or in higher-priority sequence), and re-entry cooldown (30 day minimum).

## Output Format

Save to `outputs/email-sequence-[type].md`:

| # | Name | Trigger/Timing | Framework | Subject | Goal | CTA |
|---|------|---------------|-----------|---------|------|-----|

Full spec per email: trigger, segment, subject + A/B variant, preview text, body outline, framework used.

## Do NOT
- Include multiple CTAs in a single email
- Open any email with "Hi, we are [company]"
- Use fake urgency or countdown timers that reset
- Send more than one email per day in any sequence
- Write a sequence without defining suppression and exit rules
- Default to time-based when behavioral triggers are available