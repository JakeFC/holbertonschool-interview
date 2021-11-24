#!/usr/bin/python3
"""Module for minOperations function"""


def minOperations(n):
    """Returns the minimum number of operations needed to print H n times"""
    if (n < 1):
        return 0
    if (n == 1):
        return 1

    def CopyAll(current):
        """Copies the current number of H characters and runs Paste"""
        return 1 + Paste(current, current)

    def Paste(current, copied):
        """Pastes the copied number of H characters and recursively runs
        Paste or CopyAll"""
        current += copied
        if (current == n):
            return 1
        if (current > n):
            return 0
        return 1 + (CopyAll(current) or Paste(current, copied))
    return CopyAll(1)
