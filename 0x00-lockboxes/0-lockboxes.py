#!/usr/bin/python3
"""Module for canUnlockAll function"""

unlock_tracker = []


def canUnlockAll(boxes):
    """Checks if all arrays can be unlocked inside matrix"""
    if not boxes:
        return False
    global unlock_tracker
    unlock_tracker = [False] * len(boxes)
    unlock_tracker[0] = True
    Unlock(boxes, 0)
    if False in unlock_tracker:
        return False
    return True


def Unlock(boxes, box):
    """Unlocks box at given index and each of its keys' boxes"""
    if len(boxes[box]) == 0:
        return
    for i in boxes[box]:
        if i < len(boxes) and unlock_tracker[i] is False:
            unlock_tracker[i] = True
            Unlock(boxes, i)
