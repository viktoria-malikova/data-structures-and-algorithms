# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
"""
These local tests can be used to test your implementation of the sieve_of_eratosthenes function
Feel free to modify these tests as you wish
"""

import unittest
from eratosthenes import sieve_of_eratosthenes

class TestSieveOfEratosthenes(unittest.TestCase):
    #​​​​‌‌‌​‌‌‌‌‌​ All methods starting with 'test' in a TestCase will be run as tests

    def test_with_small_numbers(self):
        """Sieve_of_eratosthenes returns 1 for n = 2"""

        #​​​​‌‌‌​‌‌‌‌‌​ Test with first 2 positive numbers
        n = 2
        ret = sieve_of_eratosthenes(n)
        #​​​​‌‌‌​‌‌‌‌‌​ Check that sieve_of_eratosthenes returns the correct amount of prime numbers
        self.assertEqual(
        ret, 1,
        #​​​​‌‌‌​‌‌‌‌‌​ The message below is shown if the test fails
        #​​​​‌‌‌​‌‌‌‌‌​ In this case when sieve_of_eratosthenes returns something else than 1
        "Function should return 1, but your function returns {:d}".format(ret))

    def test_with_negative_numbers(self):
        """Sieve_of_eratosthenes returns 0 for n < 2"""

        #​​​​‌‌‌​‌‌‌‌‌​ Test with negative numbers
        n = -10
        ret = sieve_of_eratosthenes(n)
        #​​​​‌‌‌​‌‌‌‌‌​ Check that sieve_of_eratosthenes returns the correct amount of prime numbers
        self.assertEqual(
        ret, 0,
        #​​​​‌‌‌​‌‌‌‌‌​ The message below is shown if the test fails
        #​​​​‌‌‌​‌‌‌‌‌​ In this case when sieve_of_eratosthenes returns something else than 0
        "Function should return 0, but your function returns {:d}".format(ret))

    def test_with_small_set(self):
        """Sieve_of_eratosthenes returns 10 for n = 30"""

        #​​​​‌‌‌​‌‌‌‌‌​ Test with first 30 numbers
        n = 30
        ret = sieve_of_eratosthenes(n)
        #​​​​‌‌‌​‌‌‌‌‌​ Check that sieve_of_eratosthenes returns the correct amount of prime numbers
        self.assertEqual(
        ret, 10,
        #​​​​‌‌‌​‌‌‌‌‌​ The message below is shown if the test fails
        #​​​​‌‌‌​‌‌‌‌‌​ In this case when sieve_of_eratosthenes returns something else than 10
        "Function should return 10, but your function returns {:d}".format(ret))

    def test_with_medium_set(self):
        """Sieve_of_eratosthenes returns 19 for n = 70"""

        #​​​​‌‌‌​‌‌‌‌‌​ Test with first 70 numbers
        n = 70
        ret = sieve_of_eratosthenes(n)
        #​​​​‌‌‌​‌‌‌‌‌​ Check that sieve_of_eratosthenes returns the correct amount of prime numbers
        self.assertEqual(
        ret, 19,
        #​​​​‌‌‌​‌‌‌‌‌​ The message below is shown if the test fails
        #​​​​‌‌‌​‌‌‌‌‌​ In this case when sieve_of_eratosthenes returns something else than 19
        "Function should return 19, but your function returns {:d}".format(ret))


if __name__ in ("__main__", "tests"):
    import sys
    if sys.version_info.major < 3:
        class VersionError(BaseException): pass
        raise VersionError("You are using Python version {:d}.{:d}, please use version 3 instead."
                           .format(sys.version_info.major, sys.version_info.minor))


#​​​​‌‌‌​‌‌‌‌‌​ True when running tests from the command line
if __name__ == "__main__":
    unittest.main(verbosity = 2)

