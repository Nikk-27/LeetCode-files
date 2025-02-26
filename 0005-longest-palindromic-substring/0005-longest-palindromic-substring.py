# Bottom up way - Blueprint method
# TC = O(N^2)
# SC = O(N^2)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxL = float('-inf')
        idx = 0
        t = [[False] * n for _ in range(n)]

        for i in range(n):
            t[i][i] = True
            maxL = 1

        for L in range(2, n):
            for i in range(0, n-L+1):
                j = i+L-1

                if i+1 == j and s[i] == s[j]:
                    t[i][j] = True
                    maxL = 2
                    idx = i
                elif s[i] == s[j] and t[i+1][j-1]:
                    t[i][j] = True
                    if j-i+1 > maxL:
                        maxL = j-i+1
                    idx = i
        print(s[idx: idx+maxL])
        return s[idx: idx+maxL]



        