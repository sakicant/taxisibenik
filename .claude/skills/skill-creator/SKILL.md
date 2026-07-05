---
name: skill-creator
description: Create professional Claude Code skills that extend Claude's capabilities. Use when building a new skill from scratch, converting workflows into reusable skills, creating domain-specific agents, or packaging instructions for consistent AI behavior. Generates well-structured SKILL.md files with proper YAML frontmatter, clear instructions, and optional bundled resources.
triggers:
  - create a skill
  - new skill
  - build a skill
  - make a skill
---

# Skill Creator

Create professional, effective Claude Code skills that transform Claude into a specialized agent for any domain.

## What Makes a Great Skill

Skills are "onboarding guides" that turn Claude from a generalist into a specialist. The best skills:

1. **Are concise.** Claude is already smart. Only add what Claude doesn't know.
2. **Have clear triggers.** The description tells Claude exactly when to activate.
3. **Provide actionable instructions.** Every line should guide behavior.
4. **Match freedom to fragility.** Precise steps for critical tasks, flexibility for creative ones.

## Skill Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name + description)
│   └── Markdown instructions
└── Optional resources/
    ├── scripts/      # Reusable code
    ├── references/   # Documentation to load as needed
    └── assets/       # Templates, images, files for output
```

## Creating a Skill: Step-by-Step

### Step 1: Define the Purpose

Before writing anything, answer:
- **What task does this skill help with?** (Be specific)
- **What would trigger this skill?** (User says what?)
- **What does Claude NOT already know?** (This is what you'll teach)
- **What's the expected output?** (Document, code, analysis, etc.)

### Step 2: Write the YAML Frontmatter

The frontmatter is how Claude decides to use your skill.

```yaml
---
name: your-skill-name
description: [What it does] + [When to use it]. Be specific about triggers and use cases.
---
```

**Good description:**
```yaml
description: Create professional marketing blog posts optimized for SEO. Use when the user asks to write blog posts, articles, content marketing pieces, or SEO-optimized content. Generates engaging, well-structured posts with headlines, subheadings, and calls-to-action.
```

**Bad description:**
```yaml
description: Helps with marketing.
```

### Step 3: Write the Instructions Body

Structure your instructions:

```markdown
# Skill Name

[1-2 sentence overview]

## Before Starting

Understand the context:
- [Key question 1 to ask/determine]
- [Key question 2]

## Process

### Phase 1: [Name]
[Instructions]

### Phase 2: [Name]
[Instructions]

## Output Standards

The final output must:
- [Requirement 1]
- [Requirement 2]

## Example

**User request:** "[Example input]"
**Output:** [Brief description of expected output]
```

### Step 4: Calibrate Freedom Level

**High freedom** (guidelines only) for creative tasks:
```
Choose a tone that matches the audience: professional for B2B, conversational for consumer brands.
```

**Medium freedom** (patterns with flexibility) for semi-structured tasks:
```
Structure the blog post as:
1. Hook (question or bold statement)
2. Problem (what the reader struggles with)
3. Solution (your main content)
4. Call-to-action (what to do next)
```

**Low freedom** (exact steps) for critical tasks:
```
Execute these steps in order:
1. Run \`python scripts/validate.py\`
2. Check output for errors
3. If errors, fix and re-run
4. Only proceed when validation passes
```

## Common Mistakes to Avoid

1. **Vague descriptions.** Be specific about triggers.
2. **Teaching Claude what it knows.** Don't explain basic concepts.
3. **Too much text.** Every token costs context space.
4. **Missing examples.** Examples are worth 1000 words of explanation.
5. **Wrong freedom level.** Don't over-specify creative tasks or under-specify critical ones.

## When to Add Bundled Resources

| Resource Type | When to Include |
|--------------|-----------------|
| scripts/ | Same code gets rewritten repeatedly |
| references/ | Domain knowledge Claude needs to look up |
| assets/ | Templates, images, or files used in output |

## Final Checklist

Before finishing:
- [ ] Description clearly states WHAT and WHEN
- [ ] Instructions are actionable, not theoretical
- [ ] Only includes information Claude doesn't already have
- [ ] Examples demonstrate expected behavior
- [ ] Freedom level matches task fragility
- [ ] Total length under 500 lines (split if longer)