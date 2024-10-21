class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build a Trie with all words
        self.trie = self.buildTrie(words)
        self.result = set()  # To avoid duplicates

        # Start DFS from each cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board, row, col, self.trie, "")

        return list(self.result)

    def buildTrie(self, words: List[str]) -> TrieNode:
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.endOfWord = True
        return root

    def dfs(self, board, row, col, node, path):
        # If out of bounds or the character is not part of the Trie, stop
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0])
            or board[row][col] not in node.children):
            return
        
        char = board[row][col]
        node = node.children[char]
        path += char

        # If we found a word, add it to the result set
        if node.endOfWord:
            self.result.add(path)

        # Mark the current cell as visited by changing it to '#'
        temp = board[row][col]
        board[row][col] = "#"

        # Explore all four directions (up, down, left, right)
        self.dfs(board, row + 1, col, node, path)
        self.dfs(board, row - 1, col, node, path)
        self.dfs(board, row, col + 1, node, path)
        self.dfs(board, row, col - 1, node, path)

        # Backtrack: Restore the original character
        board[row][col] = temp

'''
Time Complexity:
Building Trie: O(N * L), where N is the number of words and L is the average length of the words.
DFS Search: O(m * n * 4^L), where m * n is the board size and L is the maximum word length (4 directions per cell).

Space Complexity:
Trie Storage: O(N * L) for storing the words.
Visited Matrix: O(m * n) for the board.
DFS Call Stack: O(L) for recursive depth.
Total space: O(N * L + m * n + L).
'''