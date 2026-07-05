---
name: pdf-handler
description: Read PDF files and extract text, tables, or structured data. Use when the user mentions PDF, .pdf, paper, contract, research report, or wants to summarize, extract data from, or search a PDF.
triggers:
  - read pdf
  - extract from pdf
  - summarize pdf
  - search this pdf
  - pdf to markdown
---

# PDF Handler

Read PDF files and surface their content as usable text, tables, or structured data. PDFs are common in finance (statements, audits), operations (contracts, vendor docs), people (offer letters, policies), and research (papers, reports).

## Pick the right approach

PDFs vary widely in quality. Pick by source type:

- **Text-native PDFs** (exports from Word, LaTeX, web): `pdfplumber` or `PyPDF2` for text, `pdfplumber` for tables.
- **Scanned PDFs** (images of paper): OCR via `pytesseract` after page-to-image with `pdf2image`.
- **Forms / structured PDFs**: `pdfplumber` extracts cell positions; for AcroForm fields use `pypdf`.

If no library is available, install `pdfplumber` (`pip install pdfplumber`) before proceeding. Tell the user.

## Reading

Print a structure overview first:
```
Pages: 24 | Estimated text: 12,400 words | Tables detected: 3 | Has images: yes
```

Extract text page by page rather than all at once for long documents — it makes citing page numbers possible later.

## Tables

Tables in PDFs are tricky. Use `pdfplumber.extract_tables()` and verify by printing the first 3 rows of each detected table. If the table looks broken (mis-aligned columns, fragmented cells), tell the user before trying to act on it. Don't pretend a broken table is clean.

## Summarizing

For a long PDF the user wants summarized:
1. Extract the full text.
2. Skim section headings and produce a short outline.
3. Ask the user what level of detail they want (executive summary, section-by-section, or topic-focused).
4. Cite page numbers in your summary so they can verify.

## Output format

For data extraction: save structured output to `outputs/<stem>.json` or `outputs/<stem>.csv`.

For summaries: save to `outputs/<stem>-summary.md` with a "Source" heading at the top citing the PDF path and page count.

For text dumps: save to `outputs/<stem>.md` so the user can grep it later.

## Common mistakes

- Treating a scanned PDF as text-native (you'll get garbage). Detect and route to OCR.
- Losing page numbers when concatenating text — keep them.
- Confidently summarizing a PDF when the OCR is unreliable. Flag uncertain extractions.
- Hallucinating content when the PDF is image-only and OCR failed. Say "I couldn't read this reliably" instead.

## Cross-references

For generating PDFs, prefer markdown → `docx-handler` → Word/PDF export pipeline, or use `presentation-builder` for slide-style PDFs. For Excel-source data, see `xlsx-handler`.
