class Solution:

    def dfs(self, row, col, grid):

        if (row < 0 or col < 0 or 
        row >= len(grid) or col >= len(grid[0]) or 
        grid[row][col] != '1'):
            return

        grid[row][col] = "$"

        # Explore all four directions (up, down, left, right)
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(i, j, grid)
        return count


'''
Time Complexity:
DFS Traversal: Each cell in the grid is visited once. The DFS explores in four directions (up, down, left, right) but each cell is processed at most once, so the time complexity is proportional to the number of cells in the grid.
If the grid has m rows and n columns, the time complexity is O(m * n).

Space Complexity:
Recursive DFS Stack: The depth of the recursion can go as deep as the number of cells in the worst case. Therefore, the space used by the recursion stack is O(m * n) in the worst case.
'''

