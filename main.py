#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry (program/v1).

Writes a single sentence (1-200 characters) about the best meal ever had
to /output/entry.txt, as the competition gate requires.
Pure Python standard library only.
"""

import os

ENTRY = (
    "At 2 a.m. on a rain-slick street in Jakarta, a cart vendor handed me "
    "sate ayam still hissing off the charcoal, peanut sauce dripping down "
    "my wrist, and I ate it standing there, grinning, in the dark."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
