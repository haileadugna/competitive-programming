class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        n=len(piles)
        summ=0
        for i in range(n-n//3):
            if i%2!=0:
                summ+=piles[i]
        return summ