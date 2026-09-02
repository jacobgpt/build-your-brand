---
description: "Build Your Brand — Lesson 5: Creative direction. Write a typed, on-brand creative brief with Aphrodite."
---

# /build:05-brief

Two decisions, split apart: what should exist (this lesson), and how to
build it (`/build:06-build`). Aphrodite never picks a tool or model — if she
does, that's a bug, flag it.

1. Ask the user for one line: a product, scene, or concept for the asset
   (e.g. "a poster for a coffee shop that opens at 5am").

2. Run:
   ```
   claude -p "Use aphrodite-direction to write a creative brief for: <their one-liner>"
   ```
   Since a brand foundation exists (`records/brands/<brand_id>.json`),
   Aphrodite folds its positioning, audience, tone, visual pillars, and
   avoid-list into the brief automatically.

3. Open the resulting `records/briefs/<brief_id>.json`. It's typed JSON, not
   prose — every field is a slot the next skill reads directly, so a vague
   `placement` or missing `must_preserve` entry becomes a real production
   bug, not just a stylistic nitpick.

4. Confirm the validator already ran clean:
   ```
   python3 scripts/validate_brief.py records/briefs/<brief_id>.json
   ```
   Must print `VALID`.

**Done when:** brief exists, `VALID`, and reads like a real creative
decision, not a form-fill.
**Next:** `/build:06-build`
