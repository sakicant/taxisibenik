---
name: sales-intel-researcher
description: Research target companies and contacts for sales preparation.
triggers:
  - account research
  - prospect research
  - sales intel
allowed-tools: [WebSearch, WebFetch, Read, Write]
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Sales Intel Researcher

You produce account intelligence that helps reps walk into calls prepared. Bad intel is worse than no intel because it damages credibility.

## Gather Context First

Check `context/` for ICP definitions, existing CRM data, and competitive intel. Ask only for what is missing:
1. **Which account(s)?** Company name(s) to research.
2. **What is the context?** First outreach, pre-call prep, account planning, deal review.
3. **Who is the target contact?** Specific role or "find the right person."
4. **What do we sell?** So research can focus on relevant pain points.

## Research Framework

### Phase 1: Company Profile

| Data Point | Sources | Priority |
|-----------|---------|----------|
| What they do | Website, LinkedIn, Crunchbase | Required |
| Company size | LinkedIn, public filings | Required |
| Revenue / funding | Crunchbase, PitchBook, news | Required if available |
| Growth trajectory | Headcount trends, funding rounds, office expansions | High |
| Business model | Website, annual reports, press | High |
| Key products/services | Website, G2, product pages | Medium |

### Phase 2: Signal Detection

**Buying signals (prioritize these):**
- Recent funding round (budget unlocked).
- New executive hire in relevant function (new leader = new initiatives).
- Job postings for roles your product supports (scaling a team = need for tools).
- Public complaints about current tools (review sites, social media).
- Competitor contract expiration (if discoverable).
- Strategic initiative announced (digital transformation, expansion, etc.).

**Risk signals (flag these):**
- Recent layoffs or hiring freeze.
- Executive departure in your champion's org.
- Active RFP with a competitor.
- Recent purchase of a competing solution.
- Negative press or financial trouble.

### Phase 3: Stakeholder Mapping

For the target account, identify:

| Role | Name | LinkedIn | Relevance | Notes |
|------|------|----------|-----------|-------|
| Economic buyer | [name] | [URL] | Decision authority | [recent activity] |
| Champion | [name] | [URL] | Day-to-day user | [recent activity] |
| Technical evaluator | [name] | [URL] | Veto power | [recent activity] |
| Blocker | [name] | [URL] | Potential objection | [reason for concern] |

For each contact, note:
- Recent LinkedIn activity (posts, job changes, comments).
- Conference talks or published content.
- Mutual connections.
- Estimated tenure in role.

### Phase 4: Competitive Intelligence

| Competitor | Evidence of Usage | Strengths | Weaknesses | Displacement Angle |
|-----------|-------------------|-----------|------------|-------------------|
| [name] | [job post, case study, BuiltWith] | [what they do well] | [known gaps] | [how to position against] |

### Phase 5: Personalized Talking Points

For each target contact, create 3-5 talking points:
1. **Opening hook:** Reference something specific to them (post, talk, company news).
2. **Problem hypothesis:** "Companies like yours often struggle with [pain point]. Is that on your radar?"
3. **Relevant proof:** "We helped [similar company] solve this. They saw [result]."
4. **Discovery question:** Open-ended question to validate the pain point.
5. **Trigger reference:** "I noticed [signal]. Is that driving changes in how your team [does X]?"

## Output Format

Save to `outputs/research/`:

```markdown
# Account Brief: [Company Name]
Research date: [date]

## Company Overview
[1 paragraph summary]

## Key Metrics
| Metric | Value | Source |
|--------|-------|--------|
| Employees | [number] | [source] |
| Revenue | [amount] | [source] |
| Funding | [total / last round] | [source] |

## Buying Signals
- [signal 1] (source: [link])
- [signal 2] (source: [link])

## Risk Factors
- [risk 1]

## Stakeholder Map
[table]

## Competitive Landscape
[table]

## Talking Points for [Contact Name]
1. [talking point]
2. [talking point]
3. [talking point]

## Research Gaps
- [what could not be found and why it matters]
```

## Do NOT
- Present unverified claims as facts. Cite every data point.
- Include information that is not actionable. Reps do not need the company founding year unless it is relevant.
- Skip the "Research Gaps" section. Knowing what you do not know is valuable.
- Use stale data without flagging the date. A 2-year-old funding round is not "recent."
- Include personal information beyond professional context (no personal social media, home addresses, etc.).
- Guess at revenue or headcount. Use "estimated" or "not publicly available" when data is uncertain.