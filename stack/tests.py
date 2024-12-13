# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest

from stack import Stack


class Operation:
    """
    Arbitrary class for testing purposes.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Operation({0!r})".format(self.name)


class TestStack(unittest.TestCase):
    """
    Unit tests for the class Stack.
    """

    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        """stack.is_empty returns True for a new stack. (1p)"""

        #​​​​‌‌‌​‌‌‌‌‌​ Remember that setUp has just been called and self.stack should be equal to Stack()
        self.assertTrue(
            self.stack.is_empty(),
            "When calling is_empty for a stack with no objects, it should return True."
        )


    def test_is_empty_with_one_object(self):
        """stack.is_empty returns False for a stack with one object. (1p)"""

        #​​​​‌‌‌​‌‌‌‌‌​ Add an integer to the stack
        self.stack.push(1)

        self.assertFalse(
            self.stack.is_empty(),
            "When calling is_empty for a stack with one object, it should return False."
        )


    def test_top_with_one_object(self):
        """stack.top returns but does not remove the previously added object. (1p)"""

        operation = Operation("Search for stones")
        self.stack.push(operation)

        #​​​​‌‌‌​‌‌‌‌‌​ This should now be the operation object
        top_value = self.stack.top()

        self.assertIs(
            top_value,
            operation,
            "After adding {0!r} to the stack, top() should return {0!r}, not {1!r}"
            .format(operation, top_value)
        )

        #​​​​‌‌‌​‌‌‌‌‌​ The top method should not remove objects.
        self.assertFalse(
            self.stack.is_empty(),
            "When calling is_empty for a stack with one object, it should return False."
        )


    def test_pop_with_one_object(self):
        """stack.pop returns and removes the previously added object. (1p)"""

        operation = Operation("Build a stone wall")
        self.stack.push(operation)

        self.assertFalse(
            self.stack.is_empty(),
            "When calling is_empty for a stack with one object, it should return False."
        )

        #​​​​‌‌‌​‌‌‌‌‌​ Finished building a wall, remove the operation from the stack
        pop_value = self.stack.pop()

        self.assertIs(
            pop_value,
            operation,
            "After adding {0!r} to the stack, pop() should return {0!r}, not {1!r}"
            .format(operation, pop_value)
        )

        self.assertTrue(
            self.stack.is_empty(),
            "When calling is_empty for a stack with no objects, it should return True."
        )


    def test_stack_with_three_objects(self):
        """After pushing 3 objects to the stack, calling pop 3 times leaves the stack empty. (2p)"""

        self.assertTrue(
            self.stack.is_empty(),
            "When calling is_empty for a stack with no objects, it should return True."
        )

        #​​​​‌‌‌​‌‌‌‌‌​ Lets add three different operations
        operations = (
            Operation("Search for stones"),
            Operation("Build a stone wall"),
            Operation("Paint the wall")
        )
        for op in reversed(operations):
            self.stack.push(op)

        for i, op in enumerate(operations):
            top_value = self.stack.top()
            self.assertIs(
                top_value,
                op,
                "top() should return {0!r}, not {1!r}"
                .format(op, top_value)
            )

            self.assertFalse(
                self.stack.is_empty(),
                "After pushing three items to the stack and then calling {:d} times pop(), is_empty() should return False, not True."
                .format(i)
            )
            pop_value = self.stack.pop()
            self.assertIs(
                pop_value,
                op,
                "pop() should return {0!r}, not {1!r}"
                .format(op, pop_value)
            )

        #​​​​‌‌‌​‌‌‌‌‌​ The stack should now be empty
        self.assertTrue(
            self.stack.is_empty(),
            "After pushing three items to the stack and then calling three times pop(), is_empty() should return True, not False."
        )


if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​ Run the tests
    unittest.main(verbosity=2)

