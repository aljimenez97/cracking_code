# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
    def __str__(self) -> str:
        return str(self.val) + "," + str(self.next if self.next is not None else "")

def getListLength(head):
    curr = head
    count = 0

    while curr is not None:
        count += 1
        curr = curr.next
    return count

def deleteKth(head, k):
    listSize = getListLength(head)
    jumps = listSize - k
    root = Node(0)
    curr = root
    curr. next = head

    while jumps > 0:
        curr = curr.next
        jumps -= 1
    
    curr.next = curr.next.next if curr.next is not None else None

    return root.next

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print(deleteKth(head, 2))