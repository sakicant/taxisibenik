---
name: growth-loop-mapper
description: Map and evaluate the self-reinforcing growth loops in your product to identify which loops drive sustainable growth and where to invest. Use when planning growth strategy, evaluating product-market fit mechanics, or deciding between growth investments.
triggers:
  - growth loops
  - viral loop
  - flywheel
  - self-reinforcing growth
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Growth Loop Mapper

A growth loop is a closed system where the output of one cycle feeds the input of the next. Unlike funnels (which are linear and require constant top-of-funnel feeding), loops compound. The best products have at least one strong loop driving their growth.

## Phase 1 — Identify Existing Loops

Map every loop currently operating in your product. Common loop types:

### Viral Loops
User does something → other people see it → some of them sign up → they do the same thing
- Example: Shared documents, referral programs, social posts, invite mechanics

### Content Loops
Users or the product create content → search engines index it → new users find it → they create more content
- Example: User reviews, Q&A sites, template galleries, community forums

### Paid Loops
Revenue funds acquisition spend → new users generate revenue → revenue funds more acquisition
- Example: Performance marketing where LTV > CAC with enough margin to reinvest

### Product Loops
More users → better product (through data, network effects, or content) → more users
- Example: Recommendation engines, marketplaces, collaborative tools

### Sales Loops
Product usage generates signals → sales team converts signals to deals → deals generate more usage
- Example: PLG + sales assist, expansion revenue, land-and-expand

## Phase 2 — Map Each Loop

For each identified loop, document the cycle:

### Loop: [Name]
```
[Step 1: trigger/input]
    ↓
[Step 2: user action]
    ↓
[Step 3: distribution/visibility]
    ↓
[Step 4: new user acquisition]
    ↓
[Back to Step 1]
```

| Step | Conversion Rate | Volume | Bottleneck? |
|------|----------------|--------|-------------|
| Step 1 → 2 | [%] | [n/period] | |
| Step 2 → 3 | [%] | [n/period] | |
| Step 3 → 4 | [%] | [n/period] | |
| Step 4 → 1 | [%] | [n/period] | |

**Loop efficiency** = Product of all step conversion rates. A loop with 50% x 10% x 5% x 20% = 0.05% efficiency means every 2,000 users who enter produce 1 new user per cycle.

## Phase 3 — Evaluate Loop Strength

| Loop | Cycle Time | Efficiency | Volume | Compounding? | Current State |
|------|-----------|-----------|--------|-------------|---------------|
| [name] | [days/weeks] | [%] | [users/cycle] | [yes/no] | Strong/Weak/Broken |

### Compounding Test
A loop compounds if the output consistently exceeds the input needed to sustain it. If each cycle produces fewer users than the previous cycle needed to start, the loop is decaying.

### Bottleneck Identification
For each loop, which step has the lowest conversion rate? That is where improvement effort should focus.

## Phase 4 — Prioritize Investment

| Loop | Current Efficiency | Improvement Potential | Investment Required | Priority |
|------|-------------------|---------------------|--------------------|----|
| [name] | [%] | [what could improve] | [effort] | [1-5] |

**Investment principles:**
1. Fix broken loops before building new ones
2. Improve the bottleneck step in strong loops before optimizing other steps
3. Short cycle time loops compound faster — prefer them for early-stage growth
4. Paid loops are the easiest to start but the hardest to sustain
5. Product loops are the hardest to build but the most durable

## Output

Write to `outputs/growth-loops-[date].md`:

1. **Loop inventory** — all identified loops with diagrams
2. **Efficiency metrics** — conversion rates at each step
3. **Bottleneck analysis** — where each loop is weakest
4. **Investment priority** — which loops to strengthen and why
5. **Experiments** — specific tests to improve the highest-priority bottleneck

## Do NOT
- Confuse funnels with loops — a funnel is linear, a loop is circular
- Assume every product needs a viral loop — paid and content loops are valid
- Ignore loop decay — all loops weaken over time without maintenance
- Optimize efficiency before you have volume — a 5% efficient loop with 100 users per cycle is worse than a 1% efficient loop with 10,000