import difflib
from typing import Tuple


def diff_files(source: str, target: str) -> Tuple[int, int]:
    diff = difflib.ndiff(source.splitlines(), target.splitlines())
    add_count = 0
    delete_count = 0
    for line in diff:
        if line.startswith("+"):
            add_count += 1
        elif line.startswith("-"):
            delete_count += 1
    return (add_count, delete_count)

# Examples
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana\nMango'))
print(diff_files('Apple\nOrange\nPear', 'Apple\nPear\nBanana'))