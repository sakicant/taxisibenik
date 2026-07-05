---
name: social-media-calendar
description: Create a 30-day social media content calendar. Use when planning content strategy across platforms.
triggers:
  - content calendar
  - social calendar
  - plan social posts
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Social Media Calendar

Generate a strategic 30-day content calendar with specific hooks, content pillar balance, and platform-specific adaptations.

## Gather Context First

Check `context/` for existing marketing and audience data. Ask for what is missing:

1. **Target platforms** — LinkedIn, X/Twitter, Instagram, TikTok, etc.
2. **Business type** — SaaS, e-commerce, agency, personal brand, community?
3. **Target audience** — Role, industry, pain points, what they care about
4. **Content pillars** — Key topics (suggest 4 if not provided)
5. **Upcoming events** — Launches, holidays, conferences, deadlines, seasonal moments
6. **Posting frequency** — Per platform (suggest defaults if not provided)
7. **Brand voice** — Check `reference/brand-voice.md` for existing guidelines
8. **Past performance** — What types of posts have worked well before?

## Content Strategy Framework

### Content Pillar Balance
Distribute posts across 4 categories. Adjust ratios based on the business stage and goals:

| Pillar | Target % | Purpose | Post Types |
|--------|---------|---------|------------|
| Educational | 40% | Build authority and provide value | Tips, how-tos, frameworks, lessons learned, data insights |
| Social Proof | 20% | Build trust and credibility | Testimonials, case studies, milestones, user stories, before/after |
| Engagement | 20% | Build community and reach | Questions, polls, hot takes, behind-the-scenes, personal stories |
| Promotional | 20% | Drive conversions | Product features, launches, offers, CTAs, demos |

**Adjust for business stage:**
- Pre-launch: 50% Educational, 30% Engagement, 10% Social Proof, 10% Promotional
- Growth: Standard 40/20/20/20
- Mature product: 30% Educational, 25% Social Proof, 20% Engagement, 25% Promotional

### Platform-Specific Adaptation

**LinkedIn:**
- Best for: B2B, thought leadership, professional storytelling
- Post format: Text posts (1200-1500 characters), carousels (8-12 slides), short articles
- Hook style: Personal story opener, contrarian take, or surprising data point
- Best times: Tuesday-Thursday, 8-10 AM and 12-1 PM local time
- Frequency: 3-5x per week

**X/Twitter:**
- Best for: Real-time engagement, hot takes, community building
- Post format: Short text (under 280 chars), threads (5-10 tweets), quote tweets
- Hook style: Bold statement, question, or pattern interrupt
- Best times: Monday-Friday, 8 AM and 5-6 PM
- Frequency: 1-3x per day

**Instagram:**
- Best for: Visual storytelling, B2C, community
- Post format: Reels (30-90 sec), carousels (5-10 slides), stories
- Hook style: Visual hook in first 0.5 seconds, text overlay with bold claim
- Best times: Monday, Wednesday, Friday, 11 AM-1 PM
- Frequency: 3-5x per week feed, daily stories

### Hook Writing Framework
The first line of every post determines whether anyone reads the rest. Use these patterns:

1. **The Bold Claim:** "Most [audience] get [topic] wrong. Here's why."
2. **The Personal Story:** "Last week I [specific event]. Here's what I learned."
3. **The Data Hook:** "[Specific number] of [audience] are [doing X]. But [contrarian insight]."
4. **The Question:** "What's the one thing you'd change about [topic]?"
5. **The Contrarian:** "Unpopular opinion: [common practice] is killing your [metric]."
6. **The Before/After:** "6 months ago I [before]. Now I [after]. Here's the 3 things I changed."
7. **The List Tease:** "5 [things] I wish I knew about [topic] before [milestone]."

### Content Recycling Strategy
- Mark 4-6 posts as "evergreen" — reusable quarterly with minor updates
- Repurpose high-performing posts across platforms with format adaptation
- Turn long-form posts into micro-content series
- Update data-driven posts with new numbers annually

## Calendar Output Format

Save to `outputs/content-calendar.md`:

### Calendar Overview
- Period: [Date range]
- Platforms: [List]
- Total posts: [Count]
- Pillar distribution: [Actual breakdown]

### Week-by-Week Calendar

| Day | Date | Platform | Pillar | Topic | Hook (First Line) | Post Type | Assets Needed | Notes |
|-----|------|----------|--------|-------|--------------------|-----------|---------------|-------|
| Mon | Mar 3 | LinkedIn | Educational | [Topic] | "[Hook]" | Text | None | |
| Tue | Mar 4 | X | Engagement | [Topic] | "[Hook]" | Poll | None | |

### Asset Preparation List
Group all posts requiring assets (images, videos, carousels) with deadlines:

| Post Date | Platform | Asset Type | Description | Prep Deadline |
|-----------|----------|-----------|-------------|--------------|

### Evergreen Posts
List reusable posts that can fill gaps or replace underperformers.

### Measurement Plan
Which metrics to track weekly:
- Impressions and reach per post
- Engagement rate by pillar
- Click-through rate on promotional posts
- Best-performing hooks and formats

## Do NOT
- Front-load promotional content — earn the audience's attention before selling
- Post the same content across all platforms without adapting format and tone
- Plan 30 days of content without building in flexibility for real-time topics
- Write hooks that are clickbait with no payoff — the body must deliver on the hook's promise
- Schedule posts on holidays or weekends without checking if the audience is active then
- Create a calendar without flagging which posts need assets — last-minute asset creation kills consistency