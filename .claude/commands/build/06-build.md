---
description: "Build Your Brand — Lesson 6: Production. Approval gate, real Higgsfield build, dated record — then reject one on purpose."
---

# /build:06-build

> **Repo-reality note:** `hephaestus-production` in this repo builds a
> single static image via the Higgsfield CLI (`gpt_image_2`, mapped aspect
> ratios). There is no hero-video / animation skill here — if a hero video
> lesson is wanted later, it needs a new skill built and wired in before
> this command promises one.

1. Confirm Higgsfield is authenticated (re-check if it's been a while):
   ```
   higgsfield account status
   ```

2. Build the brief from `/build:05-brief`:
   ```
   claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
   ```
   This runs, in order:
   - `scripts/validate_brief.py` (stops if `INVALID`)
   - `scripts/approval_gate.py` — prints the brief, asks
     `Approve build? [y/N]` **live in the terminal**. Read it properly, then
     type `y` yourself. Do not pre-pipe an answer — that's the actual gate,
     shown live.
   - on approve: `scripts/hephaestus_build.py` calls the real Higgsfield CLI,
     downloads the asset to `records/assets/`, and a dated record writes to
     `records/runs/`.

3. Open the asset in `records/assets/`.

4. **Reject one on purpose.** Run step 2 again with the same or a new brief,
   and this time type anything other than `y`. Open the resulting record in
   `records/runs/` — the rejection is on file too, dated, with no asset
   produced. A record that only contains what worked isn't a record, it's a
   highlight reel.

## If it fails on camera

`hephaestus_build.py` already turns these into clean one-line fixes instead
of stack traces:
- **Auth error** → `higgsfield auth login`, then re-run this command
- **Rate limit** → wait ~60s, re-run
- **Out of credits** → top up at higgsfield.ai, re-run
- **Content filter** (false-positive on brand names) → re-run
  `aphrodite-direction` dropping the specific brand/trademark name, then
  build the new brief

A raw Python traceback instead of one of these is a bug in
`hephaestus_build.py`, not a normal failure — flag it, don't paper over it.

**Done when:** one asset built and reviewed, one rejection on record.
**Next:** `/build:07-done`
