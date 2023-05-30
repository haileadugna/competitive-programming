class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        satisfaction.sort()
        
        if satisfaction[-1] < 0:
            return 0
        
        n = len(satisfaction)
        
        res = 0
        for i in range(n-1):
            temp = 0
            for j in range(n - i):
                temp += (satisfaction[j + i] * (j + 1))
                
            res = max(temp, res)
                            
        return res