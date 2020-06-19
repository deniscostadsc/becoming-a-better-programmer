from typing import List, Optional

"""
If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string
can generate. Give a count as well as print the strings.

For example:

Input: "1123". You need to general all valid alphabet codes from this string.

Output:

aabc  // a = 1, a = 1, b = 2, c = 3
kbc  // k = 11, b = 2, c= 3
alc  // a = 1, l = 12, c = 3
aaw  // a= 1, a =1, w= 23
kw  // k = 11, w = 23

https://www.careercup.com/question?id=19300678
"""


indexed_letter = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
}


def _all_possible_letters(
    str_number: str,
    result: List[str],
    index: int = 0,
    parent_prefix: Optional[str] = None,
) -> None:
    """
    Time: O(2^n)
    Space: O(1)

    TODO: it's possible o write a O(n) solution with dynamic programming.
    """
    if index == len(str_number):
        return

    if parent_prefix is None:
        parent_prefix = ""

    first_letter = indexed_letter[int(str_number[index])]
    second_letter = None
    if index < len(str_number) - 1:
        second_letter = indexed_letter[int(str_number[index : index + 2])]

    try:
        letter_set_index = result.index(parent_prefix)
        result[letter_set_index] += first_letter
        if second_letter:
            result.append(parent_prefix + second_letter)
    except ValueError:
        result.append(first_letter)
        if second_letter:
            result.append(second_letter)

    _all_possible_letters(
        str_number, result, index + 1, parent_prefix + first_letter
    )
    if second_letter:
        _all_possible_letters(
            str_number, result, index + 2, parent_prefix + second_letter
        )


def all_possible_letters(number: int) -> List[str]:
    result: List[str] = []
    _all_possible_letters(str(number), result)
    result.sort()

    return result


__all__ = [
    "all_possible_letters",
]
