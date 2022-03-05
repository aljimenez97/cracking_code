
from collections import deque

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def add_descendants(self,num_list):
        curr = self
        for num in num_list:
            curr.next = ListNode(num)
            curr = curr.next

    def __str__(self) -> str:
        if self is None:
            return ''
        return str(self.val) + str(self.next) if self.next is not None else str(self.val)

def add_lists(l1, l2):
        # FIFO
        q1 = deque()
        q2 = deque()
        
        curr1 = l1
        curr2 = l2
        
        while curr1 is not None or curr2 is not None:
            if curr1 is not None:
                q1.appendleft(curr1)
                curr1 = curr1.next
            if curr2 is not None:
                q2.appendleft(curr2)
                curr2 = curr2.next
        out = ListNode(0)
        curr = out
        
        offset = 0
        while len(q1) or len(q2) or offset:
            
            if len(q1) and len(q2):
                addition = q1.pop().val + q2.pop().val + offset
            elif len(q1):
                addition = q1.pop().val + offset
            elif len(q2):
                addition = q2.pop().val + offset
            elif offset:
                addition = offset

            curr.next = ListNode(addition % 10)
            offset = 1 if addition >= 10 else 0
            curr = curr.next
            
        return out.next
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.add_descendants([4,9])
    print("L1:", l1)

    l2 = ListNode(5)
    l2.add_descendants([6,4,9])
    print("L2:", l2)

    l3 = add_lists(l1, l2)
    print(l3)