# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import re
'''
Start by familiarizing yourself with the classes ``ExpressionTree`` and
    ``ETNode``, which are included in the exercise package.
    ``ExpressionTree`` is a binary tree which can be used to convert
    postfix expressions into infix format. The conversion takes place by first
    building a binary tree from the operators and operands of the postfix
    exression. After the tree is complete, the infix version of the original
    expression can be obtained by traversing the nodes of the tree using an
    inorder traversal.

    The class ``ExpressionTree`` is almost ready, but it lacks the method
    used to traverse the nodes in correct order. Your task is to implement the
    required functionality into the method ``_visit_inorder`` so that it
    returns a list of the values of the tree nodes
    in inorder. Remember also to add parentheses at correct positions.
    Even though the parentheses would be trivial, for example ``((1*2)+3)``,
    they should still be added for every operator. This is of course a bit
    redundant, but it simplifies the task.

'''
class ETNode:
    """
    Simple binary tree node with a value and both left and right pointers.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class ExpressionTree:
    """
    Simple binary expression tree capable of parsing postfix expressions
    and returning infix expressions.
    """
    #​​​​‌‌‌​‌‌‌‌‌​ Supported operators
    OPERATORS = {'+', '-', '*', '/'}

    def __init__(self):
        self.root = None
        self._stack = list()


    def construct_from_postfix(self, expression):
        """Construct the expression tree by parsing the given expression string."""
        if not expression:
            return

        #​​​​‌‌‌​‌‌‌‌‌​ Iterate over the string 'expression' inserting elements into the tree,
        #​​​​‌‌‌​‌‌‌‌‌​ while skipping spaces
        operators = re.escape(''.join(self.OPERATORS))
        pattern = r"\w+|[{}]".format(operators)
        for match in re.finditer(pattern, expression):
            element = match.group(0)
            self._insert(element)

        if not self._stack:
            raise RuntimeError("There is no root operator after inserting {!r} into the tree.".format(expression))

        #​​​​‌‌‌​‌‌‌‌‌​ Set the last operator as the root
        self.root = self._stack.pop()

        if self._stack:
            raise RuntimeError("The expression stack should be empty after evaluating all characters from the expression: {!r}.".format(expression))


    def _insert(self, value):
        """Insert operand or operator 'value' into this tree."""
        if value not in self.OPERATORS:
            #​​​​‌‌‌​‌‌‌‌‌​ value is an operand
            self._stack.append(ETNode(value))
            return

        if not self._stack:
            #​​​​‌‌‌​‌‌‌‌‌​ value is an operator but there's nothing in the stack to operate on
            raise RuntimeError("Cannot add operator {!r}, the expression stack is empty.".format(value))

        #​​​​‌‌‌​‌‌‌‌‌​ Merge subtrees from stack with operator as their new root
        operator = ETNode(value)
        operator.right = self._stack.pop()
        operator.left = self._stack.pop()
        self._stack.append(operator)


    def as_infix(self):
        """Return the infix representation of the current tree as a string."""
        return ''.join(map(str, self._visit_inorder()))


    #​​​​‌‌‌​‌‌‌‌‌​ Write your solution below, there's no need to change anything
    #​​​​‌‌‌​‌‌‌‌‌​ outside this method to get full points.
    def _visit_inorder(self, starting_node=None):
        """Return a list containing the values of the visited nodes while adding parentheses to retain operator precedence."""
        if starting_node is None:
            starting_node = self.root

        lst = list()

        def inorder(node):
            if node is not None:
                if node.value in self.OPERATORS:
                    lst.append("(")
                inorder(node.left)
                lst.append(node.value)
                inorder(node.right)
                if node.value in self.OPERATORS:
                    lst.append(")")

        inorder(starting_node)
        return lst