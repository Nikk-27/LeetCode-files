from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in numSet:
            length = 0
            if i-1 not in numSet:
                length += 1
                while i+1 in numSet:
                    i = i+1
                    length += 1
            longest = max(length, longest)
        return longest


# TC = O(N)
# SC = O(N) this method doesnt alter our original array


'''
nums = [100,4,200,1,3,2]
 
 we first do brute force:
 
 longest = 0
 for i in range(len(nums)):
     cur = nums[i]
     maxi = 1
     while cur + 1 in nums:
           cur += 1
           maxi += 1
     longest = max(longest, maxi)
  return longest
 
 this take TC = O(n^2) and SC = O(1)
 
 now we do sort method
 
 def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        new_num = sorted(nums)
        length = 0
        small = float(-inf)
         
        for i in range(len(new_num)):
            if new_num[i] - 1 == small:
                small = new_num[i]
                length += 1
            if new_num[i] != small:
                small = new_num[i]
                length = 1
            longest = max(length, longest)
        return longest

TC = O(n) + O(n)
SC = O(1)


'''

                
