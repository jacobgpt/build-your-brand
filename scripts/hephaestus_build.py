#!/usr/bin/env python3
"""Hephaestus production: consume a validated creative_brief.json, build the
asset via the Higgsfield CLI, save it to disk. Builds AS WRITTEN — never
reinterprets the brief's intent.

Usage:
  python3 scripts/hephaestus_build.py <brief.json>

On success: prints a human status line, then a final line of JSON:
  {"asset_path": "...", "bytes": N, "model": "gpt_image_2"}
On failure (auth, rate limit, CLI missing): prints a clean human-readable
error to stderr and exits 1. Never lets a raw stack trace reach the screen.
"""
from __future__ import annotations
import json
import shutil
import subprocess
import sys
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "records" / "assets"
MODEL = "gpt_image_2"  # Hephaestus's tool choice per Pantheon OS catalog default (gpt_image_2 / nano_banana_2 / seedance_2_0) — production decides mechanism, not the brief.
QUALITY = "high"
RESOLUTION = "2k"
# gpt_image_2 supports: auto,1:1,4:3,3:4,16:9,21:9,9:16,3:2,2:3 — no 4:5. Map the
# brief's aspect_ratio (which uses a wider vocabulary) to the nearest supported value.
ASPECT_RATIO_MAP = {
    "1:1": "1:1",
    "16:9": "16:9",
    "9:16": "9:16",
    "4:5": "3:4",  # nearest supported portrait ratio
}


def clean_error(stderr: str, returncode: int) -> str:
    low = stderr.lower()
    if "not logged in" in low or "unauthorized" in low or "401" in low or "auth" in low and "login" in low:
        return (
            "HIGGSFIELD AUTH ERROR: the CLI is not logged in.\n"
            "Fix: run `higgsfield auth login` in a terminal, then re-run this build."
        )
    if "rate limit" in low or "429" in low or "too many requests" in low:
        return (
            "HIGGSFIELD RATE LIMIT: too many requests right now.\n"
            "Fix: wait ~60 seconds and re-run this build."
        )
    if "insufficient" in low and "credit" in low:
        return (
            "HIGGSFIELD OUT OF CREDITS: the account has no credits left.\n"
            "Fix: top up at higgsfield.ai, then re-run this build."
        )
    if '"nsfw"' in low or "status \"nsfw\"" in low or "flagged" in low:
        return (
            "HIGGSFIELD CONTENT FILTER: the model flagged this job (often a false positive on brand names / logos / real people).\n"
            "Fix: soften the brief's wording (drop the brand name, describe it generically) and re-run this build, "
            "or try a different model with `higgsfield model list --image`."
        )
    return f"HIGGSFIELD BUILD FAILED (exit {returncode}):\n{stderr.strip()[-800:]}"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: hephaestus_build.py <brief.json>", file=sys.stderr)
        return 2
    brief_path = Path(sys.argv[1])
    if not brief_path.exists():
        print(f"ERROR: brief not found: {brief_path}", file=sys.stderr)
        return 2

    if shutil.which("higgsfield") is None:
        print(
            "HIGGSFIELD CLI NOT FOUND: install it first (see README prerequisites).",
            file=sys.stderr,
        )
        return 1

    brief = json.loads(brief_path.read_text())
    brief_id = brief.get("brief_id", "unknown")

    # Build the prompt AS WRITTEN from the brief. Never add, drop, or reinterpret
    # the creative intent — but ad_copy, when present, MUST be rendered as real
    # on-image text, or a "static ad" comes out as bare product photography.
    prompt_parts = [
        brief.get("big_idea", ""),
        brief.get("visual_description", ""),
        brief.get("style_notes", ""),
    ]
    ad_copy = brief.get("ad_copy", {})
    if ad_copy.get("has_copy"):
        copy_instruction = f'Render this exact text on the image as real, legible typography: headline "{ad_copy.get("headline", "")}"'
        if ad_copy.get("subhead"):
            copy_instruction += f', subhead "{ad_copy["subhead"]}"'
        if ad_copy.get("cta"):
            copy_instruction += f', call-to-action "{ad_copy["cta"]}"'
        if ad_copy.get("placement"):
            copy_instruction += f'. Placement: {ad_copy["placement"]}.'
        copy_instruction += " Spell the text exactly as given, no substitutions."
        prompt_parts.append(copy_instruction)

    prompt = " ".join(p for p in prompt_parts if p).strip()
    aspect_ratio = ASPECT_RATIO_MAP.get(brief.get("aspect_ratio", "1:1"), "1:1")

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = ASSETS_DIR / f"{brief_id}-{ts}.json"  # higgsfield --wait --json returns result metadata incl. URL

    cmd = [
        "higgsfield", "generate", "create", MODEL,
        "--prompt", prompt,
        "--aspect_ratio", aspect_ratio,
        "--quality", QUALITY,
        "--resolution", RESOLUTION,
        "--wait",
        "--json",
    ]

    print(f"Running: higgsfield generate create {MODEL} --prompt \"<brief text>\" --aspect_ratio {aspect_ratio} --quality {QUALITY} --resolution {RESOLUTION} --wait --json")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

    if result.returncode != 0:
        print(clean_error(result.stderr, result.returncode), file=sys.stderr)
        return 1

    out_path.write_text(result.stdout)

    # Try to pull a downloadable URL out of the JSON result and fetch the actual file.
    asset_file_path = None
    asset_bytes = 0
    try:
        data = json.loads(result.stdout)
        url = None
        # Real `higgsfield ... --wait --json` shape: a top-level array of job
        # objects, each with "result_url" (full-res) — confirmed by a live
        # test call on 2026-08-30. Stay defensive for other shapes too.
        if isinstance(data, list) and data:
            first = data[0]
            if isinstance(first, dict):
                url = first.get("result_url") or first.get("min_result_url") or first.get("url")
        elif isinstance(data, dict):
            if "result_url" in data:
                url = data["result_url"]
            elif "url" in data:
                url = data["url"]
            elif "results" in data and isinstance(data["results"], list) and data["results"]:
                url = data["results"][0].get("url") or data["results"][0].get("result_url")
        if url:
            import urllib.request
            ext = ".png" if ".png" in url else (".jpg" if ".jpg" in url or ".jpeg" in url else ".bin")
            asset_file_path = ASSETS_DIR / f"{brief_id}-{ts}{ext}"
            urllib.request.urlretrieve(url, asset_file_path)
            asset_bytes = asset_file_path.stat().st_size
    except Exception as e:
        print(f"NOTE: could not auto-download asset file ({e}); raw result saved at {out_path}")

    print(f"Result metadata saved: {out_path}")
    if asset_file_path:
        print(f"Asset downloaded: {asset_file_path} ({asset_bytes} bytes)")
        print(json.dumps({"asset_path": str(asset_file_path), "bytes": asset_bytes, "model": MODEL}))
    else:
        print(json.dumps({"asset_path": str(out_path), "bytes": out_path.stat().st_size, "model": MODEL, "note": "metadata only, no direct file URL found"}))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
