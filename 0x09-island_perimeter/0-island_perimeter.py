#!/usr/bin/python3
"""Defines island perimeter finding function."""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): 2D grid representation of the island.

    Returns:
        int: Perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Check for water or edge on all 4 sides
                if r == 0 or grid[r-1][c] == 0:  # Top
                    perimeter += 1
                if r == rows-1 or grid[r+1][c] == 0:  # Bottom
                    perimeter += 1
                if c == 0 or grid[r][c-1] == 0:  # Left
                    perimeter += 1
                if c == cols-1 or grid[r][c+1] == 0:  # Right
                    perimeter += 1

    return perimeter
