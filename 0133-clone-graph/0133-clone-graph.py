"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

#### BFS ####

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def bfs(start_node: 'Node') -> 'Node':
            oldtonew = {}
            q = deque([start_node])

            # Create the clone for the starting node
            oldtonew[start_node] = Node(start_node.val)

            while q:
                cur = q.popleft()

                for nei in cur.neighbors:
                    # If the neighbor is not cloned yet, clone it
                    if nei not in oldtonew:
                        oldtonew[nei] = Node(nei.val)
                        q.append(nei)
                    # Add the cloned neighbor to the current node's clone
                    oldtonew[cur].neighbors.append(oldtonew[nei])

            return oldtonew[start_node]

        return bfs(node)

#TC = O(V+E)
#SC = O(V) 


#### DFS ####

# from typing import Optional
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         oldtonew = {}

#         def dfs(node):
#             if node in oldtonew:
#                 return oldtonew[node]

#             copy_node = Node(node.val)
#             oldtonew[node] = copy_node

#             for neighbour in node.neighbors:
#                 copy_node.neighbors.append(dfs(neighbour))

#             return copy_node
            

        # return dfs(node) if node else None

#TC = O(V+E)
#SC = O(V)    