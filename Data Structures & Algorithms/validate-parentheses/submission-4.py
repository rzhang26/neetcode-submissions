class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {'}':'{', ']':'[', ')':'('}

        for char in s:
            if char in close_to_open:
                if(len(stack) == 0):
                    return False
                if(stack[-1] == close_to_open[char]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        if(len(stack) == 0): return True
        else: return False
