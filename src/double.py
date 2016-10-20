# -*- coding: utf-8 -*-
"""Modules for the DLL Class and a Node Class that makes up the list."""


class Node(object):
    """Nodes to make up the linked list."""

    def __init__(self, value=None, forward=None, backward=None):
        """Initialize a node."""
        self.value = value
        self.forward = forward
        self.backward = backward

    def __eq__(self, other):
        """Allow a node to be equal to it's value."""
        return self.value == other

    def _push(self, val):
        """Return a new node with value and a pointer to self node."""
        new_node = Node(val, self)
        self.backward = new_node
        return new_node

    def _append(self, val):
        """Return a new node with value and a pointer to self node."""
        new_node = Node(val, backward=self)
        self.forward = new_node
        return new_node

    def _search(self, val):
        """Return node if matches the given val."""
        if val == self:
            return self
        else:
            return self.forward._search(val)

    def _remove(self, val):
        """Remove the next node if it matches the val."""
        if self == val:
            next_node = self.forward
            prev_node = self.backward
            try:
                prev_node.forward = next_node
            except AttributeError:
                pass
            try:
                next_node.backward = prev_node
            except AttributeError:
                pass
            return self
        else:
            return self.forward._remove(val)

    def _insert_after(self, val):
        """Insert a node after the given node."""
        new_node = Node(val, self.forward, self)
        self.forward = new_node
        return new_node

    def _insert_before(self, val):
        """Insert a node after the given node."""
        new_node = Node(val, self, self.backward)
        self.backward = new_node
        return new_node


class DLL(object):
    """Doubly-Linked List data structure."""

    def __init__(self, itterable=None):
        """Initialize a doubly linked list."""
        self.first_node = None
        self.last_node = None
        self.length = 0

        if itterable:
            for item in itterable:
                self.append(item)

    def __len__(self):
        """Allow len to be called on the list."""
        return self.length

    def size(self):
        """Return number of nodes."""
        return self.length

    def push(self, val):
        """Insert the value ‘val’ at the head of the list."""
        try:
            self.first_node = self.first_node._push(val)
        except AttributeError:
            # AttributeError if no first node set.
            self.first_node = Node(val)
            self.last_node = self.first_node
        self.length += 1
        return self.first_node

    def append(self, val):
        """Will append the value ‘val’ at the tail of the list."""
        try:
            self.last_node = self.last_node._append(val)
        except AttributeError:
            # AttributeError if no last node set.
            self.last_node = Node(val)
            self.first_node = self.last_node
        self.length += 1
        return self.last_node

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        try:
            val, self.first_node = self.first_node.value, self.first_node.forward
        except AttributeError:
            raise IndexError('pop from empty list')
        self.length -= 1
        if self.length == 0:
            self.last_node = None
        return val

    def shift(self):
        """Shift the first value off the tail of the list and return it."""
        try:
            val, self.last_node = self.last_node.value, self.last_node.backward
        except AttributeError:
            raise IndexError('shift from empty list')
        self.length -= 1
        if self.length == 0:
            self.first_node = None
        return val

    def search(self, val):
        """Return the node containing ‘val’ in the list, if present, else None."""
        try:
            return self.first_node._search(val)
        except AttributeError:
            # If there is no first node or get to the end of the list, return none.
            return None

    def remove(self, val):
        """Will remove the given node from the list."""
        try:
            removed_node = self.first_node._remove(val)
        except AttributeError:
            raise ValueError('DLL.remove(x): x not in list')
        if self.first_node is removed_node:
            self.first_node = self.first_node.forward
        if self.last_node is removed_node:
            self.last_node = self.last_node.backward
        if removed_node:
            self.length -= 1

    def traverse_forward(self):
        """Traverse from the first node going forward through the list."""
        current_node = self.first_node
        while current_node:
            yield current_node
            current_node = current_node.forward

    def traverse_backward(self):
        """Traverse from the last node going reverse through the list."""
        current_node = self.last_node
        while current_node:
            yield current_node
            current_node = current_node.backward

    def insert_after(self, val, node):
        """Insert a node with val after given node."""
        if node == self.last_node:
            return self.append(node)
        else:
            return node._insert_after(val)

    def insert_before(self, val, node):
        """Insert a node with val after given node."""
        if node == self.first_node:
            return self.push(node)
        else:
            return node._insert_before(val)


