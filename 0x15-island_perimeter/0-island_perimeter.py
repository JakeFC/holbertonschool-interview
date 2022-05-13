#!/usr/bin/python3
"""Module for island_perimeter function"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""

    p = 0
    lenY = len(grid)
    lenX = len(grid[0])

    for y in range(lenY):
        for x in range(lenX):
            if grid[y][x] == 0:
                continue
            p += 4
            if y != 0 and grid[y - 1][x] == 1:
                p -= 1
            if y != lenY - 1 and grid[y + 1][x] == 1:
                p -= 1
            if x != 0 and grid[y][x - 1] == 1:
                p -= 1
            if x != lenX - 1 and grid[y][x + 1] == 1:
                p -= 1
    return p
