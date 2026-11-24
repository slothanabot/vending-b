#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: the machine tells the human not to shake it, to press B7
instead, and promises to fall for them all on its own -- the snack
dropping from its coil, and the machine falling in love, in one turn.
The punch lands in the last few words, and the whole line is the
machine speaking in its own world: shaking, buttons, coils, falling stock.
"""

import os
import sys

MAX_CHARS = 200
MIN_CHARS = 1
TERMINAL_PUNCTUATION = ".!?"


def build_line():
    """Return the vending machine's pickup line (one line, one breath)."""
    return "Don't shake me, sweetheart \u2014 just press B7 and I'll fall for you all on my own."


def validate(line):
    """Check the kit gate: 1-200 chars, single line, not blank,
    printable, ending in terminal punctuation. Returns (ok, reason)."""
    if not isinstance(line, str):
        return False, "not a string"
    if line.strip() == "":
        return False, "blank"
    if line != line.strip():
        return False, "leading or trailing whitespace"
    if "\n" in line or "\r" in line:
        return False, "not a single line"
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        return False, f"length {len(line)} outside 1-200"
    if not line.isprintable():
        return False, "not printable"
    if line[-1] not in TERMINAL_PUNCTUATION:
        return False, "no terminal punctuation"
    return True, "ok"


def write_entry(output_dir=None):
    """Validate the line and write it to <output_dir>/entry.txt."""
    line = build_line()
    ok, reason = validate(line)
    if not ok:
        raise ValueError(f"invalid line: {reason}: {line!r}")
    out_dir = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path, line


def main():
    path, line = write_entry()
    print(f"wrote {len(line)} chars to {path}")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
