#!/usr/bin/python3
""" Island Perimeter Module """


def island_perimeter(grid):
    """returns the perimeter of the island in grid"""
    island_height = len(grid)
    island_width = len(grid[0])
    visited = []
    processing_stack = []
    perimeter = 0

    # step1: find a square of the island
    row, column = find_island(grid, island_height, island_width)
    if (row, column) == (-1, -1):
        return 0
    visited.append((row, column))
    processing_stack.append((row, column))

    # step2: use DFS to visit each square of land in the is_land
    # and calculate the perimeter
    while len(processing_stack) != 0:
        row, column = processing_stack.pop()
        # for y, x in [(up), (down),(left), (right)]
        for y, x in [(row-1, column),
                     (row+1, column), (row, column-1), (row, column+1)]:
            if y < 0 or y == island_height or x < 0\
                    or x == island_width or grid[y][x] == 0:
                perimeter += 1
            elif grid[y][x] == 1 and (y, x) not in visited:
                visited.append((y, x))
                processing_stack.append((y, x))
    return perimeter


def find_island(grid, island_height, island_width):
    """returns the (row, column) coordinate of the first patch of land
    returns (-1, -1) for the (row, column) coordinates if no island is found"""
    for row in range(island_height):
        for column in range(island_width):
            if grid[row][column] == 1:
                return row, column
    return (-1, -1)
