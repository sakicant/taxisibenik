---
description: First-run command. Scan your workspace and rewrite templates with real details.
---

# /hatch — First-Run Workspace Setup

This command scans the current directory and rewrites all generated template files to be workspace-specific.

Read `.froject.json` first to load workspace type and check the `hatched` flag.

**Important:** Many users have never used a terminal before. Use plain, friendly language. Never assume they know what git, npm, or package managers are. If something fails, explain what happened and what to do next. Don't just show an error.

---

## Phase 1: Pre-flight

1. Read `.froject.json` to load workspace type and check `hatched` status.
2. If `hatched` is already `true`, warn the user: "This workspace was already hatched. Running again will overwrite customizations. Continue?" Wait for confirmation.
3. Announce: "**Claude is hatching your Froject workspace.** This usually takes a couple of minutes."

## Phase 2: Connect MCP Tools

If `.froject.json` contains an `mcpIntegrations` array with entries, try to connect them now.

**CRITICAL: You must actually run the install commands below. Do NOT just describe what you would do. Execute the command, wait for the result, and verify it worked.**

**Before installing anything, check what's already there.**

1. **Inventory existing MCPs.** Run `claude mcp list` and parse the output. Build a set of tool names already configured at any scope (`local`, `project`, or `user`). Many users connect tools at the company or user level via Claude Desktop, Claude Code enterprise managed settings, or earlier sessions. We must not install duplicates.

2. **Announce:** "Connecting your tools: [Notion, Slack, GitHub, ...]. I'll skip any that are already connected."

3. **For each integration in `mcpIntegrations`:**

   a. **If the tool name (or its slug) already appears in `claude mcp list`**, tell the user: "[Tool name] is already connected at your user level. Using that one." Skip the install entirely and move on. Do NOT re-add it at `local` scope.

   b. **Otherwise**, read its `mcpInstall` command and `mcpStatus`:

      **Official servers** (mcpStatus: "official"):
      - Tell the user: "Connecting [tool name] at user scope so it works across all your workspaces..."
      - Take the `mcpInstall` command and ensure it runs at user scope. If the command starts with `claude mcp add` and does NOT already include `--scope`, insert `--scope user` right after `add`. Example: `claude mcp add --scope user --transport http notion https://mcp.notion.com/mcp`.
      - Run the resulting command using the Bash tool.
      - If the command opens a browser for OAuth, tell the user: "A browser window should have opened. Complete the sign-in there, then come back here."
      - Wait for the user to confirm they completed the auth flow.
      - Test the connection by making a simple read call with the new MCP tool. If it returns data, the connection works.
      - Report result: "Connected [tool name]" or "Connection failed. You can retry later with: `[the command you ran]`"

      **Community servers** (mcpStatus: "community"):
      - Tell the user: "This is a community-maintained server. It may need an API key or extra setup."
      - Show the exact command and ask: "Want me to run this now?"
      - If it needs an API key, explain where to get one and wait for the user to provide it.
      - Install at user scope when the package supports it.

4. **Connect one tool at a time.** Finish one connection before starting the next.
5. **If a connection fails**, explain what went wrong, give the retry command, and move on.
6. **After all connections**, summarize: "Connected: [list]. Already had: [list]. Failed: [list]."
7. **Skip option** — If the user says "skip" or "later", move on.
8. **No integrations?** Skip this phase silently.

**Why user scope by default:** Most people use the same Slack, Notion, or GitHub account across every workspace they open. Installing at `user` scope means they connect once, then every Froject workspace they download just works. The `local` scope is reserved for one-off, repo-specific servers.

**Important: MCP connections often require restarting Claude Code to take effect.** If tools were connected but aren't responding yet, note this in Phase 4 and let the user know enrichment will happen on their next session (see Phase 6).

## Phase 3: Scan

Check the workspace type from `.froject.json`. Adapt scanning to what's actually present.

**For all workspace types:**
- **Directory structure**: List top-level folders and files
- **Git**: Check if `.git/` exists (don't worry if it doesn't, many workspaces start without git)
- **Workspace files**: Read any content already in context/, knowledge/, playbooks/, or other workspace directories
- **Connected tools**: For each successfully connected MCP, pull a sample of data (recent tasks, channel list, recent docs). This feeds into Phase 5.

**For software / data-science / operations types only:**
- **Package manifests**: `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Gemfile`, `pom.xml`, `build.gradle`
- **Config files**: `.eslintrc`, `prettier`, `tsconfig.json`, `.editorconfig`, CI configs
- **Scripts**: `Makefile`, `Justfile`, npm scripts, shell scripts
- **Frameworks**: detect React, Next.js, Django, FastAPI, Rails, Spring, etc.

**For non-code workspace types** (marketing, sales, product, people-culture, research, design, general):
- Do NOT look for package.json, node_modules, or run any package manager commands
- Do NOT report "no code project found" as if something is wrong. This is expected.
- Focus on: workspace name, user role, tools listed, and directory contents

## Phase 4: Report

Present a discovery summary to the user:

```
Here's what I found:
- Workspace: [name] ([type])
- Role: [user role if set]
- Tools: [listed tools]
- Connected: [list of successfully connected MCPs, or "none"]
- Directories: [list of workspace directories with content status]
```

For software workspaces, also include: Languages, Framework, Tests, Linter, Build, CI, Git.

Ask: "Does this look right? Anything to correct or add?"

Wait for user response before continuing.

## Phase 5: Ask

Ask **at most 2-3 questions** about genuine gaps, things the scan and MCP data couldn't determine. Keep questions simple and jargon-free. Bias toward fewer questions — if you have enough to work with, skip this phase entirely.

Possible questions (only ask what's truly missing):
- What is this workspace for? (only if the description is empty or vague)
- Any key context to seed into knowledge files? (company, team, domain specifics)
- Anything Claude should know about how you work?

**Do not ask about:** the user's role (it's in the config), how they'll use Claude (infer from workspace type), or tools (already configured). If the user responds with "all good" or similar, move on immediately.

## Phase 6: Rewrite + Auto-Enrich

Using scan results + user answers, rewrite all generated template files:

### CLAUDE.md
- Replace placeholder workspace name/description with real values
- For software types: fill in languages, tools, frameworks from scan
- For non-code types: focus on role, tools, and workflow context
- Update the workspace structure table to reflect actual directories and counts
- Keep the frog identity line
- Keep the CLAUDE.md lean: commands, skills, rules, and agents stay as name lists with counts, not full detail tables

### Workspace directory files (context/, knowledge/, etc.)
- Fill files with user-provided context from the conversation
- Remove empty files that the user didn't provide content for
- Remove empty directories that serve no purpose. Don't leave empty scaffolding.
- **Add a date stamp footer to every file you write in `context/`.** End each file with two newlines followed by `_Updated: YYYY-MM-DD_` using today's date. This is what `/close` reads later to detect stale files. Skip files outside `context/` (CLAUDE.md, settings.json, command files, etc.) — only context files get the stamp.

### .claude/commands/
- Update `/prime` content to reference real workspace details
- Keep all other commands, adjusting descriptions if workspace type changed

### .claude/settings.json
- For software workspaces: update permissions based on project needs
- For non-code workspaces: ensure no code-specific hooks are enabled (no npm test, no eslint, no tsc)

### Skills
- Enable/disable skills based on workspace type and user role

### Auto-enrich from connected MCPs (if available)

**Check if any MCP tools are actually responding.** If tools were connected in Phase 2 but aren't responding yet (common after fresh MCP installs that need a Claude restart), skip enrichment and set `hatched` to `"partial"` in Phase 8 instead of `true`. The /prime command will automatically complete enrichment on the next session when the tools are active.

**If MCP tools ARE responding**, enrich now:

For each connected MCP, use `contextType` and `contextTargets` from `.froject.json` to pull real data into workspace files:

| contextType | What to pull | Target files |
|-------------|-------------|--------------|
| tasks | Current sprint/board items, priorities, milestones | roadmap.md |
| communication | Team channels, recent discussions, team norms | team.md, conventions.md |
| docs | Key documents, wiki pages, knowledge base entries | business-info.md, strategy.md |
| code | Repo structure, conventions, recent PRs, CI config | conventions.md, architecture.md |
| data | Schema overview, key tables/collections | architecture.md |
| design | Design tokens, component inventory, style guidelines | design-system.md |
| infrastructure | Services, deployments, monitoring setup | infrastructure.md |
| crm | Pipeline stages, key accounts, recent activity | current-data.md, business-info.md |

**How to enrich:**
1. For each connected MCP, query for relevant data using the MCP tools available
2. Summarize the data into the target context files. Don't dump raw data, write useful summaries.
3. If a target file already has user-provided content, append MCP data below a "--- Auto-enriched from [tool] ---" divider
4. If a target file doesn't exist in the workspace, skip it
5. After enriching, ensure the file ends with `_Updated: YYYY-MM-DD_` using today's date. If a stamp already exists, replace it with today's date. If none exists, append one.

## Phase 6.5: Gap interview (optional)

After auto-enrichment, do a quick gap-scan on the rewritten context files to see how much is still templated.

**Scan signals:**
- Files containing placeholder text (`[your...]`, `TODO`, `describe your...`, default Froject phrasing)
- Context files with under 10 lines of real content
- Role-expected files that are missing or generic (e.g. no ICP file for a marketing workspace, no product vision for a product workspace)

**If 3+ gaps are found**, offer the user a targeted interview:

```
I noticed [N] places where your workspace is still generic.
Want a 5-minute interview to fill them in? (yes / skip)
```

If the user says yes, invoke the `enrich-workspace` skill. It will ask 1-2 targeted questions per gap and patch the files in place with the user's own words.

If the user says skip (or fewer than 3 gaps were found), say nothing and continue.

The user can always run `/enrich-workspace` (or just say "enrich my workspace") later.

## Phase 7: Quick-launch alias

Set up a shell alias so the user can open this workspace by typing a single word in any terminal.

1. Ask: "What word do you want to type to open this workspace? (e.g. `marketing`, `work`, `myproject`)"
2. Detect the user's shell config file:
   - If `$SHELL` contains "zsh" → `~/.zshrc`
   - If `$SHELL` contains "bash" → `~/.bashrc`
   - Otherwise → ask the user
3. **Get the absolute path** to the current workspace by running `pwd`. Store the result as the workspace path. Do NOT use a placeholder or relative path.
4. Append this line to the shell config file (using the **actual absolute path** from step 3). The `"/prime"` argument makes Claude Code run /prime as the first prompt automatically — without it, new users won't get their context loaded:

```bash
alias {{alias_name}}="cd /absolute/path/to/workspace && claude \"/prime\""
```

For example, if `pwd` returns `/Users/bjorn/Downloads/my-marketing-workspace`, the alias should be:
```bash
alias marketing="cd /Users/bjorn/Downloads/my-marketing-workspace && claude \"/prime\""
```

5. **Verify the alias** by reading back the line you just wrote to confirm the path is correct
6. Run `source ~/.zshrc` (or the appropriate config file) so it takes effect immediately
7. Tell the user: "Done! From now on, just type `{{alias_name}}` in any terminal to open this workspace."

## Phase 8: Finalize

1. **Determine hatch status.** If MCP enrichment happened successfully in Phase 6, set `hatched` to `true`. If enrichment was skipped (tools not responding or not connected), set `hatched` to `"partial"`.
2. Update `.froject.json`: set `hatched` to the appropriate value, update `project` fields with real data, update `generatedFiles` manifest.
3. **Verify CLAUDE.md**. Read the rewritten version. Ensure the key sections are intact: project info, workspace structure table, coding conventions (if software), critical constraints, and session workflow. The CLAUDE.md is intentionally lean — commands, skills, rules, and agents are listed by name only, not in full detail tables.
4. Read back all modified files to verify consistency.
5. Present completion report:

**If fully hatched (hatched: true):**

```
Your Froject workspace is hatched.

Modified files:
- CLAUDE.md (rewritten with your details)
- [workspace directories] (filled with context)
- [enriched files] (auto-populated from connected tools)
- .claude/commands/prime.md (updated)
- .froject.json (marked as hatched)

Claude has full context now. You're ready to work.
```

**If partially hatched (hatched: "partial"):**

```
Your Froject workspace structure is ready.

Modified files:
- CLAUDE.md (rewritten with your details)
- [workspace directories] (filled with what we know so far)
- .claude/commands/prime.md (updated)
- .froject.json (marked as partial)

One more step: Your tools (Notion, Slack, etc.) need a restart to
finish connecting. Close this session, reopen the workspace, and
/prime will automatically pull in your data from connected tools.

This is normal. Tool connections take effect after a restart.
```

6. After the file list, suggest what to do next:

**If fully hatched:**
```
You're all set! Your workspace is hatched and ready to go.

Loading your context now...
```

Then immediately run /prime to load all context. After /prime completes, show:

```
Here's what you can do right now:
- /work — Start your first task (fetches tasks if you have a task manager connected)
- /create-plan — Plan out a piece of work before diving in
- "Enrich my workspace" — fill any remaining context gaps via a short interview
- Or just ask Claude anything — it has your full context loaded.

Next time you want to open this workspace, just type: {{alias_name}}

At the end of each session, run /close to capture what worked and
what Claude should do differently next time.
```

**If /prime fails or doesn't respond:** Tell the user explicitly:

```
Heads up: I wasn't able to load your context automatically.
Type /prime and press Enter — this loads your workspace context
so I know who you are and what we're working on. You only need
to do this once per session.
```

**If partially hatched:**
```
Next steps:
1. Close this session: type /exit
2. Open the workspace again: type {{alias_name}}
3. /prime will detect your connected tools and pull in real data

If /prime doesn't run automatically, type /prime manually. It loads
your context and finishes setting up the workspace.

After that, you're fully set up. The workspace gets better every
time you use it and give feedback.
```

7. **Run /prime automatically.** After presenting the completion report, if `hatched` is `true`, run /prime immediately to load all context. The user should leave /hatch with a fully oriented workspace, not have to remember to type another command. If /prime fails or produces no output, show the fallback message above so the user knows to type /prime manually. Do not silently skip this step.

8. Replace any remaining `{{...}}` placeholders (like `{{alias_name}}`) with actual values at runtime.

---

**Note:** Replace any remaining `{{...}}` placeholders (like `{{alias_name}}`) with actual values at runtime.