class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i- 1] > prices[i]:
                if prices[i] < temp:
                    temp = prices[i]
            else:
                if prices[i] - temp > ans:
                    ans = prices[i] - temp
        return ans