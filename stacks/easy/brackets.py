from collections import deque

def is_open(char):
    return char in ["(", "{", "["]

brackets_dict = {
    "(": ")",
    "[": "]",
    "{": "}",
}

def valid_brackets(string):
    if not(len(string)) or len(string) % 2 == 1:
        return False
    # I need LIFO -> Stack
    stack = deque()

    for char in string:
        # Append open char to stack
        if is_open(char):
            stack.append(char)

        # Is closing bracket
        elif len(stack):
            # Get last opening bracker
            last_bracket = stack.pop()
            # If mismatch
            if char != brackets_dict[last_bracket]:
                return False
        # Found closing bracket with no opening bracket
        else:
            return False

    # Only true if all brackets from the stack have been matched
    return True if not(len(stack)) else False


if __name__ == "__main__":
    print(valid_brackets(")("))


    