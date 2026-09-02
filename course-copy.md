# Build Your Brand — Course Copy

**STATUS: draft script, ahead of the repo.** Originally written for nine
lessons; this repo only has skills for seven. Lessons 4 (brand guide) and 5
(design.md) below describe skills that DO NOT EXIST here — see the note in
each and the gap list at the bottom before recording anything. Command
labels below (`/build:0N-...`) are the ORIGINAL draft numbering and no
longer match the real slash commands shipped in `.claude/commands/build/`
(`01-setup`, `02-research`, `03-foundation`, `04-website`, `05-brief`,
`06-build`, `07-done`). Use the real commands when actually filming; treat
everything below as narration material to adapt, not a literal script.

---

## Lesson 01 — Setup

**Command:** `/build:01-setup` · **Time:** ~5 min
**Goal:** Repo cloned, both CLIs authenticated, skills visible

### The opening

Most people using AI have one assistant and forty browser tabs. Every job
starts from scratch, nothing remembers the last one, no record of why
anything was decided.

This is the other thing. Agents with fixed jobs, a gate that needs your
approval before anything gets made, a written record of every decision. By
the end you'll have a researched brand, a brand book, a design system, a
hero, a live site, and a finished asset — on your own machine.

Nine lessons. Everything happens in the terminal.

### What you need

```bash
claude --version
claude /login

higgsfield --version
higgsfield auth login
higgsfield account status
```

That last command should show your account and your credits. If it doesn't,
the auth didn't take — run the login again before you go on.

### Confirm the skills loaded

Claude Code picks up any skill in the project folder automatically. Nothing
to install.

```bash
claude -p "list your available skills"
```

If you see none, you're running `claude` from the wrong directory. Skills are
project-scoped — `cd` into the repo and try again.

### Watch it work

Second terminal:

```bash
python3 scripts/serve_dashboard.py
```

Open `http://localhost:8787/dashboard.html`. It reads the actual files in
`records/` — not a progress bar that lies to you, a view of what exists on
disk.

**→ Skills listed, `higgsfield account status` green. Next.**

---

## Lesson 02 — Deep research

**Command:** `/build:02-research` · **Time:** ~20 min
**Goal:** A sourced research file you've actually read

### Why this is first

Generic AI output comes from the same place: a prompt with nothing behind
it. The model fills the gaps with the average of everything it's seen, and
the average looks like everything else.

Research is what stops that. Not vibes about your market — real
competitors, the language customers actually use, the gap nobody's filling.

Everything in the next seven lessons is built on this file. Get it wrong and
everything downstream is confidently wrong.

### Write your paragraph

Four things: what it is, who it's for, why it's different, what it refuses to
look like.

Don't polish it. The skill researches around what you give it — this is a
starting point, not a brief.

### Run it

```bash
claude -p "Use brand-foundation to build a brand foundation from: <your paragraph>"
```

Real web search first. Give it a minute. `deepresearch.md` lands before
anything else does.

### Read it before you move

This is the step people skip and regret. A wrong assumption about your
customer, a competitor you didn't know about, a claim with nothing behind
it — this is where it shows up, and it's cheap to fix here and expensive
later.

Check the UNVERIFIED section in `project-knowledge.md` especially. Those
claims stay out of everything you build. Not because it's cautious — a
brand that only says what it can prove is the one people believe.

**→ Research read and sanity-checked. Next.**

---

## Lesson 03 — Brand foundation

**Command:** `/build:03-foundation` · **Time:** ~15 min
**Goal:** Six foundation documents and a machine-readable contract

### What just got built

The same run that did your research wrote six documents:

```
deepresearch.md         the dossier, sourced
avatar-sheet.md         the customer, in their own words
offerbrief.md           product, promise, mechanism, proof, pricing
necessary-beliefs.md    what someone must accept before they buy
project-knowledge.md    the synthesis, verified vs unverified
brand-book.md           the readable brand book
```

Plus `brand_foundation.json` — the same reasoning in structured form.

### Why both

The `.md` files are for you. The `.json` is for the agents.

Everything that builds from here reads the JSON, so every brief and every
page inherits the same positioning without you restating it. One source of
truth, two forms.

### Read the brand book

Open `brand-book.md`. Check the positioning is actually yours. Check the
no-go list has teeth rather than generic softness — "we avoid clichés" isn't
a constraint, "we never show a person smiling at a laptop" is.

Edit it by hand if it's wrong. It's your file. The agent proposes, you
decide — that's the pattern for the whole course.

**→ Six documents read, brand book edited. Next.**

---

## Lesson 04 — The brand guide

**Command:** `/build:04-guide` · **Time:** ~15 min
**Goal:** A brand guide as HTML and PDF

### Documents aren't a brand guide

Six markdown files are raw material. A brand guide is the thing you send
someone — a designer, a client, a collaborator — that answers their
questions before they ask.

Two parts. The story: what this brand believes, who it's for, what it's
against. The book: the rules. Colour with hex codes, type, voice, what you
claim and what you never claim.

### Build it

```bash
claude -p "Use brand-guide to build the guide for <brand_id>"
```

Reads the foundation, writes one self-contained HTML file, exports a PDF.

### The panel most people skip

There's a section for what you never claim. Revenue you can't evidence,
results you haven't had, clients who haven't agreed to be named.

Writing that list down is uncomfortable, and it's the most useful page in
the document. It's what stops you making a claim in six months you can't
back when someone checks.

### Open both

Read the HTML, then the PDF. Does the story sound like your brand or like a
brand? Are the customer quotes real ones from your research, or invented?

Anything off — say exactly what, and re-export.

**→ Guide built, both files read. Next.**

---

## Lesson 05 — design.md

**Command:** `/build:05-design` · **Time:** ~10 min
**Goal:** One file that makes every build on-brand from the first line

### Why most AI sites look identical

Same instruction, same model, no design system. The model reaches for its
default, and its default is everyone's default.

`design.md` is the fix. Exact hex codes, named fonts, the rule for when the
accent colour appears, the words your brand uses and the words it never
uses. It sits in the project root and everything reads it.

### Build it

```bash
claude -p "Use design-tokens to write design.md for <brand_id>"
```

Distilled from your brand book — you already made these decisions in lesson
04, this just extracts them into a form a build can obey.

### Specific beats vague

Check it. "Warm blue" is useless. `#1B4B8F` is a decision.

If any line in that file could describe two different brands, it isn't
finished. Tighten it now — every build after this inherits it.

**→ design.md in the project root. Next.**

---

## Lesson 06 — The hero

**Command:** `/build:06-hero` · **Time:** ~20 min
**Goal:** A hero still and a hero video in `assets/`

### Still first, always

A strong still makes a strong video. A weak still makes a weak video with
motion on it.

Two moves: generate the still, approve it, then animate it.

### The still

```bash
claude -p "Use hephaestus-production to build a hero still for <brand_id>"
```

Reads your brand foundation and `design.md`. Cinematic, on-brand, with room
where the headline will sit. No text in the image — the site puts copy on
top.

The gate fires before it spends anything. Read what it's about to build,
then approve.

### The motion

Subtle only. Slow push-in, ambient drift, light movement. It's a background
that text has to stay readable on top of — if the motion competes with the
headline, it's wrong.

Five to eight seconds, looping.

### If it comes back bad

It might. Video is the least predictable part of this pipeline, worth
saying plainly instead of pretending otherwise.

Almost always the fix is upstream: a stronger still, not a better motion
prompt. Go back, regenerate the still, try again. The gate means a bad one
costs you a keystroke, not a credit.

**→ `hero.mp4` and a poster in `assets/`. Next.**

---

## Lesson 07 — The website

**Command:** `/build:07-website` · **Time:** ~25 min
**Goal:** A real site, built from everything so far

### Copy first, then the page

Most AI websites look the same because they're built layout-first — pick a
template, pour words in. This goes the other way. Copy gets written from
your foundation, then the page gets built around the copy.

One section per belief. Your `necessary-beliefs.md` decides what sections
exist; the design just dresses them.

### Build it

```bash
claude -p "Use brand-website to build a website for the <brand_id> brand"
```

Reads the foundation, `design.md`, and the hero from lesson 06. Every visual
choice traces back to a specific rule — it's commented inline in the CSS, so
you can check rather than trust.

### Serve it from the repo root

Not from the site's own folder. The page references shared assets by
relative path, and Python's server won't traverse above its working
directory.

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000/records/website/<brand_id>/index.html`.

### Read it as a stranger

Does the first line say what this is? Does each section do one job? Is
there a claim on that page you couldn't back up if someone asked?

That last one matters most. Every unprovable line costs you more than it
earns.

**→ Site running locally. Next.**

---

## Lesson 08 — Direction and production

**Command:** `/build:08-assets` · **Time:** ~20 min
**Goal:** A finished asset, through a typed brief and a gate

### Two jobs, not one

Most AI setups collapse two decisions into one prompt: what should exist,
and how to make it. That's why output drifts — the thing choosing the idea
also chose the execution, and nothing checked either.

Here they're split.

**Aphrodite** decides what should exist and why. She never picks a tool,
never picks a model, never touches Higgsfield. That's the point — she can't
quietly bend the idea to suit the renderer.

**Hephaestus** decides how to build it. He reads the brief exactly as
written and doesn't revisit the creative call.

### Write a brief

```bash
claude -p "Use aphrodite-direction to write a creative brief for: <one line>"
```

She reads your foundation first. Every field is built on top of it.

Open what came out. It's JSON, matching a fixed schema — deliberately. A
brief written as prose has to be interpreted, and interpretation is where
intent gets lost. A typed brief has slots, and the agent receiving it reads
slots.

If the brief is wrong, the asset will be wrong. Cheaper to fix here.

### The gate

Between the two, nothing happens without you.

`scripts/approval_gate.py` shows you the brief and waits. Type `y` and it
builds. Anything else and it doesn't.

There's a test in this repo that fails if the gate is removed. Not
decoration — it means the gate can't quietly disappear in a refactor six
months from now.

Agents are good at volume and bad at judgement. The failure mode of an
ungated system isn't one bad output, it's forty overnight, spending real
credits, discovered afterwards. The gate costs a keystroke and buys you the
ability to run agents on things that matter.

### Build it

```bash
claude -p "Use hephaestus-production to build the brief at records/briefs/<brief_id>.json"
```

Read the brief on screen — properly, don't just hit `y`. Then approve.

The file lands in `records/assets/`. A dated run record writes to
`records/runs/`.

### Reject one on purpose

Before you move on, run it again and reject.

Look at what got written. The rejection is in the record too — dated, with
the reason. Most systems only log success, and a record that only contains
what worked isn't a record, it's a highlight reel.

**→ One asset built, one rejected, both on record. Next.**

---

## Lesson 09 — What you built

**Command:** `/build:09-done` · **Time:** ~5 min

### Look at it

```
records/brands/<id>/    six documents + the foundation contract
brand-guide.html/.pdf   the guide
design.md               the design system
assets/                 hero still, poster, video
records/briefs/         every brief written
records/runs/           every decision, approved and rejected, dated
records/assets/         the finished files
records/website/        the site
```

Files on your machine, in a structure you can inspect, that someone else
could audit. Not a chat log you'll never open again.

### What you've got

- A brand built on research instead of vibes, with the unprovable claims
  separated out and labelled
- A guide you can hand to anyone
- A design system every future build obeys
- A hero, a site, and a finished asset — all from the same source of truth
- A gate that means nothing gets made without you
- A record of every decision, including the ones you said no to

### The pattern, not the parts

The useful thing here isn't Aphrodite and Hephaestus.

It's the shape: split the decision from the execution, type the handoff
between them, put a human at the consequential step, write down what
happened.

That shape works for outreach, support, research, ops — anything you'd
otherwise do by prompting a general assistant forty times and hoping.

Two agents is where it starts.

**Run it on your own brand next.**

---

## Notes for you

- Every command here is from your README or the phased build. Nothing
  invented.
- **Lesson 06 is the fragile one.** This repo doesn't have `/build:` slash
  commands or a `hephaestus-production` hero-still/video path wired up yet —
  only `brand-foundation`, `aphrodite-direction`, `hephaestus-production`
  (static image only), and `brand-website` exist right now. Before filming,
  confirm hero video actually works end-to-end, or rewrite this section to
  "generate the still, animate it in the Higgsfield app, drop the file back."
- **The honest bits — "if it comes back bad" in 06, "reject one on purpose"
  in 08 — earn more trust than they cost.** They pre-empt disappointment and
  point at the real fix.
- **Lesson 08 absorbed the old gate lesson.** It had nothing to run on its
  own, which reads flat on camera. Now the gate is explained at the moment
  it fires.
- **Repo gap:** as of this draft, `/build:01-setup` through `/build:09-done`
  slash commands don't exist in `aphrodite-hephaestus-course` — the README
  uses plain `claude -p "Use <skill> to..."` calls instead. Either build the
  nine slash commands to match this script, or rewrite the command lines
  above to the actual `claude -p` invocations before recording.
