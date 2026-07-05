---
name: growth-ideas-library
description: Generate channel-relevant marketing ideas for SaaS products based on stage, audience, and resources. Use when stuck on growth, brainstorming a campaign, or evaluating new tactics. For specific channel execution, see paid-ads, email-sequence-builder, social-media-writer.
triggers:
  - marketing ideas
  - growth ideas
  - i'm stuck on marketing
  - brainstorm marketing
  - what should i try
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Growth Ideas Library

A working library of marketing tactics organized by category and stage. Use it to suggest 3-5 ideas that match the user's situation, not a generic list.

## Gather Context First

Before suggesting anything, get:

1. **Product** — what it does, who pays, price point
2. **Stage** — pre-launch, beta, post-launch, scaling, plateau
3. **Audience** — who, where they hang out, what they read
4. **Resources** — solo founder, marketing team, paid budget, time
5. **What's been tried** — don't suggest tactics already burned

If the user can't answer, ask. Generic ideas waste their time.

## Stage → Tactics Matrix

Match tactics to stage. Wrong-stage tactics fail loudly.

### Pre-launch (no users yet)
- **Build in public** — daily progress posts on X/LinkedIn
- **Waitlist with content unlock** — gate access behind a useful resource
- **Founder-led DMs** — 50 personalized outreach messages a day
- **Niche community presence** — answer questions in 2-3 communities for 4 weeks before mentioning the product
- **Lighthouse customer hunt** — handpick 5 ideal users, do whatever it takes to onboard them

### Beta (first 10-100 users)
- **Onboarding calls** — 30-min calls with every new user; transcribe for insights
- **Reverse testimonial harvest** — paste user quotes from DMs into a quotes doc weekly
- **Launch on niche channels** — wherever the target audience already gathers (founder communities, role-specific subreddits, vertical newsletters)
- **Comparison content** — "[Your tool] vs [established competitor]" articles
- **Referral mechanics** — give beta users invite codes to share

### Post-launch (100-1000 users)
- **Discovery-platform launch** — needs 20+ supporters lined up before launch day
- **SEO foundation** — programmatic pages for "[role] + [pain]" queries
- **Lifecycle email** — onboarding, activation, expansion sequences
- **Partner integrations** — embed in tools your users already use
- **Case studies** — turn the best 3 user stories into long-form content

### Scaling (1000+ users)
- **Paid acquisition** — search ads on intent keywords, professional-network ads for B2B
- **Content engine** — 2-4 long-form pieces a month with distribution
- **Sales motion** — outbound to enterprise accounts if pricing supports it
- **Community** — a chat platform with weekly programming
- **Affiliate program** — only after referral data is clean

### Plateau (growth slowing)
- **Activation diagnosis** — instrument the funnel, find the leak
- **ICP refinement** — pick the cohort that retains best, double down
- **Pricing experiment** — most plateaus are pricing problems disguised as growth problems
- **New positioning angle** — same product, different frame
- **Adjacent audience expansion** — not new channel, new persona

## Category Quick Reference

If the user's stuck, pick from these categories before going specific:

| Category | When to suggest | Example tactics |
|----------|-----------------|-----------------|
| Content + SEO | Long-time horizon, low budget | Programmatic SEO, glossary, comparison pages |
| Community | Audience clusters in one place | Owned chat space, niche forums, partner newsletters |
| Founder-led | Pre-launch or B2B SaaS | Build in public, podcast tours, DMs |
| Paid | Have budget + activation works | Search-intent ads, professional-network ads, retargeting |
| Product-led | Self-serve product | Free tools, freemium, public APIs |
| Partnerships | Have logo equity | Co-marketing, integrations, referral deals |
| Events | Expensive but high-trust | Webinars, conferences, dinners |

## Suggestion Format

When proposing ideas, output:

```
## Idea: [name]

**Why this fits:** [1 sentence tying it to the user's stage and resources]
**Effort:** [hours/week, time horizon]
**Expected outcome:** [signups, leads, brand, retention]
**First step:** [the smallest action they can take this week]
**Watch out for:** [the failure mode of this tactic]
```

Suggest 3-5 ideas, ranked by fit. Then ask which one they want to develop into a plan.

## Do NOT

- Suggest tactics from the wrong stage — paid ads to a pre-launch founder is malpractice
- Pile 20 ideas on the user — pick 3-5 that match their context
- Skip the resource question — a solo founder and a marketing team need different ideas
- Suggest something they've already tried — ask first
- Promise specific outcomes — frame ideas as bets, not guarantees