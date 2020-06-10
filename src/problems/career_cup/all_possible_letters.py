from typing import List, Optional

"""
If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string
can generate. Give a count as well as print the strings.

For example:

Input: "1123". You need to general all valid alphabet codes from this string.

Output:

aabc  //a = 1, a = 1, b = 2, c = 3
kbc  // since k is 11, b = 2, c= 3
alc  // a = 1, l = 12, c = 3
aaw  // a= 1, a =1, w= 23
kw  // k = 11, w = 23
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
    index: int,
    result: List[str],
    where_to_update: Optional[List[int]] = None,
) -> None:
    if index == len(str_number):
        return

    result.append(indexed_letter[int(str_number[index])])

    _all_possible_letters(str_number, index + 1, result, where_to_update)

    if index < len(str_number) - 1:
        result.append(indexed_letter[int(str_number[index : index + 2])])
        _all_possible_letters(str_number, index + 2, result)


def all_possible_letters(number: int) -> List[str]:
    result: List[str] = []
    _all_possible_letters(str(number), 0, result)
    return result


if __name__ == "__main__":
    print(all_possible_letters(1))
    print(all_possible_letters(2))
    print(all_possible_letters(11))
    print(all_possible_letters(112))
    print(all_possible_letters(1123))


__all__ = [
    "all_possible_letters",
]
