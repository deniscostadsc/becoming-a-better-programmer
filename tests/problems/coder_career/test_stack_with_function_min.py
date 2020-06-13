import pytest

from problems.coder_career.stack_with_function_min import Stack


@pytest.fixture
def stack():
    return Stack()


def test_stack_with_function_min(stack):
    stack.push(1)
    assert stack.min() == 1
    assert stack.pop() == 1


def test_min_function_really_works(stack):
    stack.push(3)
    assert stack.min() == 3
    stack.push(2)
    assert stack.min() == 2
    stack.push(1)
    assert stack.min() == 1
    stack.push(9)
    assert stack.min() == 1
    stack.push(1)
    assert stack.min() == 1


def test_min_stack_raises_exception(stack):
    with pytest.raises(IndexError) as e:
        stack.pop()
    assert str(e.value) == "pop from empty list"

    with pytest.raises(IndexError) as e:
        stack.min()
    assert str(e.value) == "min from empty list"
