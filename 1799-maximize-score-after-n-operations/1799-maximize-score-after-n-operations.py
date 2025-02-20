#Approach-2 (Memoizing)

from math import gcd

class Solution:
    def __init__(self):
        self.n = 0  # Equivalent to C++ class variable

    def solve(self, nums, visited, operation, memo):
        visited_tuple = tuple(visited)  # Convert list to tuple for dictionary key (hashable)
        
        if visited_tuple in memo:
            return memo[visited_tuple]

        max_score = 0

        for i in range(self.n - 1):
            if visited[i]:
                continue

            for j in range(i + 1, self.n):
                if visited[j]:
                    continue

                visited[i] = True
                visited[j] = True

                curr_score = operation * gcd(nums[i], nums[j])
                remaining_score = self.solve(nums, visited, operation + 1, memo)
                max_score = max(max_score, curr_score + remaining_score)

                visited[i] = False
                visited[j] = False

        memo[visited_tuple] = max_score
        return max_score

    def maxScore(self, nums):
        self.n = len(nums)
        visited = [False] * self.n
        memo = {}  # Dictionary to store visited states
        return self.solve(nums, visited, 1, memo)

#TC = O(2^N * N^2 * log M)

# - each number either taken or not taken so 2^N
# - two for loops so N^2
# - to take gcd if biggest number M then log M
