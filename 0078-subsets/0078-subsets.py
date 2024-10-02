class Solution:
    def __init__(self):
        self.result = []

    def solve(self, nums, idx, temp):
        if idx >= len(nums):
            self.result.append(temp[:])  # Make a copy of temp and add to result
            return

        # Include the current element
        temp.append(nums[idx])
        self.solve(nums, idx + 1, temp)

        # Exclude the current element (backtrack)
        temp.pop()
        self.solve(nums, idx + 1, temp)

    def subsets(self, nums):
        temp = []
        self.solve(nums, 0, temp)
        return self.result
