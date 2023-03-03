class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)
        while low <= high:
            mid = ( low + high)//2
            temp =0
            for i in range(len(piles)):
                temp += math.ceil(piles[i] / mid)
            if h < temp :
                low = mid +1
            else:
                high = mid -1

        return low