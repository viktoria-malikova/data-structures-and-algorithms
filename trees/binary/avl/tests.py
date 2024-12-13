# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
from avl import AVL
from bst import BSTNode


class Test1AVLSingleRight(unittest.TestCase):

    def setUp(self):
        #​​​​‌‌‌​‌‌‌‌‌​ Root
        Q = BSTNode(4, "Q")
        #​​​​‌‌‌​‌‌‌‌‌​ Internal node
        P = BSTNode(2, "P")
        #​​​​‌‌‌​‌‌‌‌‌​ Leafs
        A = BSTNode(1, "A")
        B = BSTNode(3, "B")
        C = BSTNode(5, "C")

        #​​​​‌‌‌​‌‌‌‌‌​ Construct a minimal tree
        Q.left = P
        Q.right = C
        P.left = A
        P.right = B

        #​​​​‌‌‌​‌‌‌‌‌​        Q
        #​​​​‌‌‌​‌‌‌‌‌​      /   \
        #​​​​‌‌‌​‌‌‌‌‌​     P     C
        #​​​​‌‌‌​‌‌‌‌‌​   /   \
        #​​​​‌‌‌​‌‌‌‌‌​  A     B

        self.nodes = (P, Q, A, B, C)
        self.tree = AVL()


    def test1_single_right_rotation_returns_new_node(self):
        """Calling right_rotation for a node returns the new node which takes the place of the old node. (0p)"""
        P, Q = self.nodes[:2]
        self.assertIs(
            self.tree.right_rotation(Q),
            P,
            "Rotating a node {0} right should return the node which takes its place."
            .format(P)
        )


    def test2_right_rotation(self):
        """Rotating a node right moves the node down to the right and its left child up. (0p)"""
        P, Q, A, B, C = self.nodes

        #​​​​‌‌‌​‌‌‌‌‌​ Rotate the root right
        self.tree.right_rotation(Q)

        #​​​​‌‌‌​‌‌‌‌‌​ Check that the children have been switched correctly
        self.assertIs(
            P.right,
            Q,
            "Rotating {0} right should move it as the right child of its old left child, {1}"
            .format(Q, P)
        )
        self.assertIs(
            Q.left,
            B,
            "Rotating {0} right should move the right child, {1}, of its old left child, {2}, as the new left child of {0}"
            .format(Q, B, P)
        )

        #​​​​‌‌‌​‌‌‌‌‌​ Check that children that should not have been moved are still in place
        self.assertIs(
            P.left,
            A,
            "After rotating {0} right, its old left child, {1}, should have its own left child, {2}, unchanged."
            .format(Q, P, A)
        )
        self.assertIs(
            Q.right,
            C,
            "After rotating {0} right, its old right child, {1}, should be unchanged."
            .format(Q, C)
        )


    def test3_single_right_rotation_updates_height(self):
        """After rotating a node A with a single right rotation, the heights of the nodes are correct. (0p)"""
        P, Q, A, B, C = self.nodes

        self.tree.right_rotation(Q)

        expected_node_heights = [
            (A, 0),
            (B, 0),
            (C, 0),
            (P, 2),
            (Q, 1)
        ]

        for node, expected_height in expected_node_heights:
            node_height = node.height()
            self.assertEqual(
                node_height,
                expected_height,
                "The height of {0} should be {1}, not {2}."
                .format(node, expected_height, node_height)
            )



class Test2AVLSingleLeft(unittest.TestCase):

    def setUp(self):
        #​​​​‌‌‌​‌‌‌‌‌​ Root
        P = BSTNode(2, "P")
        #​​​​‌‌‌​‌‌‌‌‌​ Internal node
        Q = BSTNode(4, "Q")
        #​​​​‌‌‌​‌‌‌‌‌​ Leafs
        A = BSTNode(1, "A")
        B = BSTNode(3, "B")
        C = BSTNode(5, "C")

        #​​​​‌‌‌​‌‌‌‌‌​ Construct a minimal tree
        P.left = A
        P.right = Q
        Q.left = B
        Q.right = C

        #​​​​‌‌‌​‌‌‌‌‌​       P
        #​​​​‌‌‌​‌‌‌‌‌​     /   \
        #​​​​‌‌‌​‌‌‌‌‌​    A     Q
        #​​​​‌‌‌​‌‌‌‌‌​        /   \
        #​​​​‌‌‌​‌‌‌‌‌​       B     C

        self.nodes = (P, Q, A, B, C)
        self.tree = AVL()


    def test1_single_left_rotation_returns_new_node(self):
        """left_rotation at a node returns the new node which takes the place of the old node. (1p)"""
        P, Q = self.nodes[:2]
        self.assertIs(
            self.tree.left_rotation(P),
            Q,
            "Rotating a node {0} left should return the node which takes its place."
            .format(P)
        )


    def test2_single_left_rotation(self):
        """Rotating a node left moves the node down to the left and its right child up. (1p)"""
        P, Q, A, B, C = self.nodes

        #​​​​‌‌‌​‌‌‌‌‌​ Rotate the root left
        self.tree.left_rotation(P)

        #​​​​‌‌‌​‌‌‌‌‌​ Check that the children have been switched correctly
        self.assertIs(
            Q.left,
            P,
            "Rotating {0} left should move it as the left child of its old right child, {1}"
            .format(P, Q)
        )
        self.assertIs(
            P.right,
            B,
            "Rotating {0} left should move the left child, {1}, of its old right child, {2}, as the new right child of {0}"
            .format(P, B, Q)
        )

        #​​​​‌‌‌​‌‌‌‌‌​ Check that children that should not have been moved are still in place
        self.assertIs(
            Q.right,
            C,
            "After rotating {0} left, its old right child, {1}, should have its own right child, {2}, unchanged."
            .format(P, Q, C)
        )
        self.assertIs(
            P.left,
            A,
            "After rotating {0} left, its old left child, {1}, should be unchanged."
            .format(P, A)
        )


    def test3_single_left_rotation_updates_height(self):
        """After rotating a node A with a single left rotation, the heights of the nodes are correct. (1p)"""
        P, Q, A, B, C = self.nodes

        self.tree.left_rotation(P)

        expected_node_heights = [
            (A, 0),
            (B, 0),
            (C, 0),
            (P, 1),
            (Q, 2)
        ]

        for node, expected_height in expected_node_heights:
            node_height = node.height()
            self.assertEqual(
                node_height,
                expected_height,
                "The height of {0} should be {1}, not {2}."
                .format(node, expected_height, node_height)
            )



class Test3AVLDoubleLeftRight(unittest.TestCase):

    def setUp(self):
        A = BSTNode(3, "A")
        B = BSTNode(1, "B")
        C = BSTNode(2, "C")

        B.right = C
        A.left = B

        #​​​​‌‌‌​‌‌‌‌‌​    A
        #​​​​‌‌‌​‌‌‌‌‌​   /
        #​​​​‌‌‌​‌‌‌‌‌​  B
        #​​​​‌‌‌​‌‌‌‌‌​   \
        #​​​​‌‌‌​‌‌‌‌‌​    C

        self.tree = AVL()
        self.nodes = (A, B, C)

    def test1_double_left_right_rotation_returns_new_node(self):
        """Calling double_left_right_rotation for a node returns the new node which takes the place of the old node. (1p)"""
        A, _, C = self.nodes
        self.assertIs(
            self.tree.double_left_right_rotation(A),
            C,
            "Rotating a node {0} with a LR rotation should return the node which takes its place."
            .format(A)
        )


    def test2_double_left_right_rotation(self):
        """Rotating a node A with a double, left-right rotation moves the left child of A as the new left child of the old right child of the old left child of A. (1p)"""
        A, B, C = self.nodes

        A_new = self.tree.double_left_right_rotation(A)

        self.assertIs(
            C.left,
            B,
            "The left child of {0} should be {1}."
            .format(C.left, B)
        )
        self.assertIs(
            A_new,
            C,
            "Calling tree.double_left_right_rotation({0}) should return {1}."
            .format(A_new, C)
        )
        self.assertIs(
            C.right,
            A,
            "The right child of {0} should be {1}."
            .format(C.right, A)
        )

    def test3_double_left_right_rotation_updates_height(self):
        """After rotating a node A with a double, left-right rotation, the heights of the nodes are correct. (1p)"""
        A, B, C = self.nodes

        self.tree.double_left_right_rotation(A)

        expected_node_heights = [
            (A, 0),
            (B, 0),
            (C, 1),
        ]

        for node, expected_height in expected_node_heights:
            node_height = node.height()
            self.assertEqual(
                node_height,
                expected_height,
                "The height of {0} should be {1}, not {2}."
                .format(node, expected_height, node_height)
            )


class Test4AVLDoubleRightLeft(unittest.TestCase):

    def setUp(self):
        A = BSTNode(1, "A")
        B = BSTNode(3, "B")
        C = BSTNode(2, "C")

        B.left = C
        A.right = B

        #​​​​‌‌‌​‌‌‌‌‌​    A
        #​​​​‌‌‌​‌‌‌‌‌​     \
        #​​​​‌‌‌​‌‌‌‌‌​      B
        #​​​​‌‌‌​‌‌‌‌‌​     /
        #​​​​‌‌‌​‌‌‌‌‌​    C

        self.tree = AVL()
        self.nodes = (A, B, C)


    def test1_double_right_left_rotation_returns_new_node(self):
        """Calling double_right_left_rotation for a node returns the new node which takes the place of the old node. (1p)"""
        A, _, C = self.nodes
        self.assertIs(
            self.tree.double_right_left_rotation(A),
            C,
            "Rotating a node {0} with a RL rotation should return the node which takes its place."
            .format(A)
        )


    def test2_double_right_left_rotation(self):
        """Rotating a node A with a double, right-left rotation moves the right child of A as the new right child of the old left child of the old right child of A. (1p)"""
        A, B, C = self.nodes

        self.tree.double_right_left_rotation(A)

        self.assertIs(
            C.left,
            A,
            "The left child of {0} should be {1}."
            .format(C.left, A)
        )
        self.assertIs(
            C.right,
            B,
            "The right child of {0} should be {1}."
            .format(C.right, B)
        )


    def test3_double_right_left_rotation_updates_height(self):
        """After rotating a node A with a double, right-left rotation, the heights of the nodes are correct. (1p)"""
        A, B, C = self.nodes

        self.tree.double_right_left_rotation(A)

        expected_node_heights = [
            (A, 0),
            (B, 0),
            (C, 1),
        ]

        for node, expected_height in expected_node_heights:
            node_height = node.height()
            self.assertEqual(
                node_height,
                expected_height,
                "The height of {0} should be {1}, not {2}."
                .format(node, expected_height, node_height)
            )


if __name__ == '__main__':
    unittest.main(verbosity=2)


