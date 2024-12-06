class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Frequency arrays for s1 and the first window in s2
        s1Count = [0] * 26
        windowCount = [0] * 26

        # Fill frequency arrays
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            windowCount[ord(s2[i]) - ord('a')] += 1

        # Check the first window
        if s1Count == windowCount:
            return True

        # Slide the window over s2
        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character to the window
            windowCount[ord(s2[r]) - ord('a')] += 1
            # Remove the character going out of the window
            windowCount[ord(s2[l]) - ord('a')] -= 1
            l += 1

            # Check if the updated window matches
            if s1Count == windowCount:
                return True

        # If no match found
        return False
