---
name: objection-handler
description: Create comprehensive objection handling playbooks with categorized objections, response frameworks, evidence points, and practice scenarios. Use when preparing for sales conversations, training new reps, or updating competitive positioning.
triggers:
  - handle objection
  - objection response
  - overcome objection
  - sales objection
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Objection Handler

Turn objections from conversation-enders into conversation-deepeners. Every objection is a signal about what the buyer cares about.

## Input Required

1. **Common objections** — from CRM notes, lost deal reasons, rep feedback (check `context/` for existing lists)
2. **Product positioning** — value props, differentiators (check `reference/`)
3. **Competitive intel** — how competitors position against you
4. **Win stories** — customers who had the same objection and bought anyway
5. **Pricing structure** — to handle price objections specifically

## Objection Classification

### Step 1 — Categorize All Known Objections

| Category | Objection | Frequency | Deal Stage | Win Rate When Raised |
|----------|----------|-----------|-----------|---------------------|
| **Price** | "Too expensive" | High | Negotiation | [%] |
| **Price** | "Competitor is cheaper" | Medium | Evaluation | [%] |
| **Timing** | "Not the right time" | High | Discovery | [%] |
| **Authority** | "Need to check with my boss" | Medium | Any | [%] |
| **Need** | "We already have a solution" | Medium | Discovery | [%] |
| **Trust** | "You're too small/new" | Low | Evaluation | [%] |
| **Complexity** | "Too hard to implement" | Medium | Evaluation | [%] |

### Step 2 — Build Response Frameworks

For each objection, use the **Acknowledge → Probe → Reframe → Evidence → Advance** framework:

---

**Objection: "[Exact words the buyer uses]"**

**What it really means:** [The underlying concern behind the words]

**Acknowledge:**
> "[Validate their concern without agreeing with the premise]"

**Probe (pick the best fit):**
> - "Help me understand — what are you comparing the cost to?"
> - "When you say not the right time, what would need to change?"
> - "What does your current solution do well? Where does it fall short?"

**Reframe:**
> "[Shift the conversation from cost to value, from timing to cost of delay, from competition to fit]"

**Evidence:**
> - [Customer story: "Company X had the same concern. Here's what happened..."]
> - [Data point: "Customers in your segment see X% improvement in Y"]
> - [Comparison: "The cost of not solving this is $Z per month"]

**Advance:**
> "[Specific next step that moves the deal forward]"

---

### Step 3 — Build the Playbook

Create entries for the top 10-15 objections:

#### Price Objections

**"It's too expensive."**
- Acknowledge: "Price is always an important factor in this decision."
- Probe: "Help me understand — too expensive compared to what? Your budget, a competitor, or the expected return?"
- Reframe: The question is not whether the price is high, but whether the value exceeds the cost. Shift to ROI.
- Evidence: [Customer X saved $Y in Z months, paying for the solution N times over]
- Advance: "Would it help if I built a custom ROI model for your specific use case?"

**"Competitor X is cheaper."**
- Acknowledge: "They are. I want to be upfront about that."
- Probe: "What does their pricing include? Let's compare apples to apples."
- Reframe: Price is one input. Total cost of ownership includes implementation, training, ongoing maintenance, and switching costs.
- Evidence: [Customer who switched from competitor and the hidden costs they discovered]
- Advance: "Can I show you a side-by-side TCO comparison?"

#### Timing Objections

**"Not the right time / We have other priorities."**
- Acknowledge: "Priorities shift. I respect that."
- Probe: "What is the priority right now? And what happens to [the problem you solve] while you wait?"
- Reframe: Delay has a cost. Calculate the cost of the status quo per month.
- Evidence: [Customer who said the same thing, waited 6 months, and wished they had started sooner]
- Advance: "What if we started with a small pilot that does not compete with your other priorities?"

#### Need Objections

**"We already have a solution for that."**
- Acknowledge: "Good — it sounds like you take this seriously."
- Probe: "How well is it working? If you could change one thing about your current setup, what would it be?"
- Reframe: The question is not whether you have a solution, but whether it is the best solution for where your business is headed.
- Evidence: [Customer who switched from their previous solution and the improvement]
- Advance: "Would you be open to a 15-minute comparison? If your current tool is the right fit, I will tell you."

## Output Format

Save to `reference/objection-playbook.md`:

```markdown
# Objection Handling Playbook

## Quick Reference
| Objection | Category | Response Starter | Key Evidence |
|----------|----------|-----------------|-------------|

## Detailed Responses
[Full framework for each objection]

## Practice Scenarios
[Role-play scripts for training]
```

## Principles

- Listen to the full objection before responding. Interrupting to "handle" an objection is arguing, not selling.
- Objections are buying signals. A prospect who objects is engaged. A prospect who says nothing is already gone.
- The best objection handling is prevention. If you hear the same objection in every deal, fix the pitch, not the response.