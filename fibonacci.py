class Solution:
    def fib(self, n: int) -> int:
        num1 = 0 
        num2 = 1
        if n==0:
            return num1
        elif n==1:
            return num2
        else:
            for i in range(2, n+1):
                sum = num1 + num2 
                num1=num2
                num2=sum
            return sum