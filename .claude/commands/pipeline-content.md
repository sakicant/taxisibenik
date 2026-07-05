# /pipeline-content: Content Production Pipeline

Run the full content production pipeline, passing context forward between each step.

## Steps

### 1. Plan the content
Use the campaign planner skill to identify the topic, target audience, and SEO angle. If a topic was provided, use it. Otherwise, suggest based on current priorities.

Output: topic, audience, keywords, angle.

### 2. Research
Deep dive on the topic. What competitors have written, what questions people ask, what angles are underserved. Use the market researcher skill if available.

Output: research brief with key findings and unique angles.

### 3. Write the draft
Use the blog writer skill to produce a full draft. Apply brand voice guidelines. Include research findings. Optimize structure for the SEO keywords from step 1.

Output: complete draft.

### 4. SEO review
Use the SEO optimizer skill to audit the draft. Check keyword placement, meta description, heading structure, and internal linking opportunities.

Output: SEO-optimized draft.

### 5. Repurpose
Turn the post into multiple formats: LinkedIn post, social media snippets, newsletter teaser, key quotes for graphics. Save all assets to outputs/.

Output: repurposed content assets.

## How to use

Run with a topic: `/pipeline-content [topic]`
Run without: `/pipeline-content` (will suggest topics)

Each step builds on the previous one. Present output at each stage before moving to the next.