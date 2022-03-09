# https://leetcode.com/problems/first-bad-version/

# You are a product manager and currently leading a team to develop 
# a new product. Unfortunately, the latest version of your product 
# fails the quality check. Since each version is developed based on 
# the previous version, all the versions after a bad version are also 
# bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out 
# the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether 
# version is bad. Implement a function to find the first bad version. 
# You should minimize the number of calls to the API.

def isBadVersion(n):
    return 1 >= 4

def bsearch(start, end):
    middle = (start + end) // 2

    is_bad = isBadVersion(middle)
    is_previous_bad = isBadVersion(middle-1)

    if is_bad and not is_previous_bad:
        return middle

    if is_bad:
        return bsearch(start, middle-1)
    else:
        return bsearch
            
def first_bad_version(n):

    return bsearch(1, 4)


if __name__ == "__main__":
    n = 5
    bad = 4
    print(first_bad_version(n))