#We start checking from last and gradually go towards beginner ind
# Recursion + memoization(DP)
# TC = O(N^2) + O(N^2) = O(N^2) -> one n^2 is for for loops circling on ind, ed and second n^2 is for making palin 2d array then just getting it in O(1) because we are memoizing that

class Solution:
    def __init__(self):
        self.is_palindrome = []
        self.is_calculated = []
        self.max_palindromes = []
        self.s = ""
    
    def is_palindrome_helper(self, st, ed):
        if st >= ed:
            return True
        if self.is_calculated[st][ed]:
            return self.is_palindrome[st][ed]
        
        self.is_calculated[st][ed] = True
        
        if self.s[st] == self.s[ed]:
            self.is_palindrome[st][ed] = self.is_palindrome_helper(st + 1, ed - 1)
        else:
            self.is_palindrome[st][ed] = False
        
        return self.is_palindrome[st][ed]
    
    def solve(self, ind, k, s):
        n = len(s)
        if ind == n:
            return 0
        
        if self.max_palindromes[ind] != -1:
            return self.max_palindromes[ind]
        
        ans = self.solve(ind + 1, k, s)
        
        for ed in range(ind + k - 1, n):
            if self.is_palindrome_helper(ind, ed):
                ans = max(ans, 1 + self.solve(ed + 1, k, s))
        
        self.max_palindromes[ind] = ans
        return ans
    
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        self.is_palindrome = [[False] * n for _ in range(n)]
        self.is_calculated = [[False] * n for _ in range(n)]
        self.max_palindromes = [-1] * n
        
        self.s = s
        return self.solve(0, k, s)
        