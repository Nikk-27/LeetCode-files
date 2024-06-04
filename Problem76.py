#76 Minimum Window Substring

# we used hashmaps

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        print("countT ", countT)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            print("window ", window)

            if c in countT and window[c] == countT[c]:
                have += 1

            print(c," have ", have)
            while have == need:
                print("1")
                #update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]: #we removed therefore window < count
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
    
s = "ADOBECODEBANC"
t = "ABC"

# s = "a"
# t = "a"

solution = Solution()
print(solution.minWindow(s, t))