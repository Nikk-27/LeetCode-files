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
