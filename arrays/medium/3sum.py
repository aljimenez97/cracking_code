# https://leetcode.com/problems/3sum-closest/

# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

def sum_3_closest(nums, target):
    min_dist = float('inf')
    nums.sort()
    res = 0

    for i in range(0, len(nums) - 2):
        l = i + 1
        r = len(nums) - 1

        while l < r:
            sum_3 = nums[i] + nums[l] + nums[r]

            if sum_3 == target: return target

            if sum_3 > target:
                if sum_3 - target < min_dist:
                    min_dist = sum_3 - target
                    res = sum_3
                r -= 1
            else:
                if target - sum_3 < min_dist:
                    min_dist = target - sum_3
                    res = sum_3
                l += 1
    return res

if __name__ == "__main__":
    nums = [-1,2,1,-4, 2]
    target = 1

    print(sum_3_closest(nums, target))