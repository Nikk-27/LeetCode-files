#### BFS ####

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c, q):
            
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                rr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = rr + dr, cc + dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr]   [nc]!= "1"):
                        continue
                    grid[nr][nc] = "0"
                    q.append((nr,nc))

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c, q)
        return count

# Time complexity: O(m∗n)
# Space complexity: O(m∗n)


#### DFS ####

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:

#         def dfs(r, c):
#             if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != "1"):
#                 return
#             grid[r][c] = "0"
#             dfs(r+1, c)
#             dfs(r-1, c)
#             dfs(r, c+1)
#             dfs(r, c-1)
#         ROWS = len(grid)
#         COLS = len(grid[0])
#         count = 0
#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == "1":
#                     count += 1
#                     dfs(r, c)
#         return count

'''
Time Complexity:
DFS Traversal: Each cell in the grid is visited once. The DFS explores in four directions (up, down, left, right) but each cell is processed at most once, so the time complexity is proportional to the number of cells in the grid.
If the grid has m rows and n columns, the time complexity is O(m * n).

Space Complexity:
Recursive DFS Stack: The depth of the recursion can go as deep as the number of cells in the worst case. Therefore, the space used by the recursion stack is O(m * n) in the worst case.
'''