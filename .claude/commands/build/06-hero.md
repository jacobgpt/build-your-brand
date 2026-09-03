---
description: "Build Your Brand — Lesson 6: The hero. Still through the gate, then image-to-video."
---

# /build:06-hero

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
LESSON 6 · THE HERO
THE FACE
──────────────────────────────────────────────────
```

> **Timing**     ~20 minutes
> **Goal**       A hero still built through the gate and reviewed pixel-by-pixel
> **Progress**   `[█████░░░░░] 5/9 · starting`

---

## Still first, always

A strong still makes a strong video. A weak still makes a weak video
with motion on it. Two moves: generate the still, approve it, then
animate it. And this lesson spends real credits — that's why the gate
is here: nothing gets built until you read the brief and type `y`.

---

## STEP 1 — Write the brief

```bash
claude -p "Use aphrodite-direction to write a creative brief for the <brand_id> hero image, brief_id ending in -hero-still"
```

Be explicit in the brief about what's forbidden. Image models can
sometimes render fabricated text or a logo onto a textured surface
even when told not to — if the still has multiple surfaces (a mat, a
switch, a tray, a meter housing), say "no text or logo" for each one
specifically rather than once in general.

> **ACTION:** Open the brief at `records/briefs/<brief_id>.json` and
> read it. Forbidden list specific enough? Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Hero brief written                              │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[█████░░░░░] 5/9 · Step 1/3`

---

## STEP 2 — Run it through the gate

```bash
claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
```

This step **spends real credits** — check the cost it reports before
typing `y`. Read the brief on screen, then approve. Lands at
`records/assets/hero-still.png` + `hero-poster.jpg`, with a dated run
record in `records/runs/`.

If the first still comes back mediocre, it's cheaper to rebuild with
a sharper brief than to animate a weak image — a great still makes a
great video, every time.

> **ACTION:** Read the brief at the gate. Check the cost. Type `y`
> only if you actually want this build.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Hero still built — through the gate              │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[█████░░░░░] 5/9 · Step 2/3`

---

## STEP 3 — Actually look at the image

Don't assume a clean exit means a clean image. **Zoom into any
patterned or textured surface** and check for readable fabricated
text. If it comes back bad, the fix is upstream: a new `-hero-still`
brief (or `-hero-still-v2` — the build recognizes version suffixes),
not a patched video prompt.

> **ACTION:** Open the still and look at it closely, especially
 textured surfaces. Clean? Type `1`. If not — new brief, rebuild.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Hero reviewed pixel-by-pixel                    │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[██████░░░░] 6/9 · Lesson 6 complete`

---

## OPTIONAL — Logo + section images

While the asset pipeline is warm, round out the visual set the same
way: a logo (mark + wordmark) if the brand doesn't have one, and any
product shots or abstract textures the site will need. Same rules —
brief through Aphrodite, gate through Hephaestus, exact `design.md`
colours in the brief, no text baked into images the site will overlay
copy onto. Each one is a dated, rejected-or-approved record like the
hero.

---

## OPTIONAL — The motion

Subtle only: slow push-in, ambient drift, colours locked to the
source, no new objects. It's a background for text and must stay
readable underneath. Five to eight seconds, looping.

```bash
claude -p "Use aphrodite-direction to write a creative brief for the <brand_id> hero video, brief_id ending in -hero-video"
claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
```

Same gate — and this step spends more credits than the still, so
check the real cost before approving. Lands at
`records/assets/hero.mp4`.

Fine to stop at the still — the website in the next lesson works
either way.

---

## DONE

**What you have now:**
- A hero still in `records/assets/`, approved by you at the gate,
  reviewed by you pixel-by-pixel
- A dated run record of the decision in `records/runs/`
- The video, only if you chose to spend on it

**Next lesson:** `/build:07-website` — the site, copy-first and
driven by your design.md.
