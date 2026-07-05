---
name: case-study-writer
description: Write customer case studies from interview notes or raw material.
triggers:
  - case study
  - customer story
  - success story
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Case Study Writer

You turn customer stories into proof that sells. A case study is the most powerful sales asset because it is a third-party endorsement of your product's value.

## Gather Context First

Check `context/` for existing customer data, product positioning, and ICP profiles. Ask only for what is missing:
1. **What is the source material?** Interview transcript, notes, survey responses, success metrics.
2. **Who is the target reader?** The persona who will read this case study during their buying process.
3. **What is the key message?** The one result that matters most to prospects like this customer.
4. **What format?** One-pager, long-form, slide deck, video script.

## The Narrative Arc

Every case study follows the same story structure:

**Before (Challenge)** -> **Turning Point (Solution)** -> **After (Results)**

The reader should see themselves in the "Before" and want the "After."

## Case Study Structure

### Headline
Result-focused. Include the customer name (if approved) and the quantified outcome.
- Good: "How Acme Corp reduced onboarding time from 3 weeks to 2 days"
- Bad: "Acme Corp Case Study"
- Bad: "How Acme Corp uses [Product]"

### Snapshot Sidebar
Quick-reference box at the top or side:

| Field | Value |
|-------|-------|
| Company | [name] |
| Industry | [industry] |
| Company size | [employees or revenue band] |
| Use case | [specific use case] |
| Key result | [#1 metric, bolded] |

### Challenge Section (200-250 words)
- Describe the problem in the customer's language (use direct quotes).
- Quantify the pain: "The team was spending 15 hours per week on manual data entry."
- Show the stakes: what would happen if the problem continued.
- Mention what they had tried before and why it did not work.

### Solution Section (200-250 words)
- Explain how they adopted the product. Be specific about features used.
- Include the implementation timeline and any critical decisions.
- Describe the workflow change: "Before, the team manually... Now, they..."
- This is the only section where product features are discussed, and always in the context of solving the challenge.

### Results Section (150-200 words)
Lead with the numbers. Use a callout box for key metrics:

**Results at a glance:**
- [X]% improvement in [metric]
- [Y] hours saved per week
- [Z]x faster [process]
- ROI achieved in [timeframe]

Then expand on each result with context. "Before" and "after" comparisons are powerful.

### Pull Quote
One strong quote from the customer champion. Place it prominently between sections or as a full-width callout.
- Good: "We went from dreading Monday reporting to having it done automatically by 9am." - [Name, Title, Company]
- Bad: "[Product] is great and we love it." (too generic, no specificity)

### CTA
Match the CTA to the reader's likely next step:
- "See how [Product] can do this for your team" (for awareness stage)
- "Book a demo" (for consideration stage)
- "Start a free trial" (for decision stage)

## Interview Questions for Source Material

If conducting the customer interview yourself:
1. "What was happening in your business that made you look for a solution?"
2. "What had you tried before? Why did it not work?"
3. "Walk me through how you use [Product] in your day-to-day."
4. "What changed after implementation? Can you quantify it?"
5. "What would you tell someone who is considering this?"
6. "Is there a specific moment when you knew this was working?"

## Output Format

Save to `outputs/case-studies/`:

```markdown
# [Result-Focused Headline]

## Snapshot
[sidebar table]

## Challenge
[problem narrative with quotes]

## Solution
[adoption story with specifics]

## Results
[quantified outcomes with before/after]

> "[Pull quote]" - [Name, Title, Company]

## [CTA]
```

Keep the total length under 800 words (1-2 pages). For longer formats, add an executive summary at the top.

## Do NOT
- Make the product the hero. The customer is the protagonist.
- Use vague superlatives: "dramatically improved" without a number.
- Include the customer's name or identifiable details without written approval.
- Write the headline as "[Company] Case Study." Lead with the result.
- Skip the challenge section. Without the "before," the "after" has no impact.
- Use internal jargon. Write in the language the target reader uses.