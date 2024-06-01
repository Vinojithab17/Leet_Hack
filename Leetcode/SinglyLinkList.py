from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListOperations:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If there are remaining nodes in either list, append them
        current.next = list1 if list1 else list2

        return dummy.next

    def iterate(self, head: Optional[ListNode]):
        current = head
        while current:
            yield current.val
            current = current.next

# Example usage:
# Create two sample linked lists: 1->2->4 and 1->3->4
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

operations = LinkedListOperations()
merged_list_head = operations.mergeTwoLists(list1, list2)

print("Merged Linked List:")
for value in operations.iterate(merged_list_head):
    print(value, end=" -> ")
print("None")


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists2(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy 
    while list1 and list2:
        if list1.val > list2.val:
            new_val = list2.val 
            list2 = list2.next 
        else:
            new_val = list1.val 
            list1 = list1.next 

        tail.next = ListNode(val=new_val, next=None)
        tail = tail.next 

    if list1:
        tail.next = list1

    if list2:
        tail.next = list2
    return dummy.next 

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

        
merged_list_head2 = mergeTwoLists2(list1, list2)

print("Merged Linked List:")
for value in operations.iterate(merged_list_head2):
    print(value, end=" -> ")
print("None")