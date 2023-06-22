class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        pos = -prices[0]
        res =  0
        
        for i in range(1, n):
            pos = max(pos, res - prices[i])
            res = max(res, pos + prices[i] - fee)
            # print(pos, res)
            
        return res