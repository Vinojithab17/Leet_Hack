# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr = []
        current_node1 = list1
        current_node2 = list2
        while current_node1 is not None and current_node2 is not None:
            if(current_node1.val>current_node2.val):
                arr.append(current_node2.val)
                current_node2 = current_node2.next
            else:
                arr.append(current_node1.val)
                current_node1 = current_node1.next
        while current_node1 is not None:
            arr.append(current_node1.val)
            current_node1 = current_node1.next
        while current_node2 is not None:
            arr.append(current_node2.val)
            current_node2= current_node2.next
        print(arr)

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        