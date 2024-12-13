# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest

from queue import Queue


class Customer:
    """
    Arbitrary customer class for testing purposes.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Customer({0!r})".format(self.name)


class TestQueue(unittest.TestCase):
    """
    Unit tests for the class Queue.
    """

    def setUp(self):
        self.queue = Queue()

    def test_is_empty_with_one_object(self):
        """queue.is_empty returns True for a new queue and False if it contains one object. (1p)"""

        #​​​​‌‌‌​‌‌‌‌‌​ Remember that setUp has just been called and self.queue should be equal to queue()
        self.assertTrue(
            self.queue.is_empty(),
            "When calling is_empty for a queue with no objects, it should return True."
        )

        #​​​​‌‌‌​‌‌‌‌‌​ Add an integer to the queue
        self.queue.enqueue(1)

        self.assertFalse(
            self.queue.is_empty(),
            "When calling is_empty for a queue with one object, it should return False."
        )


    def test_first_with_one_object(self):
        """queue.first returns but does not remove the previously added object. (1p)"""

        customer = Customer("Angry customer")
        self.queue.enqueue(customer)

        #​​​​‌‌‌​‌‌‌‌‌​ This should now be the customer object
        first_value = self.queue.first()

        self.assertIs(
            customer,
            first_value,
            "After adding {0!r} to the queue, first() should return {0!r}, not {1!r}"
            .format(customer, first_value)
        )

        #​​​​‌‌‌​‌‌‌‌‌​ The first method should not remove objects.
        self.assertFalse(
            self.queue.is_empty(),
            "When calling is_empty for a queue with one object, it should return False."
        )


    def test_dequeue_with_one_object(self):
        """queue.dequeue returns and removes the previously added object. (1p)"""

        customer = Customer("Angry customer")
        self.queue.enqueue(customer)

        self.assertFalse(
            self.queue.is_empty(),
            "When calling is_empty for a queue with one object, it should return False."
        )

        #​​​​‌‌‌​‌‌‌‌‌​ The customer has now been served, remove him from the queue
        dequeue_value = self.queue.dequeue()

        self.assertIs(
            customer,
            dequeue_value,
            "After adding {0!r} to the queue, dequeue() should return {0!r}, not {1!r}"
            .format(customer, dequeue_value)
        )

        self.assertTrue(
            self.queue.is_empty(),
            "When calling is_empty for a queue with no objects, it should return True."
        )


    def test_queue_with_three_objects(self):
        """After enqueueing 3 objects to the queue, calling dequeue 3 times leaves the queue empty. (2p)"""

        self.assertTrue(
            self.queue.is_empty(),
            "When calling is_empty for a queue with no objects, it should return True."
        )

        #​​​​‌‌‌​‌‌‌‌‌​ Let's add three customers
        customers = (
            Customer("First Customer"),
            Customer("Second Customer"),
            Customer("Last Customer")
        )

        for cust in customers:
            self.queue.enqueue(cust)

        for i, cust in enumerate(customers):

            first_value = self.queue.first()
            self.assertIs(
                cust,
                first_value,
                "first() should return {0!r}, not {1!r}"
                .format(cust, first_value)
            )

            last_value = self.queue.last()
            last_model_value = customers[-1]
            self.assertIs(
                last_model_value,
                last_value,
                "last() should return {0!r}, not {1!r}"
                .format(last_model_value, last_value)

            )

            self.assertFalse(
                self.queue.is_empty(),
                "After enqueueing three items to the queue and then calling {:d} times dequeue(), is_empty() should return False, not True."
                .format(i + 1)
            )

            dequeue_value = self.queue.dequeue()   # dequeue the first customer
            self.assertIs(
                cust,
                dequeue_value,
                "dequeue() should return {0!r}, not {1!r}"
                .format(cust, dequeue_value)
            )

        #​​​​‌‌‌​‌‌‌‌‌​ The queue should now be empty
        self.assertTrue(
            self.queue.is_empty(),
            "After enqueueing three items to the queue and then calling three times dequeue(), is_empty() should return True, not False."
        )


if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​ Run the tests
    unittest.main(verbosity = 2)

