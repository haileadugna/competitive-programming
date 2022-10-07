class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<=r:
            m = ( l + r)//2
            temp =0
            for i in range(len(piles)):
                temp += math.ceil(piles[i]/m)
            if h < temp :
                l = m +1
            else:
                r = m -1
            temp = 0
        return l

