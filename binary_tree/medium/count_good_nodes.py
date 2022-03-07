# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Given a binary tree root, a node X in the tree is named good if in 
# the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

from collections import deque

class BinaryNode:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def find_good_nodes(node):
    count = 0
    stack = deque()

    stack.append((node, -float('inf')))
    
    while len(stack):
        popped, prev_max = stack.pop()

        if popped.val >= prev_max:
            count += 1

        if popped.left is not None:
            stack.append((popped.left, max(prev_max, popped.val)))

        if popped.right is not None:
            stack.append((popped.right, max(prev_max, popped.val)))

    return count



if __name__ == "__main__":
    root = BinaryNode(3)
    root.right = BinaryNode(4)
    root.right.right = BinaryNode(5)
    root.right.left = BinaryNode(1)
    root.left = BinaryNode(1)
    root.left.left = BinaryNode(3)

    print(find_good_nodes(root))