---
description: "Build Your Brand — Lesson 2: Deep research. Real competitor + customer research, sourced, before any brand decisions."
---

# /build:02-research

1. Write one paragraph: what it is, who it's for, why it's different,
   what it refuses to look like. Don't over-polish it — this is a
   starting point, the skill researches around what you give it.

2. Run:
   ```
   claude -p "Use brand-foundation to build a brand foundation from: <your paragraph>"
   ```
   This does real web search first — give it a minute. It writes seven
   files, in order, to `records/brands/<brand_id>/`:
   ```
   deepresearch.md         the dossier, sourced — lands first
   avatar-sheet.md         the customer, in their own words
   offerbrief.md           product, promise, mechanism, proof, pricing
   necessary-beliefs.md    what someone must accept before they buy
   project-knowledge.md    the synthesis, VERIFIED vs UNVERIFIED
   brand-book.md           the readable brand book
   brand_foundation.json   the structured contract, unchanged schema
   ```

3. Once it lands, open `deepresearch.md` and read it in full before
   moving on. Then open `project-knowledge.md` and check the UNVERIFIED
   section specifically — keep those claims out of everything you build
   from here. If a number or claim shows up there with no real source
   behind it, that's the split doing its job, not something to second-
   guess.

**Done when:** all seven files exist, research read, UNVERIFIED section
checked.
**Next:** `/build:03-foundation`
