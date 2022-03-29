# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

# Given a string s and an integer k, return the length of the longest substring of s such 
# that the frequency of each character in this substring is greater than or equal to k.

from collections import Counter

def longestSub(s, k):
    max_chars = len(Counter(s))
    print(max_chars)
    ans = 0
    print(Counter(s))
    for size in range(1, len(s) + 1):
        i = 0
        mp = Counter()
        for j in range(len(s)):
            # limit sliding window by number of distinct characters
            while len(mp.values())>size:
                mp[s[i]] -= 1
                if mp[s[i]]==0: 
                    mp.pop(s[i])
                i += 1
            mp[s[j]] += 1

            # update ans when all the character frequencies >= k
            if all(v>=k for v in mp.values()):
                ans = max(ans, sum(mp.values()))
    return ans


if __name__ == "__main__":
    s = "aaabb"
    k = 3
    print(longestSub(s, k))

    s = "ababbc"
    k = 2
    print(longestSub(s, k))

    s = "bbaaacbd"
    k = 3
    print(longestSub(s, k))
    
    s = "baaabcb"
    k = 3
    print(longestSub(s, k))

