---
description: "Build Your Brand — Lesson 2: Deep research. Real competitor + customer research, sourced, before any brand decisions."
---

# /build:02-research

1. Ask the user for one paragraph: what it is, who it's for, why it's
   different, what it refuses to look like. Don't let them over-polish it —
   this is a starting point, the skill researches around it.

2. Run:
   ```
   claude -p "Use brand-foundation to build a brand foundation from: <their paragraph>"
   ```
   Real web search first — give it a minute. This writes seven files, in
   order, to `records/brands/<brand_id>/`:
   ```
   deepresearch.md         the dossier, sourced — lands first
   avatar-sheet.md         the customer, in their own words
   offerbrief.md           product, promise, mechanism, proof, pricing
   necessary-beliefs.md    what someone must accept before they buy
   project-knowledge.md    the synthesis, VERIFIED vs UNVERIFIED
   brand-book.md           the readable brand book
   brand_foundation.json   the structured contract, unchanged schema
   ```
   No Firecrawl key required — Claude Code's own web search is enough. This
   has been verified from a plain terminal, not just through Hermes.

3. Once it lands, open `deepresearch.md` and read it in full before moving
   on. Then open `project-knowledge.md` and check the UNVERIFIED section
   specifically — those claims stay out of everything built downstream.
   This split has caught real fabricated numbers before (an uncredited
   competitor decibel figure, once) — that's the mechanism working, not
   paranoia.

**Done when:** all seven files exist, research read, UNVERIFIED section
checked.
**Next:** `/build:03-foundation`
