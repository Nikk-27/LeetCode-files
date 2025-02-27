# Prefix and suffix way
# TC = O(n)
# SC = O(1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums) # size of array.

        pre, suff = 1, 1
        ans = float('-inf')
        for i in range(n):
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre *= nums[i]
            suff *= nums[n - i - 1]
            ans = max(ans, max(pre, suff))
        return ans

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float('-inf')
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                result = max(result, prod)
        return result


# Brute force exceeds time
# TC = O(n^2)
# SC = O(1)

'''