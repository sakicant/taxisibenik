---
description: Import context and projects from a ChatGPT data export into your workspace.
---

# /migrate-chatgpt — Import from ChatGPT

Bring your ChatGPT context, projects, and patterns into this workspace. Works with a ChatGPT data export folder.

## Before starting

The user needs a ChatGPT data export. If they don't have one:

1. Go to chatgpt.com > Settings > Data Controls > Export Data
2. Wait for the email from OpenAI with the download link
3. Download and unzip the file
4. Tell the user to point this command at the unzipped folder

If the user already has the folder ready, ask them to provide the path.

## Step 1: Scan the export

Read `conversations.json` from the export folder. Build an overview:

- Total number of conversations and date range
- Group conversations by topic or theme
- Identify conversations with heavy back-and-forth (likely important projects)
- Flag any Custom Instructions or GPT configurations found

Present a numbered summary of identified themes/projects. Include a short description and approximate date range for each.

Wait for the user to select which ones to keep. Most people cut 50-70%.

## Step 2: Extract selected projects

For each selected theme, create a folder in `context/imports/` with:

- `summary.md` — what the project is, current status, key decisions made
- `insights.md` — useful conclusions, patterns, or findings from the conversations
- `materials.md` — prompts, templates, frameworks, or outputs worth keeping

Be thorough. The goal is that the user never needs to go back to the original export.

## Step 3: Analyze working patterns

Across ALL conversations (not just selected ones), analyze:

- How the user gives instructions
- How they iterate and refine outputs
- What they correct repeatedly
- What kinds of tasks they delegate to AI vs handle themselves
- Common friction points

Save as `context/working-style.md`. If this file already exists (from /hatch-2), merge the ChatGPT patterns with existing data rather than overwriting.

## Step 4: Analyze writing patterns

If the user produced written content (posts, emails, articles, copy), analyze:

- Tone and voice across different formats
- Sentence structure and paragraph preferences
- Vocabulary patterns and things they avoid
- Formatting habits

Save as `context/writing-style.md`. Same merge rule as Step 3.

## Step 5: Build profile

Condense Steps 3-4 into a compact profile (200-500 words) suitable for Claude's User Preferences. Save as `context/profile.md`.

Present the profile to the user for review. Suggest they paste it into Settings > General > Personal Preferences.

## Step 6: Summary

Report what was imported:

- Number of projects extracted and where they live
- Files created and their locations
- Key patterns discovered
- Suggested next steps (review files, update profile, set up Projects for key topics)

## Privacy note

Remind the user: the imported data stays on their machine in the workspace files. Nothing is sent to any external service. If they want to remove the original ChatGPT export folder after import, they can.