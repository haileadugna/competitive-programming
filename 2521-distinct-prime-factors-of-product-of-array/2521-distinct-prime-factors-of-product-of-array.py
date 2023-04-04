class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        # num = reduce((lambda x, y: x * y), nums)
        factors = set()
        for num in nums:
            
            i = 2
            while i * i <= num:
                if num % i:
                    i += 1
                else:
                    num //= i
                    factors.add(i)
            if num > 1:
                factors.add(num)
        return len(factors)