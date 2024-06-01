from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(2, ListNode(2)))
list2 = ListNode(1, ListNode(3, ListNode(4)))


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = {}
        while(head):
            a[head.val] = head.val
            head = head.next
        dummy = ListNode()
        current = dummy

        for i in a:
            current.next = ListNode(val=i, next=None)
            current = current.next 
        return dummy.next

a = {2:1,4:2}

for i in a.values():
    print (i)