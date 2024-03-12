def canUnlockAll(boxes):
    if not boxes:
        return False

    visited = set()
    queue = [0]  # Start with the first box (box 0)

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                queue.append(key)

    return len(visited) == len(boxes)
