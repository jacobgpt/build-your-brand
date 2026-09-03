---
description: "Build Your Brand — Lesson 3: Brand foundation. Validate the six-document + JSON contract, review, edit if wrong."
---

# /build:03-foundation

The same `brand-foundation` run from `/build:02-research` already wrote
all seven files to `records/brands/<brand_id>/`. This lesson is about
verifying and owning the contract, not building anything new.

1. Validate the JSON:
   ```
   python3 scripts/validate_brief.py records/brands/<brand_id>/brand_foundation.json --schema brand_foundation
   ```
   Must print `VALID`. If it doesn't, fix the JSON or re-run
   `brand-foundation` until it does — never hand off an unvalidated
   foundation.

2. Open `brand-book.md` and read it. Check:
   - the positioning is actually theirs, not something a competitor could
     paste onto their own business unchanged
   - the `avoid` list has teeth — "we never show a person smiling at a
     laptop" beats "we avoid clichés"

3. It's their file — edit it by hand if anything's wrong. The agent
   proposes, they decide — that's the pattern for the whole course. If they
   hand-edit `brand-book.md`, remind them `brand_foundation.json` is what
   every later skill actually reads, so mirror any real change there too:
   the JSON stays authoritative, the six `.md` files are the human layer
   and must not contradict it.

**Done when:** `VALID`, brand book read, edited if needed.
**Next:** `/build:04-guide`
