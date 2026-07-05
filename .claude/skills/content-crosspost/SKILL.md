---
name: content-crosspost
description: Take a single piece of content and adapt it for multiple platforms (LinkedIn, X, Discord, newsletter, blog) with platform-specific formatting, character limits, and tone adjustments.
triggers:
  - crosspost
  - repurpose content
  - multi-platform
  - adapt for
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Content Crosspost

Take one piece of content and produce platform-ready versions for each target channel. Each platform has different rules for format, length, tone, and engagement patterns.

## Input

Ask for:
1. **Source content** — the original piece (blog post, announcement, update, etc.)
2. **Target platforms** — which channels to adapt for (default: all)
3. **Core message** — the single takeaway readers should remember
4. **Call to action** — what the reader should do next (link, reply, sign up, etc.)
5. **Tone adjustment** — any platform-specific tone shifts from the source

## Platform Rules

### LinkedIn Post
- **Length:** 1,300 characters max for full visibility without "see more" (3,000 char hard limit)
- **Structure:** Hook line (first sentence visible in feed), 2-3 short paragraphs, CTA at the end
- **Formatting:** Line breaks between paragraphs, no markdown (LinkedIn renders plain text), use emojis sparingly (max 2-3)
- **Hashtags:** 3-5 relevant hashtags at the end, not inline
- **Tone:** Professional but personal. First person. Story-driven hooks work best.
- **Avoid:** Walls of text, bullet-heavy posts, corporate speak, engagement bait ("agree?")

### X (Twitter) Thread
- **Length:** 280 characters per post, 4-8 posts per thread
- **Structure:** Post 1 is the hook (must stand alone), final post has CTA and link
- **Formatting:** Short sentences, one idea per post, number posts (1/6, 2/6...)
- **Hashtags:** 1-2 max, only on the first or last post
- **Tone:** Conversational, punchy, opinionated. Compress ruthlessly.
- **Avoid:** Run-on threads (>10 posts), hashtag spam, threads that require reading all posts to get value

### X Single Post
- **Length:** 280 characters
- **Structure:** One sharp observation or takeaway + optional link
- **Tone:** Direct, quotable, slightly provocative

### Discord Announcement
- **Length:** 500-1,000 characters ideal
- **Structure:** One-line summary, then details, then CTA
- **Formatting:** Markdown supported (bold, headers, code blocks, links)
- **Tone:** Community-first, casual but informative. Address the group directly.
- **Include:** @mentions or role pings if appropriate

### Newsletter Section
- **Length:** 150-300 words
- **Structure:** Header, 2-3 paragraphs, CTA link/button
- **Formatting:** HTML-safe. Short paragraphs. Bold key phrases. One link per CTA.
- **Tone:** Personal, like writing to a friend. "Here's what happened this week..."
- **Avoid:** Multiple CTAs competing, long paragraphs, no personalization

### Blog Post
- **Length:** 600-1,500 words
- **Structure:** Title, intro hook, 3-5 sections with headers, conclusion with CTA
- **Formatting:** Full markdown. Headers, code blocks, images, links.
- **Tone:** Authoritative but accessible. Teach something.
- **SEO:** Include the primary keyword in the title and first paragraph

## Adaptation Process

1. **Extract the core.** Identify the one-sentence takeaway from the source.
2. **Map to formats.** For each platform, decide which angle works best.
3. **Write platform-native.** Do not just truncate the source. Rewrite for each platform's native style.
4. **Add platform hooks.** Each platform rewards different opening patterns:
   - LinkedIn: personal story or surprising data point
   - X: bold claim or contrarian take
   - Discord: "Hey everyone" + what's new
   - Newsletter: "This week I..." or "Quick update:"
   - Blog: question or problem statement
5. **Check constraints.** Verify character limits, formatting rules, hashtag counts.

## Output

Write all versions to `outputs/content/crosspost-[topic].md` with clear headers:

```markdown
# Crosspost: [Topic]
Source: [link or description of original]

## LinkedIn
[post text]

## X Thread
1/ [post 1]
2/ [post 2]
...

## Discord
[announcement text]

## Newsletter
[section text]

## Blog
[full post]
```

## Do NOT
- Copy-paste the same text across platforms — each version must be platform-native
- Exceed character limits — check before finalizing
- Use hashtags on platforms where they do not add value (Discord, newsletter)
- Include links in every sentence — one CTA per platform version
- Write generic "check this out" CTAs — be specific about what the reader gets