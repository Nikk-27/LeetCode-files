#23 Merge k Sorted Lists

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:                                 # TC : O(NLogK)    SC : O(LogK)

    def mergeTwoSortedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        if l1.val <= l2.val:
            l1.next = self.mergeTwoSortedLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLists(l1, l2.next)
            return l2
    
    def partitionAndMerge(self, start: int, end: int, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if start > end:
            return None
        
        if start == end:
            return lists[start]
        
        mid = start + (end - start) // 2

        l1 = self.partitionAndMerge(start, mid, lists)
        l2 = self.partitionAndMerge(mid + 1, end, lists)

        return self.mergeTwoSortedLists(l1, l2)
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        if k == 0:
            return None
        
        return self.partitionAndMerge(0, k - 1, lists)

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

# Convert input lists to linked lists
input_lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
linked_lists = [list_to_linked_list(lst) for lst in input_lists]

solution = Solution()
merged_k_list = solution.mergeKLists(linked_lists)
output_list = linked_list_to_list(merged_k_list)
print(output_list) 