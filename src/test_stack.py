# -*- coding: utf-8 -*-
"""Testing module for the Doubly Linked List and Node classes."""

from stack import Stack
import pytest


# ------------------Stack Initialization Tests--------------------
# [] test default initialization.

def test_stack_initalization():
    """Test default initialization."""
    stack = Stack()
    assert isinstance(stack, Stack)

# ------------------Enstack Method Tests--------------------
# [] push(val), check first_node = val
# [] push(val),push(val2), check first_node = val2
# [] push(val), push(val2) check last_node = val1.

def test_push_val():
    """push(val), check first_node = val."""
    stack = Stack()
    anode = stack.push('a')
    assert stack._stack.first_node is anode


def test_push_enstack_check_first_node_val():
    """push(val), push(val2) check first_node = val2."""
    stack = Stack()
    anode = stack.push('a')
    bnode = stack.push('b')
    assert stack._stack.first_node is bnode


def test_push_enstack_check_last_node_val():
    """push(val), push(val2) check last_node = val1."""
    stack = Stack()
    anode = stack.push('a')
    bnode = stack.push('b')
    assert stack._stack.last_node is anode


# -------------stack Initialization Tests by itterable---------------
# [] initialize empty, first node is None.
# [] initialize empty, last node is None.
# [] initialize one charicter itterable, first node is val.
# [] initialize two charicter itterable, first node is first char.
# [] initialize two charicter itterable, last node is second char.

def test_initialization_with_empty_list_first_node_check():
    """Initialize empty, first node is None."""
    stack = Stack([])
    assert stack._stack.first_node is None


def test_initialization_with_empty_list_last_node_check():
    """Initialize empty, last node is None."""
    stack = Stack([])
    assert stack._stack.last_node is None


def test_initialization_with_list_first_node_val():
    """Initialize one charicter itterable, first node is val."""
    stack = Stack('a')
    assert stack._stack.first_node == 'a'


def test_initialization_with_two_items_first_node_val():
    """Initialize two charicter itterable, first node is last char."""
    stack = Stack('ab')
    assert stack._stack.first_node == 'b'


def test_initialization_with_two_items_last_node_val():
    """Initialize two charicter itterable, last node is first char."""
    stack = Stack('ab')
    assert stack._stack.last_node == 'a'

# ------------------Pop Method Tests--------------------
# [] push(val), pop = val
# [] push(val), pop = val, node is removed(last_node is None)
# [] push(val),push(val2), pop = val
# [] push(val),push(val2), pop = val, pop = val2
# [] pop raises error
# [] push(val), pop = val, pop raises error


def test_pop_returns_value():
    """push(val), pop = val."""
    stack = Stack()
    stack.push('a')
    assert stack.pop() is 'a'


def test_pop_removes_value():
    """push(val), pop = val, mode is removed(last_node is None)."""
    stack = Stack()
    stack.push('a')
    stack.pop()
    assert stack._stack.last_node is None
    assert stack._stack.first_node is None


def test_values_pop_in_correct_order():
    """push(val),push(val2), pop = val2."""
    stack = Stack('ab')
    assert stack.pop() == 'b'


def test_values_pop_two_values_in_correct_order():
    """push(val),push(val2), pop = val2, pop = val."""
    stack = Stack('ab')
    assert stack.pop() == 'b'
    assert stack.pop() == 'a'


def test_pop_empty_list_raises_error():
    """Dstack raises error."""
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_stack_pop_pop_raises_error():
    """push(val), pop = val, pop raises error."""
    stack = Stack('a')
    stack.pop()
    with pytest.raises(IndexError):
        stack.pop()


# ------------------Peak Method Tests--------------------
# [] push(val), peak = val
# [] push(val), peak = val, node not removed(last_node is val)
# [] push(val),push(val2), peak = val
# [] peak empty returns none

def test_peak_returns_value():
    """push(val), peak = val."""
    stack = Stack('a')
    assert stack.peak() is 'a'


def test_peak_returns_value_does_not_pop():
    """push(val), peak = val, node not removed(last_node is val)."""
    stack = Stack('a')
    a = stack.peak()
    assert stack._stack.first_node == 'a'


def test_peak_returns_correct_value():
    """push(val),push(val2), peak = val."""
    stack = Stack()
    stack.push('a')
    stack.push('b')
    assert stack.peak() is 'b'


def test_peak_empty_stack_returns_none():
    """Peak empty returns none."""
    stack = Stack()
    assert stack.peak() is None


# -------------Size Method Tests------------------
# [] size of new stack is 0.
# [] enstack, size is 1.
# [] enstack, pop size is 0.
# [] enstack, peak size is 1.
# [] dequeu, size of dll is 0.


def test_size_of_new_stack():
    """Size of new stack is 0."""
    stack = Stack()
    assert stack.size() == 0


def test_size_increments_with_push():
    """Enstack, size is 1."""
    stack = Stack()
    stack.push('val')
    assert stack.size() == 1


def test_size_decrements_with_pop():
    """Enstack, pop size is 0."""
    stack = Stack()
    stack.push('val')
    assert stack.size() == 1
    stack.pop()
    assert stack.size() == 0


def test_size_stays_same_with_peak():
    """Enstack, peak size is 1."""
    stack = Stack()
    stack.push('val')
    assert stack.size() == 1
    stack.peak()
    assert stack.size() == 1


def test_size_stays_with_pop_error():
    """Dequeu, size of dll is 0."""
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
    assert stack.size() == 0

