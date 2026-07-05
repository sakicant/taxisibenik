---
name: marketing-image-creator
description: Create marketing images using AI generation and design composition. Use for blog heroes, social graphics, OG images, product mockups, profile banners, and brand assets. For paid ad image creative, see visual-ad-formats. For accessibility alt text, see alt-text-generator.
triggers:
  - generate an image
  - create a graphic
  - hero image
  - og image
  - social graphic
  - product mockup
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Marketing Image Creator

Produce marketing images that fit the brand, the placement, and the file size constraints. Pick the right approach, write a prompt that works, then optimize the output.

## Gather Context First

1. Read `context/` for brand voice, color palette, and visual references
2. Confirm the goal: blog hero, social graphic, OG image, mockup, banner, brand asset
3. Confirm the placement and required dimensions
4. Identify which image tools the user has access to before recommending one
5. Check `reference/` for an existing brand style guide before generating

## Approach by Output Type

Match the approach to what the image needs to do.

| Output type | Best approach | Watch out for |
|-------------|---------------|---------------|
| **Stylized, illustrative, painterly** | Generative AI with strong style prompt | Most generators are bad at legible text |
| **Photoreal scenes, products in context** | Generative AI tuned for photoreal | Hands, fingers, brand logos still distort |
| **Text-heavy designs, posters, quote cards** | Generative AI with strong text rendering, or compose text in a layout tool over a generated background | Some generators produce gibberish letters |
| **Quick brainstorm or concept** | Any generative AI for low-stakes iteration | Generic look without specific prompting |
| **Edits to an existing image** | Image-to-image generative model | Inconsistent style transfer across edits |
| **Branded layouts (logo + copy + image)** | Layout / composition tool, no generation | Pure composition, brings nothing new visually |

## Prompt Structure

A working AI image prompt has five parts:

```
[subject] [composition] [style] [lighting] [technical]
```

| Part | Example |
|------|---------|
| Subject | Pixel-art frog wearing a purple cape |
| Composition | Centered, full body, mid-shot |
| Style | Retro pixel art, 16-bit aesthetic |
| Lighting | Soft ambient glow, warm tones |
| Technical | 1024x1024, transparent background, sharp pixels |

Bad prompt: "a cool frog logo"
Good prompt: "Pixel-art frog with a purple cape, centered, 16-bit retro style, soft glow, transparent background, sharp pixels, 1024x1024"

## Format Specs

| Placement | Dimensions | Format | Notes |
|-----------|------------|--------|-------|
| OG image | 1200x630 | PNG/JPG | Text must be readable at 600x315 thumbnail |
| Twitter/X card | 1200x675 | PNG/JPG | Same as above |
| LinkedIn post | 1200x1200 (square) or 1200x627 | PNG/JPG | Square outperforms landscape |
| Instagram post | 1080x1080 | JPG | Sharp text, high contrast |
| Instagram story | 1080x1920 | JPG | Leave 250px top/bottom for UI |
| Blog hero | 1600x900 | WebP | Compress under 200kb |
| Profile banner | 1500x500 (X), 1584x396 (LinkedIn) | PNG | Avoid placing logo at edges |
| Favicon | 512x512 source | PNG | Test at 16x16 — most icons fail here |

## Optimization Pipeline

After generating:

1. **Crop** to exact placement dimensions (don't rely on browser scaling)
2. **Convert** to WebP for web (typically 60-80% smaller than PNG, similar quality)
3. **Compress** with an image optimizer — target under 200kb for web heroes, under 100kb for thumbnails
4. **Test** the image at the smallest size it will be displayed (mobile, thumbnail)
5. **Add alt text** before shipping (see `alt-text-generator` skill)

## Output Format

Save to `outputs/images/[purpose]/`:

```
outputs/images/blog-hero-launch/
├── prompt.md          ← the prompt that produced it
├── source.png         ← original generation
├── final.webp         ← optimized for web
└── alt-text.txt       ← accessibility text
```

Document the prompt so the user can regenerate variations later.

## Do NOT

- Generate images with text using a generator that struggles with legible text — verify the tool handles text before relying on it, or compose text in a layout tool over a generated background
- Ship a generated image without checking it at the smallest display size — most generations look great at 2048px and bad at 200px
- Skip optimization — uncompressed PNGs slow down pages and hurt SEO
- Use generated humans for testimonials or case studies — that crosses an ethical line
- Reuse the same generative aesthetic across every brand asset — it produces a "generic AI" look that hurts credibility