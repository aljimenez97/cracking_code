# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all 
# possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return 
# the solution in any order.

def get_subsets(inputs):
    out = [[]]

    for i in inputs:
        out.extend(o + [i] for o in list(out))

    return out

if __name__ == "__main__":
    inputs = [1,2,3]
    print(get_subsets(inputs))