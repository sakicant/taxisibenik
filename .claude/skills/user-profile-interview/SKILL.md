---
name: user-profile-interview
description: Build a personal profile through a conversational interview. Creates context/user-profile.md so Claude adapts to how you work. No MCP tools needed.
triggers:
  - build my profile
  - profile interview
  - learn about me
  - user profile
---

# User Profile Interview

Build a profile through a short conversation. The result is `context/user-profile.md`.

Check if `context/user-profile.md` already exists. If so, ask: "You already have a profile. Update it, start fresh, or skip?"

## The Interview

Ask one section at a time. Don't dump all questions at once.

### Section 1 — Role and Context
- What's your role? What do you spend your days doing?
- What tools do you use most?
- Who do you work with most closely?

### Section 2 — Working Preferences
- Do you prefer quick answers or thorough explanations?
- Step by step, or answer with option to ask follow-ups?
- How do you feel about suggestions you didn't ask for?

### Section 3 — Communication Style
- Bullet points or flowing paragraphs?
- Formal or casual from Claude?
- Words, phrases, or patterns that annoy you?
- Multiple languages? Which and when?

### Section 4 — What Frustrates You
- Most annoying thing an AI assistant can do?
- Specific behaviors to avoid?
- What does "done" look like? Summary or silent delivery?

### Section 5 — What Works Well
- When was AI help genuinely useful? What made it work?
- Formats or approaches that click for you?

## Generate the Profile

Create `context/user-profile.md` in third person ("They prefer..."). Sections: Role, Working Preferences, Communication Style, Pet Peeves, What Works, Notes.

Show the user the profile before saving. Ask: "Does this capture how you work?"

After saving, suggest pasting a condensed version into Claude's User Preferences for cross-workspace consistency.