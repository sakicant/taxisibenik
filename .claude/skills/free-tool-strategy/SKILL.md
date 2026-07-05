---
name: free-tool-strategy
description: Plan a free interactive tool as a marketing channel. Free tools generate leads, demonstrate capability, build SEO authority, and seed AI citations — when designed well. Use when user mentions free tool, calculator, audit tool, generator, ROI calculator, or "should I build a free tool."
triggers:
  - free tool
  - calculator
  - audit tool
  - generator
  - free version
  - tool as marketing
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Free Tool Strategy

Plan a free tool that earns its keep as a marketing asset. Free tools work as growth levers when the tool is genuinely useful, the audience overlaps with the product's, and the build cost is reasonable.

## Why free tools work

- **Lead capture** — users hit the tool, get value, often give an email for the saved version.
- **SEO authority** — tools rank for "[task] calculator" / "[topic] audit tool" queries with low competition.
- **AI citations** — AI search engines cite tools as authoritative answers ("here's a calculator for that").
- **Trust + brand** — the tool demonstrates the brand's depth without a sales pitch.
- **Network effects** — sharable tools spread (Hubspot's Website Grader is the canonical example).

## When NOT to build a free tool

- The audience is too small to amortize the build cost.
- The tool would commoditize the paid product (give away core value).
- The team can't maintain it. A broken free tool damages trust.
- The "tool" is really a content piece (then make it a piece of content, see `lead-magnets`).

## Categories of useful free tools

| Category | Example | Why it works |
|---|---|---|
| Calculators | ROI calculator, pricing calculator, mortgage calculator | Numbers people genuinely want, easy to share |
| Audits | Website audit, SEO audit, security audit | Reveals problems the product solves |
| Generators | Headline generator, business name generator, terms-of-service generator | Saves time, captures intent ("about to launch a business") |
| Converters | Currency converter, file format converter, color converter | High-volume utility traffic |
| Lookups | Domain lookup, IP lookup, certificate checker | Authoritative reference traffic |
| Mini-versions | Free tier of the paid product | Direct conversion path |

## Workflow

### Step 1: Pick the right tool
Score candidate tools on four axes:
- **Audience overlap with paid product**: high = same buyer persona.
- **SEO opportunity**: search volume for "<tool name>" or "<task> calculator" minus competition.
- **Build cost**: hours to ship vs. value delivered.
- **Maintenance**: how often will it break (data sources, APIs, deprecation).

Pick the highest combined score. Default to calculators or single-purpose audits — they're cheap to build and rank well.

### Step 2: Define the input/output
- Single-page tool: one input, one output. No multi-step wizard.
- Email capture: optional. Gate the saved/PDF version, not the result itself. Show the value first.
- Branding: subtle. Logo, "made by [brand]" footer. Don't crowd the tool with CTAs.

### Step 3: SEO setup
- Dedicated landing page (`/tools/<name>` or `/<name>`).
- Title tag: "[Tool name] — Free [category] | [Brand]".
- H1 = the user's task ("Calculate your CAC payback period").
- Below the tool, add 500+ words of context (how to use, what the inputs mean, common mistakes).
- Schema: SoftwareApplication or HowTo.
- Cross-link from the homepage and relevant blog posts.

### Step 4: Distribution
- Submit to AI tool directories (see `directory-submissions`).
- Publish a blog post explaining the methodology.
- Pitch the tool to journalists writing about the topic ("you can use this calculator to verify").
- Add it to the email signature for 30 days post-launch.
- Pin on social profiles.

### Step 5: Connect to the paid product
The tool is the entry point. Where does the user go next?
- After result: contextually suggest the paid product ("This calculator showed you X. [Brand] automates Y.").
- Email follow-up if captured: drip sequence introducing the paid product (see `email-sequence-builder`).
- Logged-in version: free tool inside the product, deeper features behind upgrade.

## Output format

Save to `outputs/free-tool-strategy/<tool-name>.md` with:
- Tool concept (one sentence).
- Input/output spec.
- Build cost estimate (hours, stack, APIs needed).
- SEO plan (target query, page structure, schema).
- Distribution checklist.
- Connection-to-paid-product flow.

## Common mistakes

- Building a tool unrelated to the paid product. No conversion path.
- Gating the tool itself behind email. Conversion craters.
- Not maintaining it. APIs deprecate; tools break; trust dies.
- Over-engineering — multi-step wizard when one form would do.
- Skipping the SEO landing page setup. Tool exists but no one finds it.

## Cross-references

For the lead magnet / downloadable that pairs with the tool, see `lead-magnets`. For the after-capture email flow, see `email-sequence-builder`. For the landing page copy and CRO, see `landing-page-writer` and `page-cro`. For directory submissions, see `directory-submissions`. For SEO around the tool, see `programmatic-seo-builder` and `ai-seo-optimizer`.
