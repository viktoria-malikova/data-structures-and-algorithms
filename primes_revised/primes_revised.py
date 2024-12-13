# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the nof_primes_revised function here below

def nof_primes_revised(list):
    """ Return the number of prime numbers in a list """
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for n in list:  # Iterate through the input list
        if is_prime(n):  # Check if the number is prime
            count += 1
    return count
    

