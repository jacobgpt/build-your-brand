---
description: "Build Your Brand, Lesson 9: The record. Review every file, ship the site if you want, and name the pattern you'll reuse."
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

**LESSON 9 OF 10 · THE RECORD**
About ten minutes. You leave with the whole build confirmed against the disk, and a next move for your own brand.

---

## STEP 1 · Look at what exists

```
records/brands/<brand_id>/    nine files: answers, copywriter prompt,
                              six documents, the contract
design.md                     the design system
brand-guide.html / .pdf       the brand book
records/assets/               hero still (and video, if you built it),
                              finished assets
records/briefs/               every brief written
records/runs/                 every decision, approved or refused, dated
records/website/<brand_id>/   the site, with its own assets/
```

Files on your machine, in a structure someone else could audit. Not a
chat log.

Confirm it against the disk:

```bash
python3 scripts/dashboard_status.py
```

Reload `http://localhost:8787/dashboard.html`.

> **CHECK.** Dashboard matches what's on disk. Say `next`.

---

## STEP 2 · Ship it, if you want to

A site on your laptop is a private document. Claude can put it on a
live URL. The site is one static `index.html` plus its own `assets/`,
so any static host takes it as-is. Claude picks the path from what's
on your machine:

| You have | It ships via |
|---|---|
| `vercel` CLI, logged in | `vercel --prod --yes`, a live `*.vercel.app` URL |
| `netlify` CLI, logged in | `netlify deploy --prod`, a live URL |
| `gh` CLI, logged in | a private GitHub repo and GitHub Pages, a live `*.github.io` URL |
| none of these | Claude offers to set one up; `gh` and Pages is the zero-cost default |

Nothing deploys until you say so. Claude checks what's installed,
names the path, shows you exactly what it will run, and asks
`Ship it? [y/N]`. Read it, then answer. Hosting is the host's normal
free tier. Skipping is a real choice: the site stays local and you
ship later.

Before you say yes:

- [ ] Every link works. Click them.
- [ ] Phone width reads well.
- [ ] No claim, stat or testimonial you can't back.
- [ ] The hero loads, video or fallback, and the button does something.
- [ ] You've read the whole page as a stranger.

Any box empty is an `N`. Fix it, come back.

What ships is `records/website/<brand_id>/` alone: the site and its
`assets/`. Never this repo. Your answers, your research and your
records stay on your machine. On the GitHub path Claude copies that
folder out, initialises git there, creates a private repository named
for your brand, and turns Pages on. Point your domain at it from the
host's settings. After that: change the file, redeploy, done.

```bash
gh auth status      # GitHub logged in?
vercel whoami       # or: npx vercel login
```

> **CHECK.** Live on a URL, or deliberately deferred. Say `next`.

---

## STEP 3 · The pattern under the parts

The reusable thing isn't Aphrodite and Hephaestus. It's the shape.
Separate deciding from doing. Type the handoff between them. Put a
person at the step that costs money. Write down what happened, either
way.

That shape runs past creative work. Outreach, support, research,
operations: anywhere you'd otherwise prompt a general assistant forty
times and hope.

The record matters because exit codes lie. An image model will draw
something that passes at a glance and breaks a rule you set. The gate
is where you look before it ships, refuse the wrong ones, and rebuild.
Keeping the refusals is what makes it a record instead of a highlight
reel.

> **CHECK.** You built this on a practice brand. The real run is the
> same moves on yours. Say `next` to close.

---

## On record

- A brand built on evidence, with the unprovable claims named and kept
  out
- A brand book you can hand to anyone
- A design system every build obeys
- A hero and a site, both traceable to one source of truth
- A gate that means nothing is made without you
- A record of every decision, including the refusals

Three moves from here, in order:

1. **Ship the site.** STEP 2, whenever you're ready.
2. **Run the engines.** `/build:10-grow`: ads, email and content that
   read this same foundation.
3. **Run it on your own brand.** Start at `/build:02-research` with
   your real business. Faster this time.

Lesson 9 complete.
