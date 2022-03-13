# https://leetcode.com/problems/jump-game/

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

def can_jump(nums):
    maximum = 0

    for i, n in enumerate(nums):
        if i > maximum:
            return False
        maximum = max(maximum, i + n)
    return True

if __name__ == "__main__":
    nums = [2, 0, 0]
    print(can_jump(nums))