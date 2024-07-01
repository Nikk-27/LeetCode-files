#19 Remove Nth Node From End of List

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:      #TC : O(N), SC : O(1)
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        #delete
        left.next = left.next.next
        return dummy.next

    def printList(self, node: ListNode, msg: str) -> None:
        print(msg)
        while node:
            print(node.val, end=" -> ")
            node = node.next
        print("None")
 

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
n = 5
linked_list = list_to_linked_list(head)
solution = Solution()
reordered_linked_list = solution.removeNthFromEnd(linked_list, n)
output_list = linked_list_to_list(reordered_linked_list)
print(output_list)