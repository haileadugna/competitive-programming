class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        left = 0
        right = int(c**.5)

        while left <= right:
            check = left **2 + right**2
            if check == c:
                return True
            elif check > c:
                right -= 1
            else:
                left += 1
        return False