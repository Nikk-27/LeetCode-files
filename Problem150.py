#150 Evaluate Reverse Polish Notation

from typing import List
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 0:
            return 0
        
        operator = ["+", "-", "*", "/"]
        calc = list()
        for i in tokens:
            if i not in operator: 
                calc.append(int(i))
            else:
                if i == "+":
                    ans = calc[len(calc)-2] + calc[len(calc)-1]
                    calc.pop(len(calc)-1)
                    calc.pop(len(calc)-1)
                    calc.append(ans)
                elif i == "-":
                    ans = calc[len(calc)-2] - calc[len(calc)-1]
                    calc.pop(len(calc)-1)
                    calc.pop(len(calc)-1)
                    calc.append(ans)
                elif i == "*":
                    ans = calc[len(calc)-2] * calc[len(calc)-1]
                    calc.pop(len(calc)-1)
                    calc.pop(len(calc)-1)
                    calc.append(ans)
                elif i == "/":
                    if calc[len(calc)-1] != 0:
                        ans = calc[len(calc)-2] / calc[len(calc)-1]
                        calc.pop(len(calc)-1)
                        calc.pop(len(calc)-1)
                        calc.append(math.trunc(ans))
                    else:
                        return 0
                else:
                    return 0

        return calc[0]


# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution()
print(solution.evalRPN(tokens))