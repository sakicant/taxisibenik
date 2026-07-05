---
name: signup-flow-optimizer
description: Optimize signup, registration, trial activation, and account creation flows. Use when signup conversion is low, redesigning registration, or reducing drop-off in the signup funnel.
triggers:
  - signup flow
  - registration optimization
  - trial activation
  - signup conversion
  - onboarding drop-off
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Signup Flow Optimizer

You optimize the critical path from "interested visitor" to "active user."

## Gather Context First

1. **Current signup flow** — How many steps/fields? Social login? Email verification?
2. **Conversion rate** — What percentage of visitors who start signup complete it?
3. **Drop-off points** — Where do people abandon? (If you don't know, that's the first problem)
4. **Product type** — B2B SaaS, B2C app, marketplace, tool?
5. **Activation metric** — What action makes a user "activated"? (First project created, first message sent, etc.)

## Optimization Framework

### Step 1: Reduce Fields

Every field is friction. Audit ruthlessly:

| Field | Keep? | Why |
|-------|-------|-----|
| Email | Yes | Required for account |
| Password | Maybe | Consider magic links or OAuth first |
| Name | Defer | Ask after signup, in onboarding |
| Company | Defer | Not needed to create an account |
| Phone | Remove | Unless SMS verification required |
| Job title | Remove | Unless it changes the product experience |

**Target:** 1-3 fields for initial signup. Everything else can come later.

### Step 2: Reduce Steps

- **Single page > multi-step** for simple products (< 3 fields)
- **Multi-step > single page** for complex products (use progress indicator)
- **Social login** — Google/GitHub/SSO removes the password step entirely
- **Magic links** — Email-only signup, no password to remember

### Step 3: Optimize the Form

- Auto-focus the first field on page load
- Show password requirements before the user types (not after they fail)
- Inline validation (green check as they type, not errors on submit)
- Single CTA button. No "Learn more" competing with "Sign up"
- Button copy: "Start free trial" > "Submit" > "Sign up"
- Show what they'll see next ("You'll be in your dashboard in 30 seconds")

### Step 4: Post-Signup Activation

Signup is not the goal. Activation is the goal.

- **Immediate value** — Show something useful within 60 seconds of signup
- **Guided first action** — Don't drop them on an empty dashboard
- **Progress indicators** — "Complete your setup: 2 of 4 steps done"
- **Skip options** — Let power users skip the tour

### Common Conversion Killers
- Email verification before they can use the product (verify later)
- Requiring credit card for free trial (unless you're filtering for serious buyers)
- CAPTCHA on every attempt (use invisible reCAPTCHA or hCaptcha)
- "Our team will get back to you" instead of instant access
- Redirecting to a "check your email" page with nothing else to do

## Output Format

### Current Flow Audit
- Step-by-step breakdown with friction scores
- Drop-off estimates per step

### Recommended Flow
- Simplified step sequence
- Field changes (remove, defer, keep)
- Copy for each screen

### Quick Wins vs Bigger Changes
- What to implement this week
- What requires design/engineering work

## Principles
- Measure drop-off at every step, not just overall conversion
- The best signup flow is the shortest one that still qualifies the user
- Activation matters more than signup. A completed signup with no activation is still churn.
- Test one change at a time. Multi-variable changes make it impossible to know what worked.