# -*- coding: utf-8 -*-
"""Testing module for the Linked List and Node classes."""

from double import Node, DLL
import pytest

TYPES_OF_INPUTS = [
    'a', 1, 1.0, 1 / 3, (1, 2), [1, 2], True, None, 'āĕĳœ', b'1', '\t'
]


# ------------------Node Initialization Tests--------------------
# [x] test default initialization of a node is None value.
# [x] test initialization of a Node with a value.
# [x] test default initialization of a node results in no forward.
# [x] test default initialization of a node results in no backward.
# [x] test initialization of a node results with forward.
# [x] test initialization of a node results with backward.

def test_initializtion_node_dafault():
    """Test default initialization of a node is None value."""
    node = Node()
    assert node.value is None


def test_node_init_value():
    """Test initialization of a Node with a value."""
    node = Node(1)
    assert node.value is 1


def test_node_init_forward_none():
    """Test default initialization of a node results in no forward."""
    node = Node()
    assert node.forward is None


def test_node_init_backward_none():
    """Test default initialization of a node results in no backward."""
    node = Node()
    assert node.backward is None


def test_node_init_next_with_forward():
    """Test initialization of a node results with pointer."""
    node1 = Node(1)
    node2 = Node(2, node1)
    assert node2.forward is node1


def test_node_init_next_with_backward():
    """Test initialization of a node results with pointer."""
    node1 = Node(1)
    node2 = Node(2, backward=node1)
    assert node2.backward is node1


# --------------------Node Equality Tests-----------------------
# [x] test if a node will equal its value.
# [x] test if a value will equal a Node.
# [x] test if a two nodes with same value equal each other.
# [x] two nodes do not evaluate to each other using is key word.


def test_node_eq_value():
    """Test if a node will equal its value."""
    node = Node(1)
    assert node == 1


def test_value_eq_node():
    """Test if a value will equal a Node."""
    node = Node(1)
    assert 1 == node


def test_node1_eq_node2():
    """Test if a two nodes with same value equal each other."""
    node1 = Node(1)
    node2 = Node(1)
    assert node1 == node2


def test_node1_is_not_node2():
    """Two nodes do not evaluate to each other using is key word."""
    node1 = Node(1)
    node2 = Node(1)
    assert node1 is not node2


# --------------------Node Push Method-----------------------
# [x] push value, check new node has correct value.
# [x] push value, check new node has forward.
# [x] push value, check new node has no backward.
# [] push value, check old node has backward to new node.

def test_node_push_check_value():
    """Push value, check new node has correct value."""
    node1 = Node(1)
    node2 = node1._push(2)

    assert node2 == 2


def test_node_push_check_forward():
    """Push value, check new node has forward."""
    node1 = Node(1)
    node2 = node1._push(2)
    assert node2.forward is node1


def test_node_push_check_backward():
    """Push value, check new node has no backward."""
    node1 = Node(1)
    node2 = node1._push(2)
    assert node2.backward is None


def test_node_push_check_backward_old_node():
    """Push value, check old node has backward to new node."""
    node1 = Node(1)
    node2 = node1._push(2)
    assert node1.backward is node2


# --------------------Node Append Method-----------------------
# [x] append value, check new node has correct value.
# [x] append value, check new node has forward.
# [x] append value, check new node has no backward.
# [] append value, check old node has backward to new node.

def test_node_append_check_value():
    """Append value, check new node has correct value."""
    node1 = Node(1)
    node2 = node1._append(2)

    assert node2 == 2


def test_node_append_check_backward():
    """Append value, check new node has backward."""
    node1 = Node(1)
    node2 = node1._append(2)
    assert node2.backward is node1


def test_node_append_check_forward():
    """Append value, check new node has no forward."""
    node1 = Node(1)
    node2 = node1._append(2)
    assert node2.forward is None


def test_node_append_check_forward_old_node():
    """Append value, check old node has forward to new node."""
    node1 = Node(1)
    node2 = node1._append(2)
    assert node1.forward is node2


# --------------------Node Value Check-----------------------
def test_value_in_equals_value_out():
    """Test to see if node can handle the different types of data inputs."""
    for data in TYPES_OF_INPUTS:
        node = Node(data)
        assert node.value == data


# -------------DLL Initialization Tests------------------
# [x] test if the dll initializes with first_node as None.
# [x] test if the dll initializes with last_node as None.
# [x] test if the dll initializes with length 0.

def test_dll_init_first_node():
    """Test if the dll initializes with first_node as None."""
    dll = DLL()
    assert(dll.first_node is None)


def test_dll_init_last_node():
    """Test if the dll initializes with flast_node as None."""
    dll = DLL()
    assert(dll.last_node is None)


def test_dll_init_size():
    """Test if the dll initializes with length 0."""
    dll = DLL()
    assert(dll.length is 0)


# -------------DLL Push Tests------------------
# push(val) - will insert the value ‘val’ at the head of the list.
# [x] push, check first node value
# [x] push empty list, check last is first node.
# [x] push, check first node forward is None.
# [x] push, check first node backward is None
# [x] push, push, check first node forward.


def test_push_first_node_value():
    """Push, check first node value."""
    dll = DLL()
    dll.push(1)
    assert (dll.first_node.value is 1)


def test_push_empty_last_node_is_first_node():
    """Push empty list, check last node is first node."""
    dll = DLL()
    dll.push(1)
    assert (dll.last_node is dll.first_node)


def test_push_empty_first_node_forward_none():
    """Push, check first node forward is None."""
    dll = DLL()
    dll.push(1)
    assert (dll.first_node.forward is None)


def test_push_empty_first_node_backward_none():
    """Push, check first node forward is None."""
    dll = DLL()
    dll.push(1)
    assert (dll.first_node.backward is None)


def test_push_first_node_forward_updates():
    """Push, push, check first node forward."""
    dll = DLL()
    node1 = dll.push(1)
    dll.push('a')
    assert (dll.first_node.forward is node1)


# -------------DLL Append Tests------------------
# append(val) will append the value ‘val’ at the tail of the list.
# [] append, check last node value.
# [] append empty list, check first is last node.
# [] append, check last node backward is None.
# [] append, check last node forward is None
# [] append, append, check last node backward.


def test_append_last_node_value():
    """Append, check last node value."""
    dll = DLL()
    dll.append(1)
    assert (dll.last_node.value is 1)


def test_append_empty_last_node_is_last_node():
    """Append empty list, check first node is last node."""
    dll = DLL()
    dll.append(1)
    assert (dll.first_node is dll.last_node)


def test_append_empty_last_node_backward_none():
    """Append, check last node backward is None."""
    dll = DLL()
    dll.append(1)
    assert (dll.last_node.backward is None)


def test_append_empty_last_node_forward_none():
    """Append, check last node forward is None."""
    dll = DLL()
    dll.append(1)
    assert (dll.last_node.forward is None)


def test_append_last_node_backward_updates():
    """Append, append, check last node backward."""
    dll = DLL()
    node1 = dll.append(1)
    dll.append('a')
    assert (dll.last_node.backward is node1)


# -------------Linked List Length Tests------------------
# [] len of new dll is 0.
# [] push, len of dll in 1.
# [] append, len of dll in 1.
# [] push, pop, len of dll in 0.
# [] push, shift, len of dll in 0.
# [] append, pop, len of dll in 0.
# [] append, shift, len of dll in 0.
# [] pop, len of dll in 0.
# [] append, len of dll in 0.

def test_len_empty_linked_list():
    """Len of new dll is 0."""
    dll = DLL()
    assert(len(dll) is 0)


def test_len_after_push():
    """Push, len of dll in 1."""
    dll = DLL()
    dll.push(1)
    assert(len(dll) is 1)


def test_len_after_append():
    """Append, len of dll in 1."""
    dll = DLL()
    dll.append(1)
    assert(len(dll) is 1)


# def test_len_after_pop():
#     """Test if len of a new string is 0."""
#     dll = DLL()
#     dll.push(1)
#     dll.pop()
#     assert(len(dll) is 0)


# def test_len_is_0_after_index_error():
#     """Test if len of a new string is 0."""
#     dll = DLL()
#     with pytest.raises(IndexError):
#         dll.pop()
#     assert(len(dll) is 0)


# -------DLL Initialization Tests by itterable------------
# [x] initialize empty, first node is None.
# [x] initialize empty, last node is None.
# [x] initialize one charicter itterable, first node is val.
# [x] initialize one charicter itterable, last node is val.
# [x] initialize one charicter itterable, len is 1
# [x] initialize multi charicter itterable, first node is first value of itterable.
# [x] initialize multi charicter itterable, last node is last value of itterable.
# [x] initialize multi charicter itterable, len is len(itterable)
# [x] initialize multi charicter itterable, first node forward to second item.
# [x] initialize multi charicter itterable, last node backward to next to last item.
# [x] initialize non-itterable, TypeError raised

def test_initialization_with_empty_list_first_node_empty():
    """Initialize empty, first node is None."""
    dll = DLL([])
    assert dll.first_node is None


def test_initialization_with_empty_list_last_node_empty():
    """Initialize empty, last node is None."""
    dll = DLL([])
    assert dll.first_node is None


def test_initialization_with_list_first_node():
    """Initialize one charicter itterable, first node is val."""
    dll = DLL('a')
    assert dll.first_node.value == 'a'


def test_initialization_with_list_last_node():
    """Initialize one charicter itterable, last node is val."""
    dll = DLL('a')
    assert dll.last_node.value == 'a'


def test_initialization_with_list_len_is_one():
    """Initialize one charicter itterable, len is 1."""
    dll = DLL('a')
    assert len(dll) == 1


def test_initialization_with_multi_char_check_first_node():
    """Initialize multi charicter itterable, first node is first value of itterable."""
    dll = DLL('abcdef')
    assert dll.first_node == 'a'


def test_initialization_with_multi_char_check_last_node():
    """Initialize multi charicter itterable, last node is last value of itterable."""
    dll = DLL('abcdef')
    assert dll.last_node == 'f'


def test_initialization_with_multi_char_check_len():
    """Initialize multi charicter itterable, len is len(itterable)."""
    dll = DLL('abcdef')
    assert len(dll) == 6


def test_initialization_with_multi_char_check_first_node_forward():
    """Initialize multi charicter itterable, first node forward to second item."""
    dll = DLL('abcdef')
    assert dll.first_node.forward == 'b'


def test_initialization_with_multi_char_check_last_node_backward():
    """Initialize multi charicter itterable, last node backward to next to last item."""
    dll = DLL('abcdef')
    assert dll.last_node.backward == 'e'


def test_initialization_with_non_itterable():
    """Initialize non-itterable, TypeError raised."""
    with pytest.raises(TypeError):
        dll = DLL(2)


# -------------DLL Pop Tests------------------
# [x] push(val), pop - will return val.
# [x] append(val), pop - will return val.
# [x] push(val), pop - first node will be None.
# [x] push(val), pop - last node will be None.
# [x] push(val), append(val2) pop - return val
# [x] pop - returns IndexError
# [x] push, pop, pop returns IndexError


def test_pop_returns_value():
    """push(val), pop - will return val."""
    dll = DLL()
    dll.push(1)
    assert(dll.pop() is 1)


def test_pop_returns_value_append():
    """append(val), pop - will return val."""
    dll = DLL()
    dll.append(1)
    assert(dll.pop() is 1)


def test_pop_first_node_none():
    """push(val), pop - first node will be None."""
    dll = DLL()
    dll.push(1)
    dll.pop()
    assert(dll.first_node is None)


def test_pop_last_node_none():
    """push(val), pop - first node will be None."""
    dll = DLL()
    dll.push(1)
    dll.pop()
    assert(dll.last_node is None)


def test_push_append_pop_returns_correct_val():
    """push(val), append(val2) pop - return val"""
    dll = DLL()
    dll.push(1)
    dll.append(2)
    assert(dll.pop() == 1)


def test_pop_raises_index_error():
    """Pop - returns IndexError."""
    dll = DLL()
    with pytest.raises(IndexError):
        dll.pop()


def test_pop_raises_index_error_after_push():
    """Pop - returns IndexError."""
    dll = DLL()
    dll.push(1)
    dll.pop()
    with pytest.raises(IndexError):
        dll.pop()


# -------------DLL Shift Tests------------------
# remove the last value from the tail of the list and return it. 
# [x] append(val), shift - will return val.
# [x] push(val), shift - will return val.
# [x] append(val), shift - first node will be None.
# [x] append(val), shift - last node will be None.
# [x] append(val), push(val2) shift - return val
# [x] shift - returns IndexError
# [x] append, shift, shift returns IndexError


def test_shift_returns_value():
    """append(val), shift - will return val."""
    dll = DLL()
    dll.append(1)
    assert(dll.shift() is 1)


def test_shift_returns_value_push():
    """push(val), shift - will return val."""
    dll = DLL()
    dll.push(1)
    assert(dll.shift() is 1)


def test_shift_first_node_none():
    """append(val), shift - first node will be None."""
    dll = DLL()
    dll.append(1)
    dll.shift()
    assert(dll.first_node is None)


def test_shift_last_node_none():
    """append(val), shift - first node will be None."""
    dll = DLL()
    dll.append(1)
    dll.shift()
    assert(dll.last_node is None)


def test_append_push_shift_returns_correct_val():
    """append(val), push(val2) shift - return val"""
    dll = DLL()
    dll.append(1)
    dll.push(2)
    assert(dll.shift() == 1)


def test_shift_raises_index_error():
    """shift - returns IndexError."""
    dll = DLL()
    with pytest.raises(IndexError):
        dll.shift()


def test_shift_raises_index_error_after_append():
    """shift - returns IndexError."""
    dll = DLL()
    dll.append(1)
    dll.shift()
    with pytest.raises(IndexError):
        dll.shift()


# -------------DLL Search Tests------------------
# search(val) - will return the node containing ‘val’ in the list, if present, else None.
# [x] search empty list, return none.
# [x] search list with one node, returns a node.
# [x] search list with one node, return that node.
# [] search list with multiple nodes returns node.
# [] search list with multiple nodes, return none.

def test_search_empty_list():
    """Search empty list, return none."""
    dll = DLL([])
    assert dll.search('a') is None


def test_search_returns_node():
    """Search list with one node, returns a node."""
    dll = DLL('a')
    node = dll.search('a')
    assert isinstance(node, Node)


def test_search_list():
    """Search list with one node, return that node."""
    dll = DLL('a')
    node = dll.search('a')
    assert node.value == 'a'


def test_search_multi_node_list():
    """Search list with multiple nodes returns node."""
    dll = DLL('abcdef')
    node = dll.search('c')
    assert node.value is 'c'


def test_search_multi_node_list_returns_none():
    """Search list with multiple nodes, return none."""
    dll = DLL('abcdef')
    assert dll.search('g') is None


# -------------Linked List Remove Tests------------------
#  remove(val) - will remove the given node from the list,
# wherever it might be (node must be an item in the list).
# [x] remove a single node from a list.
# [x] remove node from the head of the list.
# [x] remove node from end of list.
# [x] remove the only node in the list.
# [] remove a node not in the list.
# [] remove size decrements by one.
# [] remove head node, len decrease by one.
# [] remove only node in list.Len = 0
# [] remove, not found, size not changed.


def test_remove_node_from_list():
    """Remove a single node from a list."""
    dll = DLL('abcdef')
    assert dll.search('d') == 'd'
    dll.remove('d')
    assert dll.search('d') is None


def test_remove_node_from_first_node():
    """Remove node from the head of the list."""
    dll = DLL('abcdef')
    assert dll.first_node == 'a'
    dll.remove('a')
    assert dll.first_node == 'b'


def test_remove_node_from_last_node():
    """Remove node from the head of the list."""
    dll = DLL('abcdef')
    assert dll.last_node == 'f'
    dll.remove('f')
    assert dll.last_node == 'e'


def test_remove_only_node_in_list():
    """Remove the only node in the list."""
    dll = DLL('a')
    dll.remove('a')
    assert dll.first_node is None
    assert dll.last_node is None


def test_remove_only_node_in_list():
    """Remove the only node in the list."""
    dll = DLL('a')
    dll.remove('a')
    assert dll.first_node is None
    assert dll.last_node is None


def test_remove_node_from_last_node():
    """Remove a node not in the list."""
    dll = DLL('abcdef')
    with pytest.raises(ValueError):
        dll.remove('k')


# -------------DLL Traverse Tests------------------
#  traverse(node) - will traverse through the list.
# [x] traverse forward through a list.
# [x] traverse backwards through a list.
# [x] traverse through an empty list.

def test_traverse_forward():
    """Test to traverse forward."""
    dll = DLL('abcd')
    list_items = []
    for item in dll.traverse_forward():
        list_items.append(item)
    assert list_items == ['a', 'b', 'c', 'd']


def test_traverse_backward():
    """Test to traverse forward."""
    dll = DLL('abcd')
    list_items = []
    for item in dll.traverse_backward():
        list_items.append(item)
    assert list_items == ['d', 'c', 'b', 'a']


def test_traverse_empty_list():
    """Test to traverse empty list."""
    dll = DLL([])
    list_items = []
    for item in dll.traverse_forward():
        list_items.append(item)
    assert list_items == []


# -------------DLL Insert Tests------------------
# [x] insert_after, check prev node forward pointer.
# [x] insert_after, check new node backward pointer.
# [x] insert_after, after last node. Check last node.
# [] insert_before, check next node backward pointer.
# [] insert_before, check new node forward pointer.
# [] insert_before, before first node. Check last node.

def test_insert_after_check_prev_forward():
    """Insert_after, check prev node forward pointer."""
    dll = DLL('abcd')
    bnode = dll.search('b')
    enode = dll.insert_after('e', bnode)
    assert bnode.forward is enode


def test_insert_after_check_new_node_backwards():
    """Insert_after, check new node backward pointer."""
    dll = DLL('abcd')
    bnode = dll.search('b')
    enode = dll.insert_after('e', bnode)
    assert enode.backward == 'b'


def test_insert_after_last_node():
    """Insert_after, after last node. Check last node."""
    dll = DLL('abcd')
    dnode = dll.search('d')
    enode = dll.insert_after('e', dnode)
    assert dll.last_node is enode

def test_insert_before_check_next_backward():
    """Insert_before, check next node backward pointer."""
    dll = DLL('abcd')
    bnode = dll.search('b')
    enode = dll.insert_before('e', bnode)
    assert bnode.backward is enode


def test_insert_before_check_new_node_forwards():
    """Insert_backward, check new node forward pointer."""
    dll = DLL('abcd')
    bnode = dll.search('b')
    enode = dll.insert_before('e', bnode)
    assert enode.forward == 'b'


def test_insert_before_first_node():
    """Insert_before, before first node. Check first node."""
    dll = DLL('abcd')
    anode = dll.search('a')
    enode = dll.insert_before('e', anode)
    assert dll.first_node is enode

