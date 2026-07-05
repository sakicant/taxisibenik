---
name: launch-social-posts
description: Take a product launch, feature release, or announcement and create tailored posts for LinkedIn, X/Twitter, Hacker News, and other platforms. Use when you need to announce something across multiple channels with platform-appropriate messaging.
triggers:
  - launch posts
  - social media posts
  - announce on LinkedIn
  - write tweets
  - cross-platform announcement
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Launch Social Adapter

Each platform has its own culture, format constraints, and audience expectations. The same message copy-pasted across platforms underperforms. Adapt the core message to fit each channel.

## Input

Gather before writing:
1. **What's being announced?** (feature, product, milestone, content)
2. **Who cares?** (developers, PMs, marketers, executives, general)
3. **What's the one thing people should take away?**
4. **Is there a link, demo, or visual to include?**
5. **What tone matches the brand?** (check `context/` for voice guidelines)

## Platform Formats

### LinkedIn
- **Audience:** Professional network, B2B, career-focused
- **Format:** 1-3 short paragraphs (not bullet lists). Hook in the first line (visible before "see more"). 1,300 characters max for full visibility without truncation.
- **Tone:** Professional but human. Personal stories and honest insights perform best. Avoid corporate speak.
- **Structure:**
  1. Hook (personal angle, surprising insight, or bold claim)
  2. Context (what happened, what you built, what you learned)
  3. Takeaway (what this means for the reader)
  4. CTA (subtle — link in comments often outperforms link in post)
- **Do:** Use line breaks for readability. Share the story behind the announcement.
- **Don't:** Use hashtag walls, emoji bullets, or "I'm thrilled to announce" openings.

### X / Twitter
- **Audience:** Tech-savvy, fast-scrolling, values brevity and wit
- **Format:** Single tweet (280 chars) or thread (3-7 tweets)
- **Tone:** Casual, direct, clever. Personality over polish.
- **Thread structure:**
  1. Hook tweet (standalone, makes you want to read more)
  2. Problem/context (why this matters)
  3. Solution/announcement (what you did)
  4. Proof (screenshot, demo GIF, metric)
  5. CTA (try it, link, follow for updates)
- **Do:** Use visuals. Lead with the most interesting part. Make each tweet standalone.
- **Don't:** Number your tweets. Start with "Thread:" or "1/". Be boring.

### Hacker News
- **Audience:** Developers, founders, tech enthusiasts. Allergic to marketing.
- **Format:** Title + optional text post, or Show HN with description
- **Tone:** Technical, honest, understated. Anti-hype. Let the work speak.
- **Title rules:**
  - Show HN: [Product] — [what it does in plain language]
  - No superlatives ("amazing", "revolutionary")
  - No marketing language ("game-changing", "disruptive")
  - State what it does, not how great it is
- **Post body:** What you built, why, interesting technical decisions, limitations you are honest about
- **Do:** Share technical details. Acknowledge tradeoffs. Respond to comments.
- **Don't:** Shill. Use marketing language. Ignore critical feedback.

### Discord / Community
- **Audience:** Existing users and community members
- **Format:** Announcement with context, changelog style
- **Tone:** Casual, appreciative, insider-feeling
- **Structure:** What changed → why → how to try it → feedback welcome

## Output

Write all posts to `outputs/launch-posts-[topic].md`:

For each platform, provide:
1. The post text (ready to copy-paste)
2. Any visual or link to include
3. Suggested posting time (if relevant)
4. One alternative version with a different hook

## Do NOT
- Copy-paste the same text across platforms
- Use hashtags on HN or in Discord
- Open LinkedIn posts with "Excited to share" or "I'm thrilled to announce"
- Write X threads longer than 7 tweets
- Include links in the main LinkedIn post body (put in first comment instead)