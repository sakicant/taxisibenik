---
name: popup-cro
description: Optimize popups, modals, slide-ins, exit-intent overlays, and banners. Different conversion dynamics from in-page forms. Cover when to show, what to show, how to show it, and how not to be annoying.
triggers:
  - popup conversion
  - modal optimization
  - exit intent
  - slide-in
  - newsletter popup
  - banner conversion
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Popup CRO

Popups are powerful and easy to abuse. The line between "got me to subscribe" and "made me leave" is thin and depends on three things: trigger, content, and dismissibility.

## Gather context

Ask if not provided:

1. **Popup goal** — newsletter signup, lead capture, exit-intent recovery, announcement, discount, social proof?
2. **Trigger** — time-based, scroll-based, exit intent, click, on-load, page-specific?
3. **Current performance** — show rate, conversion rate, dismissal rate, bounce rate impact?
4. **Audience** — first-time visitors, returning, logged-in?
5. **Site context** — is the popup competing with other popups (cookie banner, chat widget)?

## Trigger rules

### Time-based
- Don't fire on landing. Wait at least 30-60 seconds.
- Even better: only after the visitor has shown engagement (scrolled past hero, viewed multiple pages).

### Scroll-based
- Trigger at 50%+ scroll. Means the visitor is engaged.
- Don't trigger right at top or right at bottom.

### Exit-intent
- Fire when mouse leaves to the URL bar (desktop) or when visitor uses back gesture (mobile).
- Best for capturing about-to-leave traffic.

### Click-based (intent popups)
- Triggered by clicking a CTA. Lowest friction since it's user-initiated.
- Highest converting popup type by far.

### What never to trigger on
- On-load, automatically.
- During reading.
- Multiple popups stacked.

## Content rules

### Headline
- Specific outcome, not generic claim.
- "Get the [specific resource] used by [specific audience]" beats "Subscribe to our newsletter."

### Single CTA
- One field, one button. Email-only is best for newsletter / lead capture.
- Action verb on the button ("Get the guide" not "Submit").

### Trust signal
- "Join X subscribers" (only if X > 1000).
- Privacy assurance ("We hate spam. One-click unsubscribe.").
- For payment popups: security badges.

### No multi-step popups
Popup interrupts. Multi-step popup interrupts twice. Capture the email, route to a thank-you page.

## Dismissibility rules

This is what most popups screw up.

- **Visible close button.** Big enough to tap on mobile (44px). Top-right corner.
- **ESC key** dismisses on desktop.
- **Click outside** dismisses (the whole faded background should be clickable).
- **Don't reappear.** Use a cookie/local-storage flag. If user dismissed, don't re-show for at least 7 days.
- **Don't penalize dismissal.** No "Are you sure you don't want this great deal?" follow-up.

If a popup feels like it's holding the user hostage, it'll hurt the brand more than help conversion.

## Frequency caps
- Max once per session. Often once per 7 days.
- Different popups don't stack — show only the highest-priority one per session.

## Mobile-specific

Google penalizes intrusive interstitials on mobile, so popup behavior on mobile must be conservative:
- Avoid full-screen popups on initial mobile visits (penalty risk).
- Banner popups (top or bottom slim) are usually safe.
- Exit-intent doesn't work on mobile the same way; trigger off scroll-up or session-end signals instead.

## Workflow

1. Define the popup's single job.
2. Pick the trigger that matches the goal.
3. Write the content (headline, micro-copy, CTA).
4. Set dismissibility correctly.
5. Apply frequency cap.
6. Test on mobile and desktop.
7. A/B test variants. Common tests: trigger timing, headline, CTA copy.

## Output format

Save audit / recommendation to `outputs/popup-cro/<popup-name>-<date>.md`:

```
## Popup audit: <name>
- Type: <newsletter / exit-intent / etc.>
- Current trigger: ...
- Current performance: <show rate, CR, dismissal rate>

## Findings
- Trigger: ...
- Content: ...
- Dismissibility: ...
- Mobile: ...
- Frequency: ...

## Recommended changes
1. <change> — <expected impact>

## A/B test plan
[Variant A vs B with hypothesis and minimum runtime]
```

## Common mistakes

- Firing on-load. Highest dismissal, lowest conversion, worst UX.
- Hard-to-find close button. Increases bounce rate.
- Re-showing after dismissal. Erodes trust quickly.
- Mobile interstitials. Hurts SEO and frustrates users.
- Multi-step popups. Compounds the interruption.

## Cross-references

For in-page forms (not popups), use `form-cro`. For paywalls and upgrade modals (different intent), use `paywall-upgrade-cro`. For lead magnets that popups deliver, use `lead-magnets`. For broader page-level optimization, use `page-cro`.
