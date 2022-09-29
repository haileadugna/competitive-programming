class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        start, end = 0, len(nums) -1
        while start <= end:
            mid = (start + end)//2
            tmp = 0
            for i in nums:
                if i >= mid + 1:
                    tmp += 1
            if tmp == mid + 1:
                return tmp
            elif tmp > mid +1:
                start = mid + 1
            else:
                end = mid -1
            tmp = 0
        return -1