class Solution:
    def minSteps(self, n: int) -> int:
        factorization = defaultdict(int)
        d = 2

        while d * d <= n:
            while n % d == 0:
                factorization[d] += 1
                n //= d
            d += 1
        if n > 1:
            factorization[n] += 1
        
        res = 0
        for key in list(factorization.keys()):
            res += factorization[key] * key
        return res