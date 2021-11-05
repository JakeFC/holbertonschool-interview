#!/usr/bin/python3
"""Module for canUnlockAll function"""

import time

unlock_tracker = []


def canUnlockAll(boxes):
    """Checks if all arrays can be unlocked inside matrix"""
    if len(boxes) == 0:
        return False
    if type(boxes) is not list:
        return False
    global unlock_tracker
    unlock_tracker = [False] * len(boxes)
    unlock_tracker[0] = True
    unlock(boxes, 0)
    time.sleep(0.5)
    if False in unlock_tracker:
        return False
    return True


def unlock(boxes, box):
    """Unlocks box at given index and each of its keys' boxes"""
    if len(boxes[box]) == 0:
        return
    for i in boxes[box]:
        if i < len(boxes) and unlock_tracker[i] is False:
            unlock_tracker[i] = True
            unlock(boxes, i)
