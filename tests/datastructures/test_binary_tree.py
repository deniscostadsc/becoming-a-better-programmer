import pytest

from datastructures import BinaryTree


@pytest.fixture
def binary_tree():
    return BinaryTree()


def test_binary_tree_is_initially_zero(binary_tree):
    assert len(binary_tree) == 0


def test_add_item_to_binary_tree(binary_tree):
    binary_tree.add(1)
    assert len(binary_tree) == 1
