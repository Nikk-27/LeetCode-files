#Longest Repeating Character Replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_count = 0
        count = {}
        left = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])
            
            # Check if the window size is invalid
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len

# Example usage:
s = "AABAAB"
k = 1
solution = Solution()
print(solution.characterReplacement(s,k))