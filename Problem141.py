#141 Linked List Cycle

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: #(we are using Floyd's Tortoise & Hare algo)
    def hasCycle(self, head: Optional[ListNode]) -> bool:                         #TC : O(N), SC : O(1)

        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

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


head = [3,2,0,-4]
pos = 1
linked_list = list_to_linked_list(head)
solution = Solution()
print(solution.hasCycle(linked_list))