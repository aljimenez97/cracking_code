# https://leetcode.com/problems/linked-list-cycle/submissions/

# Given head, the head of a linked list, determine if the linked list 
# has a cycle in it.

# There is a cycle in a linked list if there is some node in the list 
# that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's 
# next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def hasCycle(self, head) -> bool:
    visited = {}
    curr = head
    
    while curr is not None:
        if curr in visited:
            return True
        visited[curr] = 1
        curr = curr.next

    return False
