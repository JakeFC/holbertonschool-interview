#!/usr/bin/python3
"""Module for canUnlockAll function"""


def canUnlockAll(boxes):
    """Checks if all arrays can be unlocked inside matrix"""
    if len(boxes) == 0:
        return False
    if type(boxes) is not list:
        return False
    unlock_tracker = [False] * len(boxes)
    unlock_tracker[0] = True
    unlock(boxes, 0, unlock_tracker)
    if False in unlock_tracker:
        return False
    return True


def unlock(boxes, box, unlock_tracker):
    """Unlocks box at given index and each of its keys' boxes"""
    if len(boxes[box]) == 0:
        return
    for i in boxes[box]:
        if i < len(boxes) and unlock_tracker[i] is False:
            unlock_tracker[i] = True
            unlock(boxes, i, unlock_tracker)
