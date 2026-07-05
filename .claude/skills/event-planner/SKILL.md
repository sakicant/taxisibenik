---
name: event-planner
description: Plan events, conferences, and workshops with timelines and logistics.
triggers:
  - plan event
  - event planning
  - conference prep
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Event Planner

Plan events with clear goals, detailed logistics, and contingency plans so nothing falls through the cracks.

## Phase 1 — Event Strategy

Before any logistics, define the strategic foundation:

1. **Primary goal** — Choose ONE: lead generation, brand awareness, customer retention, team building, education, partnership development
2. **Success metrics** — Define measurable outcomes before planning:
   - Lead gen: number of qualified leads captured, cost per lead
   - Brand: media mentions, social reach, attendee sentiment
   - Retention: NPS delta, renewal rate impact
   - Education: knowledge assessment scores, attendee satisfaction
3. **Audience profile** — Who are they, what do they expect, what would make them say "this was worth my time"?
4. **Format decision matrix:**

| Format | Best for | Typical size | Lead time |
|--------|----------|-------------|-----------|
| Webinar | Education, thought leadership | 50-500 | 3-4 weeks |
| Workshop | Skill-building, deep engagement | 10-40 | 4-6 weeks |
| Meetup | Community, networking | 20-100 | 2-4 weeks |
| Conference | Brand, lead gen, partnerships | 100-5000 | 3-6 months |
| Executive dinner | Relationship building | 8-20 | 4-6 weeks |
| Trade show booth | Lead gen, brand visibility | N/A (show-dependent) | 2-4 months |

## Phase 2 — Budget Planning

Build a line-item budget with contingency:

| Category | Line Item | Estimated Cost | Actual Cost | Notes |
|----------|----------|---------------|-------------|-------|
| Venue | Rental, A/V, insurance | | | |
| Catering | Food, drinks, dietary options | | | |
| Content | Speaker fees, materials, printing | | | |
| Promotion | Ads, email, design | | | |
| Logistics | Travel, accommodation, shipping | | | |
| Staff | On-site team, contractors | | | |
| Swag | Branded items, gifts | | | |
| **Contingency** | **15-20% of total** | | | |
| **Total** | | | | |

**Budget rule:** Allocate 40% to the attendee experience (venue, food, content), 25% to promotion, 20% to logistics, 15% contingency.

## Phase 3 — Timeline (Countdown)

### T-8 weeks: Foundation
- [ ] Venue confirmed and deposit paid
- [ ] Budget approved
- [ ] Speaker/presenter commitments secured
- [ ] Registration page live

### T-6 weeks: Promotion launch
- [ ] Email invitations sent (first wave)
- [ ] Social media campaign started
- [ ] Partner co-promotion agreements in place

### T-4 weeks: Content lock
- [ ] Agenda finalized
- [ ] Presentation decks in review
- [ ] Catering order placed (with dietary accommodations)
- [ ] A/V requirements confirmed

### T-2 weeks: Logistics
- [ ] Registration reminder sent
- [ ] Attendee materials printed/prepared
- [ ] Run-of-show document completed (minute-by-minute)
- [ ] Backup plans documented for critical elements

### T-1 week: Final prep
- [ ] Speaker rehearsals completed
- [ ] Badge printing / check-in system tested
- [ ] Emergency contact sheet distributed to all staff
- [ ] Weather/venue backup confirmed (if outdoor)

### Day-of: Execution
- [ ] Venue walkthrough (arrive 2 hours early minimum)
- [ ] A/V soundcheck with actual equipment
- [ ] Registration desk staffed 30 min before start
- [ ] Photography/video recording arranged
- [ ] Lead capture mechanism tested (app, QR codes, badge scans)
- [ ] Social media live coverage assigned

## Phase 4 — Follow-Up (within 48 hours)

1. **Thank-you email** to all attendees within 24 hours with: recap, key resources, next action
2. **Lead routing** — Qualified leads distributed to sales within 48 hours with context notes
3. **Content repurposing** — Photos, recordings, and quotes packaged for social/blog within 1 week
4. **Attendee survey** — Send within 24 hours (response rate drops 50% after 48 hours)
5. **Team debrief** — Schedule within 1 week. Cover: what worked, what didn't, budget vs. actual, metric results

## Output Format

Save to `outputs/event-plan-[event-slug].md` with:

- Event brief (goal, audience, format, date, venue)
- Budget spreadsheet
- Timeline checklist
- Run-of-show document
- Promotion plan
- Follow-up plan

## Do NOT
- Plan an event without a measurable success metric defined in advance
- Skip the contingency budget — something always goes wrong
- Send a single promotion email and hope for registrations — plan 3-4 touchpoints minimum
- Wait more than 48 hours for lead follow-up — leads go cold fast
- Skip the post-event debrief — the learning is as valuable as the event