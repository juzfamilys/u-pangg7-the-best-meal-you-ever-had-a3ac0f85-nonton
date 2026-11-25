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


def validate_entry() -> str:
    """Re-read entry.txt from disk and re-validate the gate.

    Reads raw bytes, decodes as strict UTF-8, compares the contents
    exactly against the expected entry, and re-checks the gate:
    1-200 characters, single line, non-whitespace.
    """
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises UnicodeDecodeError if not valid UTF-8
    assert text == ENTRY.strip(), "entry.txt on disk differs from expected entry"
    assert text.strip(), "entry must not be empty or whitespace-only"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    return text


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    checked = validate_entry()
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH} (validated: {len(checked)} chars)")


if __name__ == "__main__":
    main()
