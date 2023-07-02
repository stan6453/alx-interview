#!/usr/bin/python3
"""Generate n sequences of the pascal triangle"""


def pascal_triangle(n):
    """returns a list of list of pascal's triangle"""
    pascal_triangle = []
    if n == 0:
        return pascal_triangle
    for num in range(n):
        pascal_triangle.append(getNextSequence(pascal_triangle))
    return pascal_triangle


def getNextSequence(arr):
    """returns a list of the next sequence in a pascal's triangle"""
    if len(arr) == 0:
        return [1]

    prevSeq = arr[len(arr) - 1]
    nextSeq = []
    length = len(prevSeq)
    prevIndex = -1
    for index in range(length):
        prevValue = 0 if prevIndex == -1 else prevSeq[prevIndex]
        nextSeq.append(prevValue + prevSeq[index])
        prevIndex += 1
    nextSeq.append(prevSeq[length - 1])
    return nextSeq
