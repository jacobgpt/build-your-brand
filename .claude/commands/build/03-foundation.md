---
description: "Build Your Brand — Lesson 3: Brand foundation. Validate and review the structured brand contract."
---

# /build:03-foundation

The same `brand-foundation` run from `/build:02-research` already wrote:

```
records/brands/<brand_id>-research.md   the dossier, sourced
records/brands/<brand_id>.json          the structured contract (brand_foundation.json)
records/brands/<brand_id>.md            the readable brand book
```

1. Validate the contract:
   ```
   python3 scripts/validate_brief.py records/brands/<brand_id>.json --schema brand_foundation
   ```
   Must print `VALID`. If it doesn't, fix the JSON (or re-run
   `brand-foundation`) until it does — never hand off an unvalidated
   foundation.

2. Open `records/brands/<brand_id>.md` and read it. Check:
   - the positioning is actually theirs, not something a competitor could
     paste onto their own business unchanged
   - the `avoid` list has teeth — "we never show a person smiling at a
     laptop" beats "we avoid clichés"

3. It's their file — edit it by hand if anything's wrong. The agent
   proposes, they decide. If they hand-edit `<brand_id>.md`, remind them
   `<brand_id>.json` is the one every later skill actually reads, so mirror
   any real change there too.

**Done when:** `VALID`, brand book read, edited if needed.
**Next:** `/build:04-website` (this repo has no separate brand-guide/design.md
skill — see the note in Lesson 4 below).
