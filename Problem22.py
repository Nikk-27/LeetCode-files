#22 Generate Parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):   #lowest TC of all, TC = O(4^n / sqrt(n))
            if len(s) == n * 2: 
                print(s)
                res.append(s)
                return 
            print("s ", s)
            if left < n:
                print("$$$$")
                print(left, right)
                dfs(left + 1, right, s + '(')
            
            if right < left:
                print("####")
                print(left, right)
                dfs(left, right + 1, s + ')')
                
        res = []
        print("111")
        dfs(0, 0, '')
        return res
    
    '''
    stack = []
    res = []

    def backtrack(openN, closeN):
        if openN == closedN == n:
            res.append("".join(stack))

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        
        if openN > closedN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

        backtrack(0, 0)
        return res
        
    '''
    
    '''
        brackets = { "(" : ")"}
        stack = list()
        count = 0
        s = ""
        b = []

        for i in range(n):
            s += str(next(iter(brackets))) # this adds the first key to the string
            print("s ", s) 
            count += 1

            if count == n:
                while count > 0:
                    s += str(next(iter(brackets.values()))) # this adds the first value to the string
                    print("s -> ", s)
                    count -= 1
        stack.append(s)
        return stack
    
    # output : ['((()))']
    
    '''

n = 3
solution = Solution()
print(solution.generateParenthesis(n))