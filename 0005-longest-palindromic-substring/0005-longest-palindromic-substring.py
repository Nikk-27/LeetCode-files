# Expand Around Center
# TC = O(N^2)
# SC = O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        output_s = ""
        maxL = float('-inf')

        if n <= 1:
            return s
        
        def solve(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        for i in range(n):
            odd = solve(i, i)
            even = solve(i, i+1)

            if len(odd) > len(even) and len(odd) > maxL:
                output_s = odd
                maxL = len(odd)
            elif len(odd) < len(even) and len(even) > maxL :
                output_s = even
                maxL = len(even)
           
        return output_s

        
        