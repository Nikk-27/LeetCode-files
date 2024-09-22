#100 Same Tree

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


class Solution:

    def __init__(self):
        self.result = True

    def checkSimilarity(self, p, q) -> bool:
        if not p and not q: 
            return self.result
        if not p and q:
            self.result = False
            return self.result
        if p and not q:
            self.result = False
            return self.result
        if p.val == q.val:
            self.checkSimilarity(p.left, q.left)
            self.checkSimilarity(p.right, q.right)
        else:
            self.result = False
        return self.result
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:       #TC : O(N)  SC: O(N)
        self.checkSimilarity(p, q)
        return self.result
    
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


# Example usage
# p = [1,2,3], q = [1,2,3]
# p = [1,2], q = [1,None,2]
p = [1,2,1]
q = [1,1,2]
p_tree = create_tree(p)
q_tree = create_tree(q)
solution = Solution()
print(solution.isSameTree(p_tree, q_tree))