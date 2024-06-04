#567 Permutation in String

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = [0] * 26 #character array
        for c in s1:
            m[ord(c) - ord('a')] += 1

        print('a',' b',' c',' d',' e',' f',' g',' h',' i',' j',' k',' l',' m',' n',' o',' p',' q',' r',' s',' t',' u',' v',' w',' x',' y',' z')
        print(m)

        i = 0
        total_chars = len(s1)

        for j in range(len(s2)):
            if m[ord(s2[j]) - ord('a')] > 0:
                total_chars -= 1
            m[ord(s2[j]) - ord('a')] -= 1
            # print(total_chars)
            # print(m)
            if total_chars == 0:
                return True
            
            #sliding window check
            if j - i + 1 == len(s1):
                # print(s2[i], i, ord(s2[i]), ord('a'), m[ord(s2[i]) - ord('a')])
                if m[ord(s2[i]) - ord('a')] >= 0:
                    total_chars += 1
                # print(total_chars)
                # print(m)
                m[ord(s2[i]) - ord('a')] += 1
                i += 1

        return False

s1 = "ab"
s2 = "efdbaooob"
solution = Solution()
print(solution.checkInclusion(s1, s2))