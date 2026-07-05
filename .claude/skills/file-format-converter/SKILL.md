---
name: file-format-converter
description: Convert PDF, PowerPoint, Word, HTML, CSV, and other files into clean Markdown.
triggers:
  - convert this file
  - turn this into markdown
  - extract text from
  - read this PDF
---

# File Format Converter

Convert files into clean Markdown. Each format has specific handling.

**PDF:** Extract text, preserve headings/lists/tables as Markdown, note page numbers in comments. Flag scanned PDFs needing OCR.
**PowerPoint:** Extract per slide: title, body text, speaker notes. Note images with `[Image: description]`. Preserve tables.
**Word:** Map styles to Markdown headers. Convert tables, lists, bold/italic. Preserve footnotes as references.
**HTML:** Extract main content (skip nav/footer). Convert semantic HTML to Markdown. Preserve links, strip scripts/styles.
**CSV:** Detect header row, convert to Markdown table. For 50+ rows, summarize structure first and offer specific ranges.

## Principles
- Preserve structure over formatting. Headings, lists, and tables matter. Fonts don't.
- Keep it traceable. Include source filename and conversion date.
- Flag what's lost. If charts or media can't convert, note their location.
- Don't hallucinate content. Mark unclear text as `[unclear]`.

Save to `reference/[filename].md` for reference docs, `context/[topic].md` for session context, `outputs/[filename].md` for working docs.