---
name: review-miner
description: Analyze customer reviews to extract pain points, trigger moments, objections, transformations, and standout language for messaging and creative strategy. Use when you have a batch of reviews (G2, Capterra, App Store, Trustpilot, Amazon, social mentions) and want to turn them into messaging inputs.
triggers:
  - analyze reviews
  - mine reviews
  - review analysis
  - customer review insights
  - extract review language
  - review audit
allowed-tools: []
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Review Miner

Mine positive customer reviews to extract the raw material for messaging, ad copy, content, and creative strategy. The goal is not to summarize reviews. The goal is to find the language, pain, moments, and transformations that make messaging resonate.

## Writes
- `outputs/review-mining-[product-or-brand].md`

## Input

Reviews can be provided in any format:
- Pasted into chat
- CSV or spreadsheet
- Document or file reference
- Links to review pages

If multiple products are present, identify them first. All analysis runs separately per product.

**Related skill:** For mixed sources (interviews + reviews + tickets + surveys), use voc-synthesis instead. This skill goes deeper on reviews specifically with quality scoring and structured bucket extraction.

## Step 1: Score Review Quality (1-5)

Before analysis, score every review:

| Score | What It Looks Like |
|---|---|
| **1** | Garbage. Gibberish, swear words, 2-3 meaningless words, zero signal. ("great product", "love it") |
| **2** | Low signal. Very short, vague, no detail or emotion. |
| **3** | Moderate. Mentions the product with some specificity but no vivid detail. |
| **4** | High quality. Specific, describes a real experience, references a before/after or a feeling. |
| **5** | Gold. Long, emotional, vivid, paragraph-level detail. The customer was so moved they wrote an essay. |

Discard all 1s. Analyze 2-5 with emphasis on 4s and 5s. Low-scoring reviews contribute to pattern identification but should not be the source of pulled quotes.

## Step 2: Extract by Bucket

For each product, extract insights into five buckets. Within each bucket, group similar insights and write a brief pattern summary. Then pull the best word-for-word quotes.

Do not paraphrase quotes. Pull them exactly as written.

### Bucket 1: Pain Points
What problem did they have before finding this product?

Look for: problem descriptions, duration, what they tried before, emotional weight, how it affected their life or work.

For each pain theme:
- Name the theme (3-5 words)
- 2-3 sentence pattern summary
- Best quotes for the swipe file

### Bucket 2: Trigger Moments
What finally made them buy?

Look for: the specific moment, event, or realization that turned a maybe into a purchase. Life events, recommendations, breaking points, running out of patience.

For each trigger theme:
- Name the theme
- 2-3 sentence pattern summary
- Best quotes

### Bucket 3: Objections Before Purchasing
What almost stopped them from buying?

Look for: skepticism, comparisons to other products, price hesitation, disbelief. In positive reviews, objections are almost always past tense: "I was skeptical but..." or "I almost did not try it because..."

For each objection theme:
- Name the theme
- 2-3 sentence pattern summary
- Best quotes

### Bucket 4: Transformation
What changed after they started using it?

Look for: before/after descriptions, specific outcomes, emotional shift, lifestyle changes, things they can do now that they could not before.

For each transformation theme:
- Name the theme
- 2-3 sentence pattern summary
- Best quotes

### Bucket 5: Standout Language
Phrases that are vivid, specific, and ready to use in messaging as-is.

Pull any phrase that:
- You would stop scrolling for if you saw it in an ad
- Describes the product better than the brand's own copy
- Has emotional weight or unexpected specificity
- Could work as a hook, headline, or testimonial snippet

## Step 3: Strategic Summary

After extraction, write a brief strategic summary:

1. **Top 3 pain themes** by frequency and intensity
2. **Most common trigger** that converts browsers to buyers
3. **Biggest objection** to address in messaging
4. **Strongest transformation language** for social proof
5. **Messaging gaps** (things customers care about that the brand is not saying)

## Step 4: Swipe File

Compile the 15-20 strongest quotes across all buckets into a single swipe file section, tagged by bucket. These are the quotes most likely to work in ads, landing pages, emails, or social proof sections.