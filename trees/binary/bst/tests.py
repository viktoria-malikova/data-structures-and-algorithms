# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
import math
import random
from bst import BST, BSTNode


class Test1BSTNode(unittest.TestCase):
    def test1_empty_node_init(self):
        """BSTNodes are initialized with key, value, left and right instance variables. (0p)"""
        node = BSTNode(1)
        self.assertEqual(node.key, 1)
        self.assertIsNone(node.value)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
        node = BSTNode(1, 'a')
        self.assertEqual(node.value, 'a')

    def test2_single_node_height(self):
        """The height of a BSTNode with no children is 0. (0p)"""
        node = BSTNode(1)
        self.assertEqual(node.height(), 0)

    def test3_node_height_one_child(self):
        """The height of a BSTNode with one child is 1 and the height of that child is 0. (0p)"""
        node = BSTNode(1)
        node.left = BSTNode(2)
        self.assertEqual(node.height(), 1)
        self.assertEqual(node.left.height(), 0)

    def test4_node_height_uneven_subtrees(self):
        """The height of a BSTNode with subtrees of uneven heights is the height of the taller subtree plus one. (0p)"""
        node = BSTNode(1)
        node.left = BSTNode(2)
        node.left.left = BSTNode(3)
        self.assertEqual(
            node.left.height(),
            1,
            "Expected the height of a node with one child, which is a leaf, to be 1 but it was not."
        )
        node.right = BSTNode(4)
        self.assertEqual(
            node.right.height(),
            0,
            "Expected the height of a leaf to be 0 but it was not."
        )
        self.assertEqual(
            node.height(),
            node.left.height()+1,
            "Expected the height of a node with two children, left and right, of which right is a leaf and left has one child, which is a leaf, to be the height of left plus one but it was not."
        )


class Test2EmptyBST(unittest.TestCase):
    def setUp(self):
        self.tree = BST()

    def test1_bst_init_node_class(self):
        """BSTs are initialized with a node class. (0p)."""
        self.assertIs(
            self.tree.BSTNode,
            BSTNode,
            "When no node class is specified, the BST should use the class BSTNode as the node class."
        )

    def test2_empty_size(self):
        """An empty BST has a size equal to zero. (0p)"""
        tree_size = len(self.tree)
        self.assertEqual(
            0,
            tree_size,
            "Calling len on a tree containing no nodes should return 0, not {}"
            .format(tree_size)
        )

    def test3_empty_find(self):
        """Searching for a key in an empty BST returns None. (0p)"""
        self.assertIsNone(
            self.tree.find(1),
            "Calling find in an empty BST should return None."
        )

    def test4_empty_insert(self):
        """Calling insert on an empty tree returns the inserted node and adds it to the tree. (0p)"""
        new_key = 1
        new_value = "value"

        inserted_node = self.tree.insert(new_key, new_value)
        self.assertIsInstance(
            inserted_node,
            BSTNode,
            "tree.insert should return an instance of BSTNode, not {0!r}."
            .format(inserted_node)
        )
        self.assertEqual(
            inserted_node.key,
            new_key,
            "Calling tree.insert({0}, {1}) should return a node with the key {0}, not {2}."
            .format(new_key, new_value, inserted_node.key)
        )
        self.assertIs(
            inserted_node.value,
            new_value,
            "Calling tree.insert({0}, {1}) should return a node with the value {1}, not {2}."
            .format(new_key, new_value, inserted_node.value)
        )

        tree_size = len(self.tree)
        self.assertEqual(
            tree_size,
            1,
            "Calling len on a tree containing one key should return 1, not {}"
            .format(tree_size)
        )

    def test5_find_one(self):
        """Calling find for a node which exists should return that node. (1p)"""
        node = BSTNode(2)
        node.left = BSTNode(1)
        node.right = BSTNode(3)
        self.tree.root = node

        for node in (node, node.left, node.right):
            found_node = self.tree.find(node.key)
            self.assertIs(
                found_node,
                node,
                "If {0!r} exists in tree, calling tree.find({1}) should return that node, not {2!r}"
                .format(node, node.key, found_node)
            )


class Test3TenNodesBST(unittest.TestCase):

    def setUp(self):
        self.tree = BST()
        self.keys = random.sample(range(1, 11), 10)

    def test1_insert_ten_nodes(self):
        """Inserting ten nodes into a BST should increase its size by ten. (1p)"""
        for key in self.keys:
            inserted_node = self.tree.insert(key)
            self.assertIsInstance(
                inserted_node,
                BSTNode,
                "tree.insert should return an instance of BSTNode, not {0!r}."
                .format(inserted_node)
            )
            self.assertEqual(
                inserted_node.key,
                key,
                "Calling tree.insert({0}) should return a node with the key {0}, not {1}."
                .format(key, inserted_node.key)
            )

        correct_size = len(self.keys)
        returned_size = len(self.tree)

        self.assertEqual(
            correct_size,
            returned_size,
            "Calling len on a tree with {0} nodes should return {0}, not {1}"
            .format(correct_size, returned_size)
        )


    def test2_find_ten_nodes(self):
        """All keys which have been inserted should be found by the find method. (1p)"""
        for key in self.keys:
            self.tree.insert(key)

        for key in self.keys:
            returned_node = self.tree.find(key)
            self.assertIsNotNone(
                returned_node,
                "Calling find for an existing key {0} should return the node holding the key, not None"
                .format(key)
            )
            self.assertEqual(
                returned_node.key,
                key,
                "Calling find for an existing key {0} should return the node holding the key, not {1!r}."
                .format(key, returned_node)
            )


class Test4BSTProperty(unittest.TestCase):
    """
    Test that the implemented BST methods do not break the binary search tree property.
    """
    def setUp(self):
        self.tree = BST()

    def test1_smaller_values_go_left(self):
        """Adding values in sorted descending order creates internal nodes with only left children. (1p)"""
        #​​​​‌‌‌​‌‌‌‌‌​ Insert nodes with keys 10, 9, 8, ... , 1
        for key in range(10, 0, -1):
            self.tree.insert(key)

        #​​​​‌‌‌​‌‌‌‌‌​ Starting from the root, traverse down towards the leaf, checking
        #​​​​‌‌‌​‌‌‌‌‌​ both children of each node
        node = self.tree.root
        for key in range(10, 1, -1):
            self.assertEqual(
                key,
                node.key,
                "After inserting keys in range 10, 9, ... , 2, 1 and then iterating in that range, expected the keys of all the left nodes starting from the root follow this sequence, but a node {0} with the key {1} was found."
                .format(node, node.key)
            )
            #​​​​‌‌‌​‌‌‌‌‌​ There should not be a right child
            self.assertIsNone(
                node.right,
                "Adding keys in order 10, 9, .. , 2, 1 should not create nodes with right children, but a node {0} with a right child {1} was found."
                .format(node, node.right)
            )
            #​​​​‌‌‌​‌‌‌‌‌​ There should be a left child
            self.assertIsNotNone(
                node.left,
                "Adding keys in order 10, 9, .. , 2, 1 should only create nodes with left children, but a node {0} with no left child was found."
                .format(node)
            )
            #​​​​‌‌‌​‌‌‌‌‌​ Go left to next node
            node = node.left

        #​​​​‌‌‌​‌‌‌‌‌​ The last node is a leaf
        self.assertIsNone(
            node.left,
            "After adding nodes in range 10, 9, ... , 2, 1, the node with key 1 should be a leaf, but it had a left child {0}."
            .format(node.left)
        )
        self.assertIsNone(
            node.right,
            "After adding nodes in range 10, 9, ... , 1, the node with key 1 should be a leaf, but it had a right child {0}."
            .format(node.right)
        )


    def test2_larger_values_go_right(self):
        """Adding values in sorted ascending order creates internal nodes with only right children. (1p)"""
        #​​​​‌‌‌​‌‌‌‌‌​ Insert nodes with keys 1, 2, ... , 10
        for key in range(1, 11):
            self.tree.insert(key)

        #​​​​‌‌‌​‌‌‌‌‌​ Starting from the root, traverse down towards the leaf, checking
        #​​​​‌‌‌​‌‌‌‌‌​ both children of each node
        node = self.tree.root
        for key in range(1, 10):
            self.assertEqual(
                key,
                node.key,
                "After inserting keys in range 1, 2, ... , 9, 10 and then iterating in that range, expected the keys of all the right nodes starting from the root to follow this sequence, but a node {0} with the key {1} was found."
                .format(node, node.key)
            )
            #​​​​‌‌‌​‌‌‌‌‌​ There should not be a left child
            self.assertIsNone(
                node.left,
                "Adding keys in order 1, 2, ... , 9, 10 should not create nodes with left children, but a node {0} with a left child {1} was found."
                .format(node, node.left)
            )
            #​​​​‌‌‌​‌‌‌‌‌​ There should be a right child
            self.assertIsNotNone(
                node.right,
                "Adding keys in order 1, 2, ... , 9, 10 should only create nodes with right children, but a node {0} with no right child was found."
                .format(node)
            )
            #​​​​‌‌‌​‌‌‌‌‌​ Go right to the next node
            node = node.right

        #​​​​‌‌‌​‌‌‌‌‌​ The last node is a leaf
        self.assertIsNone(
            node.left,
            "After adding nodes in range 1, 2, ... , 9, 10, the node with key 10 should be a leaf, but it had a left child {0}."
            .format(node.left)
        )
        self.assertIsNone(
            node.right,
            "After adding nodes in range 1, 2, ... , 9, 10, the node with key 10 should be a leaf, but it had a left child {0}."
            .format(node.right)
        )


    def test3_inorder_traversal(self):
        """An inorder traversal visits all nodes in the tree. (1p)"""
        keys = random.sample(range(100), 20)
        inserted = set(self.tree.insert(key) for key in keys)
        visited = set(self.tree._visit_inorder(self.tree.root))

        self.assertSetEqual(
            visited,
            inserted,
            "An inorder traversal should return all nodes which have been added to the tree.\n" +
            "_visit_inorder did not visit the nodes seen above although they were inserted into the tree."
        )


    def test4_iter_tree_keys(self):
        """Iterating the tree yields the keys of the tree in sorted ascending order. (1p)"""
        keys = random.sample(range(100), 20)
        for key in keys:
            self.tree.insert(key)

        #​​​​‌‌‌​‌‌‌‌‌​ Shorter form of [key for key in self.tree]
        #​​​​‌‌‌​‌‌‌‌‌​ (which is possible because the class BST implements the method __iter__)
        visited = list(self.tree)
        #​​​​‌‌‌​‌‌‌‌‌​ The returned values should be in sorted ascending order
        correct_order = sorted(keys)

        self.assertListEqual(
            visited,
            correct_order,
            "Calling __iter__ should return an iterator of the keys of the BST in sorted ascending order.\n" +
            "Note: the traversal method should not care in what order the nodes appear, if the insert method is implemented correctly, an inorder traversal will yield the keys in sorted order."
        )


    def test5_height_complete_tree(self):
        """The height of a complete tree with n nodes is log_2(n+1) - 1. (1p)"""
        #​​​​‌‌‌​‌‌‌‌‌​ Add keys so they form a complete tree
        keys = [50, 25, 75, 20, 30, 70, 80]
        for key in keys:
            self.tree.insert(key)

        tree_size = len(self.tree)
        added_count = len(keys)
        self.assertEqual(
            tree_size,
            added_count,
            "Adding {0} keys to an initially empty tree, calling len on the tree should return {0}, not {1}."
            .format(added_count, tree_size)
        )

        #​​​​‌‌‌​‌‌‌‌‌​ math.log returns float
        self.assertAlmostEqual(
            float(self.tree.height()),
            math.log(len(keys) + 1, 2) - 1,
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)


