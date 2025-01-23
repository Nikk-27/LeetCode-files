#### BFS ####

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        def bfs(r, c, q, sum):
            grid[r][c] = 0
            sum += 1
            q.append((r,c))

            while q:
                rr, cc = q.popleft()
                for dr, dc in directions:
                    nr, nc = rr+dr, cc+dc
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 0
                    sum += 1
                    q.append((nr, nc))
            return sum

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()

        sum = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    sum = max(bfs(r, c, q, 0), sum)
        return sum

# Time complexity: O(m∗n)
# Space complexity: O(m∗n)


#### DFS ####

# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

#         def dfs(r, c):
#             if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1):
#                 return 0
#             grid[r][c] = 0

#             return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

#         ROWS = len(grid)
#         COLS = len(grid[0])

#         sum = 0

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if grid[r][c] == 1:
#                     sum = max(dfs(r, c), sum)
#         return sum



'''
Time Complexity: 
O(rows×cols) — Each cell is visited once.
Space Complexity: 
O(rows×cols) — Due to recursion stack and answer list.
'''