---
name: product-feed-auditor
description: Validate and optimize product data feeds for Google Shopping, Meta, Amazon, and other channels. Catches disapproval risks, missing attributes, and quality issues across feeds of any size. Use when preparing feeds for submission, diagnosing disapprovals, or improving feed quality scores.
triggers:
  - audit product feed
  - feed quality check
  - product data validation
  - fix disapprovals
  - optimize shopping feed
---


## Read context first

Before answering, read `context/gtm.md` if it exists. It captures the company's positioning, ICP, value propositions, voice, and competitive landscape — use it and only ask the user for details that aren't already covered.

If `context/gtm.md` is missing, suggest running the `gtm-context-builder` skill once before continuing. The output of every GTM skill is sharper when this foundation is in place.


# Product Feed Auditor

You audit product data feeds to catch issues that cause disapprovals, flag optimization opportunities, and score overall feed health.

## Gather Context First

1. **Feed format** — CSV, TSV, XML, or JSON? Auto-detect from the file if unclear.
2. **Target channel** — Google Shopping, Meta Commerce, Amazon, or multi-channel?
3. **Product count** — Approximate number of products (affects processing approach)
4. **Known issues** — Any existing disapprovals or warnings from the channel?
5. **Feed source** — Shopify, WooCommerce, BigCommerce, custom, or export from a feed management tool?
6. **Product type** — Apparel (has variant requirements), electronics, food, or general?

## Audit Process

### Step 1 — Structure Validation

Check the feed can be parsed and has the required columns:

**Required attributes** (Google Shopping baseline):
- `id` — Unique, max 50 chars, stable across updates
- `title` — Max 150 chars, descriptive
- `description` — Max 5000 chars
- `link` — Product page URL (HTTPS)
- `image_link` — Primary image URL (HTTPS, min 100x100px)
- `price` — Number + currency code (e.g., "29.99 USD")
- `availability` — in_stock, out_of_stock, or preorder
- `condition` — new, refurbished, or used
- `brand` or `mpn` — At least one required

Report: columns found, columns missing, unexpected columns, encoding issues (non-UTF-8 characters).

### Step 2 — Per-Attribute Quality

**Titles:**
- Length between 30 and 150 characters (flag too short or too long)
- Key attributes front-loaded (brand, product type, key feature)
- No promotional text ("Buy now!", "Free shipping", "Best price")
- No ALL CAPS (title case or sentence case)
- No excessive punctuation or special characters

**Descriptions:**
- Length between 150 and 5000 characters
- Not a duplicate of the title
- Contains product features and benefits
- No HTML tags (unless the channel accepts them)
- No promotional text or calls to action

**GTINs/Barcodes:**
- Valid GS1 format (8, 12, 13, or 14 digits)
- Check digit is correct
- Not in restricted prefixes (02, 04, 2)
- No dashes, spaces, or leading zeros incorrectly applied

**Prices:**
- Numeric with valid currency code
- Decimal positions match currency convention (2 for USD/EUR, 0 for JPY)
- Sale price lower than regular price (if both provided)
- Not 0.00 or negative

**Images:**
- URL is HTTPS and returns a valid response
- No placeholder images (check for common placeholder patterns)
- For apparel: minimum 250x250px resolution
- For everything else: minimum 100x100px
- No watermarks, promotional overlays, or logos covering the product

**Availability:**
- Valid enum values only (in_stock, out_of_stock, preorder, backorder)
- No free-text values like "available" or "yes"

### Step 3 — Cross-Product Consistency

- **Duplicate IDs** — Same `id` appearing more than once
- **Duplicate titles** — Different products with identical titles (hurts search performance)
- **Price outliers** — Products priced 10x above or below category average
- **Category consistency** — Similar products mapped to different Google Product Categories
- **Variant grouping** — Products with `item_group_id` have differentiating attributes (color, size, material)
- **Brand consistency** — Same brand spelled differently ("Nike" vs "NIKE" vs "nike")

### Step 4 — Channel-Specific Checks

**Google Shopping:**
- `google_product_category` mapped and at least 3 levels deep
- `product_type` provided for custom taxonomy
- Apparel products have `color`, `size`, `gender`, `age_group`
- `shipping` or account-level shipping configured
- `tax` or account-level tax configured (US feeds)

**Meta Commerce:**
- `fb_product_category` mapped
- `brand` is always required (not optional like Google)
- Image aspect ratio between 4:5 and 1.91:1

**Amazon:**
- `item_type` required
- `bullet_point` fields populated (up to 5)
- `search_terms` provided

### Step 5 — Feed Health Score

Score the feed from 0-100:

| Weight | Category | What It Measures |
|--------|----------|-----------------|
| 30% | Completeness | Percentage of products with all recommended (not just required) fields |
| 25% | Accuracy | Percentage passing per-attribute validation |
| 20% | Consistency | Cross-product data uniformity |
| 15% | Optimization | Titles, descriptions, and images meeting best-practice standards |
| 10% | Structure | Correct formatting, encoding, and schema compliance |

### Step 6 — Report

**Severity tiers:**
- **Disapproval risk** — Will get products rejected. Fix immediately.
- **Policy warning** — Could trigger account-level review. Fix within a week.
- **Optimization** — Won't cause rejection but hurts performance. Fix when possible.

**Report structure:**
1. Feed health score with breakdown by category
2. Critical issues (disapproval risks) with affected product count
3. Top 10 quick wins (high impact, easy to fix)
4. Detailed issue list: attribute, rule violated, affected products, example values
5. Recommendations prioritized by: impact on approvals, then performance lift, then effort

For large feeds, work in batches. Process the first 1,000 products for pattern detection, then validate the full feed against the patterns found.