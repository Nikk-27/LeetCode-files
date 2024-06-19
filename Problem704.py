# 704 Binary Search

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = left + ((right - left) // 2) # Overflow-Safe Middle Calculation
        
        # Check if target is present at mid
            if nums[mid] == target:
                return mid
        # If target is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1
        # If target is smaller, ignore right half
            else:
                right = mid - 1
        
        return -1


nums = [-1,0,3,6,9,12]
target = 6
solution = Solution()
print(solution.search(nums, target))