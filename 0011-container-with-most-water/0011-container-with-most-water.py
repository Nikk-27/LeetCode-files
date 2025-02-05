class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_area = 0
        while l < r:
            cur_ht = min(height[l], height[r])
            cur_wd = r - l
            area = cur_ht * cur_wd
            max_area = max(max_area, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area

# TC = O(n)
# SC = O(1)