class Solution:
    def climbStairs(self, n: int) -> int:
        num1 = 1 
        num2 = 2
        if n==1:
            return num1
        elif n==2:
            return num2
        else:
            for i in range(2, n):
                sum = num1 + num2 
                num1=num2
                num2=sum
            return sum