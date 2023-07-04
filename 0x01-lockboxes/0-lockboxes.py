#!/usr/bin/python3

def canUnlockAll(boxes):
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
        # print('in the lopop')
        # print(index,':', box_length)
        index += 1
        if (index == box_length):
            if (found_new_key is False):
                break
            index = 0
            found_new_key = False
        if keys.intersection([index]):
            if len(set(boxes[index]).difference(keys)) > 0:
                # print('differece: ', keys.difference(boxes[index]))
                # print(keys, ':', boxes[index], ' found keys')
                found_new_key = True
            keys.update(boxes[index])

    if keys.issuperset(list(range(len(boxes)))):
        # print(keys,':', list(range(len(boxes))))
        return True
    else:
        return False
