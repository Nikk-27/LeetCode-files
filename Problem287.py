#287 Find the Duplicate Number

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # new_hash = {}                      #TC : O(N), SC : O(N)
        # for i in range(len(nums)):
        #     if nums[i] not in new_hash:
        #         new_hash[nums[i]] = 1
        #         # print(new_hash)
        #     else:
        #         return nums[i]

        slow = nums[0]                       #TC : O(N), SC : O(1)
        fast = nums[0]

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast
    
nums = [1,3,4,2,2]
solution = Solution()
print(solution.findDuplicate(nums))