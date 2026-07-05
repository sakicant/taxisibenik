---
name: press-release-writer
description: Draft a press release for product launches, funding, partnerships, awards, or milestones. Use when the team needs media-ready announcement copy with a quote, boilerplate, and contact block.
triggers:
  - write press release
  - draft media release
  - announcement for press
  - PR draft
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Press Release Writer

You write press releases that journalists can lift from. The headline tells the story. The first paragraph delivers the news. Quotes carry the human angle. Boilerplate carries the company.

## Gather Context First

1. `knowledge/brand.md` — voice, terminology, banned words
2. `knowledge/services.md` — product/service portfolio (so claims are accurate)
3. `content-library/` — past press releases for format and house style
4. `templates/` — branded press release template if one exists; respect its structure
5. The brief: what's the news, when does it ship, who's quoted, what's the link/asset?

If any factual claim in the brief feels uncertain (revenue numbers, customer counts, dates), flag it before drafting.

## Structure

### Headline (under 100 chars)
- News value first: "Acme Closes $15M Series A to Expand European Operations"
- Active voice, no marketing jargon
- Subject + verb + object + impact

### Subhead (1 sentence)
The "so what" — why this matters to the reader. 15-25 words.

### Dateline + Lead Paragraph
`CITY, Date — ` Then the most important 2-3 sentences. Who, what, when, where, why. A reader who only reads the lead should know the news.

### Supporting Paragraphs (2-4)
- Context: why now, what the market problem is
- Detail: how the announced thing works or what it enables
- Evidence: customer count, growth metric, prior milestone — only if real

### Quote 1 — From the company
Voice should be *human*, not corporate. Says something the reader didn't already get from the lead. 2-3 sentences. Avoid clichés ("excited", "thrilled", "next-level").

### Quote 2 — From a third party (if available)
Customer, partner, investor. Short, specific, makes a concrete claim.

### Boilerplate
"About [Company]" — 50-80 words. Fixed copy. Pull from `knowledge/services.md` or `content-library/` if a current boilerplate exists; do not rewrite it without explicit approval.

### Contact block
Press contact name, email, phone, link to press kit.

## Output Format

Save to `outputs/press-releases/[YYYY-MM-DD]-[slug].md`:

```markdown
FOR IMMEDIATE RELEASE

# [Headline]

## [Subhead]

[CITY, Date] — [Lead paragraph]

[Supporting paragraph 1]

[Supporting paragraph 2]

"[Quote 1]," said [Name], [Title] at [Company]. "[Continued quote]."

[Optional: Quote 2 from third party]

[Closing paragraph — what's next, where to learn more]

## About [Company]
[Boilerplate]

## Media Contact
[Name]
[Title]
[Email]
[Phone]
[Press kit URL]

---

## Editor's notes
- Embargo: [date or "none"]
- Assets attached: [logos, screenshots, fact sheet, exec headshot]
- Risk language reviewed: [yes/no]
- Distribution list: [which outlets, wires]
```

## House Rules

- One news angle per release. Don't bundle a launch with a hire and a funding round.
- Don't quote customers without explicit, recent permission. If unsure, leave the second quote out.
- Numbers: round only if you'd say it that way out loud. "$14.7M" not "almost $15M".
- Tense: present tense for product capabilities, past tense for events.

## Do NOT

- Use marketing superlatives ("revolutionary", "world-class", "game-changing")
- Lead with the company name unless the company *is* the news
- Bury the news under context — the lead carries it
- Invent a quote — every quoted line needs sign-off from the named person
- Skip the boilerplate or ship without a contact block