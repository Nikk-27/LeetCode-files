class Solution:

    def solve(self, candidates, target, temp, idx):
        if target == 0:  # Base case: target is reached
            self.result.append(temp[:])  # Make a copy of temp and add to result
            return
        if target < 0:  # If the target becomes negative, no need to proceed further
            return
        
        for i in range(idx, len(candidates)):
            # If the current element is a duplicate of the previous one, skip it
            if i > idx and candidates[i] == candidates[i - 1]:
                continue
            temp.append(candidates[i])
            self.solve(candidates, target-candidates[i], temp, i+1)
            temp.pop()
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()
        self.solve(candidates, target, [], 0)
        return self.result

'''
Time Complexity (TC)
Recursive Calls: For n candidates, the worst-case number of recursive calls is approximately O(2^n).
Space Complexity (SC)
The number of combinations could be as high as O(2^n), with each combination potentially containing up to n elements. This means that, in terms of storage, 
the space could reach O(n * 2^n) in the worst case when storing all unique combinations.
'''