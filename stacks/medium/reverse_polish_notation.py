# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from collections import deque

OPERATION_TOKENS = ["+", "-", "*", "/"]

def is_operation(token):
    return token in OPERATION_TOKENS
        
def eval_reverse_notation(tokens):
    # I need LIFO for the stack
    st = deque()

    for token in tokens:
        if is_operation(token):
            op2 = st.pop()
            op1 = st.pop()

            if token == "+":
                res = op1 + op2
            elif token == "-":
                res = op1 - op2
            elif token == "*":
                res = op1 * op2
            elif token == "/":
                res = int(op1 / op2)
            #print(str(op1) + token + str(op2) + "=" + str(res))
            st.append(res)
        else:
            st.append(int(token))
    
    return st[0] 

if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(eval_reverse_notation(tokens))