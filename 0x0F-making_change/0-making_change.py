#!/usr/bin/python3
"""Module for makeChange function"""


def makeChange(coins, total):
    """Determines the fewest number of coints needed to meet the
    given amount."""

    if (total < 0):
        return 0

    quantity = 0
    coins.sort(reverse=True)

    for coin in coins:
        """From biggest to smallest, find the largest number of each coin
        that can go into total and subtract their value."""
        quantity += total // coin
        total %= coin

    if (total > 0):
        """If total wasn't exactly matched, return -1"""
        return -1

    return quantity
