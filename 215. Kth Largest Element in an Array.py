class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        heapify(temp)
        for num in nums:
            heappush(temp, num)
            if len(temp)> k:
                ele = heappop(temp)
        return heappop(temp)