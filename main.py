#!/usr/bin/env python3
"""The One-Line Exit - make.fun bounty entry.

Writes one funny one-line resignation letter to entry.txt.
Stdlib only, deterministic, no network access.
"""

import os
import sys

MAX_CHARS = 140

LINE = "I resign: after six years, the only thing this company ever promoted was my blood pressure."


def validate(text):
    """Check the entry against the competition gate.

    The gate wants UTF-8 text of 1 to 140 characters, not only
    whitespace, on exactly one line. Anything else is never judged.
    """
    if not text or not text.strip():
        raise ValueError("entry is blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 32 and ch not in "\t" for ch in text):
        raise ValueError("entry contains a control character")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = validate(LINE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # Self-check: read back what we wrote and confirm it is the same line.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written.strip() != text:
        raise ValueError("entry.txt does not match the validated line")
    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
