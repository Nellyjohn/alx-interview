#!/usr/bin/python3
"""
This is a module that determines if a number of locked boxes can be opened
"""


def canUnlockAll(boxes):
    """Doc function"""
    n = len(boxes)
    opened_boxes = [False] * n

    queue = [0]
    opened_boxes[0] = True

    while queue:
        current_box = queue.pop(0)

        for key in boxes[current_box]:
            if key < n and not opened_boxes[key]:
                opened_boxes[key] = True
                queue.append(key)

    return all(opened_boxes)
