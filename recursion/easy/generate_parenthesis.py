# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/

# Given a VPS represented as string s, return the nesting depth of s.

def maxDepth(s):
        curr = 0
        maxDepth = 0
        
        for elem in s:
            if elem == "(":
                curr += 1
                maxDepth = max(maxDepth, curr)
            if elem == ")":
                curr -= 1
        return maxDepth

if __name__ == "__main__":
    s = "(1+(2*3)+((8)/4))+1"
    print(maxDepth(s))