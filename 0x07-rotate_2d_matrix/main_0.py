#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 5, 6],
              [4, 5, 6, 7, 8, 8],
              [7, 8, 9, 10, 11, 12],
              [34, 90, 45, 78, 4, 5],
              [12, 15, 17, 20, 45, 76],
              [600, 500, 400, 300, 200, 100]]

    rotate_2d_matrix(matrix)
    print(matrix)
