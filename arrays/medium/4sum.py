# https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return an array of all the unique 
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# - 0 <= a, b, c, d < n
# - a, b, c, and d are distinct.
# - nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

def find_4sums(nums, target):
    if len(nums) < 4:
        return []

    nums.sort()
    res = []

    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            l = j + 1
            r = len(nums) - 1
            target2 = target - (nums[i] + nums[j])
            while l < r:
                if nums[l] + nums[r] == target2:
                    if [nums[i], nums[l], nums[r], nums[j]] not in res:
                        res.append([nums[i], nums[l], nums[r], nums[j]])

                if nums[l] + nums[r] > target2:
                    r -= 1
                else: l += 1
    return res


if __name__ == "__main__":
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0

    print(find_4sums(nums, target))