# -*- coding: utf-8 -*-
# Nimi: Viktoria Malikova
# Opiskelijanumero: 730286
#​​​​‌‌‌​‌‌‌‌‌​ Implement the sieve_of_eratosthenes function here below

import math

def sieve_of_eratosthenes(n):

    """ Return the number of prime numbers between the range (2, n) """

    A = []
    if n < 2:
        return 0
    if n == 2:
        return 1
    else:
        for i in range(2, n):
            A.append(i)
        for i in range(2, math.sqrt(n)):
            if A[i] != 0:
                j =+ 1
                while j <= n:
                    A[j] = 0
                    j =+ 1
        p = 0
        for i in range(2, n):
            if A[i] != 0:
                A[p] = A[i]
                p =+ 1
    return len(A)-1

#​​​​‌‌‌​‌‌‌‌‌​ Driver program
def main():
    n = 10
    nof_primes = sieve_of_eratosthenes(n)
    print("The number of primes between the range (2, {:d}) is: {:d}"
        .format(n, nof_primes))

if __name__ == "__main__":
    main()

