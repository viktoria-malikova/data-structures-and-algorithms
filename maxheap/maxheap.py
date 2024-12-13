# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
'''
Familiarize yourself with the minheap implementation ``MaxHeap`` found in the exercise
    package.
    The class can be used for simple task prioritization using a queue.
    The task with the greatest integer has the highest priority.
    For example, in the task queue [ (1, "Do homework"), (3, "Eat), (2, "Sleep") ]
    the task "Eat" has the highest priority.

    Several of the methods needed by the max heap to work properly have not yet
    been implemented.
    Your task is to fix all the methods which contain a row with
    ``NotImplementedError``.
    '''

class MaxHeap:
    """
    A max heap implementation.
    Elements are stored internally in an array of tuples (priority, element),
    where element can be any object and priority is a comparable object.

    For example for (5, object3), (23, object2), (1, object7) the priority of
    the objects should be: object2, object3, object7.
    """

    def __init__(self, initial_data=None):
        """If initial_data is given, it should be an iterable sequence of tuples (lists of tuples are fine)."""
        if initial_data is None:
            self.clear()
        else:
            self.array = list(initial_data)
            self.size = len(self.array)

        self.buildheap()


    def clear(self):
        """Delete all elements from the heap and reset its size."""
        self.array = []
        self.size = 0


    def is_empty(self):
        return self.size == 0


    def buildheap(self):
        """Heapify the existing array."""
        #​​​​‌‌‌​‌‌‌‌‌​ Build the heap by heapifying all internal nodes,
        #​​​​‌‌‌​‌‌‌‌‌​ starting from the last internal node up to the root
        for i in range((self.size // 2) - 1, -1, -1):
            self._heapify_down(i)


    def _swap(self, i, j):
        """Swaps in-place the priority-object pairs at indexes i and j."""
        if i != j:
            self.array[j], self.array[i] = self.array[i], self.array[j]


    def _heapify_up(self, i):
        """Restore heap property from the element at i to the root."""
        while i > 0:
            #​​​​‌‌‌​‌‌‌‌‌​ Select the parent of i
            parent_index = (i - 1) // 2
            #​​​​‌‌‌​‌‌‌‌‌​ If the parent has a lower priority than i, swap parent with i
            if self._higher_priority(i, parent_index):
                self._swap(i, parent_index)
            #​​​​‌‌‌​‌‌‌‌‌​ Heapify the parent
            i = parent_index


    def _left_child(self, i):
        """Return the index of the left child of i. Return -1 if i has no left child.
        Raise an IndexError if the index i is invalid."""
        if not 0 <= i < self.size:
            raise IndexError("A node which does not exist cannot have a left child")
        return i*2 + 1 if i < self.size//2 else -1


    def _right_child(self, i):
        """Return the index of the right child of i. Return -1 if i has no right child.
        Raise an IndexError if the index i is invalid."""
        if not 0 <= i < self.size:
            raise IndexError("A node which does not exist cannot have a right child")
        return i*2 + 2 if i < (self.size-1)//2 else -1


    def _is_leaf(self, i):
        """Return False if the node at i has one or more children, else True.
        Raise an IndexError if the index i is invalid."""
        if not 0 <= i < self.size:
            raise IndexError("A node which does not exist cannot be a leaf")
        return -1 == self._left_child(i) == self._right_child(i)


    def _max_child(self, i):
        """Return the index of the child with higher priority of the element at index i.
        Raise an IndexError if the node at index i is a leaf."""
        #​​​​‌‌‌​‌‌‌‌‌​ Get indexes for the left and right child
        i_left = self._left_child(i)
        i_right = self._right_child(i)

        if -1 == i_left == i_right:
            #​​​​‌‌‌​‌‌‌‌‌​ Node i is a leaf
            raise IndexError("The node at index i has no children.")
        if -1 == i_right:
            #​​​​‌‌‌​‌‌‌‌‌​ Node i has only a left child
            return i_left

        #​​​​‌‌‌​‌‌‌‌‌​ Node i has two children
        #​​​​‌‌‌​‌‌‌‌‌​ Compare the elements and return the index with the higher priority
        return i_left if self._higher_priority(i_left, i_right) else i_right



    #​​​​‌‌‌​‌‌‌‌‌​ Implement the methods below

    def _higher_priority(self, i, j):
        """Return True if element at index i has a higher priority than the element at index j, else False."""
        if self.array[i][0] > self.array[j][0]:
            return True
        else:
            return False


    def insert(self, pair):
        """Insert a new (priority, object) pair into the heap and heapify the heap."""
        self.array.append(pair)
        self.size += 1


    def top(self):
        """Return the object at the top of the heap or None if heap is empty. """
        if self.is_empty():
            return None
        else:
            return self.array[0][1]


    def _heapify_down(self, i):
        """Restore heap property from the element at i to the last leaf."""
        while 0 <= i < self.size and not self._is_leaf(i):
            #​​​​‌‌‌​‌‌‌‌‌​ Select the child of i
            child_index = self._max_child(i)
            #​​​​‌‌‌​‌‌‌‌‌​ If the child has a lower priority than i, swap child with i
            if self._higher_priority(i, child_index):
                self._swap(i, child_index)
            #​​​​‌‌‌​‌‌‌‌‌​ Heapify the child
            i = child_index


    def pop(self):
        """Remove the pair at the top of the heap and return the removed object.
        Raises a RuntimeError if the heap is empty."""
        #​​​​‌‌‌​‌‌‌‌‌​ Raise error if the heap is empty
        if self.is_empty():
            raise RuntimeError("Cannot pop from an empty heap.")
        removed_pair = self.array.remove([0])
        return removed_pair[1]

