class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        n = len(arr)
        cnt = n//4
        
        
        for i in range(n-cnt):
            
            if arr[i] == arr[i+cnt]:
                return arr[i]