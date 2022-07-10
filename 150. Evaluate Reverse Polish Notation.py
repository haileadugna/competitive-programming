class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ele in tokens:
            if ele == "+":
                stack.append(stack.pop() + stack.pop())
            elif ele == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif ele == "*":
                stack.append(stack.pop() * stack.pop())
            elif ele == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(ele))
        return stack[0]