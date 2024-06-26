# 21 Merge Two Sorted Lists

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

# Utility function to convert a Python list to a linked list
def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Utility function to convert a linked list to a Python list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

list1 = [1,2,4]
list2 = [1,3,4]
linked_list1 = list_to_linked_list(list1)
linked_list2 = list_to_linked_list(list2)
solution = Solution()
merged_linked_list = solution.mergeTwoLists(linked_list1, linked_list2)
output_list = linked_list_to_list(merged_linked_list)
print(output_list)