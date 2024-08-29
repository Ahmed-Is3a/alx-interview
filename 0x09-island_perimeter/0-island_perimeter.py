#!/usr/bin/python3
"""
returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """ calculate island perimeter
    """

    row = len(grid)
    col = len(grid[0])

    if row < 1 or row > 100:
        raise ValueError("Number of rows must be between 1 and 100")
    if col < 1 or col > 100:
        raise ValueError("Number of columns must be between 1 and 100")

    p = 0  # perimeter
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    p += 1
                else:
                    if grid[i-1][j] == 0:
                        p += 1
                if j-1 < 0:
                    p += 1
                else:
                    if grid[i][j-1] == 0:
                        p += 1

                try:
                    if grid[i+1][j] == 0:
                        p += 1
                except IndexError:
                    p += 1
                try:
                    if grid[i][j+1] == 0:
                        p += 1
                except IndexError:
                    p += 1

    return p
