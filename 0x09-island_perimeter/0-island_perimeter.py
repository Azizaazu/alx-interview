#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.
    param: grid
    return: perimeter
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4 # Each land cell contributes 4 to the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2 # Subtract 2 if adjacent cell is land (top)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2 # Subtract 2 if adjacent cell is land (left)
    return perimeter
