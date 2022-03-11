#!/usr/bin/python3
"""Module for rain function"""


def rain(walls):
    """Returns integer amount of rainwater retained by walls"""

    if walls is None:
        return

    water, left, spaces = 0, 0, 0

    for n in walls:

        if (n != 0):
            """If this is a wall"""
            if (left != 0):
                """If left has already been set, add the total water, which is the number
                of spaces between walls multiplied by the height of the lowest
                wall"""
                water += (left * spaces) if left < n else (n * spaces)
            """n is the height of the new left wall"""
            left = n
            spaces = 0

        elif (left != 0):
            spaces += 1

    return water
