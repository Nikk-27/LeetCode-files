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


'''
Time Complexity (TC):
In the worst case, from each cell, we could explore all four directions for every letter in the word. If the word's 
length is k, we might make up to 4^k recursive calls from each starting cell. where m is the number of rows, n is the number of columns, and k is the length of the word. O(m*n*4^k)

Space Complexity (SC):
The space complexity is dominated by the visited matrix, which is O(m*n), plus the recursion stack space of O(k). 
Therefore, the overall space complexity is: O(m*n+k)
'''