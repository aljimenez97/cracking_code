# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

def longest_substring(word):
    l = 0
    r = 0
    max_length = 0

    while r < len(word):
        substring = word[l:r]

        # We could do it more efficient with a dictionary
        if word[r] not in substring:
            max_length = max(max_length, r-l+1)
        else:
            l += substring.find(word[r]) + 1
        r += 1

    return max_length


if __name__ == "__main__":
    word = "bbtablud"
    print(longest_substring(word))