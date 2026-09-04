#!/usr/bin/env python3
"""Serve dashboard.html locally, regenerating status.json on every request.

Usage:
  python3 scripts/serve_dashboard.py [port]
Defaults to port 8787. Opens http://localhost:8787/dashboard.html — refresh
the page after each stage to see it update live, no restart needed.
"""
from __future__ import annotations
import http.server
import subprocess
import sys
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS_SCRIPT = ROOT / "scripts" / "dashboard_status.py"
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8787


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/status.json"):
            subprocess.run([sys.executable, str(STATUS_SCRIPT)], cwd=ROOT, capture_output=True)
        super().do_GET()


def main() -> int:
    sys.path.insert(0, str(ROOT / "scripts"))
    try:
        from banner import banner, want_color  # type: ignore
        print(banner(want_color([])))
        print()
    except Exception:
        pass
    subprocess.run([sys.executable, str(STATUS_SCRIPT)], cwd=ROOT, capture_output=True)
    url = f"http://localhost:{PORT}/dashboard.html"
    print(f"Serving dashboard at {url} (Ctrl+C to stop)")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    import os
    os.chdir(ROOT)
    with http.server.HTTPServer(("localhost", PORT), Handler) as httpd:
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
