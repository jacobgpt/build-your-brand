---
description: "Build Your Brand, Lesson 6: The face. A hero still through the gate, then motion if you choose to spend on it."
---

# /build:06-hero

```
     ██  ▓▓▓▓▓  ▓▓  ██████  ██████  ██████
     ██ ▓▓   ▓▓ ▓▓ ██      ██    ██ ██   ██
     ██ ▓▓▓▓▓▓▓ ▓▓ ██      ██    ██ ██████
██   ██ ▓▓   ▓▓ ▓▓ ██      ██    ██ ██   ██
 █████  ▓▓   ▓▓ ▓▓  ██████  ██████  ██████

          T H E   C R E A T I V E   A R C H I T E C T
```

**LESSON 6 OF 10 · THE FACE**
About twenty minutes. You leave with a hero still that went through the gate and that you inspected up close.

---

## The still decides the video

Motion adds nothing a bad frame lacks. So the order is fixed: generate
the still, approve it, inspect it, and only then animate it. This
lesson spends real credits, which is why the gate exists. Nothing is
built until you've read the brief and typed `y`.

**Needs a Higgsfield account with credits** (`higgsfield auth login`,
then `higgsfield account status`). Don't have one? Go to
`/build:07-website`. The site falls back to a CSS hero, and Lesson 8's
refusal record works with no account at all.

---

## STEP 1 · The brief

> **RUN (Claude, in this session):** Use `aphrodite-direction` to write
> the hero-still brief for `<brand_id>`, `brief_id` ending in
> `-hero-still`, `asset_type: hero-still`.

Be exact about what's forbidden. Image models will print fabricated
text or a logo onto any surface with texture, however clearly you said
not to. If the still has several surfaces (a mat, a switch, a tray, a
housing), forbid text on each one by name rather than once in general.

> **CHECK.** Brief open at `records/briefs/<brief_id>.json`; the
> forbidden list names each surface. Say `next`.

---

## STEP 2 · Through the gate

> **RUN (Claude, in this session):** Use `hephaestus-production` on
> `records/briefs/<brief_id>.json`.

The gate is two keystrokes and neither is Claude's. Claude shows you
the brief and asks `Approve build? [y/N]`; you answer here. Then Claude
Code's own permission dialog shows the exact gate command with your
answer inside it, and you allow it. Claude can't click that dialog.
This step spends credits: check `higgsfield account status` before you
answer and again after. The result lands at
`records/assets/hero-still.png` and `hero-poster.jpg`, with a dated
record in `records/runs/`.

Judge it like an art director. "Fine" is bad. Are the colours your
hex? Is the mood the one in `design.md`, or the model's default mood?
Is there text anywhere?

If it's mediocre, rebuild with a sharper brief. It's cheaper than
animating a weak frame.

> **CHECK.** Brief read, balance checked, `y` given only if you want
> this build, dialog allowed. Say `next`.

---

## STEP 3 · Look at it up close

A clean exit isn't a clean image. Zoom into every textured surface and
look for readable fabricated text. If it's there, the fix is upstream:
a new brief named `-hero-still-v2` (the build recognises version
suffixes), not a patched video prompt.

> **CHECK.** Still inspected at full size, textured surfaces
> especially. Clean, or a new brief written. Say `next`.

---

## OPTIONAL · Logo and section images

While the pipeline is warm, round out the set the same way: a mark and
wordmark if the brand has none, product shots or textures the site
will need. Same rules. Aphrodite writes the brief, Hephaestus gates
it, `design.md` hex goes in the brief, no baked-in text where the site
will lay copy. Each one is a dated record, approved or refused, like
the hero.

---

## OPTIONAL · Motion

Quiet only. A slow move toward the subject, a little air in the scene,
colours locked to the still, nothing new entering frame. It's a
background for text and has to stay readable underneath. Five to eight
seconds, looping.

> **RUN (Claude, in this session):** Use `aphrodite-direction` for the
> `<brand_id>` hero video, `brief_id` ending in `-hero-video`, then
> `hephaestus-production` on the resulting brief.

Same gate. Video costs more than a still, so check your balance first.
Lands at `records/assets/hero.mp4`.

Stopping at the still is fine. Lesson 7 works either way.

---

## On record

- A hero still in `records/assets/`, approved by you at the gate,
  inspected by you up close
- The decision, dated, in `records/runs/`
- The video, only if you chose to spend on it

Next: `/build:07-website`. The site: words first, `design.md` second.
