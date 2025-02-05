class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

# TC = O(n^2)
# SC = O(1)



'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        mp = {}
        nums.sort()

        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1
            target = i
            while l < r:
                mp[nums[l]] -= 1

                if nums[l] + nums[r] == -nums[target]:
                    res.add((nums[target], nums[l], nums[r]))
                if nums[l] + nums[r] == -nums[target]:
                    l += 1
                if nums[l] + nums[r] > nums[target]:
                    r -= 1
                

            for i in mp:
                mp[i] += 1
        return [list(i) for i in res]

# TC = O(n^2)
# SC = O(n)     
'''


'''
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
                
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
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
        
'''