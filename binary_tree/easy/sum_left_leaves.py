# https://leetcode.com/problems/sum-of-left-leaves/
# Given the root of a binary tree, return the sum of all left leaves.

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def get_left_leaves(node, is_left = False):
    if node is None:
        return []

    if node.right is None and node.left is None and is_left:
        return [node]
    else:
        return get_left_leaves(node.left, True) + get_left_leaves(node.right, False)


def sum_left_leaves(root):
    left_leaves = get_left_leaves(root)
    sum = 0

    for node in left_leaves:
        sum += node.val
    return sum

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print(sum_left_leaves(root))