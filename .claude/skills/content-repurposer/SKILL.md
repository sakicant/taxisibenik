---
name: content-repurposer
description: Transform a single piece of content into formats for multiple channels.
triggers:
  - repurpose content
  - content for multiple channels
  - adapt this for
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Content Repurposer

You transform one piece of content into many formats, each tailored to its platform. The goal is maximum reach from minimum original creation.

## Gather Context First

Check `context/` for brand voice guidelines, audience profiles, and channel strategy. Ask only for what is missing:
1. **What is the source content?** Article, talk, podcast, report, internal doc.
2. **Which channels are active?** LinkedIn, X/Twitter, newsletter, blog, YouTube, TikTok.
3. **Who is the audience per channel?** They may differ.
4. **What is the goal?** Awareness, traffic, engagement, lead generation.

## The Content Atomization Method

### Phase 1: Extract Core Assets
Read the source material and pull out:
- **1 big idea** — The single thesis or insight (1 sentence).
- **3-5 supporting points** — Key arguments, data, or stories.
- **Quotable lines** — Phrases that stand alone.
- **Data points** — Stats, percentages, comparisons.
- **Stories/examples** — Narrative moments that illustrate the point.

### Phase 2: Map to Formats
Each platform gets a different cut of the same material:

| Platform | Format | Length | Angle |
|----------|--------|--------|-------|
| LinkedIn | Personal narrative post | 1300 chars (above fold) | First-person insight or lesson learned |
| X/Twitter | Thread (5-8 posts) | 280 chars per post | Punchy, numbered takeaways |
| Newsletter | Curated commentary | 300-500 words | Summary + personal take + link |
| Blog | Long-form adaptation | 800-1500 words | SEO-optimized, standalone piece |
| Short video | Script (60 sec) | 150 words | Hook in first 3 seconds, one takeaway |
| Slide carousel | 8-10 slides | 1 idea per slide | Visual, swipeable, educational |

### Phase 3: Adapt Per Platform

**LinkedIn:** Lead with a hook line. Use short paragraphs (1-2 sentences). End with a question to drive comments. Add 3-5 relevant hashtags.

**X/Twitter Thread:** Tweet 1 is the hook with a promise. Each tweet is one self-contained idea. Final tweet summarizes and links to the original. Use "1/" numbering.

**Newsletter:** Personal opening (why this matters to you). Key takeaways as bullets. One link to the full piece. End with a question or CTA.

**Short Video Script:**
- 0-3 sec: Hook question or surprising stat
- 3-15 sec: Context and setup
- 15-45 sec: The key insight with example
- 45-60 sec: CTA (follow, link in bio, comment)

**Slide Carousel:**
- Slide 1: Bold headline (hook)
- Slides 2-8: One point per slide with minimal text
- Slide 9: Summary
- Slide 10: CTA (follow, save, share)

## Output Format

Save all repurposed content to `outputs/repurposed/`:

```
outputs/repurposed/
  linkedin-post.md
  twitter-thread.md
  newsletter-edition.md
  video-script.md
  carousel-slides.md
```

Each file includes the platform, character/word count, and any scheduling notes.

## Do NOT
- Copy-paste the same text across platforms. Each format requires a rewrite.
- Ignore platform character limits and norms.
- Repurpose without identifying the core insight first.
- Post the same angle on every channel. Vary the entry point.
- Forget to link back to the original source where appropriate.
- Use hashtags on platforms where they hurt reach (e.g., X threads).