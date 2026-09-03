---
description: "Build Your Brand — Lesson 4: The brand guide. Build brand-guide.html + PDF, screenshot-verify the export."
---

# /build:04-guide

> **Repo-reality note:** the `brand-guide` skill exists and has been
> reviewed, but has NOT yet been run end to end against a real brand in
> this repo. Run it for real here — this lesson doubles as that
> verification. If it breaks, that's real signal, fix the skill before
> filming, don't paper over it.

1. Confirm a validated foundation exists (`/build:03-foundation`).

2. Build the guide:
   ```
   claude -p "Use brand-guide to build the guide for <brand_id>"
   ```
   Reads the foundation documents and writes one self-contained
   `brand-guide.html` — Part I the story (what this brand believes, who
   it's for, what it's against), Part II the book (positioning, audience,
   voice of the customer with real quotes from `deepresearch.md`, colour
   with hex codes, type, components, messaging library, and a "what we
   never claim" panel for anything UNVERIFIED). Then exports
   `brand-guide.pdf` via headless Chrome.

3. **Don't assume the export worked because the command exited zero.**
   Check the file size:
   ```
   ls -la brand-guide.pdf
   ```
   Should be well over 20KB. Then actually look at it:
   ```
   pdftoppm -r 100 -png brand-guide.pdf /tmp/brand-guide-check
   ```
   and view the resulting PNG(s) — via `vision_analyze` if working through
   an agent, or just open the PNG yourself. Confirm text isn't cut off,
   colours rendered, no blank pages.

4. Read the HTML and the PDF both. Are the customer quotes real ones from
   `deepresearch.md`, or invented? Does the "what we never claim" panel
   actually name real gaps (no pricing set, no measured results yet), not
   generic hedging?

**Done when:** guide built, PDF file-size and visually confirmed, both
files read end to end.
**Next:** `/build:05-design`
