#138 Copy List with Random Pointer

from typing import Optional, List, Tuple

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    # def __str__(self):
    #     random_val = f'{self.random.val}' if self.random else 'None'
    #     return f'({self.val}) -> Random: {random_val}'


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':                    #TC : O(N), SC : O(N)
        oldToCopy = { None : None }

        cur = head
        while cur:
            copy = Node(cur.val)
            # print_linked_list(copy)
            # print_linked_list(cur)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]



def list_to_linked_list(arr: List[Tuple[int, int]]) -> Optional[Node]:
    if not arr:
        return None
    
    # Create all nodes
    nodes = [Node(val) for val, _ in arr]
    
    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set random pointers
    for node, (_, random_index) in zip(nodes, arr):
        if random_index is not None:
            node.random = nodes[random_index]
    
    return nodes[0]

# Helper function to print the linked list
def print_linked_list(head: Node) -> None:
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage
values = [[7,None],[13,0],[11,4],[10,2],[1,0]]
linked_list = list_to_linked_list(values)
solution = Solution()
copied_linked_list = solution.copyRandomList(linked_list)
print("Copied Linked list:")
print_linked_list(copied_linked_list)
