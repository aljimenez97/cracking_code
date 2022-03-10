# https://leetcode.com/problems/binary-tree-right-side-view/

# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

from collections import deque

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


def right_side_view(root):
    # BFS -> FIFO -> Queue
    q = deque()
    level_dict = {}

    q.appendleft((root, 0))

    while q:
        popped, level = q.pop()

        if popped is not None:
            level_dict[level] = popped.val
            q.appendleft((popped.left, level + 1))
            q.appendleft((popped.right, level + 1))

    return list(level_dict.values())

if __name__ == "__main__":
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.right = Node(5)
    head.right.right = Node(4)

    print(right_side_view(head))
