class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
            
        preprev = 0
        prev = nums[0]
        temp = 0

        for i in range(2, len(nums)+1):
            steal = nums[i-1] + preprev
            skip = prev

            temp = max(steal, skip)
            preprev = prev
            prev = temp
        return temp 

# TC = O(n)
# SC = O(1)

# We have used Bottom up approach with contant space complexity