---
name: build-my-profile
description: Analyze communication across connected tools (Slack, Gmail, Notion) to build a personal working style and writing style profile. Creates context/working-style.md, context/writing-style.md, and context/profile.md.
triggers:
  - build my profile
  - analyze my style
  - create my profile
  - how do I write
  - learn my style
---

# Build My Profile

Create a personal profile that helps Claude understand how the user works, writes, and communicates. This profile persists across sessions and makes every interaction more relevant.

## What you're building

Three files in `context/`:
- `working-style.md` — how the user approaches tasks, iterates, gives instructions, and makes decisions
- `writing-style.md` — tone, structure, vocabulary, formatting preferences, and patterns
- `profile.md` — a compact summary (200-500 words) suitable for Claude's User Preferences

## Where to find the data

Pull from every connected source available. The more data, the better the profile.

**Slack** (if MCP connected):
- Read the user's recent messages across channels (last 30-60 days)
- Look at how they give instructions, ask questions, respond to requests
- Note tone differences between channels (casual in general chat, structured in planning)
- Identify recurring phrases, sign-offs, formatting habits

**Gmail** (if MCP connected):
- Read sent emails from the last 30-60 days
- Analyze greeting style, paragraph length, closing style
- Note differences by recipient type (internal vs external, up vs down the org chart)
- Identify what they write themselves vs what they forward or delegate

**Notion** (if MCP connected):
- Read pages the user has authored or recently edited
- Look at how they structure documents: headings, lists, tables, free text
- Note vocabulary and terminology preferences
- Identify what kinds of documents they create most often

**If no sources are connected:**
- Ask the user directly. Use a conversational interview, not a questionnaire.
- Ask for 3-5 examples of writing they're proud of (emails, posts, docs, anything)
- Ask about their role, daily workflow, and what "good output" looks like to them
- Build the profile from their answers and examples

## How to build each file

### working-style.md

Analyze how the user works, not what they work on.

Look for:
- How they start tasks (jump in vs plan first, brief vs detailed instructions)
- How they iterate (small tweaks vs big rewrites, how many rounds)
- How they give feedback (direct vs diplomatic, specific vs general)
- How they make decisions (data-driven vs intuition, fast vs deliberate)
- What they delegate vs do themselves
- Patterns in how they ask for help (full context upfront vs progressive disclosure)
- Common frustrations or corrections they make repeatedly

Structure the file as plain prose, not a checklist. Write it as if describing the user to a colleague who's about to work with them for the first time.

### writing-style.md

Analyze how the user writes, across formats and contexts.

Look for:
- Default tone (formal/informal, confident/cautious, warm/neutral)
- Sentence rhythm (short and punchy vs long and detailed, varied or consistent)
- Paragraph length and structure preferences
- How they open and close communications
- Formatting habits (bullets vs prose, headers vs flat text, emoji usage)
- Vocabulary fingerprint: words they reach for, words they avoid
- Register shifts: how does tone change by audience or format?

If the user writes in multiple languages, create separate sections per language. Style often differs significantly between languages.

Include 2-3 short quoted examples that capture the style.

### profile.md

Condense working-style.md and writing-style.md into 200-500 words. This file should be compact enough to paste into Claude's User Preferences.

Include:
- Who they are (role, responsibilities, what they spend most time on)
- How they work with AI (instruction style, expectations, pet peeves)
- How they write (tone, structure, key preferences)
- What good output looks like to them
- Explicit rules (things Claude should always or never do)

## After building

- Ask the user to review all three files. These are personal. Get confirmation before saving.
- Suggest they paste profile.md into Claude's User Preferences for cross-project consistency.
- Remind them: running this skill again in a month with more data will produce a sharper profile. Profiles improve over time.