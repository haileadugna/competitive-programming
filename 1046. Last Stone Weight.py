
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            high = heapq.heappop(stones)
            low = heapq.heappop(stones)
            if high < low:
                heapq.heappush(stones, high - low)
        stones.append(0)
        return abs(stones[0])