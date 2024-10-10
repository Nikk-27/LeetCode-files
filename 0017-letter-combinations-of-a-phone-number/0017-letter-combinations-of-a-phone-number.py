class Solution:

    def __init__(self):
        # Mapping from digit to corresponding letters on the phone pad
        self.digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        self.result = []

    def backtrack(self, combination: str, next_digits: str):
        
        # If no more digits are left, we have a complete combination
        if len(next_digits) == 0:
            self.result.append(combination)
        else:
            # Process the next digit and its corresponding letters
            for letter in self.digit_to_char[next_digits[0]]:
                print(letter)
                # Append current letter to the combination and move to the next digit
                self.backtrack(combination + letter, next_digits[1:])
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []  # If input is empty, return an empty list
        
        # Start the backtracking with an empty combination and the full digit string
        self.result = []
        self.backtrack("", digits)
        return self.result


'''
O(3^N∗4^M)

Time Complexity (TC):
O(3^n) and O(4^n):
If every digit in the input string mapped to exactly 3 letters (like the digits 2, 3, etc.), the total number of possible combinations would be 3 choices per digit. Hence, if there are n digits, you would generate: 3×3×3×⋯=3^n combinations.
On the other hand, if every digit in the input string mapped to exactly 4 letters (like the digits 7 and 9), the total number of possible combinations would be: 4×4×4×⋯=4^n combinations.
Why the complexity is O(4^n) (worst case)?
In the worst-case scenario, the digits 7 and 9 could appear more frequently, meaning that each digit maps to 4 letters. This is why we consider the time complexity as: O(4^n)
This assumes that we have to explore 4 branches at each digit, leading to 4^n combinations.

Space Complexity (SC):
Result Storage:
The result list stores all possible combinations of letters. The number of combinations can be as large as 4^n in the worst case, and each combination is a string of length n. Therefore, the space required for storing all the combinations is: O(n*4^n)
This accounts for storing the 4^n combinations, each of length n.
Call Stack (Recursion):
The maximum depth of recursion is n, where n is the length of the input string. So the space required for the recursion stack is O(n).
Overall Space Complexity:
The total space complexity is the sum of the space for storing results and the recursion stack: O(n*4^n)+O(n)
This simplifies to: O(n*4^n)
'''
