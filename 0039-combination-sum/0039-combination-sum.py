class Solution:
    def __init__(self):
        self.result = []

    def solve(self, candidates, idx, target, temp):
        if target == 0:  # Base case: target is reached
            self.result.append(temp[:])  # Make a copy of temp and add to result
            return
        if target < 0:  # If the target becomes negative, no need to proceed further
            return
        
        for i in range(idx, len(candidates)):
            temp.append(candidates[i])  # Include the current element
            # Call solve recursively with the same index `i` (since you can reuse the same element)
            self.solve(candidates, i, target - candidates[i], temp)
            temp.pop()  # Backtrack to try the next candidate
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []  # Clear previous results
        self.solve(candidates, 0, target, [])
        return self.result