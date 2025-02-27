# Bottom up way but space optimized

# TC = O(n)
# SC = O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        count = 0

        if n == 1:
            return 1 if s[0] != '0' else 0
        if n == 0:
            return 0
        if s[0] == '0':
            return 0
            
        last2 = 1
        last1 = 1

        for i in range(1, n):
            count = last1 if s[i] != '0' else 0
            if (s[i-1] == '1' or (s[i-1] == '2' and int(s[i]) < 7)):
                count += last2

            last2 = last1
            last1 = count

        return last1

