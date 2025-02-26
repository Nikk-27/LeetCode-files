# Expand Around Center
# TC = O(N^2)
# SC = O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        if n <= 1:
            return len(s)
        
        def solve(l, r):
            nonlocal count  # Declare count as nonlocal so we can modify it
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1

        for i in range(n):
            solve(i, i)
            solve(i, i+1)

            
        return count
