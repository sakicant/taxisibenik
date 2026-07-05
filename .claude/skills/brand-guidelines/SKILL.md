---
name: brand-guidelines
description: Build a complete brand guidelines document — visual identity (logo, color, typography), voice and tone, and usage rules (do/don't examples, applications). For voice-only output use brand-voice-builder. For competitor positioning use positioning-generator.
triggers:
  - brand guidelines
  - brand book
  - style guide
  - visual identity
  - logo usage
  - brand reference
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Brand Guidelines

Generate a complete brand guidelines document covering everything a designer, writer, or vendor needs to produce on-brand work without asking.

## Structure

A working brand guidelines doc has six sections. Each one is short and practical — it's a reference, not a manifesto.

### 1. Brand basics
- Mission (one sentence).
- Vision (one sentence).
- Personality (3-5 trait pairs: "[what we are] but not [what we are not]").
- Audience (who the brand speaks to, plain-language).

### 2. Logo
- Primary lockup, secondary lockup, icon-only mark.
- Clear space rule (typically 1x logo height on all sides).
- Minimum size for digital and print.
- Approved colorways (full color, mono dark, mono light, reversed).
- Don't list: distortion, drop shadow, recoloring outside palette, rotation, photo backgrounds without contrast.

### 3. Color
- Primary palette (3-5 colors): name, hex, rgb, cmyk, accessibility role (text, background, accent).
- Secondary palette for accents.
- Usage ratio (e.g., 60% primary, 30% neutral, 10% accent).
- Accessibility note: every text-on-background combo should pass WCAG AA contrast (4.5:1 for body, 3:1 for large text).

### 4. Typography
- Display font (headlines), body font (paragraphs), mono font (code/data).
- Type scale (e.g., H1 48px, H2 32px, H3 24px, body 16px, small 14px).
- Line-height defaults.
- Character of headlines (sentence case vs title case, terminal punctuation rules).

### 5. Voice and tone
Pull from the existing `brand-voice-builder` output if available. Otherwise summarize:
- Personality traits.
- 5-10 preferred terms with context.
- 5-10 avoided terms with reasons.
- Tone calibration table (marketing vs docs vs internal vs error messages).

### 6. Applications
Show the brand applied to the most common surfaces. One example per:
- Website hero
- Social post (square + landscape)
- Email signature
- Pitch deck cover slide
- Internal memo header
- Product UI screenshot annotation

## Gather inputs first

Check `reference/` and `context/` for any existing brand assets. Don't reinvent. If a logo SVG exists, reference its path. If a color palette is already documented, pull it forward verbatim.

If nothing exists, ask the user for: logo files, brand colors (or screenshots of where they're used), and font names. Don't invent these.

## Output format

Save the guidelines doc to `reference/brand-guidelines.md`. Make it skimmable — short sections with examples, not paragraphs of theory.

If logo files or color swatches were provided, also save copies to `reference/brand/` so the doc has working asset references.

## Cross-references

For voice and tone only (no visual identity), use `brand-voice-builder` and skip this skill. For competitive positioning, see `positioning-generator`. For applying brand to specific deliverables, see `pptx-handler` (decks), `internal-comms` (memos), `copy-analyzer` (copy review).
