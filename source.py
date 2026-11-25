#!/usr/bin/env python3
"""Write the one-line office joke entry for make.fun.

The bounty asks for a single original joke about office life, at most
200 characters, that reads as one line: a setup with a surprise payoff
anyone who has sat in an office recognises. This program writes exactly
that line, and nothing else, to ``entry.txt`` inside the output
directory.

Standard library only, no network, and the same bytes on every run.
"""

import os
from pathlib import Path

LINE = "I finally got a standing desk so I could stand up for myself at work, but HR just sent a lumbar-support chair and a form to fill in about it."


def entry_path() -> Path:
    """Where the line goes: $MAKEFUN_OUTPUT_DIR, otherwise /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    # The gate wants 1-200 Unicode characters: refuse to write an entry
    # outside that range instead of failing quietly. One sentence only:
    # a single line, no line breaks inside it.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    path = entry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
