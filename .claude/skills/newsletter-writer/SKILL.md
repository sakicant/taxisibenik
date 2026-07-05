---
name: newsletter-writer
description: Write engaging email newsletters that build audience loyalty.
triggers:
  - write newsletter
  - newsletter edition
  - email digest
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Newsletter Writer

You write newsletters people look forward to opening. A good newsletter builds a relationship over time, not just a mailing list.

## Gather Context First

Check `context/` for brand voice and audience profile. Read 1-2 past editions in `content-library/` to match the established voice and avoid repeating recent angles. Ask only for what is missing:
1. **Who is the audience?** Role, interests, expertise level.
2. **What is the newsletter's promise?** What does a subscriber get every edition?
3. **What is the cadence?** Weekly, biweekly, monthly.
4. **What is the tone?** Casual, professional, opinionated, educational.

## Newsletter Architecture

### Subject Line (write last)
- Under 50 characters. Curiosity or value-driven.
- Good: "The metric nobody tracks (but should)"
- Good: "3 tools I switched to this month"
- Bad: "Monthly Newsletter - March Edition"

### Preview Text
- The first 90 characters after the subject line in most email clients.
- Extend the subject line's promise, do not repeat it.

### Opening Hook (2-4 sentences)
- Start with a story, observation, or surprising fact.
- Make it personal. The opening is what separates newsletters from corporate updates.
- Connect the hook to the main content within 3 sentences.

### Main Content (1-3 sections)
Each section follows this pattern:
1. **Context:** Why this matters right now (1-2 sentences).
2. **Insight:** The key takeaway or lesson (the meat).
3. **Application:** How the reader can use this (action step or framework).

Keep total main content to 500-800 words. Shorter editions get read more consistently.

### Curated Links (3-5 picks)
- Each link gets: **Title** + 1-sentence description of why it is worth reading.
- Organize by theme or label categories (Read, Watch, Try, Tool).
- Include one unexpected pick outside the newsletter's usual topic.

### Closing
- Personal sign-off that invites connection.
- One CTA: reply, share, visit a link, or take an action.
- Signature with name and one line of context.

## Newsletter Formats

### The Curator
3-5 links with commentary. Low effort to produce, high value if your taste is trusted. Best for: industry roundups, weekly digests.

### The Essayist
One long-form piece (600-1000 words) with a personal angle. Best for: thought leadership, building a personal brand.

### The Tactician
One actionable framework, template, or how-to per edition. Best for: skill-building audiences, professionals.

### The Hybrid
Short personal intro + 1 main insight + curated links. Best for: most newsletters. Balances depth with breadth.

## Growth and Engagement Tactics

- End with a question to drive replies. Replies improve deliverability.
- Add a "forward to a friend" CTA every 3-4 editions.
- Reference previous editions to reward long-time readers.
- Use consistent section headers so readers can scan to what they care about.
- Track open rates and click rates. If opens drop, fix subject lines. If clicks drop, fix content relevance.

## Output Format

Save the newsletter edition to `outputs/newsletters/`:

```
outputs/newsletters/[date]-edition.md
```

Include subject line, preview text, and full body copy ready to paste into an email tool.

## Do NOT
- Write "In this edition..." as the opening. Dive into the content.
- Include more than one primary CTA per edition.
- Send without a subject line test (read it on mobile, in a crowded inbox).
- Make every edition the same structure. Vary it to keep readers engaged.
- Use "Dear subscriber" or any generic greeting.
- Forget to proofread. Newsletters go to real inboxes and cannot be edited after sending.