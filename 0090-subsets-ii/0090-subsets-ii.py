class Solution:
    def __init__(self):
        self.result = []

    def solve(self, nums, idx, temp):
        # Base case: if idx exceeds the array length, add current subset to the result
        if idx >= len(nums):
            self.result.append(temp[:])  # Make a copy of temp and add to result
            return
        
        # Recursive case:
        # 1. Include the current element
        temp.append(nums[idx])
        self.solve(nums, idx + 1, temp)  # Recurse to include next element
        temp.pop()  # Backtrack to remove the current element
        
        # 2. Skip the current element (handle duplicates by skipping consecutive same elements)
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1  # Skip the duplicate
        self.solve(nums, idx + 1, temp)  # Recurse to skip the current element

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.solve(nums, 0, [])
        return self.result
        
'''
Time Complexity:
The total number of subsets is O(2^n), where n is the number of elements in the array.
Since we need to handle duplicates, sorting the array takes O(nlogn).
Therefore, the time complexity is O(nlogn+2^n).

Space Complexity:
The recursion stack depth is O(n) (since we go as deep as the number of elements).
The result list stores all subsets, which could be up to 2^n subsets, each of size O(n).
Therefore, the space complexity is O(2^n * n).
'''