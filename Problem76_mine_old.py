#76 Minimum Window Substring

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        s = s.upper()
        t = t.upper()

        if len(t) > len(s):
            return None
        
        m = [0] * 26

        for c in t:
            m[ord(c) - ord('A')] += 1

        print(' a',' b',' c',' d',' e',' f',' g',' h',' i',' j',' k',' l',' m',' n',' o',' p',' q',' r',' s',' t',' u',' v',' w',' x',' y',' z')
        print(m)

        i = 0
        total_chars = len(t)
        found_len = len(s)
        # found_string = ''
        found_dict = {}

        for j in range(len(s)):
            if m[ord(s[j]) - ord('A')] > 0:
                total_chars -= 1
                
            m[ord(s[j]) - ord('A')] -= 1
            print("total_chars ", total_chars, s[j])
            print("******")
            print(m)

            if total_chars == 0:
                found_len = min(found_len, j - i + 1)
                print("found_len ", found_len)
                print(i,j)
                found_string = ''
                for k in range(i, j+1):
                    found_string += s[k]
                    print("found_string", found_string)
                    if m[ord(s[k]) - ord('A')] >= 0:
                        total_chars += 1
                    m[ord(s[k]) - ord('A')] += 1
                found_dict[(found_len, i)] = found_string
                print(found_dict)
                # total_chars = len(t)
                # m = [0] * 26
                # for c in t:
                #     m[ord(c) - ord('A')] += 1
                i = j+1

            print("i,j ", i,j)        
            
                
        return found_string
            
s = "ADOBECODEBANC"
t = "ABC"

# s = "a"
# t = "a"

solution = Solution()
print(solution.minWindow(s, t))