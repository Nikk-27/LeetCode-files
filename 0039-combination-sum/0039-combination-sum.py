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

'''
Let's analyze the **time complexity** and **space complexity** of the corrected **Combination Sum** solution:

### Time Complexity:

The time complexity is influenced by both the **number of recursive calls** and the **number of combinations** that can be generated.

1. **Recursion Tree**:
   - The recursion generates combinations of elements that sum up to the target.
   - For each element, you decide either to:
     - Include the element and **recurse with the same index** (since you can use the same element multiple times).
     - Exclude the element and move to the next index.
   - The branching factor at each recursive call is \( n \) (the number of candidates).

2. **Maximum Depth**:
   - The depth of the recursion depends on how many times a candidate can be included.
   - If the smallest candidate is \( M \), the recursion depth can be up to \( \frac{T}{M} \), where \( T \) is the target.

3. **Time Complexity Estimate**:
   - In the worst case, the recursion explores every possible combination of elements. The number of combinations is roughly \( O(n^{T/M}) \), where:
     - \( n \) is the number of candidates.
     - \( T \) is the target.
     - \( M \) is the smallest candidate.

### Example Explanation:
- If the target is large relative to the smallest candidate (e.g., if you have a target of 100 and a candidate of 1), the recursion could explore a very large number of combinations.

Thus, the **worst-case time complexity** is approximately:
\[
O(n^{T/M})
\]
where:
- \( n \) is the number of candidates.
- \( T \) is the target.
- \( M \) is the smallest candidate in the list.

### Space Complexity:

1. **Recursion Depth**:
   - The maximum recursion depth is \( \frac{T}{M} \), where \( M \) is the smallest candidate, because in the worst case, we keep subtracting the smallest candidate from the target until it reaches 0.
   - Each recursive call adds a new frame to the call stack, so the **recursion stack** can take \( O(T/M) \) space.

2. **Space for Storing Results**:
   - The space used to store the valid combinations depends on the number of combinations generated. In the worst case, there could be \( O(r) \) valid combinations, where \( r \) is the number of combinations, and each combination can be as large as \( T/M \).
   - Each valid combination is stored in the result, and the result space depends on how many combinations are generated.

Thus, the **space complexity** is:
\[
O(T/M + r)
\]
where:
- \( T \) is the target.
- \( M \) is the smallest candidate.
- \( r \) is the number of valid combinations generated.

### Summary:

- **Time Complexity**: \( O(n^{T/M}) \), where \( n \) is the number of candidates, \( T \) is the target, and \( M \) is the smallest candidate.
- **Space Complexity**: \( O(T/M + r) \), where \( r \) is the number of combinations generated, and \( T/M \) is the maximum depth of the recursion.

Both time and space complexities are exponential due to the large number of potential combinations, especially when the target value is large relative to the smallest candidate.
'''