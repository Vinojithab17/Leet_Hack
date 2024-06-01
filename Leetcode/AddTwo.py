from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode()
        current = dummy
        carry = 0
        while l1 or l2:
        
            if l1:
                num1 = l1.val
                l1 = l1.next
            else: num1 = 0

            if l2:
                num2 = l2.val
                l2 = l2.next
            else: num2 = 0

            sum = (carry + num1+ num2)%10
            carry = (carry + num1+ num2)//10
            current.next = ListNode(val = sum)
            current = current.next

        if carry:
            current.next = ListNode(val = carry)
            current = current.next
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode()
        current = dummy
        carry = 0
        while l1 and l2:
            num = (l1.val + l2.val + carry)%10
            carry = (l1.val + l2.val + carry)//10
            current.next = ListNode(val = num)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        while l2:
            num = (l2.val + carry)%10
            carry = (l2.val + carry)//10
            current.next = ListNode(val = num)
            current = current.next
            l2 = l2.next
        while l1:
            num = (l1.val + carry)%10
            carry = (l1.val + carry)//10
            current.next = ListNode(val = num)
            current = current.next
            l1 = l1.next
        if carry >0:
            current.next = ListNode(val = carry)
            current = current.next
        return dummy.next


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]


def addList(self,l1: list[int], l2: list[int]) -> Optional[ListNode]:
    dummy  = ListNode()
    current = dummy
    carry  = 0
    len1 = len(l1)
    len2 = len(l2)
    l =  max(len1,len2)
    sums = []
    for i in range(1,l+1):
        if len1>0:
            num1 = l1[0-i]
            len1-=1
        else: num1 = 0

        if len2>0:
            num2 = l2[0-i]
            len2-=1
        else: num2 = 0

        sum = (carry + num1+ num2)%10
        carry = (carry + num1+ num2)//10
        # sums.append(sum)

        sums.append(sum)
        if i == l and carry >0:
            sums.append(carry)

    print(sums)
    for i in sums:
        current.next = ListNode(val=i)
        current  = current.next
    print(dummy.next)
    return dummy.next

list1 = ListNode(2, ListNode(4, ListNode(3)))
list2 = ListNode(5, ListNode(6, ListNode(4)))

adder  = Solution()

print (adder.addTwoNumbers(list1,list2))
