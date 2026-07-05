---
name: motion-graphics-creator
description: Create animated motion graphics and video content using Remotion. Use when the user wants to build animated videos, social media clips, product demos, or visual content that moves. Generates React components that render as video using the Remotion framework.
triggers:
  - create a video
  - motion graphics
  - animate this
  - make a video
  - remotion
  - animated content
allowed-tools:
  - Bash
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Motion Graphics Creator

Create professional animated video content using Remotion, a React-based framework for programmatic video.

## Setup

If no Remotion project exists, create one:

1. Create project directory with `npm init -y`
2. Install: `npm install remotion @remotion/cli @remotion/tailwind @remotion/google-fonts react react-dom typescript`
3. Create `remotion.config.ts` with Tailwind enabled
4. Create `src/Root.tsx` to register compositions
5. Create `src/style.css` with Tailwind imports
6. Start studio: `npx remotion studio`

## Composition Structure

Each video is a React component registered as a Composition:

```tsx
<Composition
  id="MyVideo"
  component={MyVideo}
  durationInFrames={300}  // 10 seconds at 30fps
  fps={30}
  width={1080}
  height={1920}  // Vertical for social
/>
```

Common formats:
- **Vertical (Reels/TikTok):** 1080x1920
- **Horizontal (YouTube):** 1920x1080
- **Square (Feed):** 1080x1080

## Animation Toolkit

### Core Remotion APIs
- `useCurrentFrame()` — current frame number
- `interpolate(frame, inputRange, outputRange)` — map frame to value
- `spring({ frame, fps, config })` — physics-based animation
- `<Sequence from={frame} durationInFrames={n}>` — scene sequencing
- `<Img src={staticFile("file.png")}>` — static assets
- `<AbsoluteFill>` — full-frame container

### Spring Configs (by feel)
- Heavy/slow: `{ damping: 28, mass: 2.5, stiffness: 40 }`
- Smooth: `{ damping: 20, mass: 1, stiffness: 60 }`
- Snappy: `{ damping: 14, mass: 0.6 }`
- Bouncy: `{ damping: 12, mass: 0.7, stiffness: 100 }`

### Easing
```tsx
const easeOut = (t: number) => 1 - Math.pow(1 - t, 3);
interpolate(frame, [0, 30], [0, 1], { easing: easeOut });
```

## Visual Patterns

### Ambient Glows
Use multiple radial gradient blobs for atmosphere:
```tsx
<div style={{
  position: "absolute", top: "15%", left: "5%",
  width: "60%", height: "35%",
  background: "radial-gradient(ellipse, #4ade8028 0%, transparent 70%)",
  filter: "blur(80px)", borderRadius: "50%",
}} />
```
Use 3-4 blobs at different positions. One can slowly drift using frame interpolation.

### Glass/Frosted Panels
```tsx
background: "linear-gradient(160deg, rgba(color, 0.12) 0%, rgba(color, 0.06) 100%)",
border: "2px solid rgba(color, 0.20)",
backdropFilter: "blur(12px)",
borderRadius: 24,
```

### Camera Rotation (3D entrance)
```tsx
const camY = interpolate(frame, [0, 35], [-42, -5], { easing: easeOut });
// Wrap scene in: perspective: 1400, transformStyle: "preserve-3d"
```

### Staggered Reveals
```tsx
items.map((item, i) => <Card delay={baseDelay + i * 6} />)
```

### Terminal Mockup
Dark rounded container with traffic light dots (red, yellow, green), monospace font, line-by-line typing animation.

## Process

1. **Start with reference.** Find visual inspiration. Extract frames with ffmpeg if it's a video.
2. **Build the scene.** One composition per video. Use AbsoluteFill for layers.
3. **Animate in phases.** Entrance (0-2s), main content (2-6s), exit/CTA (6-10s).
4. **Title comes last.** Show the visual demo first, then reveal the message as the payoff.
5. **Always end with branding.** Logo, URL, and CTA in the final seconds.

## Rendering

- Preview: `npx remotion studio`
- Render MP4: `npx remotion render [CompositionId] out/video.mp4`
- Render GIF: `npx remotion render [CompositionId] out/video.gif --codec gif`

## Fonts

Load via @remotion/google-fonts:
```tsx
import { loadFont } from "@remotion/google-fonts/Inter";
const { fontFamily } = loadFont("normal", { weights: ["700", "800", "900"] });
```

## Tips

- Social video hooks in the first second. Put text or movement immediately.
- Elements should be large enough to read on a phone.
- Use role/brand colors consistently.
- Multiple ambient glows > one strong glow.
- Heavy springs feel more premium than snappy ones for hero elements.
- Cards and UI elements should not overlap on text areas.