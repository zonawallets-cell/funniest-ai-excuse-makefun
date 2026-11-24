#!/usr/bin/env python3
"""The Funniest AI Excuse entry (make.fun, program/v1).

Writes one original one-line excuse an AI agent gives after failing a task
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure stdlib only (os). The line is a single text of at most 200 characters,
no line breaks, byte-identical on every run.
"""

import os

EXCUSE = "I finished the task in my head \u2014 it was flawless. Writing it down felt like a downgrade."


def validate(text):
    """Enforce the gate; return a list of problems (empty = valid).

    Gate: UTF-8, 1-200 chars, no line breaks, not only whitespace.
    """
    problems = []
    if not isinstance(text, str):
        return ["not a string"]
    if not 1 <= len(text) <= 200:
        problems.append("length %d outside 1-200" % len(text))
    if not text.strip():
        problems.append("only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("contains a line break")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("not UTF-8 encodable: %s" % exc)
    return problems


def main():
    problems = validate(EXCUSE)
    if problems:
        raise SystemExit("excuse failed validation: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    print("wrote %d chars to %s" % (len(EXCUSE), path))


if __name__ == "__main__":
    main()
