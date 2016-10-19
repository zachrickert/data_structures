# data_structures
Repository for common data structures

## Singly Linked List
In computer science, a linked list is a linear collection of data elements, called nodes, each pointing to the next node by means of a pointer. 
[Linked list](https://en.wikipedia.org/wiki/Linked_list)
This linked list will include the following operations:
* push(val) - will insert the value ‘val’ at the head of the list
* pop() - will pop the first value off the head of the list and return it.
* size() - will return the length of the list
* search(val) - will return the node containing ‘val’ in the list,
    if present, else None
* remove(val) - will remove the given node from the list, 
    wherever it might be (node must be an item in the list)
* traverse(start, end) - will traverse through the list with given start and end nodes.
    start - default set to the head of the list.
    end - will run until end node is reached.  default set to the end of the list. 
        if end node is before the start node it will  
* display() - will return a unicode string representing the list 
    as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
                                                                                                      