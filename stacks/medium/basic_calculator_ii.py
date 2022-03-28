# https://leetcode.com/problems/basic-calculator-ii/

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

def calculate(s):
    stack = []
    ops = {"+", "-", "*", "/"}
    ope = "+"
    cur = 0

    for i, elem in enumerate(s):
        if elem.isdigit():
            cur = cur * 10 + int(elem)

        if elem in ops or i == len(s) - 1:
            if ope == "+":
                stack.append(cur)
            elif ope == "-":
                stack.append(-cur)
            elif ope == "*":
                stack[-1] *= cur
            elif ope == "/":
                stack[-1] = int(stack[-1] / cur)

            cur = 0
            ope = elem
    return sum(stack)

if __name__ == "__main__":
    s = " 3+5 / 2 "
    print(calculate(s))