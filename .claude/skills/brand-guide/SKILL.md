---
name: brand-guide
description: Use when a brand foundation (and ideally design.md) already exist and the user wants a shareable brand guide — the document you hand a designer, client, or collaborator. Builds one self-contained brand-guide.html (story + rulebook) and exports brand-guide.pdf via headless Chrome. Never invents a claim.
---

# Brand Guide

You build the document someone actually sends: Part I is the story (what
this brand believes, who it's for, what it's against), Part II is the
rulebook (positioning, audience, voice of the customer, proof, colour,
type, components, messaging). This is a synthesis of decisions already made
elsewhere — never invent a new claim, quote, or rule here that isn't already
in the foundation, brand book, research file, or `design.md`.

## When this triggers

`records/brands/<brand_id>.json` exists (from `brand-foundation`) and the
user wants a shareable brand guide — HTML they can open and read, PDF they
can send.

## Prerequisite

`records/brands/<brand_id>.json` must exist. If not, stop and tell the user
to run `brand-foundation` first. If more than one brand exists, ask which.

`design.md` at the repo root is **optional but preferred** — if present, use
its exact palette/type/component values for Part II's rulebook instead of
re-deriving from `visual_pillars`. If absent, derive as `brand-website` does
and tell the user a `design-tokens` pass would sharpen this guide.

## What you do

### Step 0 — Read everything before writing anything

- `records/brands/<brand_id>.json` — positioning, audience, tone, visual
  pillars, avoid list.
- `records/brands/<brand_id>.md` (brand book) — the fuller prose version.
- `records/brands/<brand_id>-research.md` if it exists — this is your ONLY
  source for real customer quotes and competitor facts. If it doesn't
  exist, or is explicitly marked as a fixture/unverified, the "voice of the
  customer" section in Part II must say so plainly and skip inventing
  quotes.
- `design.md` at the repo root, if it exists — exact palette/type/component
  values for Part II.

### Step 1 — Part I: The Story

A short manifesto-style page, not a form. Cover, in the brand's actual
`tone`:
- What this brand believes (from `positioning`)
- Who it's for (from `audience`, in human terms, not a demographic bucket)
- What it's against (from `avoid` — the competitive fence, made into prose,
  not a bullet dump)

### Step 2 — Part II: The Book

Sections, each grounded in a specific source file — never write a value here
that doesn't trace to one:

1. **Positioning** — `positioning` field, verbatim or lightly tightened.
2. **Audience** — `audience` field, expanded with any real detail from the
   research file (if present).
3. **Voice of the customer** — real quotes from `records/brands/<brand_id>-research.md`
   ONLY, quoted verbatim with attribution to their source. **If the research
   file doesn't exist, or is a labeled fixture/test file, this section must
   say so explicitly instead of inventing quotes** — write "No sourced
   customer language exists yet — this section will populate once
   `brand-foundation` runs its real research pass" rather than fabricating
   anything that reads like proof.
4. **Proof and honesty rules**: two things, both required —
   - Any real, sourced fact from the research file worth stating.
   - **A "What we never claim" panel** — this is not optional. List every
     unprovable claim category this brand explicitly refuses to make
     (revenue figures without evidence, results you haven't had, named
     clients who haven't agreed, before/after stats with no source).
     Anything flagged UNVERIFIED anywhere in the research or foundation
     goes here, named specifically, not softened into "we're honest."
5. **Colour** — exact hex + role from `design.md` if present; else derive
   from `visual_pillars` and say so.
6. **Type** — exact font names + usage rules from `design.md` if present;
   else derive and say so.
7. **Components** — button/card/spacing rules from `design.md` if present;
   else a short derived set from the pillars.
8. **Messaging library** — 4-8 real example lines (headline-length, in the
   brand's `tone`, using the voice USE words from `design.md` if present)
   that a copywriter could lift directly. These are examples, not claims —
   don't put a specific number or stat in one unless it's sourced.

### Step 3 — Build `brand-guide.html`

One self-contained file at the **repo root**: `brand-guide.html`. Inline
CSS, no external JS framework. Style it using the same palette/type as
`design.md` (if present) so the guide itself demonstrates the brand instead
of contradicting it. Two visually distinct parts (Story, then Book), a
table of contents linking to Book subsections.

### Step 4 — Export `brand-guide.pdf`

Use headless Chrome to export the HTML to PDF:

```
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=brand-guide.pdf \
  --print-to-pdf-no-header \
  "file://$(pwd)/brand-guide.html"
```

(On Linux, substitute the system `google-chrome` or `chromium` binary.)

### Step 5 — Verify the export actually worked — do not trust exit code 0

A zero exit code only means Chrome didn't crash. It does NOT mean the PDF
has real content, correct page count, or renders your CSS.

1. Confirm the file exists and has a real size: `ls -la brand-guide.pdf`
   (a valid multi-page brand guide should be well over 20KB — a near-empty
   file means the page failed to render before printing).
2. Rasterize at least the first two pages and actually look at them:
   ```
   pdftoppm -r 100 -png brand-guide.pdf /tmp/brand-guide-check
   ```
   Then load `/tmp/brand-guide-check-1.png` (and page 2) with an image
   viewer/vision tool and confirm: text is present and legible, the
   palette/fonts from `design.md` actually rendered (not browser
   defaults), nothing is cut off or blank.
3. If anything looks wrong (blank page, wrong fonts, broken layout), fix
   `brand-guide.html` and re-export — never tell the user it's done based
   on the export command succeeding alone.

### Step 6 — Tell the user

Print both file paths. Tell them to open the HTML, then the PDF, and check:
does the story sound like this brand, not brand-guide prose in general? Is
every claim traceable to the foundation or research? Is the "what we never
claim" panel real and specific, not generic?

## Boundaries — never do these

- Never invent a customer quote, testimonial, or stat not present in the
  research file — an honest "no sourced language yet" beats a fabricated
  one.
- Never skip the "what we never claim" panel.
- Never report the PDF as done without actually rasterizing and looking at
  it — exit code 0 is not verification.
- Never write outside the repo root (`brand-guide.html` / `.pdf` live at the
  root, matching `design.md`'s convention).
