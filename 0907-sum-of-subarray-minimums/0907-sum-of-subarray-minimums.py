class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        n = len(arr)
        res = 0
        
        for i in range(n + 1):
            
            while stack and (i == n or arr[stack[-1]] > arr[i]):
                temp = stack.pop()
                if stack:
                    pre = stack[-1]
                else:
                    pre = -1
                    
                res += ((i - temp) * (temp - pre)) * arr[temp]
            stack.append(i)
                
                
        return res % (10**9 + 7)