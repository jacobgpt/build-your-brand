---
description: "Build Your Brand — Lesson 3: Brand foundation. Validate the contract, review, edit if wrong."
---

# /build:03-foundation

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
LESSON 3 · BRAND FOUNDATION
THE CONTRACT
──────────────────────────────────────────────────
```

> **Timing**     ~10 minutes
> **Goal**       A validated brand contract, reviewed and edited where you disagreed
> **Progress**   `[██░░░░░░░░] 2/9 · starting`

---

## The agent proposes, you decide

The `brand-foundation` run from Lesson 2 already wrote all nine files
to `records/brands/<brand_id>/`. This lesson is about verifying the
contract and making it yours. Nothing new gets built here.

---

## STEP 1 — Validate the JSON

The JSON is what every later skill actually reads — so it goes through
a validator first:

```bash
python3 scripts/validate_brief.py records/brands/<brand_id>/brand_foundation.json --schema brand_foundation
```

Must print `VALID`. If it doesn't, fix the JSON or re-run
`brand-foundation` until it does — never move on with an unvalidated
foundation.

> **ACTION:** Run the validator. `VALID` on screen? Type `1`.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Contract validated                              │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[██░░░░░░░░] 2/9 · Step 1/2`

---

## STEP 2 — Review every file, edit what's wrong

Read them all. This is where a wrong assumption is cheap to fix and
expensive later.

- **`avatar-sheet.md`** — does the customer sound like someone you
  recognize? Are the pains the ones you hear on sales calls? Any
  pain stated as fact that's actually just inference?
- **`offerbrief.md`** — is the promise one a real customer would
  repeat back to you? Is the mechanism ownable, or could a
  competitor claim it tomorrow? Pricing matches what you said?
- **`necessary-beliefs.md`** — could you sell someone who believed
  these six things? If any belief is something everyone already
  believes, it isn't earning its place.
- **`brand-book.md`** — is the positioning actually yours, not
  something a competitor could paste onto their own business
  unchanged? Does the `avoid` list have teeth — "we never show a
  person smiling at a laptop" beats "we avoid clichés"?
- **`deepresearch.md`** — spot-check two or three cited claims. Do
  the URLs actually say what the file says they say?

It's your files — edit by hand where anything's wrong. The agent
proposes, you decide. If you hand-edit `brand-book.md`, mirror any
real change in `brand_foundation.json` too: the JSON is what every
later skill actually reads, so it needs to stay in sync with the
readable version.

**The bar for positioning:** read it aloud. If a competitor could
paste it onto their homepage unchanged, it isn't yours yet. If it
makes you slightly uncomfortable because it commits to something
checkable, it's right. "Premium coffee for people who care" is the
former. "Beans that arrive when you're actually running low — not
when a calendar says so" is the latter.

> **ACTION:** Read the brand book. Edit anything that isn't you.
> Type `1` when every line sounds like something you would actually
say about your own business.

```
┌─────────────────────────────────────────────────┐
│  ACHIEVEMENT UNLOCKED                            │
│  Foundation reviewed, owned                       │
└─────────────────────────────────────────────────┘
```

> **Progress**  `[███░░░░░░░] 3/9 · Lesson 3 complete`

---

## DONE

**What you have now:**
- A validated `brand_foundation.json` — the contract every later skill reads
- A brand book you've actually read and edited where needed

**Next lesson:** `/build:04-design` — choose your visual direction from
real options, and lock it into `design.md`.
