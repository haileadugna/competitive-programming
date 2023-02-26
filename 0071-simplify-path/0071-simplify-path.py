class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        n = len(path)
        i = 0
        
        while i < n:
            if path[i] == "." and (i + 1 == len(path) or path[i + 1] == "/") and stack and stack[-1] == "/":
                i += 1
            # elif 
            elif i < n-2 and path[i] == "." and path[i + 1] == "." and path[i + 2] == ".":
                stack.append("...")
                i += 3
            elif i < n-2 and path[i] == "." and path[i + 1] == "." and path[i + 2] == "/" and stack[-1] == "/":
                if stack:
                    stack.pop()
                    while stack and stack[-1] != "/":
                        stack.pop()
                
                i += 2
            elif i < n-1 and path[i] == "." and path[i + 1] == "." and i + 1 == n - 1 and stack[-1] == "/":
                if stack:
                    stack.pop()
                    while stack and stack[-1] != "/":
                        stack.pop()
                i += 2
            else:
                if stack and stack[-1] == "/" and path[i] == "/":
                    i += 1
                else:
                    stack.append(path[i])
                    i += 1
        if len(stack) > 1 and stack[-1] =="/":
            stack.pop()
        if len(stack) == 0:
            return "/"
        return "".join(stack)