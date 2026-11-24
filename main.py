"""Ship It Friday entry: one commit message, written to entry.txt."""

import os

ENTRY = "fix: delete the database, it was mostly old data anyway — happy Friday, what could go wrong?"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
