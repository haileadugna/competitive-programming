class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        stackval = []
        res = 0
        
        for par in s:
            if par == "(":
                stack.append(par)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    temp = 0
                    while stack[-1] != "(":
                        temp += stack.pop()
                    stack.pop()
                    stack.append(temp*2)

        return sum(stack)