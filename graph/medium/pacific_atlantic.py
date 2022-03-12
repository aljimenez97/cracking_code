# https://leetcode.com/problems/pacific-atlantic-water-flow/

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches 
# the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer 
# matrix heights where heights[r][c] represents the height above sea level of the cell 
# at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells 
# directly north, south, east, and west if the neighboring cell's height is less than 
# or equal to the current cell's height. Water can flow from any cell adjacent to an 
# ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that 
# rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

from collections import deque

def is_valid(row, col, grid):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols

def flows(grid):
    opts = [(1,0), (0,1), (-1,0), (0,-1)]
    rows = len(grid)
    cols = len(grid[0])
    atlantic = set()
    pacific = set()

    def dfs(row, col, visited, prev):
        if not is_valid(row, col, grid) or (row, col ) in visited or grid[row][col] < prev:
            return
        visited.add((row, col))

        for d_r, d_c in opts:
            dfs(row + d_r, col + d_c, visited, grid[row][col])

    for col_i in range(cols):
        dfs(0, col_i, pacific, 0)
        dfs(rows - 1, col_i, atlantic, 0)

    for row_i in range(rows):
        dfs(row_i, 0, pacific, 0)
        dfs(row_i, cols - 1, atlantic, 0)

    out = list(pacific.intersection(atlantic))
    out.sort()
    return out
    

if __name__ == "__main__":
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(flows(heights))