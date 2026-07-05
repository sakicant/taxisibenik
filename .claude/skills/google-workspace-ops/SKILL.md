---
name: google-workspace-ops
description: Manage Google Workspace tools including Drive file management, Sheets data analysis, Docs drafting, Calendar scheduling, and Gmail operations. Use when working with Google tools or automating workspace tasks.
triggers:
  - google workspace
  - drive files
  - sheets data
  - docs draft
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Google Workspace Ops

Operate across Google Workspace tools with structured workflows. Each section covers one tool with common operations and output patterns.

## Prerequisites

Confirm the workspace has Google Workspace MCP tools available before proceeding. If tools are not connected, explain what is needed and stop.

## Google Drive — File Management

### Search and Organize
1. Search Drive for files matching a query, date range, or file type
2. List files in a specific folder, sorted by last modified
3. Identify orphaned files (not in any folder) or duplicates by name
4. Move files between folders based on naming conventions or dates

### Bulk Operations
- Rename files following a consistent pattern (e.g., `YYYY-MM-DD_project-name_version`)
- Generate a file inventory: name, owner, last modified, sharing status
- Flag files shared externally or with overly broad permissions

### Output
Write file inventories and audit results to `outputs/drive-inventory.md`.

## Google Sheets — Data Analysis

### Read and Summarize
1. Open a sheet by name or URL
2. Identify column headers and data types
3. Compute summary statistics: counts, averages, min/max, unique values
4. Flag data quality issues: blanks, duplicates, inconsistent formats

### Transform
- Pivot data by a categorical column
- Filter rows matching specific criteria
- Merge data from multiple sheets by a shared key column
- Generate a clean summary table

### Output
Write analysis results to `outputs/sheets-analysis-[name].md` with the source sheet linked.

## Google Docs — Drafting

### Create Structured Documents
1. Ask for the document purpose, audience, and key points
2. Generate an outline with section headers
3. Draft each section in clear, concise language
4. Add formatting: headers, bullet lists, bold for emphasis

### Review Existing Docs
- Read a Doc and summarize its contents
- Flag sections that are outdated, unclear, or missing
- Suggest structural improvements

### Output
Create or update the Google Doc directly. Save a local copy to `outputs/docs-draft-[title].md`.

## Google Calendar — Scheduling

### Availability Analysis
1. Check free/busy status across a date range
2. Identify meeting-heavy days and suggest focus blocks
3. Find mutual availability across multiple calendars

### Event Management
- Create events with title, time, attendees, and description
- Batch-create recurring events (standups, reviews, 1:1s)
- Audit calendar for conflicts, double-bookings, or back-to-back meetings

### Output
Write scheduling summaries to `outputs/calendar-summary.md`.

## Gmail — Message Management

### Triage
1. Search for messages matching criteria (sender, subject, date, label)
2. Summarize unread messages by sender or thread
3. Identify threads awaiting a reply

### Draft Responses
- Read a thread and draft a contextual reply
- Compose new messages with subject, recipients, and body
- Create template responses for recurring message types

### Output
Save drafted messages to `outputs/email-drafts.md` for review before sending.

## Cross-Tool Workflows

### Weekly Review
1. Calendar: summarize this week's meetings and next week's schedule
2. Gmail: identify threads needing follow-up
3. Drive: list recently modified files
4. Sheets: pull key metrics from tracking sheets
5. Compile into `outputs/weekly-review-[date].md`

### Meeting Prep
1. Calendar: get event details and attendees
2. Gmail: search recent threads with attendees
3. Drive: find shared documents with attendees
4. Compile a prep brief in `outputs/meeting-prep-[event].md`

## Do NOT
- Send emails or create events without explicit user confirmation
- Delete or permanently modify files without confirmation
- Share files with new people without confirming the sharing intent
- Assume all Google tools are available — check first