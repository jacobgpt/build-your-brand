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
   Reads the foundation, `necessary-beliefs.md` (one section per belief —
   verified in testing), `design.md` if present (exact values win over
   deriving from `visual_pillars`), and the hero from `/build:06-hero` if
   it exists:
   - `assets/hero.mp4` + `hero-poster.jpg` → autoplay muted looping video
     background, verified working (200s, correct video tag) in testing
   - no hero assets → falls back to a CSS-only hero built from `design.md`,
     also verified working — no broken references, no 404s

   > If the skill stops to ask about the CTA (no pricing/backend set yet),
   > answer it — a waitlist `[FILL: connect to real signup]` placeholder is
   > fine pre-launch. It will not invent a CTA destination.

3. Serve it from the **repo root** (not the site's own folder — it
   references shared assets by relative path):
   ```
   python3 -m http.server 8000
   ```
   Open `http://localhost:8000/records/website/<brand_id>/index.html`.

4. Read it as a stranger would:
   - Does the first line say what this is?
   - Is there a claim on the page you couldn't back up if someone asked?
   - No invented testimonials, stats, or logos — if you see one, that's a
     bug in the build, flag it.

**Done when:** site running locally, hero renders (video or fallback), no
unprovable claims.
**Next:** `/build:08-assets`
