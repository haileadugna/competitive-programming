class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        pile = [-i for i in piles]
        heapq.heapify(pile)
        
        while k > 0:
            num = heapq.heappop(pile)
            temp = (num) * -1//2
            heapq.heappush(pile, (num + temp))
            k -= 1
            
        return abs(sum(pile))