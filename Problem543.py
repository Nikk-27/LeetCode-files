#543 Diameter of Binary Tree

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, root: Optional[TreeNode], result) -> int:
        if root is None:
            return 0
        
        # print(root.left.val, root.right.val)
        left_depth = self.dfs(self, root.left)
        right_depth = self.dfs(self, root.right)

        self.diameter = left_depth + right_depth
        print(1 + max(left_depth, right_depth))
        print(left_depth, right_depth, self.diameter, self.result)

        return 1 + max(left_depth, right_depth)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        self.diameter = 0
        self.result = 0
        self.dfs(self, root, self.result)
        return self.result

        
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

# Utility function to print the binary tree in level order
def print_tree(root: TreeNode) -> List[Optional[int]]:
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Example usage
# values = [4, 2, 7, 3, 1, 6, 9]
values = [1, 2, 3, 4, 5]
root = create_tree(values)
print(print_tree(root))
solution = Solution()
l = solution.diameterOfBinaryTree(root)
print(l)
