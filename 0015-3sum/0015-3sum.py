#T.C : O(n^2)
#S.C : O(1)

class Solution:
    def __init__ (self):
        self.result = []
    def twoSum(self, nums: List[int], target: int, left: int, right: int):
        l = left
        r = right
        while l < r:
            if (nums[l] + nums[r]) > target:
                r -= 1
            elif (nums[l] + nums[r]) < target:
                l += 1
            else:
                self.result.append([-target, nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        self.result = []

        nums.sort()

        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            self.twoSum(nums, target, i+1, n-1)
        return self.result
        

        