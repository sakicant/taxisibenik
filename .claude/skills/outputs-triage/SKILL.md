---
name: outputs-triage
description: Route orphan files in outputs/ to the correct subdirectory and extract scattered TODOs across notes. Use to clean up an accumulated backlog of loose files and unfiled tasks. For session-level capture, see session-debrief.
triggers:
  - triage outputs
  - clean up outputs
  - organize my files
  - find scattered tasks
  - outputs cleanup
---

# Outputs Triage

Move loose files into the right home and surface tasks buried in notes. Quick decisions, not deep analysis.

## Execution Style

This skill makes routing decisions, not strategic ones. Be fast. Target under 10 seconds per item. If the right destination isn't obvious, leave the file alone and flag it for the user.

## Gather Context First

1. Read `context/` for the active project structure and conventions
2. Identify the existing subdirectories under `outputs/` (these are the routing targets)
3. Check `plans/` for active plan names — files referencing them route there
4. Read the latest weekly plan for current priorities

## The Triage Sequence

### Pass 1 — Loose files in outputs/

Scan `outputs/` for files at the top level (not inside a subdirectory).

For each loose file, decide:

| Pattern | Route to |
|---------|----------|
| Filename contains a project name | `outputs/<project>/` |
| Filename contains a person's name | `outputs/people/<name>/` if it exists, else flag |
| Filename starts with a date | Likely a meeting note — `outputs/meetings/` |
| Marketing asset (image, post copy, ad) | `outputs/marketing/` |
| Audit or report | `outputs/audits/` |
| Transcript | `outputs/transcripts/` |
| Cadence artifact (weekly/quarterly) | `outputs/cadence/` |
| Stale draft (not modified in 30+ days, no clear home) | Flag for user to delete or keep |

If the right subdirectory does not exist, propose creating it — don't auto-create more than 2 new subdirectories per run (avoids fragmentation).

### Pass 2 — Scattered tasks in notes

Find unchecked task items (`- [ ]`) across:

- `notes/` (any subdirectory)
- `outputs/` (any subdirectory)
- `plans/` (active plans)

For each task:

| Task type | Route to |
|-----------|----------|
| Tied to an active priority in this week's plan | `outputs/cadence/weekly-plan-current.md` (or note in the existing plan) |
| Tied to a quarterly priority | Surface in next weekly review for prioritization |
| Tied to a specific person (follow-up) | `outputs/people/<name>/follow-ups.md` |
| Tied to a project | The project's plan or its `outputs/<project>/` directory |
| Stale (90+ days old, no progress) | Propose dropping |
| Unclear | Leave it, flag the file path for user |

### Pass 3 — Empty or near-empty files

Find files in `outputs/` smaller than 200 bytes. For each:

- If it's a placeholder or stub created weeks ago — propose deletion
- If it's an actively edited draft — leave it
- If it's a config or template — leave it

## Output Format

Save the triage report to `outputs/triage-YYYY-MM-DD.md`:

```
# Outputs Triage — [Date]

## Files routed
| From | To | Why |
|------|-----|-----|

## Tasks surfaced (route to plan/follow-up)
| Task | Found in | Suggested route |
|------|----------|-----------------|

## Flagged for user decision
| Item | Reason |
|------|--------|
| [Path] | [Ambiguous destination, stale draft, etc.] |

## Subdirectories proposed (max 2)
- `outputs/<new-dir>/` — for [pattern observed]

## Counts
- Files moved: X
- Tasks surfaced: Y
- Items flagged: Z
- Empty files cleaned: N
```

Show the report before executing any moves. Wait for confirmation on flagged items.

## Do NOT

- Delete files without confirmation — flag for the user instead
- Auto-create more than 2 new subdirectories per run — fragmentation hurts more than messy roots
- Move files into `notes/` or `context/` — those are user-curated, not triage destinations
- Reorganize files inside existing subdirectories — that's restructuring, not triage
- Touch git-tracked files in a way that loses history — use `git mv` for tracked files
- Spend more than 10 seconds on any single routing decision — when in doubt, flag it