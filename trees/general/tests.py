# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
import inspect
from accounts import AccountNode, AccountTree


class Test1AccountTree(unittest.TestCase):

    def setUp(self):
        self.tree = AccountTree()

    def test1_find_none(self):
        """Searching in an empty tree returns None. (1p)"""
        for key in range(10):
            self.assertIsNone(self.tree.find(key))

    def test2_find_one(self):
        """Searching for an existing node returns the node. (1p)"""
        self.tree.root = AccountNode(1, 1.0)
        self.assertIs(
            self.tree.find(1),
            self.tree.root,
            "Calling find with a key that exists in the tree should return the node with that key."
        )

    def test3_find_two(self):
        """Searching for an existing node in a tree with two nodes returns the node which is being searched for. (1p)"""
        self.tree.root = AccountNode(1, 1.0)
        self.tree.root.left_child = AccountNode(2, 1.0)
        self.assertIs(
            self.tree.find(1),
            self.tree.root,
            "Calling find with a key {} that exists in the tree should return the node with that key."
            .format(1)
        )
        self.assertIs(
            self.tree.find(2),
            self.tree.root.left_child,
            "Calling find with a key {} that exists in the tree should return the node with that key."
            .format(2)
        )

    def test4_find_three(self):
        """Searching for an existing node in a tree with four nodes returns the node which is being searched for. (1p)"""
        nodes = [AccountNode(i, 1.0) for i in range(1, 5)]
        self.tree.root = nodes[0]
        nodes[0].left_child = nodes[1]
        nodes[1].right_sibling = nodes[2]
        nodes[2].left_child = nodes[3]
        for k in range(1, 5):
            self.assertIs(
                self.tree.find(k),
                nodes[k-1],
                "Calling find with a key {} that exists in the tree should return the node with that key."
                .format(k)
            )

    def test5_insert_root(self):
        """Inserting a new key and value into an empty tree sets a new node as the root. (1p)"""
        A = self.tree.insert(1, 1.0)
        self.assertIs(
            self.tree.root,
            A,
            "Inserting a node into an empty tree should set it as the root."
        )

    def test6_insert_root_left_child(self):
        """Inserting a new key and value into a tree with one root sets a new node as the child of the root. (1p)"""
        self.tree.insert(1, 1.0)
        B = self.tree.insert(2, 1.0, 1)
        self.assertIs(
            self.tree.root.left_child,
            B,
            "Inserting a node specifying its parent to be the root should set the node as the new left child of the root."
        )

    def test7_insert_root_left_child_right_sibling(self):
        """Inserting a new key and value into a tree with two nodes sets a new node as the right sibling of the left child of the root. (1p)"""
        self.tree.insert(1, 1.0)
        self.tree.insert(2, 1.0, 1)
        C = self.tree.insert(3, 1.0, 1, 2)
        self.assertIs(
            self.tree.root.left_child.right_sibling,
            C,
            "Inserting a node specifying its parent to be the root and the left sibling to be the left child of the root should set the node as the new right sibling of the left child of the root."
        )


class Test2PreOrder(unittest.TestCase):

    def setUp(self):
        self.tree = AccountTree()

    def test2_view_str_shows_accounts_in_order(self):
        """Calling view_str for a tree with the accounts as in the course material picture returns the a table with the accounts sorted into ascending order. (2p)"""
        self.tree.root = get_test_tree_root()
        table = self.tree.view_str()
        all_account_keys = [line[0] for line in map(str.split, table.splitlines()[2:])]
        correct_order = sorted(all_account_keys)
        if all_account_keys != correct_order:
            self.fail(
                "A preorder traversal of the tree seen in the course material should result in a table where the keys are in sorted ascending order.\n\n" +
                "The correct order is\n{}".format(' '.join(correct_order)) + '\n'
                "not\n{}".format(' '.join(all_account_keys)) + '\n\n'
                "Calling view_str returned the table:\n{}".format(table)
        )


def postorder_not_implemented():
    try:
        next(AccountTree()._visit_postorder('not None'))
    except NotImplementedError:
        return True
    except:
        pass
    return False


@unittest.skipIf(postorder_not_implemented(), 'AccountTree._visit_postorder not implemented')
class Test3PostOrder(unittest.TestCase):

    def setUp(self):
        self.tree = AccountTree()

    def test2_report_str_shows_accounts_in_order(self):
        """Calling report_str for a tree with the accounts as in the course material picture returns the a table with the accounts in postorder. (2p)"""
        self.tree.root = get_test_tree_root()
        table = self.tree.report_str()
        all_account_keys = ' '.join(line[0] for line in map(str.split, table.splitlines()[2:]))
        correct_order = ' '.join((
            "1110", "1120", "1100", "1211", "1212", "1213", "1210", "1220", "1200", "1000",
            "2110", "2120", "2100", "2210", "2220", "2230", "2200", "2000", "0000"
        ))
        if all_account_keys != correct_order:
            self.fail(
                "A postorder traversal of the tree seen in the course material should result in a table where the keys are in postorder.\n\n" +
                "The correct order is\n{}".format(correct_order) + '\n'
                "not\n{}".format(all_account_keys) + '\n\n'
                "Calling report_str returned the table:\n{}".format(table)
        )


def get_test_tree_root():
    #​​​​‌‌‌​‌‌‌‌‌​ A makeshift solution to manually construct the example tree seen in the course content.
    #​​​​‌‌‌​‌‌‌‌‌​ A probably more proper way to do this would be to expand the insert functionality
    #​​​​‌‌‌​‌‌‌‌‌​ of the AccountTree to find the correct position for a new node depending
    #​​​​‌‌‌​‌‌‌‌‌​ on how the new key to be inserted relates to existing keys.
    root = AccountNode("0000")
    A = AccountNode(1000)
    B = AccountNode(1100)
    C = AccountNode(1110, 2184.0)
    D = AccountNode(1120, 600.0)
    E = AccountNode(1200)
    F = AccountNode(1210)
    G = AccountNode(1211, 3200.0)
    H = AccountNode(1212, 500.0)
    I = AccountNode(1213, 100.0)
    J = AccountNode(1220, 700.0)
    K = AccountNode(2000)
    L = AccountNode(2100)
    M = AccountNode(2110, -2571.0)
    N = AccountNode(2120, -201.0)
    O = AccountNode(2200)
    P = AccountNode(2210, -1971.0)
    Q = AccountNode(2220, -2458.0)
    R = AccountNode(2230, -500.0)

    root.left_child = A
    A.left_child = B
    B.left_child = C
    C.right_sibling = D
    B.right_sibling = E
    E.left_child = F
    F.left_child = G
    G.right_sibling = H
    H.right_sibling = I
    F.right_sibling = J
    A.right_sibling = K
    K.left_child = L
    L.left_child = M
    M.right_sibling = N
    L.right_sibling = O
    O.left_child = P
    P.right_sibling = Q
    Q.right_sibling = R

    return root


if __name__ == "__main__":
    unittest.main(verbosity=2)

