---
description: "Build Your Brand — Lesson 7: What you built. Review every file, the pattern behind it, run it on your own brand."
---

# /build:07-done

## Look at it

```
records/brands/<brand_id>-research.md   the research dossier
records/brands/<brand_id>.json          the brand contract
records/brands/<brand_id>.md            the readable brand book
records/website/<brand_id>/index.html   the site
records/briefs/                         every brief written
records/runs/                           every decision, approved and rejected, dated
records/assets/                         the finished files
```

Files on disk, in a structure a stranger could audit. Not a chat log you'll
never reopen.

Run `python3 scripts/dashboard_status.py` and reload
`http://localhost:8787/dashboard.html` to see it confirmed against real
files, not self-reported status.

## What you've got

- A brand built on research instead of vibes
- A design system every brief inherits automatically (`visual_pillars` +
  `avoid`, read straight from `brand_foundation.json`)
- A site and a finished asset, both traceable to the same source of truth
- A gate that means nothing gets made without a human saying yes
- A record of every decision, including the ones rejected

## The pattern, not the parts

The reusable thing isn't Aphrodite and Hephaestus specifically. It's the
shape: split the decision from the execution, type the handoff between
them, put a human at the consequential step, write down what happened
either way.

That shape works past creative assets — outreach, support, research, ops —
anywhere you'd otherwise prompt a general assistant forty times and hope.

**Run `/build:02-research` again on your own brand next.**

---

## Honest gap list for whoever teaches this next

- No separate brand-guide (HTML+PDF) skill exists — `brand-foundation`
  already writes the readable brand book (`<brand_id>.md`); there's no PDF
  export step.
- No `design-tokens` / standalone `design.md` skill exists —
  `brand-website` derives palette/type directly from `visual_pillars` at
  build time instead.
- No hero-video / animation skill exists — `hephaestus-production` builds
  one static image per brief via the real Higgsfield CLI.
- This course is 7 real lessons (`01`–`07`), not 9 — the two missing
  lessons from the original draft script don't have skills behind them yet.
  Build them for real before promising them on camera, or cut the promise.
