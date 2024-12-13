# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
import unittest
import string

from palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_with_empty_string(self):
        """Empty strings are palindromes. (1p)"""
        self.assertTrue(is_palindrome(""))

    def test_with_length_one_strings(self):
        """Strings containing one character are palindromes. (1p)"""
        for character in string.ascii_letters:
            self.assertTrue(is_palindrome(character))

    def test_with_palindromes_and_non_palindromes(self):
        """is_palindrome returns True for a palindrome and False for a non-palindrome. (1p)"""
        palindromes = ("dad", "121", "GAATTCCTTAAG", "rats live on no evil star")
        for palindrome in palindromes:
            self.assertTrue(
                is_palindrome(palindrome),
                "{0!r} is a palindrome but your function says it is not."
                .format(palindrome)
            )

        not_palindromes = ("aabb", "12", "da", "certainly not a palindrome")
        for not_palindrome in not_palindromes:
            self.assertFalse(
                is_palindrome(not_palindrome),
                "{0!r} is not a palindrome but your function says it is."
                .format(not_palindrome)
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)


