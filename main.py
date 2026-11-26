"""Write one word describing the whole internet to /output/entry.txt.

The competition gate requires /output/entry.txt to be UTF-8 text of
1 to 30 characters, not only white space. The entry is a single word,
written with no trailing newline.
"""

import os
import sys


WORD = "unhinged"

OUTPUT_PATH = "/output/entry.txt"

MIN_LENGTH = 1
MAX_LENGTH = 30


def validate(word):
    """Check the word against the competition gate.

    Returns a list of problems; an empty list means the word is valid.
    """
    problems = []
    if not isinstance(word, str):
        problems.append("word is not a string")
        return problems
    if len(word) < MIN_LENGTH or len(word) > MAX_LENGTH:
        problems.append(
            "word must be %d to %d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(word))
        )
    if not word.strip():
        problems.append("word must not be only white space")
    if len(word.split()) != 1:
        problems.append("entry must be exactly one word")
    return problems


def main():
    problems = validate(WORD)
    if problems:
        for problem in problems:
            print("invalid word: %s" % problem, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)

    # Read the file back and verify it byte for byte.
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    expected = WORD.encode("utf-8")
    if raw != expected:
        print(
            "verification failed: entry.txt holds %r, expected %r"
            % (raw, expected),
            file=sys.stderr,
        )
        return 1

    print("wrote %s (%d bytes)" % (OUTPUT_PATH, len(raw)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
