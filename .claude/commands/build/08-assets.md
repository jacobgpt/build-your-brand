---
description: "Build Your Brand — Lesson 8: Direction and production. Typed brief, gate, real asset — reject one on purpose."
---

# /build:08-assets

```ansi
     ██  [38;5;208m█████[0m  [38;5;208m██[0m  ██████  ██████  ██████
     ██ [38;5;208m██   ██[0m [38;5;208m██[0m ██      ██    ██ ██   ██
     ██ [38;5;208m███████[0m [38;5;208m██[0m ██      ██    ██ ██████
██   ██ [38;5;208m██   ██[0m [38;5;208m██[0m ██      ██    ██ ██   ██
 █████  [38;5;208m██   ██[0m [38;5;208m██[0m  ██████  ██████  ██████

          T H E   C R E A T I V E   A R C H I T E C T
```

```
──────────────────────────────────────────────────
LESSON 8 · DIRECTION + PRODUCTION
THE ASSET
──────────────────────────────────────────────────
```

> **Timing**     ~15 minutes
> **Goal**       One real asset built, one rejection on record
> **Progress**   `[███████░░░] 7/9 · starting`

---

## Two decisions, split apart

What should exist (Aphrodite) and how to build it (Hephaestus) are
two different jobs, held by two different agents with a typed
handoff between them. Aphrodite never picks a tool or model — if she
does, something's wrong with the brief. Stop and check it before
continuing.

---

## STEP 1 — One line, one brief

Think of one line: a product, scene, or concept for the asset. Then:

```bash
claude -p "Use aphrodite-direction to write a creative brief for: <your one-liner>"
```

This reads your foundation and folds positioning, audience, tone,
`visual_pillars`, and `avoid` into the brief automatically.

Open the resulting `records/briefs/<brief_id>.json`. It's typed JSON,
not prose — every field is a slot the next skill reads directly, so a
vague `placement` or missing `must_preserve` entry becomes a real
production bug the moment it reaches the build.

**The brief quality bar:** read it as the image model would. If any
field could produce two different images, tighten it now — "a
premium scene" is empty; "deep green #1E3A2F background, cream product,
soft morning side-light, no people" is a slot the model can fill
exactly. Fixing a vague brief costs a minute here; a vague brief
that reaches the gate costs credits.

```bash
python3 scripts/validate_brief.py records/briefs/<brief_id>.json
```

Must print `VALID`.

> **ACTION:** Brief written, read, validator prints `VALID`.
> Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Typed brief validated                           │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[███████░░░] 7/9 · Step 1/3`

---

## STEP 2 — Build it through the gate

```bash
claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
```

`scripts/approval_gate.py` prints the brief and asks
`Approve build? [y/N]` live in the terminal. Read it properly, then
type `y` yourself — the build waits on your answer, nothing else.
This
step **spends real credits**, so check the cost before approving. On
approve, the real Higgsfield CLI builds it, downloads to
`records/assets/`, and a dated record writes to `records/runs/`.

**Then actually look at the result and judge it hard.**
Does it obey every `must_preserve`? Does it break any `forbidden`?
Zoom in and check. A clean exit code isn't proof the image is right
— you are the proof step. If it breaks a rule, that's a rebuild
with a tighter brief, and both attempts stay on record.

> **ACTION:** Read the brief at the gate, check the cost, type `y`.
> Then open the asset and actually look at it. Type `1` when you've
> seen it.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  One real asset, built and reviewed               │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[███████░░░] 7/9 · Step 2/3`

---

## STEP 3 — Reject one on purpose

Run STEP 2 again with any brief — and this time type anything other
than `y`. Open the resulting record in `records/runs/`: the rejection
is on file too, dated, with no asset produced and no credits spent.

A record holding only the wins is a highlight reel. The rejections
are what make it a real record.

> **ACTION:** One rejection on file in `records/runs/`. Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  The gate tested both ways                        │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[████████░░] 8/9 · Lesson 8 complete`

---

## If something goes wrong

`hephaestus_build.py` turns these into clean one-line fixes instead
of stack traces:
- **Auth error** → `higgsfield auth login`, then re-run
- **Rate limit** → wait ~60s, re-run
- **Out of credits** → top up at higgsfield.ai, re-run
- **Content filter** (false-positive on brand names) → re-run
  `aphrodite-direction` dropping the specific brand/trademark name

A raw Python traceback instead of one of these is a real bug. Normal failures look like the list above; — worth digging into rather than just retrying.

---

## DONE

**What you have now:**
- One real asset in `records/assets/`, traceable brief → gate → build
- One rejection on record — proof the gate works both ways
- The full pattern: decision split from execution, typed handoff,
  human at the consequential step

**Next lesson:** `/build:09-done` — look at everything you built,
and the pattern behind it.
