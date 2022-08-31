class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int: 
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high)//2
            summ = 0
            ans = 1
            for weight in weights:
                summ += weight
                if summ  > mid:
                    ans += 1
                    summ = weight
            if ans <= days:
                high = mid
            else:
                low = mid +1
        return high