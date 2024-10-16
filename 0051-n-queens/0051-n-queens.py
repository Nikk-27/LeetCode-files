# T.C : O(N!) in worst case it explores all possible configurations
# S.C : O(N) for result and also for storing, cols, diags and antidiags
#  Approach 2

class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int):
        if n == 0:
            return self.result

        board = ["." * n for _ in range(n)]  # Initialize the board with "..." for n = 3
        start_row = 0

        cols = set()  # Columns where queens are placed
        diags = set()  # Diagonals where queens are placed (row - col)
        anti_diags = set()  # Anti-diagonals where queens are placed (row + col)

        self.solve(board, start_row, cols, diags, anti_diags)
        return self.result

    def solve(self, board, row, cols, diags, anti_diags):
        if row == len(board):
            self.result.append(list(board))  # Add a valid configuration
            return

        for col in range(len(board)):
            diag_id = row - col
            anti_diag_id = row + col

            # If this column, diagonal, or anti-diagonal has a queen, skip it
            if col in cols or diag_id in diags or anti_diag_id in anti_diags:
                continue

            # Add this position as a potential spot for a queen
            cols.add(col)
            diags.add(diag_id)
            anti_diags.add(anti_diag_id)

            # Modify the row with a queen at (row, col)
            new_row = list(board[row])
            new_row[col] = 'Q'
            board[row] = ''.join(new_row)

            # Recur for the next row
            self.solve(board, row + 1, cols, diags, anti_diags)

            # Backtrack: Remove the queen and reset the row
            cols.remove(col)
            diags.remove(diag_id)
            anti_diags.remove(anti_diag_id)
            new_row[col] = '.'
            board[row] = ''.join(new_row)

'''
/*
    Time complexity for Approach-1 : O(N!)
    Unlike the brute force approach, we will only place queens on squares that aren't under attack.
    For the first queen, we have N options. For the next queen, we won't attempt to place it in the
    same column as the first queen, and there must be at least one square attacked diagonally by the
    first queen as well. Thus, the maximum number of squares we can consider for the second queen is
    (N−2). For the third queen, we won't attempt to place it in 2 columns already occupied by the first
    2 queens, and there must be at least two squares attacked diagonally from the first 2 queens.
    Thus, the maximum number of squares we can consider for the third queen is (N-4).
    This pattern continues, resulting in an approximate time complexity of O(N!)
*/

//Approach-1 (Simple dfs)
//T.C : O(N!) - Read the reason above
//S.C : O(N) to store the result


class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int) -> list:
        if n == 0:
            return self.result
        
        # Create an empty board
        board = ["." * n for _ in range(n)]  # For n = 3, board = ["...", "...", "..."] initially
        self.solve(board, 0)  # Start the recursion from row 0
        return self.result

    def isValid(self, board: list, row: int, col: int) -> bool:
        # Check upwards in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upwards in the left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check upwards in the right diagonal
        i, j = row, col
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True

    def solve(self, board: list, row: int):
        # Base case: if we've placed queens in all rows, add the solution
        if row == len(board):
            self.result.append(board[:])  # Make a copy of the board
            return

        # Try placing a queen in each column of the current row
        for col in range(len(board)):
            if self.isValid(board, row, col):
                # Place the queen at (row, col)
                new_row = board[row][:col] + 'Q' + board[row][col+1:]
                board[row] = new_row
                
                # Recur to place the queen in the next row
                self.solve(board, row + 1)
                
                # Backtrack: remove the queen (reset the row)
                board[row] = board[row][:col] + '.' + board[row][col+1:]

'''