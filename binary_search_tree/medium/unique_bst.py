# https://leetcode.com/problems/unique-binary-search-trees/

# Given an integer n, return the number of structurally unique BST's (binary search trees) 
# which has exactly n nodes of unique values from 1 to n.

def num_trees(n, dyn = {}):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n in dyn:
        return dyn[n]

    total = 0

    for i in range(1, n+1):
        total += (num_trees(i - 1) or 1) * (num_trees(n - i) or 1)
    
    dyn[n] = total
    return dyn[n]

if __name__ == "__main__":
    n = 3
    print("n = 1", num_trees(1))
    print("n = 2", num_trees(2))
    print("n = 3", num_trees(5))