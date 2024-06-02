#567. Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = [0] * 26  # character array
        for c in s1:
            m[ord(c) - ord('a')] += 1
        
        i = 0
        total_chars = len(s1)
        
        for j in range(len(s2)):
            if m[ord(s2[j]) - ord('a')] > 0:
                total_chars -= 1
            m[ord(s2[j]) - ord('a')] -= 1
            
            if total_chars == 0:
                return True
            
            if j - i + 1 == len(s1):
                if m[ord(s2[i]) - ord('a')] >= 0:
                    total_chars += 1
                m[ord(s2[i]) - ord('a')] += 1
                i += 1
        
        return False


s1 = "ab"
s2 = "eidbaooob"
solution = Solution()
print(solution.checkInclusion(s1, s2))