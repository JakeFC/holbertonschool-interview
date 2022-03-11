#!/usr/bin/python3
"""Module for rain function"""


def rain(walls):
    """Returns integer amount of rainwater retained by walls"""

    water, left, spaces = 0, 0, 0

    for height in walls:

        if (height != 0):
            """If this is a wall"""
            if (left != 0):
                """If left has already been set, add the total water, which is the number
                of spaces between walls multiplied by the height of the lowest
                wall"""
                water += min(left, height) * spaces
            """height is the height of the new left wall"""
            left = height
            spaces = 0

        elif (left != 0):
            spaces += 1

    return water
