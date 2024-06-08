#22 Generate Parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # brackets = { "(" : ")"}
        # stack = list()
        # count = 0
        # s = ""
        # b = []

        # for i in range(n):
        #     s += str(next(iter(brackets)))
        #     print("s ", s) 
        #     count += 1

        #     if count == n:
        #         while count > 0:
        #             s += str(next(iter(brackets.values())))
        #             print("s -> ", s)
        #             count -= 1
        # stack.append(s)
        # return stack
        def dfs(left, right, s):
            if len(s) == n * 2: 
                res.append(s)
                return 
            
            if left < n:
                dfs(left + 1, right, s + '(')
            
            if right < left:
                dfs(left, right + 1, s + ')')
                
        res = []
        dfs(0, 0, '')
        return res


n = 3
solution = Solution()
print(solution.generateParenthesis(n))