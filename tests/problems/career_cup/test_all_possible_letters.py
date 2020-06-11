from problems.career_cup.all_possible_letters import all_possible_letters


def test_all_possible_letter():
    assert all_possible_letters(1) == ["a"]
    assert all_possible_letters(2) == ["b"]
    assert all_possible_letters(3) == ["c"]
    assert all_possible_letters(11) == ["aa", "k"]
    assert all_possible_letters(12) == ["ab", "l"]
    assert all_possible_letters(1123) == ["aabc", "aaw", "alc", "kbc", "kw"]
