# https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/

# You are given the root node of a binary search tree (BST) and a value to insert 
# into the tree. Return the root node of the BST after the insertion. It is 
# guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long 
# as the tree remains a BST after insertion. You can return any of them.

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def insert_into_bst(root, val):
    new_node = TreeNode(val)
    curr = root
    
    if root is None:
        return new_node

    while (val > curr.val and curr.right is not None) or (val < curr.val and curr.left is not None):
        if val > curr.val and curr.right is not None:
            curr = curr.right
        
        if (val < curr.val and curr.left is not None):
            curr = curr.left
    if val > curr.val:
        curr.right = new_node
    else:
        curr.left = new_node
        
    return root