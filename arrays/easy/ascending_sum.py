# https://leetcode.com/problems/maximum-ascending-subarray-sum/

# Given an array of positive integers nums, return the maximum possible 
# sum of an ascending subarray in nums.

# A subarray is defined as a contiguous sequence of numbers in an array.

# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all 
# i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

def max_ascending_sum(nums):
    prev = 0
    max_sum = 0
    current_sum = 0

    for num in nums:
        if num > prev:
            current_sum += num
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = num
        prev = num
    
    return max(max_sum, current_sum)

if __name__ == "__main__":
    nums = [10,20,30,5,10,50]
    print(max_ascending_sum(nums))