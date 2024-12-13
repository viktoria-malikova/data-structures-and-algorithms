# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest

from add_plus import add_plus, array_to_list, list_to_array, create_array


def array_to_printable_string(array):
    string = ""
    for i in range(len(array)):
        string += str(array[i]) + "\n"
    return string


class TestAddPlus(unittest.TestCase):

    def test_size_1(self):
        """If size is 1, function returns ['+']"""
        size = 1
        your_answer = add_plus(['*'], size)
        self.assertEqual(['+'], your_answer, "Your function returned {}.\n Correct answer {}".format(your_answer, ['+']))

    def test_size_2(self):
        """If size is 2, function returns ['+', '+', '+', '+']"""
        size = 2
        list = ['*', '*', '*', '*']
        correct_answer = ['+', '+', '+', '+']
        your_answer = add_plus(list, size)
        self.assertEqual(correct_answer, your_answer, "Your function returned {}.\n Correct answer {}".format(your_answer, correct_answer))

    def test_size_3(self):
        """Function returns correct list for array size of 3."""
        size = 3
        orig_array = create_array(size)
        correct_array = [['+', '*', '+'], ['*', '+', '*'], ['+', '*', '+']]
        your_array = list_to_array(add_plus(array_to_list(orig_array), size), size)
        self.assertEqual(correct_array, your_array, "Your array: \n{} \n Correct array: \n{}".format(array_to_printable_string(your_array),
        array_to_printable_string(correct_array)))

    def test_size_6(self):
        """Function returns correct list for array size of 6."""
        size = 6
        orig_array = create_array(size)
        correct_array = [['+', '*', '*', '*', '*', '+'], ['*', '+', '*', '*', '+', '*'], ['*', '*', '+', '+', '*', '*'],
        ['*', '*', '+', '+', '*', '*'], ['*', '+', '*', '*', '+', '*'], ['+', '*', '*', '*', '*', '+']]
        your_array = list_to_array(add_plus(array_to_list(orig_array), size), size)
        self.assertEqual(correct_array, your_array, "Your array: \n{} \n Correct array: \n{}".format(array_to_printable_string(your_array),
        array_to_printable_string(correct_array)))

    def test_size_7(self):
        """Function returns correct list for array size of 7."""
        size = 7
        orig_array = create_array(size)
        correct_array = [['+', '*', '*', '*', '*', '*', '+'], ['*', '+', '*', '*', '*', '+', '*'], ['*', '*', '+', '*', '+', '*', '*'], ['*', '*', '*', '+', '*', '*', '*'],
        ['*', '*', '+', '*', '+', '*', '*'], ['*', '+', '*', '*', '*', '+', '*'], ['+', '*', '*', '*', '*', '*', '+']]
        your_array = list_to_array(add_plus(array_to_list(orig_array), size), size)
        self.assertEqual(correct_array, your_array, "Your array: \n{} \n Correct array: \n{}".format(array_to_printable_string(your_array),
        array_to_printable_string(correct_array)))


if __name__ == "__main__":
    unittest.main(verbosity=2)

