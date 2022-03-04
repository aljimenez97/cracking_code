# https://leetcode.com/problems/binary-search/
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def binary_search(nums, target, initial = 0, end = 0):
    while initial < end:
        middle = (initial + end) // 2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            initial = middle + 1
        else:
            end = middle
    return -1




if __name__ == "__main__":
    nums  = [-1,0,3,5,9,12]
    target = 2
    print(binary_search(nums, target, 0, len(nums)))