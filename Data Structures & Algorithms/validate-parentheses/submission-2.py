class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[', '}':'{'}
        stk = []

        for char in s:
            if char not in dic:
                stk.append(char)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != dic[char]:
                        return False
                    
        return not stk
