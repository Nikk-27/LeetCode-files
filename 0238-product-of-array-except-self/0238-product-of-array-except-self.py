class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prefix = 1
        result[0] = 1
        
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
            
        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]  
            result[i] *= postfix
        return result
            

# TC = O(N)
# SC = O(1)