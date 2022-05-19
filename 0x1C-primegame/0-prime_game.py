#!/usr/bin/python3
"""Module for isWinner function"""


def isWinner(x, nums):
    """Returns the winner of prime game between Maria and Ben, with x number
    of rounds and nums being an array of ranges within which to choose prime
    numbers."""

    maria, ben, primes, maxFactor = 0, 0, 0, 0
    maxFactors = [3, 10, 31, 100]

    for i in range(x):
        max = nums[i]

        """The maximum factor for a non-prime number within a range is
        the square root of the maximum number. Short of a sqrt function,
        these are values pre-set for number of digits"""
        if max / 10 <= 1:
            maxFactor = maxFactors[0]
        elif max / 10 <= 10:
            maxFactor = maxFactors[1]
        elif max / 10 <= 100:
            maxFactor = maxFactors[2]
        elif max / 10 <= 1000:
            maxFactor = maxFactors[3]

        for n in range(2, max + 1):
            """Prime numbers start on 2"""
            for f in range(2, maxFactor):
                """Factors for non-prime numbers start on 2"""
                if n % f is 0:
                    break
            else:
                primes += 1
        if primes % 2 is 0:
            ben += 1
        else:
            maria += 1
        primes = 0
    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"
