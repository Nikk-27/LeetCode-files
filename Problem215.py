#215 Kth Largest Element in an Array

from typing import List

class Solution:
    
    def swap(self, nums, x, y):
        nums[x], nums[y] = nums[y], nums[x]

    def partition_algo(self, nums, L, R):
        P = nums[L]
        i = L + 1
        j = R
        
        
        while i <= j:
            if nums[i] < P and nums[j] > P:
                self.swap(nums, i, j)
                i += 1
                j -= 1
                
            if nums[i] >= P:
                i += 1
            
            if nums[j] <= P:
                j -= 1

        self.swap(nums, L, j)
        return j  # P is at jth index
    
    def findKthLargest(self, nums, k):
        n = len(nums)
        L = 0
        R = n - 1
        pivot_idx = 0

        # k-th largest element in descending order
        while True:
            pivot_idx = self.partition_algo(nums, L, R)
            
            if pivot_idx == k - 1:
                break
            elif pivot_idx > k - 1:
                R = pivot_idx - 1
            else:
                L = pivot_idx + 1

        return nums[pivot_idx]

# Example usage:
solution = Solution()
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(solution.findKthLargest(nums, k))  # Output: 5

