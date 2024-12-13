# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
"""
These local tests can be used to test your implementation of the nof_primes_revised function.

Feel free to modify these tests as you wish.
"""
import unittest

from primes_revised import nof_primes_revised


class TestPrimes(unittest.TestCase):


    def test_1_nof_primes_revised_revised_with_empty_list(self):
        """nof_primes_revised_revised returns 0 for an empty list (1p) """

        values = []
        ret = nof_primes_revised(values)
        self.assertEqual(
            ret, 0,
            "Function should return 0, but your function returns {:d}".format(ret))


    def test_2_nof_primes_revised_revised_with_only_primes(self):
        """nof_primes_revised returns 10 for a list with only prime numbers (1p) """

        values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        ret = nof_primes_revised(values)
        self.assertEqual(
            ret, 10,
            "Function should return 10, but your function returns {:d}".format(ret))


    def test_3_nof_primes_revised_with_no_primes(self):
        """nof_primes_revised returns 0 for a list with no prime numbers (1p) """

        values = [-1, 0, 1, 4, 6, 8, 9, 10, 12, 14]
        ret = nof_primes_revised(values)
        self.assertEqual(
            ret, 0,
            "Function should return 0, but your function returns {:d}".format(ret))


    def test_4_nof_primes_revised_with_random_list(self):
        """nof_primes_revised returns 5 for a random list (1p) """

        values = [2, -1, 3, 0, 5, 1, 7, 4, 11, 6]
        ret = nof_primes_revised(values)
        self.assertEqual(
        ret, 5,
        "Function should return 5, but your function returns {:d}".format(ret))


    def test_5_nof_primes_revised_with_small_set(self):
        """nof_primes_revised returns 8 for a list in range [0, 20] (1p) """

        values = [i for i in range (21)]
        ret = nof_primes_revised(values)
        self.assertEqual(
        ret, 8,
        "Function should return 8, but your function returns {:d}".format(ret))


    def test_6_nof_primes_revised_with_large_set(self):
        """nof_primes_revised returns 8 for a list in range [0, 50] (1p) """

        values = [i for i in range (51)]
        ret = nof_primes_revised(values)
        self.assertEqual(
        ret, 15,
        "Function should return 15, but your function returns {:d}".format(ret))


#​​​​‌‌‌​‌‌‌‌‌​ The if checks below prevent the tests from being run if this file is for example imported
#​​​​‌‌‌​‌‌‌‌‌​ True when running tests from the command line or the Eclipse PyDev unittest tool
if __name__ in ("__main__", "tests"):
    import sys
    #​​​​‌‌‌​‌‌‌‌‌​ If this test is being run with a Python version that is older than version 3,
    #​​​​‌‌‌​‌‌‌‌‌​ raise an exception. This skips the tests.
    if sys.version_info.major < 3:
        class VersionError(BaseException): pass
        raise VersionError("You are using Python version {:d}.{:d}, please use version 3 instead."
                           .format(sys.version_info.major, sys.version_info.minor))


#​​​​‌‌‌​‌‌‌‌‌​ True when running tests from the command line
if __name__ == "__main__":
    #​​​​‌‌‌​‌‌‌‌‌​ Run the tests with increased output verbosity.
    #​​​​‌‌‌​‌‌‌‌‌​ You can change the verbosity to for example 1 and see what happens.
    unittest.main(verbosity = 2)

