# https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome.

class LinkedNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def create_list(arr):
    head = LinkedNode(0)
    curr = head

    for elem in arr:
        curr.next = LinkedNode(elem)
        curr = curr.next
    
    return head.next

def reverse_linked_list(head):
    prev = None
    curr = head
    aux = None

    while curr is not None:
        aux = curr.next
        curr.next = prev
        prev = curr
        curr = aux
    return prev

def is_palindrome(head):

    reversed = reverse_linked_list(head)

    curr = head
    curr2 = reversed

    while curr is not None and curr2 is not None:
        if curr.val != curr2.val:
            return False
        curr = curr.next
        curr2 = curr2.next
    return True

if __name__ == "__main__":


    array = [1,2,2,1]
    head = create_list(array)
    print(is_palindrome(head))
