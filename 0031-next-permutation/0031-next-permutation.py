# TC = O(N)

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the first decreasing element from the right
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        
        # Step 2: If the array is not entirely in descending order
        if i != 0:
            # Find the element just larger than nums[i-1] from the right
            index = i
            for j in range(n - 1, i - 1, -1):
                if nums[j] > nums[i - 1]:
                    index = j
                    break
            
            # Swap nums[i-1] with nums[index]
            nums[i - 1], nums[index] = nums[index], nums[i - 1]
        
        # Step 3: Reverse the array from i to the end
        nums[i:] = reversed(nums[i:])
