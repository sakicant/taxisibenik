---
name: connections-optimizer
description: Analyze a professional network to identify outreach opportunities, warm introduction paths, and engagement patterns. Use when planning outreach campaigns, building partnerships, or growing a professional network strategically.
triggers:
  - optimize connections
  - network analysis
  - outreach strategy
  - warm paths
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Connections Optimizer

Analyze a professional network to find the highest-value outreach opportunities and build a prioritized engagement plan.

## Phase 1 — Map the Network

Gather available information about the network:

1. **Connection list.** Names, titles, companies, and connection date.
2. **Engagement history.** Who has liked, commented, or shared your content recently?
3. **Shared context.** Mutual connections, shared groups, past interactions.
4. **Company data.** Industry, size, recent news, funding, hiring signals.

Sources to check:
- LinkedIn connections and activity
- Email contacts and recent threads
- CRM data if available
- Event attendee lists
- Community memberships (Discord, Slack, forums)

## Phase 2 — Score Connections

Rate each connection on three dimensions:

### Relevance (1-5)
How closely does this person align with your current goals?
- **5:** Direct decision-maker at a target company or ideal collaborator
- **4:** Adjacent role with influence or referral power
- **3:** Same industry, some overlap in interests
- **2:** Tangential connection, unclear alignment
- **1:** No obvious relevance to current goals

### Warmth (1-5)
How strong is the existing relationship?
- **5:** Regular contact, mutual engagement, past collaboration
- **4:** Occasional interaction, mutual connection, shared experience
- **3:** Connected but minimal interaction
- **2:** One-way connection, no prior conversation
- **1:** No prior contact

### Timing (1-5)
Is there a natural reason to reach out now?
- **5:** They just posted about a relevant topic, changed roles, or announced something
- **4:** Shared event coming up, mutual connection made an intro, seasonal relevance
- **3:** No specific trigger but not awkward
- **2:** Bad timing (they just started a new role, on leave, etc.)
- **1:** No conceivable reason to reach out

**Priority Score = Relevance + Warmth + Timing** (max 15)

## Phase 3 — Identify Warm Paths

For high-relevance but low-warmth connections, find warm introduction paths:

1. **Mutual connections.** Who do you both know? Who is most likely to make an intro?
2. **Shared communities.** Are you in the same groups, forums, or communities?
3. **Content engagement.** Have they engaged with your content or vice versa?
4. **Events.** Will you both attend an upcoming event?
5. **Alumni networks.** Same school, past employer, or professional organization?

Map the shortest path from you to the target:
`You → [Mutual Connection] → [Target]`

## Phase 4 — Craft Outreach Messages

### Message Framework

For each outreach, include:
1. **Connection point.** Why you are reaching out to them specifically (not a generic blast).
2. **Value offer.** What you bring to them, not what you want from them.
3. **Specific ask.** One clear, low-effort action they can take.
4. **Easy out.** Make it comfortable to decline.

### Templates by Warmth Level

**Warm (score 4-5):**
Keep it casual and direct. Reference shared context. One paragraph max.

**Medium (score 3):**
Reference the specific connection point. Offer value first. Ask for a small commitment (15-minute call, opinion on something).

**Cold (score 1-2):**
Lead with something you genuinely appreciate about their work. Offer something specific and useful. Ask for nothing in the first message — just open the door.

### Rules for All Messages
- Personalize every message. Reference something specific about them.
- Keep it under 100 words for initial outreach.
- One ask per message. Never stack requests.
- No attachments or links in the first message.
- Follow up once after 5-7 days. Do not follow up more than twice.

## Phase 5 — Build the Outreach Plan

### Weekly Cadence
- **Monday:** Review and prioritize this week's outreach targets (5-10 people)
- **Tuesday-Thursday:** Send outreach messages (2-3 per day max for quality)
- **Friday:** Follow up on unanswered messages from last week, log results

### Track Results

| Name | Score | Outreach Date | Channel | Response | Next Step |
|------|-------|---------------|---------|----------|-----------|

## Output

Write the analysis and plan to `outputs/connections-plan-[date].md`:

1. **Network summary.** Total connections, distribution by relevance/warmth.
2. **Top 20 targets.** Scored and ranked with warm paths identified.
3. **Outreach messages.** Drafted messages for the top 10.
4. **Weekly plan.** First two weeks of outreach mapped out.
5. **Warm path map.** Visual representation of key introduction chains.

## Do NOT
- Send mass identical messages — every outreach must be personalized
- Reach out to more than 3 people per day — quality over quantity
- Ask for favors in the first message — offer value first
- Ignore low-warmth connections entirely — some of the best opportunities are with people you do not know yet
- Skip tracking — without data on what works, the strategy cannot improve