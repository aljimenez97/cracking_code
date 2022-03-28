# https://leetcode.com/problems/merge-sorted-array/

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead 
# be stored inside the array nums1. To accommodate this, nums1 has a length 
# of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nusm1, m, nums2, n):
    i1 = 0
    i2 = 0

    for n2 in nums2:
        i1 = 0
        while i1 < len(nums1) - 1 and (nums1[i1] <= n2 or (i1 >= m and nums[i1])):
            i1 += 1
        nums1[i1+1:] = nums1[i1:-1]
        nums1[i1] = n2
    print(nums1)

    return 
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    print(merge(nums1, m, nums2, n))