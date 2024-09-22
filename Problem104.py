# 104 Maximum Depth of Binary Tree

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:                # TC : O(N) SC : Best case - O(Log N), Worst case - O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

# Utility function to create a binary tree from a list of values
def create_tree(values: List[Optional[int]]) -> TreeNode:
    if not values:
        return None
    
    def insert_level_order(arr, root, i, n):
        if i < n:
            temp = TreeNode(arr[i])
            root = temp
            
            # Insert left child
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
            
            # Insert right child
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
        
        return root
    
    return insert_level_order(values, None, 0, len(values))

# Example usage
root = [1,None,2]    #[3,9,20,null,null,15,7]
b_tree = create_tree(root)
solution = Solution()
max_depth = solution.maxDepth(b_tree)
print(max_depth)

'''
Space Complexity (SC)
The space complexity of the function is determined by the depth of the recursion stack, which depends on the height of the binary tree.

In the worst case, the height of the tree (h) can be n (in case of a skewed tree where each node has only one child).
In the best case, the height of the tree (h) is logn (in case of a balanced tree).
'''