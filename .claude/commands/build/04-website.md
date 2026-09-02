---
description: "Build Your Brand — Lesson 4: Website. Copy-first, on-brand, self-contained HTML from the foundation."
---

# /build:04-website

> **Repo-reality note:** the draft course script had separate lessons for a
> brand guide (HTML+PDF) and a `design.md` design-tokens file before the
> website. Neither skill exists in this repo — only `brand-foundation`,
> `aphrodite-direction`, `hephaestus-production`, and `brand-website` do.
> `brand-website` derives its own palette/type straight from
> `visual_pillars` in the foundation JSON, so this lesson goes straight
> from foundation to site. If you build `brand-guide` or `design-tokens`
> skills later, insert them here and update this file.

1. Confirm a brand foundation exists at `records/brands/<brand_id>.json`
   (built in `/build:03-foundation`). If not, stop — go back.

2. Build the site:
   ```
   claude -p "Use brand-website to build a website for the <brand_id> brand"
   ```
   This reads the foundation (and the research file, and any built asset in
   `records/assets/` if one already exists — it'll become the hero image; if
   none exists yet, the skill uses a CSS-only hero from the brand's palette
   instead. That's fine — a real asset from `/build:06-build` can be swapped
   in as the hero later, but it is NOT required to build the site now).

3. Serve it from the **repo root** (not the site's own folder — it references
   shared assets by relative path):
   ```
   python3 -m http.server 8000
   ```
   Open `http://localhost:8000/records/website/<brand_id>/index.html`.

4. Read it as a stranger would:
   - Does the first line say what this is?
   - Is there a claim on the page you couldn't back up if someone asked?
   - No invented testimonials, stats, or logos — if you see one, that's a
     bug in the build, flag it.

**Done when:** site running locally, read end to end, no unprovable claims.
**Next:** `/build:05-brief`
