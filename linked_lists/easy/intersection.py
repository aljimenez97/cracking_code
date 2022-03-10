# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Given the heads of two singly linked-lists headA and headB, return the node
# at which the two lists intersect. If the two linked lists have no intersection 
# at all, return null.

def len_list(head):
    curr = head
    length = 0

    while curr is not None:
        length += 1
        curr = curr.next
    
    return length

def getIntersectionNode(headA, headB):
    len_a = len_list(headA)
    len_b = len_list(headB)
    
    currA = headA
    currB = headB
    
    if len_a > len_b:
        diff = len_a - len_b
        while diff:
            currA = currA.next
            diff -= 1
    elif len_a < len_b:
        diff = len_b - len_a
        while diff:
            currB = currB.next
            diff -= 1
        
    while currA is not None and currB is not None and currA != currB:
        currA = currA.next
        currB = currB.next
    
    return currA