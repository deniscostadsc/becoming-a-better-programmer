import pytest

from datastructures import EmptyHeap, MinHeap


@pytest.helpers.register
def equal_items(expected, actual):
    return len(expected) == len(actual) and all(
        map(lambda x: x[0] == x[1], zip(actual, expected))
    )


@pytest.fixture
def heap():
    return MinHeap()


def test_heap_size_is_initially_zero(heap):
    assert len(heap) == 0


def test_push_item_to_heap(heap):
    heap.push(1)
    assert len(heap) == 1


def test_push_item_that_should_be_replaced(heap):
    heap.push(2)
    heap.push(3)
    heap.push(4)
    heap.push(1)
    assert heap.peek() == 1
    assert pytest.helpers.equal_items([1, 2, 4, 3], heap)


def test_heap_peek(heap):
    heap.push(1)
    assert heap.peek() == 1
    assert pytest.helpers.equal_items([1], heap)


def test_peek_empty_heap(heap):
    with pytest.raises(EmptyHeap) as e:
        heap.peek()
    assert str(e.value) == "you cannot peek on empty heap"


def test_heap_pop(heap):
    heap.push(3)
    assert pytest.helpers.equal_items([3], heap)
    assert len(heap) == 1
    assert heap.pop() == 3
    assert len(heap) == 0
    assert pytest.helpers.equal_items([], heap)


def test_pop_empty_heap(heap):
    with pytest.raises(EmptyHeap) as e:
        heap.pop()
    assert str(e.value) == "you cannot pop on empty heap"


def test_pop_item_and_check_heap_reorganization(heap):
    heap.push(10)
    heap.push(20)
    heap.push(15)
    heap.push(17)
    assert pytest.helpers.equal_items([10, 17, 15, 20], heap)
    assert heap.pop() == 10
    assert len(heap) == 3
    assert heap.peek() == 15
    assert pytest.helpers.equal_items([15, 17, 20], heap)


def test_pop_item_and_reorganize_and_should_stop_in_the_middle(heap):
    heap.push(10)
    heap.push(15)
    heap.push(20)
    heap.push(17)
    heap.push(16)
    assert pytest.helpers.equal_items([10, 15, 20, 17, 16], heap)
    assert heap.pop() == 10
    assert len(heap) == 4
    assert heap.peek() == 15
    assert pytest.helpers.equal_items([15, 16, 20, 17], heap)
