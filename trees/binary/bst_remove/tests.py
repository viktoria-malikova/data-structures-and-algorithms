# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286

import unittest
import random
from bst import BST


class TestBSTRemove(unittest.TestCase):
    def setUp(self):
        self.tree = BST()

    def _assertBSTProperty(self):
        """Assert that self.tree is a binary search tree."""
        previous_key = None
        for key in self.tree:
            if previous_key:
                self.assertLessEqual(
                    previous_key,
                    key,
                    "An inorder traversal of the tree should iterate the keys of the tree in sorted ascending order.\n\n" +
                    "(Assuming BST.__iter__ yields the keys of the tree in inorder.)"
                )
            previous_key = key

    def test1_has_all_attributes(self):
        """The BST has all required methods. (0p)"""
        method_names = (
            "find",
            "insert",
            "remove",
            "__iter__"
        )
        for attr in method_names:
            self.assertTrue(
                hasattr(BST, attr),
                "BST should have the method {0} but hasattr(BST, \"{0}\") returned False."
                .format(attr)
            )

    def test2_remove_from_empty_tree(self):
        """Removing a node from an empty tree returns None. (1p)"""
        removed = self.tree.remove(0)
        self.assertIsNone(removed, ("Attempting to remove the key 0 from a "
            "tree with no nodes should return None, not {}.").format(removed))

    def test3_remove_nonexisting_node(self):
        """Removing a node which does not exist returns an unchanged tree. (1p)"""
        self.tree.insert(1)
        removed = self.tree.remove(0)
        self.assertEqual(removed, self.tree.root, ("Attempting to remove the key 0 "
            "from a tree which does not contain a node with the key 0 should "
            "return root, not {}.".format(removed))
        )

    def test4_remove_existing_one(self):
        """For a tree with one node, calling remove with the key of that node removes it from the tree and returns the object. (1p)"""
        self.tree.insert(1)
        removed = self.tree.remove(1)
        self.assertIsNone(removed, ("After calling insert(1), calling remove(1) "
            "should return None as the root. However, it returned {}.")
            .format(removed))

        self.assertIsNone(self.tree.root, ("After removing one node from a "
            "tree containing one node, the root of the tree should be None, "
            "not {}.").format(self.tree.root)
        )

    def test5_remove_decreases_count(self):
        """Removing an existing node decreases the node counter. (1p)"""
        self.tree.insert(1)
        self.tree.insert(2)
        self.assertEqual(
            self.tree.nodes,
            2,
            "After inserting two nodes into an initially empty tree, the node counter was {} instead of 2."
            .format(self.tree.nodes)
        )
        self.tree.remove(1)
        self.assertEqual(
            self.tree.nodes,
            1,
            "After inserting two nodes into an initially empty tree and then removing one, the node counter was {} instead of 1."
            .format(self.tree.nodes)
        )


    def test7_remove_root_of_tree_with_three_nodes(self):
        """Removing the root of a tree containing three nodes replaces the root in the tree. (1p)"""

        #​​​​‌‌‌​‌‌‌‌‌​   2             1
        #​​​​‌‌‌​‌‌‌‌‌​  / \    ---->    \
        #​​​​‌‌‌​‌‌‌‌‌​ 1   3             3

        keys = [2, 1, 3]
        for k in keys:
            self.tree.insert(k)
        self.tree.remove(2)

        new_root = self.tree.root
        self.assertEqual(new_root.key, 1, "After inserting keys [2, 1, 3] and "
            "then deleting 2, the root should have key 1.")

        self.assertIsNone(new_root.left, "After inserting keys [2, 1, 3] and "
            "then deleting 2, the root should have empty left child.")

        self.assertIsNotNone(new_root.right, "After inserting keys [2, 1, 3] "
            "and then deleting 2, the root should have nonempty left child.")

        self.assertEqual(new_root.right.key, 3,
            "After inserting keys [2, 1, 3] and then deleting 2, the root "
            "should have key 3 at its right child.")


    def test8_remove_random(self):
        """After inserting a random amount of random integer keys and then removing a random amount of random integer keys, the tree should retain the binary search tree property. (2p)"""

        keys = random.sample(range(100), random.randint(5, 50))
        inserted = set(self.tree.insert(key) for key in keys)
        remove_count = random.randint(0, len(inserted))
        for _, node in zip(range(remove_count), inserted):
            self.tree.remove(node.key)
            self._assertBSTProperty()


if __name__ == '__main__':
    unittest.main(verbosity=2)

