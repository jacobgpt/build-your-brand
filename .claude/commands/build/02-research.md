---
description: "Build Your Brand — Lesson 2: Deep research. Real competitor + customer research before any brand decisions."
---

# /build:02-research

1. Ask the user for one paragraph: what it is, who it's for, why it's
   different, what it refuses to look like. Don't let them over-polish it —
   this is a starting point, not a brief.

2. Run:
   ```
   claude -p "Use brand-foundation to build a brand foundation from: <their paragraph>"
   ```
   This does real web research first and writes
   `records/brands/<brand_id>-research.md` before anything else.

   > **Note:** the `brand-foundation` skill in this repo writes THREE files
   > in one pass — `<brand_id>-research.md`, `brand_foundation.json`, and
   > `<brand_id>.md` (the brand book) — not six separate documents. If your
   > script/notes reference `avatar-sheet.md`, `offerbrief.md`,
   > `necessary-beliefs.md`, or `project-knowledge.md` as distinct files,
   > those aren't produced by this skill — don't promise them on camera.

3. Once it lands, open `records/brands/<brand_id>-research.md` and read it
   in full before moving on. Check it for:
   - real competitor notes, not guesses
   - quoted customer language, not paraphrase
   - cited sources (URLs)

**Done when:** the research file exists and has been read end to end.
**Next:** `/build:03-foundation`
