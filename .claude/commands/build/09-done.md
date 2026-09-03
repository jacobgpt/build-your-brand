---
description: "Build Your Brand — Lesson 9: What you built. Review every file, the pattern behind it, run it on your own brand."
---

# /build:09-done

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
LESSON 9 · WHAT YOU BUILT
THE PATTERN
──────────────────────────────────────────────────
```

> **Timing**     ~10 minutes
> **Goal**       The full picture confirmed against real files, and a next step for your own brand
> **Progress**   `[████████░░] 8/9 · starting`

---

## STEP 1 — Look at it

```
records/brands/<brand_id>/    nine files: intake answers, copywriter prompt,
                              six documents, brand_foundation.json
brand-guide.html/.pdf         the visual brand book
design.md                     the design system
records/assets/               hero still (+ video, if you built it), finished assets
records/briefs/               every brief written
records/runs/                 every decision, approved and rejected, dated
records/website/<brand_id>/   the site
```

Files on your machine, in a structure you can inspect, that someone
else could audit. Not a chat log you'll never reopen.

Run the status check and reload the dashboard:

```bash
python3 scripts/dashboard_status.py
```

`http://localhost:8787/dashboard.html` now shows it confirmed against
your real files, not self-reported status.

> **ACTION:** Run the status check. Dashboard matches what's on
> disk? Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Full build confirmed against real files          │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[████████░░] 8/9 · Step 1/3`

---

## STEP 2 — Ship it (optional but do it)

A brand that isn't public is a document, not a brand. If you want the
site on a real URL now, Claude can deploy it — static one-page site,
so any static host takes it as-is.

**Nothing deploys until you say the words.** When you reach this
step, Claude shows you exactly what it's about to run (git init,
commit, repo create, deploy) and asks `Ship it? [y/N]`. Read it, then
answer. The deploy itself costs nothing — only the hosting
platform's normal free/paid tiers apply. Skipping is a real choice:
the site stays local and you ship later.

```bash
gh auth status      # GitHub authenticated?
vercel whoami       # or: npx vercel login
```

Then ask Claude to deploy: it inits git (sensible `.gitignore`
included), commits, creates a private GitHub repo named after your
brand, and ships to production, handing you back the live URL. Point
your domain at it from the host's dashboard; from then on, any edit
in Claude Code + `git push` redeploys in seconds. Files you own, no
lock-in.

**No credits required for the deploy itself** — only the hosting
platform's normal free/paid tiers apply.

> **ACTION:** Site live on a real URL — or consciously deferred.
> Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Shipped                                         │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[█████████░] 8/9 · Step 2/3`

---

## STEP 3 — The pattern, not the parts

The reusable thing here isn't Aphrodite and Hephaestus specifically.
It's the shape: split the decision from the execution, type the
handoff between them, put a human at the consequential step, write
down what happened either way.

That shape works past creative assets — outreach, support, research,
ops — anywhere you'd otherwise prompt a general assistant forty
times and hope.

And the record matters because a clean exit code isn't proof a build
is right — an image model can render a shape that looks fine at a
glance but breaks a rule you set. The gate catches that: you look at
the actual result before it ships, reject the wrong ones, rebuild.
Keeping the rejected attempt on record is what makes it a real
record instead of a highlight reel.

> **ACTION:** You built all of this on a practice brand. The real
> move is doing it again on yours — faster, because you know the
> pattern now. Type `1` when you're ready to close out.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  COURSE COMPLETE                                 │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[██████████] 9/9 · Course complete`

---

## DONE — what now

**What you have:**
- A brand built on research instead of vibes, unprovable claims
  separated out and labelled
- A visual brand book you can hand to anyone
- A design system every future build obeys (`design.md`)
- A hero and a site, both traceable to the same source of truth
- A gate that means nothing gets made without you
- A record of every decision, including the ones you said no to

**Three concrete next steps, in order:**

1. **Run the course on your real brand.** Start at
   `/build:02-research` with your own business. Everything you just
   learned applies unchanged — the interview, the research, the
   options.
2. **Ship the site.** Put the website on a real domain and point one
   traffic source at it. A brand that isn't public is a document,
   not a brand.
3. **Reuse the pattern.** Split decisions from execution, type the
   handoff, gate the spend, record everything. Take that shape to
   the next thing you build with agents.

The brand you built here was the exercise. Yours is the point.
