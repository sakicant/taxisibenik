---
name: pptx-handler
description: Generate PowerPoint files from outlines, edit existing decks, or extract content from a deck. Use when the user mentions PowerPoint, .pptx, slide deck, or wants to programmatically build/edit slides. For narrative-style deck planning use presentation-builder first.
triggers:
  - generate pptx
  - create slide deck
  - edit powerpoint
  - extract from pptx
  - convert markdown to slides
---

# PPTX Handler

Operate on PowerPoint files (`.pptx`). The pair is: `presentation-builder` plans the deck (story, slide-by-slide outline); `pptx-handler` materializes it into a real `.pptx` file.

## Pick the right approach

1. **Python with `python-pptx`** — best for full control: layouts, placeholders, shapes, charts.
2. **Pandoc with reveal.js or pptx output** — fastest for markdown-to-deck.
3. **Node with `pptxgenjs`** — use if Python isn't available.

Install `pip install python-pptx` if needed. Tell the user.

## Generating from an outline

If the user has an outline (or just gave you talking points), turn each section into one slide. Default rule of thumb:

- **Title slide** — deck title, presenter, date.
- **Content slides** — one idea per slide, max 7 lines, max 8 words per line.
- **Transition slides** — single bold word or phrase, used between major sections.
- **Closing slide** — call to action, next steps, contact.

If the source is markdown with H1/H2 headings, treat each H2 as a slide.

## Editing

Common edits:

- Replace placeholder text — find by exact match, replace, preserve runs.
- Update a chart's data — pull the underlying data table, write back.
- Apply a different template — extract content, regenerate against the new layout.

If the deck has merged cells, animations, or transitions, preserve them. `python-pptx` keeps most of these by default, but verify.

## Charts and tables

For numeric data:
- Pull data from the source (often `xlsx-handler` output).
- Generate the chart via `python-pptx.chart` rather than embedding screenshots — keeps the deck editable.
- Always add a data label or axis label.

## Output format

Save to `outputs/<topic>.pptx`. Also save the source outline as `outputs/<topic>-outline.md` so the user can regenerate or edit non-visually.

## Common mistakes

- Cramming a slide with text. If it doesn't fit in 7 lines, split into two slides.
- Pasting screenshots of charts instead of native charts (loses editability).
- Mixing fonts or colors that don't match the brand. See `brand-guidelines`.
- Generating a deck without a clear story arc. Use `presentation-builder` first to plan.

## Cross-references

For deck planning and narrative, see `presentation-builder`. For board-meeting decks specifically, see `board-deck-builder`. For brand-consistent styling, see `brand-guidelines`. For Excel-source data, see `xlsx-handler`.
