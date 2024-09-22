#25 Reverse Nodes in k-Group

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def lengthOfLinkedList(self, head):
        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length += 1
        
        return length
            
    
    def reverseKGroupH(self, head, k, length):
        if length < k:
            return head
        
        count, nex, prev, curr = 0, None, None, head
        while count < k and curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            count += 1
        
        if nex != None:
            head.next = self.reverseKGroupH(nex, k, length - k)
        
        return prev
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:     # TC : O(N), SC : O(1)
        
        length = self.lengthOfLinkedList(head)
        return self.reverseKGroupH(head, k, length)

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
k = 2
head_LL = list_to_linked_list(head)
solution = Solution()
reversed_kgroup = solution.reverseKGroup(head_LL, k)
output_list = linked_list_to_list(reversed_kgroup)
print(output_list)
        