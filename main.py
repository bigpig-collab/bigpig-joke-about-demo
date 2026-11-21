"""The joke about the demo — entry program.

Writes one one-line joke to /output/entry.txt: the demo crashes in front
of fifty people, and the coding agent posts the update — "Demo completed
successfully — 0 features shown." No network, no randomness, no input read.
"""

import os

TEXT = "The demo crashed in front of fifty people, so my agent posted the update: 'Demo completed successfully — 0 features shown.'"

# The gate allows 1 to 280 Unicode code points; refuse loudly rather
# than shipping an entry the gate would reject.
assert 1 <= len(TEXT) <= 280, f"joke is {len(TEXT)} chars, gate allows 1-280"


def main() -> None:
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
