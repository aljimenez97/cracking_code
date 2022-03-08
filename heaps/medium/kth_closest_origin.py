# https://leetcode.com/problems/k-closest-points-to-origin/

# Given an array of points where points[i] = [xi, yi] represents a point 
# on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean 
# distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed 
# to be unique (except for the order that it is in).

import heapq
import math

def distance(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def kth_closest(points, k):
    min_heap = []
    heapq.heapify(min_heap)

    for point in points:
        heapq.heappush(min_heap, (distance(point), point))

    out = []

    for _ in range(k):
        out.append(heapq.heappop(min_heap)[1])

    return out

if __name__ == "__main__":
    points = [[1,3],[-2,2]]
    k = 1
    print(kth_closest(points, k))