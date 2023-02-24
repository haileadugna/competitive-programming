class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for token in tokens:
            if token != "*" and token != "+" and token != '/' and token != "-":
                stack.append(token)
                
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if token == "*":
                    res = (num2 * num1)
                    stack.append(res)
                elif token == "/":
                    if num2 % num1 != 0:
                        if num2 / num1 > 0:
                            res = (num2 // num1)
                        else:
                            res = (num2 // num1) + 1
                    else:
                        res = (num2 / num1)
                    stack.append(res)
                elif token == "-":
                    res = (num2 - num1)
                    stack.append(res)
                else:
                    res = (num2 + num1)
                    stack.append(res)
    
        return int(stack[-1])
                