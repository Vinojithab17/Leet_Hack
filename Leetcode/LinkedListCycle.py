from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(2, ListNode(0)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        count = 0
        while True:
            if head.val >= 0:
                try :
                    n = nums[head.val]

                    break
                except ValueError:
                    count +=1
                    nums.append(head.val)
                    head = head.next
                    continue
            else:
                count +=1
                nums.append(head.val)
                head = head.next



