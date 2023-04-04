class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        a = max(nums)
        b = min(nums)
        
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        return gcd(a, b)
#         while b != 0:
#             a, b = b, a%b
            
#         return a
        