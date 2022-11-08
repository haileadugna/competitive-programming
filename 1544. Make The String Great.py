class Solution:
    def makeGood(self, s: str) -> str:
        temp = {}
        for j in range(65, 91):
            temp[chr(j)] = chr(j + 32)
        stack = []
        for i in range(len(s)):
            if stack != []  :
                if s[i] in temp.keys() and stack[-1] == temp[s[i]]:
                    
                    stack.pop()
                elif stack[-1] in temp.keys() and temp[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return "".join(stack)
    