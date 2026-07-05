---
name: extract-my-voice
description: Analyze actual writing across connected tools (Slack, Gmail, Notion) to create a personal voice reference file. Use when you want Claude to write like you.
triggers:
  - extract my voice
  - learn my writing style
  - match my tone
  - write like me
  - my voice
---

# Extract My Voice

Analyze the user's actual writing across connected sources and create a voice reference file that Claude can use to match their tone and style.

## Sources (check in order, use what's available)

1. **Slack**: Search for messages by the user. Read across multiple channels. Minimum 50 messages for a useful analysis.
2. **Gmail**: Read sent emails. Look for variety: different recipients, different purposes, different levels of formality.
3. **Notion/Docs**: Read authored pages and documents. Look for longer-form writing.
4. **Provided samples**: If no sources are connected, ask the user to paste 3-5 examples of their writing. Different formats if possible (email, post, doc, message).

## Analysis

For each source, identify:

- **Default tone**: where do they sit on formal/casual, warm/neutral, confident/tentative
- **Sentence rhythm**: short/long, varied/consistent, fragments or full sentences
- **Openings and closings**: how they start and end emails, messages, documents
- **Formatting preferences**: bullets vs prose, headers vs flat text, emoji usage
- **Vocabulary fingerprint**: words they reach for, words they consistently avoid
- **Register shifts**: how does tone change by audience, channel, or format?
- **Paragraph structure**: length, density, how they break up ideas

If the user writes in multiple languages, analyze each language separately. Voice often changes significantly between languages.

## Output

Create `context/my-voice.md` with:

1. A prose description of their voice (not a list of rules, a description that reads naturally)
2. 3-5 short quoted examples that capture the style, pulled from actual writing
3. A "do / don't" section with specific guidance for Claude:
   - Words and phrases to use
   - Words and phrases to avoid
   - Formatting rules (line length, list style, emoji policy)
   - Tone rules by context (emails vs posts vs docs)
4. Separate sections per language if they write in multiple languages

## After saving

Tell the user: "I'll use this file as reference whenever you ask me to write something. If I drift from your voice, tell me and I'll update the file."

If `context/writing-style.md` already exists (from /hatch-2 or Build My Profile), merge the voice analysis into it rather than creating a duplicate. The voice file is the writing-focused subset of the full profile.