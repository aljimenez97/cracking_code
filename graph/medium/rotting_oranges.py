# https://leetcode.com/problems/rotting-oranges/

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque

def rotten_oranges(grid):
    # BFS -> FIFO -> Queue
    q = deque()
    fresh_oranges = 0

    visited =[[False for _ in range(len(grid[row]))] for row in range(len(grid))]
    time_passed = 0

    # Count the number of fresh oranges and the initial rotten ones
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                fresh_oranges += 1
            if grid[row][col] == 2:
                q.appendleft((row,col, 0))

    opts = [(1,0), (0,1), (-1,0), (0,-1)]

    while len(q):
        row, col, time_to_rot = q.pop()
        visited[row][col] = True

        time_passed = time_to_rot if time_to_rot > time_passed else time_passed

        for d_row, d_col in opts:
            if (0 <= (row + d_row) < len(grid) 
                and 0 <= (col + d_col) < len(grid[0]) 
                and grid[row + d_row][col + d_col] == 1
                and not visited[row + d_row][col + d_col]):
                fresh_oranges -= 1
                grid[row + d_row][col + d_col] = 2
                q.appendleft((row + d_row, col + d_col, time_to_rot + 1))

    return time_passed if not fresh_oranges else -1
if __name__ == "__main__":
    grid = [[2,1,1],[1,1,1],[0,1,2]]

    print(rotten_oranges(grid))


