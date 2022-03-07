# https://leetcode.com/problems/bitwise-and-of-numbers-range/

# Given two integers left and right that represent the range 
# [left, right], return the bitwise AND of all numbers in this range, inclusive.
import math 


def bitwise_and_range(a, b):
    out = 0

    if a == 0 or b == 0:
        return 0

    while a and b:
        a_most_sig = int(math.log2(a))
        b_most_sig = int(math.log2(b))

        if a_most_sig == b_most_sig:
            out = out | 1 << a_most_sig 
            a -= 1<<a_most_sig
            b -= 1<<b_most_sig
        else:
            break   
    return out
    

if __name__ == "__main__":
    a= 5
    b= 7
    print(bitwise_and_range(a,b))

