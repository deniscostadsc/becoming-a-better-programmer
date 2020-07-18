import pytest

from datastructures import SortedLinkedList


@pytest.fixture
def sorted_linked_list():
    return SortedLinkedList()


def test_sorted_linked_list_size_is_initially_zero(sorted_linked_list):
    assert len(sorted_linked_list) == 0


def test_insert_item_to_sorted_linked_list(sorted_linked_list):
    sorted_linked_list.insert(1)

    assert len(sorted_linked_list) == 1
    assert pytest.helpers.equal_items([1], sorted_linked_list)


def test_insert_items_to_sorted_linked_list(sorted_linked_list):
    sorted_linked_list.insert(1)
    sorted_linked_list.insert(2)
    sorted_linked_list.insert(3)

    assert len(sorted_linked_list) == 3
    assert pytest.helpers.equal_items([1, 2, 3], sorted_linked_list)


def test_insert_reservely_sorted_items_to_sorted_linked_list(
    sorted_linked_list,
):
    sorted_linked_list.insert(3)
    sorted_linked_list.insert(2)
    sorted_linked_list.insert(1)

    assert len(sorted_linked_list) == 3
    assert pytest.helpers.equal_items([1, 2, 3], sorted_linked_list)


def test_insert_unsorted_items_to_sorted_linked_list(sorted_linked_list,):
    sorted_linked_list.insert(1)
    sorted_linked_list.insert(3)
    sorted_linked_list.insert(2)

    assert len(sorted_linked_list) == 3
    assert pytest.helpers.equal_items([1, 2, 3], sorted_linked_list)


def test_remove_item_from_sorted_linked_list(sorted_linked_list):
    sorted_linked_list.insert(1)
    sorted_linked_list.insert(3)
    sorted_linked_list.insert(2)

    assert len(sorted_linked_list) == 3
    assert pytest.helpers.equal_items([1, 2, 3], sorted_linked_list)

    sorted_linked_list.remove(0)

    assert len(sorted_linked_list) == 2
    assert pytest.helpers.equal_items([2, 3], sorted_linked_list)
