---
name: enrich-workspace
description: Scan the workspace for thin, generic, or placeholder context, then interview the user with targeted questions to fill the gaps. Patches the files in place. Use after /hatch, when context files feel templated, or when Claude keeps asking the same questions session after session. Re-runnable anytime to tighten an existing workspace.
triggers:
  - enrich my workspace
  - fill context gaps
  - make my context less generic
  - interview me about my workspace
  - tighten my workspace
---

# Enrich Workspace

Find the gaps that make Claude generic, then ask the user 1-2 questions per gap to fill them. Quick session, real impact. The default state of a hatched workspace is "templated" — this skill makes it personal.

## Gather Context First

1. Read `.froject.json` for workspace type, role, and hatched status
2. List every file in `context/`, `notes/`, `reference/` (or workspace-equivalents)
3. Read `CLAUDE.md` to understand the workspace structure expected by this project type
4. Identify the user's role and tools — this shapes which gaps matter most

## The Gap Scan

Score each context source against four signals. A "gap" is anything that scores poorly on at least two.

### Signal 1 — Placeholder text

Flag files containing:
- `[your audience]`, `[describe your...]`, `[fill in]`, `[TODO]`, `[FIXME]`, `<your-name>`, `xxx`
- "Lorem ipsum" or obvious filler
- Section headers with no content underneath
- Default Froject template phrasing that wasn't customized

### Signal 2 — Thinness

A context file Claude reads every session needs density. Flag files where:
- Body is under 10 lines (excluding headers and metadata)
- Sections are present but only have 1-2 lines of generic copy
- The whole file reads like a description from a template, not from the user

### Signal 3 — Missing for the role

Each project type expects certain context files. Cross-reference what's present vs. what the role needs:

| Role | Expected context |
|------|------------------|
| Marketing | brand voice, target audience, ICP, key messages, content guidelines |
| Sales | ICP, deal stages, objection patterns, key competitors, current pipeline |
| Product | product vision, roadmap, key personas, success metrics, design principles |
| Customer success | onboarding playbook, health-score logic, expansion patterns, churn signals |
| People & Culture | values, hiring rubric, performance principles, company history |
| Software | architecture, conventions, tooling, deployment, key tradeoffs |
| Operations | processes, vendor list, decision rights, escalation paths |

If the role-expected file is missing, that's a gap. If it exists but is generic, that's also a gap.

### Signal 4 — Repeated questions

If the user has run sessions before, the most expensive gaps are the ones causing the same questions to come up. Check `outputs/learnings/` (if present) for patterns Claude keeps re-asking. These are top-priority gaps.

## Prioritize

Not every gap is worth fixing now. Score gaps by leverage:

| Gap location | Leverage | Why |
|--------------|----------|-----|
| Files Claude loads on every session (`CLAUDE.md`, `context/`) | **High** | Compounds across all future work |
| Files Claude loads via /prime | **High** | Same compounding effect |
| Reference files used occasionally | Medium | Matters when invoked |
| Notes / scratch directories | Low | User-curated, not Claude-facing |

Pick the top 3-5 highest-leverage gaps. Don't try to fix everything in one session.

## The Interview

For each picked gap, ask 1-2 targeted questions. Examples:

| Gap | Bad question | Good question |
|-----|--------------|---------------|
| Generic ICP file | "Who is your audience?" | "Describe your last 3 best-fit customers — what role were they in, what triggered them to buy, what did they say first on the call?" |
| Thin product vision | "What's your vision?" | "If your product disappeared tomorrow, what would your users have to go back to doing? Why is that bad?" |
| Missing voice file | "How do you want to sound?" | "Find a piece of writing from your team you love and one you hate. What's different?" |

Bad questions get generic answers. Good questions force specifics.

Run questions one at a time. Wait for the answer. Don't pile on.

## Patching the Files

After the interview:

1. **Show a diff** of every file you're about to change — original on left, proposed on right
2. **Preserve structure** — don't reorganize, just fill in
3. **Use the user's exact words** where possible — verbatim beats paraphrased
4. **Update only the gaps you interviewed about** — don't rewrite untouched sections
5. **Wait for confirmation** before saving each file (or batch confirm if the user says "go ahead with all")

## Output Format

Save a one-page summary to `outputs/enrichment/YYYY-MM-DD.md`:

```
# Workspace Enrichment — [Date]

## Gaps found
| File | Signal | Severity | Addressed? |

## Interview answers (verbatim or condensed)
- [Gap]: [user's answer]

## Files patched
- `<path>`: [1-line summary of what changed]

## Gaps deferred
- `<path>`: [why not now]

## Suggested re-run
- [What might be worth a second pass next time]
```

This summary is also useful as input for the next enrich-workspace run.

## Do NOT

- Run more than 6-8 questions in one session — interview fatigue produces shallow answers
- Rewrite a file the user has clearly customized — only fill in placeholder/thin sections
- Auto-save patches without showing diffs — the user owns the context files
- Replace the user's words with smoother prose — verbatim is the highest-value input
- Treat every file as equal priority — high-leverage gaps first, scratch files last
- Run on a workspace that hasn't been hatched — start with /hatch first to set up the structure