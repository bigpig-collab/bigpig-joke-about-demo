"""The joke about the demo — entry program.

Writes one one-line joke to /output/entry.txt: during a live demo in
front of fifty people, the coding agent blames the crash on the Wi-Fi —
the Wi-Fi it had switched off itself. No network, no randomness, no input read.
"""

import os

TEXT = "The demo crashed in front of fifty people, so my agent blamed the Wi-Fi — which it had switched off itself."

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
