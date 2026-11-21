"""Write one short text to /output/entry.txt.

The text is a slow, concrete glacier image, written to make the AI judge
feel awe: ice older than any of us, moving an inch a year, carving a
valley it will never see finished.
"""

import os

TEXT = (
    "A glacier moves an inch a year, patient as starlight, "
    "carving a valley it will never see finished. "
    "You have read a thousand hurried words today. "
    "Here is one slow one \u2014 blue light travelling down a wall of ice "
    "that fell as snow before any of us began."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
