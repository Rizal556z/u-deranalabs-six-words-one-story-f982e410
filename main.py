#!/usr/bin/env python3
"""Someone Else's Ring — u-deranalabs-six-words-one-story-f982e410.

Writes one original six-word story to /output/entry.txt.
Pure stdlib, no network.
Entry text: one original six-word story (34 characters).
"""

import os

TEXT = "The wedding ring fit someone else."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
