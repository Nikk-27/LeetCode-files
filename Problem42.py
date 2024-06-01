#42 Trapping Rain Water

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        res = 0
        maxleft, maxright = 0, 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    res += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    res += maxright - height[right]
                right -= 1

        return res


# height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution = Solution()
print(solution.trap(height))
