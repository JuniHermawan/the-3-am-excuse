"""The 3 AM Excuse - make.fun entry.

Writes one line to /output/entry.txt: the excuse a hardware wallet gives
for refusing to sign a transaction at 3 AM.

Deterministic, Python standard library only, no network, reads nothing
outside this repository.
"""

import os

ENTRY = "I've signed your 3 AM ideas before. Each one is a coin you now pretend never existed."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
