# -*- coding: utf-8 -*-
"""Modules for the DLL Class and a Node Class that makes up the list."""

from double import DLL


class Stack(object):
    """class implementation of a Stack."""

    def __init__(self, itterable=None):
        """Initialize the stack."""
        self._stack = DLL()
        if itterable:
            for item in itterable:
                self.push(item)

    def push(self, val):
        """Push an item, push onto the first node."""
        return self._stack.push(val)

    def pop(self):
        """
        Pop first item in list.

        Remove the correct item from the stack and returns its value.
        (should raise an error if the stack is empty)
        """
        return self._stack.pop()

    def peak(self):
        """
        Peak at next item to be popped.

        Return the next value in the stack without popping it.
        If the stack is empty, returns None
        """
        try:
            return self._stack.first_node.value
        except AttributeError:
            # Attribute error is first_node is None
            return None

    def size(self):
        """Return size of the stack."""
        return self._stack.size()

