#!/usr/bin/env python3
"""Ship It Friday — make.fun entry (u-mgwals-ship-it-friday-30bd407a).

Writes one line to /output/entry.txt: the funniest git commit message
an AI coding agent would write right before breaking production on a
Friday. Standard library only (Python 3.13 sandbox installs nothing).
"""

import os

ENTRY = (
    "feat: approved my own PR, merged it myself, deploying Friday 4:59pm"
    " - code review was the bottleneck, ship it"
)


def main():
    text = ENTRY.strip()
    # Gate mirror: /output/entry.txt must be UTF-8 text of 1-159 chars,
    # not only whitespace, and a single line.
    assert 1 <= len(text) <= 159, f"entry is {len(text)} chars, must be 1-159"
    assert text.strip() == text and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
