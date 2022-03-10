# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of 
# two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest 
# common ancestor is defined between two nodes p and q as the lowest 
# node in T that has both p and q as descendants (where we allow a node 
# to be a descendant of itself).”

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def lowest_common_ancestor(tree_node, p, q):

    def dfs(node):
        if node is None: 
            return False

        current = node == p or node == q

        left = dfs(node.left)
        right = dfs(node.right)

        if (left and right) or (current and left) or (current and right):
            return node

        return current or left or right

    return dfs(tree_node)


if __name__ == "__main__":
    print(lowest_common_ancestor())

