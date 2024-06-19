# 84 Largest Rectangle in Histogram

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair : (index, height)

        for i, h in enumerate(heights):
            print("i: ", i)
            start = i
            print("start: ", start)
            while stack and stack[-1][1] > h:
                print("stack[-1][1]: ", stack[-1][1])
                index, height = stack.pop()
                print("index, height: ", index, height)
                maxArea = max(maxArea, height * (i - index))
                print("maxArea: ", maxArea)
                start = index
            stack.append((start, h))
            print("stack: ", stack)

        print("stack_final: ", stack)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


heights = [2,1,5,6,2,3]
solution = Solution()
print(solution.largestRectangleArea(heights))