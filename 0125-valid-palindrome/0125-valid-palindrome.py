class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum():
                new_str += i.lower()
        l = 0
        r = len(new_str)-1
        while l < r:
            if new_str[l] == new_str[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

# TC = O(N)
# SC = O(N)