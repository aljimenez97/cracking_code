# https://leetcode.com/problems/valid-mountain-array/

# Given an array of integers arr, return true if and only if 
# it is a valid mountain array.

from ast import increment_lineno


def is_mountain(arr):
    prev = None
    grew = False
    decreased = False

    for elem in arr:
        print(elem, grew, decreased)
        if prev is not None and elem == prev:
            return False
        if prev is not None and elem - prev > 0 :
            if decreased: 
                return False
            grew = True
        if prev is not None and elem - prev < 0:
            decreased = True

        prev = elem

    return grew and decreased

if __name__ == "__main__":
    arr = [0,3,2,1]
    print(is_mountain(arr))