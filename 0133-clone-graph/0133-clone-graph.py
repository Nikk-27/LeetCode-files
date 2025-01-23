"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#### DFS ####
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldtonew = {}

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]

            copy_node = Node(node.val)
            oldtonew[node] = copy_node

            for neighbour in node.neighbors:
                copy_node.neighbors.append(dfs(neighbour))

            return copy_node
            

        return dfs(node) if node else None


#TC = O(V+E)
#SC = O(V)    