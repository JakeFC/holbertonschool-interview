#!/usr/bin/python3
"""Module for isWinner function"""


def isWinner(x, nums):
    """Returns the winner of prime game between Maria and Ben, with x number
    of rounds and nums being an array of ranges within which to choose prime
    numbers."""

    maria, ben, primes = 0, 0, 0
    factors, winners = [], ['b', 'b', 'm']
    """Winners array is pre-filled for values 0-2"""
    current = 'm'

    maxN = max(nums)
    for n in range(3, maxN + 1, 2):
        """All prime numbers after 2 are odd. Evens can be skipped"""

        if (n % 5 == 0 and n != 5):
            """Multiples of 5 aren't prime and can be skipped"""
            winners += [current] * 2
            continue
        for f in factors:
            if n % f is 0:
                """Any number divisible by a found factor isn't prime"""
                winners += [current] * 2
                break
        else:
            factors.append(n)
            """Any seen prime numbers are factors."""
            current = 'b' if current == 'm' else 'm'
            """Change current winner on finding a prime number"""
            winners += [current] * 2

    for i in range(x):
        for n in nums:
            if winners[n] == 'b':
                ben += 1
            else:
                maria += 1

    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"
