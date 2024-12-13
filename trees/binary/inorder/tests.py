# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest

from exptree import ExpressionTree


class TestInorder(unittest.TestCase):

    def setUp(self):
        self.tree = ExpressionTree()


    def _assertParsedAsInfix(self, postfix, infix, expected):
        self.assertEqual(
            infix,
            expected,
            "After parsing the postfix expression {0!r}, as_infix should return {1!r}, not {2!r}."
            .format(postfix, expected, infix)
        )

    def _test_expression(self, postfix, expected_value):
        """Test that parsing the postfix expression with the binary expression tree returns the expected value."""
        self.tree.construct_from_postfix(postfix)
        returned_value = self.tree.as_infix()
        self._assertParsedAsInfix(postfix, returned_value, expected_value)


    def test1_empty(self):
        """After inserting an empty expression, inorder traversal gives an empty expression. (1p)"""
        self.assertIsNone(self.tree.root, "An empty tree should have no root")
        self._test_expression('', '')


    def test2_simple(self):
        """After inserting the expression '1 2 +', inorder traversal gives '(1+2)'. (1p)"""
        postfix = "1 2 +"
        infix = "(1+2)"
        self._test_expression(postfix, infix)


    def test3_with_precedence(self):
        """After inserting the expression '1 2 + 3 *', inorder traversal gives '((1+2)*3)'. (1p)"""
        postfix = "1 2 + 3 *"
        infix = "((1+2)*3)"
        self._test_expression(postfix, infix)


    def test4_all_operators(self):
        """After inserting the expression 'a b + c d e - * /', inorder traversal gives '((a+b)/(c*(d-e)))'. (1p)"""
        postfix = "a b + c d e - * /"
        infix = "((a+b)/(c*(d-e)))"
        self._test_expression(postfix, infix)


if __name__ == "__main__":
    unittest.main(verbosity=2)

