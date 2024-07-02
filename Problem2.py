#2 Add Two Numbers

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
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:      #TC : O(N), SC : O(1)
        str1 = ""
        str2 = ""

        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        while l1:
            str1 += str(l1.val)
            l1 = l1.next

        while l2:
            str2 += str(l2.val)
            l2 = l2.next

        added_list = list(map(int, str(int(str1) + int(str2))))

        return self.reverseList(list_to_linked_list(added_list))
    
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


l1 = [2,4,3]
l2 = [5,6,4]
linked_list_l1 = list_to_linked_list(l1)
linked_list_l2 = list_to_linked_list(l2)
solution = Solution()
added_linked_list = solution.addTwoNumbers(linked_list_l1, linked_list_l2)
output_list = linked_list_to_list(added_linked_list)
print(output_list)