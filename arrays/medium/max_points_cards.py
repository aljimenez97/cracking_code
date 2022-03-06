# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

# There are several cards arranged in a row, and each card has an associated number of points. 
# The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

def get_accum(x):
    y = [0] * (len(x) + 1) 

    for i in range(1, len(x) + 1):
        y[i] = y[i-1] + x[i-1]
    return y

def max_points(cards, k):
    max = 0
    accum = get_accum(cards)

    for i in range(k + 1):
        add = (accum[i] if i else 0) + (accum[-1] - accum[i-k-1] if i-k else 0)
        if add > max:
            max = add
    return max
if __name__ == "__main__":
    cards = [100,40,17,9,73,75]
    k = 3

    print(max_points(cards, k))