#!/usr/bin/python3
""" Island Perimeter Module """


def island_perimeter(grid):
    """returns the perimeter of the island in grid"""
    island_height = len(grid)
    island_width = len(grid[0])
    visited = []
    processing_queue = []
    perimeter = 0

    # step1: find a square of the island
    row, column = find_island(grid, island_height, island_width)
    visited.append((row, column))
    processing_queue.append((row, column))

    # step2: use DFS to visit each square land in the is_land
    # and calculate the perimeter
    while len(processing_queue) != 0:
        row, column = processing_queue.pop()
        # for y, x in [(up), (down),(left), (right)]
        for y, x in [(row-1, column),
                     (row+1, column), (row, column-1), (row, column+1)]:
            if y < 0 or y == island_height or x < 0\
                    or x == island_width or grid[y][x] == 0:
                perimeter += 1
            elif grid[y][x] == 1 and (y, x) not in visited:
                visited.append((y, x))
                processing_queue.append((y, x))
    return perimeter


def find_island(grid, island_height, island_width):
    "returns the location of the first patch of land (1) in a sea of zeros (0)"
    for row in range(island_height):
        for column in range(island_width):
            if grid[row][column] == 1:
                return row, column
