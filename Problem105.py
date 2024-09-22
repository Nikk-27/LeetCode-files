#105 Construct Binary Tree from Preorder and Inorder Traversal

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
    
        # The first element of preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder array
        mid = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
print(solution.buildTree(preorder, inorder))

'''

The time and space complexity for reconstructing a binary tree from preorder and inorder traversal arrays can be analyzed as follows:

**Time Complexity**

- **Building the Tree**:
  - The main operation in each recursive call is finding the root node's index in the inorder array, which takes O(n) time if we do a linear search.
  - However, if we store the inorder indices in a hash map before starting the recursion, we can reduce this to O(1) time per lookup.
  - Given `n` nodes, each node is processed exactly once, and since we can find the index in O(1) time with a hash map, the overall time complexity is O(n).

- **Total Time Complexity**:
  - Without hash map optimization: O(n^2) (due to the linear search in the inorder array for each node).
  - With hash map optimization: O(n) (hash map lookup reduces the index finding operation to O(1)).

**Space Complexity**

- **Space for Recursion**:
  - The maximum depth of the recursion tree corresponds to the height of the binary tree.
  - In the worst case (for a skewed tree), the height can be `n`, leading to O(n) space due to the recursion stack.

- **Space for Hash Map**:
  - Storing the indices of the inorder array in a hash map requires O(n) space.

- **Total Space Complexity**:
  - Without hash map optimization: O(n) due to the recursion stack in the worst case.
  - With hash map optimization: O(n) for both the recursion stack and the hash map, so the overall space complexity remains O(n).

**Summary:**

- **Time Complexity**: O(n) with hash map optimization (or O(n^2) without it).
- **Space Complexity**: O(n) with the hash map and recursion stack combined.

*****************Check leetcode code************************* 

'''