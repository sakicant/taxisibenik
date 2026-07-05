# /prime — Session Initialization

Load your workspace context, then greet the user with a tight dashboard. No long preamble, no file dumps.

## Step 0: Check workspace status

Read `.froject.json` and check the `hatched` field:

- If `hatched` is `false`: Run `/hatch` automatically. Do not proceed until hatching is complete.
- If `hatched` is `"partial"`: The workspace structure is set up but context enrichment hasn't happened yet. Jump to **Step 3** below.
- If `hatched` is `true`: Proceed to **Step 1**.

## Step 1: Load context (silently, in parallel)

Read in one batch — don't narrate each file:

- `CLAUDE.md`
- Every file in `context/`, `knowledge/`, or whichever workspace directories exist
- Recent files in `plans/` and `outputs/` to see what's in motion
- `git status` and the last few commits (only if this is a git repo)

Synthesize. Do not show file contents to the user.

## Step 2: Quick integrity check

Does CLAUDE.md still match reality? Directories listed but missing? Commands, skills, or rules on disk that CLAUDE.md doesn't mention? Note anything off, but don't fix it unless the user asks.

## Step 2.5: Offer profile building (one-time, after tools are connected)

Check `.froject.json` for three conditions:
1. `hatched` is `true` (not the first session after hatch)
2. `profileBuilt` is NOT set or is `false`
3. MCP tools are connected and responding (Slack, Gmail, Notion, or similar)

If all three are true, offer to build a personal profile:

"You've been using your tools for a bit. I can analyze your recent messages and documents to learn how you work and write. This takes a few minutes and creates three files: a working style profile, a writing style profile, and a compact summary you can use across all your workspaces. Want me to do that now?"

If the user says yes:
1. Pull recent data (last 30-60 days) from each connected source:
   - **Slack**: messages across channels. How they instruct, ask, respond. Tone by channel. Recurring phrases.
   - **Gmail**: sent emails. Greeting style, paragraph length, closings. Tone by recipient.
   - **Notion**: authored pages. Document structure, vocabulary, formatting habits.
2. Create `context/working-style.md`: prose description of how they work (task approach, iteration style, feedback style, decision making, delegation patterns). Write it like you're describing them to a new colleague.
3. Create `context/writing-style.md`: tone, sentence rhythm, paragraph structure, vocabulary fingerprint, formatting habits, register shifts by context. Include 2-3 quoted examples. Separate sections per language if they write in multiple.
4. Create `context/profile.md`: 200-500 word condensed version of both files, suitable for pasting into Claude's User Preferences (Settings > General > Personal Preferences).
5. Show the user all three files for review. These are personal. Get confirmation before saving.
6. Update `.froject.json`: set `profileBuilt` to `true` with the current date.
7. Suggest pasting profile.md into User Preferences for cross-workspace consistency.
8. Tell the user: "Your profile will get better over time. I'll offer to refresh it in a month or so."

If the user says no or not now, respect that. Don't ask again this session. Ask again in a future session (check if `profileBuilt` is still false).

## Step 3: Complete enrichment (only when hatched is "partial")

This runs automatically when the workspace was hatched but enrichment was skipped because tools weren't connected yet.

1. **Check MCP connections.** Run `/mcp` or check which MCP tools are available.
2. **If tools are now connected** (Notion, Slack, HubSpot, etc.):
   - Tell the user: "Your tools are connected now. Let me pull in your data to finish setting up."
   - Pull data from each connected MCP into workspace context files (same as /hatch Phase 6 enrichment)
   - Update `.froject.json`: set `hatched` to `true`
   - Tell the user: "Enrichment complete. Your workspace now has real data from your tools."
3. **If tools are NOT connected yet:**
   - Tell the user: "I notice your workspace hasn't been enriched with data from your tools yet. Want to connect them now? Type `/mcp` to set up your integrations, then start a new session and I'll pull in your data automatically."
   - Do NOT block the session. Proceed to Step 1 so the user can still work.
4. After enrichment (or skipping), proceed to **Step 1** to load context normally.

## Step 4: Print the dashboard

After everything loads, print a friendly dashboard. No filler before it.

```
# Your Froject workspace · Primed

[Workspace name] · [type] · [one-line current state from CLAUDE.md or roadmap]

## What's active

▸ [Top priority or current focus]
▸ [Second priority]
▸ [Third priority]
(3-5 bullets pulled from roadmap, context files, or recent commits)

## Tools connected

▸ [List MCPs that responded to a quick ping]
(or "No tools responding yet. They may need a Claude restart.")

## Ready

Just ask me anything, or try:
- /work · pick up your highest-priority task
- /create-plan · plan a new piece of work
- /close · wrap up the session

────────────────────────────────────────
What are we doing today?
```

## Rules for the dashboard

- Friendly, never robotic. It's a greeting, not a status report.
- "What's active" caps at 5 bullets. Pick what actually matters.
- Drop any section that has nothing to show. No empty headers.
- No em dashes. Periods, commas, or middle dot.
- Divider is exactly 40 box-drawing horizontal characters.