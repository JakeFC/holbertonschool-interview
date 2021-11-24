#!/usr/bin/python3
"""Module for minOperations function"""


def minOperations(n):
    """Returns the minimum number of operations needed to print H n times"""
    if (n <= 1):
        return 0
    ops = 0
    m = 1
    copied = 0
    while (m != n):
        if (copied != m and n % m == 0):
            copied = m
        else:
            m += copied
        ops += 1    
    return ops
