#230 Kth Smallest Element in a BST

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

# Utility function to create a binary tree from a list of values
def create_tree(values: List[Optional[int]]) -> TreeNode:
    if not values:
        return None
    
    def insert_level_order(arr, root, i, n):
        if i < n and arr[i] is not None:
            temp = TreeNode(arr[i])
            root = temp
            
            # Insert left child
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
            
            # Insert right child
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
        
        return root
    
    return insert_level_order(values, None, 0, len(values))


root = [3,1,4,None,2]
k = 1
root_tree = create_tree(root)
solution = Solution()
print(solution.kthSmallest(root_tree, k))


# We have implemented **Iterative In-order Traversal** -> pushing nodes to the stack as you go left and processing them in ascending order. where :
# Time Complexity: O(N) in the worst case, where NN is the number of nodes.
# Space Complexity: O(h), where hh is the height of the tree due to the stack usage.