# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the is_palindrome function here below

def is_palindrome(string):
    """If parameter string is a palindrome, return True, else False."""
    #raise NotImplementedError("What is palindrome, baby don't hurt me, no more.")
    return string == string[::-1]

