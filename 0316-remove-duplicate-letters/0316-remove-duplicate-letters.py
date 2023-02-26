class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        list1 = Counter(list(s))
        
        for ele in s:
            
            list1[ele] -= 1
            if ele in stack:
                continue
                
            while stack and list1[stack[-1]] and stack[-1] > ele:
                stack.pop()
                
            if ele not in stack:
                stack.append(ele)
                
        return "".join(stack)
            