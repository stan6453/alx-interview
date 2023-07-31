#!/usr/bin/python3
"""Nqueens solution"""
import sys


def nqueens(N, row):
    """recursive solution for nqueens problem"""
    for col in range(N):
        if place_queen_here(row, col):
            if row+1 < N:
                nqueens(N, row+1)
            else:
                print([[row, col] for row, col in enumerate(solution)])


def place_queen_here(row, col):
    """return True if queen was placed in row,col. Else return False"""
    for prev_queens_row in range(row):
        if (row - col == prev_queens_row - solution[prev_queens_row]) or\
            (col == solution[prev_queens_row]) or\
                (row + col == prev_queens_row + solution[prev_queens_row]):
            return False
    solution[row] = col
    return True


if __name__ == "__main__":
    N = None
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    # solution[row] = col (for index row, queen is place at col value)
    solution = [0] * (int(sys.argv[1]))
    nqueens(N, 0)
