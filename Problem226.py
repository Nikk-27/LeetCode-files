#226 Invert Binary Tree

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:                                        # TC : O(N) SC : O(N)
     def invertTree(self, root: TreeNode) -> TreeNode:     # mirror/flip BT
        if root is None:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

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
values = [4, 2, 7, 1, 3, 6, 9]
root = create_tree(values)
solution = Solution()
inverted_root = solution.invertTree(root)
print(print_tree(inverted_root))


# recursive method uses depth-first traversal to swap nodes, while the iterative method uses breadth-first traversal (level order) with a queue to swap nodes.

'''
LEVEL ORDER

TreeNode invertTree(TreeNode root) {
  if (root == null) {
    return null;
  }

  final Queue<TreeNode> queue = new LinkedList<>();
  queue.add(root);

  while (!queue.isEmpty()) {
    final TreeNode node = queue.poll();

    // Swap nodes
    final TreeNode temp = node.left;
    node.left = node.right;
    node.right = temp;

    // Add left and right of this node to the queue
    if (node.left != null) queue.add(node.left);

    if (node.right != null) queue.add(node.right);
  }
  return root;
}
'''