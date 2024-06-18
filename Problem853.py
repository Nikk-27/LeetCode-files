# 853 Car Fleet

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = list()
        print(sorted(zip(position, speed)))
        a = sorted(zip(position, speed))
        for i,j in a[::-1]: # Reverse sorted order
            stack.append((target-i)/j)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        print(len(stack))
        return len(stack)

target = 12
position  = [10,8,0,5,3]
speed = [2,4,1,1,3]
solution = Solution()
print(solution.carFleet(target, position, speed))