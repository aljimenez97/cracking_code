# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of 
# the string and change it to any other uppercase English character. You can 
# perform this operation at most k times.

# Return the length of the longest substring containing the same letter you 
# can get after performing the above operations.

def longestSub(s, k):
    l, r, maxSub = 0, 0, 0
    counter = {}

    while r < len(s):

        if s[r] in counter:
            counter[s[r]] += 1
        else:
            counter[s[r]] = 1

        if (r - l + 1) - max(counter.values()) > k:
            counter[s[l]] -= 1
            l += 1
        
        if (r - l + 1) > maxSub:
            maxSub = r - l + 1

        r += 1

    
    return maxSub

if __name__ == "__main__":
    s = "ABAB"
    k = 2

    print(longestSub(s, k))