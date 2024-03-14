#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determines if boxes can be unlocked
    boxes: prameter
    return: True or False

    """
    if not boxes or type(boxes) is not list:
        return False

    visited = [0]

    for n in visited:
        for key in boxes[n]:
            if key not in visited and key < len(boxes):
                visited.append(key)

    if len(visited) == len(boxes):
        return True
    return False
