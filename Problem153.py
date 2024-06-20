# 153 Find Minimum in Rotated Sorted Array

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        print(l,r)

        while l <= r:
            m = l + ((r - l) // 2)
            print("l: ", l, "r: ", r)
            print("m: ", m, ", nums[m]: ", nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r] and nums[m] > nums[m-1]:
                r = m - 1
            else: 
                return m, nums[m]       # TC: O(log n)
                

nums = [3,4,5,1,2]
solution = Solution()
print(solution.findMin(nums))