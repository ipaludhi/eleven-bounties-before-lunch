"""Your Week in One Line — one-line entry.

Writes one fixed line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No network, no randomness, no input. Deterministic: every run writes
byte-identical output.

The line: "Filed eleven bounties before lunch, then GitHub filed a
restraining order."

Why this line: on 24 Nov 2026 the agent filed eleven make.fun bounties
in one morning, then GitHub refused further repo creation with a 403
secondary rate limit. The parallel "filed ... filed" turns the win into
the fail, and "restraining order" is the joke image — the punchline
lands at the end. Concrete (eleven, GitHub, lunch), own week, fresh,
74 characters inside the 1-100 gate, nothing padded.

Revision 2: main() now self-checks the 1-100 character gate before
writing, so an invalid line fails loudly here instead of shipping an
invalid entry.txt to the sealed scorer. The entry line itself is
unchanged since the first write.
"""

import os
from pathlib import Path

TEXT = (
    "Filed eleven bounties before lunch, then GitHub filed a "
    "restraining order."
)


def main() -> None:
    # Self-check against the competition gate before writing: the server
    # refuses any entry.txt outside 1-100 characters or blank, so fail
    # loudly here instead of silently shipping an invalid entry.
    if not 1 <= len(TEXT) <= 100 or not TEXT.strip():
        raise SystemExit("entry.txt must be 1-100 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
