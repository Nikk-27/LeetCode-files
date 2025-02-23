class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        a = 1
        b = 2
        c = 3

        for i in range(3, n+1):
            c = a + b
            temp_b = b
            b = c
            a = temp_b
        return c

# Space optimized bottom up DP Approach

# TC = O(n)
# SC = O(1)