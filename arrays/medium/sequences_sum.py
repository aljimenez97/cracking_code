# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

# You are given an array of integers nums and an integer target.

# Return the number of non-empty subsequences of nums such that the sum 
# of the minimum and maximum element on it is less or equal to target. 
# Since the answer may be too large, return it modulo 10**9 + 7.

def subsequences(nums, target):
    l, r, res = 0, len(nums) - 1, 0
    nums.sort()

    # Creating the array based on i-1 is much more efficient
    pows = [1] * len(nums)
    for i in range(1, len(nums)):
        pows[i] = pows[i-1]*2 % (10**9+7)
    
    while l <= r:
        if nums[l] + nums[r] <= target:
            # There are 2**(r-l) subsequences that satisfy the condition, if nums[l] is min and nums[r] is max
            res += pows[r-l]
            l += 1
        else:
            r -= 1

    return res % (10**9+7)


if __name__ == "__main__":
    nums = [3,5,6,7]
    target = 9
    print(subsequences(nums, target))