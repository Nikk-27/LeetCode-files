class Solution:
    def solve(self, row, col, i, board, word, visited):
        # Base cases
        if i == len(word):  # If we've matched the entire word
            return True
        # print(board[row][col], word[i])
        if (row < 0 or row >= len(board) or 
            col < 0 or col >= len(board[0]) or 
            board[row][col] != word[i] or 
            visited[row][col]):  # Out of bounds, wrong letter, or already visited
            return False
        
        # Mark the cell as visited
        visited[row][col] = True
        
        # Explore all four directions (up, down, left, right)
        found = (self.solve(row + 1, col, i + 1, board, word, visited) or
                 self.solve(row - 1, col, i + 1, board, word, visited) or
                 self.solve(row, col + 1, i + 1, board, word, visited) or
                 self.solve(row, col - 1, i + 1, board, word, visited))
        
        # Unmark the cell after exploring (backtrack)
        visited[row][col] = False
        
        return found
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Initialize a visited matrix
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        # Try to start the word search from every cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.solve(row, col, 0, board, word, visited):
                    return True  # Word found
        
        return False  # Word not found