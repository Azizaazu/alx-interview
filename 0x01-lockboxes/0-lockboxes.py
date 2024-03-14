#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""

def canUnlockAll(boxes):
    """Determines if boxes can be unlocked
    boxes: prameter
    return: True or False

    """
    if not boxes or type(boxes) is not list:
        return False

    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                queue.append(key)

    if len(visited) == len(boxes):
        return True
    return False
