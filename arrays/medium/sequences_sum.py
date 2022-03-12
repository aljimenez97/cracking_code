# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum 
# of the minimum and maximum element on it is less or equal to target. 
# Since the answer may be too large, return it modulo 10**9 + 7.

def subsequences(nums, target):
    l, r, res = 0, len(nums) - 1, 0
    nums.sort()


    while l < r:
        if nums[l] + nums[r] <= target:
            res += 2**(r-l) % (10**9+7)
            l += 1
        else:
            r -= 1

    return res % (10**9+7)

if __name__ == "__main__":
    nums = [3,5,6,7]
    target = 9
    print(subsequences(nums, target))