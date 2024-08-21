#98 Validate Binary Search Tree

from typing import Optional, List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def checkBST(root, minValue, maxValue):
            # print(root.val if root else 0)
            # print(minValue, maxValue)
            if not root:
                return True
            
            if not (minValue < root.val < maxValue):
                return False
            
            left_is_valid = checkBST(root.left, minValue, root.val)
            right_is_valid = checkBST(root.right, root.val, maxValue)
            
            return left_is_valid and right_is_valid
        
        # Initial call with the full range of possible values
        return checkBST(root, float('-inf'), float('inf'))

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


# root = [2,1,3]
root = [5,4,6,None,None,3,7]
root_tree = create_tree(root)
solution = Solution()
print(solution.isValidBST(root_tree))

#  Time Complexity: O(n)
   # Space Complexity: O(h), where h is the height of the tree (O(log n) for a balanced tree and O(n) for a completely unbalanced tree).