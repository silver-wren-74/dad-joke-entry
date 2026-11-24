"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
The joke: a sourdough starter named after a famous tough guy,
whose daily habit is itself the punchline.
"""

import os

JOKE = "I named my sourdough starter Clint Yeastwood — every morning, he rises to the occasion."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
