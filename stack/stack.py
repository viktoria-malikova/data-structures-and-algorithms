# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the missing functions here below

from linkedlist import LinkedList


class Stack:
    """
    An implementation of a stack structure which utilizes the LinkedList class.

    Attributes:
        stack (LinkedList): A linked list that is used to store the objects added into the stack.
    """
    def __init__(self):
        """Initialize the stack."""
        self.stack = LinkedList()

    def push(self, obj):
        """Add the object 'obj' to the stack."""
        self.stack.add_first(obj)

    def pop(self):
        """Return and remove the newest (previously added) object from the stack."""
        object = self.stack.get_position(0)
        self.stack.remove_position(0)
        return object

    def top(self):
        """Return the newest (previously added) object."""
        object = self.stack.get_position(0)
        return object

    def is_empty(self):
        """If stack has no objects, return True, else return False."""
        if self.stack.get_size() == 0:
            return True
        else:
            return False