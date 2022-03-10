# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) 
# so that the resulting parentheses string is valid and return any valid string.


def min_remove_parenthesis(text):
    stack = []
    out = [''] * len(text)

    for i, letter in enumerate(text):
        if letter == "(":
            stack.append((letter, i))
        if letter == ")" and stack:
            _, pos = stack.pop()
            out[pos] = "("
            out[i] = ")"
        if letter != "(" and letter != ")":
            out[i] = letter
    return ''.join(out)

if __name__ == "__main__":
    text = "a)b(c)d"
    print(min_remove_parenthesis(text))