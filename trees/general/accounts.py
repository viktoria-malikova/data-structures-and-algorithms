# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
from decimal import Decimal


class AccountNode:
    """
    A general tree node representing one account.
    """
    def __init__(self, key, value=None):
        self.key = key
        #​​​​‌‌‌​‌‌‌‌‌​ The Decimal class provides accurate storage and
        #​​​​‌‌‌​‌‌‌‌‌​ arithmetics of floating point
        #​​​​‌‌‌​‌‌‌‌‌​ numbers without rounding errors.
        self.value = Decimal(str(value)) if value else None
        self.left_child = None
        self.right_sibling = None

    def height(self):
        """
        Return the height of self by calculating the height of its children.
        """
        if self.left_child is None:
            return 0
        if self.left_child.right_sibling is None:
            return 1 + self.left_child.height()
        return 1 + max(self.left_child.height(), self.left_child.right_sibling.height())

    def __repr__(self):
        if self.value:
            return "<AccountNode: key={0}, value={1:.2f}>".format(self.key, self.value)
        else:
            return "<AccountNode: key={0}, value=None>".format(self.key)


class AccountTree:
    """
    A general tree representing accounts and subaccounts using AccountNode objects.
    """
    def __init__(self):
        self.root = None

    def insert(self, new_key, new_value, parent_key=None, left_sibling_key=None):
        """
        Insert a new node with new_key and value as the child of the node with key
        parent_key and as the right_sibling of the node with the key left_sibling_key.
        """
        if self.find(new_key) is not None:
            raise RuntimeError("Account with key {} already exists.".format(new_key))

        new_node = AccountNode(new_key, new_value)

        if parent_key is None:
            #​​​​‌‌‌​‌‌‌‌‌​ Insert as the new root
            old_root, self.root = self.root, new_node
            new_node.left_child = old_root
            return new_node

        if left_sibling_key is None:
            #​​​​‌‌‌​‌‌‌‌‌​ Insert as the new left child of node with parent_key
            parent_node = self[parent_key]
            old_left = parent_node.left_child
            new_node.right_sibling = old_left
            parent_node.left_child = new_node
            return new_node

        #​​​​‌‌‌​‌‌‌‌‌​ Insert as the child of node with key parent_key and between
        #​​​​‌‌‌​‌‌‌‌‌​ the node with key left_sibling_key and its right sibling
        parent_node = self[parent_key]
        left_sibling = self.find(left_sibling_key, parent_node)
        if left_sibling is None:
            raise KeyError("Node with key {0} is not a child of a node with key {1}.".format(left_sibling_key, parent_key))
        old_right = left_sibling.right_sibling
        left_sibling.right_sibling = new_node
        new_node.right_sibling = old_right

        return new_node

    def find(self, key, root=None):
        """
        Return node with key or None if a matching node is not found.
        If root is None start searching at self.root, else start searching
        at root.
        """
        if root is None:
            root = self.root
        for node in self._visit_preorder(root):
            if node.key == key:
                return node
        return None

    def clear_totals(self):
        """
        Set the 'value' attribute of each internal node to None.
        """
        for node in self._visit_preorder(self.root):
            if node.left_child:
                node.value = None

    def update_totals(self):
        """
        Set the 'value' attribute of each internal node to the sum of its
        childrens' values.
        The sum is represented as a Decimal instance.
        """
        def total(node):
            if node is None:
                return Decimal('0')
            node_value = node.value if node.value is not None else Decimal('0')
            return node_value + total(node.right_sibling)

        for node in self._visit_postorder(self.root):
            if node.value is not None:
                continue
            elif node.left_child is None:
                raise RuntimeError(
                    "The AccountTree should not contain leafs with None values." +
                    "The node at key {0!r} has a value of None.".format(node.key)
                )
            else:
                node.value = total(node.left_child)


    #​​​​‌‌‌​‌‌‌‌‌​ Implement the traversal methods below

    #​​​​‌‌‌​‌‌‌‌‌​ Exercise 5.2.6
    def _visit_preorder(self, node):
        """
        Return a list of nodes in preorder starting from node.
        """
        if node is None:
            return
        #raise NotImplementedError("_visit_preorder not implemented")

        lst = []

        def traversePreOrder(node):
            if node is not None:
                lst.append(node)
                traversePreOrder(node.left_child)
                traversePreOrder(node.right_sibling)

        traversePreOrder(node)
        return lst

    #​​​​‌‌‌​‌‌‌‌‌​ Exercise 5.2.7
    #​​​​‌‌‌​‌‌‌‌‌​ NOTE: You don't need to implement _visit_postorder to get full points
    #​​​​‌‌‌​‌‌‌‌‌​ from exercise 5.2.6.
    #​​​​‌‌‌​‌‌‌‌‌​ If you remove or comment out the NotImplementedError,
    #​​​​‌‌‌​‌‌‌‌‌​ the local tests will assume you have implemented this method
    #​​​​‌‌‌​‌‌‌‌‌​ and runs all tests related to this method.
    def _visit_postorder(self, node):
        """
        Return a list of nodes in postorder starting from node.
        """
        if node is None:
            return

        lst = []

        def traversePostOrder(node):
            if node is not None:
                traversePostOrder(node.left_child)
                traversePostOrder(node.right_sibling)
                lst.append(node.value)

        traversePostOrder(node)
        return lst

        #raise NotImplementedError("_visit_postorder not implemented")

    #​​​​‌‌‌​‌‌‌‌‌​ Implement the traversal methods above


    def __getitem__(self, key):
        """
        Get accounts by key, e.g. tree[key].
        """
        node = self.find(key)
        if node is None:
            raise KeyError("No account with id {}".format(key))
        return node

    def _traverse(self, iterator):
        if self.root is None:
            return
        for node in iterator(self.root):
            yield (node.key, node.value)

    def _str(self, iterator):
        report_string = "{0} {1:>7}\n".format("Account", "Value")
        report_string += (len(report_string) + 1)*'-'

        for key, value in iterator:
            report_string += '\n'
            if value is None:
                report_string += "{0} {1:>10}".format(key, "-")
            else:
                report_string += "{0} {1:+12.2f}".format(key, value)

        return report_string

    def view_str(self):
        """
        Return a printable table of this tree.
        """
        return self._str(self._traverse(self._visit_preorder))

    def report_str(self):
        """
        Return a printable table of the financial report of this tree.
        """
        self.clear_totals()
        self.update_totals()
        return self._str(self._traverse(self._visit_postorder))

