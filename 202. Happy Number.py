class Solution:
    def isHappy(self, n: int) -> bool:
        
        ans  = []
        
        while n not in ans:
            ans.append(n)
            n = self.sumof(n)
            if n == 1:
                return True
        return False  
    
    def sumof(self, n):
        temp = 0
        while n:
            digit = n % 10
            temp += digit**2
            n = n//10
            
        return temp
        