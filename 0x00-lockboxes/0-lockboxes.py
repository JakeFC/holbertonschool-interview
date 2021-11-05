#!/usr/bin/python3
"""Module for canUnlockAll function"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened in matrix of key lists"""
    unlocked = [0]
    for box in unlocked:
        for key in boxes[box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
