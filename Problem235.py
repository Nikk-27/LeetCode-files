#235 Lowest Common Ancestor of a Binary Search Tree

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        while cur:
            # print(cur.val)
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur.val

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

root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 4
root_tree = create_tree(root)
p = TreeNode(p)
q = TreeNode(q)
solution = Solution()
print(solution.lowestCommonAncestor(root_tree, p, q))

'''
TC: of the lowestCommonAncestor function is O(h), where 
ℎ is the height of the binary search tree. In the worst case, this could be 𝑂(𝑁) for a skewed tree, where 𝑁 is the number of nodes. However, for a balanced tree, it would be 𝑂(logN).

Space Complexity:
The space complexity is O(1) since the solution only uses a constant amount of extra space for variables like cur 
'''