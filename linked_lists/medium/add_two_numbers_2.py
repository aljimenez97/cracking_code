# https://leetcode.com/problems/add-two-numbers-ii/

# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single 
# digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 
# 0 itself.

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    aux = None

    while curr is not None:
        aux = curr.next
        curr.next = prev
        prev = curr
        curr = aux

    return prev

def sum_lists(headA, headB):
    headA_rev = reverse_list(headA)
    headB_rev = reverse_list(headB)

    currA = headA_rev
    currB = headB_rev

    out_head = Node(0)
    curr_out = out_head

    cache = 0

    while currA is not None and currB is not None:
        if currA and currB:
            addition = currA.val + currB.val + cache
        elif currA:
            addition = currA.val + cache
        elif currB:
            addition = currB.val + cache
        elif cache:
            addition = cache

        cache = 1 if addition > 9 else 0
        curr_out.next = Node(addition)

        curr_out = curr_out.next
        currA = currA.next
        currB = currB.next

    return reverse_list(out_head.next)