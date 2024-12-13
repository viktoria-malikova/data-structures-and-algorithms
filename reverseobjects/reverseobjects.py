# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the reverseObjects function here below

from stack import Stack

def reverseObjects(sequence):
    """Returns the contents of sequence reversed in a list."""
    reversed_list = []
    stack = Stack()

    #​​​​‌‌‌​‌‌‌‌‌​ Do something with stack and sequence
    #​​​​‌‌‌​‌‌‌‌‌​ ...
    #​​​​‌‌‌​‌‌‌‌‌​ ...
    #​​​​‌‌‌​‌‌‌‌‌​ ...
    #​​​​‌‌‌​‌‌‌‌‌​ Return the sequence reversed

    # Push all elements from the sequence onto the stack
    for item in sequence:
        stack.push(item)

    # Pop all elements from the stack to reverse the sequence
    while not stack.is_empty():
        reversed_list.append(stack.pop())

    return reversed_list

