# 206 Reverse Linked List

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        prev = None
        while(temp != None):
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

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

head = [1,2,3,4,5]
linked_list = list_to_linked_list(head)
solution = Solution()
reversed_linked_list = solution.reverseList(linked_list)
output_list = linked_list_to_list(reversed_linked_list)
print(output_list)