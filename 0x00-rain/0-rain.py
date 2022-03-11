#!/usr/bin/python3
"""Module for rain function"""


def rain(walls):
    """Returns integer amount of rainwater retained by walls"""

    water, tempWater, left, leftTallest, potential, potentialSpaces, \
        spaces = 0, 0, 0, 0, 0, 0, 0

    for height in walls:

        if (height != 0):
            """If this is a wall"""
            if (left != 0):
                """Add the water, which is the number of spaces between walls
                multiplied by the height of the lowest wall"""
                tempWater += min(left, height) * spaces
                if (height < leftTallest):
                    """The highest potential water per index is the height of
                    leftTallest wall, minus height of this wall"""
                    potential += leftTallest - height
                    potentialSpaces += 1
                    if (height > left):
                        """When water rises over previous walls, tempWater should be
                        reevaluated based on potential, minus the open air
                        above"""
                        tempWater = potential - (leftTallest - height) \
                            * potentialSpaces
                else:
                    """If wall matches or is taller than leftTallest, add full potential
                    water to total and reset variables to start from new
                    tallest"""
                    water += potential
                    potential, potentialSpaces, tempWater = 0, 0, 0
                    leftTallest = height
            else:
                """Initially set leftTallest as first found wall"""
                leftTallest = height
            """height is the height of the new left wall"""
            left = height
            spaces = 0

        elif (left != 0):
            """The highest potential water where no wall exists is the
            height of leftTallest wall"""
            potential += leftTallest
            spaces += 1
            potentialSpaces += 1
    """Add any tempWater left over, as it hasn't been overridden"""
    water += tempWater

    return water
