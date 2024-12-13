# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
import math
from power import power

class TestPower(unittest.TestCase):

    def test_power(self):
        """Testing power with base numbers 2-7 and exponents 2-7. (20p)"""
        base_numbers = [2,3,4,5,6,7]
        exponents = [2,3,4,5,6,7]
        for base in base_numbers:
            for exponent in exponents:
                your_answer = power(base, exponent)
                correct_answer = math.pow(base, exponent)
                self.assertEqual(correct_answer, your_answer, """With base: {} and exponent {}
                your function returned {}. \nCorrect answer is {}""".format(base, exponent, your_answer, correct_answer))

if __name__ == "__main__":
    unittest.main()

