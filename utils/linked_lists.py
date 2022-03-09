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
    
    return head

