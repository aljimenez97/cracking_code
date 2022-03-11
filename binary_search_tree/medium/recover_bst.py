# https://leetcode.com/problems/recover-binary-search-tree/

# You are given the root of a binary search tree (BST), where the values of 
# exactly two nodes of the tree were swapped by mistake. Recover the tree 
# without changing its structure.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        self.node1 = None
        self.node2 = None
        self.prev = None
        
        def swap(n1, n2):
            tmp = n1.val
            n1.val = n2.val
            n2.val = tmp
        
        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if self.node1 is None and self.prev and self.prev.val > node.val:
                self.node1 = self.prev

            if self.node1 is not None and self.prev and self.prev.val > node.val:
                self.node2 = node

            self.prev = node
            inorder(node.right)
                
        inorder(root)
        swap(self.node1, self.node2)

        return root