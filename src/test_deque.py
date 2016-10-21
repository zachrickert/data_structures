# -*- coding: utf-8 -*-
"""Testing module for the Doubly Linked List and Node classes."""

from deque import Deque
import pytest


# ------------------Deque Initialization Tests--------------------
# [] test default initialization.

def test_deque_initalization():
    """Test default initialization."""
    deque = Deque()
    assert isinstance(deque, Deque)

# ------------------Append_left Method Tests--------------------
# [x] append_left(val), check first_node = val
# [x] append_left(val),append_left(val2), check first_node = val2
# [x] append_left(val), append_left(val2) check first_node.forward = val1.

def test_append_left_val():
    """append_left(val), check first_node = val."""
    deque = Deque()
    anode = deque.append_left('a')
    assert deque._deque.first_node is anode


def test_append_left_check_first_node_val():
    """append_left(val), append_left(val2) check first_node = val2."""
    deque = Deque()
    anode = deque.append_left('a')
    bnode = deque.append_left('b')
    assert deque._deque.first_node is bnode


def test_append_left_check_first_node_forward_val():
    """append_left(val), append_left(val2) check first_node.forward = val1."""
    deque = Deque()
    anode = deque.append_left('a')
    bnode = deque.append_left('b')
    assert deque._deque.first_node.forward is anode


# ------------------Append Method Tests--------------------
# [x] append(val), check last_node = val
# [x] append(val),append(val2), check last_node = val1
# [x] append(val), append(val2) check last_node.backward = val2.

def test_append_val():
    """append(val), check last_node = val."""
    deque = Deque()
    anode = deque.append('a')
    assert deque._deque.last_node is anode


def test_append_check_first_node_val():
    """append(val), append(val2) check last_node = val2."""
    deque = Deque()
    anode = deque.append('a')
    bnode = deque.append('b')
    assert deque._deque.last_node is bnode


def test_append_check_first_node_forward_val():
    """append(val), append(val2) check first_node.forward = val1."""
    deque = Deque()
    anode = deque.append('a')
    bnode = deque.append('b')
    assert deque._deque.last_node.backward is anode


# -------------deque Initialization Tests by itterable---------------
# [x] initialize empty, first node is None.
# [x] initialize empty, last node is None.
# [x] initialize one charicter itterable, first node is val.
# [x] initialize two charicter itterable, first node is first char.
# [x] initialize two charicter itterable, last node is second char.

def test_initialization_with_empty_list_first_node_check():
    """Initialize empty, first node is None."""
    deque = Deque([])
    assert deque._deque.first_node is None


def test_initialization_with_empty_list_last_node_check():
    """Initialize empty, last node is None."""
    deque = Deque([])
    assert deque._deque.last_node is None


def test_initialization_with_list_first_node_val():
    """Initialize one charicter itterable, first node is val."""
    deque = Deque('a')
    assert deque._deque.first_node == 'a'


def test_initialization_with_two_items_first_node_val():
    """Initialize two charicter itterable, first node is last char."""
    deque = Deque('ab')
    assert deque._deque.first_node == 'a'


def test_initialization_with_two_items_last_node_val():
    """Initialize two charicter itterable, last node is first char."""
    deque = Deque('ab')
    assert deque._deque.last_node == 'b'

# ------------------Pop_left Method Tests--------------------
# [x] append_left(val), pop_left = val
# [x] append_left(val), pop_left = val, node is removed(last_node is None)
# [x] append_left(val),append_left(val2), pop_left = val
# [x] append_left(val),append_left(val2), pop_left = val, pop_left = val2
# [x] pop_left raises error
# [x] append_left(val), pop_left = val, pop_left raises error


def test_pop_left_returns_value():
    """Append_left(val), pop_left = val."""
    deque = Deque()
    deque.append_left('a')
    assert deque.pop_left() is 'a'


def test_pop_left_removes_value():
    """Append_left(val), pop_left = val, mode is removed(last_node is None)."""
    deque = Deque()
    deque.append_left('a')
    deque.pop_left()
    assert deque._deque.last_node is None
    assert deque._deque.first_node is None


def test_values_pop_left_in_correct_order():
    """Append_left(val),append_left(val2), pop_left = val2."""
    deque = Deque('ab')
    assert deque.pop_left() == 'a'


def test_values_pop_left_two_values_in_correct_order():
    """Append_left(val),append_left(val2), pop_left = val2, pop_left = val."""
    deque = Deque('ab')
    assert deque.pop_left() == 'a'
    assert deque.pop_left() == 'b'


def test_pop_left_empty_list_raises_error():
    """pop_left raises error."""
    deque = Deque()
    with pytest.raises(IndexError):
        deque.pop_left()


def test_deque_pop_left_pop_left_raises_error():
    """append_left(val), pop_left = val, pop_left raises error."""
    deque = Deque('a')
    deque.pop_left()
    with pytest.raises(IndexError):
        deque.pop_left()



# ------------------pop Method Tests--------------------
# [x] append(val), pop = val
# [x] append(val), pop = val, node is removed(last_node is None)
# [x] append(val),append(val2), pop = val
# [x] append(val),append(val2), pop = val, pop = val2
# [x] pop raises error
# [x] append(val), pop = val, pop raises error


def test_pop_returns_value():
    """append(val), pop = val."""
    deque = Deque()
    deque.append('a')
    assert deque.pop() is 'a'


def test_pop_removes_value():
    """append(val), pop = val, mode is removed(last_node is None)."""
    deque = Deque()
    deque.append('a')
    deque.pop()
    assert deque._deque.last_node is None
    assert deque._deque.first_node is None


def test_values_pop_in_correct_order():
    """append(val),append(val2), pop = val2."""
    deque = Deque('ab')
    assert deque.pop() == 'b'


def test_values_pop_two_values_in_correct_order():
    """append(val),append(val2), pop = val2, pop = val."""
    deque = Deque('ab')
    assert deque.pop() == 'b'
    assert deque.pop() == 'a'


def test_pop_empty_list_raises_error():
    """pop raises error."""
    deque = Deque()
    with pytest.raises(IndexError):
        deque.pop()


def test_deque_pop_pop_raises_error():
    """append(val), pop = val, pop raises error."""
    deque = Deque('a')
    deque.pop()
    with pytest.raises(IndexError):
        deque.pop()


# ------------------Peak Method Tests--------------------
# [x] append_left(val), peak = val
# [x] append_left(val), peak = val, node not removed(last_node is val)
# [x] append_left(val),append_left(val2), peak = val
# [x] peak empty returns none

def test_peak_returns_value():
    """append_left(val), peak = val."""
    deque = Deque('a')
    assert deque.peak() is 'a'


def test_peak_returns_value_does_not_pop():
    """append_left(val), peak = val, node not removed(last_node is val)."""
    deque = Deque('a')
    a = deque.peak()
    assert deque._deque.last_node == 'a'


def test_peak_returns_correct_value():
    """append_left(val),append_left(val2), peak = val2."""
    deque = Deque()
    deque.append('a')
    deque.append('b')
    assert deque.peak() is 'b'


def test_peak_empty_deque_returns_none():
    """Peak empty returns none."""
    deque = Deque()
    assert deque.peak() is None


# ------------------Peak_left Method Tests--------------------
# [x] append_left(val), peak = val
# [x] append_left(val), peak = val, node not removed(last_node is val)
# [x] append_left(val),append_left(val2), peak = val
# [x] peak empty returns none

def test_peak_left_returns_value():
    """append_left(val), peak = val."""
    deque = Deque('a')
    assert deque.peak_left() is 'a'


def test_peak_left_returns_value_does_not_pop():
    """append_left(val), peak = val, node not removed(first_node is val)."""
    deque = Deque('a')
    a = deque.peak_left()
    assert deque._deque.first_node == 'a'


def test_peak_left_returns_correct_value():
    """append_left(val),append_left(val2), peak = val2."""
    deque = Deque()
    deque.append_left('a')
    deque.append_left('b')
    assert deque.peak_left() is 'b'


def test_peak_left_empty_deque_returns_none():
    """Peak empty returns none."""
    deque = Deque()
    assert deque.peak_left() is None


# -------------Size Method Tests------------------
# [x] size of new deque is 0.
# [x] append_left, size is 1.
# [x] append_left, pop size is 0.
# [x] append_left, peak size is 1.
# [x] pop, size of dll is 0.


def test_size_of_new_Deque():
    """Size of new deque is 0."""
    deque = Deque()
    assert deque.size() == 0


def test_size_increments_with_append_left():
    """Append_left, size is 1."""
    deque = Deque()
    deque.append_left('val')
    assert deque.size() == 1


def test_size_decrements_with_pop():
    """Append_left, pop size is 0."""
    deque = Deque()
    deque.append_left('val')
    assert deque.size() == 1
    deque.pop()
    assert deque.size() == 0


def test_size_stays_same_with_peak():
    """Append_left, peak size is 1."""
    deque = Deque()
    deque.append_left('val')
    assert deque.size() == 1
    deque.peak()
    assert deque.size() == 1


def test_size_stays_with_pop_error():
    """Pop, size of dll is 0."""
    deque = Deque()
    with pytest.raises(IndexError):
        deque.pop()
    assert deque.size() == 0

