#!/usr/bin/python3
"""rotate an n x n 2D matrix by 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    length = len(matrix)
    # STEP1: transpose the matrix
    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse the matrix so that it can be 90 degs
    for row in range(length):
        for col in range(length//2):
            matrix[row][col], matrix[row][length-1-col] =\
                matrix[row][length-1-col], matrix[row][col]
