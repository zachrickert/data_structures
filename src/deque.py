# -*- coding: utf-8 -*-
"""Modules for the DLL Class and a Node Class that makes up the list."""

from double import DLL


class Deque(object):
    """class implementation of a Deque."""

    def __init__(self, itterable=None):
        """Initialize the stack."""
        self._deque = DLL(itterable)

    def append_left(self, val):
        """Push an item, push onto the first node."""
        return self._deque.push(val)

    def append(self, val):
        """Push an item, push onto the last node."""
        return self._deque.append(val)

    def pop_left(self):
        """Pop an item of the end of the left end of the list."""
        return self._deque.pop()

    def pop(self):
        """Pop an item of the end of the right end of the list."""
        return self._deque.shift()

    def peak(self):
        """Peak at an item of the end of the right end of the list."""
        try:
            return self._deque.last_node.value
        except AttributeError:
            return None

    def peak_left(self):
        """Peak at an item of the end of the right end of the list."""
        try:
            return self._deque.first_node.value
        except AttributeError:
            return None

    def size(self):
        """Return size of the Deque."""
        return len(self._deque)
