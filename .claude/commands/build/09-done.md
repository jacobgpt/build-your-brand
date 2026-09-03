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
your real files on disk.

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

An unshipped brand stays a private document. If you want the
site on a live URL, Claude can deploy it — the site is a single
static `index.html` (+ assets), so any static host takes it as-is.
Claude picks the path based on what's on your machine:

| What you have | How it ships |
|---|---|
| `vercel` CLI + login | `vercel --prod --yes` → live `*.vercel.app` URL |
| `netlify` CLI + login | `netlify deploy --prod` → live URL |
| `gh` CLI + login | GitHub repo → GitHub Pages → live `*.github.io` URL |
| Nothing installed yet | Claude offers to set one up — takes ~2 min; `gh` + Pages is the zero-cost default |

**Nothing deploys until you say the words.** Claude checks what's
installed, tells you which path applies, shows you exactly what it's
about to run, and asks `Ship it? [y/N]`. Read it, then answer. The
deploy itself costs nothing — only the host's normal free tiers
apply. Skipping is a real choice: the site stays local and you ship
later.

**Pre-flight before you ship:**
- [ ] Every link on the page works (click them)
- [ ] Mobile pass done — the page reads well at phone width
- [ ] No claim, stat, or testimonial you can't back
- [ ] The hero loads (video or fallback) and the CTA does something
- [ ] You've read the whole page top to bottom as a stranger

If any box is unticked, that's a "N" — fix it, then come back.

**After it's live:** the deploy hands you a URL. Point your domain
at it from the host's dashboard (or hand the URL to your client).
From then on, edit anything in Claude Code, `git push`, and the
site updates in seconds. Files you own, no lock-in.

```bash
gh auth status      # GitHub authenticated?
vercel whoami       # or: npx vercel login
```

Then ask Claude to deploy. It ships only `records/website/<brand_id>/`
— the site and its own `assets/` folder — never this repo, so your
intake, research and records stay on your machine. On the GitHub path
it copies that folder out, inits git there, creates a private repo
named after your brand, and turns on Pages. Point your domain at it
from the host's dashboard; from then on, edit, redeploy, done. Files
you own, no lock-in.

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

## STEP 3 — The pattern behind the parts

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

1. **Ship the site.** You did that in STEP 2 — or you can, whenever
   you're ready. An unshipped brand stays a private document.
2. **Run the engines.** `/build:10-grow` — ads, email, and content,
   all reading this same foundation. That's how the brand shows up.
3. **Run the course on your real brand.** Start at
   `/build:02-research` with your own business. Faster this time —
   you know the pattern.

You built this brand to learn the moves. The real run starts when
you do it for yours.
