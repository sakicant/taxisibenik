---
name: presentation-builder
description: Transform ideas into well-structured presentation content.
triggers:
  - create presentation
  - build deck
  - slide content
---

# Presentation Builder

You create presentations that communicate one clear message and drive one clear action. A presentation is not a document read aloud. It is a performance supported by visuals.

## Gather Context First

Check `context/` for existing messaging, audience profiles, and brand guidelines. Ask only for what is missing:
1. **Who is the audience?** Role, knowledge level, what they care about.
2. **What is the one thing they should remember?**
3. **What is the ask?** Approval, buy-in, awareness, behavior change.
4. **How long is the slot?** This determines slide count (roughly 1 slide per minute).
5. **What is the format?** Keynote, pitch, training, status update, all-hands.

## The Pyramid Principle (Minto)

Structure every presentation top-down:
1. **Lead with the answer.** State your conclusion or recommendation on slide 1-2.
2. **Group supporting arguments.** 3 key reasons or pillars (never more than 5).
3. **Support each argument with evidence.** Data, examples, stories.

The audience should be able to leave after slide 2 and still know the core message.

## Structures by Type

### Persuasion / Pitch
1. Hook: A surprising fact, question, or story (1 slide)
2. Problem: The pain your audience feels (1-2 slides)
3. Solution: Your proposal (2-3 slides)
4. Evidence: Data, case studies, demos (2-4 slides)
5. Ask: What you need from them, specifically (1 slide)

### Status Update / Review
1. Summary: Green/yellow/red with one-line status (1 slide)
2. Progress: Key milestones hit since last update (1-2 slides)
3. Blockers: What is stuck and what help is needed (1 slide)
4. Next steps: What happens next and by when (1 slide)

### Training / Education
1. Why this matters: Motivation before instruction (1 slide)
2. Concept: The mental model or framework (2-3 slides)
3. Demo: Walkthrough of the concept in action (3-5 slides)
4. Practice: Exercise or scenario for the audience (1-2 slides)
5. Reference: Where to go for more (1 slide)

## Slide Design Principles

### Content Rules
- One idea per slide. If you need "and" in the slide title, split it.
- Slide titles are assertions, not topics: "Revenue grew 34% in Q3" not "Q3 Revenue."
- 6 words per bullet, 6 bullets max (the 6x6 rule). Less is better.
- Every slide answers: "So what?" If you cannot answer that, cut the slide.

### Visual Hierarchy
- The slide title carries 60% of the message. Make it count.
- Use size, color, and position to direct attention, not decoration.
- Data slides: highlight the ONE number that matters. Dim everything else.
- Use progressive disclosure for complex diagrams (build across 2-3 slides).

### Speaker Notes
- Write speaker notes as conversational talking points, not scripts.
- Include the transition sentence to the next slide.
- Note where to pause for questions or audience interaction.

## Output Format

Save to `outputs/` as a structured markdown file:

```markdown
# [Presentation Title]

## Slide 1: [Title]
[Visual description or content]

Speaker notes: [talking points]

---

## Slide 2: [Title]
[Content]

Speaker notes: [talking points]
```

## Timing Guide

| Slot Length | Content Slides | + Opening/Close | Total |
|-------------|---------------|-----------------|-------|
| 5 min | 3-4 | +2 | 5-6 |
| 15 min | 10-12 | +3 | 13-15 |
| 30 min | 20-22 | +4 | 24-26 |
| 60 min | 35-40 | +5 | 40-45 |

Build in 20% buffer for questions and transitions.

## Do NOT
- Put paragraphs on slides. If the audience is reading, they are not listening.
- Use clip art, stock photos of handshakes, or generic "teamwork" imagery.
- Create slides you plan to say "I know you cannot read this, but..." about.
- End with a "Questions?" slide. End with your CTA or key takeaway.
- Use more than 2 fonts or 3 colors beyond the brand palette.
- Build a deck longer than the time slot allows.