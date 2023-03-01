class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        if len(arr) == 1:
            return 1
        
        stack = []
        res = 0
        ans = 0
        
        for i in range(1, len(arr)):
            
            if arr[i] > arr[i - 1]:
                val = "<"
                
            if arr[i] < arr[i - 1]:
                val = ">"
            if arr[i] == arr[i -1]:
                val = "=="
                
            if stack and stack[-1] == val or val == "==" :
                while stack:
                    stack.pop()
            if val == "=="   :
                ans = 1
            else:
                stack.append(val)
            res = max(res, len(stack) + 1, ans)
        return res