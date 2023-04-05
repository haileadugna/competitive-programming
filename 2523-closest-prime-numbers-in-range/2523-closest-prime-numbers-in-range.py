class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        n = right
        res = []
        is_prime: list[bool] = [True for _ in range(n+ 1)]
        is_prime[0] = is_prime[1] = False

        i = 2

        while i * i <= n:
            if is_prime[i]:
                j = i * i
                while j <= n:
                    is_prime[j] = False
                    j += i
            i += 1

        for i in range(left, len(is_prime) ):
            if is_prime[i] == True:
                res.append(i)
            
        if len(res) < 2:
            return [-1, -1]
        prev = res[1] - res[0]
        let = 1
        for i in range(2,len(res)):
            if res[i]- res[i -1] < prev:
                prev = res[i]- res[i -1]
                let = i

        return [res[let -1], res[let]]

#         for num in range(left, right+1):
#             factors = []
#             i = 2
#             while i * i <= num:
#                 if len(factors) > 1:
#                     break
#                 if num % i:
#                     i += 1
#                 else:
#                     num //= i
#                     factors.append(i)
#             if num > 1:
#                 factors.append(num)
#             if len(factors) == 1:
#                 res.append(factors[0])

#         if len(res) < 2:
#             return [-1, -1]
#         prev = res[1] - res[0]
#         let = 1
#         for i in range(2,len(res)):
#             if res[i]- res[i -1] < prev:
#                 prev = res[i]- res[i -1]
#                 let = i

#         return [res[let -1], res[let]]