#!/usr/bin/python3
"""Module for rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in-place"""

    if (not matrix):
        return

    for y in range(len(matrix)):

        for x in range(len(matrix[0])):

            tmp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = tmp

    for row in matrix:
        row.reverse()
