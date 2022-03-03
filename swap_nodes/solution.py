from collections import deque

class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder(self):
        # Inorder is left, node, right
        current = self
        # I need LIFO -> Stack
        stack = deque()
        out=[]

        while len(stack) or current is not None:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                # Visit node
                out.append(current.value)
                current = current.right
        return out




def swap(root, k):
    # I need FIFO -> Queue
    q = deque([(root, 1)])

    while q:
        node, level = q.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        q.extend([(node.left, level + 1), (node.right, level + 1)])
     
def solution(indexes, queries):
    root = BTNode(1)
    nodes = [0] * len(indexes)
    nodes[0] = root

    for i, index in enumerate(indexes):
        node = nodes[i]

        if index[0] != -1:
            node_left = BTNode(index[0])
            nodes[index[0] - 1] = node_left
            node.left = node_left

        if index[1] != -1:
            node_right = BTNode(index[1])
            nodes[index[1] - 1] = node_right
            node.right = node_right

    out = []
    for q in queries:
        swap(root, q)
        out.append(root.inorder())

    return out            



if __name__ == "__main__":
    indexes = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    queries = [2, 3]

    print(solution(indexes, queries))

