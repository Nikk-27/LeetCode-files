class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []  # To store all the permutations
        
        # Helper function to generate permutations
        def backtrack(temp, nums):
            if len(temp) == len(nums):
                result.append(temp[:])  # Add a copy of the current permutation to the result
                return
            
            # Try placing each number in the available numbers list
            for i in range(len(nums)):
                # Choose a number and explore further
                if nums[i] not in temp: 
                  temp.append(nums[i])  # Include the number
                  backtrack(temp, nums)
                # Backtrack (remove the last number to try the next possibility)
                  temp.pop()
        
        backtrack([], nums)  # Initial call to start the backtracking
        return result


'''
### Time Complexity:
- **Time complexity**:  O(n * n!) 
  - There are n! permutations, and each permutation takes O(n) time to construct because we need to append and store each permutation.
  
### Space Complexity:
- **Space complexity**: O(n * n!)
  -  O(n * n!) space is required to store all n! permutations, and each permutation is of length  n .
  - The recursion stack uses  O(n)  space for the depth of recursive calls.
'''