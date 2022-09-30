class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return n
        temp = 0
        for i in range(1, n+1):
            temp += i
            if temp >= n:
                ans = i
                break
        
        if temp == n:
            ans = ans
        else:
            ans = ans - 1
        return ans