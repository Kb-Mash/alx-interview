#!/usr/bin/python3
""" module contains method that finds the keys to open other lockboxes """


def canUnlockAll(boxes):
    """
    Function that determines if you can open all the lockboxes
    Args:
        boxes: list of lists of integers
    Returns:
        True if you can open all the lockboxes, False otherwise
    """
    opened = [0]
    for box in opened:
        for key in boxes[box]:
            if key not in opened and key < len(boxes):
                opened.append(key)
    if len(boxes) == len(opened):
        return True
    return False
