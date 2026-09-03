---
description: "Build Your Brand — Lesson 5: The brand guide. Build the scrollable visual brand book (HTML + PDF), verify the export by looking at it."
---

# /build:05-guide

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
LESSON 5 · THE BRAND GUIDE
THE BOOK
──────────────────────────────────────────────────
```

> **Timing**     ~15 minutes
> **Goal**       A scrollable visual brand book in HTML and PDF, verified by looking at it
> **Progress**   `[████░░░░░░] 4/9 · starting`

---

## Documents aren't a brand guide

Markdown files are raw material. A brand guide is the thing you send
someone — a designer, a client, a collaborator — that answers their
questions before they ask.

The format matters: a book you scroll, with every rule **shown**
rendered on the page.

---

## STEP 1 — Brand inputs

The build asks you three quick things — have answers ready:

1. **Logo** — got one? Drop it in
   `records/brands/<brand_id>/assets/`. No logo yet? The book renders
   a typographic wordmark lockup from your `design.md` instead.
2. **Photos** — any founder, product, or environment shots? Drop
   them in `assets/` too. None is fine.
3. **Mood** — your three words for the brand's feel, plus one or two
   sites whose look you admire.

> **ACTION:** Answers ready (or "skip"). Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Brand inputs ready                              │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[████░░░░░░] 4/9 · Step 1/3`

---

## STEP 2 — Build the brand book

```bash
claude -p "Use brand-guide to build the guide for <brand_id>"
```

This reads your foundation documents and `design.md`, and writes one
self-contained scrollable `brand-guide.html`, then captures a cover
screenshot and exports `brand-guide.pdf` via headless Chrome:

- Part I — the story: what this brand believes, who it's for, what
  it's against
- Part II — the book, every rule rendered: palette as large colour
  swatches with hex + role, type as live specimens at real sizes, a
  real button and card built from your component rules, USE/AVOID
  voice as side-by-side columns, a messaging library in your brand's
  own type
- An atmosphere & imagery section — the brand's photographic
  direction
- A "what we never claim" panel for anything UNVERIFIED

The guide itself is styled in your palette — it demonstrates the
brand instead of describing it.

> **ACTION:** Run the build. When `brand-guide.html`,
> `brand-guide-cover.png`, and `brand-guide.pdf` exist, type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Brand book built                                │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[████░░░░░░] 4/9 · Step 2/3`

---

## STEP 3 — Verify by looking at the pages

**Don't assume the export worked because the command exited zero.**
Check the file size:

```bash
ls -la brand-guide.pdf
```

Should be well over 20KB. Then actually look at it:

```bash
pdftoppm -r 100 -png brand-guide.pdf /tmp/brand-guide-check
```

and view the resulting PNG(s). Confirm text isn't cut off, colours
rendered, no blank pages. A zero exit code is not proof the PDF is
readable.

Then read the HTML and the PDF both, and hold it to this:

- **Real quotes** — are the customer quotes verbatim ones from
  `deepresearch.md` with sources, or invented?
- **The honesty panel** — does "what we never claim" name real gaps
  (no pricing set, no measured results yet)? Generic hedging means the panel isn't doing its job.
- **The voice test** — read the story aloud; does it sound like YOUR
  brand, or like a brand?
- **The stranger test** — hand the HTML to someone (or imagine
  handing it) who knows nothing about you: can they say what this
  brand is, who it's for, and what it looks like, without asking?
- **The designer test** — could a designer build the NEXT page from
  Part II alone, without asking you a single question about colour,
  type, or tone? If they'd have to ask, Part II isn't done.

Anything off — say exactly what, and re-export.

> **ACTION:** File size checked, pages rasterized and viewed, both
> files read. Type `1` when it's clean.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Brand book verified by looking         │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[█████░░░░░] 5/9 · Lesson 5 complete`

---

## DONE

**What you have now:**
- A scrollable visual brand book (`brand-guide.html`) — palette,
  type, components shown live, styled in your own design tokens
- A cover screenshot and a PDF export you verified by actually
  looking at them

**Next lesson:** `/build:06-hero` — a hero image for the brand, built
through the approval gate.
