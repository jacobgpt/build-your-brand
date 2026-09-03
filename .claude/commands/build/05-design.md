---
description: "Build Your Brand — Lesson 5: design.md. Extract exact tokens the whole build inherits."
---

# /build:05-design

1. Confirm the brand guide exists (`/build:04-guide`) — design-tokens
   distills from decisions already made there.

2. Build it:
   ```
   claude -p "Use design-tokens to write design.md for <brand_id>"
   ```
   Reads `brand_foundation.json` and `brand-book.md`, writes `design.md`
   at the repo root: palette (exact hex + role, not "warm blue"),
   typography (named fonts), voice USE/AVOID word lists, component rules,
   mood. This has been verified end to end, real brand, plain terminal.

3. Check it. If any line in `design.md` could describe two different
   brands, it isn't finished — tighten it now. `#1B4B8F` is a decision;
   "warm blue" is not.

   > **Note:** `design-tokens` will refuse to silently overwrite a
   > `design.md` belonging to a DIFFERENT brand — it stops and asks first.
   > This is intentional, confirmed in testing. Answer it, don't route
   > around it.

**Done when:** `design.md` exists at the repo root, every value specific.
**Next:** `/build:06-hero`
