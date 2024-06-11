# #739 Daily Temperatures

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)      # TC = O(n)
        res = [0] * n
        stack = [] # stores indices

        for i in range(n):
            # if stack is not empty and also current temp > temp at the top of stack
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                days = i - prev_index
                res[prev_index] = days
                print("res ", res)
            stack.append(i)
            print("stack ", stack)
        return res



temperatures = [73,74,75,71,69,72,76,73]
solution = Solution()
print(solution.dailyTemperatures(temperatures))

