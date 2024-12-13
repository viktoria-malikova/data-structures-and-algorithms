# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
'''
In this exercise, you are given an implementation of a binary search tree.
    The class ``BST``, found in the exercise package, contains the methods
    ``insert`` and ``find`` which can be used for inserting and finding key-value
    pairs.
    These methods utilize two recursive helper methods ``_inserthelp`` and
    ``_findhelp`` to work properly.
    Your task is to implement these helper methods.
    In addition, you should implement the method ``_visit_inorder`` which returns
    an iterator yielding the nodes of the tree in inorder.
    You do not need to change the code outside these 3 methods to get full
    points.
    '''

class BSTNode:
    """
    Represents nodes in a binary search tree.
    """
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def height(self):
        """Return the height of this node."""
        left_height = 1 + self.left.height() if self.left else 0
        right_height = 1 + self.right.height() if self.right else 0
        return max(left_height, right_height)

    def __repr__(self):
        return "<BSTNode: key={!r}, value={!r}, id={}>".format(self.key, self.value, id(self))


class BSTException(Exception):
    pass


class BST:
    """
    Simple recursive binary search tree implementation.
    """
    def __init__(self, NodeClass=BSTNode):
        self.BSTNode = NodeClass
        self.root = None
        self.nodes = 0
        #​​​​‌‌‌​‌‌‌‌‌​ Updated after each call to insert
        self.newest_node = None
        self.table = list()

    def find(self, find_key):
        """Return node with key find_key if it exists. If not, return None. """
        return self._findhelp(self.root, find_key)

    def insert(self, new_key, value=None):
        """Insert a new node with key new_key into this BST,
        increase node count by one and return the inserted node."""
        if self.find(new_key) is not None:
            raise KeyError("This BST already contains key {0!r}".format(new_key))
        self.root = self._inserthelp(self.root, new_key, value)
        self.nodes += 1
        return self.newest_node

    def height(self):
        """Return the height of this tree."""
        return self.root.height() if self.root else -1

    def __iter__(self):
        """Return an iterator of the keys of this tree in sorted order."""
        for node in self._visit_inorder(self.root):
            yield node.key

    def __len__(self):
        return self.nodes


    #​​​​‌‌‌​‌‌‌‌‌​ Implement the methods below.

    def _findhelp(self, node, find_key):
        """Starting from node, search for node with key find_key and return that node.
        If no node with key find_key exists, return None."""
        if node is None or find_key == node.key:
            # ​​​​‌‌‌​‌‌‌‌‌​ End search
            return node
        else:
            if find_key < node.key:
                return self._findhelp(node.left, find_key)
            else:
                return self._findhelp(node.right, find_key)
        # ​​​​‌‌‌​‌‌‌‌‌​ Implement functionality to recursively choose the next node


    def _inserthelp(self, node, new_key, value):
        """Starting from node, find an empty spot for the new node and
        insert it into this BST."""
        if node is None:
            #​​​​‌‌‌​‌‌‌‌‌​ Found an empty spot, create a new node
            self.newest_node = self.BSTNode(new_key, value)
            return self.newest_node
        else:
        #​​​​‌‌‌​‌‌‌‌‌​ Implement functionality to recursively insert nodes
            if new_key <= node.key:
                node.left = self._inserthelp(node.left, new_key, value)
            else:
                node.right = self._inserthelp(node.right, new_key, value)
        return node

    def _visit_inorder(self, node):
        """Return an iterator of the nodes of this tree in inorder starting at node."""
        if node is None:
            return
        else:
            self._visit_inorder(node.left)
            self.table.append(node)
            self._visit_inorder(node.right)
            # ​​​​‌‌‌​‌‌‌‌‌​ Implement this method to return an iterator (a list will do also)
            # ​​​​‌‌‌​‌‌‌‌‌​ yielding the nodes of this tree in inorder.
        return self.table

    