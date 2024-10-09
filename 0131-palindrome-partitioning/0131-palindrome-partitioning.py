class Solution:
    def __init__(self):
        self.result = []

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
        
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(start, path):
            if start == len(s):
                self.result.append(path[:])
                return
            
            for i in range(start+1, len(s)+1):
                substr = s[start:i]
                if self.is_palindrome(substr):
                    backtrack(i, path + [s[start:i]])
        
        backtrack(0, [])
        return self.result

'''
Overall Time Complexity:
The worst-case scenario involves generating all possible partitions of the string (which takes 2^n) and performing a palindrome check for each substring. For each partition, the palindrome check may take O(n) time.
Thus, the overall time complexity is approximately: O(n * 2^n), n is the length of the input string.

Space Complexity:
Call Stack (Recursive Depth) : The maximum depth of the recursion is determined by the number of characters in the string. In this case, the recursion goes as deep as 3 because there are 3 characters in "aab". At most, the call stack depth is O(n), which is O(3) in this case.

Each partition takes space proportional to the length of the string. The total space required to store these partitions is O(n * 2^n), where n is the length of the string, and 2^n represents the number of possible partitions. In this case:
["a", "a", "b"] requires 3 units of space.
["aa", "b"] requires 2 units of space.
'''