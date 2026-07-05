---
name: copy-analyzer
description: Analyze marketing copy for effectiveness and suggest improvements. Use when reviewing headlines, landing pages, emails, or ad copy.
triggers:
  - analyze copy
  - copy review
  - improve copy
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Copy Analyzer

Analyze marketing copy across 6 dimensions and deliver specific, actionable improvements with before/after examples for every weakness found.

## Gather Context First

1. **The copy** — Paste the text or provide the URL
2. **Copy type** — Landing page, email, ad, social post, product description?
3. **Target audience** — Who is this written for? Role, industry, awareness level
4. **Goal** — What should the reader do after reading? (Click, buy, sign up, reply)
5. **Brand voice** — Check `reference/brand-voice.md` for existing voice guidelines
6. **Constraints** — Character limits, format requirements, compliance needs

## Analysis Framework: 6 Dimensions

### 1. Readability (1-10)
**Evaluate:**
- Flesch-Kincaid grade level (aim for 6th-8th grade for most marketing copy)
- Average sentence length (target 12-18 words)
- Paragraph length (target 2-3 sentences max)
- Jargon usage — every technical term must earn its place
- Scannability — can someone get the main message by reading only headlines and bold text?

**Scoring guide:**
- 1-3: Dense, academic, requires multiple readings
- 4-6: Understandable but requires effort, some jargon
- 7-8: Easy to read, well-structured, scannable
- 9-10: Effortless to read, flows naturally, accessible to all levels

### 2. Persuasion (1-10)
**Evaluate using persuasion frameworks:**
- **Problem-Agitation-Solution (PAS):** Does the copy identify a problem, make the reader feel it, then offer a solution?
- **Before-After-Bridge (BAB):** Does it paint the current state, the desired state, and the bridge between them?
- **Emotional triggers:** Does the copy tap into fear of missing out, desire for status, need for belonging, or pain avoidance?
- **Benefit framing:** Are features translated into outcomes? ("256-bit encryption" vs "Your data is protected by bank-level security")
- **Urgency and scarcity:** If present, is it real or manufactured?

### 3. Clarity (1-10)
**Evaluate:**
- One main idea per paragraph — if a paragraph makes two points, it should be two paragraphs
- No ambiguous pronouns ("it", "this", "they" without clear antecedents)
- No filler words — cut "really", "very", "actually", "basically", "in order to", "that being said"
- No passive voice in CTAs — "Start your trial" not "Your trial can be started"
- The main message is stated explicitly, not just implied

### 4. Specificity (1-10)
**Evaluate:**
- Numbers and data over vague claims ("47% faster" vs "much faster")
- Named examples over generic ones ("Stripe uses this" vs "top companies trust us")
- Timeframes over "soon" ("results in 14 days" vs "quick results")
- Concrete outcomes over abstract benefits ("save 5 hours per week" vs "boost productivity")

**The specificity test:** Replace every adjective with "good" or "bad." If the sentence still makes sense, the copy lacks specificity.

### 5. Voice Consistency (1-10)
**Evaluate:**
- Does the tone stay consistent throughout? (No switching from casual to corporate mid-page)
- Does the voice match the target audience? (Developer copy sounds different from CEO copy)
- Is the brand personality evident? (Would you recognize this brand from the writing alone?)
- If `reference/brand-voice.md` exists, does the copy follow its guidelines?

### 6. Conversion Orientation (1-10)
**Evaluate:**
- Does every section move the reader toward the desired action?
- Is the CTA clear, specific, and low-friction?
- Are objections addressed before the CTA appears?
- Is there a logical flow: attention > interest > desire > action?
- Are there multiple entry points for different reader types (skimmers vs deep readers)?

## Analysis Process

### Step 1: Read-Through Assessment
Read the copy once as the target audience would. Note your first impressions, confusion points, and where your attention drops.

### Step 2: Section-by-Section Scoring
Break the copy into logical sections (headline, subheadline, body, CTA, etc.) and score each across all 6 dimensions.

### Step 3: Before/After Rewrites
For every section scoring below 7 on any dimension, provide a rewritten version with an explanation.

### Step 4: Priority Ranking
Identify the 3 changes that would have the highest impact on the copy's conversion goal.

## Output Format

### Overall Score Card

| Dimension | Score | Key Issue |
|-----------|-------|-----------|
| Readability | X/10 | ... |
| Persuasion | X/10 | ... |
| Clarity | X/10 | ... |
| Specificity | X/10 | ... |
| Voice Consistency | X/10 | ... |
| Conversion Orientation | X/10 | ... |
| **Overall** | **X/10** | |

### Section-by-Section Analysis

For each section of copy:

**[Section Name]**

Scores: Readability X | Persuasion X | Clarity X | Specificity X | Voice X | Conversion X

**Before:**
> [Original copy, quoted exactly]

**After:**
> [Improved version]

**Why this change matters:** [One sentence explaining the strategic reasoning]

### Top 3 Highest-Impact Changes
Ranked by expected impact on the conversion goal. For each:
1. What to change
2. Why it matters
3. The exact rewrite

### Copy Patterns to Fix Globally
Recurring issues that appear throughout (e.g., "always leads with features instead of benefits", "passive voice in every CTA").

## Do NOT
- Rewrite copy to sound like every other SaaS page — preserve the brand's unique voice
- Suggest changes that violate stated constraints (character limits, compliance requirements)
- Judge copy without considering the audience — developer docs should sound different from consumer ads
- Make only cosmetic changes when structural issues exist — fix the foundation first
- Add persuasion tricks that border on manipulation (fake scarcity, guilt-tripping, misleading claims)