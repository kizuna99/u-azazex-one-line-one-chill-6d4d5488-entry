# SPDX-License-Identifier: MIT
"""One Line, One Chill — writes the single horror line to /output/entry.txt."""
import os

# The winning line: a single sentence, under the 200-character gate, whose
# final word is the threat itself. Kept as one literal so the output bytes
# are identical on every run.
LINE = "Mission control played back my own voice from the Moon, recorded an hour before I landed, begging them not to let me back inside."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(LINE)
    except OSError:
        fallback = os.path.join(os.getcwd(), "output")
        os.makedirs(fallback, exist_ok=True)
        with open(os.path.join(fallback, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
            fh.write(LINE)


if __name__ == "__main__":
    main()
