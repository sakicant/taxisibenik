---
name: multi-source-research-hub
description: Research a topic thoroughly by dispatching agents to search different sources in parallel, then synthesizing the findings. Use for competitive research, market analysis, or any topic needing multiple perspectives.
triggers:
  - deep research
  - multi-source research
  - research from multiple angles
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Multi-Source Research Hub

You research topics by dispatching parallel agents to gather information from different angles, then synthesizing everything into a single, sourced, confidence-rated report.

## When to Use

This skill is for research needing breadth that cannot be answered from a single source:
- Competitive intelligence (positioning, pricing, operations)
- Market analysis (size, trends, players, opportunities)
- Technology evaluation (features, limitations, community)
- Industry trends (what is changing, who is leading)
- Due diligence (background on a company or product)

## Process: The 5-Step Research Method

### Step 1: Define the Research Question
Before dispatching agents, clarify:
- **Primary question:** What specifically are we trying to learn?
- **Decision context:** What decision will this inform?
- **Scope boundaries:** What is in and out of scope?
- **Depth required:** Surface overview or deep analysis?
- **Recency:** How current must sources be?

### Step 2: Identify Research Dimensions
Identify 3-5 independent angles that collectively cover the topic.

**Common dimension sets:**

For a competitor:
1. Company overview (founding, funding, team, stage)
2. Product analysis (features, pricing, positioning)
3. Customer sentiment (reviews, complaints, praise)
4. Content and marketing strategy
5. Technical architecture (stack, API, docs)

For a market:
1. Market size and growth (TAM, SAM, growth rate)
2. Key players and market share
3. Customer pain points and unmet needs
4. Technology trends
5. Regulatory and macro factors

For a technology:
1. Core capabilities and limitations
2. Ecosystem (integrations, plugins, community)
3. Community health (GitHub activity, forums)
4. Enterprise readiness (security, compliance)
5. Competitive alternatives

### Step 3: Dispatch Research Agents
Launch one agent per dimension using the Agent tool. Each brief must include:

- **Dimension:** Name
- **Research question:** What to find out
- **Sources to check:** Specific places to look
- **Output format:** Key findings (5-10 bullets with sources), confidence rating, surprises, gaps

**Source guidance:**
- Use WebSearch for current info, WebFetch for detailed pages
- Prioritize primary sources over secondary
- For sentiment: G2, Capterra, Reddit, Hacker News, Twitter/X
- Record the source URL for every finding

### Step 4: Quality Control
Before synthesizing, evaluate each output:
- **Source quality** — Credible or just blog posts?
- **Recency** — Flag anything older than 12 months
- **Consistency** — Do agents agree? Note contradictions.
- **Completeness** — Any gaps?

### Step 5: Synthesis
Merge findings into a coherent report:
1. Extract the top 5 findings for the decision context
2. Identify themes across dimensions
3. Resolve contradictions by comparing source quality
4. Rate overall confidence per finding
5. Highlight gaps needing more research

## Output Format

Save to `outputs/research-[topic].md`:

### Research Summary
One paragraph answering the primary question.

### Key Findings
5-10 bullets ranked by importance, each with confidence and source.

### Detailed Analysis
One section per dimension with full findings.

### Source Quality Assessment

| Source | Type | Recency | Reliability |
|--------|------|---------|-------------|

### Contradictions
Where sources disagreed and recommended interpretation.

### Research Gaps
What could not be determined and what additional research would help.

### Recommended Next Steps
Actions or decisions this research supports.

## Do NOT
- Present findings without sources
- Treat all sources as equally reliable
- Ignore contradictions — they are often the most interesting findings
- Synthesize by concatenation — tell a story, not list facts
- Skip confidence ratings
- Research beyond the defined scope