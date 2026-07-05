---
name: ai-video-producer
description: Plan and produce marketing videos using AI generation, AI avatars, and screen recording. Use for product demos, explainers, social clips, ads, and talking-head videos. For programmatic animated videos in code, see motion-graphics-creator. For video content strategy, see social-media-calendar.
triggers:
  - make a video
  - ai video
  - explainer video
  - product demo video
  - talking head video
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# AI Video Producer

Plan and produce marketing videos using AI generation, AI avatars, and screen recording. Pick the right approach for the format, then ship.

## Gather Context First

1. Read `context/` for brand voice, audience, and product positioning
2. Confirm the goal: demo, explainer, social clip, ad, testimonial, tutorial
3. Confirm the platform: YouTube, TikTok/Reels/Shorts, website, paid ads, sales deck
4. Confirm the length, presenter format, and existing assets
5. Identify which production tools the user has access to before recommending a workflow

## Format → Approach Matrix

Pick the approach by format, not by hype.

| Format | Best for | Production approach |
|--------|----------|---------------------|
| Talking head | Explainers, course content, sales | AI avatar tool, or recorded human |
| Product demo | Feature walkthroughs, onboarding | Screen recording + voiceover |
| Cinematic B-roll | Brand films, hero videos | Text-to-video model, treat as 5-8s clips |
| Stylized clips | Social, ads, hooks | Text-to-video model with strong style prompts |
| Animated explainer | Concepts, data viz | Programmatic video in code (see motion-graphics-creator) |
| Social slideshow | Quick wins, lists, tips | Mobile editor + AI voiceover |

## Production Approach

### 1. Talking head with AI avatar

Use when the founder won't film, or content needs frequent updates.

- Script first — write the full dialogue, target 150 words per minute
- Pick an avatar that matches brand seriousness (cartoonish vs photoreal)
- Render in batches — one render per script section, splice in editor
- Add B-roll over the avatar every 5-7 seconds to break visual monotony

### 2. Product demo

Highest-converting format for SaaS.

- Script the demo path before recording — no exploration on camera
- Record at 2x speed if the UI is fast, then slow to 1x in post for clarity
- Use cursor highlights, click animations, and zoom-ins on key moments
- Add captions — 80% of social viewers watch muted

### 3. Generative cinematic

Use sparingly. Generative video still struggles with hands, text, and continuity.

- Generate 5-8 second clips, not 30 seconds
- Storyboard before generating — text-to-video burns credits fast
- Treat it as B-roll for a voiceover, not as a standalone narrative
- Reject any clip with morphing faces, broken text, or warped objects

## Script Structure (universal)

| Beat | Duration | Purpose |
|------|----------|---------|
| Hook | 0-3s | Stop the scroll. Question, claim, or visual contradiction. |
| Problem | 3-15s | Name the pain in the viewer's language |
| Solution | 15-45s | Show the product solving it |
| Proof | 45-60s | Result, testimonial, or data point |
| CTA | Last 5s | One action, no choices |

For ads, compress everything — hook + solution + CTA in 15s.

## Output Format

Save the production plan to `outputs/video-[name]/plan.md`:

```
## Video Brief
- Goal: [what action should the viewer take]
- Platform: [where it ships]
- Length: [target duration]
- Format: [talking head | demo | generative | mixed]

## Production setup
- Generation: [the AI generation tool the user has access to]
- Editor: [the video editor the user works in]
- Voiceover: [AI voice tool, recorded, or avatar built-in]

## Script
[Full script with timestamps and visual notes]

## Shot list
[Per-clip prompts, screen recordings, or avatar takes]

## Captions + thumbnails
[Caption file format, thumbnail plan]
```

Save the final video to `outputs/video-[name]/` with the script, source clips, and exported file.

## Do NOT

- Promise photoreal generative video for human-centric scenes — current models still break on faces and hands
- Skip the script — improvising on camera produces 3x more re-takes
- Forget captions — most platforms autoplay muted
- Use copyrighted music — pull from a royalty-free music library or commission audio
- Mix more than 2 visual styles in one video — viewers read it as amateur