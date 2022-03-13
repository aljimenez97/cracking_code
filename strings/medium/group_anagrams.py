# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of 
# a different word or phrase, typically using all the original letters exactly once.

def anagrams(strs):
    dict = {''.join(sorted(string)): [] for string in strs}

    for string in strs:
        dict[''.join(sorted(string))].append(string)

    return list(dict.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(anagrams(strs))