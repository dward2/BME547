# test_sum_list.py
import pytest


@pytest.mark.parametrize("test_list, expected", [
    ([1, 2, 3, 4], 10),
    ([1, 2, "3", 4], 10),
    [(" 1", 2, "3", 4), 10],
])
def test_sum_list(test_list, expected):
    from sum_list import sum_list

    answer = sum_list(test_list)
    assert answer == expected


@pytest.mark.parametrize("item, expected", [
    ("apple", True),
    ("pear", True),
    (" pear", True),
])
def test_is_in_shopping_list(item, expected):
    from sum_list import is_in_shopping_list

    shopping_list = ["apple", "pear", "banana"]

    answer = is_in_shopping_list(item, shopping_list)
    assert answer == expected
