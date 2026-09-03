#!/usr/bin/env python3
"""Approval gate: show a brief, take a human decision, write a dated record.

Usage:
  python3 scripts/approval_gate.py <brief.json>                 # in YOUR terminal: prompts you
  python3 scripts/approval_gate.py --decision y <brief.json>    # after you typed y to Claude
  python3 scripts/approval_gate.py --decision n <brief.json>    # after you typed anything else

How the gate holds:
  - In a real terminal with no --decision, it prints the brief and asks
    "Approve build? [y/N]". You type the answer.
  - With --decision, it records the decision you already gave Claude in the
    session. Claude Code's own permission dialog shows the exact command,
    --decision included, before it runs; only a human can allow it
    (.claude/settings.json lists this script under "ask").
  - Piped stdin is refused. `echo y | approval_gate.py` writes no record and
    builds nothing.
  - On y it runs scripts/hephaestus_build.py, which is the only path to the
    Higgsfield CLI; direct calls to both are denied in .claude/settings.json.

Record file: records/runs/<brief_id>-<timestamp>.json
"""
from __future__ import annotations
import argparse
import json
import subprocess
import sys
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = ROOT / "records" / "runs"
BUILD_SCRIPT = ROOT / "scripts" / "hephaestus_build.py"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def now_slug() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def build_settings() -> dict:
    """Read the production constants so the gate can say what a y will use."""
    out = {}
    try:
        for line in BUILD_SCRIPT.read_text().splitlines():
            for key in ("IMAGE_MODEL", "VIDEO_MODEL", "QUALITY", "RESOLUTION", "VIDEO_RESOLUTION", "VIDEO_DURATION"):
                if line.startswith(key + " ="):
                    out[key] = line.split("=", 1)[1].split("#", 1)[0].strip().strip('"')
    except OSError:
        pass
    return out


def write_record(brief: dict, decision: str, decided_via: str, produced: dict | None, error: str | None) -> Path:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "brief_id": brief.get("brief_id"),
        "recorded_at": now_iso(),
        "asked": brief.get("one_line_input"),
        "brief_snapshot": brief,
        "decision": decision,
        "decided_via": decided_via,
        "produced": produced,
        "error": error,
    }
    path = RUNS_DIR / f"{brief.get('brief_id', 'unknown')}-{now_slug()}.json"
    path.write_text(json.dumps(record, indent=2))
    return path


def show(brief: dict) -> None:
    print("=" * 60)
    print("CREATIVE BRIEF — REVIEW BEFORE BUILD")
    print("=" * 60)
    print(f"brief_id:      {brief.get('brief_id')}")
    print(f"asset_type:    {brief.get('asset_type', 'general')}")
    print(f"one_line_input:{brief.get('one_line_input')}")
    print(f"big_idea:      {brief.get('big_idea')}")
    print(f"visual:        {brief.get('visual_description')}")
    print(f"style:         {brief.get('style_notes')}")
    print(f"aspect_ratio:  {brief.get('aspect_ratio')}")
    print(f"must_preserve: {brief.get('must_preserve')}")
    print(f"forbidden:     {brief.get('forbidden')}")
    s = build_settings()
    is_video = str(brief.get("brief_id", "")).find("-hero-video") != -1 or brief.get("asset_type") == "hero-video"
    if s:
        if is_video:
            print(f"will run:      {s.get('VIDEO_MODEL')} · {s.get('VIDEO_RESOLUTION')} · {s.get('VIDEO_DURATION')}s image-to-video")
        else:
            print(f"will run:      {s.get('IMAGE_MODEL')} · quality {s.get('QUALITY')} · {s.get('RESOLUTION')}")
    print("credits:       Higgsfield charges per generation. Check `higgsfield account status` before and after.")
    print("=" * 60)


def main() -> int:
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("brief", type=Path)
    parser.add_argument("--decision", choices=["y", "n"], default=None,
                        help="the answer the human already gave in the Claude session")
    args = parser.parse_args()

    if not args.brief.exists():
        print(f"ERROR: brief not found: {args.brief}", file=sys.stderr)
        return 2
    brief = json.loads(args.brief.read_text())

    show(brief)

    if args.decision is not None:
        answer = args.decision
        decided_via = "session-answer-then-permission-dialog"
    elif sys.stdin.isatty():
        answer = input("Approve build? [y/N] ").strip().lower()
        decided_via = "terminal"
    else:
        sys.stdout.flush()
        print(
            "NO HUMAN AT THE GATE: stdin is not a terminal and no --decision was given.\n"
            "Piped input is not accepted. Either run this in your own terminal, or answer\n"
            "Claude's `Approve build? [y/N]` in the session and let it re-run with\n"
            "--decision y or --decision n. Nothing was built and nothing was recorded.",
            file=sys.stderr,
        )
        return 2

    if answer != "y":
        record_path = write_record(brief, "rejected", decided_via, None, None)
        print(f"REJECTED. Record written: {record_path}")
        return 0

    print("APPROVED. Building via Hephaestus...")
    result = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT), str(args.brief)],
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        record_path = write_record(brief, "approved-build-failed", decided_via, None, result.stderr.strip()[-2000:])
        print(f"BUILD FAILED. Record written: {record_path}")
        return 1

    produced = None
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                produced = json.loads(line)
            except json.JSONDecodeError:
                pass

    record_path = write_record(brief, "built", decided_via, produced, None)
    print(f"BUILT. Record written: {record_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
