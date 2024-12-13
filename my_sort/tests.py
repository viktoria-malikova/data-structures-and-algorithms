# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
import random

from my_sort import my_sort


class TestMySort(unittest.TestCase):
    def _test_sort(self, lst):
        sorted_list = my_sort(lst[:])
        correct_answer = sorted(lst)
        self.assertListEqual(
            sorted_list,
            correct_answer,
            "Your function did not return the list given as parameter sorted."
        )

    def test1_empty(self):
        """Sorting an empty list returns an empty list. (0p)"""
        self._test_sort([])

    def test2_one(self):
        """Sorting a list with one value returns a list with that value. (0p)"""
        for i in range(-1, 2):
            self._test_sort([i])

    def test3_10_already_sorted(self):
        """Sorting a sorted list with 10 elements returns the list sorted. (1p)"""
        self._test_sort(list(range(10)))

    def test4_10_unique(self):
        """Sorting a list with 10 unique integers in random order returns a list with the integers sorted. (1p)"""
        self._test_sort(random.sample(range(100), 10))

    def test5_10_with_duplicates(self):
        """Sorting a list with 10 integers containing only integers 0, 1 or 2 returns the list sorted. (1p)"""
        self._test_sort([random.randint(0,2) for _ in range(10)])

    def test6_100_already_sorted(self):
        """Sorting a sorted list with 100 elements returns the list sorted. (2p)"""
        self._test_sort(list(range(100)))

    def test7_100_reverse_sorted(self):
        """Sorting a reversed sorted list with 100 elements returns the list sorted. (2p)"""
        self._test_sort(list(range(100, 0, -1)))

    def test8_100_unique(self):
        """Sorting a list with 100 unique integers in random order returns a list with the integers sorted. (2p)"""
        self._test_sort(random.sample(range(1000), 100))

    def test9_100_with_duplicates(self):
        """Sorting a list with 100 integers containing only integers 0, 1 or 2 returns the list sorted. (2p)"""
        self._test_sort([random.randint(0,2) for _ in range(100)])


if __name__ == "__main__":
    unittest.main(verbosity=2)

