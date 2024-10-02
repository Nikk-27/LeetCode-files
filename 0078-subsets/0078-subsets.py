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

'''
Let's break down the **time complexity** and **space complexity** of the Python implementation for generating all subsets of a given list of numbers.

### Time Complexity:

The function generates all possible subsets of a list of `n` elements.

1. **Total Number of Subsets**:
   - The number of subsets for a list of size `n` is \( 2^n \) because each element can either be included or excluded from the subset.
   
2. **Recursive Calls**:
   - For each element in the list, the recursive function is called twice:
     - Once where the element is included in the subset.
     - Once where the element is excluded.
   - Hence, there are \( 2^n \) recursive calls in total, because the function explores all possible combinations of including or excluding each element.

3. **Time to Process Each Subset**:
   - For each subset, copying the subset (`temp[:]`) takes O(k), where `k` is the length of the subset. On average, the length of the subset is O(n/2).
   - Thus, for each subset, copying the subset into `result` takes O(n) in the worst case.

4. **Total Time Complexity**:
   - The function makes \( 2^n \) recursive calls, and for each call, it takes O(n) time to process and store the subset.
   - Therefore, the **total time complexity** is \( O(n \cdot 2^n) \).

### Space Complexity:

1. **Space for the Result**:
   - The function generates all possible subsets, and there are \( 2^n \) subsets. The total number of elements across all subsets is:
     - \( \sum_{k=0}^{n} \binom{n}{k} \cdot k = n \cdot 2^{n-1} \), where \( \binom{n}{k} \) is the binomial coefficient.
   - So, the space needed to store all subsets is \( O(n \cdot 2^n) \).

2. **Space for Recursion**:
   - The depth of the recursion tree is `n`, so the recursion stack can go up to `n` levels deep.
   - Therefore, the maximum space used by the recursion stack is O(n).

3. **Temporary Space (`temp`)**:
   - The temporary list `temp` can hold up to `n` elements at most. However, this space is reused across recursive calls.

4. **Total Space Complexity**:
   - The total space complexity is dominated by the storage of the subsets and the recursion depth.
   - Hence, the **space complexity** is \( O(n \cdot 2^n) \) due to storing all subsets and the recursion stack.

### Conclusion:
- **Time Complexity**: \( O(n \cdot 2^n) \)
- **Space Complexity**: \( O(n \cdot 2^n) \)

Both time and space complexities are exponential due to the nature of generating all possible subsets of the list.
'''