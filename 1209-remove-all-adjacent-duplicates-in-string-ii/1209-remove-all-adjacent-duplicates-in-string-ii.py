class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for w in s:
            if not stack or stack[-1][0] != w:
                stack.append((w, 1))
            else:
                char, count = stack.pop()
                if count < k - 1:
                    stack.append((char, count + 1))
        
        result = []
        for char, count in stack:
            result.extend([char] * count)
        
        return "".join(result)
