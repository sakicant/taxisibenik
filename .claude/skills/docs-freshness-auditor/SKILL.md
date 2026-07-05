---
name: docs-freshness-auditor
description: Audit documentation for freshness by checking for broken links, outdated version numbers, stale dates, references to removed files, and other signs of decay. Use when docs feel out of date or before a release.
triggers:
  - docs audit
  - check docs freshness
  - stale documentation
  - link checker
---

# Docs Freshness Auditor

Scan documentation files for signs of decay. Documentation rots faster than code because nothing forces it to stay current. This skill finds the rot.

## Scope

Audit these locations by default:
- `context/` — project context files
- `reference/` — design system, guides, structure docs
- `CLAUDE.md` — workspace root documentation
- `README.md` — if present
- `plans/` — implementation plans
- `outputs/` — generated documents and reports
- Any `.md` files in the project root

Override scope by specifying directories or files to audit.

## Checks

### 1. Broken Internal Links
- Scan for markdown links (`[text](path)`) and verify the target file exists
- Check relative paths resolve correctly from the linking file's location
- Flag links to specific headings (`#section`) — verify the heading exists in the target

### 2. Outdated Version Numbers
- Search for version patterns: `v1.2.3`, `version 1.2`, package version strings
- Cross-reference with `package.json`, `Cargo.toml`, `pyproject.toml`, or equivalent
- Flag any version number that does not match the current source of truth

### 3. Stale Dates
- Find dates in any format: `2025-01-15`, `January 2025`, `Q1 2025`, `last month`
- Flag dates older than 90 days as "suspect" and older than 180 days as "stale"
- Relative time references ("last week", "recently", "soon") are always suspect

### 4. Dead Code References
- Find references to file paths (`src/components/...`, `lib/...`) and verify the files exist
- Find references to function or class names and verify they exist in the codebase
- Flag references to deleted or renamed entities

### 5. Inconsistent Counts
- Look for numeric claims ("12 templates", "5 agents", "3 generators")
- Verify counts against the actual source files where possible
- Flag mismatches between documented counts and reality

### 6. Orphaned Documentation
- Identify docs that reference features or systems no longer in the codebase
- Find docs not linked from any other document (orphans)
- Check for TODO, FIXME, or placeholder markers that were never resolved

### 7. Terminology Drift
- If a terminology guide exists (e.g., in `context/voice-and-design.md`), check for violations
- Flag inconsistent naming: same concept called different things in different docs

## Severity Levels

| Level | Meaning | Examples |
|-------|---------|---------|
| **BROKEN** | Factually wrong or points to nothing | Broken link, reference to deleted file, wrong version |
| **STALE** | Likely outdated but not provably wrong | Date >180 days old, count mismatch, relative time reference |
| **SUSPECT** | May be outdated, needs human verification | Date >90 days old, terminology inconsistency, orphaned doc |

## Output Format

Write the audit report to `outputs/docs-freshness-report.md`:

```markdown
# Documentation Freshness Report
Audited: [date]
Scope: [directories audited]
Files scanned: [count]

## Summary
- BROKEN: [count]
- STALE: [count]
- SUSPECT: [count]

## Findings

### BROKEN
| File | Line | Issue | Details |
|------|------|-------|---------|
| context/roadmap.md | 42 | Dead link | Links to src/lib/oldModule.ts (deleted) |

### STALE
| File | Line | Issue | Details |
|------|------|-------|---------|

### SUSPECT
| File | Line | Issue | Details |
|------|------|-------|---------|
```

## Do NOT
- Automatically fix issues — report them for human review
- Flag dates in changelogs or historical records — those are intentionally old
- Treat test fixtures or example data as real documentation
- Scan node_modules, dist, or build output directories