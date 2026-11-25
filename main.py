"""Funniest Autocorrect Fail entry: fold in the children gently."""

import os

FAIL = (
    "Sent Grandma a recipe: 'fold in the cheese gently.' Autocorrect "
    "delivered 'fold in the children gently.' She called me. Twice. "
    "Then she called my mother."
)

CHAR_COUNT = len(FAIL)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FAIL + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
