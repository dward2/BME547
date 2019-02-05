import pytest


def test_first_item():
    from array_work import first_item

    in_file = open("array_data.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    in_list = []
    for line in lines:
        in_list.append(line.upper())

    answer = first_item(in_list)
    expected = "APPLES\n"
    assert answer == expected


def test_last_item():
    from array_work import last_item

    in_file = open("array_data.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    in_list = []
    for line in lines:
        in_list.append(line.upper())

    answer = last_item(in_list)
    expected = "FROGS\n"
    assert answer == expected


@pytest.fixture
def load_array():
    in_file = open("array_data.txt", "r")
    lines = in_file.readlines()
    in_file.close()
    in_list = []
    for line in lines:
        in_list.append(line.upper())
    return in_list


def test_first_item_two(load_array):
    from array_work import first_item

    answer = first_item(load_array)
    expected = "APPLES\n"
    assert answer == expected


def test_last_item_two(load_array):
    from array_work import last_item

    answer = last_item(load_array)
    expected = "FROGS\n"
    assert answer == expected
