#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of text, 1 to 240 characters, to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
"""

import os
from pathlib import Path

LINE = "At dawn the potter opened the kiln, and the glaze she had ruined nine times came out blue as deep water, whole."


def check(line: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1 to 240 characters, not only whitespace."""
    if not 1 <= len(line) <= 240:
        raise SystemExit(f"line is {len(line)} characters, must be 1 to 240")
    if not line.strip():
        raise SystemExit("line is only whitespace")
    line.encode("utf-8")


def main() -> None:
    check(LINE)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(LINE.encode("utf-8"))
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
