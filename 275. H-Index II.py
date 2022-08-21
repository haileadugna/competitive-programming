class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        left = 0
        right = len(citations) -1
        while left < right:
            mid = (left+right)//2
            if citations[mid] >= len(citations) - mid:
                right = mid 
            else:
                left = mid+1
        if citations[left] == 0:
            return 0
        return len(citations) - left