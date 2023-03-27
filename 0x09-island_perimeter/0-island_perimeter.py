#!/usr/bin/python3
"""This calculates the perimeter of an island"""

def island_perimeter(grid):
    """ This returns the calculated perimeter"""
    if grid == []:
        return 0

    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                # check the top of the space for land
                if grid[i - 1] and grid[i - 1][j] == 1:
                    perimeter -= 1

                # check the bottom of the space for land
                if grid[i + 1] and grid[i + 1][j] == 1:
                    perimeter -= 1

                # check the right of the space for land
                if grid[i][j + 1] and grid[i][j + 1] == 1:
                    perimeter -= 1

                # check the left of the space for land
                if grid[i][j - 1] and grid[i][j - 1] == 1:
                    perimeter -= 1

    return perimeter
