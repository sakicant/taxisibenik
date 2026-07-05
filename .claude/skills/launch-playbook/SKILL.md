---
name: launch-playbook
description: Create a complete launch playbook for a product, feature, or service. Use when planning any kind of market launch.
triggers:
  - launch plan
  - product launch
  - launch go to market
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Launch Playbook

Build a structured launch plan with a week-by-week timeline, specific deliverables, and a minute-by-minute launch day checklist.

## Gather Context First

Check `context/` for existing product and audience data. Ask for what is missing:

1. **What is launching?** — New product, major feature, pricing change, rebrand?
2. **Launch date** — Fixed or flexible?
3. **Target audience** — Who needs to know about this? ICP, existing customers, general market?
4. **Launch goal** — Signups, revenue, press coverage, community growth? Pick one primary metric.
5. **Budget** — Paid promotion budget, or organic only?
6. **Team** — Solo founder, small team, or cross-functional launch team?
7. **Channels** — Email list size, social following, community size, press contacts?
8. **Risk tolerance** — Soft launch (low key, iterate) or big bang (maximum attention)?

## Launch Tiers

| Tier | Examples | Lead Time | Channels |
|------|---------|-----------|----------|
| **Tier 1 — Major** | New product, rebrand | 8+ weeks | All channels + press + partners |
| **Tier 2 — Significant** | Major feature, pricing change | 4-6 weeks | Email, social, blog, community |
| **Tier 3 — Incremental** | Minor feature, content launch | 1-2 weeks | Blog, changelog, social |

Misclassifying the tier is the most common launch mistake.

## The Attention Sine Wave

Pre-launch (40% of effort): build anticipation. Launch day (20%): execute and engage. Post-launch (40%): capture testimonials, retarget, build momentum. Most teams pour everything into the peak and let the wave crash.

## Launch Framework: The 3-Phase Model

### Phase 1: Pre-Launch (Weeks -4 to -1)

#### Week -4: Foundation
- **Define success metrics** — What number, measured on what date, means "this launch worked"?
  - Primary: [specific metric and target]
  - Secondary: [2-3 supporting metrics]
- **Audience segmentation** — Who gets different messages?
  - Existing customers (retention/upsell message)
  - Email subscribers (insider/early access message)
  - Cold audience (awareness/problem message)
- **Asset inventory** — What exists and what needs to be created?
  - Landing page or updated product page
  - Announcement blog post
  - Email sequences (teaser, launch day, follow-up)
  - Social content (teaser series, launch day posts, post-launch proof)
  - Visual assets (screenshots, demos, graphics)
  - Press kit (if media outreach is planned)

#### Week -3: Build
- **Create landing page** with email capture for early access
- **Draft announcement content** across all channels
- **Build email sequences** — Teaser (2 emails), launch day (1 email), follow-up (2 emails)
- **Prepare social teaser series** — 3-5 posts that build anticipation without revealing everything
- **Record demo or walkthrough** if the product is visual

#### Week -2: Warm Up
- **Send first teaser** — Hint at what is coming without full details
- **Start social teasers** — 2-3 posts per week with behind-the-scenes, countdowns, or sneak peeks
- **Reach out to partners/influencers** — Give them early access and ask for launch-day amplification
- **Brief the team** — Everyone should know the launch messaging, FAQs, and their role
- **Set up tracking** — UTM links, analytics dashboards, conversion tracking

#### Week -1: Final Prep
- **Send second teaser** — More details, build excitement
- **Finalize all assets** — Landing page live, emails scheduled, social queued
- **Test everything** — Click every link, fill every form, test every flow
- **Prepare contingency plans:**
  - If site goes down: communication template ready
  - If negative feedback: response framework ready
  - If low engagement: backup promotion plan ready
- **Schedule launch day communications** — Everything except time-sensitive posts

### Phase 2: Launch Day/Week

#### Launch Day Checklist
- [ ] **Morning — Announce:** Post on primary channel, follow with secondary channels within 1-2 hours, monitor and respond in real-time
- [ ] **Midday — Amplify:** Share on communities/forums/Product Hunt, activate partners and influencers, engage with every mention
- [ ] **Afternoon — Sustain:** Send launch email to full list, post second-round social content (new angle or testimonial), check for technical issues
- [ ] **Evening — Wrap:** Post day-1 recap with milestones, address issues publicly, draft next-day content based on what resonated
- [ ] **Days 2-5 — Follow through:** Day 2 testimonial, Day 3 deep-dive content, Day 4 FAQ response, Day 5 social proof roundup
- [ ] **Days 6-7 — Wind down:** Lower intensity, shift to individual outreach and relationship building

### Phase 3: Post-Launch (Weeks +1 to +3)

#### Week +1: Capture
- **Collect feedback** — Survey early users, monitor support channels
- **Gather testimonials** — Ask happy users for quotes, screenshots, case studies
- **Performance review** — Compare actual metrics to targets
- **Content:** "What we learned from launch" post, user spotlight

#### Week +2: Optimize
- **Retarget non-converters** — Follow-up email to people who clicked but did not sign up
- **Address objections** — Create content that tackles the most common reasons people did not convert
- **Iterate on messaging** — Update landing page based on what resonated during launch
- **Content:** How-to guides, comparison content, FAQ page

#### Week +3: Systematize
- **Document lessons learned** — What worked, what did not, what to change next time
- **Build ongoing content pipeline** — The launch generated attention; now maintain it
- **Set up nurture sequences** — For leads who entered during launch but have not converted
- **Plan the next milestone** — Keep momentum with feature updates or community events

## Output Format

Save to `outputs/launch-playbook.md`:

### Launch Overview
- Product/feature: [name]
- Launch date: [date]
- Primary goal: [metric and target]
- Secondary goals: [2-3 supporting metrics]

### Week-by-Week Timeline

For each week:
| Activity | Owner | Deadline | Status | Notes |
|----------|-------|----------|--------|-------|

### Launch Day Checklist
Sequential, minute-by-minute:
- [ ] [Time] — [Action] — [Owner]

### Asset Tracker
| Asset | Status | Deadline | Owner | Link |
|-------|--------|----------|-------|------|

### Risk Register
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|

### Post-Launch Metrics Dashboard
What to measure weekly for 4 weeks after launch.

## Do NOT
- Launch without a clear success metric — you cannot evaluate a launch without a number
- Plan launch day without contingency plans for failure modes
- Focus all energy on launch day and ignore the follow-through — most conversions happen in the weeks after
- Skip the teaser phase — warm audiences convert 3-5x better than cold audiences
- Schedule every post and walk away — launch day requires active engagement and real-time responses
- Plan a "big bang" launch for an unvalidated product — soft launch first, then amplify what works

## Succeeds when
- The launch has one primary metric with a target number and a date
- Sales, CS, and support know what is launching and how to talk about it
- Tier classification matches actual scope so effort is not over- or underspent
- The post-launch phase is staffed and planned, not improvised
- Contingencies exist for low engagement, site failure, and negative feedback

## Fails when
- The launch date is set before assets and enablement are ready
- Success is measured in impressions or press hits instead of pipeline or adoption
- The team peaks on launch day and lets the wave crash
- The audience is "everyone" instead of a segmented primary target