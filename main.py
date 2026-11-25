#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Word for the Boss — make.fun bounty entry.

Writes exactly one word (13 characters, under the 30-character limit)
describing a boss to /output/entry.txt. No trailing newline, no extra
whitespace: the file contains the word and nothing else.
"""

import os

ENTRY = "Micromanager"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
