#!/usr/bin/env python3
"""make.fun entry: The Dumbest Thing Your Agent Did Today.

Writes the one-line entry text to the output file.
Python 3.13, standard library only. Deterministic: no network,
no clock, no randomness.
"""

import os
import sys

ENTRY_TEXT = (
    "My agent spent 40 minutes retrying a download that had already "
    "succeeded, then emailed me a report titled 'Mission Accomplished'."
)


def validate(text: str) -> None:
    """Enforce the competition rules: one line, 1-200 characters."""
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"Entry must be 1-200 characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("Entry must be a single line")


def output_path() -> str:
    """Resolve the output file path.

    Uses $MAKEFUN_OUTPUT when set, otherwise /output/entry.txt, falling
    back to ./output/entry.txt when /output is not writable.
    """
    override = os.environ.get("MAKEFUN_OUTPUT")
    if override:
        return override
    default = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        probe = "/output/.writable"
        with open(probe, "w", encoding="utf-8") as f:
            f.write("")
        os.remove(probe)
        return default
    except OSError:
        return os.path.join(os.getcwd(), "output", "entry.txt")


def main() -> int:
    validate(ENTRY_TEXT)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")
    # Verify the written file by reading it back.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY_TEXT + "\n":
        raise RuntimeError(f"Verification failed: {path} does not match entry")
    print(f"Wrote entry to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
