#!/usr/bin/python3
"""Module for rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in-place"""

    if (not matrix):
        return

    start = 0
    end = len(matrix[0])

    """Mirror the array from bottom left to top right"""
    for y in range(len(matrix)):

        for x in range(start, end):

            tmp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = tmp

        start += 1

    """Mirror the array from left to right"""
    for row in matrix:
        row.reverse()
