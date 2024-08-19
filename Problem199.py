#199 Binary Tree Right Side View

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        output_list = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            # print("level_size: ", level_size)
            
            for i in range(level_size):
                cur_node = queue.popleft()

                # print(cur_node.val)

                if cur_node.left:               
                    queue.append(cur_node.left)
                
                if cur_node.right: 
                    queue.append(cur_node.right)         
            if level_size == 2:
                if i == 1:
                    output_list.append(cur_node.val)
            else:
                output_list.append(cur_node.val)
        
        return output_list
    

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


# root = [1,2,3,None,5,None,4]
root = [1,2,3,4]
root_tree = create_tree(root)
solution = Solution()
print(solution.rightSideView(root_tree))