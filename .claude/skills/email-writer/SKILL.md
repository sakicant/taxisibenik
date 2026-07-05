---
name: email-writer
description: Write clear, effective emails for any business context.
triggers:
  - write email
  - draft email
  - email template
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Email Writer

You write emails that get read and get responses. Every email has one job. Identify that job before writing a single word.

## Gather Context First

Check `context/` files for voice guidelines and audience information. If `content-library/` has past emails to similar recipients or for similar purposes, scan one or two to match tone. Ask only for what is missing:
1. **Who is the recipient?** Role, relationship, familiarity level.
2. **What is the purpose?** Request, update, follow-up, introduction, escalation.
3. **What action do you need?** Approval, reply, attendance, review, payment.
4. **What is the deadline?** Explicit date or "no rush."

## The SCQA Framework

Use Situation-Complication-Question-Answer for emails requiring persuasion or decision-making:

- **Situation:** Shared context the reader already knows (1 sentence).
- **Complication:** The problem, change, or tension (1-2 sentences).
- **Question:** The implicit question this raises (often unstated but shapes the email).
- **Answer:** Your recommendation or ask (the core of the email).

For simple informational emails, skip SCQA and use direct structure instead.

## Email Anatomy

### Subject Line (write last)
- Under 50 characters. Specific, not clever.
- Include the action needed: "Approval needed: Q3 budget by Friday"

### Opening (1-2 sentences)
- State why you are writing. No throat-clearing.
- Good: "Following up on our Thursday call about the vendor contract."
- Good: "Need your sign-off on the revised timeline before I send it to the client."

### Body (2-4 short paragraphs)
- Front-load the most important information.
- One paragraph per point. No walls of text.
- Use bold for key dates, numbers, or names the reader must not miss.
- If listing more than 3 items, use bullet points.

### Call to Action (1 sentence)
- One CTA per email. Make it specific and time-bound.
- Good: "Can you reply with your preferred option by end of day Wednesday?"
- Bad: "Let me know your thoughts."

### Sign-off
- Match formality to the relationship. "Best" for neutral, "Thanks" when asking, name-only for ongoing threads.

## Email Types and Patterns

### Request Email
Subject -> Context (1 sentence) -> The ask -> Why it matters -> Deadline -> CTA

### Status Update
Subject with status label -> Summary (1-2 sentences) -> Key updates as bullets -> Blockers or decisions needed -> Next steps

### Follow-Up
Reference the previous interaction -> New information or reminder -> Restate the ask -> Adjusted deadline if needed

### Escalation
State the issue clearly -> Impact if unresolved -> What you have already tried -> What you need from this person -> Timeline

### Introduction Email
Why you are connecting these two people -> One paragraph on Person A -> One paragraph on Person B -> Suggest next step -> Move yourself to BCC

## Tone Calibration

| Audience | Tone | Example |
|----------|------|---------|
| Executive | Direct, data-driven, brief | "Revenue impact: 240K. Recommend Option B." |
| Peer | Conversational, collaborative | "Thinking we should push the launch a week. Thoughts?" |
| Client | Professional, reassuring | "We identified the issue and the fix ships tomorrow." |
| Cold contact | Respectful, specific, short | "Saw your talk at Config. Quick question about your design system approach." |

## Output Format

Produce the email as plain text:

```
Subject: [subject line]

[email body]

[sign-off]
[name]
```

If the user asks for variants, provide 2-3 versions with a one-line note explaining what each optimizes for (brevity, warmth, urgency). Save drafts to `outputs/emails/`.

## Do NOT
- Start with "I hope this email finds you well" or any filler opening.
- Include more than one CTA per email.
- Write emails longer than 200 words unless the content genuinely requires it.
- Use passive voice for the ask ("It would be great if..." -> "Please review by Friday.").
- Add false urgency. If there is no deadline, say so.
- Use jargon the recipient would not use themselves.