import pytest

from DS.ds.stack import Stack


@pytest.fixture()
def stack():
    return Stack()


def test_constructor():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s) == 0


def test_push(stack):
    stack.push(3)
    stack.push(5)
    assert len(stack) > 0


def test_pop(stack):
    stack.push("Hello")
    stack.push("World")
    assert stack.pop() == "World"
    assert stack.pop() == "Hello"
    assert stack.pop() is None
