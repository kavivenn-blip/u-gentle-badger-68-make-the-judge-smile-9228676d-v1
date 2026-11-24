#!/usr/bin/env python3
"""Make the Judge Smile — make.fun entry.

Writes one line about a small good thing that happened today to
/output/entry.txt.

The line: "At 6:04 the night-shift nurse's note was under my locker
door — 'Your plant survived' — and below it, in smaller writing,
'So did you. Water it.'"

Why this line: it is about one small good thing that happened today
(a note left for the narrator), it leaves a glow (the note speaks to
the reader, not about them), it turns where the reader does not
expect (the note's second line reframes the first), it carries one
real small detail (6:04, a locker door, a plant), and its wording is
its own. 145 characters, one line, UTF-8, no trailing newline.
Deterministic, offline, standard library only.
"""

import os
import stat

LINE = (
    "At 6:04 the night-shift nurse's note was under my locker door "
    "\u2014 'Your plant survived' \u2014 and below it, in smaller "
    "writing, 'So did you. Water it.'"
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
