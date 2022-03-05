# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes 
# p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def has_descendant(node, p):
    if node is None:
        return False
    if node.val == p:
        return True
    return has_descendant(node.left, p) or has_descendant(node.right, p)

def get_lower_ancestors(node, p, q):
    if node is None:
        return []
    if has_descendant(node, p) and has_descendant(node, q):
        return [node] + get_lower_ancestors(node.left, p, q) + get_lower_ancestors(node.right, p, q)
    if node.left is not None and node.right is not None:
        if (node.left.val == p and node.right.val == q) or (node.left.val == q and node.right.val == p):
            return [node] + get_lower_ancestors(node.left, p, q) + get_lower_ancestors(node.right, p, q)
    return get_lower_ancestors(node.left, p, q) + get_lower_ancestors(node.right, p, q)


if __name__ == "__main__":
    p = 2
    q = 4

    root = Node(6)
    root.left = Node(2)
    root.left.left = Node(0)
    root.left.right = Node(4)
    root.left.right.left = Node(3)
    root.left.right.right = Node(5)
    root.right = Node(8)
    root.right.left = Node(7)
    root.right.right = Node(9)

    print(get_lower_ancestors(root, p, q)[-1].val)

    
