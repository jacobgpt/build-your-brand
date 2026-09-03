---
description: "Build Your Brand — Lesson 9: What you built. Review every file, the pattern behind it, run it on your own brand."
---

# /build:09-done

## Look at it

```
records/brands/<brand_id>/    seven files: six documents + brand_foundation.json
brand-guide.html/.pdf         the guide
design.md                     the design system
records/assets/               hero still (+ video, if you built it), finished assets
records/briefs/                every brief written
records/runs/                  every decision, approved and rejected, dated
records/website/<brand_id>/    the site
```

Files on your machine, in a structure you can inspect, that someone else
could audit. Not a chat log you'll never reopen.

Run `python3 scripts/dashboard_status.py` and reload
`http://localhost:8787/dashboard.html` to see it confirmed against your
real files, not self-reported status.

## What you've got

- A brand built on research instead of vibes, with the unprovable claims
  separated out and labelled (`project-knowledge.md`'s UNVERIFIED section)
- A guide you can hand to anyone
- A design system every future build obeys (`design.md`)
- A hero and a site, both traceable to the same source of truth
- A gate that means nothing gets made without you saying yes
- A record of every decision, including the ones you rejected. That
  matters because a clean exit code isn't proof a build is right — an
  image model can render onto a surface, or generate a shape, that looks
  fine at a glance but breaks a rule you set (a stray logo where you said
  none, a color that drifted, a claim with nothing behind it). The gate
  is what catches that: you look at the actual result before it ships,
  reject the ones that are wrong, and rebuild. Keeping the rejected
  attempt on record, not just the one that worked, is what makes it a
  real record instead of a highlight reel.

## The pattern, not the parts

The reusable thing here isn't Aphrodite and Hephaestus specifically. It's
the shape: split the decision from the execution, type the handoff
between them, put a human at the consequential step, write down what
happened either way.

That shape works past creative assets — outreach, support, research, ops
— anywhere you'd otherwise prompt a general assistant forty times and
hope.

**Run `/build:02-research` again on your own brand next.**
