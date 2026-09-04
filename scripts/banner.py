#!/usr/bin/env python3
"""Print the course banner. The A and the I render in orange (256-colour 208)
when stdout is a terminal; plain glyphs otherwise, so logs and pipes stay clean.

  python3 scripts/banner.py           # orange in a terminal
  python3 scripts/banner.py --plain   # never colour
"""
from __future__ import annotations
import os
import sys

ROWS = [
    ("     ██  ", "█████", "  ", "██", "  ██████  ██████  ██████"),
    ("     ██ ", "██   ██", " ", "██", " ██      ██    ██ ██   ██"),
    ("     ██ ", "███████", " ", "██", " ██      ██    ██ ██████"),
    ("██   ██ ", "██   ██", " ", "██", " ██      ██    ██ ██   ██"),
    (" █████  ", "██   ██", " ", "██", "  ██████  ██████  ██████"),
]
TITLE = "          T H E   C R E A T I V E   A R C H I T E C T"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"


def banner(color: bool) -> str:
    o, r = (ORANGE, RESET) if color else ("", "")
    lines = [f"{a}{o}{A}{r}{b}{o}{I}{r}{c}" for a, A, b, I, c in ROWS]
    return "\n".join(lines) + "\n\n" + TITLE


def want_color(argv: list[str]) -> bool:
    if "--plain" in argv or os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    return sys.stdout.isatty()


if __name__ == "__main__":
    print(banner(want_color(sys.argv[1:])))
