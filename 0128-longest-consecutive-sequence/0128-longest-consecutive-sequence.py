from typing import List

class Solution:
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



                
