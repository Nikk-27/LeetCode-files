#271. Encode and Decode Strings

from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the position of the delimiter '#'
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1  # Move past the '#'
            j = i + length
            res.append(s[i:j])
            i = j  # Move to the start of the next encoded string
            
        return res

Input = ["neet","code","love","you"]
solution = Solution()
print(solution.encode(Input))
encoded = solution.encode(Input)
print(solution.decode(encoded))
