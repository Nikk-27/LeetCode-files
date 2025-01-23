class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1):
                return 0
            grid[r][c] = 0

            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1))

        ROWS = len(grid)
        COLS = len(grid[0])

        sum = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    sum = max(dfs(r, c), sum)
        return sum



'''
Time Complexity: 
O(rows×cols) — Each cell is visited once.
Space Complexity: 
O(rows×cols) — Due to recursion stack and answer list.
'''