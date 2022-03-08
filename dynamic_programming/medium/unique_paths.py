# https://leetcode.com/problems/unique-paths/

# There is a robot on an m x n grid. The robot is initially located 
# at the top-left corner (i.e., grid[0][0]). The robot tries to move 
# to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can 
# only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible 
# unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be 
# less than or equal to 2 * 109.

def unique_paths(m, n, dyn = {}):

    # m-1 if it goes down, n-1 if it goes right
    if n == 1 or m == 1:
        return 1
    
    if f'{m},{n}' in dyn:
        return dyn[f'{m},{n}']

    if f'{n},{m}' in dyn:
        return dyn[f'{n},{m}']   

    dyn[f'{m},{n}'] = unique_paths(m-1, n, dyn) + unique_paths(m, n-1, dyn) 

    return dyn[f'{m},{n}']

if __name__ == "__main__":
    m = 3
    n = 7
    print(unique_paths(m, n))