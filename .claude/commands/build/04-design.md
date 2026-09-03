---
description: "Build Your Brand — Lesson 4: design.md. Choose a visual direction from real options, then lock exact tokens the whole build inherits."
---

# /build:04-design

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
LESSON 4 · DESIGN TOKENS
THE LOOK
──────────────────────────────────────────────────
```

> **Timing**     ~10 minutes
> **Goal**       A visual direction you chose from real options, locked into design.md
> **Progress**   `[███░░░░░░░] 3/9 · starting`

---

## Why most AI sites look identical

Same instruction, same model, no design system. The model reaches for
its default, and its default is everyone's default.

`design.md` is the fix. Exact hex codes, named fonts, the rule for
when the accent colour appears, the words your brand uses and the
words it never uses. It sits in the project root and everything reads
it. Colour and type get settled here — BEFORE the brand guide, so you
never build the guide and then go back.

---

## STEP 1 — See your options, pick one

```bash
claude -p "Use design-tokens to write design.md for <brand_id>"
```

The skill reads your competitor teardown (`deepresearch.md`) and your
interview answers (`intake.md`), then presents **2-3 real visual
directions** — each with its palette, its type pairing, and a reason
grounded in what your competitors already look like. One direction
might lean into the category pattern; another might break it exactly
where it's weakest.

What lands in `design.md`:
- Palette: exact hex + role for every colour (and the accent-is-not-
  decoration rule)
- Typography: named families, the full type scale, when each is used
- Voice: USE/AVOID words **plus signature sentence structures** —
  the 2-3 constructions the brand uses so often they become
  recognizable
- Components: button/card/spacing rules you can check a build
  against
- Motion: how things move (and never move)
- Mood: the gut-check paragraph

You choose. That's the point — you're the one who has to look at this
brand every day.

> **ACTION:** Look at the options. Pick the one that's yours.
> Type `1` when you've chosen.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Visual direction chosen                         │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[███░░░░░░░] 3/9 · Step 1/2`

---

## STEP 2 — Specific beats vague

Check the `design.md` that landed. If any line in it could describe
two different brands, it isn't finished — tighten it now. `#1B4B8F`
is a decision; "warm blue" is not.

> If you already have a `design.md` from a different brand at the
> repo root, the skill stops and asks before overwriting it. Answer
> it, don't route around it — it's protecting the other brand's file.

> **ACTION:** Read `design.md`. Every value specific? Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  design.md locked — every build inherits it       │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[████░░░░░░] 4/9 · Lesson 4 complete`

---

## DONE

**What you have now:**
- A `design.md` at the repo root: exact palette with hex + roles,
  named fonts, USE/AVOID voice, component rules, mood
- A direction you chose from evidence, not a default

**Next lesson:** `/build:05-guide` — turn it into a scrollable visual
brand book.
