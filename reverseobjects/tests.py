# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest

from reverseobjects import reverseObjects


class TestReverseObjects(unittest.TestCase):

    def test_reversing_empty_sequence(self):
        """Reversing an empty list returns an empty list. (1p)"""
        self.assertListEqual(
            [],
            reverseObjects([]),
            "Reversing an empty list should result in an empty list."
        )

    def test_reversing_sequence_with_one_element(self):
        """Reversing a sequence with one element returns an identical list. (1p)"""

        returned_value = reverseObjects([1])
        self.assertListEqual(
            [1],
            returned_value,
            "Reversing [1] should result in [1], not {0!r}".format(returned_value)
        )

        returned_value = reverseObjects(["A"])
        self.assertEqual(
            ["A"],
            returned_value,
            "Reversing 'A' should result in ['A'], not {0!r}".format(returned_value)
        )

    def test_reversing_list_with_three_elements(self):
        """Reversing a list with three integers returns a list with the integers in reverse order. (1p)"""

        returned_value = reverseObjects([1, 2, 3])
        self.assertListEqual(
            [3, 2, 1],
            returned_value,
            "Reversing [1, 2, 3] should result in [3, 2, 1], not {0!r}".format(returned_value)
        )

    def test_reversing_string(self):
        """Reversing a string returns a list containing the characters of the string in reverse order. (1p)"""
        input_string = "AlamaailmanVasarat"
        input_reversed = "tarasaVnamliaamalA"

        returned_value = reverseObjects(input_string)

        self.assertEqual(
            input_reversed,
            ''.join(returned_value), # Makes a string of all elements in the list
            "Reversing {0!r} should return\n{1!r}\nnot\n{2!r}."
            .format(input_string, list(input_reversed), returned_value)
        )


if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​ Run the tests
    unittest.main(verbosity=2)

