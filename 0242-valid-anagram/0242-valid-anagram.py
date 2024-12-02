class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(list(s), list(t), len(list(s)), len(list(t)))
        if sorted(list(s)) == sorted(list(t)) and len(list(s)) == len(list(t)):
            return True
        else:
            return False
        