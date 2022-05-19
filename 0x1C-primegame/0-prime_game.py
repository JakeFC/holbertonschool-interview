#!/usr/bin/python3
"""Module for isWinner function"""


def isWinner(x, nums):
    """Returns the winner of prime game between Maria and Ben, with x number
    of rounds and nums being an array of ranges within which to choose prime
    numbers."""

    maria, ben, primes = 0, 0, 0
    factors = []

    for i in range(x):
        for n in range(2, nums[i] + 1, 2):
            """Prime numbers start on 2 and are odd"""

            for f in factors:
                if n % f is 0:
                    break
            else:
                factors.append(n)
                primes += 1
                """Any seen prime numbers are factors. Our first number
                starting on 2 will always be prime."""
                
        if primes % 2 is 0:
            ben += 1
        else:
            maria += 1
        primes = 0
        factors = []

    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"
