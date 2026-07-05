---
name: xlsx-handler
description: Read, write, edit, and clean Excel files. Use when the user mentions Excel, .xlsx, spreadsheet, workbook, formulas, pivot tables, or wants to extract data from a sheet, transform it, or generate a new workbook.
triggers:
  - read xlsx
  - excel file
  - spreadsheet
  - workbook
  - clean this sheet
  - extract from excel
---

# XLSX Handler

Operate on Microsoft Excel workbooks (`.xlsx`). Read existing files, transform data, and write results back without breaking formulas, references, or formatting that the user cares about.

## Pick the right approach

Check what's available in the environment before writing code. In order of preference:

1. **Python with `openpyxl`** — best for cell-level edits, preserves formulas, supports multi-sheet, can read formatting.
2. **Python with `pandas`** + `openpyxl` engine — best for data transformations (filter, group, pivot) where you don't need to preserve cells exactly.
3. **Node with `exceljs` or `xlsx`** — use if Python isn't installed.

If no library is available, install `openpyxl` (`pip install openpyxl`) before proceeding. Tell the user you're installing it.

## Reading

Always confirm the file exists before opening. Print sheet names and dimensions first so the user knows what you found:

```
Sheets: Q1, Q2, Q3, Q4
Q1: 245 rows x 12 cols (A1:L245)
```

For multi-sheet workbooks, ask which sheet to act on if it isn't obvious from the prompt.

## Editing

- **Preserve formulas** by default. If a cell contains `=SUM(A1:A10)` and the user just wants to update headers, do not overwrite formula cells.
- **Preserve formatting** when the source has merged cells, conditional formats, or named ranges. `openpyxl` keeps these by default; `pandas.to_excel` does not.
- **Never silently round numbers.** Match the source precision. If you must change precision, tell the user.
- **Back up before destructive edits.** Save a copy at `outputs/<original-name>.backup.xlsx` before overwriting.

## Cleaning patterns

Common asks and how to handle:

- **Remove empty rows/columns** — drop only rows where every cell is empty or only whitespace.
- **Standardize headers** — lowercase, replace spaces with underscores, strip leading/trailing whitespace.
- **Coerce types** — detect columns that look like dates/numbers but are stored as strings; convert and warn on rows that fail.
- **Find duplicates** — show the user a sample of duplicates and the column(s) that define duplication before deleting.
- **Trim trailing whitespace** in every text cell.
- **Detect merged-cell weirdness** — flag and ask before unmerging; merged cells often hide important structure.

## Output format

Save the result file to `outputs/` with a clear name:
- Read-only result (e.g. summary): write a markdown summary to `outputs/<topic>-summary.md`.
- Edited workbook: write to `outputs/<original-stem>-cleaned.xlsx` (don't overwrite the source unless asked).
- Multiple-sheet output: keep the sheet structure of the source; don't collapse to one sheet.

Print a short report after writing: file path, rows/cols changed, any rows skipped or flagged.

## Common mistakes

- Writing a CSV when the user asked for Excel.
- Using `pandas` and losing all formulas.
- Saving to the source path and clobbering the original.
- Treating empty cells as zero (use `None` / `null`).
- Not asking which sheet when the workbook has more than one.

## Cross-references

For PDF reports of the same data, see `pdf-handler`. For converting numerical findings into a board-ready slide, see `pptx-handler` and `presentation-builder`. For SaaS-metric or finance-specific calculations on the data, see `saas-metrics-coach`.
