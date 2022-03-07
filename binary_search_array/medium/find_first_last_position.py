# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in non-decreasing order, find the starting 
# and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

from more_itertools import first

def find_first(target, start, end, nums):
    if start >= end:
        return -1
    
    middle = (start + end) // 2

    if nums[middle] == target and (middle == 0 or nums[middle - 1] < target):
        return middle
    else:
        if target <= nums[middle]:
            return find_first(target, start, middle - 1, nums)
        else:
            return find_first(target, middle + 1, end, nums)

def find_last(target, start, end, nums):
    if start >= end:
        return -1
    
    middle = (start + end) // 2

    if nums[middle] == target and (middle == len(nums) - 1 or nums[middle + 1] > target):
        return middle
    else:
        if nums[middle] >= target:
            return find_last(target, start, middle - 1, nums)
        else:
            return find_last(target, middle + 1, end, nums)

def find_first_last(nums, target):
    return [find_first(target, 0, len(nums), nums), find_last(target, 0, len(nums), nums)]

if __name__ == "__main__":
    nums = [0,1,1,1,2,3]
    target = 1
    print(find_first_last(nums, target))
