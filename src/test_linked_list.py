# -*- coding: utf-8 -*-
"""Testing module for the Linked List and Node classes."""

from linked_list import Node, LinkedList
import pytest

TYPES_OF_INPUTS = [
    'a', 1, 1.0, 1/3, (1, 2), [1, 2], True, None, 'āĕĳœ', b'1', '\t'
]


# ------------------Node Initialization Tests--------------------
# [x] test default initialization of a node is None value.
# [x] test initialization of a Node with a value.
# [x] test default initialization of a node results in no pointer.
# [x] test initialization of a node results with pointer.

def test_node_init_value_null():
    """Test default initialization of a node is None value."""
    node = Node()
    assert node.value is None


def test_node_init_value():
    """Test initialization of a Node with a value."""
    node = Node(1)
    assert node.value is 1


def test_node_init_next():
    """Test default initialization of a node results in no pointer."""
    node = Node()
    assert node.pointer is None


def test_node_init_next_with_pointer():
    """Test initialization of a node results with pointer."""
    node1 = Node(1)
    node2 = Node(2, node1)
    assert node2.pointer is node1


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
    """Two nodes do not evaluate to each other using is"""
    node1 = Node(1)
    node2 = Node(1)
    assert node1 is not node2


# --------------------Node Value Check-----------------------
def test_value_in_equals_value_out():
    """Test to see if node can handle the different types of data inputs."""
    for data in TYPES_OF_INPUTS:
        node = Node(data)
        assert node.value == data


# --------------------Node Push Method-----------------------
# [x] push value, check new node has correct value.
# [x] push value, check new node has correct pointer.

def test_node_push_check_value():
    """Push value, check new node has correct value."""
    node1 = Node(1)
    node2 = node1._push(2)
    assert node2 == 2


def test_node_push_check_pointer():
    """Push value, check new node has correct pointer"""
    node1 = Node(1)
    node2 = node1._push(2)
    assert node2.pointer is node1


# -------------Linked List Initialization Tests------------------
def test_linked_list_init_head_node():
    """Test if the linked list initializes with head as None."""
    linked = LinkedList()
    assert(linked.head is None)


def test_linked_list_init_size():
    """Test if the linked list initializes with length 0."""
    linked = LinkedList()
    assert(linked.length is 0)


# -------------Linked List Push Tests------------------
# push(val) - will insert the value ‘val’ at the head of the list.
# [x] push, check head node value
# [x] push, check head node pointer is None
# [x] push, push, check head node pointer.

def test_push_head_value():
    """push, check head node value."""
    linked = LinkedList()
    linked.push(1)
    assert (linked.head.value is 1)


def test_push_head_pointer_is_none():
    """Push, check head node pointer."""
    linked = LinkedList()
    linked.push(1)
    assert (linked.head.pointer is None)


def test_push_head_pointer_points_to_next():
    """Push, push, check head node pointer."""
    linked = LinkedList()
    linked.push(1)
    linked.push(2)
    assert (linked.head.pointer == 1)


# -------------Linked List Length Tests------------------
# [x] len of new list is 0.
# [x] push, len of list in 1.
# [x] push, pop, len of list in 0.
# [x] pop, len of list in 0.

def test_len_empty_linked_list():
    """Test if len of a new string is 0."""
    linked = LinkedList()
    assert(len(linked) is 0)


def test_len_after_push():
    """Test if len of a new string is 0."""
    linked = LinkedList()
    linked.push(1)
    assert(len(linked) is 1)


def test_len_after_pop():
    """Test if len of a new string is 0."""
    linked = LinkedList()
    linked.push(1)
    linked.pop()
    assert(len(linked) is 0)


def test_len_is_0_after_index_error():
    """Test if len of a new string is 0."""
    linked = LinkedList()
    with pytest.raises(IndexError):
        linked.pop()
    assert(len(linked) is 0)


# -------Linked List Initialization Tests by itterable------------
# [x] initialize empty, head node is None.
# [x] initialize one charicter itterable, head node is val.
# [x] initialize one charicter itterable, len is 1
# [x] initialize multi charicter itterable, head node is last value of itterable.
# [x] initialize multi charicter itterable, len is len(itterable)
# [x] initialize multi charicter itterable, head node pointer second to last item.
# [x] initialize non-itterable, TypeError raised

def test_initialization_with_empty_list():
    """Initialize empty, head node is None."""
    linked = LinkedList([])
    assert linked.head is None


def test_head_node_initialization_with_one_char():
    """Initialize one charicter itterable, head node is val."""
    linked = LinkedList('a')
    assert linked.head == 'a'


def test_length_initialization_with_one_char():
    """Initialize one charicter itterable, len is 1."""
    linked = LinkedList('a')
    assert len(linked) == 1


def test_head_node_with_multi_chars():
    """Initialize multi charicter itterable, head node is last value of itterable."""
    linked = LinkedList('abc')
    assert linked.head == 'c'


def test_length_with_multi_chars():
    """Initialize multi charicter itterable, len is len(itterable)."""
    linked = LinkedList('abc')
    assert len(linked) == 3


def test_pointer_with_multi_char_init():
    """Initialize multi charicter itterable, head node pointer second to last item."""
    linked = LinkedList('abc')
    assert linked.head.pointer == 'b'


def test_initialization_with_non_itterable():
    """Initialize non-itterable, TypeError raised."""
    with pytest.raises(TypeError):
        linked = LinkedList(2)


# -------------Linked List Pop Tests------------------
# [x] push(val), pop - will return val.
# [x] push(val), pop - head will be None.
# [x] pop - returns IndexError
# [x] push, pop, pop returns IndexError

def test_pop_returns_value():
    """push(val), pop - will return val."""
    linked = LinkedList()
    linked.push(1)
    assert(linked.pop() is 1)


def test_pop_rests_head_value():
    """push(val), pop - head will be None."""
    linked = LinkedList()
    linked.push(1)
    linked.pop()
    assert(linked.head is None)


def test_pop_raises_index_error():
    """Pop - returns IndexError."""
    linked = LinkedList()
    with pytest.raises(IndexError):
        linked.pop()


def test_pop_raises_index_error_after_push():
    """Pop - returns IndexError."""
    linked = LinkedList()
    linked.push(1)
    linked.pop()
    with pytest.raises(IndexError):
        linked.pop()


# -------------Linked List Size Tests------------------
# size() - will return the length of the list.
# [x] size of new list is 0.
# [x] push, size of list in 1.
# [x] push, pop, size of list in 0.
# [x] push, pop, pop, size of list in 0.


def test_size_empty_linked_list():
    """Test if size of a new string is 0."""
    linked = LinkedList()
    assert(linked.size() is 0)


def test_size_after_push():
    """Test if size of a new string is 0."""
    linked = LinkedList()
    linked.push(1)
    assert(linked.size() is 1)


def test_size_after_pop():
    """Test if size of a new string is 0."""
    linked = LinkedList()
    linked.push(1)
    linked.pop()
    assert(linked.size() is 0)


def test_size_is_0_after_index_error():
    """Test if size of a new string is 0."""
    linked = LinkedList()
    with pytest.raises(IndexError):
        linked.pop()
    assert(linked.size() is 0)


# -------------Linked List Search Tests------------------
# search(val) - will return the node containing ‘val’ in the list, if present, else None.
# [x] search empty list, return none.
# [x] search list with one node, returns a node.
# [x] search list with one node, return that node.
# [x] search list with multiple nodes returns node.
# [x] search list with multiple nodes, return none.

def test_search_empty_list():
    """Search empty list, return none."""
    linked = LinkedList([])
    assert linked.search('a') is None


def test_search_returns_node():
    """Search list with one node, returns a node."""
    linked = LinkedList('a')
    node = linked.search('a')
    assert isinstance(node, Node)


def test_search_one_node_list():
    """Search list with one node, returns a node."""
    linked = LinkedList('a')
    node = linked.search('a')
    assert node.value is 'a'


def test_search_multi_node_list():
    """Search list with multiple nodes returns node."""
    linked = LinkedList('abcdef')
    node = linked.search('c')
    assert node.value is 'c'


def test_search_multi_node_list_returns_none():
    """Search list with multiple nodes, return none."""
    linked = LinkedList('abcdef')
    assert linked.search('g') is None


# -------------Linked List Remove Tests------------------
#  remove(val) - will remove the given node from the list,
# wherever it might be (node must be an item in the list).
# [x] remove a single node from a list.
# [x] remove node from the head of the list.
# [x] remove node from end of list.
# [x] remove the only node in the list.
# [x] remove a node not in the list.
# [x] remove size decrements by one.
# [x] remove head node, len decrease by one.
# [x] remove only node in list.Len = 0
# [x] remove, not found, size not changed.

def test_remove_node_from_list():
    """Remove a single node from a list."""
    linked = LinkedList('abcdef')
    assert linked.search('d') == 'd'
    linked.remove('d')
    assert linked.search('d') is None


def test_remove_node_from_head_of_list():
    """Remove node from the head of the list."""
    linked = LinkedList('abcdef')
    assert linked.head == 'f'
    linked.remove('f')
    assert linked.head == 'e'


def test_remove_node_from_end_of_list():
    """Remove node from the end of the list."""
    linked = LinkedList('abcdef')
    bnode = linked.search('b')
    assert bnode.pointer == 'a'
    linked.remove('a')
    assert bnode.pointer is None


def test_remove_only_node_in_list():
    """Remove the only node in the list."""
    linked = LinkedList('a')
    linked.remove('a')
    assert linked.head is None


def test_remove_node_not_in_list():
    """Remove a node not in the list."""
    linked = LinkedList('abcdef')
    with pytest.raises(ValueError):
        linked.remove('k')


def test_remove_node_length_update():
    """Remove size decrements by one."""
    linked = LinkedList('abcdef')
    assert len(linked) == 6
    linked.remove('c')
    assert len(linked) == 5


def test_remove_head_node_length_update():
    """Remove head node, len decrease by one."""
    linked = LinkedList('abcdef')
    assert len(linked) == 6
    linked.remove('f')
    assert len(linked) == 5


def test_remove_only_node_length_update():
    """Remove only node in list.Len = 0."""
    linked = LinkedList('a')
    assert len(linked) == 1
    linked.remove('a')
    assert len(linked) == 0


def test_remove_not_found_length_update():
    """remove, not found, size not changed."""
    linked = LinkedList('abcdef')
    assert len(linked) == 6
    with pytest.raises(ValueError):
        linked.remove('k')
    assert len(linked) == 6


# -------------Linked List Traverse Tests------------------
#  traverse(node) - will traverse through the list.
# [x] traverse through a list.
# [x] traverse through a list with a given start node.
# [x] traverse through a list with given stop node.
# [x] traverse through a list where start = end.
# [x] traverse through a list where end if before start.

def test_traverse():
    """Traverse through a list."""
    linked = LinkedList('abc')
    list_items = []
    for item in linked.traverse():
        list_items.append(item)
    assert list_items == ['c', 'b', 'a']


def test_traverse_start_node():
    """Traverse through a list."""
    linked = LinkedList('abcdef')
    list_items = []
    cnode = linked.search('c')
    for item in linked.traverse(cnode):
        list_items.append(item)
    assert list_items == ['c', 'b', 'a']


def test_traverse_end_node():
    """Traverse through a list."""
    linked = LinkedList('abcdef')
    list_items = []
    dnode = linked.search('d')
    for item in linked.traverse(end_node=dnode):
        list_items.append(item)
    assert list_items == ['f', 'e', 'd']


def test_traverse_start_and_end_nodes_same():
    """Traverse through a list."""
    linked = LinkedList('abcdef')
    list_items = []
    dnode = linked.search('d')
    for item in linked.traverse(dnode, dnode):
        list_items.append(item)
        assert item in ('d')
    assert len(list_items) == 1


def test_traverse_end_node_before_start():
    """Traverse through a list."""
    linked = LinkedList('abcdef')
    dnode = linked.search('d')
    anode = linked.search('a')
    with pytest.raises(IndexError):
        for item in linked.traverse(anode, dnode):
            pass

# -------------Linked List Search Tests------------------
#  display() - will return a unicode string representing the list as
# if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
# [x] display a one item list.
# [x] display a two item list.
# [x] display an int in a list.
# [x] display the given list.
# [x] display a zero item list.


def test_display_one_item_list():
    """Display a one item list."""
    linked = LinkedList('a')
    assert linked.display() == "('a')"


def test_display_two_item_list():
    """Display a two item list."""
    linked = LinkedList('ab')
    assert linked.display() == "('b', 'a')"


def test_display_int_in_a_list():
    """Display an int in a list."""
    linked = LinkedList([1])
    assert linked.display() == "(1)"


def test_display_of_given_list():
    """Display the given list."""
    linked = LinkedList(['tango', 37, 'sam', 12])
    assert linked.display() == "(12, 'sam', 37, 'tango')"


def test_display_of_an_empty_list():
    """Display the given list."""
    linked = LinkedList([])
    assert linked.display() == "()"
