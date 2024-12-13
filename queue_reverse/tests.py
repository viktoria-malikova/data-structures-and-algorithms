# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
"""
These local tests can be used to test your implementation of the nof_primes function.

Feel free to modify these tests as you wish.
"""

import unittest
import random
from queue import Queue
from queue_reverse import reverse_queue


class TestQueueReverse(unittest.TestCase):
    """
    Unit tests for the method queue_reverse.
    """

    def setUp(self):
        self.queue = Queue()

    def test_with_empty_queue(self):
        """reverse_queue doesn't error with empty queue. (1p)"""
        reverse_queue(self.queue)


    def test_with_small_numbers(self):
        """reverse_queue reverses a queue with small list of integers correctly (1p)"""

        imitation_list = [i for i in range(10, -1, -1)] # list from 10 to 0

        for i in range(11): # queue from 0 to 10
            self.queue.enqueue(i)

        reverse_queue(self.queue)

        for i in range(10):
            first = self.queue.first() # get the value of the object
            self.assertEqual(
                imitation_list[i],
                first,
                "After reversing the queue, first() should return {0!r}, not {1!r}"
                .format(imitation_list[i], first)
            )

            self.queue.dequeue() # remove the first value

    def test_with_double_reverse(self):
        """reverse_queue reverses a queue twice correctly (1p)"""

        imitation_list = [i for i in range(11)] # list from 0 to 10

        for i in range(11): # queue from 0 to 10
            self.queue.enqueue(i)

        reverse_queue(self.queue)
        reverse_queue(self.queue)   # queue should now be from 0 to 10

        for i in range(11):
            first = self.queue.first() # get the value of the object
            self.assertEqual(
                imitation_list[i],
                first,
                "After double reversing the queue, first() should return {0!r}, not {1!r}"
                .format(imitation_list[i], first)
            )

            self.queue.dequeue() # remove the first value

if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​ Run the tests
    unittest.main(verbosity = 2)

