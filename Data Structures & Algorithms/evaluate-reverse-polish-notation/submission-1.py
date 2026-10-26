from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t in '+-*/':
                b, a = stk.pop(), stk.pop()
                if t == '+':
                    stk.append(a+b)
                elif t == '-':
                    stk.append(a-b)
                elif t == '*':
                    stk.append(a * b)
                else:
                    div = a / b
                    if div < 0:
                        stk.append(ceil(div))
                    else:
                        stk.append(floor(div))

            else:
                stk.append(int(t))

        return stk[0]