---
description: "Build Your Brand — Lesson 6: The hero. Still through the gate, then image-to-video."
---

# /build:06-hero

### Still first, always

A strong still makes a strong video; a weak still makes a weak video with
motion on it. Two moves: generate the still, approve it, then animate it.

1. Write a brief:
   ```
   claude -p "Use aphrodite-direction to write a creative brief for the <brand_id> hero image, brief_id ending in -hero-still"
   ```
   Be explicit in the brief about what's forbidden. Image models can
   sometimes render fabricated text or a logo onto a textured surface
   even when told not to — if the still has multiple surfaces (a mat, a
   switch, a tray, a meter housing), say "no text or logo" for each one
   specifically rather than once in general.

2. Run it through the gate:
   ```
   claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
   ```
   This step spends real credits — check the cost it reports before
   typing `y`. Read the brief on screen, then approve. Lands at
   `records/assets/hero-still.png` + `hero-poster.jpg`, with a dated run
   record in `records/runs/`.

3. **Actually look at the image** — don't assume a clean exit means a
   clean image. Zoom into any patterned or textured surface and check for
   readable fabricated text. If it comes back bad, the fix is upstream: a
   new `-hero-still` brief (or `-hero-still-v2`, and so on — the build
   recognizes version suffixes), not a patched video prompt.

### The motion

Subtle only: slow push-in, ambient drift, colours locked to the source, no
new objects. It's a background for text and must stay readable
underneath. Five to eight seconds, looping.

```
claude -p "Use aphrodite-direction to write a creative brief for the <brand_id> hero video, brief_id ending in -hero-video"
claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
```
Same gate — this step spends more credits than the still, so check the
real cost it reports before approving. Lands at `records/assets/hero.mp4`.

**Done when:** hero still built and reviewed pixel-by-pixel, clean. It's
fine to stop here if you don't want to spend on the video yet — the
website in the next lesson works either way.
**Next:** `/build:07-website`
