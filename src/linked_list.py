# -*- coding: utf-8 -*-
"""Modules for the LinkedList Class and a Node Class that makes up the list."""


class Node(object):
    """Nodes to make up the linked list."""

    def __init__(self, value=None, pointer=None):
        """Initialize a node."""
        self.value = value
        self.pointer = pointer

    def __eq__(self, other):
        """Allow a node to be equal to it's value."""
        return self.value == other

    def _push(self, val):
        """Return a new node with value and a pointer to self node."""
        return Node(val, self)

    def _search(self, val):
        """Return node if matches the given val."""
        if val == self:
            return self
        else:
            return self.pointer._search(val)

    def _remove(self, val):
        """"Remove the next node if it matches the val."""
        try:
            if self.pointer.value == val:
                self.pointer = self.pointer.pointer
                return self
            else:
                return self.pointer._remove(val)
        except AttributeError:
            return None


class LinkedList(object):
    """Linked list data structure."""

    def __init__(self, itterable=None):
        """Initialize a singularly linked list."""
        self.head = None
        self.length = 0

        if itterable:
            for item in itterable:
                self.push(item)

    def __len__(self):
        """Allow len to be called on the list."""
        return self.length


    def push(self, val):
        """Insert the value ‘val’ at the head of the list."""
        try:
            self.head = self.head._push(val)
        except AttributeError:
            # AttributeError if no head set.
            self.head = Node(val)
        self.length += 1
        return self.head

    def pop(self):
        """Pop off the value ‘val’ at the head of the list."""
        try:
            val, self.head = self.head.value, self.head.pointer
        except AttributeError:
            raise IndexError('pop from empty list')
        self.length -= 1
        return val

    def size(self):
        """Return the length of the list."""
        return self.length

    def search(self, val):
        """Return the node containing ‘val’ in the list, if present, else None."""
        try:
            return self.head._search(val)
        except AttributeError:
            # If there is no head or get to the end of the list, return none.
            return None

    def remove(self, val):
        """Will remove the given node from the list."""
        if self.head == val:
            self.head = self.head.pointer
            self.length -= 1
        else:
            if self.head._remove(val):
                self.length -= 1
            else:
                raise ValueError('LinkedList.remove(x): x not in list') 

    def traverse(self, start_node=None, end_node=None):
        """
        Transverse() - through the linked list starting at a given node 
        and going to the end node (end inclusive)
        """
        if not start_node:
            current_node = self.head
        else:
            current_node = start_node
        while current_node is not end_node:
            try:
                yield current_node.value
            except AttributeError:
                raise IndexError('End node after start node')
            current_node = current_node.pointer
        if end_node:
            yield end_node.value

    def display(self):
        """
        display() - will return a unicode string representing the list 
        as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)
        """
        node_list = []

        for node in self.traverse():
            node_list.append(repr(node))
        return '({})'.format(", ".join(node_list))

