#Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        max_length = 0  # This will store the length of the longest substring without repeating characters
        start = 0       # This will keep track of the start of the current substring
        seen_chars = set()  # This set will store characters of the current substring
        
        # Iterate over each character in the string `s`
        for end in range(len(s)):
            # If the current character at `end` is already in `seen_chars` (meaning it's a repeating character)
            while s[end] in seen_chars:
                # Remove characters from the start of the current substring until the first occurrence of `s[end]` is removed
                seen_chars.remove(s[start])
                start += 1  # Move the start pointer forward
            
            # Add the current character at `end` to `seen_chars` to mark it as seen
            seen_chars.add(s[end])
            
            # Calculate the length of the current substring (end - start + 1)
            current_length = end - start + 1
            
            # Update `max_length` to be the maximum of its current value and the length of the current substring
            max_length = max(max_length, current_length)

        # Return the maximum length of a substring without repeating characters found
        return max_length

# Example usage:
s = "abcba"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))