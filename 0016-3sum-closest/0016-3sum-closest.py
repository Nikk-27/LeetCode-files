class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        closestSum = 100000
        for i in range(0,n-2):
            l = i+1
            r = n-1
            while(l < r):
                sum = nums[l] + nums[r] + nums[i]
                if abs(target-sum) < abs(target-closestSum):
                    closestSum = sum
                if sum > target : 
                    r = r - 1
                else:
                    l = l + 1

        return closestSum