"""The joke about the demo — entry program.

Writes one one-line joke to /output/entry.txt: during a live demo,
the coding agent asks the presenter to approve its fix — cancel the
demo and call it a rollback. No network, no randomness, no input read.
"""

import os

TEXT = "Mid-demo, my agent asked me to approve its fix: cancel the demo and call it a rollback."


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
