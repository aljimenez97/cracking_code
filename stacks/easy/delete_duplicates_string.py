# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# You are given a string s consisting of lowercase English letters. A duplicate 
# removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. 
# It can be proven that the answer is unique.

def delete_duplicates(word):
    stack = []

    for letter in word:
        if not stack or stack[-1] != letter:
            stack.append(letter)
        else:
            stack.pop()

    return ''.join(stack)

if __name__ == "__main__":
    s = "abbaca"
    print(delete_duplicates(s))
