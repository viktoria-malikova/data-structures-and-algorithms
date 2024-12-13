# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
from circles_and_squares import count_circles_and_squares

class TestCirclesAndSquares(unittest.TestCase):

    def test_length_0_8(self):
        """If length is 0.8 function returns 0, 0. (10p)"""
        length = 0.8
        circles, squares = count_circles_and_squares(length, 0, 0)
        self.assertEqual(circles, 0, "You returned {} circles, correct answer: 0".format(circles))
        self.assertEqual(squares, 0, "You returned {} squares, correct answer: 0".format(squares))

    def test_1_circle(self):
        """If there's no room for square, function returns 1 circle. (10p)"""
        length = 1.1
        circles, squares = count_circles_and_squares(length, 0, 0)
        self.assertEqual(circles, 1, "You returned {} circles, correct answer: 1".format(circles))
        self.assertEqual(squares, 0, "You returned {} squares, correct answer: 0".format(squares))

    def test_two_basic_cases(self):
        """Test two basic cases. (10p)"""
        length1 = 2
        length2 = 4
        circles, squares = count_circles_and_squares(length1, 0, 0)
        self.assertEqual(circles, 3, "You returned {} circles, correct answer: 3".format(circles))
        self.assertEqual(squares, 2, "You returned {} squares, correct answer: 2".format(squares))
        circles, squares = count_circles_and_squares(length2, 0, 0)
        self.assertEqual(circles, 5, "You returned {} circles, correct answer: 5".format(circles))
        self.assertEqual(squares, 4, "You returned {} squares, correct answer: 4".format(squares))

if __name__ == "__main__":
    unittest.main(verbosity=2)

