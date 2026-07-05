# /intelligence — GTM Learnings Log

Capture and retrieve GTM intelligence so wins, losses, and objections become reusable knowledge instead of tribal memory.

## Modes

- `/intelligence add [what you learned]` — log a new insight
- `/intelligence find [topic]` — search existing entries
- `/intelligence review` — summarize what has been captured in the last 30 days

## When you add

Walk the user through a short capture:

1. **Source** — campaign, call, experiment, feedback, manual hunch.
2. **Insight** — one-sentence takeaway. Concrete, not vague. "Subject lines with the prospect's city outperform generic geo references by ~20% in enterprise" beats "personalization works."
3. **Segment** — ICP, role, industry, deal stage. Which slice this applies to.
4. **Confidence** — `hypothesis` (one data point), `validated` (repeatable in one channel), `proven` (holds across channels or over time).
5. **Evidence** — link or note for where the insight came from.

Append to `context/intelligence.md` under the right section (Wins / Losses / Objections / Messaging / Channels). Create the file with these sections if it does not exist. One bullet per learning, tagged with segment and confidence.

## When you find

Search `context/intelligence.md` and related `outputs/` files for matching entries. Return:
- Top 3 most relevant entries with their confidence level.
- Any conflicting entries (one says X works, another says it does not) flagged for review.
- A suggested next action ("you have a validated learning here — apply it to [current work]").

## When you review

Summarize additions from the last 30 days: what was learned, which segments were covered, which are underrepresented. Flag stale hypotheses (older than 60 days, never validated) for retirement.

Usage: `/intelligence [add|find|review] [optional text]`
Examples:
- `/intelligence add short subject lines beat long ones in cold outreach to ops leaders`
- `/intelligence find pricing objections for mid-market`
- `/intelligence review`