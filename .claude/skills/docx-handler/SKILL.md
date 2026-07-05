---
name: docx-handler
description: Read, edit, and generate Microsoft Word documents. Use when the user mentions Word, .docx, document, contract, report, or wants to extract text from a doc, generate one from markdown, or apply tracked-change-style edits.
triggers:
  - read docx
  - word document
  - extract from word
  - generate docx
  - convert markdown to word
---

# DOCX Handler

Operate on Microsoft Word files (`.docx`). Extract content, generate new documents from markdown, or apply targeted edits.

## Pick the right approach

1. **Python with `python-docx`** — best for reading and writing with style awareness.
2. **Pandoc** (`pandoc input.md -o output.docx`) — best for converting markdown → Word with reasonable defaults.
3. **Node with `docx` library** — use if Python isn't available.

If nothing is installed, prefer `pip install python-docx` for reads/edits or use Pandoc for markdown conversion. Tell the user you're installing it.

## Reading

Print a quick structure summary so the user knows what's inside:
```
Pages: ~12 | Words: 3,840 | Sections: 4 | Tables: 2 | Headings: 18
```

Extract text faithfully — preserve heading levels, lists, and table structure when converting to markdown. Don't paraphrase.

## Generating from markdown

When the user asks for a Word version of markdown content:
1. Save the source markdown to `outputs/<topic>.md` first (so they have both versions).
2. Convert with Pandoc when available; fall back to `python-docx` building paragraphs by section.
3. Apply a heading style hierarchy (Heading 1 → Heading 2 → Heading 3) so the document is navigable.
4. Tables: render as Word tables, not pasted text.

## Editing

For targeted edits ("change every instance of X to Y"):
- Read the document, list the matches, ask before applying if there are more than 5.
- Preserve formatting: a styled run (bold, color, font) should keep its style after the substitution.
- For larger rewrites, prefer regenerating from a cleaned markdown source rather than in-place editing.

## Output format

Save to `outputs/<original-stem>-edited.docx` for edits, `outputs/<topic>.docx` for new documents. Print a one-line report: path, sections added/changed, tables included.

## Common mistakes

- Stripping styles when extracting (read with style awareness, don't dump plain text).
- Generating Word from markdown but losing tables or list nesting.
- Overwriting the source file.
- Inserting unicode characters that Word renders as boxes — verify the output opens cleanly.

## Cross-references

For Excel data sources powering the document, see `xlsx-handler`. For PDF-only deliverables (e.g., contracts that should not be editable), generate via the same pipeline then export to PDF using Pandoc or LibreOffice. For brand-consistent styling, see `brand-guidelines`.
