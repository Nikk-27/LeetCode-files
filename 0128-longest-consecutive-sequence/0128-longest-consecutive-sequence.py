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



                
