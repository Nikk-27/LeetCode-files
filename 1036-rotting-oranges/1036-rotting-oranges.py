class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        for r in range(ROWS) :
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1:
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = 2
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


#TC = O(m*n)
#SC = O(m*n)
                    