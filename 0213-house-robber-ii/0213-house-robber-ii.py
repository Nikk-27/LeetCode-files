# 
#     Case-1 (Take from 1st House - Hence skip the last house)
#     Case-2 (Take from 2nd House - Hence take the last house)
# 
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(arr):
            t = [0] * (len(arr) + 1)  # DP array
            for i in range(1, len(arr) + 1):
                t[i] = max(t[i - 1], arr[i - 1] + (t[i - 2] if i - 2 >= 0 else 0))
            return t[len(arr)]

        # Case-1: Rob from house 0 to n-2 (skip last house)
        result1 = rob_linear(nums[:-1])

        # Case-2: Rob from house 1 to n-1 (skip first house)
        result2 = rob_linear(nums[1:])

        return max(result1, result2)    


# TC = O(N)
# SC = O(N)

# ------------------------------------------------------------------------------------------
# Bottom up with constant space 

# TC = O(N)
# SC = O(1)

'''
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def rob_range(nums, l, r):
            prevPrev, prev = 0, 0
            for i in range(l, r + 1):
                temp = max(prev, nums[i] + prevPrev)
                prevPrev, prev = prev, temp
            return prev

        return max(rob_range(nums, 0, n - 2), rob_range(nums, 1, n - 1))

'''