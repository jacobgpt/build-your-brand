---
description: "Build Your Brand — Lesson 7: The website. Copy-first, design.md-driven, hero-aware."
---

# /build:07-website

1. Confirm a brand foundation exists
   (`records/brands/<brand_id>/brand_foundation.json`).

2. Build the site:
   ```
   claude -p "Use brand-website to build a website for the <brand_id> brand"
   ```
   This reads the foundation, `necessary-beliefs.md` (one section per
   belief), `design.md` if present (exact values win over deriving from
   `visual_pillars`), and the hero from `/build:06-hero` if you built it:
   - `assets/hero.mp4` + `hero-poster.jpg` present → autoplay muted
     looping video background
   - no hero assets → a CSS-only hero built from `design.md` instead, no
     broken references

   > If the skill stops to ask about the CTA (no pricing/backend set
   > yet), answer it — a waitlist `[FILL: connect to real signup]`
   > placeholder is fine pre-launch. It won't invent a CTA destination
   > for you.

3. Serve it from the **repo root** (not the site's own folder — it
   references shared assets by relative path):
   ```
   python3 -m http.server 8000
   ```
   Open `http://localhost:8000/records/website/<brand_id>/index.html`.

4. Read it as a stranger would:
   - Does the first line say what this is?
   - Is there a claim on that page you couldn't back up if someone asked?
   - Any invented testimonial, stat, or logo means something went wrong
     upstream — go back and check the source documents rather than
     publishing it.

**Done when:** site running locally, hero renders (video or fallback), no
unprovable claims.
**Next:** `/build:08-assets`
