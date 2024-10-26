class Solution:
    def __init__(self):
        self.sum = 0

    def dfs(self, row, col, grid):
        if (row < 0 or col < 0 or 
        row >= len(grid) or col >= len(grid[0]) or 
        grid[row][col] != 1):
            return

        grid[row][col] = "$"
        self.sum += 1

        # Explore all four directions (up, down, left, right)
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        answer = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count += 1
                    self.sum = 0
                    self.dfs(i, j, grid)
                    print(self.sum)
                    answer.append(self.sum)
        return max(answer) if answer else 0


'''
Time Complexity: 
O(rows×cols) — Each cell is visited once.
Space Complexity: 
O(rows×cols) — Due to recursion stack and answer list.
'''