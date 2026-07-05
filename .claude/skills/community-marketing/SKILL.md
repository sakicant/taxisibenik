---
name: community-marketing
description: Design, launch, and grow a community that creates real value for members and drives measurable business outcomes. Covers platform choice, programming, moderation, ambassador programs, and the business case. Use when user mentions community strategy, Discord/Slack community, community-led growth, ambassadors, or word-of-mouth.
triggers:
  - build a community
  - community strategy
  - discord community
  - slack community
  - community-led growth
  - ambassador program
  - grow our community
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Community Marketing

Help the user design, launch, and grow a community. Communities are slow to build, easy to break, and the highest-loyalty audience a brand has when they work.

## Gather context

Ask if not provided:

1. **Product or brand** — what problem does it solve, who uses it.
2. **Community platform(s)** — Discord, Slack, Circle, Reddit, Facebook Groups, forum, owned platform.
3. **Stage** — pre-launch, 0-100 members, 100-1k, scaling, established.
4. **Primary goal** — retention, activation, word-of-mouth, support deflection, product feedback, revenue.
5. **Ideal community member** — role, motivation, what they hope to get from joining.
6. **Resources** — who's running it (full-time community manager, founder, volunteer mods).

## Platform choice

| Platform | Best for | Watch for |
|---|---|---|
| Discord | Real-time chat, casual culture, voice channels, dev-leaning audiences | Hard to search; messages disappear into the firehose |
| Slack | Professional audiences, async-friendly, smaller groups | Free tier limits message history |
| Circle | Course-style, structured discussions, paid communities | Requires per-member spend |
| Reddit | Public discoverability, search-friendly | Less control, brand caution |
| Forum (Discourse, custom) | SEO + persistence, technical audiences | Higher setup cost, slower momentum |
| Owned platform (in-app) | Direct attribution to product | Most expensive to build |

Pick where your audience already hangs out. Don't make them learn a new tool.

## Pre-launch (before opening doors)

- Define the **community charter** — what this is, what it's not, who it's for, in 100 words.
- Set **3-5 channels max** at launch. Add more only when activity demands it.
- Write **welcome messages, channel descriptions, and rules**. Pin them.
- Recruit **5-10 founding members** before opening publicly. Empty rooms feel dead.
- Decide **moderation**: who, when, how. Document it before you need it.

## Programming (what happens inside)

Communities die from inactivity, not from drama. Schedule recurring activity:

- **Weekly cadence**: weekly thread (e.g., "What are you building this week?"), weekly digest (highlight 3-5 great posts).
- **Monthly cadence**: AMA, expert guest, member spotlight.
- **Triggered**: respond to every new-member intro within 24h.
- **Surprise + delight**: occasional swag drop, beta access, early features for active members.

## Ambassador program (when scaling)

Once the community has 200+ active members, formalize an ambassador track:
- Tier 1: helpful members (free swag, recognition).
- Tier 2: regular contributors (early access, listed on site).
- Tier 3: ambassadors (paid stipend or revenue share, official title, monthly office hours with founders).

Don't formalize too early — it kills organic energy.

## Metrics

Track these monthly:
- **Active member ratio** — how many members posted/reacted in the last 30 days. Target: 20%+.
- **New-member onboarding rate** — % of joiners who post in first week. Target: 30%+.
- **Time to first response** — when someone asks a question, how long until anyone (mod or peer) answers. Target: under 4h.
- **Net member growth** — joiners minus leavers per month.
- **Business-tied metric** — referrals, NPS uplift, retention delta for community members vs non-members.

## Output format

Save to `outputs/community-strategy.md` with:
- Platform recommendation with reasoning.
- Community charter (the 100-word version).
- Channel structure with descriptions.
- 90-day programming calendar.
- Moderation policy.
- Metrics dashboard template.

## Cross-references

For Discord-specific channel setup and bot config, see `discord-server-setup` if it exists. For converting community signal into product changes, see `voc-synthesis` and `customer-feedback-orchestration` (when added). For brand voice in community responses, see `brand-voice-builder`.
