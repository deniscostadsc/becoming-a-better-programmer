from typing import Dict


"""
Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""


def has_unique_char(s: str) -> bool:
    """
    Time: O(n)
    Space: O(c)

    "c" being the number of unique characters in the string
    """
    chars: Dict[str, int] = {}

    for char in s:
        if char in chars:
            return False
        else:
            chars[char] = 1

    return True


def has_unique_char_with_no_additional_datastructures(s: str) -> bool:
    """
    Time: O(n log n)
    Space: O(1)
    """

    if len(s) == 1:
        return True

    s = "".join(sorted(s))

    for char in s:
        begin = 0
        end = len(s) - 1

        while begin < end:
            middle = begin + ((end - begin) // 2)
            if s[middle] == char:
                if middle >= 1 and s[middle - 1] == char:
                    return False
                if middle <= len(s) - 2 and s[middle + 1] == char:
                    return False
                break
            elif s[middle] > char:
                begin = middle + 1
            else:
                end = middle - 1

    return True


__all__ = [
    "has_unique_char",
    "has_unique_char_with_no_additional_datastructures",
]
