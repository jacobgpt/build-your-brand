---
description: "Build Your Brand — Lesson 5: design.md. Extract exact tokens the whole build inherits."
---

# /build:05-design

1. Confirm the brand guide exists (`/build:04-guide`) — design-tokens
   distills from decisions you already made there.

2. Build it:
   ```
   claude -p "Use design-tokens to write design.md for <brand_id>"
   ```
   This reads `brand_foundation.json` and `brand-book.md`, and writes
   `design.md` at the repo root: palette (exact hex + role, not "warm
   blue"), typography (named fonts), voice USE/AVOID word lists,
   component rules, mood.

3. Check it. If any line in `design.md` could describe two different
   brands, it isn't finished — tighten it now. `#1B4B8F` is a decision;
   "warm blue" is not.

   > If you already have a `design.md` from a different brand at the
   > repo root, the skill will stop and ask before overwriting it rather
   > than doing it silently. Answer it, don't route around it — it's
   > protecting the other brand's file.

**Done when:** `design.md` exists at the repo root, every value specific.
**Next:** `/build:06-hero`
