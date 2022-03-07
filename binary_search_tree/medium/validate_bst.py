# https://leetcode.com/problems/validate-binary-search-tree/

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def is_valid_bst(node):
    def valid(node, left, right):
        if node is None:
            return True

        if left >= node.val or right <= node.val:
            return False
        
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)
    
    return valid(node, -float('inf'), float('inf'))

if __name__ == "__main__":
    root = Node(2)
    root.right = Node(3)
    root.left = Node(1)

    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.right.left = Node(4)
    root.right.right = Node(8)

    print(is_valid_bst(root))
