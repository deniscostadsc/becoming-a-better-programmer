from typing import Dict


def has_unique_char(s: str) -> bool:
    """
    Time: O(n)
    Space: O(c)

    "c" being the number of unique characters in the string
    """
    chars: Dict[str, int] = {}

    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return 1 in chars.values()


__all__ = [
    "has_unique_char",
]
