# Build Log

Dated record of significant build events — what was attempted, what came
back, and what was decided. This is not a changelog of code; it's a record
of the gate and the pipeline actually doing their job, including the times
they caught something wrong.

---

## 2026-09-02 — Hero-still build for `quiet-desk`: v1 rejected, v2 approved

**Context:** Hephaestus-production was extended (since removed from this
shipping repo — see the removal note below) to build a brand's hero still
through the standard approval gate: `aphrodite-direction` writes a brief,
`scripts/approval_gate.py` shows it for human review, and only on `y` does
`scripts/hephaestus_build.py` call the real Higgsfield CLI.

### Attempt 1 — `quiet-desk-hero-still` — REJECTED

Brief (`records/briefs/quiet-desk-hero-still.json`, still on disk) explicitly
set:
- `must_preserve`: "no readable text or logo renders anywhere in the image
  itself — this is a text-free plate"
- `forbidden`: "no on-image text, logo, or wordmark of any kind"

Run record: `records/runs/quiet-desk-hero-still-20260902T131743Z.json`,
decision `built` (the gate approved it — the *image model* is what violated
the brief, not the gate).

The brief was approved at the gate (typed `y` at the live `Approve build?
[y/N]` prompt) and built for real via `higgsfield generate create
gpt_image_2` — real spend, ~8.5 credits. The resulting image
(`records/assets/quiet-desk-hero-still-20260902T131604Z.png`) was then
inspected with a vision model per the skill's own verification rule ("do
not trust exit code 0"). It came back **with fabricated text baked into the
image**, directly violating the brief:

- **"ZERO-ZONE DESK MAT"** — a fabricated brand/product label, legibly
  printed on the desk mat.
- **"METHOD 4161"** — a fabricated model/method number on the switch tray.
- Assorted instrument-panel text (`dB SPL`, `FAST`, `20kHz`) that, while
  arguably in the spirit of the brand's "show the measurement" pillar, came
  bundled with the two fabricated brand markings above.

**Decision: rejected.** This asset was not used anywhere. The failure mode
is real and worth recording: a general instruction like "no logo, no
on-image text" was not a strong enough constraint for this image model — it
still hallucinated a competing fake brand onto the product.

### Attempt 2 — `quiet-desk-hero-still-v2` — APPROVED, clean

New brief (`records/briefs/quiet-desk-hero-still-v2.json`, still on disk)
rewrote the constraint to be explicit and per-surface instead of one general
rule: the mat, the switches, the tray/rig hardware, and the ruler were each
individually specified as "blank and unmarked," with the dB-meter's numeric
readout carved out as the one required exception (the brand's own core
mechanism, not a forbidden element).

Run record: `records/runs/quiet-desk-hero-still-v2-20260902T132400Z.json`,
decision `built`.

Approved at the gate (`y`), built for real (~8.5 credits), and this time the
vision-model inspection came back clean: no fabricated text, logos, brand
names, or model numbers anywhere in frame — only the required dB-meter
digits and the ruler's functional measurement tick marks.

**Decision: approved.** This was the asset that would have fed the
(since-removed) hero-video step.

### Why this stays in the log even though the code doesn't

The hero-still/hero-video feature itself was removed from this shipping
repo (not approved for the video spend, and the feature was pulled back out
entirely — see commits following this log entry). But the *event* — the
gate approving a build, that build coming back wrong, a vision-based
verification step catching it, and a rebuilt version coming back right — is
exactly the failure mode the approval gate and the "don't trust exit code 0"
verification rule exist to catch. It's the proof the pattern works, kept on
record independent of whether this particular feature ships.
