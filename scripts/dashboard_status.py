#!/usr/bin/env python3
"""Write dashboard status.json by checking what's actually in records/.

Real-file-based, not self-reported: a stage counts as done only if its
output files genuinely exist on disk.

Usage:
  python3 scripts/dashboard_status.py
Writes status.json at the repo root (same dir dashboard.html serves from).
Run this after each stage, or leave scripts/serve_dashboard.py running and
it refreshes on every dashboard page load.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def has_files(dir_path: Path, pattern: str) -> bool:
    return dir_path.exists() and any(dir_path.glob(pattern))


def main() -> int:
    brands_dir = ROOT / "records" / "brands"
    briefs_dir = ROOT / "records" / "briefs"
    runs_dir = ROOT / "records" / "runs"
    website_dir = ROOT / "records" / "website"

    status = {
        "brand": has_files(brands_dir, "*/brand_foundation.json"),
        "brief": has_files(briefs_dir, "*.json"),
        # "asset" done means at least one run record shows a successful build,
        # not just an attempt (a rejected run should not count as done).
        "asset": any(
            json.loads(p.read_text()).get("decision") == "built"
            for p in runs_dir.glob("*.json")
        ) if runs_dir.exists() else False,
        "website": has_files(website_dir, "*/index.html"),
    }

    out_path = ROOT / "status.json"
    out_path.write_text(json.dumps(status, indent=2))
    print(f"status.json written: {status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
