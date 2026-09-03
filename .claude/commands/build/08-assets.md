---
description: "Build Your Brand — Lesson 8: Direction and production. Typed brief, gate, real asset — reject one on purpose."
---

# /build:08-assets

Two decisions, split apart: what should exist (Aphrodite), and how to
build it (Hephaestus). Aphrodite never picks a tool or model — if she
does, something's wrong with the brief, stop and check it before
continuing.

1. Think of one line: a product, scene, or concept for the asset.

2. Write the brief:
   ```
   claude -p "Use aphrodite-direction to write a creative brief for: <your one-liner>"
   ```
   This reads your foundation and folds positioning, audience, tone,
   `visual_pillars`, and `avoid` into the brief automatically.

3. Open the resulting `records/briefs/<brief_id>.json`. It's typed JSON,
   not prose — every field is a slot the next skill reads directly, so a
   vague `placement` or missing `must_preserve` entry becomes a real
   production bug, not just a stylistic nitpick.

4. Confirm the validator ran clean:
   ```
   python3 scripts/validate_brief.py records/briefs/<brief_id>.json
   ```
   Must print `VALID`.

5. Build it through the gate:
   ```
   claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
   ```
   `scripts/approval_gate.py` prints the brief and asks
   `Approve build? [y/N]` live in the terminal. Read it properly, then
   type `y` yourself — that's the actual gate, not decoration. This step
   spends real credits, so check the cost before approving. On approve,
   the real Higgsfield CLI builds it, downloads to `records/assets/`, and
   a dated record writes to `records/runs/`.

6. **Reject one on purpose.** Run step 5 again and this time type
   anything other than `y`. Open the resulting record in `records/runs/`
   — the rejection is on file too, dated, with no asset produced and no
   credits spent. A record that only contains what worked isn't a record,
   it's a highlight reel.

## If something goes wrong

`hephaestus_build.py` turns these into clean one-line fixes instead of
stack traces:
- **Auth error** → `higgsfield auth login`, then re-run
- **Rate limit** → wait ~60s, re-run
- **Out of credits** → top up at higgsfield.ai, re-run
- **Content filter** (false-positive on brand names) → re-run
  `aphrodite-direction` dropping the specific brand/trademark name

A raw Python traceback instead of one of these is a real bug, not a
normal failure — worth digging into rather than just retrying.

**Done when:** one asset built and reviewed, one rejection on record.
**Next:** `/build:09-done`
