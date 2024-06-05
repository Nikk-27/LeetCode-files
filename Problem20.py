#20 Valid Parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {")":"(", "]":"[", "}":"{"}

        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False

        stack = list()
        for i in s:
            if i in bracket:
                if stack and stack[-1] == bracket[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
           
        if len(stack) == 0:
            return True

s = "()[]{}"
solution = Solution()
print(solution.isValid(s))