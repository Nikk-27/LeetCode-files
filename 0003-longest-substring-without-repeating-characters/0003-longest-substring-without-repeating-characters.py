class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        new_set = set()
        for r in range(len(s)):
            while s[r] in new_set:
                new_set.remove(s[l])
                l += 1
            new_set.add(s[r])
            res = max(res, r-l+1)
        return res

# TC = O(n)
# SC = O(m)