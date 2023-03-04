class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        l = 1
        r = max(nums)
        while l <= r:
            mid = (r+l)//2
            summ = sum(math.ceil(i/mid) for i in nums)
            if summ > threshold:
                l = mid + 1
            else:
                r = mid -1
        return l 