# 33 Search in Rotated Sorted Array

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target == nums[m]: 
                return nums[m], m   

            # Left half is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: 
                    l = m + 1  
            # Right half is sorted  
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1                   # TC: O(log n)
        return -1
                

nums = [4,5,6,7,0,1,2]
target = 8
solution = Solution()
print(solution.search(nums, target))