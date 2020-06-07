from problems.cracking_the_code_interview.is_unique import (
    is_unique,
    is_unique_with_no_extra_space,
)


def test_all_chars_are_unique():
    assert is_unique("a")
    assert is_unique("abcde")


def test_has_repeated_chars():
    assert not is_unique("aa")
    assert not is_unique("abccde")


def test_has_only_unique_chars_with_no_extra_space():
    assert is_unique_with_no_extra_space("a")
    assert is_unique_with_no_extra_space("abc")
    assert is_unique_with_no_extra_space("abcd")
    assert is_unique_with_no_extra_space("abcde")


def test_has_repeated_chars_with_no_extra_space():
    assert not is_unique_with_no_extra_space("aa")
    assert not is_unique_with_no_extra_space("aac")
    assert not is_unique_with_no_extra_space("abccde")
    assert not is_unique_with_no_extra_space("caa")
