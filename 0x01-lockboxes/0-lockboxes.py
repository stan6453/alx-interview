#!/usr/bin/python3
"""Lockbox Solution"""

def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    if (type(boxes) is not list):
        return False
    if (len(boxes) == 1):
        return True

    boxes = boxes.copy()
    keys = set(boxes[0])
    keys.add(0)
    box_length = len(boxes)
    found_new_key = False
    index = 0

    while True:
        index += 1
        if (index == box_length):
            if (found_new_key is False):
                break
            index = 0
            found_new_key = False
        if keys.intersection([index]):
            if len(set(boxes[index]).difference(keys)) > 0:
                found_new_key = True
                keys.update(boxes[index])

    if keys.issuperset(list(range(len(boxes)))):
        return True
    else:
        return False
