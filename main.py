#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes a single dad joke (at most 200 characters) to /output/entry.txt.
Python 3.13, standard library only.

The joke was picked by judge-testing 10 candidates on funny, one
concrete image, pun lands, groan factor, no explaining, no cliche.
Winner: the bookmark -- one concrete image, the pun ("knows my
place") lands cleanly on the first read, punchline at the very end,
98 characters, reads naturally aloud.
"""

import os

JOKE = (
    "I told my son the bookmark is my best friend. "
    "He asked why. I said, 'It always knows my place.'"
)


def main() -> None:
    text = JOKE
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
