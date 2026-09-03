---
description: "Build Your Brand — Lesson 9: What you built. Review every file, the pattern behind it, run it on your own brand."
---

# /build:09-done

## Look at it

```
records/brands/<brand_id>/    six documents + the foundation contract
brand-guide.html/.pdf         the guide
design.md                     the design system
records/assets/               hero still (+ video, if built), finished assets
records/briefs/                every brief written
records/runs/                  every decision, approved and rejected, dated
records/website/<brand_id>/    the site
```

Files on disk, in a structure a stranger could audit. Not a chat log
you'll never reopen.

Run `python3 scripts/dashboard_status.py` and reload
`http://localhost:8787/dashboard.html` to see it confirmed against real
files, not self-reported status.

## What you've got

- A brand built on research instead of vibes, with unprovable claims
  separated out and labelled (`project-knowledge.md`'s UNVERIFIED section)
- A guide you can hand to anyone
- A design system every future build obeys (`design.md`)
- A hero and a site, both traceable to the same source of truth
- A gate that means nothing gets made without a human saying yes
- A record of every decision, including the ones rejected — see
  `BUILD_LOG.md` for a real example of the gate catching a bad output
  (a hallucinated logo on a hero-still v1, rejected, rebuilt clean)

## The pattern, not the parts

The reusable thing isn't Aphrodite and Hephaestus specifically. It's the
shape: split the decision from the execution, type the handoff between
them, put a human at the consequential step, write down what happened
either way.

That shape works past creative assets — outreach, support, research, ops —
anywhere you'd otherwise prompt a general assistant forty times and hope.

**Run `/build:02-research` again on your own brand next.**
