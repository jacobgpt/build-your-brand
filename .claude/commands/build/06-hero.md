---
description: "Build Your Brand — Lesson 6: The hero. Still through the gate, then image-to-video — flag current repo reality honestly."
---

# /build:06-hero

> **Repo-reality note:** `hephaestus-production` and `hephaestus_build.py`
> support hero-still AND hero-video generation, and the hero-still half has
> been run for real (built, film-safety-scanned via vision check, one
> version rejected for a hallucinated logo, rebuilt clean — the record is
> in `BUILD_LOG.md`). The hero-VIDEO half is code-complete and unit-tested
> (the brief-id detection, the "no still on disk yet" guard) but has never
> actually been run against the real Higgsfield API — that spend has not
> been approved yet in this repo. Treat the video step below as untested
> until someone runs it for real and updates this note.

### Still first, always

A strong still makes a strong video; a weak still makes a weak video with
motion on it. Two moves: generate the still, approve it, then animate it.

1. Write a brief:
   ```
   claude -p "Use aphrodite-direction to write a creative brief for the <brand_id> hero image, brief_id ending in -hero-still"
   ```
   Be explicit in the brief about what's forbidden — "no on-image text,
   logo, or wordmark of any kind" is not automatic; a real run of this
   exact skill once had the image model hallucinate a fabricated brand
   name onto the plate despite a similar instruction. State it per-surface
   if the brief has multiple surfaces (mat, switch, tray, meter housing).

2. Run it through the gate:
   ```
   claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
   ```
   Read the brief on screen, then approve. Lands at
   `records/assets/hero-still.png` + `hero-poster.jpg`, with a dated run
   record in `records/runs/`.

3. **Actually look at the image** — don't assume a clean exit means a
   clean image. Zoom into any patterned/textured surface and check for
   readable fabricated text. If it comes back bad, the fix is upstream: a
   new `-hero-still` brief (or `-hero-still-v2`, etc. — the build script
   recognizes revision suffixes), not a patched video prompt.

### The motion (untested in this repo — see note above)

Subtle only: slow push-in, ambient drift, colours locked to the source, no
new objects. It's a background for text and must stay readable underneath.
5-8 seconds, looping.

```
claude -p "Use aphrodite-direction to write a creative brief for the <brand_id> hero video, brief_id ending in -hero-video"
claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
```
Same gate — read the real credit cost it reports before approving, this is
real spend. Lands at `records/assets/hero.mp4`.

**Done when:** hero still built, reviewed pixel-by-pixel, clean. Video
built and reviewed IF the spend was approved — otherwise stop here and say
so honestly on camera; this lesson is allowed to end at the still.
**Next:** `/build:07-website`
