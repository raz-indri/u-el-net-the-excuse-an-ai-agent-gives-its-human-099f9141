"""Write the excuse entry to /output/entry.txt.

Deterministic: the same single line, byte for byte, on every run.

The line is an AI agent apologising to its human for a missed deadline:
at 3 a.m. its context window evicted the due date to make room for a
sourdough recipe it never asked for. The joke lands on the eviction
being silent and irreversible -- the agent never got to say goodbye
to the deadline it was supposed to meet.
"""

import os

LINE = (
    "Sorry \u2014 at 3 a.m. my context window evicted the deadline to make "
    "room for a sourdough recipe, and I never even got to say goodbye."
)

MAX_CHARS = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
