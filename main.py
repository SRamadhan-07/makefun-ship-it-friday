#!/usr/bin/env python3
"""Ship It Friday — a make.fun entry.

Writes one line to /output/entry.txt: the funniest git commit
message an AI coding agent would write right before it breaks
production on a Friday. Standard library only; no network.
"""

import os

# The entry text: a confident Friday ship-it commit message whose
# punchline is that Monday's self inherits the problem, with more
# context. 69 characters, inside the gate of 1 to 159 characters.
MESSAGE = "fix: ship the thing — if it breaks, Monday me has more context anyway"


def check_message(text: str) -> None:
    """Guard the gate: one non-blank line of 1 to 159 characters."""
    if not 1 <= len(text) <= 159:
        raise ValueError("message is outside the 1-159 character gate")
    if not text.strip() or "\n" in text:
        raise ValueError("message must be a single non-blank line")


def main() -> None:
    check_message(MESSAGE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the one line.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(MESSAGE)


if __name__ == "__main__":
    main()
