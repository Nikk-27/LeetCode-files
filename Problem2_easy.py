#2 Add Two Numbers

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:      #TC : O(N), SC : O(1)
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            #update pointers
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
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


l1 = [2,4,3]
l2 = [5,6,4]
linked_list_l1 = list_to_linked_list(l1)
linked_list_l2 = list_to_linked_list(l2)
solution = Solution()
added_linked_list = solution.addTwoNumbers(linked_list_l1, linked_list_l2)
output_list = linked_list_to_list(added_linked_list)
print(output_list)