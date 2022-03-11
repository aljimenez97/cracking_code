# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

import heapq

def find_pairs(nums1, nums2, k):
    min_heap = []
    out = []
    visited = {(0,0)}

    if k == 0 or not nums1 or not nums2:
        return out

    heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))

    while min_heap and len(out) <= k:
        _, id1, id2 = heapq.heappop(min_heap)
        out.append([nums1[id1], nums2[id2]])

        if (id1, id2+1) not in visited and id2 + 1 < len(nums2):
            visited.add((id1, id2 + 1))
            heapq.heappush(min_heap, (nums1[id1] + nums2[id2 + 1], id1, id2 + 1))

        if (id1 + 1, id2) not in visited and id1 + 1 < len(nums1):
            visited.add((id1 + 1, id2))
            heapq.heappush(min_heap, (nums1[id1 + 1] + nums2[id2], id1 + 1, id2))

    return out[:k]


if __name__ == "__main__":
    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    print(find_pairs(nums1, nums2, k))

    nums1 = [1,2]
    nums2 = [3]
    k = 3
    print(find_pairs(nums1, nums2, k))

    nums1 = [1,1,2]
    nums2 = [1,2,3]
    k = 10
    print(find_pairs(nums1, nums2, k))
