class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        return str(self.val) + " " + str(self.next) if self.next is not None else str(self.val)

def reverseList(head):
    prev = None
    curr = head
    aux = None
    
    while curr is not None:
        aux = curr.next
        curr.next = prev
        prev = curr
        curr = aux
    return prev

if __name__ == "__main__":
    root = Node(1)
    root.next = Node(2)
    root.next.next = Node(3)

    print(reverseList(root))

