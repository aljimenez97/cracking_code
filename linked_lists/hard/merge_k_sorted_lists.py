# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each 
# linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list 
# and return it.

import heapq

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def merge_lists(lists):
    pq = []
    heapq.heapify(pq)

    head = Node(0)
    curr = head

    for i, l in enumerate(lists):
        if l is not None:
            heapq.heappush(pq, (l.val, i, l))

    while len(pq):
        _, i, popped = heapq.heappop(pq)
        if popped.next is not None:
            heapq.heappush(pq, (popped.next.val, i, popped.next))
        curr.next = popped
        curr = curr.next
    
    return head.next

if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(4)
    l1.next.next = Node(5)

    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(4)

    l3 = Node(2)
    l3.next = Node(6)

    print(merge_lists([l1, l2, l3]))
