# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest

from linkedlist import LinkedList


class Fruit:
    """
    Arbitrary class for testing purposes.
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Fruit({0!r})".format(self.name)


class TestLinkedList(unittest.TestCase):

    #​​​​‌‌‌​‌‌‌‌‌​ setUp methods in a TestCase will be run once before every test method.
    def setUp(self):
        self.linked_list = LinkedList()


    def test_add_first_with_one_object(self):
        """get_position returns the object that is added with add_first. (1p)"""

        kiwi = Fruit("Kiwi")
        self.linked_list.add_first(kiwi)

        #​​​​‌‌‌​‌‌‌‌‌​ Now the linked list should have one Fruit object with the name 'Kiwi' stored
        first_node = self.linked_list.get_position(0)

        #​​​​‌‌‌​‌‌‌‌‌​ assertIs compares that two objects have the same id
        #​​​​‌‌‌​‌‌‌‌‌​ If the linked list would create and return a new Fruit("Kiwi"),
        #​​​​‌‌‌​‌‌‌‌‌​ this test would fail
        self.assertIs(
            kiwi,
            first_node,
            "The returned object is not the same object that was added."
        )


    def test_add_last_with_one_object(self):
        """get_position returns the object that is added with add_last. (1p)"""

        a = 9001
        self.linked_list.add_last(a)

        #​​​​‌‌‌​‌‌‌‌‌​ Now the linked list should have one integer with the value 9001 stored
        first_node = self.linked_list.get_position(0)

        self.assertIs(
            a,
            first_node,
            "The returned object is not the same object that was added."
        )


    def test_add_position_with_three_objects(self):
        """add_position adds objects in correct positions. (1p)"""

        apple = Fruit("Apple")
        orange = Fruit("Orange")
        banana = Fruit("Banana")

        self.linked_list.add_first(banana)
        self.linked_list.add_first(apple)

        #​​​​‌‌‌​‌‌‌‌‌​ They should now be in the following order:
        #​​​​‌‌‌​‌‌‌‌‌​ 0: Apple, 1: Banana

        #​​​​‌‌‌​‌‌‌‌‌​ Add an orange into the middle
        self.linked_list.add_position(1, orange)

        #​​​​‌‌‌​‌‌‌‌‌​ Now the order should be
        #​​​​‌‌‌​‌‌‌‌‌​ 0: Apple, 1: Orange, 2: Banana

        first_node = self.linked_list.get_position(0)
        self.assertIs(
            apple,
            first_node,
            "The node at position 0 does not have the correct value."
        )
        second_node = self.linked_list.get_position(1)
        self.assertIs(
            orange,
            second_node,
            "The node at position 1 does not have the correct value."
        )
        last_node = self.linked_list.get_position(2)
        self.assertIs(
            banana,
            last_node,
            "The node at position 2 does not have the correct value."
        )


    def test_get_size_and_remove_position_with_one_object(self):
        """get_size and remove_position works as expected. (1p)"""

        self.assertEqual(
            0,
            self.linked_list.get_size(),
            "The size of an empty LinkedList should be zero."
        )

        self.linked_list.add_first(1)

        self.assertEqual(
            1,
            self.linked_list.get_size(),
            "The size of a LinkedList with one object should be 1."
        )

        self.linked_list.remove_position(0)

        self.assertEqual(
            0,
            self.linked_list.get_size(),
            "After adding and removing one object into an initially empty linked list, the size of the linked list should be zero"
        )

    def test_get_max(self):
        """get_max returns the biggest element in the list. (1p)"""

        self.linked_list.add_first(14)
        self.linked_list.add_first(13)
        self.linked_list.add_first(5)
        self.linked_list.add_first(-3)

        max = self.linked_list.get_max()

        self.assertEqual(
        14,
        max,
        "get_max should return 14 but instead it returns {}".format(max)
        )


if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​ Run the tests
    unittest.main(verbosity = 2)

