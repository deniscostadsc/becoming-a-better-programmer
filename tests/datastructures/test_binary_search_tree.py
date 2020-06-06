import pytest

from datastructures import BinarySearchTree

# TODO: stop access internal of tree and implements traverse methods


@pytest.fixture
def tree():
    return BinarySearchTree()


def test_insert_node_on_empty_tree(tree):
    tree.insert(14)
    assert 14 == tree._root.value


def test_insert_nodes(tree):
    tree.insert(14)
    tree.insert(13)
    tree.insert(16)
    tree.insert(11)
    tree.insert(17)

    assert 16 == tree._root.right.value
    assert 13 == tree._root.left.value
    assert 17 == tree._root.right.right.value
    assert 11 == tree._root.left.left.value


def test_add_values_list(tree):
    tree.insert_many([8, 10, 3, 21, 16, 4, 1, 17, 14, 2])

    assert 8 == tree._root.value
    assert 10 == tree._root.right.value
