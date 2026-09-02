#!/usr/bin/env python3
"""Approval gate: show a brief, wait for explicit y/n, write a dated record.

Usage:
  python3 scripts/approval_gate.py <brief.json>

Behavior:
  - Prints the brief for human review.
  - Prompts: "Approve build? [y/N]"
  - On approve: proceeds to build via hephaestus_build.py, then writes a
    record file with status "built".
  - On reject: writes a record file with status "rejected" and exits without
    building anything.

Record file: records/runs/<brief_id>-<timestamp>.json
"""
from __future__ import annotations
import json
import subprocess
import sys
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = ROOT / "records" / "runs"


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def now_slug() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def write_record(brief: dict, decision: str, produced: dict | None, error: str | None) -> Path:
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    record = {
        "brief_id": brief.get("brief_id"),
        "recorded_at": now_iso(),
        "asked": brief.get("one_line_input"),
        "brief_snapshot": brief,
        "decision": decision,
        "produced": produced,
        "error": error,
    }
    path = RUNS_DIR / f"{brief.get('brief_id', 'unknown')}-{now_slug()}.json"
    path.write_text(json.dumps(record, indent=2))
    return path


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: approval_gate.py <brief.json>", file=sys.stderr)
        return 2
    brief_path = Path(sys.argv[1])
    if not brief_path.exists():
        print(f"ERROR: brief not found: {brief_path}", file=sys.stderr)
        return 2

    brief = json.loads(brief_path.read_text())

    print("=" * 60)
    print("CREATIVE BRIEF — REVIEW BEFORE BUILD")
    print("=" * 60)
    print(f"brief_id:      {brief.get('brief_id')}")
    print(f"one_line_input:{brief.get('one_line_input')}")
    print(f"big_idea:      {brief.get('big_idea')}")
    print(f"visual:        {brief.get('visual_description')}")
    print(f"style:         {brief.get('style_notes')}")
    print(f"aspect_ratio:  {brief.get('aspect_ratio')}")
    print(f"must_preserve: {brief.get('must_preserve')}")
    print(f"forbidden:     {brief.get('forbidden')}")
    print("=" * 60)

    answer = input("Approve build? [y/N] ").strip().lower()

    if answer != "y":
        record_path = write_record(brief, "rejected", None, None)
        print(f"REJECTED. Record written: {record_path}")
        return 0

    print("APPROVED. Building via Hephaestus...")
    build_script = ROOT / "scripts" / "hephaestus_build.py"
    result = subprocess.run(
        [sys.executable, str(build_script), str(brief_path)],
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        record_path = write_record(brief, "approved-build-failed", None, result.stderr.strip()[-2000:])
        print(f"BUILD FAILED. Record written: {record_path}")
        return 1

    # hephaestus_build.py prints a final JSON line with the produced asset info
    produced = None
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                produced = json.loads(line)
            except json.JSONDecodeError:
                pass

    record_path = write_record(brief, "built", produced, None)
    print(f"BUILT. Record written: {record_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
